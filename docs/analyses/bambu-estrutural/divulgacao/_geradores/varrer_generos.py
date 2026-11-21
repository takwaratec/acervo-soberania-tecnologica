#!/usr/bin/env python3
"""Conta mencao de genero no texto integral dos PDFs da colecao custodiada.

Reproduz a varredura citada em `capitulo-bambu-exotico-naturalizado-invasor.md`.

Os PDFs NAO sao versionados (`_privado/`, gitignored). Para que a contagem seja
reproduzivel sem os binarios, o script grava:
  - sha256 e tamanho de cada PDF lido (fixa o insumo);
  - versao de Python e de pypdf (fixa o extrator);
  - diagnostico por pagina: paginas sem texto extraido, que indicam digitalizacao
    sem camada OCR e portanto contagem possivelmente subestimada.

Uso:
    python3 varrer_generos.py CAMINHO_DA_COLECAO [-o saida.json] [--sem-hash]

`--sem-hash` pula o sha256 (varredura rapida, saida nao reproduzivel).
"""
import argparse
import hashlib
import json
import os
import platform
import re
import sys

GENEROS = [
    "Bambusa", "Phyllostachys", "Dendrocalamus", "Gigantochloa",
    "Guadua", "Merostachys", "Chusquea",
]

# Radicais de naturalizacao/invasao. Case-insensitive (o texto tem
# "Invasive" em titulo e "naturalized" em prosa).
TERMOS = ["naturali", "invasive", "exotic", "alien"]  # "allen" era erro de digitacao: contava outro radical

# Abaixo disto, a pagina e tratada como sem camada de texto.
MIN_CHARS_PAGINA = 40


def sha256(caminho, bloco=1 << 20):
    h = hashlib.sha256()
    with open(caminho, "rb") as f:
        for parte in iter(lambda: f.read(bloco), b""):
            h.update(parte)
    return h.hexdigest()


def ler_pdf(caminho):
    """Devolve (texto, diagnostico_por_pagina)."""
    from pypdf import PdfReader

    leitor = PdfReader(caminho)
    textos = []
    diagnostico = []
    for i, pagina in enumerate(leitor.pages, start=1):
        try:
            txt = pagina.extract_text() or ""
        except Exception as erro:  # pagina ilegivel nao derruba o arquivo
            textos.append("")
            diagnostico.append({"pagina": i, "chars": 0, "erro": str(erro)})
            continue
        textos.append(txt)
        if len(txt.strip()) < MIN_CHARS_PAGINA:
            diagnostico.append({"pagina": i, "chars": len(txt.strip()), "sem_texto": True})
    return " ".join(textos), diagnostico


def contar(texto):
    por_genero = {}
    for g in GENEROS:
        # palavra inteira: evita "Bambusoideae" casar com "Bambusa"
        n = len(re.findall(r"\b" + g + r"\b", texto))
        if n:
            por_genero[g] = n
    por_termo = {}
    for t in TERMOS:
        n = len(re.findall(t, texto, re.I))
        if n:
            por_termo[t] = n
    return por_genero, por_termo


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("colecao")
    ap.add_argument("-o", "--saida", default="generos_por_artigo.json")
    ap.add_argument("--sem-hash", action="store_true",
                    help="nao calcula sha256 (mais rapido, menos reproduzivel)")
    args = ap.parse_args()

    if not os.path.isdir(args.colecao):
        print(f"colecao nao encontrada: {args.colecao}", file=sys.stderr)
        return 1

    arquivos = sorted(
        os.path.join(raiz, f)
        for raiz, _, nomes in os.walk(args.colecao)
        for f in nomes
        if f.lower().endswith(".pdf")
    )
    if not arquivos:
        print("nenhum PDF na colecao", file=sys.stderr)
        return 1

    import pypdf  # so depois do parse dos args

    artigos = []
    for caminho in arquivos:
        registro = {
            "volume": os.path.basename(os.path.dirname(caminho)),
            "arquivo": os.path.basename(caminho),
            "bytes": os.path.getsize(caminho),
        }
        if not args.sem_hash:
            registro["sha256"] = sha256(caminho)
        try:
            txt, diag = ler_pdf(caminho)
        except Exception as erro:
            registro["erro"] = str(erro)
            artigos.append(registro)
            continue
        gen, ter = contar(txt)
        registro.update({
            "chars": len(txt),
            "paginas_sem_texto": diag,
            "generos": gen,
            "naturalizacao": ter,
        })
        artigos.append(registro)

    total = {
        g: {
            "pdfs": sum(1 for a in artigos if a.get("generos", {}).get(g)),
            "mencoes": sum(a.get("generos", {}).get(g, 0) for a in artigos),
        }
        for g in GENEROS
    }

    sem_texto = sum(len(a.get("paginas_sem_texto", [])) for a in artigos)
    arquivos_com_pagina_vazia = sum(1 for a in artigos if a.get("paginas_sem_texto"))

    saida = {
        "metodo": (
            "texto integral por pypdf; regex de palavra inteira para genero; "
            "radical case-insensitive para naturalizacao; inclui listas de referencia"
        ),
        "ambiente": {
            "python": platform.python_version(),
            "pypdf": pypdf.__version__,
            "plataforma": platform.platform(),
        },
        "colecao": os.path.abspath(args.colecao),
        "pdfs_lidos": len(artigos),
        "pdfs_com_erro": sum(1 for a in artigos if "erro" in a),
        "paginas_sem_texto": sem_texto,
        "arquivos_com_pagina_sem_texto": arquivos_com_pagina_vazia,
        "aviso_ocr": (
            "Paginas com menos de 40 caracteres sao tratadas como sem camada de texto. "
            "pypdf nao faz OCR: se a colecao tiver PDF digitalizado, a contagem e subestimada. "
            "Confira o campo paginas_sem_texto antes de citar os numeros."
        ),
        "nota": (
            "As contagens se sobrepoem: um artigo cita varios generos e nao somam o total. "
            "Mencao em referencia bibliografica conta. Mede em quantos artigos o genero e discutido, "
            "nao quantos artigos sao sobre o genero."
        ),
        "total_por_genero": total,
        "artigos": artigos,
    }
    with open(args.saida, "w", encoding="utf-8") as f:
        json.dump(saida, f, ensure_ascii=False, indent=1)

    print(f"pdfs lidos: {len(artigos)} | erros: {saida['pdfs_com_erro']}")
    print(f"paginas sem texto: {sem_texto} em {arquivos_com_pagina_vazia} arquivos")
    for g in GENEROS:
        print(f"  {g:16} {total[g]['pdfs']:4} artigos  {total[g]['mencoes']:6} mencoes")
    print(f"ambiente: python {saida['ambiente']['python']} / pypdf {saida['ambiente']['pypdf']}")
    print(f"saida: {args.saida}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
