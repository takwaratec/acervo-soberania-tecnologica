import json, os, subprocess, sys, tempfile, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import verifica_ponteiro_runtime as v


def git(d, *a):
    return subprocess.run(["git", "-C", d, *a], capture_output=True, text=True)


class Base(unittest.TestCase):
    def setUp(self):
        self.repo = tempfile.mkdtemp()
        git(self.repo, "init", "-q")
        git(self.repo, "config", "user.email", "t@t")
        git(self.repo, "config", "user.name", "t")
        self.rel = "ops/regency/ACTIVE_CONTRACTS_R4.json"
        os.makedirs(os.path.join(self.repo, os.path.dirname(self.rel)))
        self.ledger = {"CONTRACTS": [{"id": "A-1", "contrato_documento": "PRESENTE",
                                      "contract_path": "ops/contracts/A-1.json"}],
                       "COUNTS": {"TOTAL": 1}}
        self.escreve_ledger(self.ledger)
        os.makedirs(os.path.join(self.repo, "ops/contracts"))
        open(os.path.join(self.repo, "ops/contracts/A-1.json"), "w").write("{}\n")
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-qm", "c1")
        self.c_contrato = git(self.repo, "rev-parse", "HEAD").stdout.strip()
        self.ledger["CONTRACTS"][0]["contract_commit"] = self.c_contrato
        self.escreve_ledger(self.ledger)
        git(self.repo, "commit", "-qam", "c2")
        self.gov = git(self.repo, "rev-parse", "HEAD").stdout.strip()
        # cópia de runtime FORA do repo, que é o formato recomendado
        self.rt = tempfile.mkdtemp()
        self.copia = os.path.join(self.rt, "ledger.json")
        self.copia_bytes()
        self.pointer = os.path.join(self.rt, "pointer.json")

    def escreve_ledger(self, obj):
        with open(os.path.join(self.repo, self.rel), "w") as fh:
            json.dump(obj, fh, ensure_ascii=False, indent=1)
            fh.write("\n")

    def copia_bytes(self):
        open(self.copia, "wb").write(open(os.path.join(self.repo, self.rel), "rb").read())

    def ponteiro(self, **kw):
        import hashlib
        p = {"ledger_registry": self.copia,
             "ledger_registry_sha256": hashlib.sha256(open(self.copia, "rb").read()).hexdigest(),
             "governance_commit": self.gov,
             "ledger_origem_path": self.rel}
        p.update(kw)
        with open(self.pointer, "w") as fh:
            json.dump(p, fh)
        return p

    def roda(self, *args):
        r = v.main(["--ponteiro", self.pointer, "--repo", self.repo, *args])
        return r


class TestPonteiroRuntime(Base):
    def test_copia_selada_fora_do_repo_passa(self):
        self.ponteiro()
        self.assertEqual(self.roda(), 0)

    def test_hash_divergente_falha(self):
        self.ponteiro(ledger_registry_sha256="0" * 64)
        self.assertEqual(self.roda(), 1)

    def test_ledger_dentro_de_arvore_de_trabalho_falha(self):
        """O caso real de 27/11: ponteiro apontando para worktree de frente."""
        p = self.ponteiro()
        p["ledger_registry"] = os.path.join(self.repo, self.rel)
        import hashlib
        p["ledger_registry_sha256"] = hashlib.sha256(
            open(p["ledger_registry"], "rb").read()).hexdigest()
        with open(self.pointer, "w") as fh:
            json.dump(p, fh)
        self.assertEqual(self.roda(), 1)

    def test_copia_que_nao_e_o_publicado_falha(self):
        self.ponteiro()
        with open(self.copia, "a") as fh:
            fh.write(" ")
        p = json.load(open(self.pointer))
        import hashlib
        p["ledger_registry_sha256"] = hashlib.sha256(open(self.copia, "rb").read()).hexdigest()
        json.dump(p, open(self.pointer, "w"))
        self.assertEqual(self.roda(), 1)

    def test_entrada_ausente_com_caminho_falha(self):
        """Documento AUSENTE não pode carregar contract_path: caminho sem arquivo."""
        self.ledger["CONTRACTS"][0] = {"id": "A-1", "contrato_documento": "AUSENTE",
                                       "contract_path": "ops/contracts/A-1.json"}
        self.escreve_ledger(self.ledger)
        git(self.repo, "commit", "-qam", "c2")
        self.gov = git(self.repo, "rev-parse", "HEAD").stdout.strip()
        self.copia_bytes()
        self.ponteiro()
        self.assertEqual(self.roda(), 1)

    def test_counts_que_nao_fecha_falha(self):
        self.ledger["COUNTS"]["TOTAL"] = 7
        self.escreve_ledger(self.ledger)
        git(self.repo, "commit", "-qam", "c2")
        self.gov = git(self.repo, "rev-parse", "HEAD").stdout.strip()
        self.copia_bytes()
        self.ponteiro()
        self.assertEqual(self.roda(), 1)

    def test_contrato_sem_arquivo_no_commit_falha(self):
        self.ledger["CONTRACTS"][0]["contract_path"] = "ops/contracts/NAO-EXISTE.json"
        self.ledger["CONTRACTS"][0]["contract_commit"] = self.gov
        self.escreve_ledger(self.ledger)
        git(self.repo, "commit", "-qam", "c2")
        self.gov = git(self.repo, "rev-parse", "HEAD").stdout.strip()
        self.copia_bytes()
        self.ponteiro()
        self.assertEqual(self.roda(), 1)

    def test_commit_declarado_que_nao_abre_falha(self):
        self.ponteiro(governance_commit="0" * 40)
        self.assertEqual(self.roda(), 1)

    def test_sem_proveniencia_nao_e_pass(self):
        """Sem o repo não se prova proveniência: PARCIAL, nunca PASS."""
        self.ponteiro()
        self.assertEqual(v.main(["--ponteiro", self.pointer, "--sem-proveniencia"]), 2)

    def test_copia_fora_do_repo_sem_origem_e_nao_medido(self):
        p = self.ponteiro()
        p.pop("ledger_origem_path")
        json.dump(p, open(self.pointer, "w"))
        self.assertEqual(self.roda(), 2)

    def test_ponteiro_inexistente_e_nao_medido(self):
        self.ponteiro()
        self.assertEqual(v.main(["--ponteiro", "/nao/existe.json", "--repo", self.repo]), 2)


if __name__ == "__main__":
    unittest.main()
