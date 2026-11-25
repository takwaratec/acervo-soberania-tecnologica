#!/usr/bin/env python3
"""Gate A2 (AGENTS_LOCAL.md § Conferência de afirmação).

Documento que DECLARA conferência integral precisa do registro que a sustente, ao lado dele.
Sem registro, o veredito é FAIL. O gate NÃO julga se a conferência foi boa — só se a declaração
tem prova. Medir conteúdo é outro instrumento.

Uso:
    python3 scripts/check_declaracao_conferencia.py [raiz] [--json]
"""
import json
import os
import re
import sys

EXT = (".md",)
IGNORAR_DIR = {".git", "node_modules", "_privado", "tmp", "site"}
# A regra não se audita a si mesma: o texto da norma cita as frases proibidas como exemplo.
IGNORAR_ARQ = {"AGENTS.md", "AGENTS_LOCAL.md", "AGENTS_BASE.md"}

# Frases que DECLARAM medição. Não são estilo: são afirmação sobre o próprio trabalho.
PADROES = [
    r"toda[s]?\s+afirma[çc][õo]es?\s+num[ée]ricas?.{0,60}conferid",
    r"cada\s+afirma[çc][ãa]o\s+num[ée]rica.{0,40}conferid",
    r"todas\s+as\s+fontes?.{0,40}(lidas?\s+integralmente|conferid)",
    r"conferid[oa]s?\s+(integralmente|contra\s+a\s+fonte\s+prim[áa]ria)",
    r"verificad[oa]s?\s+contra\s+a\s+fonte\s+prim[áa]ria",
    r"nenhum\s+dado\s+foi\s+inventado.{0,40}(conferid|verificad)",
]
RE_NEUTRALIZA = re.compile(r"\bn[ãa]o\s+(foi|foram|est[áa]|est[ãa]o)\b|\bnem\s+todas\b|parcial", re.I)

# O que conta como registro ao lado do documento.
REGISTRO_NOMES = re.compile(
    r"(CONFERENCIA|CONFER[ÊE]NCIA|REGISTRO).*(\.json|\.csv|\.tsv|\.md)$", re.I)


def docs(raiz):
    for base, dirs, files in os.walk(raiz):
        dirs[:] = [d for d in dirs if d not in IGNORAR_DIR]
        for f in files:
            if f in IGNORAR_ARQ:
                continue
            if f.endswith(EXT):
                yield os.path.join(base, f)


# Linha de proveniência descreve o DOWNLOAD e o hash de um arquivo; chamar isso de conferência de
# afirmação é outra coisa. Exigimos, na mesma linha, vocabulário de afirmação, não só de arquivo.
RE_ARTEFATO = re.compile(
    r"\.pdf|\bPDFs?\b|\bp[áa]ginas?\b|sha-?256|\bhash\b", re.I)
RE_CONTEXTO_AFIRMACAO = re.compile(
    r"afirma|n[úu]mero|dado|tabela|valor|resultado|cita|texto", re.I)


def declaracoes(texto):
    achados = []
    for i, linha in enumerate(texto.splitlines(), 1):
        for p in PADROES:
            if not re.search(p, linha, re.I):
                continue
            if RE_NEUTRALIZA.search(linha):
                break
            # Proveniência de ARQUIVO se reconhece pelo objeto declarado (PDF, página, hash, data de
            # download), não por palavra solta: a linha de proveniência usa "páginas" e "hash" e não
            # fala de afirmação. Chamar isso de conferência de afirmação seria falso positivo em massa.
            if "conferid" in linha.lower() and RE_ARTEFATO.search(linha):
                break
                break  # proveniência de arquivo, não declaração de conferência de afirmação
            achados.append((i, linha.strip()[:160]))
            break
    return achados


def registros_ao_lado(caminho):
    d = os.path.dirname(caminho)
    stem = os.path.splitext(os.path.basename(caminho))[0]
    try:
        vizinhos = os.listdir(d)
    except OSError:
        return []
    # O registro tem de NOMEAR o documento. Basta "registro_<stem[...]>" ou o stem no fim do nome:
    # substring solta deixaria um registro de outro arquivo servir de prova (e meu teste cobrava isso).
    # O registro tem de nomear o documento: "REGISTRO_CONFERENCIA_<stem>" ou nome que TERMINE no
    # stem. Buscar o stem em qualquer posição deixava o próprio prefixo do registro ("registro",
    # "conferencia") casar com stems curtos — falso PASS que meu teste pegou.
    s_ = stem.lower()
    if len(s_) < 4:
        return []  # nome curto demais para provar a que documento o registro pertence
    nomes = [f for f in vizinhos
             if REGISTRO_NOMES.search(f) and f.lower().endswith(".json")]
    return [f for f in nomes if s_ in f.lower()]


def main(argv):
    raiz = argv[0] if argv and not argv[0].startswith("--") else "."
    problemas = []
    for caminho in sorted(docs(raiz)):
        try:
            texto = open(caminho, encoding="utf-8").read()
        except (OSError, UnicodeDecodeError):
            continue
        achados = declaracoes(texto)
        if not achados:
            continue
        prova = registros_ao_lado(caminho)
        rel = os.path.relpath(caminho, raiz)
        if prova:
            continue
        for linha, trecho in achados:
            problemas.append({"arquivo": rel, "linha": linha,
                              "problema": "declara conferência sem registro ao lado",
                              "trecho": trecho})
    if "--json" in argv:
        print(json.dumps(problemas, ensure_ascii=False, indent=2))
    else:
        for p in problemas:
            print(f"FAIL {p['arquivo']}:{p['linha']} — {p['problema']}")
            print(f"     {p['trecho']}")
        print(f"{len(problemas)} declaração(ões) sem registro")
    return 1 if problemas else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
