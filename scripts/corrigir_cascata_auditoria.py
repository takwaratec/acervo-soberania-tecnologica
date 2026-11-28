#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Corrige a cascata: HASHES_RESPONSE e manifesto no MESMO commit.

Descoberta registrada: o gate 14 do verificador lê o HASHES_RESPONSE no `manifest_commit`.
Se o HR for commitado depois do manifesto, o que existe naquele commit é a versão anterior.
Como o sha256 de um arquivo independe do commit que o contém, dá para calcular o hash do
manifesto antes de commitá-lo — e é assim que as duas peças entram juntas.

Segundo achado: o campo que o gate 18 lê é `commit_alvo`, não `alvo_commit`.
"""
import hashlib
import json
import subprocess
from datetime import datetime, timezone

REPO = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica"
BRANCH = "hermes/cobre-plano-20261124"
MAN = "docs/analyses/cobre/AUDITORIA_SOL_COBRE_MANIFEST_R1.json"
HR = "docs/analyses/cobre/AUDITORIA_SOL_COBRE_HASHES_RESPONSE_R1.json"
PT = "ops/command-center/auditoria-atual/COBRE.json"


def git(*a):
    r = subprocess.run(["git", "-C", REPO] + list(a), capture_output=True)
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(a)}: {r.stderr.decode()[:300]}")
    return r.stdout


def main():
    raw = open(f"{REPO}/{MAN}", "rb").read()
    man = json.loads(raw)
    alvo = man["alvo_commit"]
    man_sha = hashlib.sha256(raw).hexdigest()
    print(f"manifesto: alvo {alvo[:12]}  sha256 {man_sha[:16]}…  {len(raw):,} B")

    resp = {
        "schema": "TAKWARATEC_R4_HASHES_RESPONSE_R1",
        "manifest_id": man["manifest_id"],
        "commit_alvo": alvo,
        "sha256_do_manifesto": man_sha,
        "bytes_do_manifesto": len(raw),
        "metodo": ("sha256 calculado sobre os bytes do próprio objeto; conferido depois com "
                   "`git show <commit>:<path>` pelo mesmo algoritmo."),
        "total_fontes": len(man["fontes"]),
        "fontes_sha256": {f["path"]: f["sha256"] for f in man["fontes"]},
    }
    open(f"{REPO}/{HR}", "w", encoding="utf-8").write(
        json.dumps(resp, ensure_ascii=False, indent=1) + "\n")

    # manifesto e resposta no mesmo commit
    git("add", MAN, HR)
    git("commit", "-q", "-m",
        f"auditoria(cobre): hashes response e manifesto no mesmo commit — alvo {alvo[:8]}, "
        f"{len(man['fontes'])} fontes")
    mc = git("rev-parse", "HEAD").decode().strip()
    hr_sha = hashlib.sha256(git("show", f"{mc}:{HR}")).hexdigest()
    print(f"commit {mc[:12]}  hr sha256 {hr_sha[:16]}…")

    pt = {
        "schema": "TAKWARATEC_R4_AUDIT_POINTER_R1",
        "frente": "COBRE",
        "manifest_id": man["manifest_id"],
        "status": "ABERTO",
        "manifest_branch": BRANCH,
        "manifest_commit": mc,
        "manifest_path": MAN,
        "sha256_do_manifesto": man_sha,
        "hashes_response_path": HR,
        "sha256_do_hashes_response": hr_sha,
        "alvo_commit": alvo,
        "atualizado_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "instrucao_ao_auditor": (
            "Leia o manifesto no manifest_commit e confira sha256_do_manifesto; leia o "
            "HASHES_RESPONSE no mesmo commit e confira sha256_do_hashes_response; então abra "
            "cada fonte no alvo_commit. O repositório é público."),
    }
    open(f"{REPO}/{PT}", "w", encoding="utf-8").write(
        json.dumps(pt, ensure_ascii=False, indent=1) + "\n")
    git("add", PT)
    git("commit", "-q", "-m", f"auditoria(cobre): ponteiro repinado — manifesto {mc[:8]}")
    print(f"ponteiro commit {git('rev-parse', 'HEAD').decode().strip()[:12]}")


if __name__ == "__main__":
    main()
