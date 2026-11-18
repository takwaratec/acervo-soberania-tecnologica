#!/usr/bin/env python3
"""Conta mencao de genero no texto integral dos PDFs da colecao custodiada.

Reproduz a varredura citada em `capitulo-bambu-exotico-naturalizado-invasor.md`.
Os PDFs NAO sao versionados (_privado/, gitignored): quem audita recebe o JSON
de saida e o metodo, e pode rodar de novo onde os PDFs existirem.

Uso:
    python3 varrer_generos.py CAMINHO_DA_COLECAO [-o saida.json]

Saida: JSON com contagem por genero + registro artigo por artigo.
"""
import argparse
import json
import os
import re
import sys

GENEROS = [
    "Bambusa", "Phyllostachys", "Dendrocalamus", "Gigantochloa",
    "Guadua", "Merostachys", "Chusquea",
]

# Termos de naturalizacao/invasao, com o radical que interessa.
TERMOS = ["naturali", "invasive", "exotic", "allen"]


def texto_integral(caminho):
    from pypdf import PdfReader

    leitor = PdfReader(caminho)
    return " ".join((pagina.extract_text() or "") for pagina in leitor.pages)


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

    artigos = []
    for caminho in arquivos:
        try:
            txt = texto_integral(caminho)
        except Exception as erro:  # PDF corrompido nao derruba a varredura
            artigos.append({"arquivo": caminho, "erro": str(erro)})
            continue
        gen, ter = contar(txt)
        artigos.append({
            "volume": os.path.basename(os.path.dirname(caminho)),
            "arquivo": os.path.basename(caminho),
            "chars": len(txt),
            "generos": gen,
            "naturalizacao": ter,
        })

    total = {
        g: {
            "pdfs": sum(1 for a in artigos if a.get("generos", {}).get(g)),
            "mencoes": sum(a.get("generos", {}).get(g, 0) for a in artigos),
        }
        for g in GENEROS
    }

    saida = {
        "metodo": "texto integral por pypdf; regex de palavra inteira; inclui listas de referencias",
        "colecao": os.path.abspath(args.colecao),
        "pdfs_lidos": len(artigos),
        "pdfs_com_erro": sum(1 for a in artigos if "erro" in a),
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
    for g in GENEROS:
        print(f"  {g:16} {total[g]['pdfs']:4} artigos  {total[g]['mencoes']:6} mencoes")
    print(f"saida: {args.saida}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
