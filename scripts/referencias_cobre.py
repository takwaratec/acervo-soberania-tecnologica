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

    ("in592",
     "INSTITUTO BRASILEIRO DO MEIO AMBIENTE E DOS RECURSOS NATURAIS RENOVÁVEIS",
     1992,
     "Instrução Normativa nº 5, de 20 de outubro de 1992 — disciplina os procedimentos da "
     "Portaria Interministerial 292/89.",
     "Diário Oficial da União, 21 out. 1992.",
     "fontes/s11d/1992_in05_ibama_destinacao_final_residuos.pdf",
     "item VIII, «Da destinação final de resíduos e embalagens»: o descarte deve atender às "
     "recomendações da bula; item VI «h»: a bula deve informar o destino final dos resíduos"),

    ("comexstat",
     "BRASIL. Ministério do Desenvolvimento, Indústria, Comércio e Serviços — ComexStat",
     None,
     "Exportação e importação — NCM 2833.25 (sulfato de cobre), série 1997–2026.",
     "Base de dados oficial de comércio exterior.",
     "governanca-operacional/extracoes/cobre/serie_sulfato/",
     "177,854 t e US$ 370.053 em 2025; China 80,4% do peso e 48,3% do valor; dispersão de preço de "
     "119×; queda de 86% entre 1997 e 2020"),

    ("araujo2025",
     "ARAUJO, Letícia Medeiros de; GIANELLI, Bruno Fernando; MANCINI, Sandro Donnini; "
     "MEDEIROS, Gerson Araujo de",
     2025,
     "Life cycle assessment of the artisanal bamboo pole (Guadua angustifolia) production "
     "in the Brazilian Amazon.",
     "Brazilian Journal of Science, v. 4, n. 4, p. 13-28. DOI 10.14295/bjs.v4i4.719.",
     None,
     "a única medição brasileira do impacto de uma cadeia artesanal de bambu tratado: "
     "toxicidade carcinogênica humana = 93% do impacto normalizado, 91% dele nos resíduos "
     "de apara, corte e colmo descartado, atribuídos ao ácido bórico e ao bórax. Uma "
     "unidade, um município, um ano (Rio Branco, Acre)."),

    ("pnmcb2011",
     "BRASIL",
     2011,
     "Lei nº 12.484, de 8 de setembro de 2011 — Política Nacional de Incentivo ao Manejo "
     "Sustentado e ao Cultivo do Bambu.",
     "Diário Oficial da União.",
     None,
     "a política do bambu: crédito rural, assistência técnica e certificação de origem — e "
     "nenhuma palavra sobre tratamento químico, resíduo, licença ou fiscalização."),

    ("nbr6232",
     "ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS",
     2013,
     "NBR 6232 — Penetração e retenção de preservativos em madeira tratada sob pressão.",
     "ABNT, Rio de Janeiro.",
     None,
     "retenção de 6,5 kg/m³ e composição percentual do CCB, conforme descrita em Rusch et al. (2023)"),

    # ---- S11-c: a norma da madeira tratada e o descarte (2026-11-24) -------------
    ("pi292",
     "BRASIL. Ministério da Fazenda; Ministério da Saúde; Ministério do Interior",
     1989,
     "Portaria Interministerial nº 292, de 28 de abril de 1989 — registro de preservativos "
     "de madeira e das usinas de preservação.",
     "Diário Oficial da União, Brasília. 4 p.",
     "fontes-documentais/ago_28_Madeira_Tratada_S11c/1989_pi292_preservativos_registro.pdf",
     "a norma-mãe: registro obrigatório no Ibama (art. 1º e 3º), relatório semestral (art. 2º) "
     "e a competência de fiscalização nomeada (art. 20) — e o silêncio sobre o resíduo"),

    ("pn151",
     "INSTITUTO BRASILEIRO DO MEIO AMBIENTE E DOS RECURSOS NATURAIS RENOVÁVEIS",
     1997,
     "Portaria Normativa nº 151, de 24 de novembro de 1997 — documentação para registro de "
     "produto preservativo de madeira.",
     "Diário Oficial da União, Seção 1, p. 27.552, 25 nov. 1997. OCR degradado.",
     "fontes-documentais/ago_28_Madeira_Tratada_S11c/1997_pn151_ibama_registro_risco_ambiental.pdf",
     "o registro depende de risco ambiental determinado: o risco avaliado é o do produto em uso, "
     "não o do resíduo ao fim da vida útil"),

    ("iema2023",
     "INSTITUTO ESTADUAL DE MEIO AMBIENTE E RECURSOS HÍDRICOS DO ESPÍRITO SANTO",
     2023,
     "Nota Técnica Orientativa GGE-COED nº 01/2023 — principais aspectos acerca dos estudos e "
     "das análises referentes ao licenciamento ambiental da atividade de preservação de madeira.",
     "Iema-ES, Vitória. 36 p.",
     "fontes-documentais/ago_28_Madeira_Tratada_S11c/2023_iema_es_nt01_preservacao_madeira.pdf",
     "o regulador por dentro: CCA em 80% do volume, sete registros válidos, «não há proibição "
     "de uso no Brasil», EPA retirou o uso residencial em 2003, e «não existem muitas "
     "informações sobre o CCB... e à disposição de resíduos»"),

    ("abpm2015",
     "ASSOCIAÇÃO BRASILEIRA DA INDÚSTRIA DE MADEIRA PROCESSADA MECANICAMENTE (ABPM)",
     2015,
     "Destinação de resíduos de madeira tratada.",
     "Apresentação no 3º Simpósio Madeira e Construção, ago. 2015. 21 p.",
     "fontes-documentais/ago_28_Madeira_Tratada_S11c/2016_abpm_fg4mad_destinacao_residuos_madeira_tratada.pdf",
     "a própria cadeia produtiva: resíduo tratado não pode ter contato com alimentos ou água "
     "potável, nem queima a céu aberto ou em fogões, churrasqueiras, fornos e caldeiras"),

    ("ufsm2025",
     "CIÊNCIA FLORESTAL",
     2025,
     "Contaminação do solo pelo uso de moirões tratados com arseniato de cobre cromatado.",
     "Ciência Florestal, Santa Maria, v. 35, e86024, p. 1-16. DOI 10.5902/1980509886024.",
     "fontes-documentais/ago_28_Madeira_Tratada_S11c/2025_ufsm_ciencia_florestal_cca_moiroes_solo.pdf",
     "880 dias de campo: arsênio da madeira −55,0%, arsênio do solo +129,2%, e 32,3% acima do "
     "valor máximo de investigação agrícola da Resolução CONAMA 420/2009"),
]

# referências cujo texto-fonte será publicado no repositório pela gaveta do boro (PR-114).
# A citação já vale; o link para o arquivo custodiado entra quando a PR for mesclada.
LINK_PENDENTE = {
    "araujo2025": "PR-114 (hermes/boro-v8-fim-de-vida) — ficha em docs/analyses/boro/fichas/araujo-2025-acv-bambu-acre-93-hct.md",
    "pnmcb2011": "PNMCB — texto integral no Planalto; publicação desta frente pendente",
}

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
