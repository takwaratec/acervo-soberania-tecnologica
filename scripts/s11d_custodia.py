#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Custódia S11-d — a instrução que diz o que fazer com o resíduo.

A S11-c fechou com a IN Ibama 5/92 declarada PENDENTE: a página do DOU que eu havia
separado (21/10/1992) não trazia o ato. Estava errado — a Instrução existe, foi publicada
no DOU de 21.10.92 e está hospedada pela própria associação setorial (ABPM). Este script
a custodia, com marcador de página, e resolve a pendência.

A via oficial do Ibama (ibama.gov.br/component/legislacao) responde 403 a requisição
automatizada; o arquivo da ABPM é o fac-símile do DOU, e o sha256 fica registrado para
que a origem seja conferível.
"""
import hashlib
import json
import os
import shutil

import fitz

SCRATCH = "/Users/fabiotakwara/.hermes/cache/scratch/s11c/r7"
RAIZ = os.environ.get("COBRE_REPO", "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica")
DEST = f"{RAIZ}/_privado/fontes-documentais/ago_28_Madeira_Tratada_S11d"

DOCS = {
    "in592_1992": (
        "in592_abpm.pdf",
        "1992_in05_ibama_destinacao_final_residuos.pdf",
        "https://www.abpm.com.br/wp-content/uploads/2020/10/outubro_1992.pdf",
        "Instrução Normativa Ibama nº 5, de 20 de outubro de 1992",
        "norma",
        "Disciplina os procedimentos da Portaria Interministerial 292/89. Item VIII — «Da "
        "destinação final de resíduos e embalagens». DOU de 21.10.1992. A via oficial do Ibama "
        "(ibama.gov.br/component/legislacao) respondeu 403 a requisição automatizada; este é o "
        "fac-símile hospedado pela ABPM, associação setorial.",
    ),
    "ctf_ibama": (
        "ctf_preservativos.html",
        "2026-ctf-ibama-categorias-preservativos.md",
        "https://www.gov.br/ibama/pt-br/assuntos/quimicos-e-biologicos/preservativos-de-madeiras/registro-de-produtos-preservativos-de-madeiras",
        "Registro de produtos preservativos de madeiras — categorias do CTF (Ibama)",
        "pagina-oficial",
        "Página oficial que lista as categorias do Cadastro Técnico Federal para a cadeia. É o "
        "documento que mostra que o controle é por estabelecimento industrial.",
    ),
}


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def extrair_pdf(src, dst_md):
    doc = fitz.open(src)
    partes = []
    for n, pag in enumerate(doc, 1):
        partes.append(f"<!-- PAGE: {n} -->\n{pag.get_text().rstrip()}\n")
    open(dst_md, "w", encoding="utf-8").write("\n".join(partes))
    return len(doc)


def extrair_html(src, dst_md):
    import html as H
    import re
    raw = open(src, encoding="utf-8", errors="replace").read()
    raw = re.sub(r"<script.*?</script>|<style.*?</style>", " ", raw, flags=re.S)
    txt = H.unescape(re.sub(r"<[^>]+>", "\n", raw))
    linhas = [l.strip() for l in txt.split("\n")]
    linhas = [l for l in linhas if l and not l.startswith(("Ir para", "Compartilhe"))]
    visto, limpo = set(), []
    for l in linhas:
        if l in visto:
            continue
        visto.add(l)
        limpo.append(l)
    open(dst_md, "w", encoding="utf-8").write(
        "<!-- PAGE: 1 (página única, conteúdo extraído do HTML) -->\n" + "\n".join(limpo))
    return 1


def main():
    os.makedirs(DEST, exist_ok=True)
    entradas = []
    for chave, (arq_orig, arq_novo, url, titulo, tipo, obs) in DOCS.items():
        src = os.path.join(SCRATCH, arq_orig)
        if not os.path.exists(src):
            raise SystemExit(f"origem ausente: {src}")
        dst_pdf = os.path.join(DEST, arq_novo)
        shutil.copy2(src, dst_pdf)
        h1, h2 = sha(src), sha(dst_pdf)
        assert h1 == h2, f"cópia divergente: {arq_novo}"

        dst_md = dst_pdf.replace(".pdf", ".md")
        if arq_novo.endswith(".pdf"):
            paginas = extrair_pdf(dst_pdf, dst_md)
        else:
            paginas = extrair_html(dst_pdf, dst_md)

        entradas.append({
            "chave": chave,
            "arquivo": arq_novo,
            "titulo": titulo,
            "tipo": tipo,
            "fonte_url": url,
            "bytes": os.path.getsize(dst_pdf),
            "sha256": h2,
            "paginas": paginas,
            "observacao": obs,
            "extracao": os.path.basename(dst_md),
            "sha256_extracao": sha(dst_md),
        })
        print(f"  {arq_novo:62s} {os.path.getsize(dst_pdf):>8,} B  {paginas:>2} p.  {h2[:16]}…")

    man = {
        "schema": "ACERVO_CUSTODIA_S11D_R1",
        "gaveta": "cobre",
        "data": "2026-11-24",
        "objeto": ("A instrução que a rodada S11-c deixou pendente por erro de busca — e que responde, "
                   "na letra, o que a peça vinha afirmando que não existia: a destinação final do "
                   "resíduo de preservativo."),
        "entradas": entradas,
        "pendentes": [],
        "resolvidas": [{
            "chave": "in_ibama_05_1992",
            "motivo_anterior": "declarada pendente na S11-c: a página do DOU de 21/10/1992 separada não trazia o ato",
            "resolucao": "o ato está no DOU de 21.10.1992, hospedado pela ABPM; custodiado nesta rodada",
        }],
    }
    p = os.path.join(DEST, "MANIFEST_S11D.json")
    json.dump(man, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\nmanifesto: {p}\n{len(entradas)} documentos, {len(man['pendentes'])} pendentes")


if __name__ == "__main__":
    main()
