#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera a peça HTML única do comparativo mecânico de bambu (Ásia x América do Sul).

Saída: comparativo-mecanica-bambu.html (arquivo único, offline, abas como páginas).
"""
import html
import json
import os
import re
import sys

W = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, W)
import aba_especies_dados as DADOS
import aba_estruturas_dados as ESTRUT
import derivar_numeros as NUM
SKILL = "/Users/fabiotakwara/.hermes/cache/scratch/acervo_main"

PAGINAS = [
    ("p-apresentacao", "Apresentação"),
    ("p-corpus", "Corpus"),
    ("p-metodo", "Método"),
    ("p-origem", "Origem das espécies"),
    ("p-comparativo", "Comparativo"),
    ("p-especies", "Espécies, uma a uma"),
    ("p-nativas", "Nativas"),
    ("p-inversao", "A inversão"),
    ("p-contagem", "Contagem"),
    ("p-achados", "Achados"),
    ("p-limites", "Limites"),
    ("p-adendo", "Bambu exótico"),
    ("p-artigo", "Artigo didático"),
    ("p-l21", "Lacuna 21"),
    ("p-estruturas", "Estruturas"),
    ("p-artefatos", "Artefatos"),
    ("p-c5", "Carrossel 1"),
    ("p-c6", "Carrossel 2"),
    ("p-c7", "Carrossel 3"),
]


def esc(s):
    return html.escape(s, quote=False)


def inline(t):
    """Enfase sem cruzar fronteiras: negrito externo, italico interno, e o caso ***a***."""
    t = esc(t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*\*([^*\n]+?)\*\*\*", r"<em><strong>\1</strong></em>", t)
    # negrito que contem italico dentro: **texto *com* enfase** -> preserva o interno
    t = re.sub(
        r"(?<![\w*])\*\*(.+?)\*\*(?![\w*])",
        lambda m: "<strong>" + re.sub(r"(?<![\w*])\*([^*\n]+?)\*(?![\w*])", r"<em>\1</em>", m.group(1)) + "</strong>",
        t,
        flags=re.S,
    )
    t = re.sub(r"(?<![\w*])\*([^*\n]+?)\*(?![\w*])", r"<em>\1</em>", t)
    t = re.sub(r"(?<![\w_])_([^_\n]+?)_(?![\w_])", r"<em>\1</em>", t)
    return t


def celulas(linha):
    """Divide linha de tabela markdown preservando `|` dentro de code."""
    s = linha.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    partes, buf, dentro = [], "", False
    for ch in s:
        if ch == "`":
            dentro = not dentro
            buf += ch
        elif ch == "|" and not dentro:
            partes.append(buf.strip())
            buf = ""
        else:
            buf += ch
    partes.append(buf.strip())
    return partes


def tabela(linhas):
    head = celulas(linhas[0])
    body = [celulas(l) for l in linhas[2:]]
    out = ['<div class="tabwrap"><table><thead><tr>']
    for c in head:
        out.append(f'<th>{inline(c)}</th>')
    out.append("</tr></thead><tbody>")
    for cells in body:
        out.append("<tr>")
        for k, c in enumerate(cells):
            rot = head[k] if k < len(head) else ""
            out.append(f'<td data-l="{html.escape(rot, quote=True)}">{inline(c)}</td>')
        out.append("</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


def md_para_html(md):
    md = re.sub(r"^---\n.*?\n---\n", "", md, flags=re.S)
    linhas = md.split("\n")
    out, i = [], 0
    while i < len(linhas):
        l = linhas[i]
        if l.startswith("# "):
            i += 1
            continue
        if l.startswith("#### "):
            out.append(f"<h4>{inline(l[5:])}</h4>")
            i += 1
            continue
        if l.startswith("### "):
            out.append(f"<h3>{inline(l[4:])}</h3>")
            i += 1
            continue
        if l.startswith("## "):
            out.append(f"<h3>{inline(l[3:])}</h3>")
            i += 1
            continue
        if l.startswith("|"):
            bloco = []
            while i < len(linhas) and linhas[i].startswith("|"):
                bloco.append(linhas[i])
                i += 1
            if len(bloco) >= 2 and re.match(r"^\|[\s:|-]+\|?$", bloco[1].strip()):
                out.append(tabela(bloco))
            else:
                out.append("<p>" + "<br>".join(inline(b) for b in bloco) + "</p>")
            continue
        if l.startswith(">"):
            bloco = []
            while i < len(linhas) and linhas[i].startswith(">"):
                bloco.append(linhas[i].lstrip(">").strip())
                i += 1
            out.append('<blockquote>' + inline(" ".join(bloco)) + "</blockquote>")
            continue
        if re.match(r"^\s*[-*]\s+", l):
            out.append("<ul>")
            while i < len(linhas) and re.match(r"^\s*[-*]\s+", linhas[i]):
                # item pode continuar na linha seguinte (hard wrap do .md), indentado
                item = re.sub(r"^\s*[-*]\s+", "", linhas[i])
                i += 1
                while (
                    i < len(linhas)
                    and linhas[i].strip()
                    and not re.match(r"^(\s*[-*]\s+|\s*\d+\.\s+|#|\||>|---)", linhas[i])
                ):
                    item += " " + linhas[i].strip()
                    i += 1
                out.append("<li>" + inline(item) + "</li>")
            out.append("</ul>")
            continue
        if re.match(r"^\s*\d+\.\s+", l):
            out.append("<ol>")
            while i < len(linhas) and re.match(r"^\s*\d+\.\s+", linhas[i]):
                item = re.sub(r"^\s*\d+\.\s+", "", linhas[i])
                i += 1
                while (
                    i < len(linhas)
                    and linhas[i].strip()
                    and not re.match(r"^(\s*[-*]\s+|\s*\d+\.\s+|#|\||>|---)", linhas[i])
                ):
                    item += " " + linhas[i].strip()
                    i += 1
                out.append("<li>" + inline(item) + "</li>")
            out.append("</ol>")
            continue
        if l.strip() == "---":
            out.append('<hr class="sep">')
            i += 1
            continue
        if l.strip() == "":
            i += 1
            continue
        # Parágrafo quebrado em várias linhas (hard wrap do .md) precisa ser juntado
        # antes do inline: senão cada linha vira um <p> e o **negrito** nunca fecha.
        bloco = [l.strip()]
        i += 1
        while i < len(linhas) and linhas[i].strip() and not re.match(
            r"^(#|\||>|\s*[-*]\s|\s*\d+\.\s|---)", linhas[i].strip()
        ):
            bloco.append(linhas[i].strip())
            i += 1
        out.append("<p>" + inline(" ".join(bloco)) + "</p>")
    return limpar_numeros("\n".join(out))


CSS = """
:root{
  --bg:#f7f6f2; --bg2:#efeee8; --card:#fff; --ink:#1d1c1a; --ink2:#57544d;
  --line:#d9d6cc; --accent:#1f5f4e; --accent-l:#2b7f68; --accent-d:#14453a;
  --warn:#8a4b12; --warn-bg:#fdf3e6; --danger:#8c2b1e; --danger-bg:#fceeec;
  --ok:#1f5f4e; --ok-bg:#eaf4ef;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);
  font:17px/1.62 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue","Noto Sans",Arial,sans-serif;
  font-feature-settings:"kern" 1}
