#!/usr/bin/env python3
"""Manifesto do pacote de auditoria publicado + verificador que morde.

Entrega DOIS objetos, e o segundo existe para o primeiro nao ser decoracao:
  PACOTE_AUDITORIA.json  — inventario com sha256 de cada arquivo publicado (exclui a si
                           mesmo e ao gerador, por impossibilidade declarada)
  conferir_pacote.py     — verificador que o SOL roda: recalcula sha256 de cada entrada,
                           devolve exit 0 so se todas conferirem, exit 1 nomeando o arquivo,
                           exit 2 quando nao conseguiu medir (pacote ausente).
O commit vai por `rev-parse` no instante da geracao (nunca digitado). O verificador le do
commit que o manifesto declara, e cai para o disco quando o commit nao estiver disponivel.
"""
import hashlib
import json
import os
import subprocess

ACERVO = os.path.expanduser("~/Documents/GitHub/acervo-soberania-tecnologica")
DIR = os.path.join(ACERVO, "docs/analyses/bambusc-catalogo-20261119")
MANIF = "PACOTE_AUDITORIA.json"
GERADOR = "gerar_pacote.py"
VERIF = "conferir_pacote.py"

EXCLUIDOS = {
    MANIF: "declara o sha256 dos outros arquivos; o proprio sha nao existe antes de gravar (impossibilidade de construcao)",
    GERADOR: "produz o manifesto; excluido declaradamente para que o pacote possa ser regerado",
}


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def rev(spec):
    return subprocess.run(["git", "-C", ACERVO, "rev-parse", spec],
                          capture_output=True, text=True).stdout.strip()


itens = []
for nome in sorted(os.listdir(DIR)):
    p = os.path.join(DIR, nome)
    if not os.path.isfile(p) or nome in EXCLUIDOS:
        continue
    itens.append({"path": f"docs/analyses/bambusc-catalogo-20261119/{nome}",
                  "sha256": sha(p), "bytes": os.path.getsize(p)})

man = {
    "schema": "TAKWARATEC/PACOTE_DE_AUDITORIA/1",
    "frente": "BAMBU-BAMBUSC",
    "task": "BAMBU-BAMBUSC-CATALOGO-20261119-R1",
    "repo": "takwaratec/acervo-soberania-tecnologica",
    "branch": "bambusc/catalogo-20261119-r1",
    "commit_na_geracao": rev("HEAD"),
    "arvore_na_geracao": rev("HEAD^{tree}"),
    "gerado_em": "2026-11-19",
    "exclusao_declarada": EXCLUIDOS,
    "convencao": ("o manifesto descreve os arquivos irmaos do diretorio; quando o commit "
                  "declarado ja contem esta versao, a conferencia fecha 100%. Regere e "
                  "recommite sempre que um arquivo do diretorio mudar."),
    "como_conferir": ("python3 docs/analyses/bambusc-catalogo-20261119/conferir_pacote.py "
                      "--repo . [--commit <sha>]"),
    "inventario": itens,
}
json.dump(man, open(os.path.join(DIR, MANIF), "w"), ensure_ascii=False, indent=1)
print(f"manifesto: {len(itens)} arquivos")
for i in itens:
    print(f"  {i['sha256'][:12]}  {i['bytes']:>7}  {i['path'].split('/')[-1]}")
print(f"commit na geracao: {man['commit_na_geracao'][:12]} (arvore {man['arvore_na_geracao'][:12]})")
