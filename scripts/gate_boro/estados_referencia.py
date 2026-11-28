#!/usr/bin/env python3
"""Mede os quatro estados de custodia por referencia citada no artigo.

Estados, que NAO se convertem um no outro:

  IDENTIFICADA            a obra esta nomeada na bibliografia (autor, titulo, ano)
  ARQUIVO_CUSTODIADO      existe arquivo na camada privada, com sha256
  TEXTO_UTILIZAVEL        o arquivo tem texto conferivel (>= LIMITE chars uteis por pagina)
  LEITURA_INTEGRAL        existe artefato de leitura integral arquivado

Uso:
    python3 scripts/gate_boro/estados_referencia.py            # tabela markdown
    python3 scripts/gate_boro/estados_referencia.py --contagem # so as contagens

Requer PyMuPDF. No Mac do curador: /Users/fabiotakwara/.venvs/pdf/bin/python

Licao que este script carrega: contar so [A-Za-z] fazia o documento chines do MEE (8 paginas)
aparecer com 370 caracteres uteis, como se fosse ilegivel. E falso. Use \\w com Unicode.
"""
import hashlib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fitz  # noqa: E402
import rodar  # noqa: E402

BASE = Path(rodar.BORO)
ARTIGO = Path(__file__).resolve().parents[2] / "docs/analyses/boro/artigo-o-boro-explicado-do-zero.md"
UTEIS = re.compile(r"\w", re.UNICODE)
LIMITE = 200  # chars uteis por pagina; abaixo disso o texto nao serve para conferir

# Excecoes medidas a mao, cada uma com o motivo. Sem elas a tabela mentiria nos dois sentidos:
# diria que [4] nao esta custodiada (esta, por manifesto de API) e trataria [10] como documento
# (e derivacao).
EXCECOES = {
    4: ("sim", "sim", "custodia por MANIFEST_ComexStat.json + raw/ncm_2024.json e CSVs; "
                      "fonte de API nao tem PDF"),
    10: ("n/a", "n/a", "derivacao de massas atomicas; entradas: [7] custodiada, "
                       "USDA AMS TR-2022 nao custodiada"),
    15: ("sim", "não", "arquivo com hash valido; conteudo e muro Cloudflare (36 caracteres)"),
    16: ("não", "não", "a tese existe como PDF na branch do cobre, nao nesta gaveta"),
}


def medir():
    linhas = []
    for ref in sorted(rodar.MAPA):
        bruto = rodar.MAPA[ref] if isinstance(rodar.MAPA[ref], (list, tuple)) else [rodar.MAPA[ref]]
        arquivos = [a for a in bruto if a]
        pag = chars = 0
        sha = ""
        custodiados = 0
        for a in arquivos:
            p = BASE / a
            if p.exists():
                custodiados += 1
                doc = fitz.open(p)
                pag += doc.page_count
                chars += sum(len(UTEIS.findall(pg.get_text())) for pg in doc)
                if not sha:
                    sha = hashlib.sha256(p.read_bytes()).hexdigest()[:12]
        cpp = (chars // pag) if pag else 0
        arq = "sim" if custodiados else "não"
        txtu = "sim" if cpp >= LIMITE else ("não" if custodiados else "—")
        if ref in EXCECOES:
            arq, txtu, _ = EXCECOES[ref]
        linhas.append((ref, pag, chars, sha, arq, txtu))
    return linhas


def main():
    linhas = medir()
    if "--contagem" in sys.argv:
        for rotulo, i in (("arquivo custodiado", 4), ("texto utilizavel", 5)):
            conta = {}
            for l in linhas:
                conta[l[i]] = conta.get(l[i], 0) + 1
            print(f"{rotulo}: {conta}")
        print(f"identificada: {len(linhas)} de {len(linhas)}")
        print("leitura integral confirmada: 0 de %d (sem artefato de leitura arquivado)" % len(linhas))
        return

    print("| Ref | Identificada | Arquivo custodiado | Texto utilizável | Leitura integral |")
    print("|---:|:---:|:---:|:---:|:---:|")
    for ref, pag, chars, sha, arq, txtu in linhas:
        print(f"| [{ref}] | sim | {arq} | {txtu} | não |")
    print(f"\n<!-- arquivo={len(linhas)} | leitura integral = 0 | "
          f"gerado por scripts/gate_boro/estados_referencia.py -->")


if __name__ == "__main__":
    main()
