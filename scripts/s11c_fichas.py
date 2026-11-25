#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as cinco fichas da custódia S11-c (a norma da madeira tratada e o descarte)."""
import hashlib
import json
import os

RAIZ = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica"
FONTES = f"{RAIZ}/_privado/fontes-documentais/ago_28_Madeira_Tratada_S11c"
DEST = f"{RAIZ}/_privado/fichas/ago_28_Madeira_Tratada_S11c"

MAN = {e["chave"]: e for e in json.load(open(f"{FONTES}/MANIFEST_S11C.json", encoding="utf-8"))["entradas"]}

CABECALHO = """---
schema: ACERVO_FICHA_R1
gaveta: cobre
frente: COBRE
estado_documental: homologado-internamente
homologacao:
  tipo: INTERNA
  autoridade: FABIO
  data: 2026-11-24
  instrumento: "instrução direta do soberano no tópico da frente COBRE"
  transcricao: >
    "Sim, você vai colocar como homologação interna. Internamente nós estamos homologando.
    Se o auditor externo disser que não, nós alteramos o status."
  alcance: >
    Homologação INTERNA: vale dentro do acervo e autoriza a publicação. NÃO é homologação
    científica por par, NÃO é homologação regulatória e NÃO substitui a auditoria externa.
    O estado reverte para ficha-em-revisao se o auditor externo apontar furo material.
  auditoria_externa: PENDENTE
homologacao_automatica: false
fonte:
  arquivo: {arquivo}
  sha256: {sha}
  paginas: {paginas}
  fonte_url: {url}
  custodia: _privado/fontes-documentais/ago_28_Madeira_Tratada_S11c/
publicacao: docs/analyses/cobre/fichas/
---

> **Estado: homologada internamente (2026-11-24, autoridade FABIO).** Publicada para
> auditoria externa. Se o auditor externo apontar furo material, o estado reverte para
> `ficha-em-revisao` e a correção é publicada com a rodada seguinte.

"""

DECL_IA = """
---

## Declaração de uso de IA

**Apoio de IA.** Esta ficha foi produzida com apoio de IA (Hermes Agent), que localizou o
documento, preservou os bytes do original, extraiu o texto com marcador de página, conferiu
cada citação contra o extrato por busca literal, executou os cálculos e estruturou a
redação. A seleção interpretativa, a perspectiva e a responsabilidade pela versão publicada
permanecem com o autor.
"""

FICHAS = {}

