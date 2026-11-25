#!/usr/bin/env python3
"""Regera os paineis da peca HTML a partir dos markdown da gaveta do boro.

O corpo da peca (CSS, JS, abas) e preservado; so o conteudo dos seis paineis e
reconstruido. A peca e derivada do texte versionado — nunca editada a mao, senao
ela e uma segunda fonte que ninguem confere.
"""
import re
import sys
from pathlib import Path

import markdown

W = Path("/Users/fabiotakwara/.hermes/cache/scratch/boro-v4-wt")
GAV = W / "docs" / "analyses" / "boro"
PECA = Path("/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica/_privado/"
            "/pareceres/boro-artigo-20261124/O-boro-peca-completa.html")

PAINEIS = [
    ("p-denso", "Artigo denso", GAV / "artigo-o-boro-explicado-do-zero.md"),
    ("p-blog", "Artigo de blog", GAV / "blog-o-boro-ninguem-regula.md"),
]


def md_para_html(caminho: Path) -> str:
    txt = caminho.read_text(encoding="utf-8")
    # fora o front matter
    if txt.startswith("---"):
        fim = txt.find("\n---", 3)
        if fim > 0:
            txt = txt[fim + 4:]
    return markdown.markdown(txt, extensions=["tables", "fenced_code", "toc", "attr_list"])


def troca_painel(html: str, pid: str, novo: str) -> tuple[str, bool]:
    """Substitui o conteudo interno do <section id=pid>...</section>."""
    padrao = re.compile(r'(<section[^>]*id="' + re.escape(pid) + r'"[^>]*>)(.*?)(</section>)',
                        re.S)
    m = padrao.search(html)
    if not m:
        return html, False
    return html[:m.start(2)] + "\n" + novo + "\n" + html[m.end(2):], True


def main():
    html = PECA.read_text(encoding="utf-8")
    for pid, rotulo, caminho in PAINEIS:
        if not caminho.exists():
            sys.exit(f"markdown ausente: {caminho}")
        novo = md_para_html(caminho)
        html, ok = troca_painel(html, pid, novo)
        print(f"{pid:12s} {'OK' if ok else 'PAINEL NAO ENCONTRADO':22s} {len(novo):>7,} chars  <- {caminho.name}")
        if not ok:
            sys.exit("painel nao encontrado: abortando sem gravar")
    PECA.write_text(html, encoding="utf-8")
    print(f"\ngravado: {PECA}  ({len(html):,} chars)")


if __name__ == "__main__":
    main()
