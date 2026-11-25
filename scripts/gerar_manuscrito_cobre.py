#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera o MANUSCRITO ÚNICO em Markdown — do início ao fim, com referências bibliográficas.

FONTE:    scripts/conteudo_cobre.py (texto das seções)  +  scripts/referencias_cobre.py
SAÍDA:    docs/analyses/cobre/00-artigo-o-cobre-explicado-do-zero.md

O .md é o manuscrito canônico. A peça HTML é derivada dele (via as mesmas fontes Python),
e um gate confere que os dois dizem a mesma coisa.
"""
import os, re, sys, html as _h

_AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _AQUI)
import conteudo_cobre as C
import referencias_cobre as R
import resumos_fontes_cobre as RS


def _md(s):
    """Converte a marcação HTML dos resumos para Markdown."""
    s = re.sub(r"<strong>(.*?)</strong>", r"**\1**", s, flags=re.S)
    s = re.sub(r"<em>(.*?)</em>", r"*\1*", s, flags=re.S)
    s = re.sub(r"<[^>]+>", "", s)
    return _h.unescape(s)

REPO = os.environ.get("COBRE_REPO", "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica")
SAIDA = f"{REPO}/docs/analyses/cobre/00-artigo-o-cobre-explicado-do-zero.md"


def html_para_md(trecho):
    """Converte o HTML das seções de volta para Markdown, de forma conservadora."""
    t = trecho

    # tabelas -> pipe
    def tab(m):
        corpo = m.group(1)
        linhas, cab = [], None
        for tr in re.findall(r"<tr>(.*?)</tr>", corpo, re.S):
            ths = re.findall(r"<th>(.*?)</th>", tr, re.S)
            tds = re.findall(r'<td[^>]*>(.*?)</td>', tr, re.S)
            if ths:
                cab = ths
            elif tds:
                linhas.append(tds)
        if not cab:
            return ""
        out = ["| " + " | ".join(c.strip() for c in cab) + " |",
               "|" + "|".join(["---"] * len(cab)) + "|"]
        for ln in linhas:
            out.append("| " + " | ".join(c.strip().replace("\n", " ") for c in ln) + " |")
        return "\n".join(out) + "\n"
    t = re.sub(r'<div class="tabwrap"><table[^>]*><thead>(.*?)</tbody></table></div>', tab, t, flags=re.S)

    # caixas e blocos compostos: pareamento de div, não regex guloso
    def _bloco_div(txt, classe):
        """Extrai o miolo de <div class="classe"> ... </div> pareando as divs."""
        abre = f'<div class="{classe}">'
        i = txt.find(abre)
        if i < 0:
            return None, txt
        j = i + len(abre)
        prof = 1
        while j < len(txt) and prof:
            a = txt.find("<div", j)
            f = txt.find("</div>", j)
            if f < 0:
                return None, txt
            if 0 <= a < f:
                prof += 1
                j = a + 4
            else:
                prof -= 1
                j = f + 6
        return txt[i + len(abre):f], txt[:i] + "\x00BLOCO\x00" + txt[j:]

    def kpi(miolo):
        pares = re.findall(r'<div class="kpi"><div class="n">(.*?)</div><div class="l">(.*?)</div></div>',
                           miolo, re.S)
        if not pares:
            return ""
        out = ["| Número | O que significa |", "|---|---|"]
        out += [f"| **{n}** | {l} |" for n, l in pares]
        return "\n".join(out) + "\n"

    def cards(miolo):
        itens = re.findall(r'<div class="card"><div class="tag">(.*?)</div><h4>(.*?)</h4><p>(.*?)</p></div>',
                           miolo, re.S)
        return "\n" + "\n".join(f"- **{ti}** ({tag}) — {corpo}" for tag, ti, corpo in itens) + "\n"

    for classe, fn in (("kpis", kpi), ("grid2", cards)):
        while True:
            miolo, t = _bloco_div(t, classe)
            if miolo is None:
                break
            extra = "\n\n" + fn(miolo) + "\n\n"
            t = t.replace("\x00BLOCO\x00", extra, 1) if "\x00BLOCO\x00" in t else t

    # caixas -> blockquote com rótulo
    def caixa(m):
        classe, tit, corpo = m.group(1), m.group(2), m.group(3)
        corpo = re.sub(r"<[^>]+>", "", corpo).strip()
        return f"\n> **{tit}** — {corpo}\n"
    t = re.sub(r'<div class="(note|okbox|danger)"><strong>(.*?)</strong><p>(.*?)</p></div>',
               caixa, t, flags=re.S)


    # inline
    # marca de citação: <sup class="cit">(3)</sup> -> (3), antes de remover tags
    t = re.sub(r'<sup class="cit">(.*?)</sup>', r" \1", t, flags=re.S)
    t = re.sub(r"<blockquote>(.*?)</blockquote>", lambda m: "\n> " + re.sub(r"<[^>]+>", "", m.group(1)).strip() + "\n", t, flags=re.S)
    t = re.sub(r"<h4>(.*?)</h4>", r"\n#### \1\n", t, flags=re.S)
    t = re.sub(r"<h3>(.*?)</h3>", r"\n### \1\n", t, flags=re.S)
    t = re.sub(r"<strong>(.*?)</strong>", r"**\1**", t, flags=re.S)
    t = re.sub(r"<em>(.*?)</em>", r"*\1*", t, flags=re.S)
    t = re.sub(r"<li>(.*?)</li>", r"- \1", t, flags=re.S)
    t = re.sub(r"</?[uo]l>", "", t)
    t = re.sub(r"<p>(.*?)</p>", r"\1", t, flags=re.S)
    t = re.sub(r'<hr class="sep">', "\n---\n", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = _h.unescape(t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def montar():
    partes = []
    palavras = 0

    partes.append("""---
