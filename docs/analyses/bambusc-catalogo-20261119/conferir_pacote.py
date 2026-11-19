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

    # orfao: arquivo no diretorio que o manifesto NAO declara. Gate de completude que
    # enumera so a lista que o autor escreveu aprova o proprio esquecimento — o orfao
    # nao entra no denominador e o placar sai cheio com o buraco intacto.
    declarados = {it["path"] for it in inv}
    dir_rel = os.path.dirname(REL)
    ignorar = set((man.get("exclusao_declarada") or {}).keys())
    orfaos = []
    if os.path.isdir(os.path.join(a.repo, dir_rel)):
        for raiz, _, arqs in os.walk(os.path.join(a.repo, dir_rel)):
            for arq in arqs:
                if arq.startswith("."):
                    continue
                caminho = os.path.relpath(os.path.join(raiz, arq), a.repo).replace(os.sep, "/")
                if caminho in declarados:
                    continue
                if os.path.basename(caminho) in ignorar:
                    continue
                orfaos.append(caminho)
    for o in sorted(orfaos):
        problemas.append(f"ORFAO {o}: existe no diretorio e nao esta no manifesto")

    print(f"manifesto: {REL}")
    print(f"MEDIDO em: {origem}   <-- os sha256 abaixo foram lidos daqui")
    print(f"DECLARADO no manifesto: {man.get('commit_na_geracao')}   <-- rotulo escrito pelo gerador, "
          f"nao commit em que se mediu")
    if a.commit and a.commit != man.get("commit_na_geracao"):
        print(f"ATENCAO: o commit medido ({a.commit[:12]}) difere do declarado no manifesto "
              f"({str(man.get('commit_na_geracao'))[:12]}) — os dois numeros descrevem coisas diferentes")
    print(f"inventario: {len(inv)} entradas   conferidas: "
          f"{len([i for i in inv if not any(i['path'] in p for p in problemas)])}   orfaos: {len(orfaos)}")
    for p in problemas:
        print(f"  PROBLEMA {p}")
    return 0 if not problemas else 1


if __name__ == "__main__":
    sys.exit(main())