FICHAS["ficha-pi292-89-registro-preservativos-madeira"] = dict(
    chave="pi292_1989",
    titulo="Portaria Interministerial 292/89 — a norma que registra o preservativo e nomeia quem fiscaliza",
    frase="""A norma-mãe do setor no Brasil. Não é instrução de tratamento: é o instrumento que
obriga o preservativo a ser registrado no Ibama antes de existir no mercado, e que atribui ao
Ibama, por escrito, a competência de fiscalizar.""",
    corpo="""
## 1. O que o documento é

Portaria Interministerial assinada por três ministérios — **Fazenda, Saúde e Interior** — em
28 de abril de 1989. Não é norma técnica de tratamento: é norma de **controle administrativo**
do setor de preservação de madeiras. Estabelece o registro obrigatório de empresas, produtos
e usinas, a periodicidade dos relatórios e a competência de fiscalização.

**Recorte:** madeira (moirões, postes, dormentes), não bambu. Vale para esta gaveta porque é
o instrumento que a literatura e os órgãos ambientais citam como base legal do setor — e
porque responde, com artigo e parágrafo, a pergunta "quem fiscaliza".

---

## 2. O que ela estabelece — artigo por artigo

### 2.1 Registro obrigatório da empresa

> "Art. 1º. As empresas que se dediquem à indústria e comércio de preservativos e preservação
> de madeiras são obrigadas ao registro junto ao Instituto Brasileiro do Meio Ambiente e dos
> Recursos Naturais Renováveis - IBAMA." (p. 1)

### 2.2 Relatório semestral de produção

> "Art. 2º. As indústrias de preservativos de madeira deverão apresentar relatórios semestrais
> ao IBAMA, contendo a produção mensal de cada produto." (p. 1)

### 2.3 O produto não existe legalmente antes do registro

> "Art. 3º. Os preservativos para madeiras e seus ingredientes ativos só poderão ser
> fabricados, consumidos ou postos à venda depois de registrados no IBAMA, inclusive os
> importados." (p. 1)

Aqui está o ponto que interessa à gaveta: **"consumidos"** está na lista. Não é só fabricar e
vender — é consumir. Um preservativo não registrado não pode nem ser usado.

### 2.4 A competência de fiscalização — nomeada, não inferida

> "Art. 20. O IBAMA fiscalizará as atividades relacionadas com a preservação e comércio
> dos preservativos para madeira e de madeira preservada." (p. 4)

> "Art. 21. Ao IBAMA caberá o direito de implementar medidas visando assegurar a correta
> utilização a que se destina o preservativo para madeiras." (p. 4)

O art. 21 é mais forte do que parece: não dá ao Ibama apenas o poder de autuar, dá o de
**implementar medidas para assegurar a correta utilização**. É competência positiva.

### 2.5 A infração tem consequência civil e penal

> "Art. 22. Sem prejuízo da responsabilidade civil e penal cabíveis, a infração às disposições
> da presente Portaria Interministerial [...]" (p. 4)

---

## 3. O que esta norma NÃO diz — e é o buraco que a peça precisa mostrar

Três ausências, todas verificadas no texto integral (4 páginas, 10.859 caracteres):

- **Não trata da destinação final do resíduo.** A palavra "resíduo" não aparece na Portaria.
  Ela controla a entrada (registro do produto) e o processo (relatório de produção), não a saída
  (a peça tratada que vira resíduo ao fim da vida útil).
- **Não trata de uso doméstico.** O que ela regula é a empresa e a usina; o destino doméstico
  da peça não está no escopo.
- **Não fixa padrão de qualidade do tratamento.** Penetração e retenção são matéria de norma
  técnica da ABNT (NBR 6232), não desta Portaria.

**Consequência para a tese da peça:** a norma brasileira existe, é federal, é de 1989 e nomeia
o fiscalizador. O que ela não faz é acompanhar a peça depois que ela sai da usina. É
exatamente aí que a cadeia artesanal — e o bambu tratado em casa — opera sem norma que a nomeie:
as obrigações gerais não a distinguem, e a norma específica registra a empresa, não o quintal.

---

## 4. Relações

- **com o certificado do Tanalith 60% CCA-C (Ibama, 2024):** é este o instrumento que o
  certificado cita como base legal, junto com a Lei 6.938/81 e a IN Ibama 5/92.
- **com a NT 01/2023 do Iema-ES:** o órgão estadual descreve o licenciamento da usina e cita
  a mesma estrutura. Ver ficha própria.
- **com a peça do cobre:** entra no capítulo do limbo como a resposta à pergunta "quem
  responde" — para a **usina**. Para o resíduo doméstico, não há resposta nesta norma.
""",
)

