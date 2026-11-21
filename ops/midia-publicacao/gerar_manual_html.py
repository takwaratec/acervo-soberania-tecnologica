#!/usr/bin/env python3
"""Renderiza MANUAL_ESTEIRA_R1.md em HTML navegável.

O manual em Markdown é a FONTE. Este gerador existe porque manter dois documentos à mão
produziu divergência real: o HTML dizia "seis portões" quando o código tinha sete, e
prometia um estado `NAO_VERIFICADO` que o fluxo nunca produzia. Gerar em vez de digitar
resolve a classe do problema, não o caso.

Uso: python3 gerar_manual_html.py [--md MANUAL_ESTEIRA_R1.md] [--saida MANUAL_ESTEIRA_R1.html]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI / "piloto"))
from gerar_piloto_html import CSS, esc, md_para_html  # noqa: E402


def secoes(md: str) -> list[tuple[str, str]]:
    """Divide o manual em (título, corpo) por cabeçalho de nível 2."""
    partes = re.split(r"^## ", md, flags=re.M)
    saida = []
    for p in partes[1:]:
        titulo, _, corpo = p.partition("\n")
        saida.append((titulo.strip(), corpo))
    return saida


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", default=str(AQUI / "MANUAL_ESTEIRA_R1.md"))
    ap.add_argument("--saida", default=str(AQUI / "MANUAL_ESTEIRA_R1.html"))
    a = ap.parse_args(argv)
    md = Path(a.md).read_text(encoding="utf-8")
    cab = re.split(r"^## ", md, maxsplit=1, flags=re.M)[0]
    titulo = next((l.lstrip("# ").strip() for l in cab.splitlines() if l.startswith("# ")), "Manual")

    abas, paineis = [], []
    for i, (tit, corpo) in enumerate(secoes(md), 1):
        rotulo = re.sub(r"^\d+[A-Z]?\.\s*", "", tit)
        abas.append(f'<button data-tab="s{i}" aria-selected="{"true" if i == 1 else "false"}">'
                    f'{i} · {esc(rotulo)}</button>')
        paineis.append(f'<section id="s{i}"{" hidden" if i > 1 else ""}>\n'
                       f'<h2>{esc(tit)}</h2>\n{md_para_html(corpo)}\n</section>')

    doc = f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(titulo)}</title>
<style>{CSS}</style></head><body>
<header><h1>{esc(titulo)}</h1>
<p>Gerado de <code>{esc(Path(a.md).name)}</code>. O Markdown é a fonte; este HTML é derivado — nunca editado à mão.</p></header>
<nav role="tablist">{''.join(abas)}</nav>
<main>{''.join(paineis)}</main>
<footer>Gerado por <code>gerar_manual_html.py</code>. Sem links externos, sem dependências.</footer>
<script>
const b=[...document.querySelectorAll('nav button')];
b.forEach(x=>x.addEventListener('click',()=>{{b.forEach(o=>o.setAttribute('aria-selected',String(o===x)));
document.querySelectorAll('main section').forEach(s=>{{s.hidden=s.id!==x.dataset.tab;}});
window.scrollTo({{top:0,behavior:'instant'}});}}));
</script></body></html>
"""
    Path(a.saida).write_text(doc, encoding="utf-8")
    print(json.dumps({"saida": str(Path(a.saida).resolve()), "abas": len(abas),
                      "bytes": len(doc.encode())}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
