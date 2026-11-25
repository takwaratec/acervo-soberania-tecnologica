import json
import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts", "pacote_auditoria"))
import gerar as g

SCRIPT = os.path.join(os.path.dirname(__file__), "..", "scripts", "pacote_auditoria", "gerar.py")


def git(cwd, *a):
    r = subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True)
    if r.returncode != 0:
        raise AssertionError(f"git {' '.join(a)}: {r.stderr}")
    return r.stdout


def escreve(path, texto):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(texto)


CFG_BASE = {
    "frente": "teste",
    "pasta": "docs/analyses/teste",
    "manifest_id": "TESTE-AUDITORIA-R1",
    "autoridade": "teste",
    "alvo_branch": "main",
    "aviso_de_leitura": "a entrada e este arquivo",
    "o_que_esta_auditoria_e": "conteudo",
    "pedido_do_soberano": "teste",
    "objeto": {"artigo": "docs/analyses/teste/a.md"},
    "estado_declarado": {"homologacao_automatica": False},
    "pergunta": "as afirmacoes sao sustentadas?",
    "parte_1_perguntas": [{"id": "Q1", "pergunta": "?", "arquivo": "docs/analyses/teste/a.md"}],
    "criterios": {"PASS": "x", "FAIL": "y"},
    "severidade": {"ALTO": "x"},
    "formato_resposta": {"campos_obrigatorios": ["VEREDITO"]},
    "limites": ["l"],
    "nao_homologa": ["h"],
    "como_reproduzir": ["1. Leia docs/analyses/teste/a.md de ponta a ponta."],
    "nao_medido_declarado": {"afirmacoes_nao_medidas": 10},
    "como_ler": "a entrada e este arquivo",
    "fontes": [],
}


