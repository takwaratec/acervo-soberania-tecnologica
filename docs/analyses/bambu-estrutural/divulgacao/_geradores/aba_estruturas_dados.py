#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aba 13 — Estruturas: o que o corpus tem e o que ele não tem.

Duas partes:
  1. o que EXISTE: elementos ensaiados e a intenção estrutural declarada por cada fonte;
  2. o que NÃO existe: varredura de termos estruturais nos 10 PDFs, documentada.
"""
import os
import re

CORPUS = "/Users/fabiotakwara/.hermes/cache/scratch/bamboo_corpus_r1"

# Quais documentos foram varridos (10 com texto extraído; 2 são duplicatas de lorenzo)
ARQUIVOS = [
    ("drury2023", "Drury 2023 · Reino Unido/Canadá"),
    ("springer2026_moso_guadua_dic", "Franck 2026 · Alemanha"),
    ("sust2024_philippines_comp", "Panti 2024 · Filipinas"),
    ("lorenzo2020_jwood", "Lorenzo 2020 · Reino Unido"),
    ("forests2024_flexural_br", "Scharfenberg 2024 · Brasil"),
    ("rodriguez2023_ucayali", "Rodríguez-Sotelo 2023 · Peru"),
    ("do_acervo/c12_villavicencio2025", "Rincon & Choque 2025 · Colômbia"),
    ("rocha2024_chacoensis", "Rocha & Kikuti 2024 · Brasil"),
    ("poblete2009_chusquea", "Poblete 2009 · Chile"),
    ("guiotoku2024", "Guiotoku 2024 · Brasil"),
]

# Termos e o que cada família procura
FAMILIAS = [
    ("Tesoura / treliça", ["tesoura", "treli", "truss", "lattice", "space frame", "reticulad"]),
    ("Viga", ["viga", "beam", "joist", "girder"]),
    ("Coluna / pilar", ["pilar", "column"]),
    ("Pórtico / quadro", ["pórtico", "portico", "frame"]),
    ("Ligação / conexão", ["ligação", "conexão", "joint", "connection"]),
]

# Falsos positivos a excluir: 'coluna'/'column' de tabela, 'frame' de 'framework'
FALSOS = [
    (r"colunas? d[ae] tabela", "coluna de tabela"),
    (r"colun[ao]s? (\d|do|da|de)", "coluna de tabela"),
    (r"columna", "coluna de tabela (es)"),
    (r"columns? (?:of|in) (?:the )?table", "coluna de tabela"),
    (r"framework|agreement|amsterdam|program", "'frame' em outra palavra"),
    (r"connection between factors|connections between", "conexão lógica, não estrutural"),
    (r"joint research|joint publication|joint venture", "'joint' de parceria"),
    (r"laminate joints in non-structural", "referência bibliográfica"),
    (r"jointly|joint authors", "advérbio"),
    (r"joint line|line joints?|single joint|double line", "junção de nó do colmo (morfologia)"),
    (r"single-column (instron|load)|universal frame|testing (machine|frame)", "equipamento de ensaio"),
]


def varrer():
    """Conta ocorrências reais por família e por documento."""
    res = {}
    for chave, rotulo in ARQUIVOS:
        caminho = os.path.join(CORPUS, chave + "_text.txt")
        if not os.path.exists(caminho):
            continue
        texto = open(caminho, encoding="utf-8", errors="ignore").read()
        baixo = texto.lower()
        linha = {}
        for fam, termos in FAMILIAS:
            total = 0
            for t in termos:
                for m in re.finditer(re.escape(t), baixo):
                    ctx = baixo[max(0, m.start() - 80): m.start() + 40]
                    if any(re.search(p, ctx) for p, _ in FALSOS):
                        continue
                    total += 1
            if total:
                linha[fam] = total
        res[rotulo] = linha
    return res


# Elementos estruturais: o que a fonte declara
ELEMENTOS = [
    {
        "elemento": "Coluna (colmo inteiro)",
        "especie": "Moso, Guadua, Tali, Black Java, Madake",
        "fonte": "Drury et al. 2023 — Reino Unido / Canadá",
        "local": "Ensaio no Reino Unido; material da Colômbia, China e Indonésia",
        "resultado": "Compressão paralela de 54,62 a 88,90 MPa. O artigo declara o objetivo como "
                     "avaliar as espécies “as structural columns in modern buildings”.",
        "forca": "Ensaio em colmo inteiro, com a norma ISO 22157. É o dado mais próximo de "
                 "dimensionamento de pilar no corpus.",
        "limite": "Corpo de prova de comprimento fixo, sem esbeltez variável: não há flambagem "
                  "medida, só ruptura por compressão.",
    },
    {
        "elemento": "Viga / elemento fletido (colmo inteiro)",
        "especie": "Moso e Guadua angustifolia",
        "fonte": "Franck et al. 2026 — Alemanha",
        "local": "Ensaio na Alemanha; Moso da China, Guadua da Colômbia",
        "resultado": "Flexão em quatro pontos, vão de 2.600 mm. Moso rompeu a 76,97 MPa com flecha "
                     "de 172,8 mm (vão/15); Guadua, 56,23 MPa com 57,8 mm (vão/45).",
        "forca": "É o único do corpus que mede flecha em vão real de viga, com correção de "
                 "acomodação do apoio.",
        "limite": "Cinco corpos por espécie, vão único. Não há viga de seção composta nem "
                  "ligação de extremidade ensaiada.",
    },
    {
        "elemento": "Viga de lâminas (laminação colada)",
        "especie": "B. tuldoides, D. asper, P. aurea",
        "fonte": "Scharfenberg et al. 2024 — Brasil (Uberaba, MG)",
        "local": "Unesp Botucatu / UFTM Uberaba",
        "resultado": "Flexão de 3 pontos em lâmina de 10 cm × 1 cm. Melhor configuração: P. aurea "
                     "com nó e superfície externa tracionada, 367,13 MPa de tensão última.",
        "forca": "Único ensaio do corpus que isola a face do colmo (externa x interna) e o nó como "
                 "variáveis de projeto de viga laminada.",
        "limite": "Corpos pequenos de 1 cm: não é viga estrutural, e o valor não é comparável a "
                  "colmo inteiro. As três espécies são asiáticas — ver restrição de uso na ficha.",
    },
    {
        "elemento": "Treliça / contraventamento — apenas citado",
        "especie": "Moso e Guadua",
        "fonte": "Franck et al. 2026 — Alemanha",
        "local": "Alemanha",
        "resultado": "O artigo afirma que “a chave para boas ligações em elementos portantes, "
                     "por exemplo tesouras (truss girders), é conhecer o material e saber trabalhá-lo”, "
                     "e que muitas ligações tradicionais perdem a resistência inicial do colmo.",
        "forca": "Declara o problema de engenharia real: a ligação governa o desempenho da treliça, "
                 "não o colmo.",
        "limite": "É contexto de introdução, não ensaio. Nenhuma tesoura foi ensaiada neste corpus.",
    },
    {
        "elemento": "Ligação / conexão — nenhum ensaio",
        "especie": "—",
        "fonte": "—",
        "local": "—",
        "resultado": "Nenhum dos dez documentos ensaia ligação de bambu. Franck 2026 discute a "
                     "dificuldade, e Panti 2024 registra que os vãos de amostragem são limitados, "
                     "mas nenhum mede resistência de ligação.",
        "forca": "—",
        "limite": "É a lacuna mais grave para uso estrutural: viga, coluna e treliça são governadas "
                  "pela ligação, e a ligação não está no corpus.",
    },
]
