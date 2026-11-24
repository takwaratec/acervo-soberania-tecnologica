# -*- coding: utf-8 -*-
"""Referências bibliográficas da frente cobre — usadas pelo manuscrito .md e pela peça HTML.

Cada entrada traz: chave, autores, ano, título, veículo, e o que ela sustenta neste trabalho.
Custódia: caminho do arquivo + sha256 no MANIFEST.
"""

# (chave, autores, ano, titulo, veiculo, custodia, o_que_sustenta)
REFERENCIAS = [
    ("tonini2024",
     "TONINI, H.; OLIVEIRA, L. da S.",
     2024,
     "Tratamento da madeira na propriedade rural: procedimentos para a sua aplicação, "
     "licenciamento e gestão financeira.",
     "Comunicado Técnico 110. Embrapa Pecuária Sul, Bagé, RS. ISSN 1982-5382.",
     "fontes-documentais/ago_28_Sulfato_S11/pdf/embrapa-cot110-tratamento-madeira-propriedade-rural.pdf",
     "instrução oficial brasileira: EPI por peça, tonel de 200 L, proibição de descarte, "
     "reuso da solução excedente (L207–214), controle federal do cromo e do boro"),

    ("nmba2006",
     "NATIONAL MISSION ON BAMBOO APPLICATIONS (Índia), Department of Science and Technology",
     2006,
     "Preservation of Bamboo.",
     "Governo da Índia. 60 p.",
     "fontes-documentais/ago_28_Sulfato_S11/pdf/nmba-2006-preservation-bamboo-manual.pdf",
     "manual oficial indiano: não descartar em ralos, rios ou córregos; decantar e reusar "
     "(p. 46–47); enterro de resíduo com serragem; recomposição do lodo com ácido crômico a pH 2,5"),

    ("scharfenberg2020",
     "SCHARFENBERG, H. R.",
     2020,
     "Análise do comportamento mecânico e biológico do bambu gigante (Dendrocalamus asper) "
     "tratado com cobre e boro.",
     "Dissertação (Mestrado Profissional em Inovação Tecnológica) — Universidade Federal do "
     "Triângulo Mineiro, Uberaba. 101 p. Orientador: M. M. Shimano.",
     "fontes-documentais/ago_28_Sulfato_S11/pdf/uftm-scharfenberg-cb-cobre-boro.pdf",
     "única fonte do corpus que mede a fitotoxicidade do descarte: índice de germinação zero até "
     "diluição 1/10, comparação com glifosato, pH 1,28 (CB) e 0,22 (CCB), comprimento de radícula"),

    ("rusch2023",
     "RUSCH, F.; CANDATEN, L.; BANDERA, E.; MANGINI, T. de S.; ZANCHETTA, L. da S.; "
     "TREVISAN, R.; WASTOWSKI, A. D.",
     2023,
     "Tratamento químico, durabilidade e lixiviação de bambu tratado e submetido a ensaio em "
     "campo de apodrecimento.",
     "Pesquisa Florestal Brasileira, Colombo, v. 43, e202102187. DOI 10.4336/2023.pfb.43e202102187.",
     "fontes-documentais/ago_28_Sulfato_S11/pdf/embrapa-pfb-2023-rusch.pdf",
     "ensaio de campo de cinco anos: cobre no solo +12% sem significância estatística; cromo +86%; "
     "composição do CCB (26% sulfato de cobre, 63,5% dicromato, 10,5% ácido bórico)"),

    ("ufmg_mom",
     "MATERIALES Y MODOS DE HACER — Faculdade de Arquitetura, Universidade Federal de Minas Gerais",
     None,
     "Tratamento com bórax.",
     "Página institucional, seção 'estrutura bambu'.",
     "fontes-documentais/ago_28_Sulfato_S11/ufmg-tratamento-borax.htm",
     "receita informal publicada por universidade pública: 1 kg : 1 kg : 100 L, imersão de 8 a 10 "
     "dias, e a declaração de que o método não foi comprovado cientificamente"),

    ("blogtcs2016",
     "MATERIAIS E TÉCNICAS PARA CONSTRUÇÃO SUSTENTÁVEL (blog)",
     2016,
     "Como Tratar Bambu.",
     "Blog, 1º de fevereiro de 2016.",
     "fontes-documentais/ago_28_Sulfato_S11/blog-tecnicas-como-tratar-bambu.htm",
     "receita informal completa: fórmula 2:2:0,5 com dicromato de sódio, concentração 4,5% e "
     "instrução de dobrar para 9%; zero ocorrências de 'luvas', 'máscara', 'EPI', 'descarte', 'resíduo'"),

    ("espaconaturalmente",
     "ESPAÇO NATURALMENTE",
     None,
     "Bambu.",
     "Site comercial-educativo.",
     "fontes-documentais/ago_28_Sulfato_S11/espaconaturalmente-bambu.htm",
     "padrão de mercado: 'sulfato de cobre como fungicida'; zero ocorrências de EPI, descarte, "
     "resíduo e 'tóxico' no texto"),

    ("gauss2020",
     "GAUSS, C.",
     2020,
     "Preservação de bambu: análise comparativa de preservantes e métodos.",
     "Trabalho acadêmico. Tabela 2.5 (preservantes).",
     "fontes-academicas/2020-gauss-preservacao-bambu/extracao.md",
     "'good fungicide' / 'ineffective for termites and insects' para zinco + sulfato de cobre"),

    ("conama430",
     "BRASIL. Conselho Nacional do Meio Ambiente",
     2011,
     "Resolução CONAMA nº 430, de 13 de maio de 2011 — condições e padrões de lançamento de efluentes.",
     "Diário Oficial da União.",
     None,
     "cobre em efluente: 1,0 mg/L"),

    ("conama357",
     "BRASIL. Conselho Nacional do Meio Ambiente",
     2005,
     "Resolução CONAMA nº 357, de 17 de março de 2005 — classificação dos corpos de água.",
     "Diário Oficial da União.",
     None,
     "cobre dissolvido em água doce Classe 1: 0,009 mg/L"),

    ("oms2004",
     "WORLD HEALTH ORGANIZATION",
     2004,
     "Copper in Drinking-water: background document for development of WHO Guidelines for "
     "Drinking-water Quality.",
     "WHO/SDE/WSH/03.04/88. Genebra.",
     "fontes-normativas/who-2004-copper-drinking-water/",
     "valor provisório de 2 mg/L; LOAEL 4 mg/L (náusea, 61 voluntários); acúmulo hepático; "
     "dose diária tolerável 0,17 mg/kg/dia"),

    ("pnrs2010",
     "BRASIL",
     2010,
     "Lei nº 12.305, de 2 de agosto de 2010 — Política Nacional de Resíduos Sólidos.",
     "Diário Oficial da União.",
     "fontes_novas/pnrs_art3_XVI.txt",
     "art. 3º, XVI: resíduo sólido inclui líquidos cuja destinação em rede de esgoto ou corpo "
     "d'água seja inviável"),

    ("comexstat",
     "BRASIL. Ministério do Desenvolvimento, Indústria, Comércio e Serviços — ComexStat",
     None,
     "Exportação e importação — NCM 2833.25 (sulfato de cobre), série 1997–2026.",
     "Base de dados oficial de comércio exterior.",
     "governanca-operacional/extracoes/cobre/serie_sulfato/",
     "177,854 t e US$ 370.053 em 2025; China 80,4% do peso e 48,3% do valor; dispersão de preço de "
     "119×; queda de 86% entre 1997 e 2020"),

    ("nbr6232",
     "ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS",
     2013,
     "NBR 6232 — Penetração e retenção de preservativos em madeira tratada sob pressão.",
     "ABNT, Rio de Janeiro.",
     None,
     "retenção de 6,5 kg/m³ e composição percentual do CCB, conforme descrita em Rusch et al. (2023)"),
]