FICHAS["ficha-pn151-97-ibama-risco-ambiental"] = dict(
    chave="pn151_1997",
    titulo="Portaria Normativa Ibama 151/97 — o dossiê de risco ambiental do preservativo",
    frase="""A norma que diz o que a empresa precisa provar para registrar um preservativo, e que
amarra o registro à determinação do risco ambiental do produto.""",
    corpo="""
## 1. O que o documento é

Portaria Normativa do Ibama, publicada no Diário Oficial da União de 25 de novembro de 1997,
Seção 1, página 27.552. Regulamenta **o que deve ser protocolado** para registrar ou adequar o
registro de um produto preservativo de madeira, e condiciona esse registro à determinação do
risco ambiental.

**Limite material, declarado:** o OCR da Imprensa Nacional neste documento é degradado. Os
artigos 1º a 4º são legíveis e são os que sustentam esta ficha; o número da Portaria no
cabeçalho **não** é legível no extrato, e a identificação vem do índice oficial do Ibama, não
do texto. Quem citar esta ficha deve citar os artigos, não o cabeçalho.

---

## 2. O que ela estabelece

### 2.1 O registro depende de risco ambiental determinado

> "considerando que o procedimento de registro e adequação de registro dos produtos
> Preservativos de Madeira dependem da determinação do Risco Ambiental por eles
> representado" (p. 1)

### 2.2 O dossiê e o que ele remete

> "Para efeito de registro de produtos Preservativos de Madeira, o interessado deverá
> protocolar processo contendo a documentação completa estabelecida pelo Art. 50 da Portaria
> in'cerministerial n° 292/89 de 28 de abril de 1989 e pelo inciso II. alíneas b, d e • da
> Instrução Normativa IBAMA n° 05/92 de 20 de outubro de 1992." (p. 1)

O OCR da Imprensa Nacional grafa os ordinais como "10" e "50" onde a leitura é "1º" e
"5º" — o extrato é reproduzido como está, sem correção silenciosa.

### 2.3 A organização do dossiê por seções

> "a) Cada sessão do dossiê (C, D, E, F, e G) deverá constar de volumes separados [...]"
> (p. 1)

> "d) Cada volume deverá apresentar ao menos capa frontal e lombada na cor correspondente à
> sessão, como descrita a seguir: (Parte C - branca, Parte D - rosa, Parte E - amarela, Parte
> F - azul, Parte G - verde)." (p. 1)

### 2.4 O silêncio admitido tem consequência

> "A não apresentação de testes ou informação deverá ser justificada tecnicamente e será
> avaliada pelo Instituto Brasileiro do Meio Ambiente e dos Recursos Naturais Renováveis" (p. 1)

> "A não aceitação da justificativa técnica apresentada será comunicada oficialmente à empresa,
> que disporá de 10 (dez) dias para a complementação do processo, sob pena de arquivamento do
> mesmo" (p. 1)

---

## 3. Por que esta Portaria importa para a gaveta

Ela é a prova de que o **risco ambiental é requisito de registro**, não adorno. Um preservativo
entra no mercado brasileiro porque teve risco ambiental avaliado — e o documento que atesta
isso é o certificado de registro, como o do Tanalith (Ibama, 2024).

**O que ela não resolve:** o risco avaliado é o do **produto em uso**, não o do **resíduo ao
fim da vida útil**. A Portaria organiza as seções do dossiê do produto; não cria seção para o
destino da peça tratada. A fiscalização do resíduo não está aqui — está na norma de resíduos
sólidos, que trata madeira tratada como resíduo Classe I (ver ficha do Iema-ES).

---

## 4. Relações

- **com a PI 292/89:** é sua regulamentadora direta; cita-a no art. 1º. Ver ficha própria.
- **com a IN Ibama 5/92:** remete a ela e **não foi custodiada** — ver a pendência declarada no
  manifesto S11-c. A Instrução não foi localizada no intervalo de páginas varrido do DOU.
- **com o certificado do Tanalith:** o certificado é o resultado visível deste procedimento.
""",
)

