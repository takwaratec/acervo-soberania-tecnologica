#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Peça CORRIDA do cobre — mesmo desenho da peça corrida do boro (2026-11-24).

Diferença em relação à peça de abas: aqui o artigo flui de ponta a ponta, com
sumário, citações [N] clicáveis, bibliografia comentada e as 6 fichas anexadas
na íntegra ao final.

SAÍDA: docs/analyses/cobre/o-cobre-no-bambu-corrido.html
"""
import hashlib
import html as H
import os
import re
import sys
import unicodedata

_AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _AQUI)
import conteudo_cobre as C
import referencias_cobre as R
import resumos_fontes_cobre as RS

REPO = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica"
SAIDA = f"{REPO}/docs/analyses/cobre/o-cobre-no-bambu-corrido.html"
CSS_MOLDE = f"{_AQUI}/molde/molde.css"
CSS_CORRIDO = f"{_AQUI}/molde/molde-corrido.css"
FICHAS_DIR = f"{REPO}/docs/analyses/cobre/fichas"

PALETA = """
/* paleta do cobre — única diferença em relação ao molde do boro */
:root{ --accent:#8a4b1e; --accent-l:#a8622a; --accent-d:#42230f; }
header.top{background:var(--accent-d);color:#f5efe8;border-bottom:4px solid var(--accent-l)}
header.top .kicker{color:#d8b48f}
header.top .sub{color:#e3d6c8}
h3{color:var(--accent-d)}
blockquote{border-left-color:var(--accent-l)}
a.cite{color:#8a4b1e}
/* síntese da fonte: itálico no conjunto, com o limite em redondo para não se perder */
.resumo{font-style:italic}
.resumo .limite{font-style:normal;color:#8a4b12;font-weight:600}

"""

FICHAS = [
 ("ficha-1", "Embrapa COT 110 — a instrução oficial brasileira: EPI por peça, tonel de 200 L e a ordem de reusar",
  "ficha-embrapa-cot110-tratamento-madeira-propriedade-rural.md"),
 ("ficha-2", "NMBA 2006 — o manual indiano: não descartar em rio, decantar e reusar, e o enterro com serragem",
  "ficha-nmba-2006-preservation-of-bamboo-manual.md"),
 ("ficha-3", "Scharfenberg 2020 — fitotoxicidade medida: germinação zero até diluição 1/10 e pH 1,28",
  "ficha-scharfenberg-2020-bambu-cb-fitotoxicidade.md"),
 ("ficha-4", "UFMG / MOM — a receita publicada por universidade pública, com o aviso de que não foi comprovada",
  "ficha-ufmg-mom-tratamento-com-borax.md"),
 ("ficha-5", "Blog TCS 2016 — a receita informal completa: dicromato de sódio, 4,5% e a instrução de dobrar",
  "ficha-blog-tsc-como-tratar-bambu.md"),
 ("ficha-6", "Espaço Naturalmente — o padrão de mercado: sulfato de cobre como fungicida, sem uma palavra de aviso",
  "ficha-espaconaturalmente-bambu.md"),
]


def slug(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s


def md_para_html(md):
    """Conversor mínimo de Markdown para as fichas."""
    if md.startswith("---"):
        fim = md.find("\n---", 3)
        if fim != -1:
            md = md[fim + 4:].lstrip("\n")

    def inline(s):
        s = re.sub(r"`([^`]+)`", lambda m: "\x01" + H.escape(m.group(1)) + "\x02", s)
        s = H.escape(s, quote=False)
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<![\w*])\*([^*\n]+?)\*(?![\w*])", r"<em>\1</em>", s)
        return s.replace("\x01", "<code>").replace("\x02", "</code>")

    linhas = md.split("\n")
    out, i = [], 0
    while i < len(linhas):
        s = linhas[i].strip()
        if not s:
            i += 1
            continue
        if s in ("---", "***"):
            i += 1
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", s)
        if m:
            if len(m.group(1)) == 1:
                i += 1
                continue
            nivel = min(len(m.group(1)) + 1, 6)
            out.append(f"<h{nivel}>{inline(m.group(2))}</h{nivel}>")
            i += 1
            continue
        if s.startswith("|") and i + 1 < len(linhas) and re.match(r"^\|[\s:\-|]+\|?$", linhas[i + 1].strip()):
            def cels(lin):
                lin = lin.strip().strip("|")
                r, cur, dentro = [], "", False
                for ch in lin:
                    if ch == "`":
                        dentro = not dentro
                        cur += ch
                    elif ch == "|" and not dentro:
                        r.append(cur.strip())
                        cur = ""
                    else:
                        cur += ch
                r.append(cur.strip())
                return r
            cab = cels(s)
            i += 2
            corpo = []
            while i < len(linhas) and linhas[i].strip().startswith("|"):
                corpo.append(cels(linhas[i]))
                i += 1
            labs = [re.sub(r"<[^>]+>", "", c).strip() for c in cab]
            th = "".join(f"<th>{inline(c)}</th>" for c in cab)
            tr = "".join(
                "<tr>" + "".join(f'<td data-l="{H.escape(labs[k], quote=True)}">{inline(r[k])}</td>'
                                 for k in range(len(cab))) + "</tr>"
                for r in corpo if len(r) == len(cab))
            out.append(f'<div class="tabwrap"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>')
            continue
        if s.startswith(">"):
            buf = []
            while i < len(linhas) and linhas[i].strip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", linhas[i]))
                i += 1
            out.append("<blockquote>" + md_para_html("\n".join(buf)) + "</blockquote>")
            continue
        if re.match(r"^[-*]\s+", s) or re.match(r"^\d+\.\s+", s):
            ord_ = bool(re.match(r"^\d+\.", s))
            tag = "ol" if ord_ else "ul"
            itens = []
            while i < len(linhas) and linhas[i].strip() and (
                    re.match(r"^[-*]\s+", linhas[i].strip()) or re.match(r"^\d+\.\s+", linhas[i].strip())):
                itens.append(re.sub(r"^([-*]|\d+\.)\s+", "", linhas[i].strip()))
                i += 1
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in itens) + f"</{tag}>")
            continue
        buf = []
        while i < len(linhas) and linhas[i].strip() and \
                not re.match(r"^(#{1,6}\s|>|\||```)", linhas[i].strip()) and \
                not re.match(r"^([-*]|\d+\.)\s+", linhas[i].strip()):
            buf.append(linhas[i].strip())
            i += 1
        if buf:
            out.append(f"<p>{inline(' '.join(buf))}</p>")
    return "\n".join(out)


def montar():
    css = open(CSS_MOLDE, encoding="utf-8").read()
    css_c = open(CSS_CORRIDO, encoding="utf-8").read()

    # ---- seções do artigo (a capa vira "Antes de começar")
    corpo, toc = [], []
    secao_num = 0
    for p in C.PAGINAS:
        titulo = H.unescape(re.sub(r"<[^>]+>", "", p["h2"]))
        if p["id"] == "p-1":
            corpo.append('<h1 class="art-title">O cobre, explicado do zero</h1>\n'
                         '<h2 id="antes-de-comecar">Antes de começar</h2>\n'
                         f'{p["corpo"].strip()}')
            toc.append(("antes-de-comecar", "Antes de começar"))
            continue
        if p["num"] == "09":             # Glossário: sem número
            corpo.append(f'<h2 id="glossario">{H.escape(titulo)}</h2>\n{p["corpo"].strip()}')
            toc.append(("glossario", "Glossário"))
            continue
        if p["num"] == "10":             # Proveniência vira "Como este texto foi feito"
            corpo.append('<h2 id="como-este-texto-foi-feito">Como este texto foi feito</h2>\n'
                         + p["corpo"].strip())
            toc.append(("como-este-texto-foi-feito", "Como este texto foi feito"))
            continue
        secao_num += 1
        # tirar o "01 · " do título e renumerar como "1. "
        limpo = re.sub(r"^\d{2}\s*·\s*", "", titulo)
        limpo = re.sub(r"^\d+\.\s*", "", limpo)
        sid = slug(f"{secao_num}-{limpo}")[:58].rsplit("-", 1)[0]
        corpo.append(f'<h2 id="{sid}">{secao_num}. {H.escape(limpo)}</h2>\n'
                     f'{p["corpo"].strip()}')
        toc.append((sid, f"{secao_num}. {limpo}"))

    # ---- bibliografia comentada
    refs_html = []
    for i, (ch, aut, an, ti, ve, cu, su) in enumerate(R.REFERENCIAS, 1):
        a = R._fecha_ponto(aut)
        t = R._fecha_ponto(ti)
        an_ = R._fecha_ponto(str(an or "[s.d.]"))
        v = R._fecha_ponto(ve)
        res = RS.resumo(ch)
        refs_html.append(
            f'<p class="ref" id="ref-{i}"><strong><a class="cite" href="#ref-{i}">[{i}]</a></strong> '
            f'{H.escape(a)} <em>{H.escape(t)}</em> {H.escape(an_)} {H.escape(v)}'
            f'{" — <span class=\'resumo\'>" + res + "</span>" if res else ""}</p>')
    refs_html = "\n".join(refs_html)

    # ---- fichas
    fichas_html, indices = [], []
    for i, (fid, tit, arq) in enumerate(FICHAS, 1):
        cam = os.path.join(FICHAS_DIR, arq)
        bruto = open(cam, "rb").read()
        sha = hashlib.sha256(bruto).hexdigest()
        md = bruto.decode("utf-8")
        m = re.search(r"^estado_documental:\s*(\S+)", md, re.M)
        estado = m.group(1) if m else "?"
        indices.append(f'    <li><a href="#{fid}">{H.escape(tit)}</a></li>')
        fichas_html.append(
            f'<article class="ficha" id="{fid}"><div class="ficha-head">'
            f'<span class="ficha-num">FICHA {i:02d}</span><h3>{H.escape(tit)}</h3>'
            f'<p class="ficha-meta">{estado} · sha256 {sha[:16]} · '
            f'<code>{H.escape(arq)}</code></p></div>\n{md_para_html(md)}\n</article>')
    fichas_html = "\n".join(fichas_html)

    palavras = sum(len(re.findall(r"[A-Za-zÀ-ÿ]{2,}", re.sub(r"<[^>]+>", " ", p["corpo"])))
                   for p in C.PAGINAS)

    toc_html = "\n".join(f'    <li><a href="#{s}">{H.escape(t)}</a></li>' for s, t in toc)
    toc_html += '\n    <li><a href="#bibliografia-consultada">Bibliografia consultada</a></li>'
    toc_html += '\n    <li><a href="#anexos">Anexos — as 6 fichas técnicas na íntegra</a></li>'

    doc = f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>O cobre, explicado do zero — Acervo Soberania Tecnológica</title>
<meta name="description" content="Artigo didático integral sobre o sulfato de cobre no tratamento de bambu, com 17 citações numeradas, bibliografia comentada e as 6 fichas técnicas anexadas na íntegra.">
<meta property="og:title" content="O cobre, explicado do zero">
<meta property="og:description" content="Um metal comum, uma solução azul e a pergunta que quase ninguém faz: para onde vai a água do tratamento.">
<meta property="og:type" content="article">
<style>
{css.strip()}
{css_c.strip()}
{PALETA}
</style></head><body>
<header class="top">
<div class="kicker">Acervo Soberania Tecnológica · Gaveta Cobre · Artigo didático</div>
<h1>O cobre, explicado do zero</h1>
<p class="sub">Um metal comum, uma solução azul e a pergunta que quase ninguém faz — <strong>para onde vai a água do tratamento</strong>. Do átomo ao resíduo, sem supor que você saiba química.</p>
<div class="chips"><span class="chip chip--gold">HOMOLOGADO INTERNAMENTE</span><span class="chip chip--gold">AUDITORIA EXTERNA PENDENTE</span><span class="chip">texto corrido · sem abas</span><span class="chip">{len(R.REFERENCIAS)} referências comentadas</span><span class="chip">{len(FICHAS)} fichas anexadas</span><span class="chip">{len(C.GLOSSARIO)} termos no glossário</span><span class="chip">2026-11-24</span></div>
</header>
<main>
<nav class="toc toc-artigo" aria-label="Sumário do artigo"><h2>Sumário</h2><ol>
{toc_html}
</ol></nav>

{chr(10).join(corpo)}

<h2 id="bibliografia-consultada">Bibliografia consultada</h2>
<p>Todas as obras abaixo estão custodiadas no acervo com hash SHA-256 verificável, e cada uma tem ficha técnica própria com avaliação crítica e limites declarados. A síntese em itálico, depois de cada referência, registra <strong>o que esta obra sustenta neste artigo</strong> e <strong>qual é o limite dela</strong> — inclusive quando o dado contraria a hipótese do próprio texto.</p>
<p>As fontes primárias estão publicadas integralmente em <code>docs/analyses/cobre/fontes/</code>, com manifesto de hashes por arquivo. As fichas técnicas estão em <code>docs/analyses/cobre/fichas/</code>.</p>
{refs_html}

<section id="anexos">
<div class="anexo-intro"><strong>Anexos — fichas técnicas na íntegra.</strong> Cada obra citada tem ficha própria com dados gerais, conteúdo medido, avaliação crítica e limites declarados. Texto integral, sem resumo. Todas em <code>homologado-internamente</code>, pendentes de auditoria externa.</div>
<nav class="toc" aria-label="Índice das fichas"><h2>{len(FICHAS)} fichas desta gaveta</h2><ol>
{chr(10).join(indices)}
</ol></nav>
{fichas_html}
</section>
</main>
<footer class="rodape">
<p><strong>Sobre este documento.</strong> Texto integral e corrido, sem abas — o mesmo conteúdo do manuscrito <code>docs/analyses/cobre/00-artigo-o-cobre-explicado-do-zero.md</code>, com as 6 fichas de <code>docs/analyses/cobre/fichas/</code> anexadas ao final. A versão em abas, para leitura por capítulo, está em <code>o-cobre-no-bambu.html</code>.</p>
<p>Estado <code>homologado-internamente</code> (autoridade FABIO, 2026-11-24), auditoria externa pendente; homologação automática desativada. Cinco rodadas de auditoria independente na frente, com três reprovações e correção material em cada uma. Redação com assistência de agente de IA sob curadoria humana declarada.</p>
</footer></body></html>
"""
    open(SAIDA, "w", encoding="utf-8").write(doc)
    return doc, palavras, len(toc)


def validar(doc, palavras, nsecoes):
    print("=" * 68)
    print("VALIDAÇÃO — peça corrida")
    print("=" * 68)
    falhas = []

    ext = re.findall(r'(?:src|href)\s*=\s*["\'](?:https?:)?//', doc)
    if ext:
        falhas.append("arquivo único")
    print(f" 1. arquivo único              externos={len(ext)}")

    sem = re.findall(r"<td(?![^>]*data-l=)[^>]*>", doc)
    tot = len(re.findall(r"<td\b[^>]*>", doc))
    if sem:
        falhas.append("data-l")
    print(f" 2. data-l nas células         {tot-len(sem)}/{tot}")

    cits = re.findall(r'<a class="cite" href="#ref-(\d+)">\[(\d+)\]</a>', doc)
    hrefs = [int(a) for a, _ in cits]
    rótulos_ok = all(a == b for a, b in cits)
    print(f" 3. citações                   {len(cits)} marcas, refs {len(set(hrefs))}/14"
          + ("" if rótulos_ok else "  RÓTULO≠HREF"))
    if not rótulos_ok:
        falhas.append("rótulo da citação")

    # todo #ref-N citado existe, e toda ref tem âncora
    alvos = set(re.findall(r'id="ref-(\d+)"', doc))
    if set(map(str, hrefs)) - alvos:
        falhas.append("citação sem destino")
    print(f" 4. âncoras de referência      {len(alvos)}/14")

    # sumário -> âncoras
    links = re.findall(r'class="toc[^"]*"[^>]*>.*?</nav>', doc, re.S)
    toc_ids = re.findall(r'<li><a href="#([^"]+)">', links[0] if links else "")
    quebrados = [i for i in toc_ids if f'id="{i}"' not in doc]
    if quebrados:
        falhas.append("sumário quebrado")
    print(f" 5. sumário                    {len(toc_ids)} entradas"
          + (f"  QUEBRADAS: {quebrados[:3]}" if quebrados else ""))

    # fichas
    nf = len(re.findall(r'<article class="ficha"', doc))
    ids_f = re.findall(r'<article class="ficha" id="(ficha-\d+)"', doc)
    if nf != 6:
        falhas.append("fichas")
    print(f" 6. fichas anexadas            {nf} (ids: {', '.join(ids_f)})")

    # ficha no sumário
    faltam_idx = [i for i in ids_f if f'href="#{i}"' not in doc]
    if faltam_idx:
        falhas.append("índice das fichas")
    print(f" 7. fichas no índice           {len(ids_f)-len(faltam_idx)}/{len(ids_f)}")

    # estado homologado nas fichas
    homol = len(re.findall(r"homologado-internamente", doc))
    if homol < 6:
        falhas.append("estado das fichas")
    print(f" 8. estado homologado          {homol} ocorrências")

    # bibliografia com resumo
    resumos = len(re.findall(r'<p class="ref" id="ref-\d+">.*?class=.resumo.', doc, re.S))
    if resumos != 14:
        falhas.append("resumo na bibliografia")
    print(f" 9. bibliografia comentada     {resumos}/14 com síntese")

    from html.parser import HTMLParser
    VOID = {"meta", "br", "hr", "img", "link", "input", "source", "col", "area",
            "base", "embed", "param", "track", "wbr"}

    class V(HTMLParser):
        def __init__(s):
            super().__init__()
            s.p, s.e = [], []

        def handle_starttag(s, t, a):
            if t not in VOID:
                s.p.append(t)

        def handle_endtag(s, t):
            if t in VOID:
                return
            if s.p and s.p[-1] == t:
                s.p.pop()
            else:
                s.e.append(t)

    v = V()
    v.feed(doc)
    if v.e or v.p:
        falhas.append("estrutura")
    print(f"10. estrutura HTML            erros={len(v.e)} abertas={len(v.p)}")

    maq = re.findall(r"/Users/", doc)
    if maq:
        falhas.append("caminho de máquina")
    print(f"11. caminho de máquina        {len(maq)}")

    print(f"\n  seções no sumário: {nsecoes} | palavras: {palavras:,} | "
          f"tabelas: {len(re.findall(r'<table', doc))} | "
          f"{os.path.getsize(SAIDA):,} bytes")
    print(f"  saída: {SAIDA}")
    print(f"\nRESULTADO: {'TODOS OS CHECKS VERDES' if not falhas else 'VERMELHO em ' + ', '.join(falhas)}")
    return not falhas


if __name__ == "__main__":
    doc, palavras, nsec = montar()
    sys.exit(0 if validar(doc, palavras, nsec) else 1)
