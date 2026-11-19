#!/usr/bin/env python3
"""Verificador do PACOTE_AUDITORIA.json — roda no clone do auditor, sem credencial.

Tres desfechos, e nenhum deles colapsa no outro:
  exit 0  todas as entradas conferem
  exit 1  divergencia: nomeia o arquivo e o sha esperado/medido
  exit 2  NAO_VERIFICADO: manifesto ausente ou commit declarado nao resolvivel no clone

Regra que o script aplica a si mesmo: hash se calcula sobre BYTES do objeto (nunca sobre
string recortada), e leitura que falhou nao gera hash — arquivo ausente e ausencia medida,
nao sha do vazio (e3b0c442...).

Uso:
    python3 conferir_pacote.py --repo .
    python3 conferir_pacote.py --repo . --commit <sha>     # mede no commit declarado
    CONV_WORKTREE=1 python3 conferir_pacote.py --repo .    # forca leitura do disco
"""
import argparse
import hashlib
import json
import os
import subprocess
import sys

VAZIO = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
REL = "docs/analyses/bambusc-catalogo-20261119/PACOTE_AUDITORIA.json"


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def git(repo, *args, binary=False):
    p = subprocess.run(["git", "-C", repo, *args], capture_output=True)
    if p.returncode != 0:
        return None
    return p.stdout if binary else p.stdout.decode("utf-8", "replace").strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    ap.add_argument("--commit", default=None)
    a = ap.parse_args()

    man_path = os.path.join(a.repo, REL)
    origem = "disco"
    if os.environ.get("CONV_WORKTREE") != "1" and a.commit is None:
        # sem --commit, usa o commit que o manifesto declara
        if os.path.exists(man_path):
            try:
                a.commit = json.load(open(man_path)).get("commit_na_geracao")
            except Exception:
                a.commit = None

    man_bytes = None
    if a.commit and os.environ.get("CONV_WORKTREE") != "1":
        man_bytes = git(a.repo, "cat-file", "blob", f"{a.commit}:{REL}", binary=True)
        if man_bytes is not None:
            origem = f"commit {a.commit[:12]}"
    if man_bytes is None:
        if not os.path.exists(man_path):
            print(f"NAO_VERIFICADO: {REL} ausente"
                  + (f" e commit {a.commit[:12]} nao resolve neste clone" if a.commit else ""))
            return 2
        man_bytes = open(man_path, "rb").read()
        origem = "disco (fallback)"

    try:
        man = json.loads(man_bytes)
    except Exception as e:
        print(f"NAO_VERIFICADO: manifesto ilegivel: {e}")
        return 2

    inv = man.get("inventario") or []
    if not inv:
        print("NAO_VERIFICADO: inventario vazio — colecao vazia nao e 'nada a conferir'")
        return 2

    problemas = []
    for it in inv:
        cam = it["path"]
        esperado = it["sha256"]
        dados = None
        if a.commit and os.environ.get("CONV_WORKTREE") != "1":
            dados = git(a.repo, "cat-file", "blob", f"{a.commit}:{cam}", binary=True)
        if dados is None:
            p = os.path.join(a.repo, cam)
            if os.path.exists(p):
                dados = open(p, "rb").read()
        if dados is None:
            problemas.append(f"AUSENTE {cam}")
            continue
        medido = sha_bytes(dados)
        if medido == VAZIO:
            problemas.append(f"VAZIO {cam} (sha do vazio nao e prova)")
        elif medido != esperado:
            problemas.append(f"DIVERGE {cam}: esperado {esperado[:16]}… medido {medido[:16]}…")
        if "bytes" in it and len(dados) != it["bytes"]:
            problemas.append(f"TAMANHO {cam}: manifesto {it['bytes']} B, disco {len(dados)} B")

    print(f"manifesto: {REL}")
    print(f"origem da leitura: {origem}")
    print(f"commit declarado: {man.get('commit_na_geracao')}")
    print(f"entradas: {len(inv)}  conferidas: {len(inv) - len([p for p in problemas if p.startswith(('AUSENTE','DIVERGE','VAZIO'))])}")
    for p in problemas:
        print(f"  PROBLEMA {p}")
    return 0 if not problemas else 1


if __name__ == "__main__":
    sys.exit(main())