FICHAS["ficha-iema-es-nt01-2023-preservacao-madeira"] = dict(
    chave="iema2023",
    titulo="Iema-ES, NT 01/2023 — o regulador descrevendo o que não sabe",
    frase="""Nota técnica do órgão ambiental capixaba sobre o licenciamento da preservação de
madeira. É a fonte mais reveladora da gaveta: o próprio regulador escreve que **não existem
muitas informações sobre o CCB e sobre a disposição de resíduos**, ao mesmo tempo em que
registra que **não há proibição de uso no Brasil**.""",
    corpo="""
## 1. O que o documento é

Nota Técnica Orientativa GGE-COED nº 01/2023, do Instituto Estadual de Meio Ambiente e Recursos
Hídricos do Espírito Santo, assinada em 14 de dezembro de 2023, com 36 páginas. Descreve o
processo de licenciamento ambiental da atividade de **preservação de madeira por tratamento
químico**: insumos, autoclave, efluentes, resíduos, controles e monitoramento.

Não é norma federal. É o entendimento de um órgão licenciador estadual — e é por isso que vale:
mostra o que a autoridade ambiental efetivamente exige de quem trata madeira no Brasil.

---

## 2. O retrato do setor, dado pelo regulador

### 2.1 O CCA domina; o CCB é coadjuvante e desconhecido

> "nas empresas de preservação de madeira do Brasil, o arseniato
> de cobre cromatado (CCA) representou 80 % do volume utilizado; o CCB (preservativo a base de
> cobre cromo e boro), o lindane e o tribromofenato de sódio, representaram apenas 15,0%; o
> óleo creosoto, 5,0 %." (p. 5)

> "O método de preservação mais utilizado foi o sob pressão em autoclave (84 %); o restante da
> madeira foi tratada por imersão [...] e por adição na cola" (p. 5)

### 2.2 A admissão que sustenta a tese da peça

> "Em relação aos outros produtos preservativos como o CCB (cromo, cobre e boro) e óleo
> creosoto também são classificados como extremamente tóxicos (classe I). **Não existem muitas
> informações sobre o CCB em relação aos aspectos ambientais e à disposição de resíduos na
> madeira tratada.**" (p. 5, ênfase acrescentada)

O CCB é o preservativo da instrução da Embrapa para o produtor rural, e o mesmo detectado em
bambu na literatura brasileira (ver ficha Rusch 2023). O órgão ambiental do Espírito Santo
declara, por escrito, que **há pouca informação sobre o destino do resíduo dele**.

### 2.3 Não há proibição no Brasil — e o mesmo documento mostra o resto do mundo

> "considerando que **não há proibição de uso no Brasil** é imprescindível que seja assegurado
> o seu correto uso para prevenção de prejuízos à saúde das pessoas, bem como contaminação do
> solo e águas subterrâneas e superficiais." (p. 13, ênfase acrescentada)

> "Nos Estados Unidos, a Environmental Protection Agency – EPA - anunciou, em 2003, uma decisão
> voluntária das indústrias para **cessar a produção de madeira tratada com CCA em uso
> residencial**, ou seja, para playgrounds, decks e cercas de casas" (p. 14, ênfase
> acrescentada)

> "No Brasil, o IBAMA realiza o registro dos preservantes3 de madeira autorizados para uso,
> atualmente há sete registros validos para o composto CCA." (p. 14)

O "3" colado em "preservantes" é marca de nota de pé, e "validos" está sem acento no
original — os dois preservados como estão, sem correção silenciosa.

**A sequência lógica, que é o achado:** o mesmo documento que registra a retirada do uso
residencial nos Estados Unidos registra que no Brasil não há proibição, e que existem sete
registros válidos. Não é inferência do curador — são três frases do mesmo órgão, na mesma nota
técnica, a duas páginas de distância.

### 2.4 O efluente é reutilizado a 100 % — dentro da usina

> "Todo efluente contaminado gerado na empresa, durante o processo produtivo e/ou de secagem da
> madeira durante o período de fixação primária do preservante [...] deverá ser, em sua
> totalidade (100 %), utilizado no processo de preservação de madeira." (p. 10)

Este é o padrão que a **usina licenciada** tem de cumprir. É a régua contra a qual o banho
caseiro pode ser medido — e a razão pela qual a peça pode dizer que a exigência existe e não
alcança quem trata no quintal.

### 2.5 O resíduo é Classe I e vai para aterro industrial

> "Armazenamento temporário em local fechado, impermeabilizado e coberto e destinação em
> aterro industrial - classe I" (p. 4)

> "a madeira somente poderá sofrer qualquer tipo de manipulação após decorrido um período de 15
> (quinze) dias do tratamento (período de cura)" (p. 6)

> "resíduos de madeira tratada não podem ser destinados juntamente com os resíduos de madeira
> não tratada" (p. 10)

---

## 3. Limites desta fonte

- É **nota orientativa estadual**, não norma federal nem decisão judicial: orienta o
  licenciamento no Espírito Santo, e não vincula os outros estados.
- Os percentuais de mercado (80 % / 15 % / 5 %) são citados pelo Iema a partir da **Revista da
  Madeira**, não medidos por ele. A cadeia de origem do dado é secundária — a ficha registra
  assim.
- Descreve o processo **industrial licenciado**. Não mede o que acontece fora da usina.
- O documento data de dezembro de 2023; "sete registros válidos" é o número daquela data.

---

## 4. Relações

- **com a PI 292/89:** o Iema opera dentro da estrutura de registro que a Portaria criou.
- **com o certificado do Tanalith (Ibama, 2024):** o Tanalith é um dos sete registros válidos.
- **com a Embrapa COT 110:** o CCB que a Embrapa ensina ao produtor rural é o preservativo sobre
  o qual o regulador declara não ter informação de descarte.
- **com a peça do cobre:** entra no capítulo do limbo como a voz da autoridade ambiental — e é a
  fonte mais forte da peça para dizer que o problema é reconhecido por dentro do Estado.
""",
)

