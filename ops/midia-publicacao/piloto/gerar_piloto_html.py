#!/usr/bin/env python3
"""Gera o HTML navegável do piloto a partir do material REAL do repositório.

Nada é digitado à mão aqui: artigo, estado da arte, fichas de fonte e resultado dos
portões vêm dos arquivos. Se o material mudar, o HTML muda — e a conferência continua
valendo. Sem dependências externas: só stdlib, porque o produto tem de abrir em qualquer
máquina e sobreviver à perda do ambiente de origem.

Uso:
    python3 gerar_piloto_html.py --raiz ../.. --lote LOTE_PILOTO_BAMBU_E1.json --saida PILOTO_BAMBU_E1.html
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent


def esc(t: str) -> str:
    return html.escape(t, quote=False)


def inline(t: str) -> str:
    t = esc(t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    return t


def md_para_html(md: str) -> str:
    """Markdown mínimo: títulos, listas, tabelas, citação, régua e parágrafos."""
    linhas = md.split("\n")
    saida: list[str] = []
    i = 0
    while i < len(linhas):
        ln = linhas[i]
        s = ln.strip()
        if not s:
            i += 1
            continue
        if s.startswith("```"):
            i += 1
            bloco = []
            while i < len(linhas) and not linhas[i].strip().startswith("```"):
                bloco.append(esc(linhas[i]))
                i += 1
            i += 1
            saida.append("<pre>" + "\n".join(bloco) + "</pre>")
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            n = len(m.group(1))
            saida.append(f"<h{n}>{inline(m.group(2))}</h{n}>")
            i += 1
            continue
        if re.match(r"^(---|\*\*\*|___)$", s):
            saida.append("<hr>")
            i += 1
            continue
        if s.startswith("|"):
            cab = []
            corpo = []
            while i < len(linhas) and linhas[i].strip().startswith("|"):
                celulas = [c.strip() for c in linhas[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in celulas if c):
                    (cab if not cab else corpo).append(celulas)
                i += 1
            t = "<table>"
            if cab:
                t += "<thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in cab[0]) + "</tr></thead>"
            t += "<tbody>"
            for linha in corpo:
                t += "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in linha) + "</tr>"
            t += "</tbody></table>"
            saida.append(t)
            continue
        if s.startswith(">"):
            bloco = []
            while i < len(linhas) and linhas[i].strip().startswith(">"):
                bloco.append(linhas[i].strip().lstrip(">").strip())
                i += 1
            saida.append("<blockquote>" + md_para_html("\n".join(bloco)) + "</blockquote>")
            continue
        m = re.match(r"^(\d+)\.\s+(.*)$", s)
        if m:
            itens = []
            while i < len(linhas):
                mm = re.match(r"^\s*(\d+)\.\s+(.*)$", linhas[i])
                if not mm:
                    break
                itens.append(f"<li>{inline(mm.group(2))}</li>")
                i += 1
            saida.append("<ol>" + "".join(itens) + "</ol>")
            continue
        if s.startswith("- "):
            itens = []
            while i < len(linhas) and re.match(r"^\s*-\s+", linhas[i]):
                itens.append(f"<li>{inline(re.sub(r'^\s*-\s+', '', linhas[i]))}</li>")
                i += 1
            saida.append("<ul>" + "".join(itens) + "</ul>")
            continue
        par = []
        while i < len(linhas):
            t = linhas[i].strip()
            if not t or t.startswith(("#", "|", ">", "- ", "```")) or re.match(r"^\d+\.\s", t) \
               or re.match(r"^(---|\*\*\*|___)$", t):
                break
            par.append(t)
            i += 1
        saida.append("<p>" + inline(" ".join(par)) + "</p>")
    return "\n".join(saida)


def frontmatter(texto: str) -> dict:
    m = re.match(r"^---\s*$(.*?)^---\s*$", texto, re.S | re.M)
    if not m:
        return {}
    fm = {}
    for ln in m.group(1).split("\n"):
        mm = re.match(r"^([\w-]+):\s*(.*)$", ln)
        if mm:
            fm[mm.group(1)] = mm.group(2).strip().strip('"').strip("'")
    return fm


def sem_frontmatter(texto: str) -> str:
    return re.sub(r"^---\s*$.*?^---\s*$\s*", "", texto, count=1, flags=re.S | re.M)


CSS = """
:root{--fg:#1a1a1a;--mut:#5d6470;--lin:#d8dbe0;--bg:#fbfbfa;--ac:#1f5f4e;--ac2:#eef5f2;--warn:#8a4b00;--warnbg:#fdf4e7}
*{box-sizing:border-box}
body{margin:0;font:16px/1.62 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:var(--fg);background:#fff}
header{padding:18px 22px 14px;border-bottom:1px solid var(--lin);background:var(--bg)}
header h1{margin:0 0 4px;font-size:23px;letter-spacing:-.2px}
header p{margin:0;color:var(--mut);font-size:14px}
nav{display:flex;flex-wrap:wrap;gap:5px;padding:9px 22px;border-bottom:1px solid var(--lin);position:sticky;top:0;background:#fff;z-index:5}
nav button{border:1px solid var(--lin);background:#fff;color:var(--fg);padding:6px 10px;border-radius:999px;cursor:pointer;font-size:13px;white-space:nowrap}
nav button[aria-selected=true]{background:var(--ac);border-color:var(--ac);color:#fff}
main{max-width:900px;margin:0 auto;padding:18px 22px 70px}
section[hidden]{display:none}
h2{font-size:20px;margin:28px 0 10px;padding-bottom:6px;border-bottom:1px solid var(--lin)}
h3{font-size:16.5px;margin:22px 0 8px}
p{margin:0 0 12px}
ul,ol{margin:0 0 14px;padding-left:22px}
li{margin:4px 0}
code{background:#f1f3f5;padding:1px 5px;border-radius:4px;font-size:13.5px}
pre{background:#f6f7f8;padding:12px;border-radius:8px;overflow:auto;font-size:12.5px}
blockquote{margin:0 0 14px;padding:10px 14px;background:var(--ac2);border-left:3px solid var(--ac);border-radius:0 6px 6px 0}
table{border-collapse:collapse;width:100%;margin:0 0 16px;font-size:14px}
th,td{border:1px solid var(--lin);padding:7px 9px;text-align:left;vertical-align:top}
th{background:#f3f5f7}
.nota{background:var(--warnbg);border:1px solid #f0d9b8;color:var(--warn);padding:12px 14px;border-radius:8px;margin:0 0 18px;font-size:14.5px}
.ok{background:var(--ac2);border:1px solid #cfe3da;padding:12px 14px;border-radius:8px;margin:0 0 18px;font-size:14.5px}
.slide{border:1px solid var(--lin);border-radius:12px;padding:18px;margin:0 0 12px;background:var(--bg)}
.slide .n{font-size:12px;color:var(--mut);letter-spacing:.08em;text-transform:uppercase}
.slide .t{font-size:18px;line-height:1.4;margin:8px 0 10px}
.slide .f{font-size:12.5px;color:var(--mut);border-top:1px dashed var(--lin);padding-top:8px}
.slide .f code{font-size:12px}
.mono{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12.5px;word-break:break-all}
footer{border-top:1px solid var(--lin);padding:16px 22px;color:var(--mut);font-size:12.5px;text-align:center}
@media(max-width:520px){header h1{font-size:21px}main{padding:18px 14px 60px}nav{padding:10px 14px}}
"""


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--raiz", default="../..")
    ap.add_argument("--lote", default=str(AQUI / "LOTE_PILOTO_BAMBU_E1.json"))
    ap.add_argument("--saida", default=str(AQUI / "PILOTO_BAMBU_E1.html"))
    a = ap.parse_args(argv)
    raiz = Path(a.raiz).resolve()
    lote = json.loads(Path(a.lote).read_text(encoding="utf-8"))

    montador = AQUI.parent / "montar_lote.py"
    res = subprocess.run([sys.executable, "-B", str(montador), "--lote", a.lote, "--raiz", str(raiz)],
                         capture_output=True, text=True)
    try:
        portoes = json.loads(res.stdout)
    except json.JSONDecodeError:
        portoes = {"erros": [res.stderr[:500]], "verificadas": 0, "liberadas": 0}

    peca = lote["pecas"][0]
    art_path = raiz / peca["deriva_de"]["path"]
    eda_path = raiz / peca["colecao"]["estado_da_arte"]
    art_txt = art_path.read_text(encoding="utf-8")
    eda_txt = eda_path.read_text(encoding="utf-8")
    art_fm = frontmatter(art_txt)
    eda_fm = frontmatter(eda_txt)

    gaveta = eda_path.parent
    fichas = []
    for f in sorted(gaveta.glob("*.md")):
        fm = frontmatter(f.read_text(encoding="utf-8"))
        fichas.append({
            "arquivo": f.name,
            "tipo": fm.get("tipo_documental", "—"),
            "estado": fm.get("estado_documental", "—"),
            "titulo": fm.get("titulo", fm.get("title", ""))[:110],
        })

    slides = []
    for it in peca["itens"]:
        slides.append(f"""<div class="slide"><div class="n">Slide {it['ordem']:02d}</div>
<div class="t">{esc(it['texto_curto'])}</div>
<div class="f">verificação textual: <code>{esc(it['fonte'])}</code></div></div>""")

    pend = "".join(f"<li>{esc(x)}</li>" for x in portoes.get("pendencias_de_liberacao", []))
    erros = portoes.get("erros", [])
    bloco_erros = ("<div class='ok'><b>Nenhum bloqueio material.</b> A peça passou por P0–P5: "
                   "estrutura, origem, coleção, formato e verificação textual das fontes.</div>"
                   if not erros else
                   "<div class='nota'><b>Bloqueios materiais:</b><ul>" +
                   "".join(f"<li>{esc(e)}</li>" for e in erros) + "</ul></div>")

    tab_fichas = "".join(
        f"<tr><td class='mono'>{esc(f['arquivo'])}</td><td>{esc(f['tipo'])}</td><td>{esc(f['estado'])}</td></tr>"
        for f in fichas)

    doc = f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Piloto Bambu Estrutural — esteira editorial</title>
<style>{CSS}</style></head><body>
<header>
<h1>Piloto: Bambu Estrutural</h1>
<p>Cadeia editorial com material real do Acervo — estado da arte → artigo didático → carrossel.<br>
Lote&nbsp;<code>{esc(lote['lote'])}</code> · {esc(lote.get('status',''))}</p>
</header>
<nav role="tablist">
<button data-tab="t1" aria-selected="true">1 · Estado da cadeia</button>
<button data-tab="t2" aria-selected="false">2 · Carrossel</button>
<button data-tab="t3" aria-selected="false">3 · Artigo didático</button>
<button data-tab="t4" aria-selected="false">4 · Estado da arte</button>
<button data-tab="t5" aria-selected="false">5 · Fontes da gaveta</button>
<button data-tab="t6" aria-selected="false">6 · Verificação</button>
</nav>
<main>

<section id="t1">
<h2>Estado da cadeia</h2>
<div class="nota"><b>Este material não está publicado e não está homologado.</b>
Além disso, o piloto não é uma autorização: a liberação para publicação é ato humano e
não foi registrada.</div>
{bloco_erros}
<h3>O caminho percorrido</h3>
<ul>
<li><b>Fichas e fontes</b> — {len(fichas)} documentos na gaveta <code>{esc(gaveta.name)}</code>, com fonte integral conferida.</li>
<li><b>Estado da arte</b> — <code>{esc(eda_path.name)}</code>, estado <code>{esc(eda_fm.get('estado_documental','—'))}</code>.</li>
<li><b>Artigo didático</b> — <code>{esc(art_path.name)}</code>, estado <code>{esc(art_fm.get('estado_documental','—'))}</code>, escrito para leitor não especialista.</li>
<li><b>Peça de mídia</b> — carrossel de {len(slides)} slides, derivado do artigo; cada slide cita no corpo do artigo a fonte que afirma.</li>
<li><b>Verificação automática</b> — {portoes.get('verificadas', 0)} peça verificada, {portoes.get('liberadas', 0)} liberada, {portoes.get('prontas_para_liberacao', 0)} pronta aguardando liberação.</li>
</ul>
<h3>O que falta para publicar</h3>
<ul>{pend or "<li>nada pendente</li>"}</ul>
<h3>Por que está assim</h3>
<p>A coleção está em revisão documental. A esteira foi ajustada para <b>não impedir o trabalho editorial</b>
enquanto isso: a peça é produzida e verificada, e a publicação fica condicionada à homologação e ao ato
de liberação. Antes, o estado em revisão derrubava a peça — o que transformava homologação em pedágio
de produção.</p>
</section>

<section id="t2" hidden>
<h2>Carrossel — {len(slides)} slides</h2>
<p>Texto de cada slide e a frase que o sustenta no artigo. A verificação do portão é textual:
confere que a frase existe no corpo do artigo; não julga o sentido.</p>
{''.join(slides)}
<h3>Legenda</h3>
<p>{esc(peca.get('legenda',''))}</p>
<p class="mono">{esc(' '.join(peca.get('hashtags',[])))}</p>
</section>

<section id="t3" hidden>
<h2>Artigo didático</h2>
{md_para_html(sem_frontmatter(art_txt))}
</section>

<section id="t4" hidden>
<h2>Estado da arte</h2>
{md_para_html(sem_frontmatter(eda_txt))}
</section>

<section id="t5" hidden>
<h2>Fontes da gaveta</h2>
<p>{len(fichas)} documentos em <code>{esc(gaveta.name)}</code>. Tipo e estado vêm do frontmatter de cada arquivo —
é a natureza efetiva do documento, não o que a peça declara.</p>
<table><thead><tr><th>Arquivo</th><th>Tipo</th><th>Estado</th></tr></thead><tbody>{tab_fichas}</tbody></table>
</section>

<section id="t6" hidden>
<h2>Verificação</h2>
<h3>Saída do montador</h3>
<pre>{esc(json.dumps(portoes, ensure_ascii=False, indent=1))}</pre>
<h3>Hashes</h3>
<table><thead><tr><th>Objeto</th><th>sha256</th></tr></thead><tbody>
<tr><td>Peça (lote)</td><td class="mono">{esc(peca.get('sha256_da_peca',''))}</td></tr>
<tr><td>Artigo (origem)</td><td class="mono">{esc(peca['deriva_de']['sha256'])}</td></tr>
<tr><td>Estado da arte</td><td class="mono">{hashlib.sha256(eda_path.read_bytes()).hexdigest()}</td></tr>
</tbody></table>
<p class="mono">O hash prova integridade do conteúdo. Não prova identidade nem consentimento.</p>
<h3>O que cada portão perguntou</h3>
<ul>
<li><b>P0</b> — estrutura fechada, id único, limites declarados.</li>
<li><b>P1</b> — a origem é documento editorial de verdade (o tipo no frontmatter da origem, não o declarado pela peça).</li>
<li><b>P2</b> — a origem existe e o sha256 confere.</li>
<li><b>P3</b> — estado da arte e artigo distintos, cada um resolvendo, e pertencentes à coleção.</li>
<li><b>P4</b> — formato coerente com o número de itens.</li>
<li><b>P5</b> — cada fonte citada aparece literalmente no corpo da origem.</li>
<li><b>P6</b> — liberação registrada, com autoridade, data, canal e hash do conteúdo.</li>
</ul>
</section>

</main>
<footer>Gerado por <code>gerar_piloto_html.py</code> a partir dos arquivos do repositório. Sem links externos, sem dependências.</footer>
<script>
const botoes=[...document.querySelectorAll('nav button')];
botoes.forEach(b=>b.addEventListener('click',()=>{{
  botoes.forEach(o=>o.setAttribute('aria-selected', String(o===b)));
  document.querySelectorAll('main section').forEach(s=>{{s.hidden = s.id!==b.dataset.tab;}});
  window.scrollTo({{top:0,behavior:'instant'}});
}}));
</script>
</body></html>
"""
    Path(a.saida).write_text(doc, encoding="utf-8")
    print(json.dumps({"saida": str(Path(a.saida).resolve()), "bytes": len(doc.encode()),
                      "slides": len(slides), "fichas": len(fichas),
                      "verificadas": portoes.get("verificadas"),
                      "liberadas": portoes.get("liberadas")}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
