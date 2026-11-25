#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Portão da leitura integral: nenhum parágrafo sem classe, nenhuma classe sem parágrafo.

Compara o índice de cada documento (todos os ids extraídos) com a classificação declarada.
Parágrafo não classificado = documento não lido na íntegra. Id classificado que não existe no
índice = classificação inventada. Os dois reprovam.

Emite também o relatório humano por documento, com a cobertura provada.
"""
import json
import os
import re
import sys

RAIZ = os.environ.get("COBRE_REPO", "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica")
DEST = f"{RAIZ}/docs/analyses/cobre/leitura-integral"
sys.path.insert(0, f"{RAIZ}/scripts")

from s11e_classificacao import CLASSIFICACAO  # noqa: E402


def expandir(doc_id, ini, fim, ordem):
    """Fatia da ordem real do documento — suporta intervalo que atravessa página."""
    a = f"{doc_id}:{ini}"
    b = f"{doc_id}:{fim}"
    if a not in ordem or b not in ordem:
        raise SystemExit(f"extremo de intervalo inexistente: {ini} ou {fim}")
    i, j = ordem.index(a), ordem.index(b)
    if j < i:
        raise SystemExit(f"intervalo invertido: {ini}-{fim}")
    return ordem[i:j + 1]


def main():
    docs = sorted(f[:-16] for f in os.listdir(DEST) if f.endswith(".paragrafos.json"))
    total_ok = total_geral = 0
    problemas = []
    for doc in docs:
        indice = json.load(open(f"{DEST}/{doc}.paragrafos.json", encoding="utf-8"))
        ids_indice = [p["id"] for p in indice["paragrafos"]]
        faixas = CLASSIFICACAO.get(doc, [])
        ids_classe = []
        for rng, _c, _t, _r in faixas:
            ini, _, fim = rng.partition("-")
            ids_classe += expandir(doc, ini, fim or ini, ids_indice)
        faltando = [i for i in ids_indice if i not in set(ids_classe)]
        sobrando = [i for i in ids_classe if i not in set(ids_indice)]
        duplicado = len(ids_classe) != len(set(ids_classe)) or len(ids_indice) != len(set(ids_indice))
        ok = not faltando and not sobrando and not duplicado
        total_geral += len(ids_indice)
        total_ok += len(ids_indice) - len(faltando) if ids_classe else 0

        # relatório humano
        linhas = [
            f"# Leitura integral — {indice['documento']}",
            "",
            f"Custódia: `_privado/fontes-documentais/{indice['custodia']}/`  ",
            f"Parágrafos: **{len(ids_indice)}** · cobertura classificada: "
            f"**{len(ids_indice) - len(faltando)}/{len(ids_indice)}**  ",
            f"Estado: **{'INTEGRAL' if ok else 'PARCIAL'}**",
            "",
        ]
        if not ok:
            linhas += [f"> **NÃO LIDO NA ÍNTEGRA.** "
                       f"{len(faltando)} parágrafos sem classe. "
                       f"Achado pendente — este documento não sustenta afirmação da peça.", ""]
        linhas += ["| parágrafos | classe | o que o trecho faz | toca a tese |",
                   "|---|---|---|---|"]
        for rng, classe, tema, relevante in faixas:
            rotulo = rng.replace("-", "–")
            linhas.append(f"| `{rotulo}` | {classe} | {tema} | {'**sim**' if relevante else 'não'} |")
        if faltando:
            linhas += ["", "**Parágrafos sem classe:**", ""]
            linhas += [f"- `{i}`" for i in faltando[:60]]
            if len(faltando) > 60:
                linhas.append(f"- … e mais {len(faltando) - 60}")
        open(f"{DEST}/{doc}.leitura.md", "w", encoding="utf-8").write("\n".join(linhas) + "\n")

        print(f"  {doc:52s} {len(ids_indice) - len(faltando):>4}/{len(ids_indice):<4} "
              f"{'INTEGRAL' if ok else 'PARCIAL'}")
        if not ok:
            problemas.append((doc, len(faltando), len(sobrando), duplicado))

    print(f"\nCOBERTURA: {total_ok}/{total_geral} parágrafos classificados")
    for doc, f, s, d in problemas:
        detalhe = []
        if f:
            detalhe.append(f"{f} sem classe")
        if s:
            detalhe.append(f"{s} inventados")
        if d:
            detalhe.append("id duplicado")
        print(f"  REPROVA {doc}: {', '.join(detalhe)}")
    sys.exit(0 if not problemas else 1)


if __name__ == "__main__":
    main()