schema: ACERVO_ARTIGO_R1
gaveta: cobre
frente: COBRE
titulo: "O cobre, explicado do zero"
subtitulo: "Um metal comum, uma solução azul e a pergunta que quase ninguém faz: para onde vai a água do tratamento"
tipo_documental: ensaio-tecnico
estado_documental: em-revisao-documental
homologacao_automatica: false
versao: 3
data_revisao: 2026-11-24
responsavel_curadoria: Fabio Takwara
assistencia_documental: agente de IA, sujeito a revisao humana
publico: "leigo em quimica e em linguagem academica"
camada: "B — adaptacao publica em linguagem nao especializada"
peca_html: "o-cobre-no-bambu.html (gerada de scripts/conteudo_cobre.py)"
fichas: "docs/analyses/cobre/fichas/ (11 fichas)"
referencias: "21 entradas, numeradas — ver secao Referencias"
---

# O cobre, explicado do zero

## Um metal comum, uma solução azul e a pergunta que quase ninguém faz: para onde vai a água do tratamento

> **Nota de leitura.** Este é o manuscrito completo, do início ao fim, com as referências
> bibliográficas numeradas ao final. As chamadas no corpo aparecem entre parênteses — por
> exemplo (1) remete à primeira referência da lista. As 11 fichas técnicas que sustentam
> os números estão identificadas na seção **Fontes custodiadas**.