FICHAS["ficha-abpm-fg4mad-destinacao-residuo-madeira-tratada"] = dict(
    chave="fg4mad2016",
    titulo="ABPM/FG4mad — o que a própria cadeia diz que o resíduo não pode",
    frase="""Apresentação da associação brasileira do setor de preservação de madeira listando, em
uma página, tudo que o resíduo de madeira tratada **não pode** — inclusive queima em fogão,
churrasqueira, forno ou caldeira de baixa temperatura.""",
    corpo="""
## 1. O que o documento é

Apresentação técnica em 21 páginas, assinada por **Flavio C. Geraldo, presidente da ABPM**
(Associação Brasileira da Indústria de Madeira Processada Mecanicamente), para o 3º Simpósio
Madeira e Construção, em agosto de 2015, e hospedada pela FG4mad. O título é "Destinação de
Resíduos de Madeira Tratada".

**Natureza:** não é norma nem artigo científico. É **material da associação setorial** — o que
a própria cadeia produtiva ensina aos seus sobre o destino do resíduo. Vale por isso: o que a
indústria diz que não se pode fazer não é exagero de ambientalista.

**Limite de custódia, declarado:** a hospedagem original apresenta **certificado TLS expirado**.
O arquivo foi baixado com verificação desativada e os bytes foram preservados; o `sha256`
registra exatamente o que foi obtido. Não há outra cópia em domínio público localizada.

---

## 2. A página que interessa

> "Resíduos de Madeira Tratada não Podem:
> ‐ Contato com alimentos /água potável
> ‐ Cama para animais
> ‐ **Queima a céu aberto ou em fogões/churrasqueiras/fornos/caldeiras de baixa temperatura**"
> (p. 12, ênfase acrescentada)

> "Por conterem substâncias químicas impregnadas, estão sujeitas às regras de controle de
> disposição de resíduos sólidos perigosos." (p. 12)

> "Legislações determinam as responsabilidades e ações do agente gerador / transportador /
> triagem/tratamento e destinação" (p. 12)

### 2.1 As formas de destinação admitidas

> "Formas de destinação ‐ Áreas de transbordo e triagem (ATT) • Ecopontos (pequenos volumes –
> 1m³) • Reutilização • Reciclagem • Recuperação Energética • Aterros Licenciados - Classe II A
> ( não perigosos / inertes e não inertes) ou Classe I (perigosos)" (p. 12)

Note a **"recuperação energética"** na lista: queimar em instalação licenciada é destino
admitido; queimar em fogão de casa não é. A distinção é da **instalação**, não do ato de
queimar — e é precisamente a distinção que a peça precisa fazer com clareza, para não
escorregar em afirmação absoluta.

---

## 3. Por que esta fonte vale mais do que a norma

A norma diz o que o gerador **deve** fazer. Este documento diz o que o resíduo **não pode** —
e foi escrito por quem produz o resíduo. Uma proibição declarada pela própria associação
industrial é o tipo de fonte que não se rebate chamando o autor de militante.

**O que ela não faz:** não mede quanto resíduo é queimado em fogão doméstico no Brasil, nem
onde. Ela declara a proibição. A medição da prática é outra pergunta, e continua em aberto
(ver a pendência do item 2 no material de revisão).

---

## 4. Relações

- **com a NT 01/2023 do Iema-ES:** o órgão ambiental manda o resíduo Classe I para aterro
  industrial licenciado; a associação setorial diz o mesmo, em linguagem de apresentação.
- **com a Embrapa COT 110:** a instrução rural proíbe descartar a solução no ambiente; esta
  apresentação proíbe queimar a peça tratada. As duas cobrem pontas diferentes do mesmo
  problema.
- **com a peça do cobre:** é a fonte que permite dizer, sem exagero, que queimar madeira
  tratada em fogão de casa é proibido — e proibido por quem a produz.
""",
)

