#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Portão de fidelidade: cada trecho entre aspas nas fichas tem de existir no extrato.

Regra da casa: citação entre aspas que não retorna no grep do extrato é parágrafo com
aparências de prova. Aqui cada bloco de citação é normalizado (espaço, aspas tipográficas,
hífen) e procurado literalmente na extração do documento de origem.
Fragmentos separados por "[...]" são conferidos em separado.

Cobre todas as custódias declaradas em CUSTODIAS — a S11-c (madeira tratada) e a S11-d
(a instrução que disciplina a destinação final).
"""
import os
import re
import sys

RAIZ = os.environ.get("COBRE_REPO", "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica")

CUSTODIAS = {
    "ago_28_Madeira_Tratada_S11c": {
        "ficha-pi292-89-registro-preservativos-madeira.md":
            "1989_pi292_preservativos_registro.md",
        "ficha-pn151-97-ibama-risco-ambiental.md":
            "1997_pn151_ibama_registro_risco_ambiental.md",
        "ficha-iema-es-nt01-2023-preservacao-madeira.md":
            "2023_iema_es_nt01_preservacao_madeira.md",
        "ficha-abpm-fg4mad-destinacao-residuo-madeira-tratada.md":
            "2016_abpm_fg4mad_destinacao_residuos_madeira_tratada.md",
        "ficha-ufsm-2025-cca-moiroes-contaminacao-solo.md":
            "2025_ufsm_ciencia_florestal_cca_moiroes_solo.md",
    },
    "ago_28_Madeira_Tratada_S11d": {
        "ficha-in05-92-ibama-destinacao-final-residuos.md":
            "1992_in05_ibama_destinacao_final_residuos.md",
    },
}


def norm(s):
    s = s.replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2014", "-").replace("\u2013", "-").replace("\u00ad", "")
    # negrito/itálico é apresentação, não texto: sai antes da comparação
    s = s.replace("*", "")
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def paginas(texto):
    out = []
    for bloco in texto.split("<!-- PAGE: ")[1:]:
        n, resto = bloco.split(" -->", 1)
        out.append((int(n), norm(resto)))
    return out


falhas, ok, total = [], 0, 0
for custodia, mapa in CUSTODIAS.items():
    fichas_dir = f"{RAIZ}/_privado/fichas/{custodia}"
    fontes_dir = f"{RAIZ}/_privado/fontes-documentais/{custodia}"
    for ficha, fonte in mapa.items():
        fp = os.path.join(fichas_dir, ficha)
        if not os.path.exists(fp):
            print(f"AUSENTE: {ficha}")
            continue
        linhas = open(fp, encoding="utf-8").read().split("\n")
        pags = paginas(open(os.path.join(fontes_dir, fonte), encoding="utf-8").read())
        inteiro = " ".join(p for _n, p in pags)
        # citação = linha que começa com ">" e abre aspas (retas ou tipográficas)
        i = 0
        while i < len(linhas):
            if linhas[i].startswith(">") and ('"' in linhas[i] or "\u201c" in linhas[i]):
                bloco = []
                while i < len(linhas) and linhas[i].startswith(">"):
                    bloco.append(linhas[i].lstrip("> ").strip())
                    i += 1
                cit = " ".join(bloco)
                cit = re.sub(r"\u2014|—", "-", cit)
                cit = re.sub(r"\(p\.\s*\d+[^)]*\)", "", cit)
                cit = re.sub(r",?\s*ênfase acrescentada", "", cit)
                cit = cit.replace("\u201c", "").replace("\u201d", "").replace('"', "").strip()
                for frag in re.split(r"\[\.\.\.\]|\[…\]", cit):
                    f = norm(frag).strip(" .;,")
                    if len(f) < 18:
                        continue
                    total += 1
                    if f in inteiro:
                        ok += 1
                    else:
                        falhas.append((ficha, f[:110]))
            else:
                i += 1

print(f"CITAÇÕES CONFERIDAS: {total}  OK: {ok}  FALHAS: {len(falhas)}")
for f, t in falhas:
    print(f"  FALHA [{f[:46]}] {t}")
sys.exit(0 if not falhas else 1)
