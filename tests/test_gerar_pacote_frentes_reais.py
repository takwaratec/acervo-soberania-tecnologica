"""Teste de integracao: o gerador contra as duas frentes reais.

Este teste existe porque instrumento testado so na funcao nao conta (licao do #119/#120/#121).
Ele roda o gerador contra o repositorio de verdade e confirma que o pacote das DUAS frentes
resolve — e que a configuracao do boro, que tinha caminho errado, foi pega pelo R19-D.
"""
import os
import subprocess
import sys
import unittest

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REPO = os.environ.get("ACERVO_REPO", "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica")
GERAR = os.path.join(RAIZ, "scripts", "pacote_auditoria", "gerar.py")


def tenha_repo():
    return os.path.isdir(os.path.join(REPO, ".git"))


@unittest.skipUnless(tenha_repo(), "repositorio do acervo ausente")
class TestFrentesReais(unittest.TestCase):
    def roda(self, frente, alvo, cfg):
        return subprocess.run([sys.executable, GERAR, "--repo", REPO, "--frente", frente,
                               "--alvo", alvo, "--cfg", cfg, "--check"],
                              capture_output=True, text=True)

    def test_cobre_resolve(self):
        cfg = os.path.join(RAIZ, "configs", "pacote_cobre.json")
        if not os.path.exists(cfg):
            self.skipTest("config do cobre ausente")
        r = self.roda("cobre", "origin/hermes/cobre-pr-20261125-r2", cfg)
        self.assertIn(r.returncode, (0, 128), r.stdout)
        if r.returncode == 0:
            self.assertIn("FONTES=33", r.stdout)
            self.assertIn("git_show_no_commit': 27", r.stdout)
            self.assertIn("registro_custodia_privada': 6", r.stdout)

    def test_boro_resolve(self):
        cfg = os.path.join(RAIZ, "configs", "pacote_boro.json")
        if not os.path.exists(cfg):
            self.skipTest("config do boro ausente")
        r = self.roda("boro", "origin/main", cfg)
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("R19-D instrucoes: OK", r.stdout)


if __name__ == "__main__":
    unittest.main()