# chave -> número na lista de referências
NUMERO = {r[0]: i + 1 for i, r in enumerate(REFERENCIAS)}


def citar(*chaves):
    """Devolve a marcação de citação para as chaves dadas: (1), (1,3), etc."""
    nums = sorted(NUMERO[k] for k in chaves)
    return "(" + ", ".join(str(n) for n in nums) + ")"


def _fecha_ponto(s):
    """Um ponto final, nunca dois: 'S.' + '.' não vira 'S..'."""
    s = s.rstrip()
    return s if s.endswith(".") else s + "."


def lista_abnt():
    """Lista numerada no padrão ABNT, em Markdown. Um ponto só, nunca '..'."""
    linhas = []
    for i, (chave, aut, ano, tit, veic, cust, sust) in enumerate(REFERENCIAS, 1):
        a = (_fecha_ponto(aut) + " ") if aut else ""
        an = (_fecha_ponto(str(ano)) + " ") if ano else "[s.d.]. "
        tit = _fecha_ponto(tit)
        veic = _fecha_ponto(veic)
        linhas.append(f"{i}. {a}**{tit}** {an}{veic}")
    return "\n".join(linhas)


def json_manifesto():
    return [
        {"n": i, "chave": c, "autores": a, "ano": an, "titulo": t, "veiculo": v,
         "custodia": cu, "sustenta": s}
        for i, (c, a, an, t, v, cu, s) in enumerate(REFERENCIAS, 1)
    ]