class TestGerador(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()
        git(self.d, "init", "-q", "-b", "main")
        git(self.d, "config", "user.email", "t@t")
        git(self.d, "config", "user.name", "t")
        os.makedirs(os.path.join(self.d, "docs/analyses/teste"), exist_ok=True)
        escreve(os.path.join(self.d, "docs/analyses/teste/a.md"), "# artigo\n")
        git(self.d, "add", "-A")
        git(self.d, "commit", "-qm", "base")
        self.cfg = json.loads(json.dumps(CFG_BASE))
        self.cfg_path = os.path.join(self.d, "cfg.json")

    def grava_cfg(self, cfg):
        with open(self.cfg_path, "w") as f:
            json.dump(cfg, f)

    def roda(self, *extra, cfg=None):
        self.grava_cfg(cfg or self.cfg)
        return subprocess.run(
            [sys.executable, SCRIPT, "--repo", self.d, "--cfg", self.cfg_path,
             "--frente", "teste", "--alvo", "HEAD", *extra],
            capture_output=True, text=True)

    # --- R19-A: metodo impossivel -------------------------------------------
    def test_fonte_fora_do_rastreio_sem_caminho_privado_recusa(self):
        self.cfg["fontes"] = [{"path": "docs/analyses/teste/x.pdf", "papel": "pdf",
                               "no_repositorio": False}]
        r = self.roda()
        self.assertEqual(r.returncode, 2, r.stdout)
        self.assertIn("R19-A", r.stdout)

    def test_caminho_privado_declarado_e_inexistente_recusa(self):
        self.cfg["fontes"] = [{"path": "docs/analyses/teste/x.pdf", "no_repositorio": False,
                               "caminho_privado": "_privado/nao_existe.pdf"}]
        r = self.roda()
        self.assertEqual(r.returncode, 2, r.stdout)
        self.assertIn("R19-A", r.stdout)

    def test_caminho_privado_existente_prova_o_hash_do_disco(self):
        os.makedirs(os.path.join(self.d, "_privado"), exist_ok=True)
        escreve(os.path.join(self.d, "_privado/x.pdf"), "%PDF-fake")
        self.cfg["fontes"] = [{"path": "docs/analyses/teste/x.pdf", "no_repositorio": False,
                               "caminho_privado": "_privado/x.pdf"}]
        r = self.roda("--check")
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("registro_custodia_privada", r.stdout)

    # --- R19-B: ponteiro fantasma -------------------------------------------
    def test_fonte_no_repositorio_que_nao_existe_recusa(self):
        self.cfg["fontes"] = [{"path": "docs/analyses/teste/fantasma.md"}]
        r = self.roda()
        self.assertEqual(r.returncode, 2, r.stdout)
        self.assertIn("R19-B", r.stdout)

    def test_referencia_resolvivel_inexistente_recusa(self):
        self.cfg["referencias_resolviveis"] = ["ops/command-center/auditoria-atual/X.json"]
        r = self.roda()
        self.assertEqual(r.returncode, 2, r.stdout)
        self.assertIn("R19-B", r.stdout)

    # --- R19-D: caminho vazio na instrucao ----------------------------------
    def test_instrucao_aponta_para_diretorio_esvaziado_recusa(self):
        self.cfg["como_reproduzir"] = ["6. Compare cada ficha com docs/analyses/teste/fontes/pdf/."]
        r = self.roda()
        self.assertEqual(r.returncode, 2, r.stdout)
        self.assertIn("R19-D", r.stdout)

    def test_instrucao_aponta_para_diretorio_com_arquivo_passa(self):
        os.makedirs(os.path.join(self.d, "docs/analyses/teste/fontes/md"), exist_ok=True)
        escreve(os.path.join(self.d, "docs/analyses/teste/fontes/md/x.md"), "x")
        git(self.d, "add", "-A")
        git(self.d, "commit", "-qm", "fonte")
        self.cfg["como_reproduzir"] = ["4. Abra docs/analyses/teste/fontes/md/ e localize o trecho."]
        r = self.roda("--check")
        self.assertEqual(r.returncode, 0, r.stdout)

    # --- R19-C: par + contagem por caminho ----------------------------------
    def test_gera_o_par_e_a_contagem_conta_por_caminho(self):
        r = self.roda()
        self.assertEqual(r.returncode, 0, r.stdout)
        pasta = os.path.join(self.d, "docs/analyses/teste")
        ms = [f for f in os.listdir(pasta) if "MANIFEST_R1" in f]
        rs = [f for f in os.listdir(pasta) if "HASHES_RESPONSE_R1" in f]
        self.assertEqual(len(ms), 1)
        self.assertEqual(len(rs), 1, "R19-C: manifesto e resposta tem de sair juntos")
        with open(os.path.join(pasta, ms[0]), encoding="utf-8") as fh:
            doc = json.load(fh)
        self.assertEqual(doc["alvo_commit"], git(self.d, "rev-parse", "HEAD").strip())
        self.assertIn("metodos_de_hash", doc)

    def test_contagem_de_selos_por_caminho_nao_por_mensagem(self):
        """O erro real: contava por mensagem de commit e via 19 de 28. Caminho ve todos."""
        pasta = "docs/analyses/teste"
        os.makedirs(os.path.join(self.d, pasta), exist_ok=True)
        for suf in ("aaaa1111", "bbbb2222"):
            for pref in ("MANIFEST_R1", "HASHES_RESPONSE_R1"):
                p = os.path.join(self.d, pasta, f"AUDITORIA_SOL_TESTE_{pref}_{suf}.json")
                escreve(p, "{}")
            git(self.d, "add", "-A")
            git(self.d, "commit", "-qm", "commit sem o alvo na mensagem")
        s = g.contar_selos(self.d, pasta)
        self.assertEqual(s["manifestos_no_historico"], 2)
        self.assertEqual(s["respostas_no_historico"], 2)
        self.assertEqual(s["so_manifesto"], [])
        self.assertEqual(s["so_resposta"], [])

    def test_selo_orfao_e_revelado(self):
        pasta = "docs/analyses/teste"
        os.makedirs(os.path.join(self.d, pasta), exist_ok=True)
        escreve(os.path.join(self.d, pasta, "AUDITORIA_SOL_TESTE_MANIFEST_R1_cccc3333.json"), "{}")
        git(self.d, "add", "-A")
        git(self.d, "commit", "-qm", "orfao")
        s = g.contar_selos(self.d, pasta)
        self.assertEqual(s["so_manifesto"], ["cccc3333"])

    # --- A2: nao_medido declarado e obrigatorio -----------------------------
    def test_nao_medido_declarado_e_obrigatorio(self):
        del self.cfg["nao_medido_declarado"]
        r = self.roda()
        self.assertNotEqual(r.returncode, 0, "sem declarar o que nao foi medido o pacote nao pode sair")


    def test_custodia_fora_do_repo_exige_raiz_privada(self):
        """Em worktree o _privado/ nao existe: sem --privado o gerador recusa, em vez de mentir."""
        self.cfg["fontes"] = [{"path": "docs/analyses/teste/x.pdf", "no_repositorio": False,
                               "caminho_privado": "_privado/x.pdf"}]
        r = self.roda()
        self.assertEqual(r.returncode, 2, r.stdout)
        self.assertIn("R19-A", r.stdout)
        # criando em outra raiz e apontando --privado, passa
        outra = tempfile.mkdtemp()
        escreve(os.path.join(outra, "_privado", "x.pdf"), "%PDF-fake")
        self.grava_cfg(self.cfg)
        r2 = subprocess.run([sys.executable, SCRIPT, "--repo", self.d, "--cfg", self.cfg_path,
                             "--frente", "teste", "--alvo", "HEAD", "--check", "--privado", outra],
                            capture_output=True, text=True)
        self.assertEqual(r2.returncode, 0, r2.stdout)


if __name__ == "__main__":
    unittest.main()
