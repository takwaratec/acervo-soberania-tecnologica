#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Conteúdo da aba 06 — Espécies, norma por norma.

Cada bloco traz: ficha da espécie, o número medido, a equivalência didática
(derivada em derivar_numeros.py), a norma que o ensaio usou e o uso que a
FONTE indica — nunca uso inventado pelo agente.
"""

ORDEM = ["Madake", "Moso", "Guadua", "Tali", "BlackJava"]

NOMES = {
    "Madake": "Phyllostachys bambusoides",
    "Moso": "Phyllostachys edulis",
    "Guadua": "Guadua angustifolia",
    "Tali": "Gigantochloa apus",
    "BlackJava": "Gigantochloa atroviolacea",
}

# Drury et al. 2023 — ISO 22157:2019, compressão paralela, colmo inteiro, n=6
DRURY_ESPECIE = {
    "Madake": {
        "origem": "China, Japão",
        "diametro": "colmo estreito, Ø ≈ 45 mm",
        "area": "739 mm² de parede",
        "conclusao_fonte": (
            "A maior tensão média do estudo, e o artigo explica por quê: colmo de diâmetro "
            "menor concentra mais fibra por unidade de área. É o caso em que a tensão é alta "
            "e a carga total é baixa."
        ),
    },
    "Moso": {
        "origem": "China",
        "diametro": "colmo largo, Ø ≈ 80 mm",
        "area": "1.605 mm² de parede",
        "conclusao_fonte": (
            "Segunda maior tensão e a maior carga média de uma série junto com Tali e Guadua "
            "(112,1 kN). O artigo registra que o nó aumentou a resistência à compressão em "
            "Moso e Madake."
        ),
    },
    "Guadua": {
        "origem": "Colômbia, Equador, Venezuela",
        "diametro": "colmo largo, Ø ≈ 80 mm",
        "area": "1.728 mm² de parede",
        "conclusao_fonte": (
            "O artigo destaca a Guadua por consistência, não por resistência: coeficiente de "
            "variação de 5,53% na tensão e 7,92% no módulo, o mais baixo do ensaio, com curvas "
            "tensão–deformação muito semelhantes entre corpos de prova. Menor dispersão é o "
            "que permite adotar valor característico alto."
        ),
    },
    "Tali": {
        "origem": "Java, Indonésia",
        "diametro": "colmo largo, Ø ≈ 80 mm",
        "area": "1.939 mm² de parede",
        "conclusao_fonte": (
            "Registrou a maior carga absoluta do estudo (152,4 kN, corpo TI3) com tensão média "
            "moderada — o caso mais claro de que carga total e tensão são grandezas diferentes."
        ),
    },
    "BlackJava": {
        "origem": "Java, Indonésia",
        "diametro": "colmo médio, Ø ≈ 76 mm",
        "area": "1.511 mm² de parede",
        "conclusao_fonte": (
            "A menor tensão média das cinco. O artigo registra que, nesta espécie, o internó "
            "resistiu mais que o nó."
        ),
    },
}

# Panti et al. 2024 — ISO 22157-1:2017, valor característico por ISO 12122-1:2014
PANTI_ESPECIE = {
    "B. blumeana": {
        "nome": "Bambusa blumeana",
        "origem": "Sudeste Asiático",
        "n": "93 corpos de prova",
        "uso_fonte": (
            "O artigo calcula o valor característico para fundamentar a norma filipina "
            "(NSCP) e compara os quatro bambus com madeiras estruturais não secas das "
            "Filipinas: todos os bambus ficaram acima das madeiras. Não há recomendação de "
            "uso por espécie — o objetivo declarado é normativo."
        ),
    },
    "B. vulgaris": {
        "nome": "Bambusa vulgaris",
        "origem": "Sul da Ásia (cultivada em toda a faixa tropical)",
        "n": "36 corpos de prova",
        "uso_fonte": "Mesma finalidade: estabelecer valor característico para a norma filipina.",
    },
    "D. asper": {
        "nome": "Dendrocalamus asper",
        "origem": "Bangladesh a Taiwan e Malesia",
        "n": "36 corpos de prova",
        "uso_fonte": "Mesma finalidade: estabelecer valor característico para a norma filipina.",
    },
    "G. angustifolia": {
        "nome": "Guadua angustifolia",
        "origem": "Noroeste da América do Sul",
        "n": "30 corpos de prova",
        "uso_fonte": (
            "Mesma finalidade. O artigo não trata a Guadua como nativa — ela entra como uma "
            "das quatro espécies disponíveis nas Filipinas."
        ),
    },
}

# Lorenzo et al. 2020 — JG/T 199-2007 e característico por BS EN 1990 Anexo D
LORENZO_ESPECIE = {
    "Moso": {"nome": "Phyllostachys edulis"},
    "Guadua": {"nome": "Guadua angustifolia"},
    "Oldhamii": {"nome": "Dendrocalamus oldhamii"},
}

# Uso indicado — extraído do que a FONTE declara
USO_FONTE = {
    "drury": (
        "Drury et al. não recomendam uso por espécie. A conclusão é sobre "
        "comportamento à compressão e sobre a necessidade de avaliar confiabilidade do "
        "material em estudos futuros. O artigo situa o contexto: andaimes de bambu ainda "
        "são preferidos no sul da China e em Hong Kong, e o bambu é alternativa à madeira "
        "no sul da Ásia, Índia e América Latina."
    ),
    "franck": (
        "Franck et al. apresentam a comparação como subsídio à substituição de materiais "
        "intensivos em energia na construção. Não emitem recomendação de uso por espécie."
    ),
    "panti": (
        "Panti et al. têm objetivo normativo declarado: contribuir para a norma estrutural "
        "filipina (NSCP). Os quatro bambus superaram madeiras estruturais filipinas não secas."
    ),
    "lorenzo": (
        "Lorenzo et al. medem propriedades para fabricação robótica de elementos. Não "
        "recomendam uso por espécie."
    ),
    "rincon": (
        "Rincon & Choque verificam se a Guadua de Villavicencio atende aos requisitos "
        "mínimos da NSR-10 colombiana, para uso habitacional. O artigo não declara aptidão "
        "para uso estrutural — conclui que as diferenças entre sítios existem e que é "
        "preciso padronizar protocolo para poder comparar."
    ),
    "rodriguez": (
        "Rodríguez-Sotelo et al. concluem que G. lynnclarkiae e G. weberbaueri têm "
        "propriedades adequadas a diferentes usos, incluindo construção civil, e que para "
        "G. superba se recomenda estudo posterior de rigidez e resistência antes do uso em "
        "habitação. Classificam a compressão paralela pela escala de Spavento & Keil (2008) "
        "para madeiras: as três ficam entre 'baixo' e 'médio', com G. weberbaueri no nível médio."
    ),
    "rocha": (
        "Rocha & Kikuti concluem que os resultados permitem avaliar a viabilidade de usar "
        "G. chacoensis na construção civil, e observam que a resistência à compressão ficou "
        "abaixo da literatura citada, enquanto a tração ficou próxima."
    ),
    "scharfenberg": (
        "O artigo declara que as três espécies foram selecionadas por disponibilidade local "
        "e aplicabilidade construtiva em partes estruturais para habitação. ATENÇÃO: o artigo "
        "descreve as três como nativas do Brasil, o que diverge do Kew POWO — ver a "
        "restrição de uso nesta mesma peça."
    ),
    "poblete": (
        "Poblete et al. concluem que as propriedades do colihue o situam no limite inferior "
        "das madeiras comerciais, similares ao álamo, e indicam uso como matéria-prima para "
        "painéis decorativos, artesanato e algumas partes de móveis. Recomendam investigar "
        "painéis particulados, painéis de fibra e papel."
    ),
    "guiotoku": (
        "Guiotoku et al. não fazem ensaio mecânico nem recomendam uso construtivo. O estudo "
        "é físico-químico e o contexto é ecológico: M. skvortzovii e C. meyeriana são "
        "invasoras dominantes, A. simplex é ameaçada e C. cf. gracilis é rara."
    ),
}

NORMAS = [
    ("ISO 22157:2019", "Determinação de propriedades físicas e mecânicas do bambu. Usada por Drury 2023 e Franck 2026.",
     "Corpo de prova é o colmo inteiro; resultado é tensão última e módulo medidos no colmo real."),
    ("ISO 22157-1:2017 + ISO 12122-1:2014", "Ensaio e cálculo de valor característico (percentil 5 com 75% de confiança). Usadas por Panti 2024.",
     "Transforma média em valor de projeto: é o que a norma exige para dimensionar."),
    ("NTC 5525 (Colômbia)", "Norma técnica colombiana para Guadua. Usada por Rincon 2025 e Rodríguez-Sotelo 2023.",
     "Base do cálculo de esforço admissível na NSR-10."),
    ("NSR-10, cap. G.12 (Colômbia)", "Regulamento de construção sismo-resistente, capítulo da Guadua.",
     "Define os fatores de redução que transformam valor característico em admissível."),
    ("NTP 251 (Peru)", "Normas técnicas peruanas de madeira adaptadas para bambu. Usadas por Rodríguez-Sotelo 2023.",
     "Compressão perpendicular e procedimentos de acondicionamento."),
    ("ABNT NBR 16828 (Brasil)", "Norma brasileira de estruturas de bambu. Usada por Rocha & Kikuti 2024.",
     "É a norma que a lacuna L21 exige como campanha — e a única do corpus aplicada a uma nativa brasileira."),
    ("JG/T 199-2007 (China) + BS EN 1990 Anexo D", "Ensaio chinês e método europeu de valor característico. Usados por Lorenzo 2020.",
     "Valor característico calculado por fractil, não por percentil simples."),
    ("ASTM D143", "Corpos de prova pequenos de madeira. Usada por Scharfenberg 2024 para preparar lâminas.",
     "Ensaio em lâmina, não em colmo: os valores não são comparáveis aos de colmo inteiro."),
    ("DIN 52 185/52 186 (Alemanha)", "Compressão paralela e flexão em madeira. Usadas por Poblete 2009.",
     "Norma de madeira, não de bambu — o colihue foi ensaiado como madeira."),
]

CUIDADOS = [
    ("Tensão não é carga",
     "88,90 MPa do Madake é a maior tensão, mas o colmo Ø45 suporta 6,7 tf. A Guadua, com "
     "60,73 MPa, suporta 10,7 tf num colmo Ø80. Tensão é força dividida por área; colmo mais "
     "grosso tem mais área. Comparar só a tensão premia o colmo fino."),
    ("Média não é valor de projeto",
     "Dois estudos, duas cadeias — misturá-las produz um número que não existe. Nas Filipinas (Panti 2024), "
     "a Guadua tem média de 57,5 MPa e característico de 37,0 MPa: redução de 1,56 vez, antes do fator de "
     "segurança. Em Villavicencio (Rincon 2025), a média é de 100 MPa e o admissível pela NSR-10 fica em "
     "17,8 MPa: redução de 5,6 vezes. O característico de um estudo não se divide pelo admissível de outro — "
     "a razão entre eles não significa nada. Em qualquer dos dois casos, citar a média como capacidade de "
     "projeto exagera a carga admissível."),
    ("A norma muda o número",
     "Moso aparece com 69,88 MPa (ISO 22157, colmo inteiro), 66,72 MPa (Franck, colmo inteiro "
     "com DIC) e 54 MPa de média / 40 MPa característico (JG/T 199, corpo pequeno). Guadua: "
     "60,73 / 66,35 / 58 e 38. Nenhum desses números está errado — cada um responde a uma "
     "pergunta diferente."),
    ("MPa é força por área",
     "1 MPa = 1 N/mm² = 10,2 kgf/cm². 200 MPa equivale a 2,04 tf/cm² — o peso de um carro "
     "popular concentrado em um selo postal. Nenhuma dessas tensões é 'peso de caminhão': "
     "90 MPa é 0,91 tf/cm², bem mais modesto que a intuição sugere."),
]
