# -*- coding: utf-8 -*-
"""Publica as fontes documentais do cobre para auditoria externa.

O auditor externo lê SÓ o publicado (Constituição R4, Art. 5.6). As fontes estão em
`_privado/`, que é gitignored — sem isto o pacote cita fonte que o auditor não alcança.

Copia os ORIGINAIS (PDF, HTML) e os extratos .md, preservando bytes, e gera o manifesto
com sha256 de cada arquivo, conferido depois da cópia.
"""
import hashlib
import json
import os
import shutil

REPO = os.environ.get("COBRE_REPO", "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica")
ORIG = f"{REPO}/_privado/fontes-documentais/ago_28_Sulfato_S11"
DEST = f"{REPO}/docs/analyses/cobre/fontes"


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def publicar():
    os.makedirs(DEST, exist_ok=True)
    itens = []
    for raiz, _, arquivos in os.walk(ORIG):
        for a in sorted(arquivos):
            if a == "MANIFEST_S11.json":
                continue
            src = os.path.join(raiz, a)
            rel = os.path.relpath(src, ORIG)
            dst = os.path.join(DEST, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)

            h_orig = sha(src)
            h_dest = sha(dst)
            assert h_orig == h_dest, f"cópia divergente: {rel}"
            itens.append({
                "path": f"docs/analyses/cobre/fontes/{rel}",
                "origem_privada": f"_privado/fontes-documentais/ago_28_Sulfato_S11/{rel}",
                "bytes": os.path.getsize(dst),
                "sha256": h_dest,
            })
    return itens


if __name__ == "__main__":
    print("=== publicando fontes do cobre ===")
    itens = publicar()
    for i in itens:
        print(f"  {i['path']:72s} {i['bytes']:>9,} B  {i['sha256'][:16]}…")

    man = {
        "schema": "ACERVO_FONTES_PUBLICADAS_R1",
        "gaveta": "cobre",
        "frente": "COBRE",
        "data": "2026-11-24",
        "nota": ("Originais custodiados em _privado (gitignored) e publicados aqui byte a byte "
                 "para que o auditor externo os alcance pelo repositório. O sha256 foi calculado "
                 "no arquivo de origem e RECONFERIDO no publicado."),
        "total": len(itens),
        "fontes": itens,
    }
    p = f"{DEST}/MANIFEST_FONTES_PUBLICADAS.json"
    json.dump(man, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\nmanifesto: {p}\ntotal: {len(itens)} arquivos")
