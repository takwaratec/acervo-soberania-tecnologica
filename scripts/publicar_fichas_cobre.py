# -*- coding: utf-8 -*-
"""Promove as 6 fichas de _privado (gitignored) para a área versionada e as declara
HOMOLOGADAS INTERNAMENTE, com a autoridade do soberano registrada.

FONTE:  _privado/fichas/ago_28_Sulfato_S11/*.md  (lida byte a byte, preservada)
DESTINO: docs/analyses/cobre/fichas/*.md          (versionado, público)
"""
import hashlib
import os
import re
import shutil

REPO = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica"
ORIG = f"{REPO}/_privado/fichas/ago_28_Sulfato_S11"
DEST = f"{REPO}/docs/analyses/cobre/fichas"

os.makedirs(DEST, exist_ok=True)

CABECALHO = """---
schema: ACERVO_FICHA_R1
gaveta: cobre
frente: COBRE
estado_documental: homologado-internamente
homologacao:
  tipo: INTERNA
  autoridade: FABIO
  data: 2026-11-24
  instrumento: "instrução direta do soberano no tópico da frente COBRE"
  transcricao: >
    "Sim, você vai colocar como homologação interna. Internamente nós estamos homologando.
    Se o auditor externo disser que não, nós alteramos o status. Mas a princípio sim, estamos
    homologando, vai para o repositório público, entra na pasta de análises do acervo soberania
    tecnológica conforme foi instruído."
  alcance: >
    Homologação INTERNA: vale dentro do acervo e autoriza a publicação. NÃO é homologação
    científica por par, NÃO é homologação regulatória e NÃO substitui a auditoria externa.
    O estado reverte para ficha-em-revisao se o auditor externo apontar furo material.
  auditoria_externa: PENDENTE
homologacao_automatica: false
publicacao: docs/analyses/cobre/fichas/
---

> **Estado: homologada internamente (2026-11-24, autoridade FABIO).** Publicada para
> auditoria externa. Se o auditor externo apontar furo material, o estado reverte para
> `ficha-em-revisao` e a correção é publicada com a rodada seguinte.
"""


def promover():
    origem = sorted(f for f in os.listdir(ORIG) if f.endswith(".md"))
    assert len(origem) == 6, f"esperava 6 fichas, achei {len(origem)}"
    rel = []
    for arq in origem:
        src = os.path.join(ORIG, arq)
        dst = os.path.join(DEST, arq)
        bruto = open(src, "rb").read()
        sha_antes = hashlib.sha256(bruto).hexdigest()

        txt = bruto.decode("utf-8")
        # substituir o bloco de frontmatter
        if txt.startswith("---"):
            fim = txt.find("\n---", 3)
            corpo = txt[fim + 4:].lstrip("\n")
        else:
            corpo = txt
        novo = CABECALHO + "\n" + corpo

        open(dst, "w", encoding="utf-8").write(novo)
        sha_depois = hashlib.sha256(open(dst, "rb").read()).hexdigest()
        rel.append({
            "arquivo": arq,
            "origem": f"_privado/fichas/ago_28_Sulfato_S11/{arq}",
            "destino": f"docs/analyses/cobre/fichas/{arq}",
            "sha256_origem": sha_antes,
            "sha256_publicado": sha_depois,
            "bytes": os.path.getsize(dst),
        })
        print(f"  {arq}\n    origem  {sha_antes[:16]}…\n    publicado {sha_depois[:16]}…  {os.path.getsize(dst):,} B")
    return rel


if __name__ == "__main__":
    print("=== promovendo 6 fichas para a área versionada ===")
    r = promover()
    import json
    p = f"{DEST}/MANIFEST_FICHAS_PUBLICADAS.json"
    json.dump({"schema": "ACERVO_FICHAS_PUBLICADAS_R1", "fichas": r,
               "estado": "homologado-internamente",
               "autoridade": "FABIO", "data": "2026-11-24"},
              open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\nmanifesto: {p}")
    print(f"total: {len(r)} fichas")
