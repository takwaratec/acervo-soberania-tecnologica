#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Monta a peça do cobre no MOLDE HOMOLOGADO (peça de boro, 2026-11-24).

REPO:     acervo-soberania-tecnologica
MOLDE:    scripts/molde/molde.css + molde.js  (extraídos byte a byte da peça homologada)
CONTEÚDO: scripts/conteudo_cobre.py
SAÍDA:    docs/analyses/cobre/o-cobre-no-bambu.html

Única alteração em relação ao molde: a paleta de destaque (verde do boro -> cobre),
aplicada como override declarado no fim do CSS. Estrutura, mecânica e JS são os do molde.
"""
import os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import conteudo_cobre as C

REPO = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica"
_AQUI = os.path.dirname(os.path.abspath(__file__))
CSS_PATH = os.path.join(_AQUI, "molde", "molde.css")
JS_PATH = os.path.join(_AQUI, "molde", "molde.js")
SAIDA = f"{REPO}/docs/analyses/cobre/o-cobre-no-bambu.html"

PALETA = """
/* ---------------------------------------------------------------------------
   Override de paleta — única diferença em relação ao molde homologado.
   O molde do boro usa verde (--accent #1f5f4e); esta peça é sobre cobre,
   então o destaque vai para o tom do metal. Estrutura e mecânica: intactas.
   --------------------------------------------------------------------------- */
