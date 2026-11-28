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

W = Path(__file__).resolve().parents[2]  # raiz do repo, nao caminho de worktree
GAV = W / "docs" / "analyses" / "boro"
PECA = Path("/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica/_privado/"
            "/pareceres/boro-artigo-20261124/O-boro-peca-completa.html")

PAINEIS = [
    ("p-denso", "Artigo denso", GAV / "artigo-o-boro-explicado-do-zero.md"),
    ("p-blog", "Artigo de blog", GAV / "blog-o-boro-ninguem-regula.md"),
]


def rotular_celulas(html: str) -> str:
    """Poe data-l em TODA celula, tirado do <th> da coluna.

    A peca esconde o thead no celular (`thead{display:none}`) e mostra o rotulo por
    `td::before{content:attr(data-l)}`. Celula sem data-l vira card sem unidade: o leitor
    ve "200,7 mil" e nao sabe se e tonelada, dolar ou ano. O conversor so marca parte das
    celulas; aqui todas recebem o rotulo da propria coluna.
    """
    def por_tabela(m):
        tab = m.group(0)
        cab = re.findall(r"<th[^>]*>(.*?)</th>", tab, re.S)
        if not cab:
            return tab
        rotulos = [re.sub(r"<[^>]+>", "", c).strip() for c in cab]
        corpo_i = tab.find("<tbody>")
        if corpo_i < 0:
            return tab
        cabeca, corpo = tab[:corpo_i], tab[corpo_i:]

        def por_linha(lm):
            linha = lm.group(0)
            k = [0]

            def por_celula(cm):
                abre, conteudo = cm.group(1), cm.group(2)
                if "data-l=" in abre:
                    k[0] += 1
                    return cm.group(0)
                i = k[0]
                k[0] += 1
                if i < len(rotulos) and rotulos[i]:
                    abre = abre[:-1] + f' data-l="{rotulos[i].replace(chr(34), "&quot;")}">'
                return abre + conteudo + "</td>"

            return re.sub(r"(<td[^>]*>)(.*?)</td>", por_celula, linha, flags=re.S)

        corpo = re.sub(r"<tr[^>]*>.*?</tr>", por_linha, corpo, flags=re.S)
        return cabeca + corpo

    return re.sub(r"<table.*?</table>", por_tabela, html, flags=re.S)


def md_para_html(caminho: Path) -> str:
    txt = caminho.read_text(encoding="utf-8")
    # fora o front matter
    if txt.startswith("---"):
        fim = txt.find("\n---", 3)
        if fim > 0:
            txt = txt[fim + 4:]
    html = markdown.markdown(txt, extensions=["tables", "fenced_code", "toc", "attr_list"])
    return rotular_celulas(html)


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