header.top{background:var(--accent-d);color:#f2f0ea;padding:26px 22px 20px;border-bottom:4px solid var(--accent-l)}
header.top .kicker{font:600 12px/1 ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.16em;
  text-transform:uppercase;color:#9fc9bb;margin-bottom:10px}
header.top h1{margin:0 0 8px;font-size:29px;line-height:1.2;font-weight:650;letter-spacing:-.01em}
header.top .sub{margin:0;color:#cfd8d3;font-size:16px;max-width:62ch}
.chips{display:flex;flex-wrap:wrap;gap:7px;margin-top:16px;align-items:flex-start}
.chip{background:rgba(255,255,255,.11);border:1px solid rgba(255,255,255,.22);color:#e8efe9;
  padding:4px 10px;border-radius:999px;font:600 12px/1.5 ui-monospace,SFMono-Regular,Menlo,monospace;
  white-space:nowrap}
.chip--gold{background:#e8d7a8;border-color:#c9b478;color:#3d2f0d}
nav.tabs{position:sticky;top:0;z-index:20;background:var(--bg2);border-bottom:1px solid var(--line);
  display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:6px;padding:10px 12px}
nav.tabs button{appearance:none;border:1px solid var(--line);background:var(--card);color:var(--ink2);
  font:600 12.5px/1.25 inherit;padding:8px 6px;border-radius:8px;cursor:pointer;text-align:center;
  overflow-wrap:anywhere;hyphens:auto}
nav.tabs button[aria-selected="true"]{background:var(--accent);border-color:var(--accent);color:#fff}
main{max-width:1080px;margin:0 auto;padding:0 20px 80px}
section[role="tabpanel"]{display:none;scroll-margin-top:180px}
section[role="tabpanel"].active{display:block;animation:fade .18s ease}
@keyframes fade{from{opacity:.4}to{opacity:1}}
h2{font-size:25px;line-height:1.25;margin:32px 0 6px;letter-spacing:-.01em}
h2 .num{display:inline-block;background:var(--accent);color:#fff;font:700 13px/1 ui-monospace,Menlo,monospace;
  padding:5px 8px;border-radius:6px;margin-right:10px;vertical-align:3px}
h3{font-size:19.5px;margin:30px 0 8px;color:var(--accent-d);letter-spacing:-.005em}
h4{font-size:16.5px;margin:22px 0 6px;color:var(--ink)}
p{margin:11px 0}
ul,ol{margin:11px 0 11px 22px;padding:0}
li{margin:5px 0}
hr.sep{border:0;border-top:1px solid var(--line);margin:30px 0}
em{font-style:italic}
code{font:600 14px/1.4 ui-monospace,SFMono-Regular,Menlo,monospace;background:var(--bg2);
  padding:1px 5px;border-radius:4px;overflow-wrap:anywhere}
a{color:var(--accent);text-decoration:underline;text-underline-offset:2px}
blockquote{margin:16px 0;padding:13px 17px;background:var(--bg2);border-left:3px solid var(--accent-l);
  border-radius:0 8px 8px 0;color:var(--ink2);font-size:16px}
.tabwrap{overflow-x:auto;margin:16px 0;border:1px solid var(--line);border-radius:9px;background:var(--card)}
table{border-collapse:collapse;width:100%;font-size:14.5px;min-width:520px}
th,td{padding:9px 11px;text-align:left;border-bottom:1px solid var(--line);vertical-align:top}
th{background:var(--bg2);font-weight:650;font-size:13px;letter-spacing:.02em;
  position:sticky;top:0}
tbody tr:last-child td{border-bottom:0}
tbody tr:nth-child(even){background:#fbfaf7}
.note,.okbox,.danger{margin:18px 0;padding:14px 17px;border-radius:9px;font-size:15.5px;line-height:1.55}
.note{background:var(--warn-bg);border:1px solid #e6c9a4;border-left:4px solid var(--warn)}
.note>strong:first-child{display:block;color:var(--warn);margin-bottom:4px}
.okbox{background:var(--ok-bg);border:1px solid #bcdccd;border-left:4px solid var(--ok)}
.okbox>strong:first-child{display:block;color:var(--accent-d);margin-bottom:4px}
.danger{background:var(--danger-bg);border:1px solid #e8bdb6;border-left:4px solid var(--danger)}
.danger>strong:first-child{display:block;color:var(--danger);margin-bottom:4px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:22px 0}
.kpi{background:var(--card);border:1px solid var(--line);border-radius:11px;padding:15px 16px}
.kpi .n{font:700 27px/1.05 ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--accent-d);
  letter-spacing:-.02em;overflow-wrap:anywhere}
.kpi .l{font-size:12px;text-transform:uppercase;letter-spacing:.09em;color:var(--ink2);margin-top:7px;
  line-height:1.35}
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;margin:18px 0}
.card{background:var(--card);border:1px solid var(--line);border-radius:11px;padding:16px 18px}
.card h4{margin-top:0}
.card .tag{font:600 11.5px/1 ui-monospace,Menlo,monospace;text-transform:uppercase;letter-spacing:.1em;
  color:var(--accent-l)}
.page-nav{display:flex;justify-content:space-between;gap:12px;margin:44px 0 0;padding-top:20px;
  border-top:1px solid var(--line)}
.page-nav a,.page-nav span{font:600 14px/1.3 inherit;padding:11px 15px;border-radius:9px;
  border:1px solid var(--line);background:var(--card);color:var(--accent);text-decoration:none}
.page-nav span{color:#a9a59b;background:transparent;border-color:transparent}
footer.rodape{margin:40px 0 0;padding:18px 0 0;border-top:1px solid var(--line);
  font-size:13px;color:var(--ink2);line-height:1.6}
.meta{font:600 12.5px/1.4 ui-monospace,Menlo,monospace;color:var(--ink2);letter-spacing:.01em;
  margin:0 0 14px}
@media(max-width:1000px){nav.tabs{grid-template-columns:repeat(4,minmax(0,1fr))}}
@media(max-width:760px){
  body{font-size:16px;line-height:1.6}
  header.top{padding:20px 16px 16px}
  header.top h1{font-size:22px;line-height:1.32}
  header.top .sub{font-size:14.5px}
  nav.tabs{grid-template-columns:repeat(3,minmax(0,1fr));padding:6px;gap:4px}
  nav.tabs button{font-size:10.5px;padding:6px 3px;line-height:1.2;letter-spacing:-.01em}
  nav.tabs button[aria-selected="true"]{font-size:10.5px}
  main{padding:0 15px 70px}
  h2{font-size:21px;margin-top:24px}
  h3{font-size:17.5px}
  section[role="tabpanel"]{scroll-margin-top:210px}
  .tabwrap{overflow-x:visible;border:0;background:transparent}
  table{min-width:0;display:block;font-size:14.5px}
  thead{display:none}
  tbody,tr,td{display:block;width:100%}
  tr{background:var(--card);border:1px solid var(--line);border-radius:9px;margin-bottom:10px;padding:4px 0}
  tbody tr:nth-child(even){background:var(--card)}
  td{border:0;padding:7px 13px;display:block}
  td>*{display:inline}
  td::before{content:attr(data-l);display:block;font:600 11.5px/1.45 ui-monospace,Menlo,monospace;
    color:var(--ink2);text-transform:uppercase;letter-spacing:.05em;overflow-wrap:anywhere;margin-bottom:3px}
  td code{overflow-wrap:anywhere;word-break:break-word}
  th{position:static}
  .page-nav{flex-direction:column}
}
@media(max-width:420px){
  header.top h1{font-size:19.5px}
  .kpi .n{font-size:23px}
}
@media print{
  nav.tabs,.page-nav{display:none}
  section[role="tabpanel"]{display:block !important;page-break-after:always}
  section[role="tabpanel"]:last-child{page-break-after:auto}
  header.top{background:#fff;color:#000;border-bottom:2px solid #000}
  header.top h1,header.top .sub{color:#000}
  .chip{background:#eee;color:#000;border-color:#999}
  a{color:#000}
  .tabwrap{overflow:visible}
  table{min-width:0}
}
"""

JS = """
(function(){
  var TABS = __TABS__;
  var nav = document.querySelector('nav.tabs');
  var secs = Array.prototype.slice.call(document.querySelectorAll('section[role="tabpanel"]'));
  function abrir(id, push){
    var alvo = document.getElementById(id);
    if(!alvo){ return; }
    secs.forEach(function(s){ s.classList.toggle('active', s.id===id); });
    Array.prototype.forEach.call(nav.querySelectorAll('button'), function(b){
      var on = b.getAttribute('data-tab')===id;
      b.setAttribute('aria-selected', on ? 'true':'false');
      b.setAttribute('tabindex', on ? '0':'-1');
      if(on){ b.setAttribute('aria-current','page'); } else { b.removeAttribute('aria-current'); }
    });
    if(push){ location.hash = id; }
    requestAnimationFrame(function(){ window.scrollTo(0,0); });
  }
  nav.addEventListener('click', function(ev){
    var b = ev.target.closest ? ev.target.closest('button[data-tab]') : null;
    if(b){ abrir(b.getAttribute('data-tab'), true); }
  });
  document.addEventListener('click', function(ev){
    var a = ev.target.closest ? ev.target.closest('a[href^="#"]') : null;
    if(a){
      var id = a.getAttribute('href').slice(1);
      if(document.getElementById(id)){ ev.preventDefault(); abrir(id, true); }
    }
  });
  window.addEventListener('hashchange', function(){ abrir((location.hash||'').slice(1)||TABS[0][0], false); });
  window.addEventListener('pageshow', function(){ abrir((location.hash||'').slice(1)||TABS[0][0], false); });
  document.addEventListener('DOMContentLoaded', function(){
    abrir((location.hash||'').slice(1)||TABS[0][0], false);
  });
})();
"""


def nav_html():
    b = []
    for pid, rot in PAGINAS:
        b.append(
            f'<button type="button" role="tab" data-tab="{pid}" aria-controls="{pid}" '
            f'aria-selected="false" tabindex="-1">{rot}</button>'
        )
    return '<nav class="tabs" role="tablist" aria-label="Páginas">' + "".join(b) + "</nav>"


def page_nav(idx):
    ant = '<span>—</span>'
    prox = '<span>—</span>'
    if idx > 0:
        ant = f'<a href="#{PAGINAS[idx-1][0]}">← {PAGINAS[idx-1][1]}</a>'
    if idx < len(PAGINAS) - 1:
        prox = f'<a href="#{PAGINAS[idx+1][0]}">{PAGINAS[idx+1][1]} →</a>'
    return f'<div class="page-nav">{ant}{prox}</div>'


def secao(idx, corpo):
    pid, rot = PAGINAS[idx]
    n = f"{idx+1:02d}"
    return (
        f'<section role="tabpanel" id="{pid}" aria-labelledby="h-{pid}" class="{"active" if idx==0 else ""}">'
        f'<h2 id="h-{pid}"><span class="num">{n}</span>{rot}</h2>'
        f"{corpo}{page_nav(idx)}</section>"
    )


def corte(txt, ini, fim):
    """Recorta bloco entre dois marcadores exatos; falha alto se o marcador não existir."""
    if ini not in txt:
        raise SystemExit(f"marcador inicial ausente: {ini!r}")
    i = txt.index(ini)
    if fim is None:
        return txt[i:]
    if fim not in txt[i:]:
        raise SystemExit(f"marcador final ausente: {fim!r}")
    j = txt.index(fim, i)
    return txt[i:j]


def limpar_numeros(h):
    """A página já numera; remove o prefixo do .md ('4.1 ', '5. ') dos h3 herdados."""
    return re.sub(r"<h3>(\d+(?:\.\d+)*)\.?\s+", "<h3>", h)


# Fontes canônicas fora de _geradores/. Cópia local envelhece calada: a matriz já foi
# corrigida na fonte e o gerador continuou lendo a versão antiga.
FONTES = {
    "matriz.md": os.path.join(W, "..", "..", "matriz-comparativa-mecanica-asia-america-sul.md"),
    "ficha.md": os.path.join(W, "..", "..", "scharfenberg-2024-flexao-tres-especies-brasil.md"),
    "adendo.md": os.path.join(W, "..", "bambu-exotico-invasor-brasil-fontes.md"),
    "artigo.md": os.path.join(W, "..", "artigo-didatico-bambu.md"),
    "carrossel-5.md": os.path.join(W, "..", "carrossel-5-seu-bambu-aguenta.md"),
    "carrossel-6.md": os.path.join(W, "..", "carrossel-6-bambu-que-ninguem-cuida.md"),
    "carrossel-7.md": os.path.join(W, "..", "carrossel-7-lacuna-l21.md"),
}


def ler(nome):
    alvo = FONTES.get(nome, os.path.join(W, nome))
    with open(alvo, encoding="utf-8") as f:
        return f.read()


def pagina_especies():
    """Aba 06 — cada espécie testada, com número, equivalência, norma e uso declarado na fonte."""
    import io, contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        N = NUM.main()          # toda a aritmética vem daqui

    def g(x):
        return f"{x:,.1f}".replace(",", "X").replace(".", ",").replace("X", ".")

    h = []
    h.append(
        '<p class="meta">Toda equivalência desta página é derivada em <code>derivar_numeros.py</code>: '
        "1 MPa = 1 N/mm² = 10,197 kgf/cm²; 1 tf = 9,81 kN. Nenhum número é estimado a olho.</p>"
    )

    h.append(
        '<div class="note"><strong>Como ler um MPa antes de qualquer comparação</strong>'
        "1 MPa é 10,2 kgf/cm² — a força de dez quilos empurrando um centímetro quadrado. "
        "<strong>200 MPa</strong> são 2.039 kgf/cm², ou <strong>2,04 tf/cm²</strong>: o peso de um carro "
        "popular concentrado sobre um selo postal. "
        "<strong>90 MPa</strong> — a maior tensão de compressão entre as cinco espécies — são 0,91 tf/cm². "
        "A tensão de um bambu estrutural fica nessa ordem de grandeza: mais de uma tonelada por centímetro "
        "quadrado, e não o peso de um caminhão. Já a <em>carga</em> que um colmo aguenta chega facilmente "
        "a dez toneladas, porque a área da parede multiplica a tensão.</div>"
    )

    # ---------------- 1. Drury: compressão paralela, cinco espécies ----------------
    h.append("<h3>1. Compressão paralela em colmo inteiro — cinco espécies, quatro países de origem</h3>")
    h.append(
        "<p>Drury et al. (2023), ISO 22157:2019, seis corpos de prova por espécie, colmo inteiro. "
        "É o único ensaio do corpus que mede cinco espécies no mesmo laboratório sob o mesmo protocolo — "
        "e quatro delas são asiáticas.</p>"
    )
    h.append('<div class="tabwrap"><table><thead><tr>'
             "<th>Espécie</th><th>Tensão média</th><th>Em kgf/cm²</th><th>Área de parede</th>"
             "<th>Carga de pico no colmo</th><th>Módulo</th></tr></thead><tbody>")
    for esp in DADOS.ORDEM:
        d = N["drury"][esp]
        h.append(
            f'<tr><td data-l="Espécie">{esp}</td>'
            f'<td data-l="Tensão média"><strong>{g(d["fc_MPa"])} MPa</strong></td>'
            f'<td data-l="Em kgf/cm²">{g(d["kgf_cm2"])} kgf/cm²</td>'
            f'<td data-l="Área de parede">{d["area_mm2"]:.0f} mm²</td>'
            f'<td data-l="Carga de pico">{g(d["carga"]["kN"])} kN = <strong>{g(d["carga"]["tf"])} tf</strong></td>'
            f'<td data-l="Módulo">—</td></tr>'
        )
    h.append("</tbody></table></div>")

    h.append(
        '<div class="okbox"><strong>O exemplo que desarma a leitura ingênua</strong>'
        f'O Madake tem a maior tensão do ensaio ({g(N["drury"]["Madake"]["fc_MPa"])} MPa) e a '
        f'<em>menor</em> carga de pico: {g(N["drury"]["Madake"]["carga"]["tf"])} tf, porque o colmo tem '
        f'Ø 45 mm e apenas 739 mm² de parede. A Guadua tem tensão 31% menor '
        f'({g(N["drury"]["Guadua"]["fc_MPa"])} MPa) e carga <em>maior</em>: '
        f'{g(N["drury"]["Guadua"]["carga"]["tf"])} tf, porque o colmo tem Ø 80 mm. '
        "Quem escolhe espécie por resistência está escolhendo o número errado.</div>"
    )

    # ---------------- 2. Ficha por espécie ----------------
    h.append("<h3>2. Espécie por espécie</h3>")
    h.append(
        "<p>O que o ensaio mediu, o que o número significa na prática, e o que a fonte declara sobre uso — "
        "sem recomendação inventada pelo curador.</p>"
    )
    for esp in DADOS.ORDEM:
        d = N["drury"][esp]
        e = DADOS.DRURY_ESPECIE[esp]
        h.append('<div class="card" style="margin:16px 0">')
        h.append(f'<div class="tag">Drury 2023 · ISO 22157 · n=6</div>')
        h.append(f'<h4>{esp} — <em>{DADOS.NOMES[esp]}</em></h4>')
        h.append(f"<p><strong>Origem nativa:</strong> {e['origem']} · <strong>Corpo de prova:</strong> "
                 f"{e['diametro']}, {e['area']}</p>")
        h.append(
            f'<p><strong>Número:</strong> {g(d["fc_MPa"])} MPa de tensão média à compressão '
            f'({g(d["kgf_cm2"])} kgf/cm²). <strong>Na prática:</strong> um colmo desta seção rompe sob '
            f'carga axial de {g(d["carga"]["kN"])} kN, ou {g(d["carga"]["tf"])} tf — '
            f'aproximadamente o peso de {int(round(d["carga"]["tf"]/1.5))} carros populares empilhados '
            f'sobre a seção do colmo.</p>'
        )
        h.append(f"<p><strong>O que a fonte diz:</strong> {e['conclusao_fonte']}</p>")
        h.append("</div>")

    # ---------------- 3. Valor característico: Panti ----------------
    h.append("<h3>3. Do corpo de prova ao valor de projeto — as quatro espécies filipinas</h3>")
    h.append(
        "<p>Panti et al. (2024) fazem a operação que transforma ensaio em norma: medem a média e calculam "
        "o <strong>valor característico</strong> (percentil 5 com 75% de confiança, ISO 12122-1). "
        "A diferença entre as duas colunas é o que separa um número de laboratório de um número de projeto.</p>"
    )
    h.append('<div class="tabwrap"><table><thead><tr>'
             "<th>Espécie</th><th>n</th><th>Média</th><th>Característico f<sub>c,0,k</sub></th>"
             "<th>Redução</th><th>Carga caract. em colmo Ø80</th></tr></thead><tbody>")
    for esp, v in DADOS.PANTI_ESPECIE.items():
        d = N["panti"][esp]
        h.append(
            f'<tr><td data-l="Espécie">{v["nome"]}</td>'
            f'<td data-l="n">{v["n"]}</td>'
            f'<td data-l="Média">{g(N["panti"][esp]["fck_MPa"]*d["fator_media_para_fck"])} MPa</td>'
            f'<td data-l="Característico"><strong>{g(d["fck_MPa"])} MPa</strong></td>'
            f'<td data-l="Redução">÷{g(d["fator_media_para_fck"]).replace(",0","")}</td>'
            f'<td data-l="Carga caract.">{g(d["carga_em_colmo_80"]["tf"])} tf</td></tr>'
        )
    h.append("</tbody></table></div>")
    h.append(
        '<div class="note"><strong>Redução em cascata — o número que mais se cita errado</strong>' 
        f'Guadua das Filipinas: média {g(57.53)} MPa, característico {g(36.99)} MPa ' 
        f'(÷{g(N["controles"]["reducao_media_caracteristico"]).replace(",0","")}). ' 
        f'Guadua de Villavicencio: média 100 MPa, admissível {g(17.8)} MPa pela NSR-10 — ' 
        f'redução de {g(N["controles"]["reducao_media_admissivel"]).replace(",0","")}×. ' 
        f'Em carga, no ensaio filipino, num colmo Ø80: {g(N["controles"]["carga_media_colmo_80"]["tf"])} tf de média, ' 
        f'{g(N["controles"]["carga_caract_colmo_80"]["tf"])} tf de característica, ' 
        f'{g(N["controles"]["carga_admissivel_colmo_80"]["tf"])} tf de admissível. ' 
        "Dimensionar com a média é projetar uma estrutura várias vezes mais carregada do que a norma permite.</div>"
    )
    h.append(f"<p><strong>Uso declarado pela fonte (Panti):</strong> {DADOS.USO_FONTE['panti']}</p>")

    # ---------------- 4. Guadua x Moso, colmo inteiro ----------------
    h.append("<h3>4. Guadua × Moso no mesmo laboratório, colmo inteiro</h3>")
    h.append(
        "<p>Franck et al. (2026), ISO 22157 com correlação de imagem digital. Colmos de 3.000 mm, "
        "vão livre de 2.600 mm. É o ensaio mais controlado do corpus — e o que melhor separa "
        "<em>resistência</em> de <em>rigidez</em>.</p>"
    )
    fr = N["franck"]
    h.append('<div class="tabwrap"><table><thead><tr>'
             "<th>Propriedade</th><th>Moso</th><th>Guadua</th><th>Leitura</th></tr></thead><tbody>")
    h.append(
        f'<tr><td data-l="Propriedade">Compressão f<sub>c,0</sub> (internó)</td>'
        f'<td data-l="Moso">{g(fr["Moso"]["fc_MPa"])} MPa</td>'
        f'<td data-l="Guadua">{g(fr["Guadua"]["fc_MPa"])} MPa</td>'
        f'<td data-l="Leitura">Empate: 0,37 MPa de diferença, dentro do desvio</td></tr>'
    )
    h.append(
        f'<tr><td data-l="Propriedade">Carga axial de pico</td>'
        f'<td data-l="Moso">{g(fr["Moso"]["tf"])} tf</td>'
        f'<td data-l="Guadua">{g(fr["Guadua"]["tf"])} tf</td>'
        f'<td data-l="Leitura">Guadua fica 19% acima — o colmo dela é mais largo</td></tr>'
    )
    h.append(
        f'<tr><td data-l="Propriedade">Módulo de elasticidade (MOE)</td>'
        f'<td data-l="Moso">{g(fr["Moso"]["MOE_GPa"])} GPa</td>'
        f'<td data-l="Guadua"><strong>{g(fr["Guadua"]["MOE_GPa"])} GPa</strong></td>'
        f'<td data-l="Leitura">Guadua é {g(fr["razao_MOE"])}× mais rígida — aqui a diferença é real</td></tr>'
    )
    h.append(
        f'<tr><td data-l="Propriedade">Flexão f<sub>m,0</sub></td>'
        f'<td data-l="Moso"><strong>{g(fr["Moso"]["fm_MPa"])} MPa</strong></td>'
        f'<td data-l="Guadua">{g(fr["Guadua"]["fm_MPa"])} MPa</td>'
        f'<td data-l="Leitura">Moso {g(fr["razao_fletor"])}× mais resistente à flexão</td></tr>'
    )
    h.append(
        f'<tr><td data-l="Propriedade">Flecha no rompimento</td>'
        f'<td data-l="Moso">{g(fr["Moso"]["deflexao_mm"]).replace(".0","")} mm = vão/15</td>'
        f'<td data-l="Guadua">{g(fr["Guadua"]["deflexao_mm"]).replace(".0","")} mm = vão/45</td>'
        f'<td data-l="Leitura">Guadua deflete {g(fr["razao_deflexao"])}× menos antes de romper</td></tr>'
    )
    h.append("</tbody></table></div>")
    h.append(
        '<div class="okbox"><strong>O que esses cinco números ensinam juntos</strong>'
        "A Guadua perde em resistência (56 MPa contra 77 na flexão), ganha em rigidez "
        f"({g(fr['razao_MOE'])}×) e deflete um terço do que o Moso deflete antes de romper. "
        "Em uma viga, deflexão é o critério que costuma governar o projeto, não a ruptura. "
        "Por isso a espécie 'mais resistente' pode ser a pior escolha para vencer um vão — e vice-versa.</div>"
    )
    h.append(f"<p><strong>Uso declarado pela fonte (Franck):</strong> {DADOS.USO_FONTE['franck']}</p>")

    # ---------------- 5. Corpos pequenos: Lorenzo ----------------
    h.append("<h3>5. Corpos pequenos e fabricação robótica — o mesmo par, outro protocolo</h3>")
    h.append(
        "<p>Lorenzo et al. (2020) usam JG/T 199-2007 e calculam valor característico pelo BS EN 1990. "
        "O corpo de prova é pequeno e a fabricação é robotizada, o que reduz variabilidade. "
        "Compare com a tabela 4: mesma Guadua, mesma pergunta, números diferentes.</p>"
    )
    h.append('<div class="tabwrap"><table><thead><tr>'
             "<th>Espécie</th><th>Densidade</th><th>f<sub>c</sub> média</th><th>f<sub>c,k</sub> característico</th>"
             "<th>MOE médio</th><th>Cisalhamento</th></tr></thead><tbody>")
    for esp, v in DADOS.LORENZO_ESPECIE.items():
        d = NUM.LORENZO[esp]
        h.append(
            f'<tr><td data-l="Espécie">{esp} — <em>{v["nome"]}</em></td>'
            f'<td data-l="Densidade">{d["dens"]} kg/m³</td>'
            f'<td data-l="Média">{d["fc"]} MPa</td>'
            f'<td data-l="Característico"><strong>{d["fck"]} MPa</strong></td>'
            f'<td data-l="MOE">{d["E"]/1000:.1f} GPa</td>'
            f'<td data-l="Cisalhamento">{d["fv"]} MPa</td></tr>'
        )
    h.append("</tbody></table></div>")
    h.append(
        '<div class="note"><strong>Por que o mesmo bambu aparece com 60,73 e com 58 MPa</strong>'
        "Porque carga em corpo pequeno não é carga em colmo inteiro, e valor característico não é média. "
        "Nenhum dos dois números está errado — eles respondem a perguntas diferentes. Somar tabelas de "
        "normas distintas sem declarar o protocolo produz um número que ninguém consegue auditar.</div>"
    )
    h.append(f"<p><strong>Uso declarado pela fonte (Lorenzo):</strong> {DADOS.USO_FONTE['lorenzo']}</p>")

    # ---------------- 6. Nativas ----------------
    h.append("<h3>6. As nativas sul-americanas, uma a uma</h3>")

    h.append('<div class="card" style="margin:16px 0">')
    h.append('<div class="tag">Rodríguez-Sotelo 2023 · NTC 5525 + NTP · Ucayali, Peru</div>')
    h.append("<h4>Três Guaduas amazônicas — a mesma norma, o mesmo laboratório, e uma dispersão que ninguém esperava</h4>")
    h.append('<div class="tabwrap"><table><thead><tr>'
             "<th>Espécie</th><th>Flexão MoR (média)</th><th>Melhor nível do colmo</th>"
             "<th>MOE em flexão</th><th>Cisalhamento (c/ nó)</th></tr></thead><tbody>")
    for esp, d in NUM.RODRIGUEZ.items():
        cort = NUM.RODRIGUEZ_CORTE[esp.split()[-1]]
        h.append(
            f'<tr><td data-l="Espécie"><em>{esp}</em></td>'
            f'<td data-l="Flexão MoR"><strong>{g(d["MoR"])} MPa</strong></td>'
            f'<td data-l="Melhor nível">{g(max(d["MoR_basal"], d["MoR_cepa"]))} MPa '
            f'({"basal" if d["MoR_basal"]>d["MoR_cepa"] else "cepa"})</td>'
            f'<td data-l="MOE">{g(d["MoE"])} MPa = {d["MoE"]/1000:.2f} GPa</td>'
            f'<td data-l="Cisalhamento">{g(cort[0])} MPa</td></tr>'
        )
    h.append("</tbody></table></div>")
    h.append(
        f"<p><strong>Compressão paralela:</strong> as três espécies e os três níveis deram média estatisticamente "
        f"igual de <strong>{g(NUM.RODRIGUEZ_COMP['MoR'])} MPa</strong>, com MOE de "
        f"{g(NUM.RODRIGUEZ_COMP['MoE'])} MPa ({NUM.RODRIGUEZ_COMP['MoE']/1000:.2f} GPa). "
        "É o único caso do corpus em que três espécies do mesmo gênero foram comparadas sob protocolo único — "
        "e o resultado mais forte está na dispersão, não na média.</p>"
    )
    h.append(
        '<div class="danger"><strong>A inversão dentro do gênero</strong>'
        f"Em flexão: <em>G. superba</em> {g(NUM.RODRIGUEZ['G. superba']['MoR'])} MPa de média contra "
        f"<em>G. weberbaueri</em> {g(NUM.RODRIGUEZ['G. weberbaueri']['MoR'])} MPa. "
        f"Razão de {g(NUM.RODRIGUEZ['G. superba']['MoR']/NUM.RODRIGUEZ['G. weberbaueri']['MoR'])}× entre duas "
        "espécies do mesmo gênero, do mesmo país, ensaiadas no mesmo laboratório. "
        "Compare com a diferença entre continentes (1,15×): a variação interna é 3,5 vezes maior. "
        "Escolher 'Guadua' como se fosse uma espécie só é o erro que esse número desfaz.</div>"
    )
    h.append(f"<p><strong>Uso declarado pela fonte:</strong> {DADOS.USO_FONTE['rodriguez']}</p>")
    h.append("</div>")

    h.append('<div class="card" style="margin:16px 0">')
    h.append('<div class="tag">Rincon &amp; Choque 2025 · NTC 5525 + NSR-10 · Villavicencio, Colômbia</div>')
    h.append("<h4>Guadua angustifolia — 193 ensaios, seis sítios</h4>")
    h.append('<div class="tabwrap"><table><thead><tr>'
             "<th>Ensaio</th><th>n</th><th>Tensão média</th><th>Em kgf/cm²</th><th>CV</th></tr></thead><tbody>")
    rincon = [("Compressão paralela", 40, 100.0, 0.16), ("Compressão perpendicular", 38, 80.2, 0.20),
              ("Cisalhamento", 67, 93.3, 0.13), ("Flexão", 12, 83.6, 0.07),
              ("Tração paralela", 36, 89.9, 0.09)]
    for nome, n, v, cv in rincon:
        h.append(
            f'<tr><td data-l="Ensaio">{nome}</td><td data-l="n">{n}</td>'
            f'<td data-l="Média"><strong>{g(v)} MPa</strong></td>'
            f'<td data-l="kgf/cm²">{g(v*10.197162)} kgf/cm²</td>'
            f'<td data-l="CV">{cv:.0%}</td></tr>'
        )
    h.append("</tbody></table></div>")
    h.append(
        "<p><strong>A leitura didática:</strong> 100 MPa de compressão paralela é 1.020 kgf/cm² — uma tonelada "
        "sobre um centímetro quadrado. Mas esse é o número de laboratório. O esforço <em>admissível</em> que o "
        "artigo calcula pela NSR-10 para o mesmo material fica em <strong>17,8 MPa</strong> (182 kgf/cm²) na "
        "porção basal de Villavicencio. A distância entre os dois é de 5,6×, e é exatamente a distância entre "
        "'o que o material aguenta uma vez' e 'o que se pode projetar com segurança'.</p>"
    )
    h.append(
        "<p><strong>E o número que ninguém espera:</strong> a Guadua do sítio Oiba tem admissível de "
        "<strong>1,88 MPa</strong> na porção basal — dez vezes menos que o sítio Tolima, no mesmo país, "
        "com a mesma norma. Solo, altitude e clima mudam o material.</p>"
    )
    h.append(f"<p><strong>Uso declarado pela fonte:</strong> {DADOS.USO_FONTE['rincon']}</p>")
    h.append("</div>")

    h.append('<div class="card" style="margin:16px 0">')
    h.append('<div class="tag">Rocha &amp; Kikuti 2024 · ABNT NBR 16828 · Brasil</div>')
    h.append("<h4>Guadua chacoensis — a única nativa ensaiada sob norma brasileira</h4>")
    h.append(
        "<p>Compressão <strong>26,19 ± 5,37 MPa</strong> (267 kgf/cm²) · tração <strong>60,14 ± 18,47 MPa</strong> "
        "(613 kgf/cm²) · densidade 0,70 g/cm³ · 9,35% e 12,19% de umidade. "
        "Note a assimetria: a tração é mais que o dobro da compressão, e o desvio da tração é de 31% — "
        "o material é muito mais previsível comprimido do que tracionado.</p>"
    )
    h.append(f"<p><strong>Uso declarado pela fonte:</strong> {DADOS.USO_FONTE['rocha']}</p>")
    h.append("</div>")

    h.append('<div class="card" style="margin:16px 0">')
    h.append('<div class="tag">Poblete 2009 · DIN 52 185/186 · Chile</div>')
    h.append("<h4>Chusquea culeou — o único não-Guadua com dado mecânico no corpus</h4>")
    h.append(
        "<p>O artigo compara o colihue com madeiras chilenas e conclui que o material está no limite inferior "
        "das madeiras comerciais, similar ao álamo: <strong>superior ao álamo e inferior ao Pinus radiata em "
        "todas as propriedades</strong>. Os autores também registram que a parte externa do colmo, mais densa, "
        "foi removida para preparar os corpos de prova — o que reduz os valores medidos.</p>"
    )
    h.append(f"<p><strong>Uso declarado pela fonte:</strong> {DADOS.USO_FONTE['poblete']}</p>")
    h.append("</div>")

    h.append('<div class="card" style="margin:16px 0">')
    h.append('<div class="tag">Guiotoku 2024 · sem ensaio mecânico · Brasil</div>')
    h.append("<h4>Quatro nativas do sul do Brasil — e a razão de não terem número mecânico</h4>")
    h.append(
        "<p><em>Merostachys skvortzovii</em>, <em>Chusquea meyeriana</em>, <em>Apoclada simplex</em> e "
        "<em>Chusquea cf. gracilis</em>. O estudo mede lignina, celulose, extrativos, cinzas e elementos "
        "inorgânicos — <strong>nenhuma propriedade mecânica</strong>. Lignina entre 19,9% e 25,3%; celulose de "
        "57,3% a 63,7%; silício de 251,7 a 4.333 mg/kg, com o adulto de <em>M. skvortzovii</em> três vezes "
        "acima do juvenil.</p>"
    )
    h.append(f"<p><strong>Uso declarado pela fonte:</strong> {DADOS.USO_FONTE['guiotoku']}</p>")
    h.append(
        '<div class="note"><strong>Por que esta espécie importa para a lacuna L21</strong>'
        "Este é o material que o mapa de lacunas diz faltar — e ele está na coleção desde 2024. O que falta "
        "não é a espécie: é o ensaio mecânico. Química não substitui campanha de compressão.</div>"
    )
    h.append("</div>")

    # ---------------- 7. Normas ----------------
    h.append("<h3>7. As normas — o que cada uma diz e o que muda no número</h3>")
    h.append('<div class="tabwrap"><table><thead><tr>'
             "<th>Norma</th><th>O que é</th><th>O que muda no resultado</th></tr></thead><tbody>")
    for n, o, m in DADOS.NORMAS:
        h.append(
            f'<tr><td data-l="Norma"><strong>{n}</strong></td>'
            f'<td data-l="O que é">{o}</td>'
            f'<td data-l="O que muda">{m}</td></tr>'
        )
    h.append("</tbody></table></div>")

    # ---------------- 8. Cuidados ----------------
    h.append("<h3>8. Quatro cuidados que mudam a conclusão</h3>")
    for tit, txt in DADOS.CUIDADOS:
        cls = "danger" if "não é" in tit else "note"
        h.append(f'<div class="{cls}"><strong>{tit}</strong>{txt}</div>')

    h.append(
        '<p class="meta" style="margin-top:28px">Números desta página: Drury 2023 (Tabela 2, p.7, '
        "recalculado das 30 linhas) · Panti 2024 (Tabela 6, p.14) · Franck 2026 (Tabelas 4 e 8, p.11 e 15) · "
        "Lorenzo 2020 (Tabela 3, p.6) · Rodríguez-Sotelo 2023 (Tabelas 4–6, p.15–18) · "
        "Rincon &amp; Choque 2025 (Tabela 7, p.7; Tabela 12) · Rocha &amp; Kikuti 2024 (p.24–25) · "
        "Poblete 2009 (p.7–8) · Guiotoku 2024 (p.5–6).</p>"
    )
    return "".join(h)


def pagina_estruturas():
    """Aba 13 — elementos estruturais: o que foi ensaiado, onde, e o que não existe."""
    varredura = ESTRUT.varrer()

    h = []
    h.append(
        '<p class="meta">Varredura de 10 PDFs integrais por termos estruturais '
        "(tesoura, treliça, viga, coluna, pórtico, ligação), com filtro de falsos positivos. "
        "Resultado bruto em <code>varredura_estrutural.json</code>.</p>"
    )

    h.append(
        '<div class="danger"><strong>Resposta curta</strong>'
        "Não. O corpus tem <strong>elementos</strong> ensaiados — colmo inteiro à compressão (pilar) e à "
        "flexão (viga) — em cinco países. Não tem <strong>estruturas</strong>: nenhuma tesoura, treliça, "
        "pórtico ou ligação foi ensaiada. As 22 menções estruturais nos 10 documentos são contexto de "
        "introdução ou referência bibliográfica, não campanha de ensaio.</div>"
    )

    h.append(
        '<div class="kpis">'
        '<div class="kpi"><div class="n">3</div><div class="l">elementos com ensaio real</div></div>'
        '<div class="kpi"><div class="n">5</div><div class="l">países de ensaio</div></div>'
        '<div class="kpi"><div class="n">0</div><div class="l">treliças ensaiadas</div></div>'
        '<div class="kpi"><div class="n">0</div><div class="l">ligações ensaiadas</div></div>'
        "</div>"
    )

    # ---- tabela dos elementos ----
    h.append("<h3>1. Elementos ensaiados, espécie e localização</h3>")
    h.append(
        "<p>Cada linha é um elemento estrutural com ensaio real por trás — e a coluna de limite diz o que "
        "o ensaio não cobre. É a diferença entre <em>propriedade do material</em> e "
        "<em>desempenho de estrutura</em>.</p>"
    )
    h.append('<div class="tabwrap"><table><thead><tr>'
             "<th>Elemento</th><th>Espécies</th><th>Onde</th><th>Resultado</th>"
             "<th>O que cobre</th><th>O que não cobre</th></tr></thead><tbody>")
    for e in ESTRUT.ELEMENTOS:
        h.append(
            f'<tr><td data-l="Elemento"><strong>{e["elemento"]}</strong></td>'
            f'<td data-l="Espécies">{e["especie"]}</td>'
            f'<td data-l="Onde">{e["fonte"]}<br><span style="color:var(--ink2)">{e["local"]}</span></td>'
            f'<td data-l="Resultado">{e["resultado"]}</td>'
            f'<td data-l="O que cobre">{e["forca"]}</td>'
            f'<td data-l="O que não cobre">{e["limite"]}</td></tr>'
        )
    h.append("</tbody></table></div>")

    h.append(
        '<div class="okbox"><strong>O que essa tabela mostra sobre distribuição geográfica</strong>'
        "Os ensaios de elemento acontecem na Europa (Reino Unido, Alemanha) com material tropical, e no "
        "Brasil com material de origem asiática. Nenhum dos três elementos foi ensaiado na América do Sul "
        "com uma espécie nativa coletada localmente — a única exceção é o ensaio peruano de Rodríguez-Sotelo, "
        "que é de propriedade do material em corpo pequeno, não de elemento estrutural.</div>"
    )

    # ---- varredura ----
    h.append("<h3>2. A varredura: onde o corpus fala de estrutura e onde se cala</h3>")
    h.append(
        "<p>Contagem de menções reais por documento, depois de excluir 'coluna de tabela', 'framework', "
        "'joint research' e 'joint line' (junção de nó do colmo). Total: <strong>22 menções em 5 de 10 "
        "documentos</strong>.</p>"
    )
    h.append('<div class="tabwrap"><table><thead><tr>'
             "<th>Documento</th><th>Tesoura/treliça</th><th>Viga</th><th>Coluna/pilar</th>"
             "<th>Pórtico</th><th>Ligação</th></tr></thead><tbody>")
    fams = ["Tesoura / treliça", "Viga", "Coluna / pilar", "Pórtico / quadro", "Ligação / conexão"]
    for doc, fam in varredura.items():
        cels = "".join(
            f'<td data-l="{f}">{fam.get(f, 0) if fam.get(f, 0) else "—"}</td>' for f in fams
        )
        marca = "" if fam else ' style="color:var(--ink2)"'
        h.append(f'<tr><td data-l="Documento"><span{marca}>{doc}</span></td>{cels}</tr>')
    h.append("</tbody></table></div>")

    h.append(
        '<div class="note"><strong>Como ler a tabela de varredura</strong>'
        "Número alto não significa ensaio. Panti (7 menções a coluna) usa 'short-column' e 'long-column' "
        "para explicar modos de falha citando Li et al., não para ensaiar pilar. Franck (4 menções a "
        "ligação) dedica um parágrafo a dizer que a ligação é o gargalo — e não ensaia nenhuma. "
        "Drury (2 menções a coluna) declara o objetivo de avaliar os colmos 'as structural columns', mas o "
        "corpo de prova é de comprimento fixo, sem esbeltez variável.</div>"
    )

    # ---- o que falta ----
    h.append("<h3>3. O que falta para responder à pergunta de engenharia</h3>")
    h.append('<div class="tabwrap"><table><thead><tr>'
             "<th>Pergunta</th><th>Tem no corpus?</th><th>O que existe</th></tr></thead><tbody>")
    perguntas = [
        ("Resistência do colmo à compressão", "Sim",
         "Cinco espécies em colmo inteiro (Drury), quatro em corpo de prova (Panti), três nativas (Rodríguez-Sotelo)"),
        ("Resistência do colmo à flexão", "Sim",
         "Moso e Guadua em colmo inteiro com flecha medida (Franck)"),
        ("Resistência da lâmina ao momento fletor", "Parcial",
         "Três espécies em corpo de 1 cm (Scharfenberg) — não é viga estrutural"),
        ("Flambagem de pilar em escala real", "Não",
         "Nada. Nenhum ensaio com esbeltez variável"),
        ("Comportamento de ligação (nó de treliça)", "Não",
         "Só a declaração de Franck de que é o gargalo"),
        ("Tesoura ou treliça montada", "Não",
         "Nada. Uma menção de contexto"),
        ("Viga composta ou laminada colada estrutural", "Não",
         "Só referências bibliográficas de outros autores"),
        ("Norma de projeto para nativa brasileira", "Não",
         "ABNT NBR 16828 existe e foi usada por Rocha & Kikuti, mas só em corpo de prova"),
    ]
    for q, tem, oque in perguntas:
        cor = "var(--ok)" if tem == "Sim" else ("var(--warn)" if tem == "Parcial" else "var(--danger)")
        h.append(
            f'<tr><td data-l="Pergunta">{q}</td>'
            f'<td data-l="Tem no corpus"><strong style="color:{cor}">{tem}</strong></td>'
            f'<td data-l="O que existe">{oque}</td></tr>'
        )
    h.append("</tbody></table></div>")

    h.append(
        '<div class="danger"><strong>A consequência para a L21</strong>'
        "A lacuna não é só de campanha mecânica de material. Mesmo que se cumprisse a L21 ao pé da letra — "
        "campanha NBR 16828-1/2 em espécies nativas —, o resultado seria caracterização de material, não "
        "aptidão estrutural. Tesoura, treliça e pilar exigem mais três coisas que nenhum documento do corpus "
        "fornece: ensaio de ligação, ensaio de elemento em escala real e verificação de flambagem. "
        "É uma lacuna atrás da lacuna.</div>"
    )

    h.append("<h3>4. Onde buscar, se a pergunta virar frente</h3>")
    h.append(
        "<p>Sem inventar referência: os próprios documentos do corpus indicam para onde ir. "
        "Franck 2026 cita a aprovação técnica alemã <strong>Z-9.1-895</strong> (2020/2025) para bambu "
        "laminado (LBL) — é norma de produto, não de ligação. Panti 2024 cita Li et al. para flambagem de "
        "pilar. Drury 2023 cita a linha de padronização de colmo inteiro. Nenhum deles entrega o dado de "
        "treliça; todos apontam que ele existe fora do corpus.</p>"
    )
    h.append(
        '<div class="note"><strong>Recomendação de escopo, não de busca</strong>'
        "Se a frente quiser responder a pergunta estrutural, a ordem é: (1) ligação, porque é o que governa "
        "treliça; (2) flambagem, porque é o que governa coluna; (3) elemento montado. Começar por mais "
        "caracterização de material — que é o que os 12 PDFs já fazem — não move a resposta.</div>"
    )
    return "".join(h)



def garantir_rotulos(h):
    """Toda <td> recebe data-l derivado do <th> da própria coluna.

    Tabela empilhada em tela estreita mostra valor sem nome quando falta data-l;
    corrigir o HTML à mão se perde na próxima geração, então o rótulo é derivado aqui.
    """
    def _tab(m):
        tab = m.group(0)
        ths = re.findall(r"<th[^>]*>(.*?)</th>", tab, re.S)
        ths = [re.sub(r"<[^>]+>", "", x).strip() for x in ths]
        if not ths:
            return tab
        linha = [0]

        def _tr(mt):
            linha[0] = 0
            def _td(md):
                k = linha[0]
                linha[0] += 1
                if "data-l=" in md.group(1) or k >= len(ths):
                    return md.group(0)
                return md.group(0).replace("<td", f'<td data-l="{ths[k]}"', 1)
            return re.sub(r"<td([^>]*)>", _td, mt.group(0))
        corpo = re.sub(r"<tr>.*?</tr>", _tr, tab, flags=re.S)
        return corpo
    return re.sub(r"<table>.*?</table>", _tab, h, flags=re.S)


def main():
    matriz = ler("matriz.md")
    ficha = ler("ficha.md")
    try:
        adendo = ler("adendo.md")
    except FileNotFoundError:
        adendo = ""

    corpo = {}

    corpo["p-apresentacao"] = f"""
<p class="meta">MTCC · Bambu Science · leitura e revisão · 18 de novembro de 2026</p>
<p>Esta peça reúne o que a frente produziu ao testar uma hipótese sobre comparação internacional de
propriedades mecânicas de bambu. A pergunta era: <strong>existe um comparativo mecânico entre Ásia e América
do Sul na literatura, e o que ele mostra sobre o bambu sul-americano?</strong></p>
<p>A resposta curta: existe, mas é menor e mais estreito do que a hipótese supunha — e o achado mais forte
apareceu num lugar que não era o esperado, <em>dentro</em> do gênero <em>Guadua</em>.</p>

<div class="kpis">
  <div class="kpi"><div class="n">12</div><div class="l">PDFs lidos integralmente</div></div>
  <div class="kpi"><div class="n">4</div><div class="l">comparativos entre continentes</div></div>
  <div class="kpi"><div class="n">1,53×</div><div class="l">variação dentro de Guadua</div></div>
  <div class="kpi"><div class="n">1,15×</div><div class="l">diferença entre continentes</div></div>
</div>

<h3>O que esta peça é</h3>
<p>Um relatório de leitura de uma análise documental. Todo número vem de um PDF integral, com a página
indicada. As fontes estão custodiadas com SHA-256, e o texto de cada documento está versionado nos dois
pull requests abertos.</p>

<h3>O que esta peça não é</h3>
<ul>
  <li><strong>Não é estado da arte homologado.</strong> Documento em revisão documental.</li>
  <li><strong>Não é revisão sistemática.</strong> Doze documentos não esgotam a literatura; a busca foi por
      citação e repositório, não por varredura de bases indexadas.</li>
  <li><strong>Não fecha a lacuna L21.</strong> Ela permanece aberta — e a página 12 explica por quê.</li>
  <li><strong>Não corrige fonte de terceiro.</strong> A divergência encontrada está registrada, não
      consertada.</li>
</ul>

<h3>Como ler</h3>
<p>Quinze páginas, na ordem em que o raciocínio foi construído. Se você tem cinco minutos, leia as páginas
<strong>08 (A inversão)</strong>, <strong>10 (Achados)</strong> e <strong>12 (L21)</strong> — são as que
mudam decisão. Para a pergunta sobre tesoura, treliça, viga e coluna, a <strong>14</strong>. Para conferir espécie por espécie, com as equivalências em toneladas, a página
<strong>06</strong>. A matriz crua fica na <strong>05</strong>.</p>

<div class="note"><strong>Uma frase que resume o percurso</strong>
A hipótese de partida era "as Américas estudam mais o bambu asiático do que o nativo". A medição
confirmou uma parte e derrubou outra: o problema não é falta de estudo de nativa, é que <em>quase toda</em>
nativa estudada é uma só.</div>
"""

    corpo["p-corpus"] = md_para_html(corte(matriz, "## 1. Corpus efetivamente lido", "## 2. Nota metodológica"))
    corpo["p-corpus"] = "<h3>Os doze documentos</h3>" + corpo["p-corpus"]

    corpo["p-metodo"] = md_para_html(corte(matriz, "## 2. Nota metodológica", "## 3. Classificação de origem"))

    corpo["p-origem"] = md_para_html(corte(matriz, "## 3. Classificação de origem", "## 4. A matriz"))

    sec41 = corte(matriz, "### 4.1 Comparativos que colocam", "### 4.2 Estudos de espécies nativas")
    sec42 = corte(matriz, "### 4.2 Estudos de espécies nativas", "### 4.3 O caso que inverte")
    sec43 = corte(matriz, "### 4.3 O caso que inverte", "## 5. Contagem")
    corpo["p-comparativo"] = (
        "<h3>A matriz</h3>"
        "<p>Duas tabelas, uma pergunta cada: quem coloca Ásia e América do Sul no mesmo ensaio "
        "(4.1), e o que se sabe das nativas isoladamente (4.2). A leitura de cada uma vem logo "
        "abaixo da tabela, porque a tabela sozinha não conclui nada.</p>"
        + md_para_html(sec41).replace("<h3>4.1 ", "<h3>Comparativos que ").replace("<h3>4.2 ", "<h3>Nativas: ").replace("<h3>4.3 ", "<h3>")
        + '<div class="okbox"><strong>O que a tabela 4.1 prova</strong>'
        "Em quatro estudos, quatro países de ensaio, quatro desenhos independentes, a América do Sul "
        "comparece com <strong>uma única espécie</strong> — sempre <em>Guadua angustifolia</em>. "
        "Não existe 'Ásia × América do Sul' na literatura: existe Ásia + Guadua. "
        "A ausência do resto do continente não é falha de busca; é o desenho dos estudos.</div>"
        + md_para_html(sec42)
        + '<div class="note"><strong>O que a tabela 4.2 prova</strong>'
        "Seis espécies nativas com dado mecânico, cinco do gênero <em>Guadua</em>. Fora do gênero, "
        "exatamente uma: <em>Chusquea culeou</em>, artigo de 2009. <em>Merostachys</em>, "
        "<em>Apoclada</em>, <em>Eremocaulon</em> e <em>Glaziophyton</em> têm zero ensaio mecânico — "
        "por isso a página 06 trata cada espécie separadamente, e a página 07 mostra o que existe "
        "fora da Guadua.</div>"
        + md_para_html(sec43)
        + '<div class="danger"><strong>E a tabela 4.3 inverte a pergunta</strong>'
        "O artigo sobre 'três espécies do Brasil' declara as três como nativas, duas vezes, na página 2. "
        "As três são asiáticas pelo Kew POWO. É o único documento do corpus que trata 'espécies "
        "brasileiras' em bloco — e trata três bambus que o Brasil não tem como nativos. "
        "A ficha com a restrição de uso está no PR #97.</div>"
    )

    corpo["p-especies"] = pagina_especies()

    corpo["p-inversao"] = """
<h3>Onde os números se contradizem — e por que isso importa</h3>
<p>Três estudos medem Guadua e espécies asiáticas com rigor comparável. Lidos juntos, eles não sustentam
a pergunta "qual continente tem o bambu mais resistente".</p>

<div class="grid2">
  <div class="card">
    <div class="tag">Drury 2023 · ISO 22157</div>
    <h4>Moso ganha por 9 MPa</h4>
    <p>Média de compressão paralela em colmo inteiro, n=6 por espécie: Moso <strong>69,88</strong> MPa,
    Guadua <strong>60,73</strong> MPa. Diferença de 9,15 MPa — razão de <strong>1,15×</strong>.</p>
  </div>
  <div class="card">
    <div class="tag">Franck 2026 · DIC</div>
    <h4>Empate técnico</h4>
    <p>Moso <strong>66,72 ± 0,54</strong> MPa contra Guadua <strong>66,35 ± 3,24</strong> MPa. Diferença de
    <strong>0,37</strong> MPa — dentro do desvio.</p>
  </div>
  <div class="card">
    <div class="tag">Franck 2026 · rigidez</div>
    <h4>Aqui a diferença é grande</h4>
    <p>MOE de compressão: Guadua <strong>20,31</strong> GPa contra Moso <strong>10,99</strong> GPa —
    <strong>1,85×</strong>. Guadua é quase duas vezes mais rígida.</p>
  </div>
  <div class="card">
    <div class="tag">Rodríguez-Sotelo 2023 · mesma norma, mesmo laboratório</div>
    <h4>Dentro de Guadua: 1,53×</h4>
    <p>Flexão, mesma norma, mesmo laboratório, <strong>mesma região do colmo</strong> (média):
    <em>G. lynnclarkiae</em> <strong>21,01</strong> MPa contra <em>G. weberbaueri</em> <strong>13,77</strong> MPa.</p>
    <p class="fine">Os extremos do mesmo estudo vão de 13,77 (média de <em>G. weberbaueri</em>) a 84,49 (base de
    <em>G. superba</em>) — 6,1×, mas aí se divide base por média. Não é comparação válida, e não é a que se usa aqui.</p>
  </div>
</div>

<div class="okbox"><strong>A frase que se pode escrever</strong>
A variação dentro do gênero <em>Guadua</em> (1,53×, comparando a mesma região do colmo) é <strong>maior</strong> que
qualquer diferença entre continentes medida (1,15×). Perguntar "o bambu asiático é mais resistente que o sul-americano?" é uma
pergunta mal formada — a dispersão interna do gênero engole o efeito continental.</div>

<div class="note"><strong>Consequência prática</strong>
Dimensionar uma espécie nativa com propriedades de outra espécie do mesmo gênero é extrapolação não
verificada. É esse o risco que o número sustenta — e não o risco geográfico que o mapa de lacunas descrevia
até hoje. A rigidez, e não a resistência, é o eixo onde a diferença entre continentes aparece de forma
consistente.</div>

<p>Existe ainda um desenho que <em>mede</em> as duas espécies no mesmo laboratório sob o mesmo protocolo, e
foi reanalisado aqui: Lorenzo et al. (2020) usam fabricação robótica para reduzir variabilidade de corpo de
prova e reportam valores característicos — Oldhamii <strong>50</strong>, Moso <strong>40</strong>, Guadua
<strong>38</strong> MPa. Sob valor característico, a distância entre as duas espécies-emblema é de 2 MPa.</p>
"""

    corpo["p-contagem"] = md_para_html(corte(matriz, "## 5. Contagem", "## 6. Os três achados"))
    corpo["p-contagem"] = (
        "<h3>O que a matriz permite afirmar, linha por linha</h3>" + corpo["p-contagem"]
    )

    corpo["p-achados"] = md_para_html(corte(matriz, "## 6. Os três achados", "## 7. O que este documento"))

    corpo["p-limites"] = md_para_html(corte(matriz, "## 7. O que este documento", "## 8. Consequência"))
    corpo["p-limites"] = "<h3>O que esta análise não conclui</h3>" + corpo["p-limites"]

    corpo["p-l21"] = md_para_html(corte(matriz, "## 8. Consequência", "---"))
    corpo["p-l21"] = (
        '<div class="note"><strong>A lacuna 21, por extenso</strong>\n'
        "O Acervo mantém um mapa de lacunas: a lista do que falta na pesquisa brasileira de bambu, item por item. "
        "Esta é a <strong>lacuna número 21</strong> dessa lista — <em>caracterização mecânica própria de espécies "
        "nativas amazônicas</em>. No resto do documento ela aparece abreviada como <strong>L21</strong>: "
        "<strong>L</strong> de lacuna, <strong>21</strong> de posição. É um endereço, não um código interno.</div>"
        "<h3>A lacuna permanece aberta — e por um motivo específico</h3>"
        + corpo["p-l21"]
        + """
<div class="danger"><strong>O que a L21 pede, literalmente</strong>
Campanha de ensaios mecânicos e físicos (<strong>NBR 16828-1/2</strong>) das espécies nativas, com
identificação botânica e procedência. As seis espécies reunidas nesta análise são <em>valores de
literatura</em>, produzidos sob normas distintas e em campanhas isoladas. Reunir literatura não é executar
campanha — por isso a lacuna não fecha.</div>
<p>A reescrita da L21 será feita em documento próprio, com estas três distinções: <strong>cobertura de
espécie</strong> (o que existe além de <em>Guadua</em>), <strong>cobertura normativa</strong> (quem tem
norma de projeto, não apenas ensaio) e <strong>comparabilidade</strong> (o que pode ser somado sem
correção).</p>
"""
    )

    # página nativas: extrai a seção 4.2 e 4.3 da matriz
    corpo["p-nativas"] = (
        "<h3>As nativas, e o que existe fora da Guadua</h3>"
        "<p>A tabela com os números de cada nativa está na página 05 (seção 4.2), e a ficha "
        "espécie por espécie — com as equivalências em kgf/cm² e toneladas — está na página 06. "
        "Esta página faz a pergunta seguinte: <strong>o que isso significa para o gênero que não é "
        "Guadua?</strong></p>"
        '<div class="danger"><strong>A lacuna real não é geográfica, é de gênero</strong>'
        "O mapa de lacunas trata o problema como cobertura de país. O dado diz outra coisa: cinco das seis "
        "nativas com ensaio mecânico são <em>Guadua</em>. O continente inteiro está representado por um "
        "gênero, e dentro dele por uma espécie, a <em>G. angustifolia</em>, que é a que aparece nos quatro "
        "comparativos internacionais.</div>"
        "<h3>Os quatro gêneros sem ensaio mecânico</h3>"
        "<p><em>Merostachys</em>, <em>Apoclada</em>, <em>Eremocaulon</em> e <em>Glaziophyton</em> têm "
        "<strong>zero</strong> dado mecânico no corpus. Para dois deles existe caracterização "
        "físico-química publicada — lignina, celulose, extrativos, elementos inorgânicos — mas química "
        "não é resistência. Nenhum desses gêneros tem norma de projeto em nenhum país.</p>"
        '<div class="note"><strong>Por que a química não substitui o ensaio</strong>'
        "Guiotoku et al. (2024) medem lignina entre 19,9% e 25,3% e celulose entre 57,3% e 63,7% para "
        "quatro nativas do sul do Brasil. É dado valioso para seleção de matéria-prima e para pirólise. "
        "Não permite calcular tensão admissível, módulo de elasticidade nem carga de ruptura — e portanto "
        "não permite dimensionar nada.</div>"
        "<h3>O único não-Guadua com dado mecânico</h3>"
        "<p><em>Chusquea culeou</em> (Poblete et al. 2009, Chile): o artigo conclui que o colihue está no "
        "limite inferior das madeiras comerciais, similar ao álamo e inferior ao <em>Pinus radiata</em> em "
        "todas as propriedades, e indica uso em painéis decorativos, artesanato e partes de móveis. "
        "É o único dado mecânico fora do gênero <em>Guadua</em> em dezessete anos de literatura no corpus.</p>"
    )

    corpo["p-estruturas"] = pagina_estruturas()

    corpo["p-artefatos"] = """
<h3>O que foi produzido e onde está</h3>
<div class="tabwrap"><table>
<thead><tr><th>Artefato</th><th>Estado</th><th>Caminho</th></tr></thead>
<tbody>
<tr><td>Matriz comparativa</td><td>PR #96 · validate SUCCESS · MERGEABLE</td>
    <td><code>docs/analyses/bambu-estrutural/matriz-comparativa-mecanica-asia-america-sul.md</code></td></tr>
<tr><td>Ficha Scharfenberg 2024</td><td>PR #97 · validate SUCCESS · MERGEABLE</td>
    <td><code>docs/analyses/bambu-estrutural/scharfenberg-2024-flexao-tres-especies-brasil.md</code></td></tr>
<tr><td>Custódia dos 12 PDFs</td><td>local, <code>_privado/</code></td>
    <td><code>_privado/fontes-documentais/comparativo-mecanica-2026-11/</code></td></tr>
<tr><td>Manifesto de custódia</td><td>SHA-256 por arquivo</td>
    <td><code>_privado/fontes-documentais/comparativo-mecanica-2026-11/MANIFESTO_CUSTODIA.json</code></td></tr>
</tbody></table></div>

<h3>Os dois pull requests</h3>
<p>Ambos abertos, ambos com CI verde, nenhum mergeado. A separação é deliberada: a matriz é evidência
versionada; a ficha é restrição de uso de uma fonte. Uma não depende da outra para existir.</p>
<ul>
  <li><strong>PR #96 — matriz comparativa.</strong> +204 −0, 1 arquivo. Dois commits: o documento e uma
      correção de substância que declara a L21 aberta e torna a lacuna visível na contagem.</li>
  <li><strong>PR #97 — ficha Scharfenberg.</strong> +165 −0, 1 arquivo. A restrição de origem está no
      frontmatter e numa seção própria.</li>
</ul>

<h3>O que ficou fora, de propósito</h3>
<ul>
  <li>Reescrita da L21 — documento próprio, depois da matriz.</li>
  <li>Edição do <code>mapa-de-lacunas.md</code> — não tocado.</li>
  <li>Entrada no <code>index.md</code> do eixo — depois do merge, senão cria link quebrado.</li>
  <li>Erratum ou carta ao periódico sobre a classificação de origem — frente separada, decisão sua.</li>
  <li>Fichas das outras cinco fontes novas — PR próprio.</li>
</ul>

<div class="note"><strong>Aguardando decisão</strong>
Autorizar o merge dos dois PRs. Depois disso, o próximo passo é o PR da L21 reescrita citando a matriz.</div>
"""

    corpo["p-adendo"] = md_para_html(corte(ler("adendo.md"), "## Duas espécies, dois comportamentos", None))
    corpo["p-artigo"] = md_para_html(corte(ler("artigo.md"), "Você vê um bambuzal", None))
    for pid, arq in (("p-c5", "carrossel-5.md"), ("p-c6", "carrossel-6.md"), ("p-c7", "carrossel-7.md")):
        corpo[pid] = md_para_html(corte(ler(arq), "## Slide 1", None))

    corpo["p-artefatos"] += (
        "<h3>Custódia dos documentos</h3>"
        + md_para_html(corte(matriz, "## 9. Custódia dos documentos", None))
    )

    secoes = "".join(secao(i, corpo[pid]) for i, (pid, _) in enumerate(PAGINAS))

    tabs_js = json.dumps([[p, r] for p, r in PAGINAS], ensure_ascii=False)

    doc = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Comparativo mecânico de bambu — Ásia × América do Sul</title>
<meta name="description" content="Doze PDFs, quatro comparativos entre continentes e a variação intra-gênero que supera a diferença continental. Leitura e revisão.">
<meta property="og:type" content="article">
<meta property="og:title" content="Comparativo mecânico de bambu — Ásia × América do Sul">
<meta property="og:description" content="Doze PDFs, quatro comparativos entre continentes e a variação intra-gênero que supera a diferença continental.">
<style>{CSS}</style>
</head>
<body>
<header class="top">
  <div class="kicker">MTCC · Bambu Science · leitura e revisão</div>
  <h1>Propriedades mecânicas de bambu lenhoso:<br>Ásia × América do Sul</h1>
  <p class="sub">Doze PDFs integrais, quatro comparativos entre continentes, e o achado que inverteu a
  hipótese de partida: a variação dentro do gênero <em>Guadua</em> é maior que qualquer diferença entre
  continentes.</p>
  <div class="chips">
    <span class="chip chip--gold">REVISÃO · NÃO HOMOLOGADO</span>
    <span class="chip">12 PDFs · 42,3 MB</span>
    <span class="chip">4 comparativos</span>
    <span class="chip">PR #96 · PR #97</span>
    <span class="chip">18/11/2026</span>
  </div>
</header>
{nav_html()}
<main>
{secoes}
<footer class="rodape">
  Peça de leitura gerada a partir dos documentos versionados nos pull requests #96 e #97.
  Todo número provém de PDF integral custodiado, com página indicada.
  Documento em revisão documental — não é estado da arte homologado.
</footer>
</main>
<script>{JS.replace("__TABS__", tabs_js)}</script>
</body>
</html>
"""
    saida = os.path.join(W, "comparativo-mecanica-bambu.html")
    doc = garantir_rotulos(doc)
    with open(saida, "w", encoding="utf-8") as f:
        f.write(doc)
    print("gerado:", saida, len(doc), "chars")
    return saida


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