:root{
  --accent:#8a4b1e; --accent-l:#a8622a; --accent-d:#42230f;
}
header.top{background:var(--accent-d);color:#f5efe8;border-bottom:4px solid var(--accent-l)}
header.top .kicker{color:#d8b48f}
header.top .sub{color:#e3d6c8}
h3{color:var(--accent-d)}
blockquote{border-left-color:var(--accent-l)}
"""


def fmt_pt(n):
    """separador de milhar em português"""
    return f"{n:,}".replace(",", ".")


def montar():
    css = open(CSS_PATH, encoding="utf-8").read()
    js = open(JS_PATH, encoding="utf-8").read()

    for marcador in ("--barra-h", "scroll-margin-top", "ResizeObserver",
                     "replaceState", "data-tab", 'role="tabpanel"'):
        assert marcador in css + js, f"molde sem o marcador {marcador}"

    navs, secs = [], []
    for i, p in enumerate(C.PAGINAS):
        sel = "true" if i == 0 else "false"
        tab = "0" if i == 0 else "-1"
        navs.append(
            f'  <button type="button" role="tab" data-tab="{p["id"]}" '
            f'aria-controls="{p["id"]}" aria-selected="{sel}" tabindex="{tab}">{p["aba"]}</button>')
        cls = ' class="active"' if i == 0 else ""
        secs.append(
            f'<section role="tabpanel" id="{p["id"]}" aria-labelledby="h-{p["id"]}"{cls}>\n'
            f'  <h2 id="h-{p["id"]}"><span class="num">{p["num"]}</span>{p["h2"]}</h2>\n'
            f'  <p class="meta">{p["meta"]}</p>\n'
            f'  {p["corpo"].strip()}\n'
            f'</section>')

    palavras = sum(len(re.findall(r"[A-Za-zÀ-ÿ]{2,}", p["corpo"])) for p in C.PAGINAS)

    doc = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>O cobre, explicado do zero</title>
<meta name="description" content="Artigo didático sobre o sulfato de cobre no tratamento de bambu para quem não tem formação em química: o que é o elemento, de onde vem, para que serve, quanto é seguro — e o que acontece com a água que sobra.">
<meta property="og:title" content="O cobre, explicado do zero">
<meta property="og:description" content="Um metal comum, uma solução azul e a pergunta que quase ninguém faz: para onde vai a água do tratamento.">
<meta property="og:type" content="article">
<style>
{css.strip()}
{PALETA}
</style>
</head>
<body>
<header class="top">
  <div class="kicker">Acervo Soberania Tecnológica · Gaveta Cobre · Artigo didático</div>
  <h1>O cobre, explicado do zero</h1>
  <p class="sub">Um metal comum, uma solução azul e a pergunta que quase ninguém faz: <strong>para onde vai a água do tratamento</strong> — do átomo ao resíduo, sem supor que você saiba química.</p>
  <div class="chips">
    <span class="chip chip--gold">EM REVISÃO DOCUMENTAL · NÃO HOMOLOGADO</span>
    <span class="chip">{len(C.PAGINAS)} abas</span>
    <span class="chip">~{fmt_pt(palavras)} palavras</span>
    <span class="chip">{len(C.GLOSSARIO)} termos no glossário</span>
    <span class="chip">2026-11-24</span>
  </div>
</header>
<nav class="tabs" role="tablist" aria-label="Páginas">
{chr(10).join(navs)}
</nav>
<main>
{chr(10).join(secs)}
</main>
<footer class="rodape">
<p><strong>Sobre este documento.</strong> Artigo didático produzido a partir da frente do cobre do Acervo Soberania Tecnológica. Estado: <code>em-revisao-documental</code>, homologação automática desativada — homologação é ato humano.</p>
<p>Os números citados podem ser conferidos um a um nas fichas técnicas da gaveta, cada uma com a fonte primária custodiada e assinatura digital. O material passou por cinco auditorias independentes nesta rodada, com três reprovações e correção material em cada uma.</p>
<p>Estrutura e mecânica de abas: molde homologado da casa. Conteúdo: <code>scripts/conteudo_cobre.py</code>.</p>
</footer>
<script>
{js.strip()}
</script>
</body>
</html>
"""
    open(SAIDA, "w", encoding="utf-8").write(doc)
    return doc, palavras


def validar(doc, palavras):
    print("=" * 68)
    print("VALIDAÇÃO — molde homologado")
    print("=" * 68)
    falhas = []

    ext = re.findall(r'(?:src|href)\s*=\s*["\'](?:https?:)?//', doc)
    cdn = re.findall(r"fonts\.googleapis|cdn\.|unpkg|jsdelivr", doc, re.I)
    falhas.append("arquivo único") if (ext or cdn) else None
    print(f"  1. arquivo único            externos={len(ext)} cdn={len(cdn)}")

    sem_lab = re.findall(r"<td(?![^>]*data-l=)[^>]*>", doc)
    tot_td = len(re.findall(r"<td\b[^>]*>", doc))
    if sem_lab: falhas.append("data-l")
    print(f"  2. data-l nas células       {tot_td - len(sem_lab)}/{tot_td}")

    tabs = re.findall(r'data-tab="([\w-]+)"', doc)
    pans = re.findall(r'<section role="tabpanel" id="([\w-]+)" aria-labelledby="h-([\w-]+)"', doc)
    h2s = re.findall(r'<h2 id="h-([\w-]+)"', doc)
    ok_lig = (len(tabs) == len(pans) == len(h2s)
              and all(p[0] == t and p[1] == t for t, p in zip(tabs, pans)))
    if not ok_lig: falhas.append("ligação aba/painel")
    print(f"  3. aba/painel/título        abas={len(tabs)} painéis={len(pans)} h2={len(h2s)}")

    ativos = len(re.findall(r'<button[^>]*aria-selected="true"', doc))
    if ativos != 1: falhas.append("aba ativa")
    print(f"  4. aba ativa na entrada     {ativos}")

    tem_var = "--barra-h" in doc and "scroll-margin-top:calc(var(--barra-h" in doc
    fixo = re.search(r"scroll-margin-top:\s*\d+px", doc)
    if not tem_var or fixo: falhas.append("folga fixa")
    print(f"  5. folga derivada da barra  var={'ok' if tem_var else 'FALHA'} fixo={'achou' if fixo else 'nenhum'}")

    if "flex-wrap:nowrap" not in doc: falhas.append("barra mobile")
    print(f"  6. barra mobile 1 linha     {'OK' if 'flex-wrap:nowrap' in doc else 'FALHA'}")

    _imp = ('section[role="tabpanel"]{display:block !important' in doc
            and "page-break-after:always" in doc)
    if not _imp:
        falhas.append("impressão")
    print(f"  7. impressão todas as abas  {'OK' if _imp else 'FALHA'}")

    maq = re.findall(r"/Users/[^\s\"<]+", doc)
    if maq: falhas.append("caminho de máquina")
    print(f"  8. caminho de máquina       {len(maq)}")

    from html.parser import HTMLParser
    VOID = {"meta","br","hr","img","link","input","source","col","area","base","embed","param","track","wbr"}
    class V(HTMLParser):
        def __init__(s):
            super().__init__(); s.p = []; s.e = []
        def handle_starttag(s, t, a):
            if t not in VOID: s.p.append(t)
        def handle_endtag(s, t):
            if t in VOID: return
            if s.p and s.p[-1] == t: s.p.pop()
            else: s.e.append(t)
    v = V(); v.feed(doc)
    if v.e or v.p: falhas.append("estrutura")
    print(f"  9. estrutura HTML           erros={len(v.e)} abertas={len(v.p)}")

    ruins = 0
    for tb in re.findall(r"<table[^>]*>(.*?)</table>", doc, re.S):
        nth = len(re.findall(r"<th>", tb))
        for tr in re.findall(r"<tr>(?:(?!</tr>).)*</tr>", tb, re.S):
            ntd = len(re.findall(r"<td\b", tr))
            if ntd and ntd != nth: ruins += 1
    if ruins: falhas.append("colunas")
    print(f" 10. colunas por linha        {ruins} divergentes")

    print(f"\n  páginas: {len(C.PAGINAS)} | palavras: {palavras:,} | glossário: {len(C.GLOSSARIO)} | "
          f"tabelas: {len(re.findall(r'<table', doc))} | {os.path.getsize(SAIDA):,} bytes")
    print(f"  saída: {SAIDA}")
    print(f"\nRESULTADO: {'TODOS OS CHECKS VERDES' if not falhas else 'VERMELHO em ' + ', '.join(falhas)}")
    return not falhas


if __name__ == "__main__":
    doc, palavras = montar()
    sys.exit(0 if validar(doc, palavras) else 1)
