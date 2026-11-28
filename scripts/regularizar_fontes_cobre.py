#!/usr/bin/env python3
"""Regulariza os manifestos de fonte do cobre — C-03 e C-05.

C-03: o identificador da fonte era o número da referência na bibliografia (`ref`). Número
muda quando a bibliografia muda; identificador não pode mudar. Aqui cada fonte ganha `id`
estável (slug do arquivo) e o número passa a ser `ref_bibliografia`, declarado como legado.

C-05: os manifestos diziam que os PDFs estavam "publicados byte a byte para que o auditor
externo os alcance" — mas nenhum PDF está na árvore (governance-check proíbe). O manifesto
descrevia um objeto que não existe onde ele dizia. Passa a declarar: fora do rastreio, com
caminho privado e sha256, e o que o auditor consegue de fato.

Gera `fontes/INDICE_FONTES.json` — fonte única de verdade sobre as fontes da gaveta.

Uso:
  python3 scripts/regularizar_fontes_cobre.py            # mede
  python3 scripts/regularizar_fontes_cobre.py --aplicar
"""
import json
import os
import re
import sys

REPO = os.environ.get("COBRE_REPO", ".")
BASE = os.path.join(REPO, "docs/analyses/cobre")
FONTES = os.path.join(BASE, "fontes")
CUSTODIA = os.path.join(FONTES, "CUSTODIA_PRIVADA_PDFS.json")
INDICE = os.path.join(FONTES, "INDICE_FONTES.json")
MANIFESTOS = ["MANIFEST_FONTES_PUBLICADAS.json",
              "MANIFEST_FONTES_COMPLEMENTARES.json",
              "MANIFEST_FONTES_NORMATIVAS.json"]

NOTA_HONESTA = (
    "Estas fontes NÃO estão na árvore do repositório. `governance-check.yml` proíbe PDF "
    "versionado, e os PDFs foram retirados do rastreio; cada um continua em `_privado`, com o "
    "mesmo sha256 do byte que estava versionado (ver `CUSTODIA_PRIVADA_PDFS.json`). O que o "
    "auditor externo alcança aqui é o metadado e o hash — não o byte. Para ler o arquivo, é "
    "preciso pedi-lo pelo `caminho_privado`; `git show` não se aplica a estas fontes. O extrato "
    "textual curado de cada uma está em `fontes/md/`, reduzido ao que a peça cita (C-02)."
)


def slug(caminho: str) -> str:
    nome = os.path.basename(caminho)
    nome = re.sub(r"\.(pdf|htm|html|md|json)$", "", nome, flags=re.I)
    s = re.sub(r"[^a-z0-9]+", "-", nome.lower()).strip("-")
    return s


def main():
    aplicar = "--aplicar" in sys.argv
    cust = json.load(open(CUSTODIA, encoding="utf-8"))["pdfs"]
    por_sha = {v["sha256"]: (k, v) for k, v in cust.items()}

    indice = {}
    contagem = {"publicada": 0, "fora_do_rastreio": 0, "ausente": 0}

    for nome_man in MANIFESTOS:
        caminho_man = os.path.join(FONTES, nome_man)
        man = json.load(open(caminho_man, encoding="utf-8"))
        novos = []
        for e in man["fontes"]:
            p = e.get("path", "")
            esta = os.path.exists(os.path.join(REPO, p))
            ident = slug(p)
            item = dict(e)
            item.pop("ref", None)
            item["id"] = ident
            if "ref" in e:
                item["ref_bibliografia"] = e["ref"]
                item["ref_bibliografia_legado"] = True
            item["esta_no_repositorio"] = esta
            if esta:
                contagem["publicada"] += 1
            else:
                par = por_sha.get(e.get("sha256", ""))
                if par:
                    item["caminho_privado"] = par[1]["caminho_privado"]
                    item["custodia_verificada"] = True
                    contagem["fora_do_rastreio"] += 1
                else:
                    item["caminho_privado"] = None
                    item["custodia_verificada"] = False
                    contagem["ausente"] += 1
            novos.append(item)

            reg = indice.setdefault(ident, {
                "id": ident,
                "arquivo": os.path.basename(p),
                "sha256": e.get("sha256"),
                "bytes": e.get("bytes"),
                "esta_no_repositorio": esta,
                "caminho_privado": item.get("caminho_privado"),
                "extrato_curado": f"fontes/md/{os.path.splitext(os.path.basename(p))[0]}.md",
                "ref_bibliografia": [],
                "manifestos": [],
            })
            if e.get("ref") is not None:
                reg["ref_bibliografia"].append(e["ref"])
            reg["manifestos"].append(nome_man)

        man["fontes"] = novos
        man["nota"] = NOTA_HONESTA
        man["identificador"] = ("`id` é o identificador estável da fonte (slug do arquivo). "
                                "`ref_bibliografia` é o número na lista de referências e muda "
                                "quando a bibliografia muda: não use como chave.")
        man["regularizado_em"] = "2026-11-25"
        man["regularizacao"] = "C-03 (identificador estável) e C-05 (manifesto não afirma PDF publicado)"
        if aplicar:
            open(caminho_man, "w", encoding="utf-8").write(
                json.dumps(man, ensure_ascii=False, indent=1) + "\n")

    for reg in indice.values():
        reg["ref_bibliografia"] = sorted(set(reg["ref_bibliografia"]))
        reg["manifestos"] = sorted(set(reg["manifestos"]))

    saida = {
        "schema": "INDICE_FONTES_R1",
        "gaveta": "cobre",
        "frente": "COBRE",
        "mede": ("uma linha por fonte da gaveta, com identificador estável e o estado real de "
                 "custódia. Não mede se a fonte sustenta a afirmação: isso é a ficha."),
        "regra_de_id": "slug do nome do arquivo, minúsculo; não deriva da numeração da bibliografia",
        "total": len(indice),
        "fontes": dict(sorted(indice.items())),
    }
    print(f"fontes indexadas: {len(indice)} · publicadas na árvore: {contagem['publicada']} · "
          f"fora do rastreio com custódia provada: {contagem['fora_do_rastreio']} · "
          f"sem custódia localizada: {contagem['ausente']}")
    if aplicar:
        open(INDICE, "w", encoding="utf-8").write(json.dumps(saida, ensure_ascii=False, indent=1) + "\n")
        print(f"escrito: {INDICE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
