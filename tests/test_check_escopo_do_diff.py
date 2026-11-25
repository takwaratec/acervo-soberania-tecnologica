import os, subprocess, sys, tempfile, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import check_escopo_do_diff as g

SCRIPT = os.path.join(os.path.dirname(__file__), "..", "scripts", "check_escopo_do_diff.py")


def git(cwd, *a):
    return subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True, check=True).stdout


class TestEscopo(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()
        git(self.d, "init", "-q", "-b", "main")
        git(self.d, "config", "user.email", "t@t")
        git(self.d, "config", "user.name", "t")
        for p in ("docs/analyses/x/a.md", "docs/analyses/y/b.md"):
            os.makedirs(os.path.join(self.d, os.path.dirname(p)), exist_ok=True)
            open(os.path.join(self.d, p), "w").write("base\n")
        git(self.d, "add", "-A")
        git(self.d, "commit", "-qm", "base")
        git(self.d, "branch", "base-ref")

    def roda(self, *a):
        return subprocess.run([sys.executable, SCRIPT, "--base", "base-ref", *a],
                              cwd=self.d, capture_output=True, text=True)

    def test_diff_limpo_passa(self):
        open(os.path.join(self.d, "docs/analyses/x/a.md"), "w").write("novo\n")
        git(self.d, "commit", "-aqm", "x")
        r = self.roda("--permitir", "docs/analyses/x")
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_arquivo_fora_da_gaveta_falha(self):
        open(os.path.join(self.d, "docs/analyses/y/b.md"), "w").write("mexido\n")
        git(self.d, "commit", "-aqm", "y")
        r = self.roda("--permitir", "docs/analyses/x")
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("docs/analyses/y/b.md", r.stdout)

    def test_delecao_fora_da_gaveta_aparece_como_delecao(self):
        os.remove(os.path.join(self.d, "docs/analyses/y/b.md"))
        git(self.d, "commit", "-aqm", "del")
        r = self.roda("--permitir", "docs/analyses/x")
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("DELECAO docs/analyses/y/b.md", r.stdout)

    def test_sem_permitir_recusa(self):
        r = self.roda()
        self.assertEqual(r.returncode, 2, r.stdout)

    def test_prefixo_nao_cobre_arquivo_de_nome_parecido(self):
        os.makedirs(os.path.join(self.d, "docs/analyses/xy"), exist_ok=True)
        open(os.path.join(self.d, "docs/analyses/xy/c.md"), "w").write("x\n")
        git(self.d, "add", "-A")
        git(self.d, "commit", "-qm", "xy")
        r = self.roda("--permitir", "docs/analyses/x")
        self.assertEqual(r.returncode, 1, r.stdout)


if __name__ == "__main__":
    unittest.main()
