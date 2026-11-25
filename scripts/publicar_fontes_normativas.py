# -*- coding: utf-8 -*-
"""Publica as fontes NORMATIVAS e de CUSTÓDIA das 14 referências do cobre.

Algumas referências apontam para material fora de `ago_28_Sulfato_S11` (CONAMA, OMS,
PNRS, ComexStat, Gauss). O auditor externo só lê o publicado — cada uma é copiada byte
a byte para docs/analyses/cobre/fontes/ e entra no manifesto com sha256.
"""
import hashlib
import json
import os
import shutil

REPO = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica"
PRIV = f"{REPO}/_privado"
DEST = f"{REPO}/docs/analyses/cobre/fontes"

# (ref nº, origem, destino relativo)
MAPA = [
    (9,  f"{PRIV}/fontes-documentais/ago_28_Boratos_Cobre/pdf/BR_CONAMA_430_2011_Efluentes.pdf",
         "pdf/BR_CONAMA_430_2011_Efluentes.pdf"),
    (9,  f"{PRIV}/fontes-documentais/ago_28_Boratos_Cobre/md/BR_CONAMA_430_2011_Efluentes.md",
         "md/BR_CONAMA_430_2011_Efluentes.md"),
    (10, f"{PRIV}/fontes-documentais/ago_28_Boratos_Cobre/pdf/BR_CONAMA_357_2005_Qualidade_Aguas.pdf",
         "pdf/BR_CONAMA_357_2005_Qualidade_Aguas.pdf"),
    (10, f"{PRIV}/fontes-documentais/ago_28_Boratos_Cobre/md/BR_CONAMA_357_2005_Qualidade_Aguas.md",
         "md/BR_CONAMA_357_2005_Qualidade_Aguas.md"),
    (12, f"{PRIV}/governanca-operacional/extracoes/cobre/fontes_novas/pnrs_art3_XVI.txt",
         "pnrs_art3_XVI.txt"),
]


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def publicar():
    itens = []
    for ref, src, rel in MAPA:
        if not os.path.exists(src):
            print(f"  ! AUSENTE (ref {ref}): {src}")
            continue
        dst = os.path.join(DEST, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        h1, h2 = sha(src), sha(dst)
        assert h1 == h2, f"cópia divergente: {rel}"
        itens.append({"ref": ref, "path": f"docs/analyses/cobre/fontes/{rel}",
                      "bytes": os.path.getsize(dst), "sha256": h2})
        print(f"  ref {ref:2d}  {rel:52s} {os.path.getsize(dst):>9,} B  {h2[:16]}…")
    return itens


if __name__ == "__main__":
    print("=== publicando fontes normativas ===")
    itens = publicar()
    p = f"{DEST}/MANIFEST_FONTES_NORMATIVAS.json"
    json.dump({"schema": "ACERVO_FONTES_NORMATIVAS_R1", "gaveta": "cobre",
               "data": "2026-11-24",
               "nota": ("Fontes normativas das referências 9, 10 e 12, publicadas byte a byte "
                        "para o auditor externo. Hash calculado na origem e reconferido no destino."),
               "total": len(itens), "fontes": itens},
              open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\nmanifesto: {p}\ntotal: {len(itens)}")