---
""")

    for p in C.PAGINAS:
        corpo = html_para_md(p["corpo"])
        palavras += len(re.findall(r"[A-Za-zÀ-ÿ]{2,}", corpo))
        # a capa, o resumo-final e o glossário não levam número; o resto leva.
        # A regra é por id porque o número muda de dono quando entra capítulo novo.
        sem_numero = {"p-1", "p-9", "p-10", "p-11"}
        cab = (f"\n## {_h.unescape(p['h2'])}\n\n" if p["id"] in sem_numero
               else f"\n## {p['num']} · {_h.unescape(p['h2'])}\n\n")
        partes.append(cab + corpo + "\n\n---\n")

    # fichas
    partes.append("## Fontes custodiadas e fichas técnicas\n")
    partes.append(
        "Cada ficha identifica a fonte primária, o hash de integridade e o que ela autoriza afirmar. "
        "Estão em `docs/analyses/cobre/fichas/`.\n")
    fichas = [
        ("1. Embrapa COT 110", "ficha-embrapa-cot110-tratamento-madeira-propriedade-rural.md",
         "instrução oficial brasileira — EPI, tonel, reuso"),
        ("2. NMBA 2006 (Índia)", "ficha-nmba-2006-preservation-of-bamboo-manual.md",
         "manual oficial indiano — decantar, reusar, proibições"),
        ("3. Scharfenberg 2020 (UFTM)", "ficha-scharfenberg-2020-bambu-cb-fitotoxicidade.md",
         "mede a fitotoxicidade do descarte"),
        ("4. UFMG / MOM", "ficha-ufmg-mom-tratamento-com-borax.md",
         "receita publicada por universidade pública"),
        ("5. Blog TCS 2016", "ficha-blog-tsc-como-tratar-bambu.md",
         "receita informal completa, sem aviso"),
        ("6. Espaço Naturalmente", "ficha-espaconaturalmente-bambu.md",
         "padrão de mercado"),
        ("7. Portaria Interministerial 292/89", "ficha-pi292-89-registro-preservativos-madeira.md",
         "registro obrigatório no Ibama e competência de fiscalização (art. 20)"),
        ("8. Portaria Normativa Ibama 151/97", "ficha-pn151-97-ibama-risco-ambiental.md",
         "o registro condicionado à determinação do risco ambiental"),
        ("9. Iema-ES, NT 01/2023", "ficha-iema-es-nt01-2023-preservacao-madeira.md",
         "«não há proibição no Brasil» e a falta de dados sobre o resíduo do CCB"),
        ("10. ABPM / FG4mad", "ficha-abpm-fg4mad-destinacao-residuo-madeira-tratada.md",
         "a própria cadeia proíbe queima em fogão e a céu aberto"),
        ("11. Ciência Florestal 2025", "ficha-ufsm-2025-cca-moiroes-contaminacao-solo.md",
         "880 dias de campo: arsênio no solo +129,2%"),
    ]
    for tit, arq, desc in fichas:
        partes.append(f"- **{tit}** — {desc}. Ficha: `{arq}`")
    partes.append("")

    # referências
    partes.append("---\n\n## Referências\n")
    partes.append(
        "Numeradas na ordem em que aparecem pela primeira vez no texto. Onde a fonte é uma "
        "página web sem data declarada, registra-se [s.d.].\n")
    for i, (ch, a, an, ti, ve, cu, su) in enumerate(R.REFERENCIAS, 1):
        res = RS.resumo(ch)
        linhas = R.lista_abnt().split("\n")
        break
    # entradas numeradas, com a síntese em itálico (igual à bibliografia da peça)
    for i, (ch, a, an, ti, ve, cu, su) in enumerate(R.REFERENCIAS, 1):
        res = RS.resumo(ch)
        partes.append(
            f"{i}. {R._fecha_ponto(a)} **{R._fecha_ponto(ti)}** "
            f"{R._fecha_ponto(str(an or '[s.d.]'))} {R._fecha_ponto(ve)}"
            + (f" — {_md(res)}" if res else ""))

    # declaração
    partes.append("""---

## Autoria, assistência e responsabilidade

**Autor:** Fabio Takwara.

**Apoio de IA:** ferramenta de inteligência artificial foi utilizada para localizar relações
entre fontes, estruturar o comparativo, conferir consistência interna, apoiar a redação e
executar os cálculos de diluição. **A seleção interpretativa, a perspectiva e a
responsabilidade pela versão publicada permanecem com o autor.**

**Natureza:** artigo de divulgação — Camada B, adaptação pública em linguagem não especializada.

**Estado:** em revisão documental. Não homologado.

**Conflitos de interesse:** declarados inexistentes.

**Financiamento:** não se aplica a esta versão.
""")

    doc = "\n".join(partes)
    doc = re.sub(r"\n{3,}", "\n\n", doc)
    open(SAIDA, "w", encoding="utf-8").write(doc)
    return doc, palavras


if __name__ == "__main__":
    doc, palavras = montar()
    secs = len(re.findall(r"^## ", doc, re.M))
    refs = len(R.REFERENCIAS)
    linhas = doc.count("\n") + 1
    print(f"  seções de nível 2: {secs}")
    print(f"  referências: {refs}")
    print(f"  palavras no corpo: ~{palavras:,}".replace(",", "."))
    print(f"  tabelas markdown: {len(re.findall(r'^\|---', doc, re.M))}")
    print(f"  linhas: {linhas} | bytes: {len(doc.encode()):,}")
    print(f"  saída: {SAIDA}")
    faltando = [c for c in ("Referências", "Fontes custodiadas", "Autoria") if c not in doc]
    print(f"\nRESULTADO: {'MANUSCRITO COMPLETO' if not faltando else 'FALTA ' + str(faltando)}")
