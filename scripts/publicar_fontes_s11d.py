# -*- coding: utf-8 -*-
"""Publica as fontes da custódia S11-d — a instrução que diz o que fazer com o resíduo.

Mesma regra da S11-c: cópia byte a byte, sha256 conferido na origem e no destino, extração
com marcador de página junto (é ela que torna a citação conferível pelo auditor externo).
"""
import hashlib
import json
import os
import shutil

REPO = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica"
ORIG = f"{REPO}/_privado/fontes-documentais/ago_28_Madeira_Tratada_S11d"
DEST = f"{REPO}/docs/analyses/cobre/fontes/s11d"

# referência nº na bibliografia -> chave do manifesto de custódia
REFS = {"in592_1992": 22}


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def main():
    man = json.load(open(f"{ORIG}/MANIFEST_S11D.json", encoding="utf-8"))
    os.makedirs(DEST, exist_ok=True)
    itens, vistos = [], set()
    for e in man["entradas"]:
        for suf in (".pdf", ".md"):
            nome = os.path.join(e["arquivo"].replace(".pdf", suf))
            if nome in vistos:
                continue
            vistos.add(nome)
            src = os.path.join(ORIG, nome)
            if not os.path.exists(src):
                print(f"  ! AUSENTE: {nome}")
                continue
            dst = os.path.join(DEST, nome)
            shutil.copy2(src, dst)
            h1, h2 = sha(src), sha(dst)
            assert h1 == h2, f"cópia divergente: {nome}"
            itens.append({
                "ref": REFS.get(e["chave"]),
                "chave": e["chave"],
                "path": f"docs/analyses/cobre/fontes/s11d/{nome}",
                "bytes": os.path.getsize(dst),
                "sha256": h2,
                "fonte_url": e["fonte_url"],
            })
            print(f"  {nome[:60]:62s} {os.path.getsize(dst):>9,} B  {h2[:16]}…")

    p = f"{DEST}/MANIFEST_FONTES_S11D.json"
    json.dump({
        "schema": "ACERVO_FONTES_S11D_R1",
        "gaveta": "cobre",
        "data": "2026-11-24",
        "nota": ("Fontes da referência 22 — a IN Ibama 5/92 resolve a pendência que a S11-c tinha "
                 "declarado. Publicada byte a byte. A via oficial do Ibama responde 403; o fac-símile "
                 "é o hospedado pela ABPM."),
        "total": len(itens),
        "fontes": itens,
        "pendentes": man["pendentes"],
    }, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\nmanifesto: {p}\ntotal: {len(itens)} arquivos")


if __name__ == "__main__":
    main()
