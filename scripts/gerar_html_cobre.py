#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera a peça única navegável: artigo didático + 6 fichas da rodada S11/S11-bis.

REPO:   acervo-soberania-tecnologica
FONTE:  docs/analyses/cobre/08-artigo-didatico-o-cobre-e-a-agua-que-sobra.md
        _privado/fichas/ago_28_Sulfato_S11/*.md
SAÍDA:  docs/analyses/cobre/o-cobre-no-bambu.html

Zero requisição externa. Conversor próprio: títulos, tabelas, listas, blockquote,
código, negrito, itálico, code, link relativo. Ênfase aninhada tratada de fora
para dentro; validação da ORDEM das tags, não do saldo.
"""
import re, html, os, sys, json, hashlib

REPO = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica"
ARTIGO = f"{REPO}/docs/analyses/cobre/08-artigo-didatico-o-cobre-e-a-agua-que-sobra.md"
FICHAS_DIR = f"{REPO}/_privado/fichas/ago_28_Sulfato_S11"
SAIDA = f"{REPO}/docs/analyses/cobre/o-cobre-no-bambu.html"

FICHAS = [
    ("cot110",  "Embrapa COT 110", "Instrução rural brasileira", "ficha-embrapa-cot110-tratamento-madeira-propriedade-rural.md"),
    ("nmba",    "NMBA 2006", "Manual do governo indiano", "ficha-nmba-2006-preservation-of-bamboo-manual.md"),
    ("ufmg",    "UFMG / MOM", "Universidade publica a receita", "ficha-ufmg-mom-tratamento-com-borax.md"),
    ("blog",    "Blog TCS 2016", "A receita informal completa", "ficha-blog-tsc-como-tratar-bambu.md"),
    ("esp",     "Espaço Naturalmente", "Site comercial", "ficha-espaconaturalmente-bambu.md"),
    ("scharf",  "Scharfenberg 2020", "Mede a fitotoxicidade do descarte", "ficha-scharfenberg-2020-bambu-cb-fitotoxicidade.md"),
]

# ---------------------------------------------------------------- conversor
def dividir_celulas(linha):
    """Divide por | rastreando backtick (| dentro de `code` não quebra)."""
    linha = linha.strip()
    if linha.startswith("|"): linha = linha[1:]
    if linha.endswith("|"): linha = linha[:-1]
    cels, atual, dentro = [], "", False
    for ch in linha:
        if ch == "`": dentro = not dentro; atual += ch
        elif ch == "|" and not dentro: cels.append(atual.strip()); atual = ""
        else: atual += ch
    cels.append(atual.strip())
    return cels

def inline(txt):
    """Ênfase de fora para dentro: code -> negrito -> itálico. Escapa HTML antes."""
    marcadores = []
    def guard(m):
        marcadores.append(m.group(1)); return f"\x00{len(marcadores)-1}\x00"
    txt = re.sub(r"`([^`]+)`", guard, txt)          # code primeiro: protege conteúdo
    txt = html.escape(txt, quote=False)
    txt = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", txt)
    txt = re.sub(r"(?<![\w*])\*([^*\n]+?)\*(?![\w*])", r"<em>\1</em>", txt)
    txt = re.sub(r"~~(.+?)~~", r"<del>\1</del>", txt)
    txt = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
                 lambda m: f'<a href="{m.group(2)}" target="_blank" rel="noopener noreferrer">{m.group(1)}</a>', txt)
    def volta(m):
        return f"<code>{html.escape(marcadores[int(m.group(1))], quote=False)}</code>"
    return re.sub(r"\x00(\d+)\x00", volta, txt)

def remover_frontmatter(md):
    if md.startswith("---"):
        fim = md.find("\n---", 3)
        if fim != -1: return md[fim+4:].lstrip("\n")
    return md

def converter(md):
    md = remover_frontmatter(md)
    linhas = md.split("\n")
    out, i = [], 0
    while i < len(linhas):
        l = linhas[i]
        s = l.strip()
        if not s:
            i += 1; continue
        # cerca de código
        if s.startswith("```"):
            i += 1; buf = []
            while i < len(linhas) and not linhas[i].strip().startswith("```"):
                buf.append(html.escape(linhas[i])); i += 1
            i += 1
            out.append("<pre><code>" + "\n".join(buf) + "</code></pre>"); continue
        # título (o h1 do md é descartado: o painel já nomeia)
        m = re.match(r"^(#{1,6})\s+(.*)$", s)
        if m:
            nivel = min(len(m.group(1)) + 1, 6)   # # -> h2
            if len(m.group(1)) == 1:
                i += 1; continue
            out.append(f"<h{nivel}>{inline(m.group(2))}</h{nivel}>"); i += 1; continue
        # tabela
        if s.startswith("|") and i + 1 < len(linhas) and re.match(r"^\|[\s:\-|]+\|?$", linhas[i+1].strip()):
            cabecalho = dividir_celulas(s)
            i += 2
            corpo = []
            while i < len(linhas) and linhas[i].strip().startswith("|"):
                corpo.append(dividir_celulas(linhas[i])); i += 1
            n = len(cabecalho)
            corpo = [c for c in corpo if len(c) == n]   # descarta linha malformada
            h = "<thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in cabecalho) + "</tr></thead>"
            b = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>" for row in corpo)
            out.append(f'<div class="tabwrap"><table>{h}<tbody>{b}</tbody></table></div>'); continue
        # blockquote (agrupa linhas >)
        if s.startswith(">"):
            buf = []
            while i < len(linhas) and linhas[i].strip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", linhas[i])); i += 1
            out.append("<blockquote>" + converter("\n".join(buf)) + "</blockquote>"); continue
        # lista
        if re.match(r"^[-*]\s+", s) or re.match(r"^\d+\.\s+", s):
            ordenada = bool(re.match(r"^\d+\.\s+", s))
            tag = "ol" if ordenada else "ul"
            itens = []
            while i < len(linhas) and linhas[i].strip() and (
                re.match(r"^[-*]\s+", linhas[i].strip()) or re.match(r"^\d+\.\s+", linhas[i].strip())):
                itens.append(re.sub(r"^([-*]|\d+\.)\s+", "", linhas[i].strip())); i += 1
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in itens) + f"</{tag}>"); continue
        # parágrafo
        buf = []
        while i < len(linhas) and linhas[i].strip() and not re.match(r"^(#{1,6}\s|>|\||```)", linhas[i].strip()) \
              and not re.match(r"^([-*]|\d+\.)\s+", linhas[i].strip()):
            buf.append(linhas[i].strip()); i += 1
        if buf: out.append(f"<p>{inline(' '.join(buf))}</p>")
    return "\n".join(out)

# ---------------------------------------------------------------- montagem
CSS = """
:root{--bg:#fbfaf7;--fg:#1d1d1b;--mut:#5c5c57;--lin:#e2ded4;--acc:#7a4a22;--acc2:#e8dfd0;
--note:#f3ede1;--ok:#e6f0e4;--danger:#f7e4e0;--barra-h:0px}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--fg);
font:17px/1.62 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
-webkit-text-size-adjust:100%}
header{background:#fff;border-bottom:1px solid var(--lin);padding:30px 22px 22px}
.kicker{font:600 11px/1 ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.14em;
text-transform:uppercase;color:var(--acc);margin:0 0 12px}
h1{margin:0 0 10px;font-size:clamp(24px,4.2vw,38px);line-height:1.15;letter-spacing:-.02em}
.sub{margin:0;color:var(--mut);font-size:16px;max-width:62ch}
.chips{display:flex;flex-wrap:wrap;gap:7px;margin-top:16px}
.chip{background:var(--acc2);color:#54331a;border-radius:999px;padding:5px 11px;
font:600 11.5px/1 ui-monospace,Menlo,monospace}
nav.tabs{position:sticky;top:0;z-index:20;background:#fffefb;border-bottom:1px solid var(--lin);
display:grid;grid-template-columns:repeat(6,1fr)}
nav.tabs button{appearance:none;background:none;border:0;border-bottom:3px solid transparent;
padding:13px 8px;font:600 12.5px/1.25 inherit;color:var(--mut);cursor:pointer;text-align:center}
nav.tabs button[aria-selected="true"]{color:var(--acc);border-bottom-color:var(--acc);background:#fff}
nav.tabs button:hover{background:var(--note)}
main{max-width:1180px;margin:0 auto;padding:0 22px 90px}
.tab{display:none;padding-top:30px}
.tab[aria-hidden="false"]{display:block}
.tab:focus{outline:none}
.painel-head{border-bottom:1px solid var(--lin);padding-bottom:14px;margin-bottom:22px}
.painel-head h2{margin:0;font-size:clamp(21px,3vw,29px);line-height:1.2}
.painel-head p{margin:7px 0 0;color:var(--mut);font-size:14.5px}
h3{font-size:20px;margin:34px 0 10px;line-height:1.25}
h4{font-size:17px;margin:26px 0 8px;color:#3a2a18}
h5,h6{font-size:15.5px;margin:20px 0 6px;color:#3a2a18}
p{margin:0 0 15px;max-width:74ch}
ul,ol{margin:0 0 16px;padding-left:24px;max-width:74ch}
li{margin:0 0 7px}
blockquote{margin:18px 0;padding:14px 18px;background:var(--note);border-left:4px solid var(--acc);
border-radius:0 6px 6px 0;color:#3a2a18}
blockquote p{margin:0 0 9px;max-width:none}
blockquote p:last-child{margin:0}
.tabwrap{overflow-x:auto;margin:18px 0;border:1px solid var(--lin);border-radius:7px;background:#fff}
table{border-collapse:collapse;width:100%;font-size:14.5px}
th,td{padding:9px 12px;text-align:left;border-bottom:1px solid var(--lin);vertical-align:top}
thead th{background:#f4f0e7;font-weight:700;font-size:13px;white-space:nowrap}
tbody tr:last-child td{border-bottom:0}
tbody tr:nth-child(even){background:#fcfbf7}
code{font:13.5px/1.5 ui-monospace,SFMono-Regular,Menlo,monospace;background:#f0ece2;
padding:1.5px 5px;border-radius:4px}
pre{background:#242019;color:#f2ede0;padding:15px;border-radius:7px;overflow-x:auto;margin:16px 0}
pre code{background:none;color:inherit;padding:0;font-size:13px}
a{color:var(--acc);text-underline-offset:2px}
.note,.ok,.danger{margin:18px 0;padding:13px 16px;border-radius:7px;font-size:15px}
.note{background:var(--note);border-left:4px solid #c39a5c}
.ok{background:var(--ok);border-left:4px solid #5c8f52}
.danger{background:var(--danger);border-left:4px solid #b1492f}
.meta{font:12px/1.5 ui-monospace,Menlo,monospace;color:var(--mut);background:#f4f0e7;
padding:7px 11px;border-radius:6px;margin:0 0 14px;word-break:break-all}
.lead{font-size:18px;color:#3a2a18}
footer{border-top:1px solid var(--lin);padding:22px;color:var(--mut);font-size:13.5px;
text-align:center;max-width:1180px;margin:0 auto}
footer p{margin:0 auto;max-width:70ch}
@media(max-width:900px){
nav.tabs{display:flex;overflow-x:auto;-webkit-overflow-scrolling:touch;flex-wrap:nowrap}
nav.tabs button{flex:0 0 auto;white-space:nowrap;padding:12px 14px}
}
@media(max-width:760px){
body{font-size:16.5px}
main{padding:0 15px 70px}
header{padding:22px 15px 18px}
table{font-size:13.5px}
th,td{padding:8px 9px}
}
@media print{
nav.tabs{display:none}
main .tab{display:block!important;page-break-before:always}
main .tab:first-of-type{page-break-before:auto}
main .tab[aria-hidden="true"]{display:block!important}
h2,h3,h4{break-after:avoid}
header{border-bottom:2px solid #000}
}
"""

JS = """
(function(){
  var nav=document.querySelector('nav.tabs');
  var btns=[].slice.call(nav.querySelectorAll('button'));
  var paineis=[].slice.call(document.querySelectorAll('main .tab'));
  function medirBarra(){
    var h=nav.getBoundingClientRect().height;
    document.documentElement.style.setProperty('--barra-h',h+'px');
    paineis.forEach(function(p){p.style.scrollMarginTop=(h+18)+'px';});
    [].slice.call(document.querySelectorAll('main h3, main h4')).forEach(function(el){
      el.style.scrollMarginTop=(h+22)+'px';});
  }
  function ativar(id,focar){
    var alvo=document.getElementById(id); if(!alvo) return false;
    paineis.forEach(function(p){p.setAttribute('aria-hidden', p.id===id?'false':'true');});
    btns.forEach(function(b){
      var on=b.getAttribute('aria-controls')===id;
      b.setAttribute('aria-selected',on?'true':'false'); b.tabIndex=on?0:-1;});
    if(focar){alvo.setAttribute('tabindex','-1');
      try{alvo.focus({preventScroll:true});}catch(e){alvo.focus();}}
    window.scrollTo(0,0);
    if(history.replaceState) history.replaceState(null,'','#'+id);
    medirBarra();
    return true;
  }
  btns.forEach(function(b){
    b.addEventListener('click',function(){ativar(b.getAttribute('aria-controls'),false);});
    b.addEventListener('keydown',function(e){
      var i=btns.indexOf(b), n=btns.length;
      if(e.key==='ArrowRight'){e.preventDefault();var t=btns[(i+1)%n];t.focus();t.click();}
      if(e.key==='ArrowLeft'){e.preventDefault();var p=btns[(i-1+n)%n];p.focus();p.click();}
      if(e.key==='Home'){e.preventDefault();btns[0].focus();btns[0].click();}
      if(e.key==='End'){e.preventDefault();btns[n-1].focus();btns[n-1].click();}
    });
  });
  function daHash(){
    var h=(location.hash||'').replace('#','');
    var el=h?document.getElementById(h):null;
    return (el && el.classList.contains('tab')) ? h : btns[0].getAttribute('aria-controls');
  }
  ativar(daHash(),false);
  window.addEventListener('hashchange',function(){ ativar(daHash(),false); });
  window.addEventListener('resize',medirBarra);
  window.addEventListener('load',medirBarra);
  medirBarra();
  window.__pecaPronta=true;
})();
"""

def painel(id_, titulo, sub, corpo, meta=None):
    m = f'<p class="meta">{html.escape(meta)}</p>' if meta else ""
    return (f'<section class="tab" id="{id_}" role="tabpanel" aria-labelledby="t-{id_}" aria-hidden="true">\n'
            f'<div class="painel-head"><h2 id="h-{id_}">{html.escape(titulo)}</h2>'
            f'<p>{html.escape(sub)}</p></div>\n{m}\n{corpo}\n</section>')

def main():
    artigo_md = open(ARTIGO, encoding="utf-8").read()
    secoes = []

    # Aba 0: apresentação
    apres = """
<p class="lead">Este documento reúne duas coisas num só lugar: <strong>um artigo escrito para quem não é
da química nem da academia</strong>, e <strong>as seis fichas técnicas</strong> que sustentam cada
afirmação dele. As fichas são a prova; o artigo é a leitura.</p>

<h3>O que é</h3>
<p>Um estudo sobre o <strong>sulfato de cobre no tratamento do bambu</strong> — o que é o elemento,
como age, o que a lei diz, o que as instruções mandam, e principalmente <strong>para onde vai a
água que sobra do tratamento</strong>. Escrito em linguagem comum, com cada número ligado à fonte
que o produziu.</p>

<h3>De onde vem — e a força de cada fonte</h3>
<div class="tabwrap"><table>
<thead><tr><th>Fonte</th><th>Natureza</th><th>Força probatória</th></tr></thead>
<tbody>
<tr><td><strong>Embrapa COT 110</strong> (Tonini &amp; Oliveira, 2024)</td><td>instrução oficial brasileira</td><td><strong>alta</strong> — documento institucional datado, com ISSN</td></tr>
<tr><td><strong>NMBA 2006</strong> (Governo da Índia)</td><td>manual oficial estrangeiro</td><td><strong>alta</strong> para o que prescreve; <strong>não transferível</strong> ao Brasil na destinação</td></tr>
<tr><td><strong>Scharfenberg 2020</strong> (UFTM)</td><td>dissertação de mestrado, 101 p.</td><td><strong>alta</strong> nos dados medidos; literatura cinzenta qualificada</td></tr>
<tr><td><strong>UFMG / MOM</strong></td><td>página de universidade pública</td><td><strong>média</strong> — prova que a receita circula com aparência de autoridade</td></tr>
<tr><td><strong>Blog TCS 2016</strong></td><td>blog de divulgação</td><td><strong>média</strong> — prova documental da receita informal; química parcialmente correta</td></tr>
<tr><td><strong>Espaço Naturalmente</strong></td><td>site comercial</td><td><strong>baixa</strong> como técnica; <strong>alta</strong> como padrão de mercado</td></tr>
<tr><td><strong>ComexStat / CONAMA / WHO / PNRS</strong></td><td>dado oficial e norma</td><td><strong>alta</strong> — números primários</td></tr>
</tbody></table></div>

<h3>O que NÃO é</h3>
<ul>
<li><strong>Não é parecer jurídico.</strong> A leitura da PNRS é interpretação declarada, não consulta.</li>
<li><strong>Não afirma que o tratamento é inútil</strong> nem que deve ser abandonado.</li>
<li><strong>Não afirma que o cobre é pior que o boro</strong> — não existe ensaio comparativo.</li>
<li><strong>Não afirma o que o usuário faz na prática</strong> — isso exigiria trabalho de campo.</li>
<li><strong>Não é peça de denúncia nem tem endosso de pessoa ou instituição.</strong></li>
<li><strong>Não está homologado.</strong> Nenhuma afirmação aqui passou por revisão humana final.</li>
</ul>

<h3>A pergunta que organiza tudo</h3>
<div class="note"><p>Depois que o bambu sai do tanque, <strong>o que acontece com a água?</strong>
Ela contém metais em concentração alta. As instruções mandam reusar. <strong>Nenhuma diz o que
fazer quando o reuso acaba.</strong></p></div>

<h3>Como ler</h3>
<ul>
<li><strong>Quer entender o assunto:</strong> leia a aba <em>O cobre e a água que sobra</em>, do começo ao fim. É o artigo.</li>
<li><strong>Quer conferir uma afirmação:</strong> vá à ficha da fonte e procure a seção citada no anexo do artigo.</li>
<li><strong>Quer só o achado:</strong> abra <em>Scharfenberg 2020</em> — é a única fonte desta pesquisa que mediu o descarte.</li>
<li><strong>Quer o contraste:</strong> leia <em>Embrapa COT 110</em> e <em>Blog TCS 2016</em> em sequência. Um avisa; o outro ensina a mesma química sem avisar.</li>
</ul>

<h3>Estado do material</h3>
<div class="tabwrap"><table>
<thead><tr><th>Item</th><th>Situação</th></tr></thead>
<tbody>
<tr><td>Fontes custodiadas</td><td><strong>9</strong>, com sha256 em <code>MANIFEST_S11.json</code></td></tr>
<tr><td>Fichas produzidas</td><td><strong>6</strong>, todas em <code>ficha-em-revisao</code></td></tr>
<tr><td>Auditorias da rodada S11</td><td>R7 a R11 — três reprovações com correção material; <strong>APROVA_COM_RESSALVA</strong> na R10, <strong>CERTIFICA</strong> na R11</td></tr>
<tr><td>Homologação humana</td><td><strong>não houve</strong> — é o próximo passo, e é do soberano</td></tr>
</tbody></table></div>
"""
    secoes.append(painel("apresentacao", "Apresentação", "O que é este documento, de onde vem, e o que ele não é", apres))

    # Aba 1: artigo
    secoes.append(painel("artigo", "O cobre e a água que sobra",
                         " Artigo didático — leigo em química e em linguagem acadêmica",
                         converter(artigo_md),
                         meta="ARTIGO · docs/analyses/cobre/08-artigo-didatico-o-cobre-e-a-agua-que-sobra.md · nenhuma afirmação homologada"))

    # Abas 2..7: fichas
    for id_, titulo, sub, arq in FICHAS:
        caminho = os.path.join(FICHAS_DIR, arq)
        md = open(caminho, encoding="utf-8").read()
        b = open(caminho, "rb").read()
        secoes.append(painel(id_, titulo, sub, converter(md),
                             meta=f"FICHA · {arq} · sha256 {hashlib.sha256(b).hexdigest()[:16]} · {len(b)} B"))

    # montar — a lista de abas tem de ser a MESMA usada nos painéis
    ABAS = [("apresentacao", "Apresentação")] + [(id_, nome) for id_, nome, _s, _f in FICHAS]
    ABAS.insert(1, ("artigo", "O cobre e a água que sobra"))
    assert len(ABAS) == len(secoes), f"abas={len(ABAS)} paineis={len(secoes)}"
    nav = "".join(
        f'<button id="t-{id_}" role="tab" aria-controls="{id_}" aria-selected="{"true" if i==0 else "false"}" '
        f'tabindex="{"0" if i==0 else "-1"}">{html.escape(nome)}</button>'
        for i, (id_, nome) in enumerate(ABAS)
    )
    assert len(re.findall(r'<button id="t-', nav)) == len(secoes), "nav != paineis"
    doc = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>O cobre no bambu — artigo e fichas</title>
<meta name="description" content="Sulfato de cobre no tratamento de bambu: o que é, como age, e para onde vai a água que sobra. Artigo didático e seis fichas técnicas com fonte e hash.">
<meta property="og:title" content="O cobre no bambu — artigo e fichas">
<meta property="og:description" content="O que é o sulfato de cobre, o que ele faz no bambu, e o que acontece com a solução que sobra — com cada número ligado à fonte.">
<meta property="og:type" content="article">
<style>{CSS}</style>
</head>
<body>
<header>
<p class="kicker">Acervo Soberania Tecnológica · frente COBRE</p>
<h1>O cobre no bambu</h1>
<p class="sub">O que é o sulfato de cobre, o que ele faz no tratamento, e <strong>para onde vai a
água que sobra</strong> — artigo didático e seis fichas técnicas, cada afirmação ligada à fonte.</p>
<div class="chips">
<span class="chip">EM REVISÃO DOCUMENTAL</span>
<span class="chip">9 FONTES CUSTODIADAS</span>
<span class="chip">6 FICHAS</span>
<span class="chip">NÃO HOMOLOGADO</span>
</div>
</header>
<nav class="tabs" role="tablist" aria-label="Seções do documento">{nav}</nav>
<main>
{chr(10).join(secoes)}
</main>
<footer>
<p><strong>Documento em revisão documental.</strong> Nenhuma afirmação passou por homologação
humana. As fontes estão custodiadas com sha256; as fichas estão em <code>ficha-em-revisao</code>.
Assistência documental por agente de IA, sujeita a revisão humana.</p>
</footer>
<script>{JS}</script>
</body>
</html>"""
    open(SAIDA, "w", encoding="utf-8").write(doc)

    # diagnóstico obrigatório
    print(f"seções: {len(secoes)}")
    for id_, nome, sub, arq in FICHAS:
        p = os.path.join(FICHAS_DIR, arq)
        print(f"  {id_:10s} md={len(open(p,encoding='utf-8').read()):6d} chars")
    print(f"artigo: {len(artigo_md)} chars")
    print(f"saída:  {SAIDA} ({len(doc)} chars)")
    # ordem de ênfase aninhada
    ruim = re.findall(r"<strong>[^<]*<em>[^<]*</strong></em>", doc)
    print(f"ênfase aninhada fora de ordem: {len(ruim)}")
    return doc

if __name__ == "__main__":
    main()
