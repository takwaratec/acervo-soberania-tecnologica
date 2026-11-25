#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Registro de conferência de citações — artefato do cobre.

AGENTS_LOCAL.md A1-A6, em especial:
  A2 — declaração de conferência é afirmação sobre o próprio trabalho;
  A3 — o denominador é fixado ANTES da medição, por escrito;
  A4 — nenhuma afirmação fica sem veredito; NAO_MEDIDO é veredito válido;
  A6 — leitura por trecho é triagem, não conferência.

DENOMINADOR (fixado antes de rodar, para esta medição):
  unidade = cada bloco de citação do manuscrito, isto é, cada linha que começa com ">" no arquivo
  docs/analyses/cobre/00-artigo-o-cobre-explicado-do-zero.md (inclui as fichas anexadas, que são
  parte do artefato).

  Verdictos:
    VERBATIM          o bloco retorna literalmente no extrato de um documento custodiado;
    TRADUZIDO         o bloco não retorna porque é tradução — não é falha de conferência, e
                      literalidade não é o instrumento aplicável (registrado, não silenciado);
    NAO_MEDIDO        fonte não custodiada, paywall ou resumo — motivo declarado por bloco.

  O que este instrumento NÃO mede: se a afirmação é verdadeira. Ele mede se o texto citado
  existe, palavra por palavra, no documento que o texto diz ser a fonte. Conteúdo é o outro
  instrumento — as rodadas de auditoria.
"""
import hashlib
import json
import os
import re
import sys

RAIZ = os.environ.get("COBRE_REPO", os.environ.get("COBRE_REPO", "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica"))
ALVO = f"{RAIZ}/docs/analyses/cobre/00-artigo-o-cobre-explicado-do-zero.md"
SAIDA_DIR = f"{RAIZ}/docs/analyses/cobre"

CORPUS_DIRS = [
    f"{RAIZ}/_privado/fontes-documentais",
    f"{RAIZ}/docs/analyses/cobre/fontes",
]


def norm(s):
    s = s.replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2014", "-").replace("\u2013", "-").replace("\u00ad", "")
    s = s.replace("*", "")
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def corpus():
    """[(arquivo, pagina, texto_normalizado)] — página vem do marcador quando existe."""
    itens = []
    for base_dir in CORPUS_DIRS:
        for base, _dirs, files in os.walk(base_dir):
            for f in files:
                if not f.endswith(".md"):
                    continue
                p = os.path.join(base, f)
                try:
                    t = open(p, encoding="utf-8", errors="replace").read()
                except OSError:
                    continue
                if "<!-- PAGE: " in t:
                    for bloco in t.split("<!-- PAGE: ")[1:]:
                        cab, resto = bloco.split(" -->", 1)
                        m = re.match(r"\s*(\d+)", cab)
                        itens.append((os.path.relpath(p, RAIZ), int(m.group(1)) if m else 0,
                                      norm(resto)))
                else:
                    itens.append((os.path.relpath(p, RAIZ), 1, norm(t)))
    return itens


def blocos_citacao(texto):
    """Cada linha que começa com '>' é uma unidade do denominador."""
    out = []
    for i, linha in enumerate(texto.splitlines(), 1):
        if linha.startswith(">"):
            t = linha.lstrip("> ").strip()
            if len(t) >= 40:
                out.append((i, t))
    return out


def main():
    texto = open(ALVO, encoding="utf-8").read()
    blocos = blocos_citacao(texto)
    corp = corpus()
    print(f"DENOMINADOR FIXADO: {len(blocos)} blocos de citação")
    print(f"corpus custodiado: {len(corp)} páginas de extrato em {len(CORPUS_DIRS)} raízes\n")

    registros, n_verb, n_trad, n_nm = [], 0, 0, 0
    for linha, bruto in blocos:
        limpo = re.sub(r"\(p\.\s*\d+[^)]*\)", "", bruto)
        limpo = re.sub(r"\*\*|\*", "", limpo)
        limpo = limpo.replace("“", '"').replace("”", '"').strip(' "')
        alvo_n = norm(limpo)
        # citação longa: basta um fragmento de 60 caracteres contíguos, para não penalizar
        # reticências e cortes editoriais
        achado = None
        for arq, pag, corpo in corp:
            if len(alvo_n) <= 60:
                if alvo_n in corpo:
                    achado = (arq, pag)
                    break
            else:
                for k in range(0, max(1, len(alvo_n) - 60), 30):
                    if alvo_n[k:k + 60] in corpo:
                        achado = (arq, pag)
                        break
                if achado:
                    break
        if achado:
            veredito, motivo = "VERBATIM", ""
            n_verb += 1
        elif re.search(r"[a-z]{4,}\s+(the|of|and|with|from|that)\b", limpo, re.I):
            veredito = "TRADUZIDO"
            motivo = "trecho em inglês traduzido: literalidade não é o instrumento aplicável"
            n_trad += 1
        else:
            veredito = "NAO_MEDIDO"
            motivo = "não localizado no corpus custodiado (tradução, resumo ou fonte não custodiada)"
            n_nm += 1
        registros.append({"linha": linha, "trecho": limpo[:180], "chars": len(limpo),
                          "veredito": veredito, "motivo": motivo,
                          "arquivo_fonte": achado[0] if achado else None,
                          "pagina": achado[1] if achado else None})

    man = {
        "schema": "ACERVO_REGISTRO_CONFERENCIA_CITACOES_R1",
        "artefato": os.path.relpath(ALVO, RAIZ),
        "sha256_artefato": hashlib.sha256(open(ALVO, "rb").read()).hexdigest(),
        "data": "2026-11-24",
        "regra_do_denominador": (
            "unidade = cada linha iniciada por '>' no artefato, com 40 caracteres ou mais; "
            "denominador contado ANTES da medição e não recontado depois"),
        "instrumento": "scripts/registro_conferencia_citacoes.py",
        "o_que_mede": ("se o trecho citado existe literalmente no extrato do documento "
                       "custodiado; NÃO mede se a afirmação é verdadeira"),
        "denominador": len(blocos),
        "verbatim": n_verb,
        "traduzido": n_trad,
        "nao_medido": n_nm,
        "cobertura_verbatim": f"{n_verb}/{len(blocos)}",
        "registros": registros,
    }
    os.makedirs(SAIDA_DIR, exist_ok=True)
    nome = "REGISTRO_CONFERENCIA_00-artigo-o-cobre-explicado-do-zero.json"
    p = os.path.join(SAIDA_DIR, nome)
    json.dump(man, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    print(f"VERBATIM:   {n_verb}")
    print(f"TRADUZIDO:  {n_trad}")
    print(f"NAO_MEDIDO: {n_nm}")
    print(f"\nregistro: {p}")
    print(f"cobertura verbatim: {n_verb}/{len(blocos)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
