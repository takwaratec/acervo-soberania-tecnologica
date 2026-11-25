#!/usr/bin/env python3
"""Registro auditavel de afirmacao numerica do artigo do boro.

Um comando: python3.11 rodar.py
Saida: registro.jsonl (uma linha por afirmacao), resumo.json, REGISTRO.md

Regra declarada antes da medicao: REGRA_DE_CONTAGEM.md (neste diretorio).
Nada aqui decide se o texto esta certo: mede e registra.
"""
import importlib.util
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
GATE_DIR = os.environ.get("GATE_DIR", "/Users/fabiotakwara/.hermes/cache/scratch/gate-boro/ops/command-center/metodo")
ACERVO = os.environ.get("ACERVO", "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica")
ARTIGO = os.environ.get("ARTIGO", os.path.join(
    "/Users/fabiotakwara/.hermes/cache/scratch/boro-v4-wt/docs/analyses/boro",
    "artigo-o-boro-explicado-do-zero.md"))
BORO = os.path.join(ACERVO, "_privado/governanca-operacional/extracoes/boro")

# [n] -> fonte custodiada. None = nao ha fonte custodiada para a entrada.
MAPA = {
    1: "herdado/ago_28_Boratos_Cobre/pdf/WHO_2009_Boron-in-Drinking-Water_Background.pdf",
    2: "herdado/ago_28_Boratos_Cobre/pdf/WHO_2022_Boron_Chemical-Fact-Sheet.pdf",
    3: "fontes_novas/USGS_MCS2026_Boron.pdf",
    4: None,  # ComexStat: dados brutos em JSON, tratado a parte
    5: "fontes_novas/EMA_BoricAcid_Borates_Excipients.pdf",
    6: "fontes_novas/BVS_ANVISA_RDC199_2006.pdf",
    7: "fontes_novas/atsdr_tp26/ATSDR_tp26_BORON.pdf",
    8: "fontes_novas/nih_ods/NIH_ODS_Boron_HealthProfessional_20261116.html",
    9: "fontes_novas/r4_indicadas/EU_2023_1435_CLP_regulamento.html",
    10: None,  # massa atomica: derivacao aritmetica declarada, nao fonte externa
    11: "herdado/ago_28_CCA_CCB/pdf/Ferrarini_2012_CCA_Boro_Fluor.pdf",
    12: "fontes_novas/r5_residuos/asia/Liese_Preservation_of_Bamboo_in_Service.pdf",
    13: "fontes_novas/r5_residuos/Kaminski_2016_Structural_use_of_bamboo_Part2_durability.pdf",
    14: None,
    15: "fontes_novas/r5_residuos/Archello_2023_Arc_GreenSchool.html",
    16: None,
    17: "fontes_novas/r5_residuos/AKAA_2010_OnSiteReview_GreenSchool_Bali.pdf",
    18: "fontes_novas/r5_residuos/IBUKU_FAQ_maintenance.html",
    19: "fontes_novas/r5_residuos/Araujo_2025_ACV_colmo_bambu_Amazonia.pdf",
    20: "fontes_novas/r5_residuos/asia/China_GBT_40245_2021_recovery_waste_preservative_wood.html",
    21: "fontes_novas/r5_residuos/asia/INBAR_2019_Bamboo_Circular_Economy.pdf",
    22: None,
    23: "fontes_novas/r5_residuos/asia/HK_BD_Guidelines_Design_Construction_Bamboo_Scaffolds.pdf",
    24: "herdado/ago_28_Boratos_Cobre/pdf/Liu_2023_Bamboo_Boric-Acid_Borax.pdf",
    25: "herdado/ago_28_CCA_CCB/pdf/Rusch_2023_CCB_Bambu.pdf",
    26: ["fontes_novas/r4_indicadas/NIOSH_npgd0057_tetraborato_anidro.html",
         "fontes_novas/r4_indicadas/NIOSH_npgd0058_borax_decahydrate.html",
         "fontes_novas/r4_indicadas/NIOSH_npgd0059_tetraborato_pentahidratado.html"],
    27: "fontes_novas/br_limbo/Lei_12305_2010_PNRS.html",
    28: "fontes_novas/br_limbo/Lei_12484_2011_Bambu.html",
    29: "fontes_novas/atsdr_tp26/chapters/at_c6.pdf",
    30: None,
    31: "fontes_novas/andes_mineracao/original/Turker_2016_Kirka_wetland_arsenic_mine_effluent.pdf",
    32: "fontes_novas/andes_mineracao/original/MEE_2023_12_01_Qaidam_salares_inspecao.html",
}

