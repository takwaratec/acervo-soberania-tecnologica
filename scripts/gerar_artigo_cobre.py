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
import referencias_cobre as R
from conteudo_cobre import tabela

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

/* citações numeradas clicáveis e bibliografia comentada */
a.cite{font:700 .82em/1 inherit;color:var(--accent);text-decoration:none}
a.cite:hover{text-decoration:underline}
p.ref{padding-left:2.4rem;text-indent:-2.4rem;margin:12px 0}
p.ref:target{background:var(--warn-bg);outline:2px solid #d4b862;border-radius:4px}
/* síntese da fonte: itálico no conjunto, com o limite em redondo para não se perder */
.resumo{font-style:italic}
.resumo .limite{font-style:normal;color:#8a4b12;font-weight:600}
.pendente{font:600 11px/1.4 ui-monospace,Menlo,monospace;color:var(--warn);
  background:var(--warn-bg);padding:1px 6px;border-radius:4px;
  display:inline;white-space:normal;overflow-wrap:anywhere;box-decoration-break:clone}


/* Com 18 abas (11 do artigo + 6 fichas + referências), a grade de 6 colunas do molde
   empilha em 3 linhas e a barra fixa passa a ocupar 132px — 13% da tela. Linha única
   rolável mantém a altura constante, como o próprio molde já faz no celular. */
nav.tabs{display:flex;flex-wrap:nowrap;overflow-x:auto;overflow-y:hidden;gap:6px;
  grid-template-columns:none;scrollbar-width:thin}
nav.tabs button{flex:0 0 auto;white-space:nowrap;overflow-wrap:normal;hyphens:none}
"""


FICHAS = [
    ("f-1", "Ficha · Embrapa COT 110", "Instrução oficial brasileira",
     "ficha-embrapa-cot110-tratamento-madeira-propriedade-rural.md"),
    ("f-2", "Ficha · NMBA 2006", "Manual oficial indiano",
     "ficha-nmba-2006-preservation-of-bamboo-manual.md"),
    ("f-3", "Ficha · Scharfenberg 2020", "Mede a fitotoxicidade do descarte",
     "ficha-scharfenberg-2020-bambu-cb-fitotoxicidade.md"),
    ("f-4", "Ficha · UFMG / MOM", "Universidade publica a receita",
     "ficha-ufmg-mom-tratamento-com-borax.md"),
    ("f-5", "Ficha · Blog TCS 2016", "A receita informal completa",
     "ficha-blog-tsc-como-tratar-bambu.md"),
    ("f-6", "Ficha · Espaço Naturalmente", "Padrão de mercado",
     "ficha-espaconaturalmente-bambu.md"),
    ("f-7", "Ficha · Portaria 292/89", "A norma que nomeia quem fiscaliza",
     "ficha-pi292-89-registro-preservativos-madeira.md"),
    ("f-8", "Ficha · Portaria Ibama 151/97", "O risco ambiental como requisito",
     "ficha-pn151-97-ibama-risco-ambiental.md"),
    ("f-9", "Ficha · Iema-ES NT 01/2023", "O regulador escrevendo o que não sabe",
     "ficha-iema-es-nt01-2023-preservacao-madeira.md"),
    ("f-10", "Ficha · ABPM / FG4mad", "A própria cadeia proíbe a queima",
     "ficha-abpm-fg4mad-destinacao-residuo-madeira-tratada.md"),
    ("f-11", "Ficha · Ciência Florestal 2025", "880 dias medindo arsênio no solo",
     "ficha-ufsm-2025-cca-moiroes-contaminacao-solo.md"),
    ("f-12", "Ficha · Instrução Normativa 5/92", "O item que manda a bula dizer o descarte",
     "ficha-in05-92-ibama-destinacao-final-residuos.md"),
]
# lê as fichas da área publicada, que é o que o leitor recebe e o auditor confere
FICHAS_DIR = f"{REPO}/docs/analyses/cobre/fichas"


def md_para_html(md):
    """Conversor mínimo para as fichas: títulos, tabelas, listas, citação, negrito, itálico, código."""
    import html as h
    if md.startswith("---"):
        fim = md.find("\n---", 3)
        if fim != -1:
            md = md[fim + 4:].lstrip("\n")
    import re as _re

    def inline(s):
        s = _re.sub(r"`([^`]+)`", lambda m: "\x01" + h.escape(m.group(1)) + "\x02", s)
        s = h.escape(s, quote=False)
        s = _re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = _re.sub(r"(?<![\w*])\*([^*\n]+?)\*(?![\w*])", r"<em>\1</em>", s)
        s = s.replace("\x01", "<code>").replace("\x02", "</code>")
        return s

    linhas = md.split("\n")
    out, i = [], 0
    while i < len(linhas):
        l = linhas[i]; s = l.strip()
        if not s:
            i += 1; continue
        if s in ("---", "***"):
            i += 1; continue
        m = _re.match(r"^(#{1,6})\s+(.*)$", s)
        if m:
            nivel = min(len(m.group(1)) + 1, 6)
            if len(m.group(1)) == 1:
                i += 1; continue
            out.append(f"<h{nivel}>{inline(m.group(2))}</h{nivel}>"); i += 1; continue
        if s.startswith("|") and i + 1 < len(linhas) and _re.match(r"^\|[\s:\-|]+\|?$", linhas[i+1].strip()):
            def celulas(lin):
                lin = lin.strip().strip("|")
                cels, cur, dentro = [], "", False
                for ch in lin:
                    if ch == "`": dentro = not dentro; cur += ch
                    elif ch == "|" and not dentro: cels.append(cur.strip()); cur = ""
                    else: cur += ch
                cels.append(cur.strip()); return cels
            cab = celulas(s); i += 2; corpo = []
            while i < len(linhas) and linhas[i].strip().startswith("|"):
                corpo.append(celulas(linhas[i])); i += 1
            labs = [_re.sub(r"<[^>]+>", "", c).strip() for c in cab]
            th = "".join(f"<th>{inline(c)}</th>" for c in cab)
            tr = "".join("<tr>" + "".join(
                f'<td data-l="{h.escape(labs[k], quote=True)}">{inline(r[k])}</td>'
                for k in range(len(cab))) + "</tr>" for r in corpo if len(r) == len(cab))
            out.append(f'<div class="tabwrap"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>')
            continue
        if s.startswith(">"):
            buf = []
            while i < len(linhas) and linhas[i].strip().startswith(">"):
                buf.append(_re.sub(r"^\s*>\s?", "", linhas[i])); i += 1
            out.append("<blockquote>" + md_para_html("\n".join(buf)) + "</blockquote>"); continue
        if _re.match(r"^[-*]\s+", s) or _re.match(r"^\d+\.\s+", s):
            ordenada = bool(_re.match(r"^\d+\.", s))
            tag = "ol" if ordenada else "ul"; itens = []
            while i < len(linhas) and linhas[i].strip() and (
                _re.match(r"^[-*]\s+", linhas[i].strip()) or _re.match(r"^\d+\.\s+", linhas[i].strip())):
                itens.append(_re.sub(r"^([-*]|\d+\.)\s+", "", linhas[i].strip())); i += 1
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in itens) + f"</{tag}>"); continue
        buf = []
        while i < len(linhas) and linhas[i].strip() and not _re.match(r"^(#{1,6}\s|>|\||```)", linhas[i].strip()) \
              and not _re.match(r"^([-*]|\d+\.)\s+", linhas[i].strip()):
            buf.append(linhas[i].strip()); i += 1
        if buf:
            out.append(f"<p>{inline(' '.join(buf))}</p>")
    return "\n".join(out)


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

    import hashlib, html as _hh
    # --- fichas técnicas
    for fid, titulo, sub, arq in FICHAS:
        cam = os.path.join(FICHAS_DIR, arq)
        md = open(cam, encoding="utf-8").read()
        b = open(cam, "rb").read()
        navs.append(
            f'  <button type="button" role="tab" data-tab="{fid}" '
            f'aria-controls="{fid}" aria-selected="false" tabindex="-1">{titulo}</button>')
        secs.append(
            f'<section role="tabpanel" id="{fid}" aria-labelledby="h-{fid}">\n'
            f'  <h2 id="h-{fid}"><span class="num">F</span>{titulo}</h2>\n'
            f'  <p class="meta">FICHA TÉCNICA · sha256 {hashlib.sha256(b).hexdigest()[:16]} · '
            f'{len(b):,} B · {_hh.escape(arq)}</p>\n'
            f'  <p><em>{sub}.</em></p>\n'
            f'  {md_para_html(md)}\n'
            f'</section>')

    # --- referências bibliográficas
    assert ".." not in R.lista_abnt(), "referências com ponto duplo"
    import resumos_fontes_cobre as RS
    _refs = "".join(
        f'<p class="ref" id="ref-{i}"><strong><a class="cite" href="#refs" data-ref="ref-{i}">'
        f'[{i}]</a></strong> {_hh.escape(R._fecha_ponto(a))} '
        f'<em>{_hh.escape(R._fecha_ponto(ti))}</em> '
        f'{_hh.escape(R._fecha_ponto(str(an or "[s.d.]")))} {_hh.escape(R._fecha_ponto(ve))}'
        f'{" — <span class=\'resumo\'>" + RS.resumo(ch) + "</span>" if RS.resumo(ch) else ""}</p>'
        for i, (ch, a, an, ti, ve, cu, su) in enumerate(R.REFERENCIAS, 1))
    navs.append('  <button type="button" role="tab" data-tab="refs" '
                'aria-controls="refs" aria-selected="false" tabindex="-1">Referências</button>')
    secs.append(
        '<section role="tabpanel" id="refs" aria-labelledby="h-refs">\n'
        '  <h2 id="h-refs"><span class="num">R</span>Referências bibliográficas</h2>\n'
        f'  <p class="meta">REFERÊNCIAS · {len(R.REFERENCIAS)} ENTRADAS · GAVETA COBRE · 2026-11-24</p>\n'
        '  <p>Numeradas na ordem em que aparecem pela primeira vez no texto. Onde a fonte é uma '
        'página web sem data declarada, registra-se [s.d.]. Todas as fontes custodiadas têm o hash '
        'de integridade na ficha correspondente e no manifesto de custódia da linha (<code>MANIFEST_S11.json</code> ou <code>MANIFEST_S11C.json</code>).</p>\n'
        f'  {_refs}\n'
        '</section>')

    # Na versão em abas a citação não pode apontar para #ref-N: o molde.js trata todo
    # a[href^="#"] como troca de aba, e "ref-3" não é aba — a página ficaria em branco.
    # Aponta-se para o painel #refs e o alvo fino vai em data-ref, com handler próprio.
    for s in secs:
        pass
    secs = [re.sub(r'<a class="cite" href="#(ref-\d+)">',
                   r'<a class="cite" href="#refs" data-ref="\1">', x) for x in secs]

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
    <span class="chip">{len(navs)} abas</span>
    <span class="chip">~{fmt_pt(palavras)} palavras</span>
    <span class="chip">{len(C.GLOSSARIO)} termos no glossário</span>
    <span class="chip">{len(FICHAS)} fichas + {len(R.REFERENCIAS)} referências</span>
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
<script>
/* a citação abre a aba de referências (molde.js) e depois rola até o verbete exato */
document.addEventListener('click', function(ev){{
  var a = ev.target.closest ? ev.target.closest('a.cite[data-ref]') : null;
  if(!a){{ return; }}
  var alvo = document.getElementById(a.getAttribute('data-ref'));
  if(!alvo){{ return; }}
  setTimeout(function(){{
    var y = alvo.getBoundingClientRect().top + window.pageYOffset
            - (window.innerHeight / 2) + (alvo.offsetHeight / 2);
    window.scrollTo(0, Math.max(0, y));
  }}, 140);
}});
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
