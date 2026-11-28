#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rodada 2 de aquisição — rotas por host, sobre o que a rodada 1 não alcançou.

Cada repositório publica o binário por um caminho próprio, e tratar todos como "link direto"
foi o que deixou 33 obras sem PDF. Rotas:
  BDTD    — a página do registro não é a obra: o link do repositório está dentro dela.
  UnB     — o Tainacan publica `10482/<n>`; o DSpace antigo serve o bitstream desse handle.
  UFRGS   — handle `10183/<n>` mora no Lume; o `hdl.handle.net` devolve página, não arquivo.
  UFV     — Locus é DSpace com WAF na landing: OAI-PMH `ore` publica o bitstream (como a UFSC).
  UNICAMP — `20.500.12733/<n>` mora no repositório novo, que é JS: tenta a rota de acervo.
Regra intacta: só conta como custódia o arquivo que começa em %PDF e tem mais de 20 KB.
"""
from __future__ import annotations
import json, re, subprocess, sys, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from mtcc_custodia import baixar, curl, pdfs_na_pagina, eh_pdf, paginas  # noqa: E402
import hashlib

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"


def html_de(url, tmp="/tmp/_r2.html"):
    code, ctype, _ = curl(url, tmp, 20)
    p = Path(tmp)
    return (p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""), code


def candidatos(item):
    """URLs plausíveis de PDF, derivadas do host — não inventadas, resolvidas."""
    urls = [t["url"] for t in item.get("tentativas", [])]
    saida = []

    for u in urls:
        # BDTD: o link da obra está no registro
        if "bdtd.ibict.br" in u:
            h, _ = html_de(u)
            for pat in [r'href="(https?://[^"]*/handle/[^"]+)"', r'href="(https?://[^"]+\.pdf[^"]*)"']:
                for m in re.finditer(pat, h):
                    saida.append(m.group(1).replace("&amp;", "&"))
            if not saida:
                mm = re.search(r"(https?://repositorio[^\"<\s]+|https?://[a-z0-9.-]+/[^\"<\s]*handle[^\"<\s]*)", h)
                if mm:
                    saida.append(mm.group(1))

        # UnB / Tainacan: identifier 10482/<n> → DSpace antigo
        if "tainacan" in u or "repositorio.unb.br" in u:
            h, _ = html_de(u)
            m = re.search(r"(10482/\d+)", h)
            if m:
                saida.append(f"https://repositorio.unb.br/handle/{m.group(1)}")

        # UFRGS / Lume
        m = re.search(r"10183/(\d+)", u)
        if m:
            saida.append(f"https://lume.ufrgs.br/handle/10183/{m.group(1)}")
            saida.append(f"https://lume.ufrgs.br/bitstream/handle/10183/{m.group(1)}/0001.pdf")

        # UFV / Locus — OAI-PMH
        if "locus.ufv.br" in u:
            m = re.search(r"/handle/(\d+/\d+)", u)
            if m:
                ident = f"oai:www.locus.ufv.br:{m.group(1)}"
                h, _ = html_de(f"https://www.locus.ufv.br/oai/request?verb=GetRecord&metadataPrefix=ore&identifier={ident}")
                saida += re.findall(r'href="(https?://[^"]*locus[^"]*bitstream[^"]*)"', h)
                saida += re.findall(r'href="(https?://[^"]*\.pdf[^"]*)"', h)

        # UNICAMP
        if "20.500.12733" in u or "unicamp" in u:
            h, _ = html_de(u)
            saida += re.findall(r'href="(https?://[^"]*/bitstream/[^"]+)"', h)

    return list(dict.fromkeys([x for x in saida if x.startswith("http")]))


def processar(item, pdf_dir: Path):
    slug = item["arquivo_alvo"].replace(".md", "")
    destino = pdf_dir / f"{slug}.pdf"
    tent = list(item.get("tentativas", []))
    for u in candidatos(item)[:4]:
        ok, code, n, why = baixar(u, destino)
        tent.append({"url": u, "http": code, "bytes": n, "resultado": why, "via": "rodada2"})
        if ok:
            return {"arquivo_alvo": item["arquivo_alvo"], "titulo": item.get("titulo"),
                    "ano": item.get("ano"), "estado": "CUSTODIADO",
                    "sha256": hashlib.sha256(destino.read_bytes()).hexdigest(),
                    "bytes": destino.stat().st_size, "paginas": paginas(destino),
                    "arquivo_pdf": destino.name, "origem_url": u, "rota": "rodada2",
                    "tentativas": tent, "verificado_em": "2026-11-28"}
        # a página pode listar o bitstream
        if code == "200":
            h, _ = html_de(u)
            for cand in pdfs_na_pagina(h, u)[:3]:
                ok2, c2, n2, w2 = baixar(cand, destino)
                tent.append({"url": cand, "http": c2, "bytes": n2, "resultado": w2, "via": "rodada2_pagina"})
                if ok2:
                    return {"arquivo_alvo": item["arquivo_alvo"], "titulo": item.get("titulo"),
                            "ano": item.get("ano"), "estado": "CUSTODIADO",
                            "sha256": hashlib.sha256(destino.read_bytes()).hexdigest(),
                            "bytes": destino.stat().st_size, "paginas": paginas(destino),
                            "arquivo_pdf": destino.name, "origem_url": cand, "rota": "rodada2_pagina",
                            "tentativas": tent, "verificado_em": "2026-11-28"}
    return {"arquivo_alvo": item["arquivo_alvo"], "titulo": item.get("titulo"), "ano": item.get("ano"),
            "estado": "NAO_ALCANCADO", "motivo": (tent[-1]["resultado"] if tent else "sem rota"),
            "tentativas": tent, "verificado_em": "2026-11-28"}


if __name__ == "__main__":
    base = Path(__file__).parent
    C = json.loads((base / "CUSTODIA_CONSOLIDADA.json").read_text(encoding="utf-8"))
    pdf_dir = base / "custodia" / "pdf"
    pdf_dir.mkdir(parents=True, exist_ok=True)
    fila = [c for c in C if c["estado"] != "CUSTODIADO" and c.get("tentativas")]
    saida = base / "custodia" / "CUSTODIA_RODADA2.jsonl"
    feitos = set()
    if saida.exists():
        feitos = {json.loads(l)["arquivo_alvo"] for l in saida.read_text(encoding="utf-8").splitlines() if l.strip()}
    fila = [c for c in fila if c["arquivo_alvo"] not in feitos]
    for i, item in enumerate(fila, 1):
        r = processar(item, pdf_dir)
        with saida.open("a", encoding="utf-8") as f:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"[{i}/{len(fila)}] {r['estado']:14} {r['arquivo_alvo'][:46]} {r.get('motivo','')}", flush=True)
        time.sleep(0.3)
