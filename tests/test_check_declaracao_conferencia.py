import os, subprocess, sys, tempfile, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import check_declaracao_conferencia as g

class TestDeclaracao(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()
    def escreve(self, nome, txt):
        p = os.path.join(self.d, nome)
        open(p, "w", encoding="utf-8").write(txt)
        return p

    def test_declaracao_sem_registro_falha(self):
        self.escreve("artigo-x.md", "Toda afirmação numérica foi conferida contra a fonte primária.\n")
        self.assertEqual(len(g.declaracoes(open(self.escreve("a.md","x"),encoding="utf-8").read())), 0)
        probs = subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__),"..","scripts","check_declaracao_conferencia.py"), self.d, "--json"], capture_output=True, text=True)
        self.assertEqual(probs.returncode, 1)
        self.assertIn("artigo-x.md", probs.stdout)

    def test_declaracao_com_registro_passa(self):
        self.escreve("artigo-y.md", "Toda afirmação numérica foi conferida contra a fonte primária.\n")
        self.escreve("REGISTRO_CONFERENCIA_artigo-y.json", "[]")
        r = subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__),"..","scripts","check_declaracao_conferencia.py"), self.d], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_relato_medido_passa(self):
        self.escreve("artigo-z.md", "De 377 afirmações, 120 foram conferidas; as demais ficaram como não conferidas.\n")
        r = subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__),"..","scripts","check_declaracao_conferencia.py"), self.d], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_negacao_nao_conta_como_declaracao(self):
        self.escreve("n.md", "Nem todas as fontes foram lidas integralmente.\n")
        r = subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__),"..","scripts","check_declaracao_conferencia.py"), self.d], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_proveniencia_de_arquivo_nao_e_declaracao_de_conferencia(self):
        self.escreve("p.md", "- Proveniência: PDF baixado do portal em 2026-07-31 e conferido integralmente (6 páginas; hash SHA-256).\n")
        r = subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__),"..","scripts","check_declaracao_conferencia.py"), self.d], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_registro_de_outro_documento_nao_serve(self):
        self.escreve("a.md", "Toda afirmação numérica foi conferida contra a fonte primária.\n")
        self.escreve("REGISTRO_CONFERENCIA_zzz.json", "[]")
        r = subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__),"..","scripts","check_declaracao_conferencia.py"), self.d], capture_output=True, text=True)
        self.assertEqual(r.returncode, 1, r.stdout)

if __name__ == "__main__":
    unittest.main()
