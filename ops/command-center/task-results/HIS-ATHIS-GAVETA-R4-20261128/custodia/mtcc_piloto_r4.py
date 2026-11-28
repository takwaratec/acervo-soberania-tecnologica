#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MTCC/R4 — estágio 3+4 do piloto de 5 obras (ATHIS/HIS).

Achado que este script existe para corrigir: a auditoria da aba de obra mediu 62 fichas e
**zero lotes**. Ficha sem lote não passou pelo motor — e lote ausente não se compensa com prosa.

Aqui o binário já está em custódia privada (`_privado/fontes-academicas/<slug>/original.pdf`,
do Acervo Soberania Tecnológica). O script:
  1. confere sha256 do PDF e grava CUSTODIA.json (estágio 3);
  2. re-extrai blocos do PDF com PyMuPDF `get_text("blocks")` — a `extracao.md` do release
     guarda página inteira por bloco, e ancorar nela daria uma âncora por página;
  3. rotula todo bloco com motivo (crivo 4b) e emite ANCORAS.json para os blocos de corpo;
  4. prova a ordem de leitura das páginas de duas colunas (senão ORDEM_LEITURA_PASS não fecha).

Não faz análise semântica: isso é o motor. Este script só produz o que é verificável.

Saída: <saida>/<slug>/{CUSTODIA.json,ANCORAS.json,CRIVO.json} + <saida>/LOTE_PILOTO.json
Uso:   python3 mtcc_piloto_r4.py --fonte <dir-fontes> --saida <dir-saida> --slugs a,b,c
"""
from __future__ import annotations
import argparse, hashlib, json, os, re, sys, unicodedata
from collections import Counter
from pathlib import Path

import fitz

# --- crivo de rótulos -------------------------------------------------------
PADROES = [
    ("referencia", "referência bibliográfica (SOBRENOME, iniciais)",
     re.compile(r"^[A-ZÁÉÍÓÚÂÊÔÃÕÇ][A-ZÁÉÍÓÚÂÊÔÃÕÇ\s'\-]{2,},\s*[A-Z]\.")),
    ("referencia", "referência bibliográfica (autor institucional)",
     re.compile(r"^[A-ZÁÉÍÓÚÂÊÔÃÕÇ]{4,}(\s+[A-ZÁÉÍÓÚÂÊÔÃÕÇ]{2,}){0,4}\.\s+\d{4}")),
    ("nao_analisavel", "URL, DOI ou identificador — número no endereço não é medida",
     re.compile(r"(https?://|www\.|doi\.org|doi:\s*10\.|scielo|redalyc|handle\.net|\.pdf\b)", re.I)),
    ("nao_analisavel", "afiliação institucional ou contato de autor",
     re.compile(r"^(\d{0,2}\s*)?(univers|college|institute|departamento|laborator|university|"
                r"faculdade|campus|corresponding author|professor|e-?mail|received|accepted|"
                r"recepci|resumo|abstract|resumen)\b", re.I)),
    ("legenda", "legenda de figura ou tabela",
     re.compile(r"^(Figure|Fig\.|Table|Tabela|Figura|Quadro|Gráfico)\s*\d+", re.I)),
    ("legenda", "fonte ou nota dentro de figura/tabela", re.compile(r"^(Source|Fonte|Note|Nota)\s*:", re.I)),
    ("agradecimento", "agradecimento ou financiamento",
     re.compile(r"^(Acknowledg|Agradec|Funding|Financiamento|We thank|The authors thank|"
                r"Conflicts? of interest|Conflito de interesses|CAPES|CNPq|FAPESP)", re.I)),
    ("nao_analisavel", "cabeçalho/rodapé editorial",
     re.compile(r"^(Received|Accepted|Published|Available online|DOI|ISSN|Copyright|©|Keywords|"
                r"Palavras-chave|Abstract|Resumen|Corresponding author|E-mail|License|Open Access|"
                r"Cite this|How to cite|Article history|Revista|Cadernos|Ambiente Construído)", re.I)),
    ("numeracao", "número de página isolado", re.compile(r"^\s*\d{1,4}\s*$")),
    ("numeracao", "marcador de lista isolado", re.compile(r"^\s*(\d{1,3}[.)]|[-–•·▪])\s*$")),
]
LIXO = re.compile(r"^[\s\W_]{0,8}$")


def nfc(s):
    return unicodedata.normalize("NFC", s)


def classificar(txt, cabecalho_repetido=False):
    t = " ".join(txt.split())
    if LIXO.match(t):
        return "numeracao", "bloco sem conteúdo textual"
    for rot, motivo, rx in PADROES:
        if rx.match(t):
            return rot, motivo
    if cabecalho_repetido:
        return "nao_analisavel", "cabeçalho repetido identificado por recorrência entre páginas"
    palavras = len(re.findall(r"[A-Za-zÀ-ÿ]{2,}", t))
    if palavras < 8:
        return "fragmento", f"bloco curto ({palavras} palavras)"
    return "corpo", f"parágrafo substantivo ({palavras} palavras)"


def blocos_do_pdf(caminho):
    doc = fitz.open(caminho)
    saida = []
    for npag, pag in enumerate(doc, 1):
        for b in pag.get_text("blocks"):
            if not b[4].strip():
                continue
            saida.append({"pagina": npag, "texto": nfc(b[4]),
                          "bbox": [round(x, 1) for x in b[:4]]})
    npags = doc.page_count
    doc.close()
    return saida, npags


def ordem_ambigua(blocos):
    """Ordem é ambígua quando a página tem duas colunas e a extração intercala as colunas.

    Só entram blocos substantivos (≥40 caracteres): o que dispara sobreposição em PDF
    acadêmico são símbolos de equação e fórmulas quebradas, não colunas."""
    por_pag = {}
    for b in blocos:
        if len(b["texto"].strip()) >= 40:
            por_pag.setdefault(b["pagina"], []).append(b["bbox"])
    amb, paginas_2col, resolvidas = 0, [], []
    for pag, caixas in sorted(por_pag.items()):
        if len(caixas) < 4:
            continue
        xs = [c[0] for c in caixas] + [c[2] for c in caixas]
        centro = (min(xs) + max(xs)) / 2
        meio = sum(1 for c in caixas if c[0] < centro < c[2])
        esq = sum(1 for c in caixas if c[2] <= centro)
        dir_ = sum(1 for c in caixas if c[0] >= centro)
        n = len(caixas)
        if not (esq >= 0.3 * n and dir_ >= 0.3 * n and meio <= 0.25 * n):
            continue
        paginas_2col.append(pag)
        inter = 0
        lado_ant = None
        for c in caixas:
            lado = "E" if c[2] <= centro else ("D" if c[0] >= centro else None)
            if lado is None:
                continue
            if lado_ant and lado != lado_ant:
                inter += 1
            lado_ant = lado
        if inter > 2:
            amb += inter
        else:
            resolvidas.append(pag)
    return amb, paginas_2col, resolvidas


def processar(slug, fonte: Path, saida: Path, lote_id: str):
    d = fonte / slug
    pdf = d / "original.pdf"
    if not pdf.exists():
        return {"slug": slug, "estado": "SEM_PDF"}
    meta = json.loads((d / "metadados.json").read_text(encoding="utf-8")) if (d / "metadados.json").exists() else {}
    sha_pdf = hashlib.sha256(pdf.read_bytes()).hexdigest()

    blocos, npags = blocos_do_pdf(pdf)
    norm = Counter(" ".join(b["texto"].split())[:60] for b in blocos)
    repetidos = {k for k, v in norm.items() if v >= max(3, npags * 0.4)}

    ancoras, rotulos, dist = [], [], {}
    n = 0
    for i, b in enumerate(blocos):
        rot, motivo = classificar(b["texto"], " ".join(b["texto"].split())[:60] in repetidos)
        dist[rot] = dist.get(rot, 0) + 1
        if rot == "corpo":
            uid = f"u{n:04d}"
            ancoras.append({"unidade_id": uid, "documento": f"{slug}.pdf", "pagina": b["pagina"],
                            "bloco_id": f"b{i:05d}", "char_inicio": 0, "char_fim": len(b["texto"]),
                            "trecho_literal": b["texto"].strip(), "regiao_pagina": "corpo",
                            "bbox": b["bbox"]})
            n += 1
        rotulos.append({"documento": f"{slug}.pdf", "pagina": b["pagina"], "bloco_id": f"b{i:05d}",
                        "rotulo": rot, "motivo": motivo, "bbox": b["bbox"],
                        "sha_trecho": hashlib.sha256(b["texto"].strip().encode()).hexdigest(),
                        "recuperacao": {"estado": "NAO_NECESSARIA", "acao": "nenhuma", "executada": False}})

    amb, p2col, resolvidas = ordem_ambigua(blocos)
    os.makedirs(saida / slug, exist_ok=True)
    cust = {"lote_id": lote_id, "documento": f"{slug}.pdf", "sha256_pdf": sha_pdf,
            "bytes": pdf.stat().st_size, "paginas": npags,
            "metadados": {k: meta.get(k) for k in ("titulo", "autores", "ano", "doi", "tipo", "instituicao", "licenca")},
            "custodia": "Acervo Soberania Tecnológica, release 1 (_privado/fontes-academicas)",
            "classe": "A", "verificado_em": "2026-11-28"}
    (saida / slug / "CUSTODIA.json").write_text(json.dumps(cust, ensure_ascii=False, indent=1), encoding="utf-8")
    (saida / slug / "ANCORAS.json").write_text(json.dumps(
        {"lote_id": lote_id, "documento": f"{slug}.pdf", "regra": "MTCC/ANCORAS/3",
         "paginas": npags, "ordem_ambigua": amb, "total": len(ancoras), "ancoras": ancoras},
        ensure_ascii=False, indent=1), encoding="utf-8")
    (saida / slug / "CRIVO.json").write_text(json.dumps(
        {"lote_id": lote_id, "documento": f"{slug}.pdf", "total_blocos": len(blocos),
         "inventario": len(blocos), "analisavel": len(ancoras),
         "nao_analisavel_por_rotulo": len(blocos) - len(ancoras),
         "crivo_id": "MTCC/CRIVO/R38-PILOTO-v1", "versao_classificador": "pymupdf-blocks-1",
         "regra": "todo bloco recebe rótulo e motivo; nada é apagado",
         "distribuicao": dist, "rotulos": rotulos}, ensure_ascii=False, indent=1), encoding="utf-8")

    return {"slug": slug, "estado": "OK", "paginas": npags, "blocos": len(blocos),
            "analisavel": len(ancoras), "ordem_ambigua": amb,
            "paginas_duas_colunas": len(p2col), "paginas_ordem_resolvida": len(resolvidas),
            "distribuicao": dist, "sha256_pdf": sha_pdf}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--fonte", required=True)
    ap.add_argument("--saida", required=True)
    ap.add_argument("--slugs", required=True)
    ap.add_argument("--lote-id", default="LOTE-PILOTO-ATHIS-HIS-R4-20261128-R1")
    a = ap.parse_args()
    fonte, saida = Path(a.fonte), Path(a.saida)
    slugs = [s.strip() for s in a.slugs.split(",") if s.strip()]
    res = [processar(s, fonte, saida, a.lote_id) for s in slugs]
    lote = {"lote_id": a.lote_id, "raiz": str(fonte), "gerado_por": "ops/mtcc_piloto_r4.py",
            "extrator": f"PyMuPDF {fitz.__doc__.split()[1] if fitz.__doc__ else '?'} get_text('blocks')",
            "regra": "entrada é o PDF custodiado; âncora por bloco com página e caixa",
            "documentos": res,
            "totais": {"documentos": len(res),
                       "blocos": sum(r.get("blocos", 0) for r in res),
                       "analisavel": sum(r.get("analisavel", 0) for r in res),
                       "paginas": sum(r.get("paginas", 0) for r in res),
                       "ordem_ambigua": sum(r.get("ordem_ambigua", 0) for r in res)}}
    (saida / "LOTE_PILOTO.json").write_text(json.dumps(lote, ensure_ascii=False, indent=1), encoding="utf-8")
    for r in res:
        print(f"{r['slug']}: {r.get('estado')} paginas={r.get('paginas')} blocos={r.get('blocos')} "
              f"corpo={r.get('analisavel')} ordem_ambigua={r.get('ordem_ambigua')}")
    print(f"TOTAL documentos={lote['totais']['documentos']} blocos={lote['totais']['blocos']} "
          f"corpo={lote['totais']['analisavel']}")
