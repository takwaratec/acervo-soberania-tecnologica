#!/usr/bin/env python3
"""Verifica o ponteiro de runtime: o que ele declara tem de ser o que se lê.

POR QUE ESTE ARQUIVO EXISTE
---------------------------
Em 27/11/2026 o ponteiro de runtime do R4 declarava `ledger_registry_sha256` e apontava para
`.../_worktrees/r4-transicao-20261102-r1/ops/.../ACTIVE_CONTRACTS_R4.json` — um worktree de frente,
parado na branch `hermes/r4-g2-promocao-20261108-r1`. Aquele caminho servia `8b0ce094` (1.109.716 B)
enquanto o ledger publicado em `main` era `7e4c3ebc` (1.110.310 B). A diferença era uma linha: a
promoção dos contratos CALC. O runtime lia um ledger que não tinha a promoção, e as três camadas de
autoridade concordavam — porque nenhuma delas verificava o CAMINHO, só o hash.

A regra que este gate mede: **o ponteiro de runtime nomeia estado publicado, não árvore de trabalho.**
Cópia de runtime é permitida — é o formato recomendado — desde que seja byte a byte igual ao blob do
commit declarado, por caminho declarado em `ledger_origem_path`. Arquivo dentro de worktree é FAIL: ali
o conteúdo muda de baixo do ponteiro sem que o ponteiro mude.

Segundo defeito medido: contrato declarado `AUSENTE` de documento não pode carregar `contract_path` nem
`contract_sha256` — caminho preenchido para arquivo inexistente é hash órfão ao contrário (`git show`
devolve vazio, `shasum` devolve `e3b0c442…`, os dois parecem sucesso).

Terceiro: cada contrato é medido no commit que ele mesmo declara (`contract_commit`), não no commit de
governança. Contrato R3 nasce em commit de submissão; medir contra a governança acusou 43 contratos
"sem arquivo" que existiam.

Uso:
    python3 scripts/verifica_ponteiro_runtime.py --repo <repo-de-governanca> \\
        --ponteiro ~/.hermes/delivery-loop-v2/r3-runtime-r1/r4-active-regency.json

    # quando só a medição local é possível (CI sem o repositório de governança)
    python3 scripts/verifica_ponteiro_runtime.py --sem-proveniencia

Exit 0 = PASS · 1 = FAIL (lista o que não fecha) · 2 = NAO_MEDIDO (não deu para medir tudo).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys

PONTEIRO_PADRAO = os.path.expanduser(
    "~/.hermes/delivery-loop-v2/r3-runtime-r1/r4-active-regency.json")


class MedicaoFalhou(Exception):
    """Não deu para medir — nunca é PASS."""


def _sha(arquivo):
    with open(arquivo, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def _git_bytes(*args, cwd=None):
    """`git show` sem passar por texto: strip() apaga o \\n final e o hash muda por um byte."""
    r = subprocess.run(["git", *args], cwd=cwd, capture_output=True)
    return r.returncode, r.stdout


def _git(*args, cwd=None):
    r = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    return r.returncode, r.stdout.strip(), r.stderr.strip()


def dentro_de_arvore_git(caminho):
    """O arquivo está dentro de um repositório git? Devolve o topo da árvore ou None."""
    d = os.path.dirname(os.path.abspath(caminho))
    while True:
        if os.path.exists(os.path.join(d, ".git")):
            return d
        pai = os.path.dirname(d)
        if pai == d:
            return None
        d = pai


def medir(ponteiro, repo=None, sem_proveniencia=False):
    """Devolve (achados, nao_medido, notas). Achado é (classe, texto); nota é medição não-defeito."""
    achados, nao_medido, notas = [], [], []

    if not os.path.isfile(ponteiro):
        raise MedicaoFalhou(f"ponteiro não encontrado: {ponteiro}")
    try:
        with open(ponteiro, encoding="utf-8") as fh:
            p = json.load(fh)
    except Exception as e:
        raise MedicaoFalhou(f"ponteiro ilegível: {e}")

    for campo in ("ledger_registry", "ledger_registry_sha256", "governance_commit"):
        if not p.get(campo):
            raise MedicaoFalhou(f"ponteiro não declara '{campo}': nada a medir")

    led = p["ledger_registry"]
    decl = p["ledger_registry_sha256"]
    gov = p["governance_commit"]

    if not os.path.isfile(led):
        achados.append(("PONTEIRO_QUEBRADO", f"ledger declarado não existe: {led}"))
        return achados, nao_medido, notas

    lido = _sha(led)
    if lido != decl:
        achados.append(("HASH_DIVERGENTE", f"declarado {decl[:16]} != lido {lido[:16]} em {led}"))

    topo = dentro_de_arvore_git(led)
    if topo:
        achados.append(("PONTEIRO_EM_ARVORE_DE_TRABALHO",
                        f"ledger mora dentro do repositório git '{topo}': o conteúdo muda com "
                        f"checkout e o ponteiro passa a declarar hash de outro arquivo"))

    try:
        with open(led, "rb") as fh:
            L = json.loads(fh.read().decode("utf-8"))
    except Exception as e:
        achados.append(("LEDGER_ILEGIVEL", f"{led}: {e}"))
        return achados, nao_medido, notas

    contratos = L.get("CONTRACTS") or []
    total = (L.get("COUNTS") or {}).get("TOTAL")
    if total is None:
        achados.append(("LEDGER_SEM_COUNTS", "ledger não declara COUNTS.TOTAL"))
    elif total != len(contratos):
        achados.append(("COUNTS_NAO_FECHA", f"COUNTS.TOTAL={total} mas há {len(contratos)} entradas"))

    ids = [c.get("id") for c in contratos]
    dup = sorted({i for i in ids if ids.count(i) > 1})
    if dup:
        achados.append(("ID_DUPLICADO", f"ids repetidos: {', '.join(dup)}"))

    for c in contratos:
        if c.get("contrato_documento") == "AUSENTE" and (c.get("contract_sha256") or c.get("contract_path")):
            achados.append(("ENTRADA_ORFA",
                            f"{c.get('id')}: documento declarado AUSENTE mas carrega "
                            f"contract_path/contract_sha256 — caminho sem arquivo é hash órfão ao "
                            f"contrário"))

    if sem_proveniencia or not repo:
        nao_medido.append("proveniencia (governance_commit contém o ledger e os contratos): exige --repo")
        return achados, nao_medido, notas

    rc, _, err = _git("cat-file", "-e", f"{gov}^{{commit}}", cwd=repo)
    if rc != 0:
        achados.append(("COMMIT_DECLARADO_NAO_EXISTE",
                        f"governance_commit {gov[:8]} não abre em {repo}: {err}"))
        return achados, nao_medido, notas

    if dentro_de_arvore_git(led):
        origem = os.path.relpath(os.path.abspath(led), repo)
    else:
        origem = p.get("ledger_origem_path")
        if not origem:
            nao_medido.append(
                "proveniencia do ledger: cópia fora do repo sem 'ledger_origem_path' — não há caminho "
                "no commit para comparar")
            origem = None

    if origem:
        rc, _, _ = _git("cat-file", "-e", f"{gov}:{origem}", cwd=repo)
        if rc != 0:
            achados.append(("LEDGER_FORA_DO_COMMIT",
                            f"o ponteiro declara {gov[:8]} mas '{origem}' não existe nesse commit"))
        else:
            rc, blob = _git_bytes("show", f"{gov}:{origem}", cwd=repo)
            if rc == 0:
                h_blob = hashlib.sha256(blob).hexdigest()
                if h_blob != lido:
                    achados.append(("COPIA_NAO_E_O_PUBLICADO",
                                    f"cópia de runtime {lido[:16]} != blob em {gov[:8]} {h_blob[:16]}"))

    sem_commit = []
    for c in contratos:
        cp = c.get("contract_path")
        if not cp:
            continue
        cc = c.get("contract_commit")
        base = cc or gov
        if not cc:
            # sem `contract_commit` o hash declarado é o do ato de assinatura, não o do arquivo de
            # hoje: medir contra a governança acusa divergência que não é defeito (o CUTOVER de
            # 08/11 foi editado em 16/11). Sem o commit da assinatura não se prova o hash.
            sem_commit.append(f"{c.get('id')} (sem contract_commit)")
            continue
        rc, _, _ = _git("cat-file", "-e", f"{cc}^{{commit}}", cwd=repo)
        if rc != 0:
            sem_commit.append(f"{c.get('id')} (commit {cc[:8]} ausente)")
            continue
        rc, _, _ = _git("cat-file", "-e", f"{base}:{cp}", cwd=repo)
        if rc != 0:
            achados.append(("CONTRATO_SEM_ARQUIVO", f"{c.get('id')}: '{cp}' não existe em {base[:8]}"))
            continue
        esperado = c.get("contract_sha256")
        if esperado:
            rc, blob = _git_bytes("show", f"{base}:{cp}", cwd=repo)
            rc2, blob_sha, _ = _git("rev-parse", f"{base}:{cp}", cwd=repo)
            if rc == 0:
                h = hashlib.sha256(blob).hexdigest()
                if esperado == blob_sha:
                    # duas convenções convivem no ledger: sha256 do conteúdo e blob sha do git.
                    # Aceitar as duas é honesto; fingir que só existe uma reprovaria 2 contratos
                    # corretos.
                    notas.append(f"{c.get('id')} declara blob sha em contract_sha256 "
                                 f"({blob_sha[:16]}) — conferido como blob, não como conteúdo")
                elif h != esperado:
                    achados.append(("CONTRATO_HASH_DIVERGENTE",
                                    f"{c.get('id')}: declarado {esperado[:16]} != arquivo {h[:16]} "
                                    f"(nem blob {blob_sha[:16]}) em {base[:8]}"))

    if sem_commit:
        nao_medido.append(
            f"{len(sem_commit)} contrato(s) com contract_commit ausente deste repositório — sem o "
            f"commit onde nasceram não se prova o documento: {', '.join(sem_commit[:5])}"
            + (" …" if len(sem_commit) > 5 else ""))

    return achados, nao_medido, notas


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--ponteiro", default=PONTEIRO_PADRAO)
    ap.add_argument("--repo", help="repositório de governança onde os commits declarados vivem")
    ap.add_argument("--sem-proveniencia", action="store_true",
                    help="mede só o que é local; a proveniência sai NAO_MEDIDO, nunca PASS")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)

    try:
        achados, nao_medido, notas = medir(a.ponteiro, a.repo, a.sem_proveniencia)
    except MedicaoFalhou as e:
        print(f"NAO_MEDIDO {e}")
        return 2

    for classe, texto in achados:
        print(f"FAIL {classe} — {texto}")
    for n in nao_medido:
        print(f"NAO_MEDIDO {n}")
    for n in notas:
        print(f"NOTA {n}")

    veredito = "FAIL" if achados else ("PASS" if not nao_medido else "PARCIAL")

    if a.json:
        print(json.dumps({"ponteiro": a.ponteiro, "achados": achados,
                          "nao_medido": nao_medido, "notas": notas, "veredito": veredito},
                         ensure_ascii=False, indent=1))
    else:
        print(f"VEREDITO={veredito} · {len(achados)} achado(s) · {len(nao_medido)} nao medido(s)")

    return 1 if achados else (0 if veredito == "PASS" else 2)


if __name__ == "__main__":
    sys.exit(main())
