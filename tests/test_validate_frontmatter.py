#!/usr/bin/env python3
"""Testes do validador de front matter (scripts/validate_frontmatter.py).

Cobertura mínima exigida:
- arquivo válido sem avisos → exit 0;
- arquivo com estado legado sem `--strict` → exit 0 (aviso exibido);
- arquivo com estado legado com `--strict` → exit 1;
- arquivo com erro real sem `--strict` → exit 1;
- arquivo com erro real com `--strict` → exit 1.

Execução:
    python3 -m unittest discover -s tests -v
"""

import os
import shutil
import subprocess
import sys
import tempfile
import unittest

SCRIPT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts", "validate_frontmatter.py")

FICHA_VALIDA = """---
tipo_documental: ficha-cientifica
estado_documental: em-revisao-documental
responsavel_curadoria: Fabio Takwara
doi: 10.1000/xyz
---
# Ficha válida
"""

FICHA_ESTADO_LEGADO = """---
tipo_documental: ficha-cientifica
estado_documental: curado
responsavel_curadoria: Fabio Takwara
doi: 10.1000/xyz
---
# Ficha com estado legado
"""

FICHA_ERRO_REAL = """---
tipo_documental: ficha-cientifica
estado_documental: estado-inexistente
responsavel_curadoria: Fabio Takwara
doi: 10.1000/xyz
---
# Ficha com erro real
"""

FICHA_SEM_FRONTMATTER = """# Ficha sem front matter
"""


class ValidadorFrontMatterTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="fm-test-")
        self.docs = os.path.join(self.tmp, "docs")
        self.analyses = os.path.join(self.docs, "analyses")
        os.makedirs(self.analyses)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _escrever(self, nome, conteudo):
        caminho = os.path.join(self.analyses, nome)
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(conteudo)
        return caminho

    def _rodar(self, *args):
        return subprocess.run(
            [sys.executable, SCRIPT, "--docs", self.docs] + list(args),
            capture_output=True,
            text=True,
        )

    def test_arquivo_valido_sem_avisos_exit0(self):
        self._escrever("valida.md", FICHA_VALIDA)
        r = self._rodar()
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("Erros: 0 | Avisos: 0", r.stdout)

    def test_estado_legado_sem_strict_exit0(self):
        self._escrever("legado.md", FICHA_ESTADO_LEGADO)
        r = self._rodar()
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("Avisos: 1", r.stdout)
        self.assertIn("AVISO", r.stdout)

    def test_estado_legado_com_strict_exit1(self):
        self._escrever("legado.md", FICHA_ESTADO_LEGADO)
        r = self._rodar("--strict")
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("Erros: 1", r.stdout)

    def test_erro_real_sem_strict_exit1(self):
        self._escrever("erro.md", FICHA_ERRO_REAL)
        r = self._rodar()
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("Erros: 1", r.stdout)

    def test_erro_real_com_strict_exit1(self):
        self._escrever("erro.md", FICHA_ERRO_REAL)
        r = self._rodar("--strict")
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("Erros: 1", r.stdout)

    def test_sem_frontmatter_exit1_em_ambos_modos(self):
        self._escrever("semfm.md", FICHA_SEM_FRONTMATTER)
        r1 = self._rodar()
        self.assertEqual(r1.returncode, 1, r1.stdout)
        r2 = self._rodar("--strict")
        self.assertEqual(r2.returncode, 1, r2.stdout)


if __name__ == "__main__":
    unittest.main()
