#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Normaliza o front matter dos documentos do cobre conforme GOVERNANCA_DOCUMENTAL.md.

Só toca arquivos que entram nesta PR. O mapeamento é declarado e explícito — metadado inventado
em silêncio é o mesmo defeito que o gate A2 cobra no texto.

Campos que o validador exige em todo documento:
    tipo_documental · estado_documental · responsavel_curadoria

Estados legados desta gaveta → canônicos:
    homologado-internamente → homologado-documentalmente
    superado                → historico
"""
import os
import re
import subprocess
import sys

REPO = os.environ.get("COBRE_REPO", os.getcwd())
CURADOR = "Fabio F. Resck"

# tipo_documental por padrão de caminho — declarado, na ordem em que casa
REGRAS_TIPO = [
    (r"/fichas/ficha-", "ficha-cientifica"),
    (r"/leitura-integral/.*\.(leitura|indice)\.md$", "instrumento-de-pesquisa"),
    (r"/leitura-integral/LEITURA_INTEGRAL_SINTESE\.md$", "sintese-critica"),
    (r"/fontes/md/", "fonte-primaria-privada"),
    # extratos com marcador de página: o arquivo é o INSTRUMENTO de leitura do documento (o PDF
    # custodiado com sha256 está ao lado), não o documento em si.
    (r"/fontes/s11[cd]/", "instrumento-de-pesquisa"),
    (r"/fontes/.*MANIFEST.*\.md$", "instrumento-de-pesquisa"),
    (r"/00-artigo-|/99-artigo-", "ensaio-tecnico"),
    (r"/0\d-plano-|/99-plano-|/01-plano-de-pesquisa", "instrumento-de-pesquisa"),
    (r"/0\d-resultados-|/05-resultados", "sintese-critica"),
    (r"/mtcc/", "sintese-critica"),
    (r"/AUDITORIA_|/COMECE_AQUI", "documento-institucional"),
    (r"/00-mapa-reprocessamento\.md$", "instrumento-de-pesquisa"),
]

ESTADOS_OK = {
    "recebido", "identificacao-pendente", "protegido-privado", "duplicata-fonte-auxiliar",
    "extracao-preliminar", "em-revisao-documental", "homologado-documentalmente",
    "visao-autoral", "historico", "quarentena", "retirado-da-publicacao",
}
MAPA_ESTADO = {
    "homologado-internamente": "homologado-documentalmente",
    "superado": "historico",
}


def destino_tipo(caminho):
    for padrao, tipo in REGRAS_TIPO:
        if re.search(padrao, caminho):
            return tipo
    return None


def separar(txt):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", txt, re.DOTALL)
    if not m:
        return None, txt
    return m.group(1), txt[m.end():]


def main():
    arquivos = subprocess.run(["git", "diff", "--name-only", "origin/main"], cwd=REPO,
                              capture_output=True, text=True).stdout.split()
    alvos = [a for a in arquivos if a.startswith("docs/") and a.endswith(".md")]
    tocados, sem_tipo = [], []
    for rel in alvos:
        p = os.path.join(REPO, rel)
        if not os.path.exists(p):
            continue
        txt = open(p, encoding="utf-8").read()
        fm, corpo = separar(txt)
        linhas = (fm.splitlines() if fm else [])
        dados = {}
        for l in linhas:
            m = re.match(r"^([a-z_]+):\s*(.*)$", l)
            if m:
                dados[m.group(1)] = m.group(2).strip().strip('"')

        mudou = []
        # tipo_documental
        if not dados.get("tipo_documental"):
            t = destino_tipo(rel)
            if t:
                linhas.append(f"tipo_documental: {t}")
                mudou.append(f"tipo_documental={t}")
            else:
                sem_tipo.append(rel)
        # estado_documental
        est = dados.get("estado_documental")
        if not est:
            linhas.append("estado_documental: em-revisao-documental")
            mudou.append("estado_documental=em-revisao-documental")
        elif est not in ESTADOS_OK:
            novo = MAPA_ESTADO.get(est)
            if novo:
                linhas = [f"estado_documental: {novo}" if l.startswith("estado_documental:") else l
                          for l in linhas]
                mudou.append(f"estado_documental {est}->{novo}")
        # responsavel_curadoria
        if not dados.get("responsavel_curadoria"):
            linhas.append(f"responsavel_curadoria: {CURADOR}")
            mudou.append("responsavel_curadoria")

        if not mudou:
            continue
        novo_txt = "---\n" + "\n".join(linhas) + "\n---\n" + corpo
        open(p, "w", encoding="utf-8").write(novo_txt)
        tocados.append((rel, mudou))

    print(f"arquivos ajustados: {len(tocados)}")
    for rel, m in tocados:
        print(f"  {rel}\n      {' · '.join(m)}")
    if sem_tipo:
        print(f"\nSEM TIPO INFERÍVEL ({len(sem_tipo)}) — precisam de decisão:")
        for a in sem_tipo:
            print("  ", a)


if __name__ == "__main__":
    sys.exit(main())
