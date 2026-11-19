#!/usr/bin/env python3
"""Gera o inventário do pacote Sol a partir de um ref do git — derivado, não digitado.

Por que existe: o inventário anterior registrava um commit que já não era o HEAD, listava sete
arquivos que não existem mais e repetia uma entrada. Nada disso era declarado. Este gerador
deriva tudo do próprio git: bytes e sha256 saem de `git show`, o commit sai de `git rev-parse`,
e as remoções saem da diferença contra o inventário anterior — com o commit que removeu cada uma.

Regra de escopo (a mesma do inventário anterior, agora escrita):
  - `docs/analyses/bambu-estrutural/*.md`            (fichas da gaveta, nível 1)
  - `docs/analyses/bambu-estrutural/divulgacao/*.{md,html}`
  - `docs/analyses/bambu-estrutural/divulgacao/_geradores/**`  (qualquer extensão)

Exclusão declarada: este próprio gerador não entra na lista, porque o hash dele não existe antes
de ele ser gravado. A exclusão é explícita no campo `exclusao_declarada`.

O campo `commit` aponta para o commit cuja árvore foi descrita — por construção, o pai do commit
que grava este arquivo. Os arquivos listados não mudam entre um e outro; só o inventário entra.

Uso:  python3 gerar_inventario_pacote.py [--ref HEAD] [--json saida.json]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys

BASE = "docs/analyses/bambu-estrutural"
GERADORES = f"{BASE}/divulgacao/_geradores"
SAIDA = f"{GERADORES}/INVENTARIO_PACOTE_SOL.json"
EU = f"{GERADORES}/gerar_inventario_pacote.py"


def sh(*cmd: str) -> str:
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


def commits_de(path: str, ref: str, removido: bool) -> str:
    filtro = "--diff-filter=D" if removido else "--diff-filter=A"
    out = sh("git", "log", filtro, "--format=%h %s", ref, "--", path).splitlines()
    return out[0] if out else "nao localizado no historico deste ref"


def no_escopo(path: str) -> bool:
    if path in (EU, SAIDA):
        return False
    if path.startswith(GERADORES + "/"):
        return True
    if path.startswith(BASE + "/divulgacao/"):
        return path.endswith((".md", ".html"))
    if path.count("/") == BASE.count("/") + 1 and path.startswith(BASE + "/"):
        return path.endswith(".md")
    return False


def blobs(ref: str) -> list[str]:
    return [p for p in sh("git", "ls-tree", "-r", "--name-only", ref).splitlines() if p.strip()]


def hash_do(ref: str, path: str) -> tuple[int, str] | None:
    r = subprocess.run(["git", "show", f"{ref}:{path}"], capture_output=True)
    if r.returncode != 0:
        return None
    return len(r.stdout), hashlib.sha256(r.stdout).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", default="HEAD")
    ap.add_argument("--json", default=SAIDA)
    a = ap.parse_args()

    commit = sh("git", "rev-parse", a.ref).strip()
    if not commit:
        print("ref inválido", file=sys.stderr)
        return 2
    arvore = sh("git", "rev-parse", f"{a.ref}^{{tree}}").strip()

    atuais = []
    for p in blobs(a.ref):
        if not no_escopo(p):
            continue
        h = hash_do(a.ref, p)
        if h is None:
            continue
        atuais.append({"caminho": p, "bytes": h[0], "sha256": h[1]})

    # duplicatas não existem por construção (dict por caminho)
    anterior = []
    r = subprocess.run(["git", "show", f"{a.ref}:{SAIDA}"], capture_output=True, text=True)
    if r.returncode == 0:
        try:
            anterior = json.loads(r.stdout).get("arquivos", [])
        except json.JSONDecodeError:
            anterior = []

    atual_paths = {x["caminho"] for x in atuais}
    vistos, unicos = set(), []
    for x in anterior:
        # o inventario antigo gravava caminhos relativos a BASE; normalizo para repo-relative
        if not x["caminho"].startswith(BASE + "/"):
            x = dict(x, caminho=f"{BASE}/{x['caminho']}")
        if x["caminho"] in vistos:
            continue
        vistos.add(x["caminho"])
        unicos.append(x)

    removidos = [
        {"caminho": x["caminho"], "bytes": x["bytes"], "sha256": x["sha256"],
         "motivo": commits_de(x["caminho"], a.ref, True)}
        for x in unicos if x["caminho"] not in atual_paths
    ]
    adicionados = sorted(atual_paths - {x["caminho"] for x in unicos})
    alterados = sorted(
        x["caminho"] for x in unicos
        if x["caminho"] in atual_paths
        and x["sha256"] != next(y["sha256"] for y in atuais if y["caminho"] == x["caminho"])
    )

    doc = {
        "esquema": "inventario-pacote-sol/2",
        "escopo_declarado": [
            f"{BASE}/*.md",
            f"{BASE}/divulgacao/*.md",
            f"{BASE}/divulgacao/*.html",
            f"{GERADORES}/**",
        ],
        "exclusao_declarada": [
            f"{EU} — o hash do gerador nao existe antes de ele ser gravado",
            f"{SAIDA} — um inventario nao pode conter o proprio hash; os demais itens sao verificaveis",
        ],
        "commit": commit,
        "arvore": arvore,
        "commit_nota": "commit cuja arvore foi descrita; o commit que grava este arquivo "
                       "acrescenta apenas ele, sem alterar nenhum item abaixo",
        "total": len(atuais),
        "arquivos": atuais,
        "removidos": removidos,
        "adicionados_desde_o_inventario_anterior": adicionados,
        "alterados_desde_o_inventario_anterior": alterados,
        "duplicatas_corrigidas": len(anterior) - len(unicos),
    }
    with open(a.json, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=1)
        fh.write("\n")

    print(f"commit:    {commit[:8]}")
    print(f"arvore:    {arvore[:8]}")
    print(f"arquivos:  {len(atuais)}")
    print(f"removidos: {len(removidos)}")
    for x in removidos:
        print(f"   - {x['caminho']}  ({x['motivo'][:70]})")
    print(f"adicionados: {len(adicionados)}")
    print(f"alterados:   {len(alterados)}")
    print(f"duplicatas corrigidas: {doc['duplicatas_corrigidas']}")
    print(f"gravado em: {a.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
