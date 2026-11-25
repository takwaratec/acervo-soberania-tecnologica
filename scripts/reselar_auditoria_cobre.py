#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Resela o pacote de auditoria COBRE sobre um alvo novo.

Regra da casa, que este script respeita na ordem: material -> manifesto -> HASHES_RESPONSE
-> ponteiro. O manifesto não pode conter o hash do commit que o publica, e por isso cada
peça ganha o seu próprio commit, e todo hash é lido do commit (`git show`), nunca do disco.

Uso: reselar_auditoria_cobre.py <alvo_commit_40hex>
"""
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone

REPO = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica"
BRANCH = "hermes/cobre-plano-20261124"
MAN = "docs/analyses/cobre/AUDITORIA_SOL_COBRE_MANIFEST_R1.json"
HR = "docs/analyses/cobre/AUDITORIA_SOL_COBRE_HASHES_RESPONSE_R1.json"
PT = "ops/command-center/auditoria-atual/COBRE.json"

# fontes novas desta rodada (S11-c)
NOVAS = [
    ("docs/analyses/cobre/fichas/ficha-pi292-89-registro-preservativos-madeira.md",
     "ficha 7 — a norma-mãe: registro obrigatório e art. 20 (competência de fiscalização)"),
    ("docs/analyses/cobre/fichas/ficha-pn151-97-ibama-risco-ambiental.md",
     "ficha 8 — o registro condicionado à determinação do risco ambiental"),
    ("docs/analyses/cobre/fichas/ficha-iema-es-nt01-2023-preservacao-madeira.md",
     "ficha 9 — o regulador do ES: «não há proibição no Brasil» e a falta de dados do CCB"),
    ("docs/analyses/cobre/fichas/ficha-abpm-fg4mad-destinacao-residuo-madeira-tratada.md",
     "ficha 10 — a própria cadeia: resíduo tratado não pode queima em fogão nem a céu aberto"),
    ("docs/analyses/cobre/fichas/ficha-ufsm-2025-cca-moiroes-contaminacao-solo.md",
     "ficha 11 — 880 dias de campo: As na madeira −55,0%, no solo +129,2%"),
    ("docs/analyses/cobre/fontes/s11c/1989_pi292_preservativos_registro.pdf",
     "ref 17 — Portaria Interministerial 292/89, texto integral (4 p.)"),
    ("docs/analyses/cobre/fontes/s11c/1997_pn151_ibama_registro_risco_ambiental.pdf",
     "ref 18 — Portaria Normativa Ibama 151/97 (DOU, OCR degradado)"),
    ("docs/analyses/cobre/fontes/s11c/2023_iema_es_nt01_preservacao_madeira.pdf",
     "ref 19 — NT 01/2023 do Iema-ES (36 p.)"),
    ("docs/analyses/cobre/fontes/s11c/2016_abpm_fg4mad_destinacao_residuos_madeira_tratada.pdf",
     "ref 20 — ABPM/FG4mad, destinação de resíduo de madeira tratada (21 p.)"),
    ("docs/analyses/cobre/fontes/s11c/2025_ufsm_ciencia_florestal_cca_moiroes_solo.pdf",
     "ref 21 — Ciência Florestal v.35 e86024 (16 p.)"),
    ("docs/analyses/cobre/fontes/s11c/MANIFEST_FONTES_S11C.json",
     "manifesto da custódia S11-c, com as duas pendências declaradas"),
]


def git(*a, check=True):
    r = subprocess.run(["git", "-C", REPO] + list(a), capture_output=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"git {' '.join(a)}: {r.stderr.decode()[:300]}")
    return r


def blob_sha(commit, path):
    r = git("show", f"{commit}:{path}")
    return hashlib.sha256(r.stdout).hexdigest(), len(r.stdout)


def main():
    alvo = sys.argv[1]
    assert len(alvo) == 40, "alvo precisa ser sha de 40 hex"
    git("cat-file", "-e", f"{alvo}^{{commit}}")

    man = json.load(open(f"{REPO}/{MAN}", encoding="utf-8"))

    # 1) reconferir cada fonte existente no alvo novo
    novas, vistas = 0, set()
    for f in man["fontes"]:
        h, n = blob_sha(alvo, f["path"])
        f["sha256"], f["bytes"] = h, n
        vistas.add(f["path"])

    # 2) acrescentar as fontes desta rodada
    for path, papel in NOVAS:
        if path in vistas:
            continue
        h, n = blob_sha(alvo, path)
        man["fontes"].append({"path": path, "sha256": h, "bytes": n, "papel": papel})
        novas += 1

    # 3) metadados
    man["alvo_commit"] = alvo
    man["gerado_utc"] = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    man["total_fontes"] = len(man["fontes"])
    man["alvo_nota"] = ("alvo_commit é o último commit que mudou os bytes auditados (artigo, "
                        "manuscrito, 11 fichas, fontes). Todos os sha256 de fontes[] foram lidos "
                        "do próprio commit, com `git show <alvo>:<path>`.")
    man["pergunta"] = ("As afirmações do artigo e das 11 fichas são fielmente sustentadas pelas "
                       "21 fontes custodiadas neste repositório, e o que não está medido está "
                       "declarado como tal?")
    obj = man.get("objeto", {})
    for k in list(obj):
        if "ficha" in k:
            obj[k] = obj[k] if isinstance(obj[k], (int, str)) else obj[k]
    man["objeto"] = obj
    ed = man.get("estado_declarado", {})
    ed["fichas"] = f"{len([f for f in man['fontes'] if '/fichas/' in f['path']])} fichas, todas homologado-internamente, autoridade FABIO, reversíveis"
    ed["artigo"] = ("peça corrida (molde do boro, 13 seções), peça em abas e manuscrito único de "
                    "ponta a ponta com 21 referências ABNT comentadas")
    man["estado_declarado"] = ed
    if "parte_1_perguntas" in man:
        # idempotente: rodar o reselar duas vezes não pode duplicar a pergunta
        _existentes = {q.get("id") for q in man["parte_1_perguntas"]}
        _novas = []
        _novas.append({
            "id": "Q9",
            "pergunta": ("O capítulo 9 afirma que a norma federal de preservação de madeira (PI 292/89) "
                         "existe, nomeia o Ibama como fiscalizador (art. 20) e NÃO trata da destinação "
                         "final do resíduo. Isso é sustentado pelo texto integral da Portaria, e a "
                         "palavra «resíduo» está de fato ausente dela?"),
            "arquivo": "docs/analyses/cobre/o-cobre-no-bambu-corrido.html",
            "ancora": "seção 9 — A norma existe — e ela não chega ao quintal",
            "fonte": "docs/analyses/cobre/fontes/s11c/1989_pi292_preservativos_registro.pdf",
        })
        _novas.append({
            "id": "Q10",
            "pergunta": ("A distinção «a madeira tem norma que não se cumpre; o bambu não tem norma a "
                         "cumprir» é sustentada pelas fontes custodiadas, e o capítulo declara "
                         "explicitamente que não há caso brasileiro documentado de intoxicação por "
                         "queimar madeira tratada em fogão doméstico?"),
            "arquivo": "docs/analyses/cobre/o-cobre-no-bambu-corrido.html",
            "ancora": "seção 9 — «O que não se mediu — e por que isso é resultado»",
            "fonte": "docs/analyses/cobre/fontes/s11c/2016_abpm_fg4mad_destinacao_residuos_madeira_tratada.pdf",
        })

        man["parte_1_perguntas"].extend(q for q in _novas if q["id"] not in _existentes)

    open(f"{REPO}/{MAN}", "w", encoding="utf-8").write(
        json.dumps(man, ensure_ascii=False, indent=1) + "\n")
    print(f"MANIFESTO reescrito: {man['total_fontes']} fontes ({novas} novas) em alvo {alvo[:12]}")

    # 4) commit do manifesto
    git("add", MAN)
    git("commit", "-q", "-m",
        f"auditoria(cobre): manifesto reselado no alvo {alvo[:8]} — 21 refs, 11 fichas, {man['total_fontes']} fontes")
    man_commit = git("rev-parse", "HEAD").stdout.decode().strip()
    man_sha, man_bytes = blob_sha(man_commit, MAN)
    print(f"MANIFESTO commit {man_commit[:12]}  sha256 {man_sha[:16]}…  {man_bytes:,} B")

    # 5) HASHES_RESPONSE
    resp = {
        "schema": "TAKWARATEC_R4_HASHES_RESPONSE_R1",
        "manifest_id": man["manifest_id"],
        "alvo_commit": alvo,
        "manifest_commit": man_commit,
        "sha256_do_manifesto": man_sha,
        "bytes_do_manifesto": man_bytes,
        "metodo": ("Cada sha256 foi calculado sobre os bytes servidos por `git show "
                   "<commit>:<path>`, no próprio repositório, e não sobre cópia local."),
        "total_fontes": man["total_fontes"],
        "fontes_sha256": {f["path"]: f["sha256"] for f in man["fontes"]},
    }
    open(f"{REPO}/{HR}", "w", encoding="utf-8").write(
        json.dumps(resp, ensure_ascii=False, indent=1) + "\n")
    git("add", HR)
    git("commit", "-q", "-m", f"auditoria(cobre): HASHES_RESPONSE do manifesto {man_sha[:12]}")
    hr_commit = git("rev-parse", "HEAD").stdout.decode().strip()
    hr_sha, _ = blob_sha(hr_commit, HR)
    print(f"HASHES_RESPONSE commit {hr_commit[:12]}  sha256 {hr_sha[:16]}…")

    # 6) ponteiro
    pt = {
        "schema": "TAKWARATEC_R4_AUDIT_POINTER_R1",
        "frente": "COBRE",
        "manifest_id": man["manifest_id"],
        "status": "ABERTO",
        "manifest_branch": BRANCH,
        "manifest_commit": man_commit,
        "manifest_path": MAN,
        "sha256_do_manifesto": man_sha,
        "hashes_response_path": HR,
        "sha256_do_hashes_response": hr_sha,
        "hashes_response_commit": hr_commit,
        "alvo_commit": alvo,
        "atualizado_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "instrucao_ao_auditor": (
            "Leia o manifesto no manifest_commit, confira sha256_do_manifesto, depois "
            "HASHES_RESPONSE, e só então as fontes no alvo_commit. O repositório é público."),
    }
    open(f"{REPO}/{PT}", "w", encoding="utf-8").write(
        json.dumps(pt, ensure_ascii=False, indent=1) + "\n")
    git("add", PT)
    git("commit", "-q", "-m", f"auditoria(cobre): ponteiro repinado — alvo {alvo[:8]}, manifesto {man_sha[:12]}")
    print(f"PONTEIRO commit {git('rev-parse', 'HEAD').stdout.decode().strip()[:12]}")
    print("\nCASCATA COMPLETA. Falta: git push e a verificação dos 23 gates.")


if __name__ == "__main__":
    main()
