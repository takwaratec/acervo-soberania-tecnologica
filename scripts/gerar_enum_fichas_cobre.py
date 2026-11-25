#!/usr/bin/env python3
"""Gera a lista de fichas do artigo a partir do inventário (C-07).

A lista era escrita à mão e a ficha da IN Ibama 5/1992 ficou de fora por três versões:
o inventário tinha 12, a enumeração tinha 11, e nada acusava. Aqui a lista sai do
manifesto de fichas publicadas + o texto editorial de `fichas/ENUMERACAO_FICHAS.json`,
e o script FALHA se os dois conjuntos não forem iguais — ficha sem entrada ou entrada
sem ficha não passa.

Uso:
  python3 scripts/gerar_enum_fichas_cobre.py          # confere, não escreve
  python3 scripts/gerar_enum_fichas_cobre.py --aplicar
"""
import json
import os
import re
import sys

REPO = os.environ.get("COBRE_REPO", ".")
BASE = os.path.join(REPO, "docs/analyses/cobre")
ARTIGO = os.path.join(BASE, "00-artigo-o-cobre-explicado-do-zero.md")
MANIF = os.path.join(BASE, "fichas/MANIFEST_FICHAS_PUBLICADAS.json")
ENUM = os.path.join(BASE, "fichas/ENUMERACAO_FICHAS.json")
CABECALHO = "## Fontes custodiadas e fichas técnicas"


def main():
    aplicar = "--aplicar" in sys.argv
    man = {f["arquivo"] for f in json.load(open(MANIF, encoding="utf-8"))["fichas"]}
    enum = json.load(open(ENUM, encoding="utf-8"))["fichas"]
    itens = {e["arquivo"] for e in enum}

    faltam = man - itens
    sobram = itens - man
    if faltam or sobram:
        print(f"FALHA: {len(faltam)} ficha(s) no inventário sem entrada na enumeração: "
              f"{sorted(faltam)}")
        print(f"       {len(sobram)} entrada(s) na enumeração sem ficha no inventário: "
              f"{sorted(sobram)}")
        return 1

    linhas = []
    for e in sorted(enum, key=lambda x: x["ordem"]):
        linhas.append(f'- **{e["ordem"]}. {e["rotulo"]}** — {e["descricao"]}. '
                      f'Ficha: `{e["arquivo"]}`')
    bloco = "\n".join(linhas)

    texto = open(ARTIGO, encoding="utf-8").read()
    if CABECALHO not in texto:
        print(f"FALHA: cabeçalho '{CABECALHO}' não encontrado em {ARTIGO}")
        return 1
    antes, resto = texto.split(CABECALHO, 1)
    corpo, depois = re.split(r"\n---\n", resto, maxsplit=1)
    # preserva a linha de abertura ("Cada ficha identifica ...")
    abertura = corpo.strip().split("\n\n")[0]
    novo = f"{abertura}\n\n{bloco}\n"
    final = antes + CABECALHO + "\n\n" + novo + "\n---\n" + depois

    n_antigas = len(re.findall(r"^- \*\*\d+\.", corpo, re.M))
    print(f"fichas no inventário: {len(man)} · na enumeração: {len(enum)} · "
          f"bullets no artigo antes: {n_antigas} · depois: {len(linhas)}")
    if aplicar:
        open(ARTIGO, "w", encoding="utf-8").write(final)
        print(f"escrito: {ARTIGO}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
