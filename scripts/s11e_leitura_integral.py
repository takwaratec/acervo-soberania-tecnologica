#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leitura integral por parágrafo — as sete custodiadas.

O defeito que este script existe para corrigir: documento custodiado e lido por recorte é
meia custódia. A IN 5/92 tem 15 páginas e eu usei quatro itens dela; o resultado foi uma
tese construída sobre pedaços.

O que ele faz:
 1. segmenta cada extração (que já tem marcador `<!-- PAGE: n -->`) em parágrafos;
 2. dá a cada parágrafo um identificador estável — DOC:pN.¶K — e grava o texto;
 3. emite um índice humano por documento (id, página, tamanho, começo do texto);
 4. emite um JSON com o texto de todos os parágrafos, para a classificação depois.

A classificação por parágrafo é feita em arquivo separado, e o portão
`s11e_gate_leitura.py` exige que TODO parágrafo do índice esteja classificado e que
nenhum classificado seja inventado.
"""
import json
import os
import re
import unicodedata

RAIZ = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica"
CUSTODIAS = {
    "ago_28_Madeira_Tratada_S11c": [
        "1989_pi292_preservativos_registro.md",
        "1997_pn151_ibama_registro_risco_ambiental.md",
        "2023_iema_es_nt01_preservacao_madeira.md",
        "2016_abpm_fg4mad_destinacao_residuos_madeira_tratada.md",
        "2025_ufsm_ciencia_florestal_cca_moiroes_solo.md",
    ],
    "ago_28_Madeira_Tratada_S11d": [
        "1992_in05_ibama_destinacao_final_residuos.md",
        "2026-ctf-ibama-categorias-preservativos.md",
    ],
}

DEST = f"{RAIZ}/docs/analyses/cobre/leitura-integral"


def nfc(s):
    return unicodedata.normalize("NFC", s)


def norm_ws(s):
    s = s.replace("\u00ad", "")
    s = re.sub(r"[ \t]+", " ", s)
    return s.strip()


# Em texto legal a unidade não é o bloco separado por linha em branco: é o artigo, o item e a
# alínea. Segmentar só por linha em branco deu 8 parágrafos para 4 páginas de Portaria — e foi
# exatamente esse tipo de recorte grosso que produziu a leitura parcial.
MARCADORES = re.compile(
    r"\n(?="
    r"Art\.\s*\d"                       # artigo
    r"|§\s*\d"                          # parágrafo
    r"|[IVXLC]+\s*[-–]\s+[A-ZÀ-Ú]"      # item romano — «VIII - DA DESTINAÇÃO FINAL»
    r"|[a-z]\)\s"                       # alínea — «a) é proibida...»
    r"|\d+\s*[-–]\s+[a-zà-ú]"           # lista numerada
    r")"
)


# Documento extraído de HTML não preserva linha em branco: a unidade só pode ser a linha.
# Em PDF a linha é quebra de composição e cortar por ela parte frases ao meio — por isso a
# regra é por documento, não por heurística de tamanho.
POR_LINHA = {"2026-ctf-ibama-categorias-preservativos.md"}


def subdividir(bloco, por_linha=False):
    """Quebra um bloco nos marcadores legais; em HTML, por linha."""
    if por_linha:
        return [norm_ws(l) for l in bloco.split("\n") if len(norm_ws(l)) >= 3]
    pedacos = []
    for parte in MARCADORES.split(bloco):
        p = norm_ws(parte)
        if len(p) >= 3:
            pedacos.append(p)
    return pedacos


def segmentar(texto, por_linha=False):
    """Devolve [(pagina, k, paragrafo)] — parágrafo = artigo, item, alínea ou bloco."""
    saida = []
    for bloco in texto.split("<!-- PAGE: ")[1:]:
        cabeca, resto = bloco.split(" -->", 1)
        m = re.match(r"\s*(\d+)", cabeca)
        pag = int(m.group(1)) if m else 0
        k = 0
        for par in re.split(r"\n\s*\n", resto):
            for p in subdividir(par, por_linha=por_linha):
                k += 1
                saida.append((pag, k, p))
    return saida


def main():
    os.makedirs(DEST, exist_ok=True)
    total = 0
    resumo = []
    for custodia, docs in CUSTODIAS.items():
        for nome in docs:
            caminho = os.path.join(RAIZ, "_privado/fontes-documentais", custodia, nome)
            texto = nfc(open(caminho, encoding="utf-8").read())
            pars = segmentar(texto, por_linha=nome in POR_LINHA)
            doc_id = re.sub(r"^\d{4}[-_]?", "", nome).replace(".md", "")
            doc_id = re.sub(r"[^a-z0-9]+", "-", doc_id.lower()).strip("-")

            registros = []
            linhas_indice = [
                f"# Índice de parágrafos — {nome}",
                "",
                f"Extração: `_privado/fontes-documentais/{custodia}/{nome}`  ",
                f"Parágrafos: **{len(pars)}** · páginas: **{max(p for p, _k, _t in pars)}**",
                "",
                "| id | pág | chars | começo do parágrafo |",
                "|---|---|---|---|",
            ]
            for pag, k, txt in pars:
                pid = f"{doc_id}:p{pag}.¶{k}"
                txt = nfc(txt)
                registros.append({"id": pid, "pagina": pag, "k": k,
                                  "chars": len(txt), "texto": txt})
                amostra = re.sub(r"\s+", " ", txt)[:110].replace("|", "\\|")
                linhas_indice.append(f"| `{pid}` | {pag} | {len(txt)} | {amostra} |")

            base = os.path.join(DEST, doc_id)
            open(base + ".indice.md", "w", encoding="utf-8").write("\n".join(linhas_indice) + "\n")
            json.dump({"documento": nome, "custodia": custodia, "doc_id": doc_id,
                       "total": len(registros), "paragrafos": registros},
                      open(base + ".paragrafos.json", "w", encoding="utf-8"),
                      ensure_ascii=False, indent=1)
            total += len(registros)
            resumo.append((doc_id, len(registros), max(p for p, _k, _t in pars),
                           sum(1 for _p, _k, t in pars if len(t) >= 40)))
            print(f"  {doc_id:52s} {len(registros):>4} ¶   "
                  f"{max(p for p, _k, _t in pars):>3} p.   "
                  f"{sum(1 for _p, _k, t in pars if len(t) >= 40):>4} substantivos")

    man = {
        "schema": "ACERVO_LEITURA_INTEGRAL_R1",
        "gaveta": "cobre",
        "data": "2026-11-24",
        "regra": ("Documento custodiado é lido na íntegra, parágrafo por parágrafo, com índice "
                  "estável. A classificação é feita sobre o índice e o portão exige cobertura "
                  "total: parágrafo sem classe reprova, classe sem parágrafo reprova."),
        "total_paragrafos": total,
        "documentos": [{"doc_id": d, "paragrafos": n, "paginas": p, "substantivos": s}
                       for d, n, p, s in resumo],
    }
    json.dump(man, open(os.path.join(DEST, "MANIFEST_LEITURA_INTEGRAL.json"), "w",
                        encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\nTOTAL: {total} parágrafos em {sum(len(v) for v in CUSTODIAS.values())} documentos")
    print(f"DESTINO: {DEST}")


if __name__ == "__main__":
    main()
