#!/usr/bin/env python3
"""SELOS.md — índice dos selos da frente do cobre.

A árvore carrega UM par (manifesto + resposta de hashes) para o alvo vigente.
O payload dos selos anteriores vive no git, onde já estava; aqui fica o índice:
alvo, sha256 das duas peças, data e commit em que o par completo existe.

Rodar depois do reselo. Lê tudo do histórico — não depende dos arquivos no disco.
"""
import os
import re
import subprocess
import sys
import hashlib

REPO = os.environ.get("COBRE_REPO", ".")
DIR = "docs/analyses/cobre"
SAIDA = f"{DIR}/SELOS.md"
MSG = "auditoria(cobre): manifesto e hashes do alvo"


def _git(*a):
    r = subprocess.run(["git", "-C", REPO, *a], capture_output=True)
    if r.returncode != 0:
        raise SystemExit(f"git {' '.join(a)} falhou: {r.stderr.decode()[:300]}")
    return r.stdout


def git_txt(*a) -> str:
    return _git(*a).decode()


def git_bin(*a) -> bytes:
    return _git(*a)


def main():
    log = git_txt("log", "--format=%H|%cI|%s", "--", DIR).splitlines()
    selos = []
    vistos = set()
    for linha in log:
        partes = linha.split("|", 2)
        if len(partes) < 3:
            continue
        commit, data, assunto = partes
        if not assunto.startswith(MSG):
            continue
        m = re.search(r"alvo ([0-9a-f]{8})", assunto)
        if not m:
            continue
        a8 = m.group(1)
        if a8 in vistos:
            continue
        mp = f"{DIR}/AUDITORIA_SOL_COBRE_MANIFEST_R1_{a8}.json"
        hp = f"{DIR}/AUDITORIA_SOL_COBRE_HASHES_RESPONSE_R1_{a8}.json"
        try:
            man = git_bin("show", f"{commit}:{mp}")
            hrs = git_bin("show", f"{commit}:{hp}")
        except SystemExit:
            continue
        vistos.add(a8)
        selos.append({
            "alvo": a8,
            "man": hashlib.sha256(man).hexdigest(),
            "hr": hashlib.sha256(hrs).hexdigest(),
            "data": data,
            "commit": commit,
        })

    linhas = [
        "---",
        "schema: ACERVO_INDICE_R1",
        "gaveta: cobre",
        "frente: COBRE",
        "titulo: \"Selos da frente do cobre\"",
        "tipo_documental: indice",
        "estado_documental: em-revisao-documental",
        "homologacao_automatica: false",
        "responsavel_curadoria: Fabio Takwara",
        "assistencia_documental: agente de IA, sujeito a revisao humana",
        "---",
        "",
        "# Selos da frente do cobre",
        "",
        "A árvore carrega **um** par: `AUDITORIA_SOL_COBRE_MANIFEST_R1_<alvo>.json` e",
        "`AUDITORIA_SOL_COBRE_HASHES_RESPONSE_R1_<alvo>.json`, para o alvo vigente.",
        "Os pares anteriores foram retirados da árvore e continuam no git — o commit de cada",
        "um está na tabela. `git show <commit>:<arquivo>` recupera o byte, e o sha256 abaixo",
        "confere se o que veio é o mesmo.",
        "",
        "| alvo_commit | sha256 do manifesto | sha256 da resposta | data | commit do par |",
        "|---|---|---|---|---|",
    ]
    for s in selos:
        linhas.append(f"| `{s['alvo']}` | `{s['man'][:16]}…` | `{s['hr'][:16]}…` | "
                      f"{s['data'][:19]}Z | `{s['commit'][:12]}` |")
    linhas += [
        "",
        f"Total de selos indexados: **{len(selos)}**.",
        "",
        "Gerado por `scripts/gerar_selos_cobre.py` a partir do histórico; não editar à mão.",
    ]
    open(os.path.join(REPO, SAIDA), "w", encoding="utf-8").write("\n".join(linhas) + "\n")
    print(f"SELOS: {SAIDA} — {len(selos)} selos indexados")


if __name__ == "__main__":
    main()
