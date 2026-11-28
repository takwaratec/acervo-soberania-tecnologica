#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MTCC/R4 — estágio 3 (aquisição e custódia) da gaveta HIS/ATHIS.

Baixa obtendo o binário de verdade, não a página de registro. Três rotas, nesta ordem:
  1. link direto de PDF declarado na ficha (endpoint_pdf / bitstream / download);
  2. resolvido a partir da página de registro (citation_pdf_url, bitstream, /download);
  3. UFSC: a landing está atrás de WAF, mas o OAI-PMH está aberto — `ore` publica a URL do
     bitstream. É por aí que se chega ao PDF sem burlar proteção.

Regras duras:
  - só grava o arquivo se ele COMEÇA com %PDF (5 bytes) e tem >20 KB; 404/HTML/JS não é PDF;
  - grava sha256, bytes, páginas e URL exata de onde veio (`origem_url`) — sem isso a custódia
    não sustenta nada;
  - o que não foi alcançado entra como `NAO_ALCANCADO` com o código HTTP medido, nunca como
    "não existe" e nunca substituído por resumo.

Saída: <saida>/CUSTODIA.jsonl (uma linha por obra, append; retomável) + binário em <saida>/pdf/
"""
from __future__ import annotations
import argparse, hashlib, json, os, re, subprocess, sys, time
from pathlib import Path

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"


def curl(url, destino=None, timeout=120, headers=None):
    """Retorna (http_code, content_type, bytes). Se destino, grava o corpo lá."""
    # --location-trusted + compressão: o bitstream da UFSC devolve HTML de WAF quando o
    # curl não anuncia gzip/br, e o UFMS responde multipart (--38db…) sem o `--compressed`.
    cmd = ["curl", "-sS", "-L", "--location-trusted", "--compressed", "--max-time", str(timeout),
           "-A", UA, "-H", "Accept: application/pdf,*/*", "-w", "%{http_code}\\n%{content_type}",
           "-o", destino or "/dev/null", url]
    for h in (headers or []):
        cmd[1:1] = ["-H", h]
    r = subprocess.run(cmd, capture_output=True, text=True)
    linhas = (r.stdout or "").strip().split("\n")
    code, ctype = (linhas[-2], linhas[-1]) if len(linhas) >= 2 else ("000", "")
    n = os.path.getsize(destino) if destino and os.path.exists(destino) else 0
    return code, ctype, n


def eh_pdf(caminho):
    try:
        with open(caminho, "rb") as f:
            cab = f.read(5)
            if cab == b"%PDF-":
                return True
            # resposta multipart: o PDF começa depois do cabeçalho da parte
            f.seek(0)
            blob = f.read(4096)
            i = blob.find(b"%PDF-")
            return i > 0
    except OSError:
        return False


def desembrulha_multipart(caminho):
    """Recorta o PDF de uma resposta multipart, preservando os bytes originais do PDF."""
    dados = Path(caminho).read_bytes()
    i = dados.find(b"%PDF-")
    if i <= 0:
        return False
    Path(caminho).write_bytes(dados[i:])
    return True


def paginas(caminho):
    r = subprocess.run(["/Users/fabiotakwara/.venvs/pdf/bin/python", "-c",
                        "import fitz,sys;print(fitz.open(sys.argv[1]).page_count)", str(caminho)],
                       capture_output=True, text=True)
    return int(r.stdout.strip()) if r.returncode == 0 and r.stdout.strip().isdigit() else None


def baixar(url, destino, timeout=180):
    """Tenta baixar; confirma PDF pelos magic bytes. Devolve (ok, code, bytes, motivo)."""
    code, ctype, n = curl(url, str(destino), timeout)
    if code != "200":
        return False, code, n, f"HTTP {code}"
    if not eh_pdf(destino):
        destino.unlink(missing_ok=True)
        return False, code, n, f"não é PDF (content-type {ctype})"
    if desembrulha_multipart(destino):
        n = destino.stat().st_size
    if n < 20000:
        destino.unlink(missing_ok=True)
        return False, code, n, f"PDF truncado ({n} bytes)"
    return True, code, n, "ok"


PDF_HINTS = [r'name="citation_pdf_url"[^>]*content="([^"]+)"',
             r'href="([^"]*bitstream[^"]*\.pdf[^"]*)"',
             r'href="([^"]*/download[^"]*)"',
             r'href="([^"]+\.pdf)"']


def pdfs_na_pagina(html, base):
    achados = []
    for pat in PDF_HINTS:
        for m in re.finditer(pat, html, re.I):
            u = m.group(1).replace("&amp;", "&")
            if u.startswith("/"):
                u = re.match(r"(https?://[^/]+)", base).group(1) + u
            if u not in achados:
                achados.append(u)
    return achados


def de_ufsc_oai(handle_url):
    """UFSC: resolve o bitstream pelo OAI-PMH `ore` (a landing está atrás de WAF)."""
    m = re.search(r"/(\d+/\d+)", handle_url)
    if not m:
        return []
    ident = f"oai:repositorio.ufsc.br:{m.group(1)}"
    u = f"https://repositorio.ufsc.br/oai/request?verb=GetRecord&metadataPrefix=ore&identifier={ident}"
    code, _, _ = curl(u, "/tmp/_ore.xml", 60)
    if code != "200":
        return []
    html = Path("/tmp/_ore.xml").read_text(encoding="utf-8", errors="ignore")
    return re.findall(r'href="(https://repositorio\.ufsc\.br/bitstream/[^"]+\.pdf)"', html)


def processar(item, saida: Path):
    slug = item["arquivo_alvo"].replace(".md", "")
    pdf_dir = saida / "pdf"
    pdf_dir.mkdir(parents=True, exist_ok=True)
    destino = pdf_dir / f"{slug}.pdf"
    urls = [u for u in [item.get("pdf_direto"), item.get("url")] if u]
    tentativas, motivo = [], "sem URL de fonte"

    for u in urls:
        ok, code, n, why = baixar(u, destino)
        tentativas.append({"url": u, "http": code, "bytes": n, "resultado": why})
        if ok:
            return registrar(item, destino, u, tentativas)
        # página de registro: procurar PDF dentro dela
        if code == "200":
            tmp = Path("/tmp/_pag.html")
            curl(u, str(tmp), 90)
            html = tmp.read_text(encoding="utf-8", errors="ignore") if tmp.exists() else ""
            for cand in pdfs_na_pagina(html, u):
                ok2, code2, n2, why2 = baixar(cand, destino)
                tentativas.append({"url": cand, "http": code2, "bytes": n2, "resultado": why2,
                                   "via": "pdf_na_pagina"})
                if ok2:
                    return registrar(item, destino, cand, tentativas)
        # UFSC (WAF na landing, OAI aberto)
        if "repositorio.ufsc.br" in u:
            for cand in de_ufsc_oai(u):
                ok3, code3, n3, why3 = baixar(cand, destino)
                tentativas.append({"url": cand, "http": code3, "bytes": n3, "resultado": why3,
                                   "via": "oai_ore_ufsc"})
                if ok3:
                    return registrar(item, destino, cand, tentativas)
        motivo = tentativas[-1]["resultado"] if tentativas else motivo

    return {"arquivo_alvo": item["arquivo_alvo"], "titulo": item.get("titulo"),
            "ano": item.get("ano"), "estado": "NAO_ALCANCADO", "motivo": motivo,
            "tentativas": tentativas, "verificado_em": "2026-11-28"}


def registrar(item, destino, origem, tentativas):
    return {"arquivo_alvo": item["arquivo_alvo"], "titulo": item.get("titulo"),
            "ano": item.get("ano"), "estado": "CUSTODIADO",
            "sha256": hashlib.sha256(destino.read_bytes()).hexdigest(),
            "bytes": destino.stat().st_size, "paginas": paginas(destino),
            "arquivo_pdf": destino.name, "origem_url": origem,
            "rota": tentativas[-1].get("via", "link_direto"),
            "tentativas": tentativas, "verificado_em": "2026-11-28"}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--inventario", required=True)
    ap.add_argument("--saida", required=True)
    ap.add_argument("--limite", type=int, default=0)
    a = ap.parse_args()
    saida = Path(a.saida)
    saida.mkdir(parents=True, exist_ok=True)
    itens = json.loads(Path(a.inventario).read_text(encoding="utf-8"))
    jsonl = saida / "CUSTODIA.jsonl"
    feitos = set()
    if jsonl.exists():
        for l in jsonl.read_text(encoding="utf-8").splitlines():
            if l.strip():
                feitos.add(json.loads(l)["arquivo_alvo"])
    fila = [i for i in itens if i.get("arquivo_alvo") and i["arquivo_alvo"] not in feitos]
    if a.limite:
        fila = fila[:a.limite]
    for i, item in enumerate(fila, 1):
        res = processar(item, saida)
        with jsonl.open("a", encoding="utf-8") as f:
            f.write(json.dumps(res, ensure_ascii=False) + "\n")
        print(f"[{i}/{len(fila)}] {res['estado']:14} {res['arquivo_alvo'][:52]} {res.get('motivo','')}", flush=True)
        time.sleep(0.4)
    ok = sum(1 for l in jsonl.read_text(encoding="utf-8").splitlines() if '"CUSTODIADO"' in l)
    tot = len([l for l in jsonl.read_text(encoding="utf-8").splitlines() if l.strip()])
    print(f"TOTAL custodiados={ok} de {tot} tentados")
