# -*- coding: utf-8 -*-
"""Publica as fontes da custódia S11-c (a norma da madeira tratada e o descarte).

O auditor externo lê apenas o publicado; `_privado/` é gitignored. Cada PDF é copiado
byte a byte, com sha256 conferido na origem e no destino, e a extração .md vai junto
porque é ela que carrega o marcador de página usado nas citações das fichas.
"""
import hashlib
import json
import os
import shutil

REPO = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica"
ORIG = f"{REPO}/_privado/fontes-documentais/ago_28_Madeira_Tratada_S11c"
DEST = f"{REPO}/docs/analyses/cobre/fontes/s11c"

# referência nº na bibliografia da peça -> chave do manifesto de custódia
REFS = {"pi292_1989": 17, "pn151_1997": 18, "iema2023": 19, "fg4mad2016": 20, "ufsm2025": 21}


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def publicar():
    man = json.load(open(f"{ORIG}/MANIFEST_S11C.json", encoding="utf-8"))
    os.makedirs(DEST, exist_ok=True)
    itens = []
    for e in man["entradas"]:
        chave = e["chave"]
        for suf in (".pdf", ".md"):
            nome = e["arquivo"].replace(".pdf", suf)
            src = os.path.join(ORIG, nome)
            if not os.path.exists(src):
                print(f"  ! AUSENTE: {nome}")
                continue
            dst = os.path.join(DEST, nome)
            shutil.copy2(src, dst)
            h1, h2 = sha(src), sha(dst)
            assert h1 == h2, f"cópia divergente: {nome}"
            itens.append({
                "ref": REFS[chave],
                "chave": chave,
                "path": f"docs/analyses/cobre/fontes/s11c/{nome}",
                "bytes": os.path.getsize(dst),
                "sha256": h2,
                "fonte_url": e["fonte_url"],
            })
            print(f"  ref {REFS[chave]:2d}  {nome[:56]:58s} {os.path.getsize(dst):>9,} B  {h2[:16]}…")
    return man, itens


if __name__ == "__main__":
    print("=== publicando as fontes da custódia S11-c ===")
    man, itens = publicar()
    p = f"{DEST}/MANIFEST_FONTES_S11C.json"
    json.dump({
        "schema": "ACERVO_FONTES_S11C_R1",
        "gaveta": "cobre",
        "data": "2026-11-24",
        "nota": ("Fontes das referências 17 a 21, publicadas byte a byte para o auditor externo. "
                 "Hash calculado na origem e reconferido no destino. As duas pendências "
                 "(IN Ibama 5/92 e UNIPAR 2022) estão declaradas sem arquivo, com motivo."),
        "total": len(itens),
        "fontes": itens,
        "pendentes": man["pendentes"],
    }, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\nmanifesto: {p}\ntotal: {len(itens)} arquivos")
    print(f"pendentes declaradas: {len(man['pendentes'])}")
