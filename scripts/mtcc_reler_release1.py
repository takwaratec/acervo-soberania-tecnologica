#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Releitura MTCC/R38 do corpus do Release 1 — com re-extração do PDF.

POR QUE RE-EXTRAIR: a extração em `extracao.md` do Release 1 guarda uma página inteira
por bloco (o PDF não trouxe quebras de parágrafo). Ancorar sobre ela daria uma âncora
por página, o que não sustenta afirmação conferível — e o estágio 6 do MTCC exige
span de bloco com intervalo de caracteres. Então o bloco é reconstruído do PDF pelo
próprio PyMuPDF (`get_text("blocks")`), que devolve caixa, página e ordem de leitura.

O que este script NÃO faz: análise semântica. Ele produz os dois artefatos
determinísticos do método — ANCORAS e CRIVO — e deixa o julgamento para o motor.

SAÍDA: _privado/governanca-operacional/mtcc-release1/<slug>/{ANCORAS,CRIVO}.json
       _privado/governanca-operacional/mtcc-release1/LOTE.json
"""
import hashlib
import json
import os
import re
import unicodedata

import fitz

RAIZ = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica"
FONTES = f"{RAIZ}/_privado/fontes-academicas/revisao-89"
SAIDA = f"{RAIZ}/_privado/governanca-operacional/mtcc-release1"
LOTE_ID = "LOTE-MTCC-RELEASE1-20261124-R1"

# ---------------------------------------------------------------- crivo de rótulos
PADROES = [
    ("referencia", "referência bibliográfica (SOBRENOME, iniciais)",
     re.compile(r"^[A-ZÁÉÍÓÚÂÊÔÃÕÇ][A-ZÁÉÍÓÚÂÊÔÃÕÇ\s'\-]{2,},\s*[A-Z]\.")),
    ("referencia", "referência bibliográfica (autor institucional)",
     re.compile(r"^[A-ZÁÉÍÓÚÂÊÔÃÕÇ]{4,}(\s+[A-ZÁÉÍÓÚÂÊÔÃÕÇ]{2,}){0,4}\.\s+\d{4}")),
    ("legenda", "legenda de figura ou tabela",
     re.compile(r"^(Figure|Fig\.|Table|Tabela|Figura|Quadro|Tabela)\s*\d+", re.I)),
    ("legenda", "texto dentro de figura/tabela, sem frase própria",
     re.compile(r"^(Source|Fonte|Note|Nota)\s*:", re.I)),
    ("agradecimento", "agradecimento ou financiamento",
     re.compile(r"^(Acknowledg|Agradec|Funding|Financiamento|We thank|The authors thank|"
                r"Conflicts? of interest|Conflito de interesses)", re.I)),
    ("nao_analisavel", "cabeçalho/rodapé editorial ou metadado de publicação",
     re.compile(r"^(Received|Accepted|Published|Available online|DOI|ISSN|Copyright|©|"
                r"Keywords|Palavras-chave|Abstract|Resumen|Resumo|Corresponding author|"
                r"E-mail|License|Open Access|Cite this|How to cite|Article history)", re.I)),
    ("nao_analisavel", "cabeçalho repetido da revista em toda página",
     re.compile(r"^(Brazilian Journal|Revista|Journal of|Scientia|Pesquisa Florestal|"
                r"Floresta|Bamboo Science)", re.I)),
    ("numeracao", "número de página isolado",
     re.compile(r"^\s*\d{1,4}\s*$")),
    ("numeracao", "marcador de lista isolado",
     re.compile(r"^\s*(\d{1,3}[.)]|[-•·▪])\s*$")),
]

LIXO = re.compile(r"^[\s\W_]{0,8}$")


def nfc(s):
    return unicodedata.normalize("NFC", s)


def classificar(txt, eh_cabecalho_repetido=False):
    t = " ".join(txt.split())
    if LIXO.match(t):
        return "numeracao", "bloco sem conteúdo textual (só pontuação ou espaço)"
    for rot, motivo, rx in PADROES:
        if rx.match(t):
            return rot, motivo
    palavras = len(re.findall(r"[A-Za-zÀ-ÿ]{2,}", t))
    if eh_cabecalho_repetido:
        return "nao_analisavel", "cabeçalho repetido identificado por recorrência entre páginas"
    if palavras < 8:
        return "fragmento", f"bloco curto ({palavras} palavras)"
    return "corpo", f"parágrafo substantivo ({palavras} palavras)"


def blocos_do_pdf(caminho):
    """Blocos na ordem de leitura, com página e caixa. Marcador de ordem ambígua:
    a extração prova a ordem quando as caixas não se sobrepõem na horizontal."""
    doc = fitz.open(caminho)
    saida = []
    for npag, pag in enumerate(doc, 1):
        caixas = pag.get_text("blocks")
        caixas.sort(key=lambda b: (round(b[1] / 4), b[0]))
        for b in caixas:
            txt = nfc(b[4])
            if not txt.strip():
                continue
            saida.append({"pagina": npag, "texto": txt,
                          "bbox": [round(x, 1) for x in b[:4]]})
    doc.close()
    return saida


def ordens_ambiguas(blocos, npag_total):
    """Ordem de leitura é ambígua quando a página tem DUAS COLUNAS de texto corrido.

    Medido no corpus: o que dispara sobreposição aqui são SÍMBOLOS DE EQUAÇÃO
    (blocos de 1–3 caracteres em x/y cruzados) e fórmulas quebradas em pedaços, não
    colunas. Por isso só entram na conta blocos substantivos (≥40 caracteres), e a
    coluna é decidida pela quebra vertical do miolo da página: se ≥60% dos blocos
    substantivos ficam à esquerda do centro e ≥25% à direita (ou o inverso), há
    duas colunas; sobreposição entre colunas distintas é ambígua."""
    por_pag = {}
    for b in blocos:
        if len(b["texto"].strip()) < 40:
            continue
        por_pag.setdefault(b["pagina"], []).append(b["bbox"])
    amb = 0
    for _p, caixas in por_pag.items():
        if len(caixas) < 4:
            continue
        xs = [c[0] for c in caixas] + [c[2] for c in caixas]
        if not xs:
            continue
        centro = (min(xs) + max(xs)) / 2
        meio = sum(1 for c in caixas if c[0] < centro < c[2])
        esq = sum(1 for c in caixas if c[2] <= centro)
        dir_ = sum(1 for c in caixas if c[0] >= centro)
        n = len(caixas)
        duas_colunas = (esq >= 0.3 * n and dir_ >= 0.3 * n and meio <= 0.25 * n)
        if not duas_colunas:
            continue
        # página de duas colunas: a ordem exportada tem de casar com a leitura
        # coluna-esquerda inteira antes da direita. Se blocos intercalam, é ambíguo.
        inter = 0
        ultimo_lado = None
        for c in caixas:
            lado = "E" if c[2] <= centro else ("D" if c[0] >= centro else None)
            if lado is None:
                continue
            if ultimo_lado and lado != ultimo_lado:
                inter += 1
                ultimo_lado = lado
            else:
                ultimo_lado = lado
        if inter > 2:
            amb += inter
    return amb


def processar(rec):
    slug = rec["slug"]
    pdf = f"{FONTES}/{slug}/original.pdf"
    if not os.path.exists(pdf):
        return {"slug": slug, "estado": "SEM_PDF"}
    ex = f"{FONTES}/{slug}/extracao.md"
    sha_ext = hashlib.sha256(open(ex, "rb").read()).hexdigest() if os.path.exists(ex) else None
    sha_pdf = hashlib.sha256(open(pdf, "rb").read()).hexdigest()

    blocos = blocos_do_pdf(pdf)
    # cabeçalho repetido: bloco normalizado que aparece em >=40% das páginas
    from collections import Counter
    norm = Counter(" ".join(b["texto"].split())[:60] for b in blocos)
    npags = len({b["pagina"] for b in blocos})
    repetidos = {k for k, v in norm.items() if v >= max(3, npags * 0.4)}

    ancoras, rotulos, dist = [], [], {}
    n = 0
    for i, b in enumerate(blocos):
        t_norm = " ".join(b["texto"].split())[:60]
        rot, motivo = classificar(b["texto"], t_norm in repetidos)
        dist[rot] = dist.get(rot, 0) + 1
        b["rotulo"] = rot
        if rot == "corpo":
            uid = f"u{n:04d}"
            n += 1
            ancoras.append({
                "unidade_id": uid,
                "documento": f"{slug}.pdf",
                "pagina": b["pagina"],
                "bloco_id": f"b{i:05d}",
                "char_inicio": 0,
                "char_fim": len(b["texto"]),
                "trecho_literal": b["texto"].strip(),
                "regiao_pagina": "corpo",
                "bbox": b["bbox"],
            })
            aid = uid
        else:
            aid = f"r{i:05d}"
        rotulos.append({
            "ancora_id": aid,
            "documento": f"{slug}.pdf",
            "pagina": b["pagina"],
            "bloco_id": f"b{i:05d}",
            "rotulo": rot,
            "motivo": motivo,
            "bbox": b["bbox"],
            "sha_trecho": hashlib.sha256(b["texto"].strip().encode()).hexdigest(),
            "recuperacao": {"estado": "NAO_NECESSARIA", "acao": "nenhuma", "executada": False},
        })

    amb = ordens_ambiguas(blocos, npags)
    os.makedirs(f"{SAIDA}/{slug}", exist_ok=True)
    a = {"lote_id": LOTE_ID, "documento": f"{slug}.pdf", "total": len(ancoras),
         "regra": "MTCC/ANCORAS/3", "paginas": npags,
         "ordem_ambigua": amb, "ancoras": ancoras}
    c = {"lote_id": LOTE_ID, "documento": f"{slug}.pdf",
         "total_blocos": len(blocos), "inventario": len(blocos),
         "analisavel": len(ancoras), "nao_analisavel_por_rotulo": len(blocos) - len(ancoras),
         "crivo_id": "MTCC/CRIVO/R38-RELEASE1-v2",
         "versao_classificador": "pymupdf-blocks-1",
         "regra": "todo bloco recebe rótulo e motivo; nada é apagado",
         "distribuicao": dist, "rotulos": rotulos}
    json.dump(a, open(f"{SAIDA}/{slug}/ANCORAS.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    json.dump(c, open(f"{SAIDA}/{slug}/CRIVO.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    return {"slug": slug, "estado": "OK", "paginas": npags, "blocos": len(blocos),
            "analisavel": len(ancoras), "ordem_ambigua": amb,
            "distribuicao": dist, "sha256_pdf": sha_pdf, "sha256_extracao": sha_ext}


if __name__ == "__main__":
    man = json.load(open(f"{FONTES}/MANIFESTO_FONTES.json", encoding="utf-8"))
    res = [processar(r) for r in man["records"]]
    lote = {"lote_id": LOTE_ID, "raiz": "fontes-academicas/revisao-89",
            "gerado_por": "scripts/mtcc_reler_release1.py",
            "extrator": f"PyMuPDF {fitz.__doc__.split()[1] if fitz.__doc__ else '?'} get_text('blocks')",
            "regra": "entrada é o PDF; âncora por bloco com página e caixa",
            "documentos": res,
            "totais": {"documentos": len(res),
                       "blocos": sum(r.get("blocos", 0) for r in res),
                       "analisavel": sum(r.get("analisavel", 0) for r in res),
                       "paginas": sum(r.get("paginas", 0) for r in res)}}
    os.makedirs(SAIDA, exist_ok=True)
    json.dump(lote, open(f"{SAIDA}/LOTE.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(json.dumps(lote["totais"], ensure_ascii=False))
    for r in res:
        if r["estado"] != "OK":
            print(f"  {r['slug']}: {r['estado']}")
            continue
        print(f"  {r['slug'][:40]:42s} p={r['paginas']:>2} blocos={r['blocos']:>4} "
              f"corpo={r['analisavel']:>4} amb={r['ordem_ambigua']:>2} {r['distribuicao']}")