MOTIVO_SEM_FONTE = {
    4: "ComexStat e base de dados, nao documento paginado; medida a parte contra raw/ncm_*.json",
    10: "derivacao aritmetica declarada a partir de massas atomicas; nao ha fonte externa a conferir",
    14: "obra citada sem arquivo custodiado nesta gaveta",
    16: "obra citada sem arquivo custodiado nesta gaveta",
    22: "obra citada sem arquivo custodiado nesta gaveta",
    30: "obra citada sem arquivo custodiado nesta gaveta",
}


def carregar_gate():
    sys.path.insert(0, GATE_DIR)
    spec = importlib.util.spec_from_file_location(
        "gate_fidelidade", os.path.join(GATE_DIR, "gate_fidelidade_fonte.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def texto_com_paginas(caminho):
    """Devolve texto com marcador de pagina. PDF: pagina do arquivo. HTML: p. 1."""
    if caminho.endswith(".html"):
        bruto = open(caminho, encoding="utf-8", errors="replace").read()
        bruto = re.sub(r"(?is)<(script|style).*?</\1>", " ", bruto)
        bruto = re.sub(r"(?s)<[^>]+>", " ", bruto)
        bruto = re.sub(r"&nbsp;", " ", bruto)
        bruto = re.sub(r"\s+", " ", bruto)
        return "=== PÁGINA 1 ===\n" + bruto
    import fitz
    doc = fitz.open(caminho)
    partes = []
    for i in range(doc.page_count):
        partes.append(f"=== PÁGINA {i + 1} ===\n" + (doc[i].get_text() or ""))
    return "\n".join(partes)


def corpo_do_artigo(t):
    ini = t.find("\n## 1.")
    if ini < 0:
        ini = 0
    fim = t.find("## Glossário")
    if fim < 0:
        fim = len(t)
    return t[ini:fim]


def paragrafos(corpo):
    """Paragrafo = bloco separado por linha em branco. Tabela = bloco continuo de '|'."""
    blocos, atual = [], []
    for linha in corpo.split("\n"):
        if linha.strip() == "":
            if atual:
                blocos.append(atual)
                atual = []
        else:
            atual.append(linha)
    if atual:
        blocos.append(atual)
    return blocos


RE_NUM = re.compile(r"\d+(?:[.,]\d+)*(?:[eE][+-]?\d+|[×x]\s*10[-−]?\d+)?")
RE_UNIDADE = re.compile(
    r"^\s*(%|mg/m³|mg/m3|mg/L|mg/kg|mg B/kg/dia|mg B/m³|mg B/L|µg/L|ug/L|g/mol|g|kg|t|kt|m³|m3|"
    r"mg|µg|ug|mPt|ppm|°C|h|MPa|mm|cm|km|ha|mu|anos|vezes|kW|L|mL|mmol|mol|B/kg|mg B|µg B)",
    re.I)
RE_SECAO = re.compile(r"^## ")
RE_TABELA = re.compile(r"^\|")


def extrair_afirmacoes(corpo):
    """Aplica REGRA_DE_CONTAGEM.md. Devolve lista de dicts."""
    saida = []
    secao = "?"
    ultima_fonte = None
    nota_ativa = None
    nota_texto = ""
    nota_tipo = "TABELA_COM_NOTA"
    BLOCOS = paragrafos(corpo)
    for i_bloco, bloco in enumerate(BLOCOS):
        primeira = bloco[0].strip()
        if RE_SECAO.match(primeira):
            secao = primeira.lstrip("# ").strip()
            nota_ativa = None
            bloco = bloco[1:]
            if not bloco:
                continue
        if not bloco:
            continue
        # Bloco que DECLARA o estatuto (nota de tabela / de onde vem o numero) e metadado:
        # nao afirma nada sobre o mundo. Seus digitos nao sao afirmacao, e o estatuto vale
        # para a tabela seguinte.
        bruto = "\n".join(bloco)
        if RE_ESTATUTO.search(bruto):
            nota_texto = bruto
            if RE_NOTA_TABELA.search(bruto):
                nota_tipo = "TABELA_COM_NOTA"
            elif re.search(r"(?i)estatuto dos n[uú]meros", bruto):
                nota_tipo = "DERIVACAO_DECLARADA" if re.search(r"(?i)c[aá]lculo", bruto) else "RESUMO_DE_FONTE_NOMEADA"
            else:
                nota_tipo = "RESUMO_DE_FONTE_NOMEADA"
            nota_ativa = nota_tipo
            if bruto.lstrip().startswith(">"):
                continue
            bloco = [re.sub(r"^\s*>\s?", "", l) for l in bloco]
        if RE_NOTA_TABELA.search(bruto):
            nota_ativa = "TABELA_COM_NOTA"
        # nota em bloco faz parte do corpo: a regra declara corpo = secoes 1-19 e nao a exclui
        bloco = [re.sub(r"^\s*>\s?", "", l) for l in bloco]
        texto = "\n".join(bloco)
        em_tabela = all(RE_TABELA.match(l.strip()) or not l.strip() for l in bloco)
        citacoes = [int(x) for x in re.findall(r"\[(\d{1,2})\]", texto)]
        if citacoes:
            ultima_fonte = citacoes[0]
        estatuto = estatuto_do_bloco(texto, ultima_fonte) if not citacoes else None
        if em_tabela and not nota_ativa and i_bloco + 1 < len(BLOCOS):
            prox = "\n".join(BLOCOS[i_bloco + 1])
            if RE_NOTA_TABELA.search(prox):
                nota_pendente = True
        # TABELA_COM_NOTA vale para a tabela seguinte; RESUMO/DERIVACAO valem ate o fim da secao
        if not citacoes and nota_ativa:
            estatuto = {"tipo": nota_ativa, "fonte": ultima_fonte}
            if nota_ativa == "TABELA_COM_NOTA":
                nota_ativa = None
        em_tabela = all(RE_TABELA.match(l.strip()) or not l.strip() for l in bloco)
        # linhas de cabecalho/separador de tabela
        for linha in bloco:
            l = linha.rstrip()
            if not l.strip():
                continue
            if em_tabela:
                if re.fullmatch(r"\|[\s:|-]+\|", l.strip()):
                    continue
                celulas = [c.strip() for c in l.strip().strip("|").split("|")]
                for k, cel in enumerate(celulas):
                    for valor, unidade in _pares(cel):
                        saida.append(dict(secao=secao, paragrafo=texto[:60].replace("\n", " "),
                                          sujeito=f"coluna {k + 1}", valor=valor,
                                          unidade=unidade, citacoes=citacoes, estatuto=estatuto,
                                          contexto=cel[:160], tabela=True))
                continue
            for valor, unidade, ini, fim in _pares_pos(l):
                ctx = l[max(0, ini - 90):min(len(l), fim + 90)].strip()
                # atribuicao: a citacao da MESMA sentenca; sem ela, a do bloco so quando ha uma
                cits = _citacoes_da_sentenca(l, ini, fim) or (citacoes if len(set(citacoes)) == 1 else [])
                saida.append(dict(secao=secao, paragrafo=texto[:60].replace("\n", " "),
                                  sujeito=ctx[:80], valor=valor, unidade=unidade,
                                  citacoes=cits, estatuto=estatuto,
                                  contexto=ctx[:200], tabela=False))
    return saida


RE_FIM_FRASE = re.compile(r"(?<=[.;:!?])\s+")


def _citacoes_da_sentenca(linha, ini, fim):
    """[n] da mesma sentenca do numero: depois dele ate o fim da frase, ou antes ate o inicio."""
    depois = linha[fim:]
    m = RE_FIM_FRASE.search(depois)
    trecho_depois = depois[:m.start()] if m else depois
    cits = [int(x) for x in re.findall(r"\[(\d{1,2})\]", trecho_depois)]
    if cits:
        return cits
    antes = linha[:ini]
    corte = max(antes.rfind(". "), antes.rfind("; "), antes.rfind(": "))
    trecho_antes = antes[corte + 1:] if corte > 0 else antes
    return [int(x) for x in re.findall(r"\[(\d{1,2})\]", trecho_antes)]


RE_NOTA_TABELA = re.compile(r"(?i)fonte da tabela inteira")
RE_ESTATUTO = re.compile(r"(?i)(fonte da tabela inteira|de onde vem cada n[uú]mero|estatuto dos n[uú]meros|"
                         r"todos os n[uú]meros deste)")
RE_RESUMO = re.compile(r"(?i)(resumo dess[ae] mesma fonte|j[aá] nomead[ao]|j[aá] citad[ao]|"
                       r"mesma fonte, j[aá] citada|do mesmo estudo)")
RE_CALCULO = re.compile(r"(?i)(c[aá]lculo (a partir|sobre)|s[aã]o \*\*c[aá]lculo\*\*|"
                        r"todos s[aã]o \*\*c[aá]lculo|dividindo|massa de boro pela massa)")


def estatuto_do_bloco(bloco_txt, ultima_fonte):
    """Le do proprio texto o estatuto da afirmacao sem [n]."""
    fonte = ultima_fonte
    if RE_NOTA_TABELA.search(bloco_txt):
        return {"tipo": "TABELA_COM_NOTA", "fonte": fonte}
    if RE_RESUMO.search(bloco_txt):
        return {"tipo": "RESUMO_DE_FONTE_NOMEADA", "fonte": fonte}
    if RE_CALCULO.search(bloco_txt):
        return {"tipo": "DERIVACAO_DECLARADA", "fonte": None}
    return None


def _pares(trecho):
    """(valor, unidade) em um trecho curto, com a regra declarada."""
    out = []
    for m in RE_NUM.finditer(trecho):
        valor = m.group(0)
        if _excluido(trecho, m.start(), valor):
            continue
        resto = trecho[m.end():m.end() + 12]
        u = RE_UNIDADE.match(resto)
        out.append((valor, (u.group(1) if u else "")))
    return out


def _pares_pos(trecho):
    out = []
    for m in RE_NUM.finditer(trecho):
        valor = m.group(0)
        if _excluido(trecho, m.start(), valor):
            continue
        resto = trecho[m.end():m.end() + 12]
        u = RE_UNIDADE.match(resto)
        out.append((valor, (u.group(1) if u else ""), m.start(), m.end()))
    return out


def _excluido(linha, pos, valor):
    """Exclusoes da regra: ano, citacao [n], secao, NCM, DOI, p. N, contagem de fichas."""
    antes = linha[max(0, pos - 12):pos]
    depois = linha[pos + len(valor):pos + len(valor) + 4]
    # numero CAS (10043-35-3): identificador de substancia, mesma classe de NCM.
    # O valor esta DENTRO de um CAS quando algum casamento cobre a posicao.
    for mcas in re.finditer(r"\d{2,7}-\d{2}-\d", linha):
        if mcas.start() <= pos and pos + len(valor) <= mcas.end():
            return True
    # subscrito de formula quimica: o digito esta COLADO a um simbolo (10H2O, 5H2O).
    # Em prosa ha espaco ("10 mg"); em formula nao ha.
    if re.match(r"^[A-Z][a-z]?[\u2080-\u2089\d]", depois):
        return True
    # codigo de perigo CLP (H360FD, H360F, H360D) e categoria de perigo (Repr. 1B, cat. 2)
    if re.search(r"H\s?\d{3}", linha[max(0, pos - 6):pos + len(valor) + 6]):
        return True
    if re.search(r"(?i)\b(rep[r]?\.?|cat[a-z]*\.?)\s*[\"']?\s*$", antes):
        return True
    # referencia a secao do proprio texto (§18, §9)
    if "§" in linha[max(0, pos - 3):pos]:
        return True
    # data por extenso ("1º de fevereiro")
    if re.match(r"(?i)\s*[ºo]?\s*de\s+(janeiro|fevereiro|março|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro)", depois):
        return True
    # ordinal de lista em negrito ("**4. A queima") — mesma classe do ordinal simples
    if re.match(r"\s*\*\*\s*$", antes) and re.match(r"^\s*\.\s", depois):
        return True
    # ordinal de lista ("1. ", "2. ") — mesma classe de numero de secao
    if re.match(r"^\s*\d{1,2}\.\s", linha) and re.match(r"^\s*\d{1,2}$", valor):
        return True
    # [n]
    if antes.endswith("[") and depois.startswith("]"):
        return True
    # p. N / pp. N
    if re.search(r"(?i)\bpp?\.\s*$", antes):
        return True
    # ano de quatro digitos isolado
    if re.fullmatch(r"(19|20)\d{2}", valor):
        return True
    # NCM de oito digitos, e NCM pontuado (2810.00.10, 2840.11, 2804.50.00)
    if re.fullmatch(r"\d{8}", valor):
        return True
    for mncm in re.finditer(r"\d{4}\.\d{2}(?:\.\d{2})?", linha):
        if mncm.start() <= pos and pos + len(valor) <= mncm.end():
            return True
    # DOI / volume / numero de secao
    if re.search(r"(?i)\bdoi[:\s]*\S*$", antes):
        return True
    if re.search(r"(?i)^[.\s]*§", antes):
        return True
    if re.search(r"(?i)\b(tabela|quadro|figura|se[cç][aã]o|art\.|artigo)\s*$", antes):
        return True
    # numero de citacao entre colchetes ao lado
    if depois.strip().startswith("]"):
        return True
    return False


def arquivos_de(c):
    rel = MAPA.get(c)
    if rel is None:
        return []
    return rel if isinstance(rel, list) else [rel]


def normaliza(v):
    return re.sub(r"[^\d.,]", "", v).replace(",", ".")


RE_MARCA = re.compile(r"^=+\s*P[\u00c1A]GINA\s+\d+\s*=+$", re.M)


def texto_utilizavel(fonte_txt):
    """Fonte custodiada que e pagina de bloqueio/JS nao mede nada."""
    corpo = RE_MARCA.sub("", fonte_txt)
    palavras = re.findall(r"[A-Za-z\u00c0-\u00ff]{3,}", corpo)
    return len(palavras) >= 40


DERIVACAO = re.compile(
    r"(?i)\b(o que d[aá]|equivale|corresponde|corresponderia|calculad[oa]|convertid[oa]|"
    r"resulta em|multiplicad[oa]|dividid[oa]|raz[aã]o de|com base na massa|a partir da massa)")


def paginas_do_valor(mod, fonte_txt, valor, contexto=""):
    """Paginas em que o valor ocorre, ordenadas por co-ocorrencia com os outros
    numeros da mesma frase.

    Presenca do valor nao basta: `60` aparece como dose na p.13 e como peso
    corporal na p.22. A pagina certa e a que traz os companheiros de frase."""
    paginas = mod.dividir_paginas(fonte_txt) or {0: fonte_txt}
    alvo = normaliza(valor)
    co = {normaliza(v) for v in RE_NUM.findall(contexto or "") if normaliza(v) != alvo}
    achadas = []
    for p, txt in paginas.items():
        presentes = {normaliza(m.group(0)) for m in RE_NUM.finditer(txt)}
        if alvo not in presentes:
            continue
        # pagina de bibliografia/referencias nao e pagina de resultado: o numero ali e
        # ano de obra citada, nao medida. Medido: p.13 de Kaminski e p.14 de Araujo.
        cits = len(re.findall(r"\((?:19|20)\d{2}[a-z]?\)", txt))
        penal = 5 if cits >= 8 else 0
        # coordenada geografica nao e medida: em "53°23'40\" W" o 40 e grau/minuto/segundo.
        # Medido: Rusch 2023 p.2 tem 40 na latitude e o indice 40 na Tabela 2 da p.5.
        for mcoord in re.finditer(r"\d+\s*°\s*\d+\s*['\u2032]\s*[\d.,]+", txt):
            if alvo in {normaliza(v) for v in re.findall(r"[\d.,]+", mcoord.group(0))}:
                penal = max(penal, 99)
        # companheiro COM unidade vale mais que numero solto: "1%" e "3%" ancoram a tabela.
        bonus = sum(1 for v in co if re.search(re.escape(v) + r"\s*%", txt))
        achadas.append((len(co & presentes) - penal + 2 * bonus, p))
    achadas.sort(key=lambda x: (-x[0], x[1]))
    return [p for _, p in achadas]


STOP = set("para como onde quando pela pelo pelos pelas esta este estes estas isso essa "
           "esse aquilo entre sobre ainda muito pouco cada mais menos sem com dos das nos nas "
           "uma que nao foi sao ser tem ter".split())


def _palavras(s):
    s = re.sub(r"[*_`]", "", s or "").lower()
    return {w for w in re.findall(r"[a-z\u00e0-\u00ff]{4,}", s) if w not in STOP}


def _sujeito_confere(cache, mod, a, fonte_ref, pagina):
    """Fracao das palavras de conteudo da afirmacao presentes na vizinhanca do numero."""
    if pagina is None:
        return None
    alvo = normaliza(a["valor"])
    for caminho, txt in cache.items():
        if txt == "SEM_TEXTO":
            continue
        paginas = mod.dividir_paginas(txt)
        if pagina not in paginas:
            continue
        corpo = paginas[pagina]
        for m in RE_NUM.finditer(corpo):
            if normaliza(m.group(0)) != alvo:
                continue
            janela = corpo[max(0, m.start() - 260):m.start() + 260].lower()
            alvo_pal = _palavras(a["contexto"])
            if not alvo_pal:
                return None
            return round(len(alvo_pal & set(re.findall(r"[a-z\u00e0-\u00ff]{4,}", janela))) / len(alvo_pal), 2)
    return None


SEM_NUM_GLOBAL = [0]


def main():
    mod = carregar_gate()
    t = open(ARTIGO, encoding="utf-8").read()
    corpo = corpo_do_artigo(t)
    afir = extrair_afirmacoes(corpo)
    print(f"afirmacoes extraidas pela regra: {len(afir)}", file=sys.stderr)

    cache = {}
    registro = []
    for i, a in enumerate(afir, 1):
        fontes = [c for c in a["citacoes"] if c in MAPA]
        veredito, pagina, motivo, fonte_usada = None, None, "", None
        # ---- estatuto declarado NO TEXTO: tres marcadores previstos na regra ----
        if not a["citacoes"]:
            est = a.get("estatuto")
            if est and est.get("tipo") and est.get("fonte") in MAPA:
                fonte_usada = est["fonte"]
                if est["tipo"] == "TABELA_COM_NOTA":
                    veredito, motivo = "TABELA_COM_NOTA", "fonte declarada em nota de tabela"
                elif est["tipo"] == "RESUMO_DE_FONTE_NOMEADA":
                    veredito, motivo = "RESUMO_DE_FONTE_NOMEADA", "resumo de fonte ja nomeada no texto"
                elif est["tipo"] == "DERIVACAO_DECLARADA":
                    veredito, motivo = "DERIVACAO_DECLARADA", "calculo declarado no texto"
            elif est and est.get("tipo") == "DERIVACAO_DECLARADA":
                veredito, motivo = "DERIVACAO_DECLARADA", "calculo declarado no texto, sem fonte de entrada"
            else:
                veredito, motivo = "NAO_MEDIDO", "afirmacao sem citacao [n]: nao ha fonte declarada"
        elif not fontes:
            veredito = "NAO_MEDIDO"
            motivo = "; ".join(f"[{c}] {MOTIVO_SEM_FONTE.get(c, 'sem fonte custodiada')}"
                               for c in a["citacoes"])
        else:
            candidatos = []
            for c in fontes:
                for rel in arquivos_de(c):
                    caminho = os.path.join(BORO, rel)
                    if not os.path.exists(caminho):
                        candidatos.append((c, None, None))
                        continue
                    if caminho not in cache:
                        cache[caminho] = texto_com_paginas(caminho)
                    fonte_txt = cache[caminho]
                    if not texto_utilizavel(fonte_txt):
                        candidatos.append((c, "SEM_TEXTO", None))
                        continue
                    pgs = paginas_do_valor(mod, fonte_txt, a["valor"], a["contexto"])
                    candidatos.append((c, fonte_txt, pgs))
            # derivacao declarada no proprio texto: nao e valor da fonte
            if DERIVACAO.search(a["contexto"] or ""):
                veredito = "NAO_MEDIDO"
                motivo = "derivacao aritmetica declarada no texto: nao e valor da fonte"
            # fonte custodiada sem camada de texto (pagina de bloqueio, JS, varredura)
            elif candidatos and all(f == "SEM_TEXTO" for _, f, _ in candidatos):
                veredito = "NAO_MEDIDO"
                motivo = "fonte custodiada sem camada de texto utilizavel (bloqueio/JS): nao mede"
            # fonte citada mas arquivo ausente
            elif all(f is None for _, f, _ in candidatos):
                veredito, motivo = "NAO_MEDIDO", "arquivo da fonte citada ausente na gaveta"
            elif veredito is None:
                achou = [(c, f, p) for c, f, p in candidatos if p]
                if achou:
                    c, f, pgs = achou[0]
                    fonte_usada, pagina = c, pgs[0]
                    limpo = re.sub(r"[*_`]", "", a["contexto"])
                    limpo = re.sub(r"\s+", " ", limpo).strip()
                    linha = f"{limpo} (fonte, p. {pagina})"
                    r = mod.conferir(linha, f, ficha_id=f"claim-{i}")
                    itens = r.get("itens") or r.get("achados") or []
                    est = (itens[0].get("estado") if itens else r.get("estado")) or ""
                    veredito = ("CONFERE" if est == "APROVADO" or est == "APROVADO_SEM_UNIDADE"
                                else "DIVERGENTE" if est == "DIVERGENTE"
                                else "AUSENTE_NA_PAGINA" if est == "AUSENTE"
                                else "NAO_MEDIDO")
                    if est == "SEM_NUMERO":
                        u = a["unidade"] or "(sem unidade)"
                        motivo = (f"unidade '{u}' fora do vocabulario do instrumento "
                                  f"(105 unidades: g, kg, m3, %; nenhuma de dose ou concentracao)")
                    elif est == "NAO_VERIFICAVEL":
                        motivo = "instrumento devolveu NAO_VERIFICAVEL nesta afirmacao"
                    else:
                        motivo = f"estado do gate: {est}"
                else:
                    c, f, _ = [(c, f, p) for c, f, p in candidatos if f][0]
                    fonte_usada = c
                    veredito = "AUSENTE_NA_PAGINA"
                    motivo = "valor nao localizado em nenhuma pagina da fonte citada"
        sujeito_ok = None
        if veredito == "CONFERE":
            sujeito_ok = _sujeito_confere(cache, mod, a, fonte_usada, pagina)
        aux = "LOCALIZADO" if pagina else ("SEM_BUSCA" if veredito == "NAO_MEDIDO" and not fonte_usada else "NAO_LOCALIZADO")
        registro.append(dict(id=i, paragrafo=a["paragrafo"], sujeito_confere=sujeito_ok, aux=aux, secao=a["secao"], valor=a["valor"], unidade=a["unidade"],
                             sujeito=a["sujeito"], contexto=a["contexto"],
                             citacoes=a["citacoes"], fonte=fonte_usada, pagina=pagina,
                             veredito=veredito, motivo=motivo, tabela=a["tabela"]))

    with open(os.path.join(AQUI, "registro.jsonl"), "w", encoding="utf-8") as f:
        for r in registro:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    # ---- registro por PARAGRAFO: nenhum paragrafo sem veredito ----
    paragrafos_reg = {}
    for r_ in registro:
        k = r_["paragrafo"]
        d_ = paragrafos_reg.setdefault(k, dict(secao=r_["secao"], total=0, confere=0,
                                               nao_medido=0, ausente=0))
        d_["total"] += 1
        d_.setdefault("com_estatuto", 0)
        if r_["veredito"] in ("TABELA_COM_NOTA", "DERIVACAO_DECLARADA", "RESUMO_DE_FONTE_NOMEADA"):
            d_["com_estatuto"] += 1
        if r_["veredito"] == "CONFERE":
            d_["confere"] += 1
        elif r_["veredito"] == "AUSENTE_NA_PAGINA":
            d_["ausente"] += 1
        else:
            d_["nao_medido"] += 1
    for d_ in paragrafos_reg.values():
        if d_["total"] == 0:
            continue
        if d_["confere"] == d_["total"]:
            d_["veredito"] = "CONFERIDO"
        elif d_["confere"] + d_["com_estatuto"] == d_["total"]:
            d_["veredito"] = "ESTATUTO_DECLARADO"
        elif d_["confere"] == 0:
            d_["veredito"] = "NAO_CONFERIDO" if d_["ausente"] == 0 else "DIVERGENTE"
        else:
            d_["veredito"] = "PARCIAL"
    from collections import Counter
    cont = Counter(r["veredito"] for r in registro)
    # paragrafos de prosa SEM nenhuma afirmacao numerica tambem recebem veredito
    todos = [b for b in paragrafos(corpo)]
    sem_num = 0
    SEM_NUM_GLOBAL[0] = 0
    for b in todos:
        txt = "\n".join(re.sub(r"^\s*>\s?", "", l) for l in b).strip()
        if not txt or RE_SECAO.match(txt):
            continue
        if txt[:60] not in paragrafos_reg:
            sem_num += 1
            paragrafos_reg[txt[:60]] = dict(secao="?", total=0, confere=0, nao_medido=0,
                                            ausente=0, veredito="SEM_AFIRMACAO_NUMERICA")
    SEM_NUM_GLOBAL[0] = sem_num
    with open(os.path.join(AQUI, "registro_paragrafos.json"), "w", encoding="utf-8") as f:
        json.dump(paragrafos_reg, f, ensure_ascii=False, indent=1)
    print(f"paragrafos sem afirmacao numerica: {sem_num}", file=sys.stderr)
    cp = Counter(v["veredito"] for v in paragrafos_reg.values())
    resumo = dict(M=len(registro), contagem=dict(cont),
                  paragrafos=len(paragrafos_reg), paragrafos_por_veredito=dict(cp),
                  N_conferidas=cont.get("CONFERE", 0),
                  sem_citacao=sum(1 for r in registro if not r["citacoes"]),
                  fontes_lidas=sorted({r["fonte"] for r in registro if r["fonte"]}))
    json.dump(resumo, open(os.path.join(AQUI, "resumo.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(json.dumps(resumo, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