FICHAS["ficha-ufsm-2025-cca-moiroes-contaminacao-solo"] = dict(
    chave="ufsm2025",
    titulo="Ciência Florestal 2025 — o arsênio que sai do moirão e entra no solo",
    frase="""Ensaio de campo de 880 dias com cinco moirões de eucalipto tratados com CCA-C: o
arsênio da madeira caiu 55,0% e o do solo subiu 129,2%, ficando 32,3% acima do valor máximo de
investigação para o setor agrícola da Resolução CONAMA 420/2009.""",
    corpo="""
## 1. O que o documento é

Artigo em **Ciência Florestal**, v. 35, e86024, p. 1-16, 2025 (DOI 10.5902/1980509886024),
publicado em acesso aberto sob CC BY 4.0. Submetido em dezembro de 2023, aprovado em março de
2024. Ensaio **de campo**, não de laboratório.

**Desenho experimental:** cinco moirões de *Eucalyptus* spp. tratados por vácuo-pressão com
**CCA tipo C** em autoclave industrial, implantados no campo. **Seis amostragens** — 1º dia,
94, 226, 318, 460 e 880 dias — em **duas profundidades** (0 a 20 cm e 20 a 40 cm), mais secção
transversal de cada moirão na instalação e no fim do experimento.

**Recorte:** madeira (moirão), não bambu. Entra na gaveta porque mede o mecanismo que a peça
descreve: o preservativo não fica na peça, ele migra.

---

## 2. O resultado, como o artigo o enuncia

> "The wood preservative chemical constituents leached from the fence posts into the soil. The
> arsenic concentration of the fence posts showed a reduction of **55.0%**. The concentration of
> arsenic in the soil increased by **129.2%**, being **32.3% higher than the maximum value for
> investigation in the agricultural sector, according to CONAMA resolution 420/2009**,
> demonstrating potential risks of contamination, direct or indirect, to human health." (p. 1,
> resumo, ênfase acrescentada)

> "The chemical components used to treat fence posts with chromated copper arsenate (CCA) leach
> from the wood and have the potential to contaminate soil, surface water and groundwater, be
> absorbed by plants and, consequently, pose risks to animals and human health, which makes its
> use questionable." (p. 1)

### 2.1 O que os três números querem dizer, para quem não é da área

- **−55,0% na madeira:** em pouco menos de dois anos e meio de campo, o moirão perdeu mais da
  metade do arsênio que tinha.
- **+129,2% no solo:** o que saiu da madeira foi para o solo em volta. Mais que dobrou.
- **32,3% acima do limite:** o solo ficou acima do **valor máximo de investigação** que a
  Resolução CONAMA 420/2009 fixa para área agrícola — ou seja, acima do ponto em que a norma
  manda investigar se há risco.

**O detalhe que dá o tamanho do problema:** não é uma peça numa fábrica. É um moirão de cerca,
em campo, no uso para o qual ele foi feito. O que a peça do cobre chama de "resíduo" começa a
migrar antes de a peça virar resíduo.

---

## 3. Limites — declarados pelo próprio desenho

- **Cinco moirões** em **um sítio**. Não é amostra para generalizar por bioma, solo ou clima.
- Mediu **solo a até 40 cm**. **Não mediu água subterrânea** — a peça não pode usar este artigo
  para afirmar contaminação de lençol.
- Mediu **lixiviação em campo**, não **queima**. O que acontece com o arsênio quando a peça é
  queimada é outra literatura (ver a ficha Scussel 2020 no acervo).
- É **CCA**, não CCB. Os dois têm cromo e cobre, mas o CCA tem arsênio e o CCB tem boro —
  transporte de conclusão de um para o outro é inferência, e precisa ser rotulada como tal.
- 880 dias é o horizonte do ensaio; o que acontece em 20 anos não está medido aqui.

---

## 4. Relações

- **com o certificado do Tanalith (Ibama, 2024):** o CCA-C registrado no Brasil é o mesmo tipo C
  usado nos moirões.
- **com a NT 01/2023 do Iema-ES:** o órgão manda monitorar solo e água subterrânea na usina
  licenciada — este artigo mostra por que. E mostra que, fora da usina, ninguém monitora.
- **com a CONAMA 420/2009:** é o parâmetro que dá sentido ao "32,3% acima".
- **com a peça do cobre:** é a fonte que sustenta a frase sobre lixiviação para o subsolo sem
  precisar de adjetivo. O número fala.
""",
)

os.makedirs(DEST, exist_ok=True)
gerados = []
for slug, f in FICHAS.items():
    m = MAN[f["chave"]]
    cab = CABECALHO.format(arquivo=m["arquivo"], sha=m["pdf_sha256"],
                           paginas=m["paginas"], url=m["fonte_url"])
    texto = (cab + f"# {f['titulo']}\n\n> **Em uma frase.** {f['frase']}\n\n---\n"
             + f["corpo"].rstrip() + "\n" + DECL_IA)
    caminho = os.path.join(DEST, slug + ".md")
    open(caminho, "w", encoding="utf-8").write(texto)
    h = hashlib.sha256(open(caminho, "rb").read()).hexdigest()
    gerados.append({"slug": slug, "arquivo": slug + ".md", "bytes": len(texto.encode()),
                    "sha256": h, "fonte_sha256": m["pdf_sha256"], "paginas": m["paginas"]})
    print(f"  {slug[:52]:54s} {len(texto.splitlines()):>4} linhas  {h[:12]}")

json.dump({"lote": "S11-c", "data": "2026-11-24", "fichas": gerados},
          open(f"{DEST}/MANIFEST_FICHAS_S11C.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print(f"\nFICHAS: {len(gerados)}  DESTINO: {DEST}")
