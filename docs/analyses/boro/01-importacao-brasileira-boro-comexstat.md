---
schema: ACERVO_ANALISE_PUBLICA_R1
tipo_documental: estado-da-arte-com-agenda-experimental
gaveta: boro
frente: BORO
titulo: "Importação brasileira de boro — série 1997–2026 por NCM (ComexStat/MDIC)"
estado_documental: em-revisao-documental
homologacao_automatica: false
versao: 1
data_extracao: 2026-11-24
responsavel_curadoria: Fabio Takwara
assistencia_documental: agente de IA, sujeito a revisao humana
fonte_primaria: API oficial ComexStat / MDIC (consulta direta, resposta gravada)
pacote_dados_privado: _privado/governanca-operacional/extracoes/boro/fontes_novas/comexstat/
complementa: 00-estado-da-questao-boro.md §5.1
---

# Importação brasileira de boro — série 1997–2026 por NCM

> **Síntese.** O Brasil importou **487.339 t** de produtos de boro em 2025, por
> **US$ 230,0 milhões** FOB — cerca de **4,4 vezes a massa e 6,3 vezes o valor de
> 1997**. Não há produção nacional de boratos declarada à USGS — o que **não**
> prova que todo o boro consumido entre pelo porto: importação de produto não é
> consumo, e reexportação e estoque não são descontados. E entra, em quase quatro quintos do valor, de **vizinhos
> sul-americanos** (Argentina, Bolívia, Chile, Peru) — não da Turquia, que é a
> origem dominante do abastecimento *norte-americano*. A dependência brasileira é
> geológica e logística, mas é **regional**, não turca. Em 2026 há uma inflexão:
> a Turquia salta de 17% para 31% do valor importado em apenas dez meses.

---

## 1. Método — o que foi consultado, e o que o número mede

**Fonte.** API oficial do ComexStat (MDIC), endpoint `POST /general`, consulta
direta ao serviço em 2026-11-24. Não é relatório de terceiro, não é planilha
reproduzida, não é estimativa: cada linha é resposta do serviço oficial, gravada
byte a byte na camada privada com SHA-256 por arquivo.

**Recorte.**

| Parâmetro | Valor |
|---|---|
| Fluxo | `import` (importação brasileira) |
| Período | 1997-01 a 2026-10 |
| NCM | 2528 · 2810 · 2840 |
| Métricas | `metricFOB` (US$ FOB) e `metricKG` (peso líquido) |
| Detalhamentos | por NCM-ano e por país de origem-ano (2010–2026) |

**Os três NCM, e o que cada um carrega.**

- **2528** — boratos naturais e seus concentrados (minério bruto: ulexite,
  colemanita, tincal), inclusive ácido bórico natural até 85% H₃BO₃.
- **2810** — óxidos de boro e ácidos bóricos, sobretudo **ácido ortobórico
  refinado** (H₃BO₃).
- **2840** — boratos refinados: **bórax** (tetraborato dissódico) e outros
  boratos; peroxoboratos.

**Nota de nomenclatura, preservada e não harmonizada:** antes de 2012 o NCM 2528
vinha desdobrado em `25281000` (boratos de sódio naturais) e `25289000` (outros);
a partir de 2012 há um código único `25280000`. A série abaixo soma os códigos
vigentes em cada ano — o corte de 2012 é mudança de nomenclatura, **não** quebra
de série econômica.

**O que `metricKG` mede — e o que não mede.** É o **peso líquido do produto
comercial declarado**, não teor de boro elementar. Uma tonelada de bórax
decahidratado contém ~113 kg de B; uma tonelada de ácido bórico contém ~175 kg de
B; uma tonelada de ulexite bruto contém ~130 kg de B e impurezas. **Somar as três
colunas em toneladas soma produtos de teor diferente.** Por isso a série principal
fica em tonelada de produto (é o dado medido) e a conversão para boro elementar
aparece apenas na §6, como estimativa com premissa declarada.

---

## 2. Série histórica — massa e valor, 1997–2026

Valores em toneladas de produto (peso líquido). 2026 é **parcial**: janeiro a
outubro, dez meses.

| Ano | 2528 boratos (t) | 2804 boro elementar (t) | 2810 ácidos e óxidos (t) | 2840 boratos refinados (t) | 2849 carbonetos (t) | 2850 nitreto (t) | **Total (t)** | Total (US$ FOB) | US$/kg |
|---|---|---|---|---|---|---|---|---|---|
| 1997 | 72.642 | 1 | 16.446 | 22.533 | 5 | 1 | **111.627** | 36,7 M | 0,329 |
| 1998 | 74.673 | 2 | 17.964 | 25.475 | 6 | 1 | **118.122** | 40,8 M | 0,346 |
| 1999 | 78.291 | 2 | 18.924 | 29.059 | 4 | 3 | **126.282** | 42,7 M | 0,338 |
| 2000 | 99.024 | 3 | 21.546 | 25.771 | 16 | 26 | **146.385** | 43,4 M | 0,296 |
| 2001 | 93.837 | 2 | 20.161 | 24.598 | 17 | 2 | **138.617** | 37,9 M | 0,273 |
| 2002 | 104.838 | 3 | 25.086 | 20.864 | 16 | 30 | **150.836** | 36,0 M | 0,238 |
| 2003 | 143.068 | 22 | 28.272 | 19.619 | 21 | 53 | **191.054** | 40,6 M | 0,212 |
| 2004 | 169.422 | 37 | 28.173 | 22.113 | 51 | 30 | **219.826** | 45,9 M | 0,209 |
| 2005 | 103.958 | 4 | 29.452 | 21.268 | 59 | 4 | **154.745** | 40,9 M | 0,264 |
| 2006 | 107.224 | 27 | 29.371 | 18.219 | 16 | 16 | **154.874** | 39,4 M | 0,255 |
| 2007 | 141.037 | 4 | 34.404 | 20.661 | 32 | 23 | **196.161** | 51,3 M | 0,262 |
| 2008 | 117.630 | 5 | 36.937 | 22.757 | 85 | 22 | **177.436** | 82,4 M | 0,464 |
| 2009 | 108.113 | 3 | 22.487 | 15.333 | 9 | 9 | **145.954** | 54,6 M | 0,374 |
| 2010 | 136.938 | 6 | 35.179 | 20.867 | 60 | 29 | **193.079** | 74,6 M | 0,386 |
| 2011 | 163.448 | 5 | 39.691 | 19.453 | 67 | 17 | **222.680** | 103,0 M | 0,463 |
| 2012 | 176.462 | 4 | 42.784 | 15.105 | 53 | 17 | **234.425** | 108,6 M | 0,463 |
| 2013 | 160.991 | 9 | 35.965 | 14.416 | 81 | 23 | **211.485** | 94,9 M | 0,449 |
| 2014 | 146.503 | 3 | 33.238 | 17.576 | 93 | 19 | **197.431** | 85,4 M | 0,432 |
| 2015 | 129.118 | 8 | 36.011 | 15.733 | 82 | 31 | **180.983** | 76,1 M | 0,421 |
| 2016 | 125.805 | 4 | 33.994 | 16.634 | 77 | 22 | **176.535** | 64,4 M | 0,365 |
| 2017 | 167.673 | 9 | 47.196 | 21.677 | 144 | 26 | **236.724** | 82,8 M | 0,350 |
| 2018 | 149.013 | 10 | 45.352 | 28.497 | 87 | 25 | **222.984** | 88,8 M | 0,398 |
| 2019 | 172.394 | 10 | 41.648 | 26.295 | 132 | 24 | **240.503** | 85,1 M | 0,354 |
| 2020 | 197.770 | 6 | 42.451 | 29.798 | 73 | 12 | **270.111** | 91,7 M | 0,340 |
| 2021 | 268.179 | 3 | 51.540 | 34.140 | 141 | 23 | **354.026** | 122,5 M | 0,346 |
| 2022 | 244.241 | 16 | 59.183 | 29.687 | 82 | 22 | **333.234** | 162,8 M | 0,489 |
| 2023 | 300.351 | 5 | 55.558 | 26.848 | 108 | 14 | **382.885** | 158,7 M | 0,414 |
| 2024 | 327.964 | 7 | 82.617 | 48.975 | 141 | 19 | **459.722** | 209,5 M | 0,456 |
| 2025 | 342.799 | 5 | 82.687 | 61.700 | 132 | 18 | **487.339** | 230,0 M | 0,472 |
| 2026* | 260.600 | 5 | 72.181 | 39.960 | 86 | 16 | **372.849** | 209,2 M | 0,561 |

\* janeiro a outubro de 2026 (dez meses).

> **Nota de correção (2026-11-25).** A série anterior somava nove códigos NCM e dava
> **204,7 milhões** para 2024, omitindo 2804.50, 2849.90.10 e 2850.00.10. Também perdia
> parte do grupo 2528 em anos antigos, quando o código aparecia fragmentado em 2528.10.00
> e 2528.90.00. A tabela foi refeita a partir dos brutos com os **doze códigos** que, ao
> longo do tempo, compõem os seis grupos. 2024 passa a **US$ 209,5 milhões** e
> **459,7 mil toneladas** — os mesmos números do artigo principal.

**Três fatos que a tabela sustenta, e um que ela não sustenta.**

1. A massa importada **quadruplicou** entre 1997 (111,6 mil t) e 2025 (487,3 mil t).
2. O valor cresceu **mais rápido que a massa** (6,3× contra 4,4×): o produto
   importado está mais refinado e mais caro por quilo em 2025 (US$ 0,472/kg)
   do que em 1997 (US$ 0,329/kg).
3. O crescimento é **recente e abrupto**: 270 mil t em 2020 → 487 mil t em 2025, **80%
   em cinco anos**. O patamar de 1997–2016 ficou entre 111 e 237 mil t.
4. A tabela **não** sustenta que o Brasil "consome" essa massa: parte do minério
   entra para ser processada e reexportada, e o ComexStat mede comércio, não
   consumo aparente. Ver §7.

---

## 3. Composição — o que exatamente entra (2025)

| NCM | Produto | Massa (t) | Valor (US$ FOB) | % do valor | US$/kg |
|---|---|---|---|---|---|
| 25280000 | Boratos naturais e concentrados | 342.799 | 102,8 M | 44,71% | 0,300 |
| 28100010 | Ácido ortobórico | 82.492 | 69,0 M | 30,01% | 0,837 |
| 28401900 | Bórax refinado (outros tetraboratos dissódicos) | 47.136 | 33,4 M | 14,51% | 0,708 |
| 28402000 | Outros boratos | 14.246 | 19,2 M | 8,33% | 1,345 |
| 28499010 | Carbonetos de boro | 132 | 1,9 M | 0,84% | 14,732 |
| 28500010 | Nitreto de boro | 18 | 1,7 M | 0,76% | 99,355 |
| 28100090 | Óxidos de boro e outros ácidos bóricos | 195 | 0.7 M | 0,29% | 3,428 |
| 28045000 | Boro; telúrio (código conjunto) | 5 | 0,5 M | 0,21% | 102,284 |
| 28403000 | Peroxoboratos (perboratos) | 119 | 0,5 M | 0,20% | 3,797 |
| 28401100 | Tetraborato dissódico anidro | 199 | 0.3 M | 0,15% | 1,712 |

**Denominador:** os **dez** códigos NCM que compõem o conjunto, totalizando **US$ 230,0 milhões** e **487.339 t** em 2025. Os três de menor massa — carbonetos, nitreto e boro elementar — aparecem na tabela porque o conjunto os inclui, não porque pesem no volume: juntos são **155 t**, e sozinhos respondem por **1,8% do valor**, com preço unitário de duas a três ordens de grandeza acima do minério.

**Leitura.** Sete de cada dez quilos importados são **minério bruto** (2528), mas
o minério responde por menos da metade do valor. O **ácido bórico refinado** é o
item de maior valor unitário entre os de volume relevante (US$ 0,84/kg) e o
segundo em valor total. O Brasil compra, portanto, **rocha barata em quantidade**
e **química refinada em valor** — perfil de país que é consumidor industrial, não
produtor.

---

## 4. Origem — de quem o Brasil compra

Acumulado 2010–2026, valor FOB. **Denominador: os dez NCMs do conjunto atual, US$ 1.967,1 milhões e 4.476.505 t.**

| Origem | US$ FOB | Massa (t) | % do valor | US$/kg |
|---|---|---|---|---|
| Argentina | 645,9 M | 1.415.370 | 32,8% | 0,456 |
| Bolívia | 416,3 M | 1.684.487 | 21,2% | 0,247 |
| Chile | 321,2 M | 586.225 | 16,3% | 0,548 |
| Turquia | 275,2 M | 506.580 | 14,0% | 0,543 |
| Estados Unidos | 138,7 M | 156.367 | 7,0% | 0,887 |
| Peru | 60,3 M | 76.299 | 3,1% | 0,790 |
| China | 36,8 M | 9.648 | 1,9% | 3,817 |
| Guatemala | 27,7 M | 36.580 | 1,4% | 0,757 |

**Argentina, Bolívia, Chile e Peru somam 73,4% do valor importado.** As quatro
são, exatamente, as quatro economias que a USGS lista como produtoras de borato
no **cinturão andino** — o mesmo cinturão que a fonte institucional aponta como
uma das três maiores concentrações econômicas de boro do mundo (§5).

Repare na inversão entre as duas colunas: a **Bolívia** manda em massa (1,68 milhão
de t) e perde em valor (21,2%), porque seu mineral entra a US$ 0,247/kg. A
**Argentina** faz o contrário: menos massa, mais dinheiro, a US$ 0,456/kg. **A
Bolívia é o minério; a Argentina é o intermediário.**

**Movimento recente — participação no valor FOB do ano (massa entre parênteses). A porcentagem é de VALOR; o parêntese é MASSA.**

| Origem | 2024 | 2025 | 2026 (10 meses) |
|---|---|---|---|
| Argentina | 26,3% (117 kt) | 29,5% (151 kt) | 32,8% (126 kt) |
| Bolívia | 24,7% (201 kt) | 22,2% (170 kt) | 17,3% (80 kt) |
| Chile | 20,2% (68 kt) | 15,7% (48 kt) | 11,4% (24 kt) |
| Turquia | 11,8% (38 kt) | 17,0% (78 kt) | **30,4% (127 kt)** |
| Estados Unidos | 8,5% (21 kt) | 7,7% (22 kt) | 1,8% (5 kt) |

**A Turquia aumentou 62% a massa embarcada ao Brasil entre 2025 e os dez primeiros
meses de 2026** (78,5 kt → 127,4 kt), e no mesmo intervalo a Bolívia caiu de 170 kt
para 80 kt. Em valor, a fatia turca foi de **17,0% para 30,4%** — cresceu mais em
valor do que em massa, o que indica produto mais refinado, não só mais volume. Isso é dado de comércio observado, não projeção. Não há,
nesta gaveta, fonte custodiada que explique a causa (contrato, nova rota,
reabertura de mina) — e portanto **não se afirma causa**. O que se afirma: a
concentração sul-americana, que era estável por quinze anos, **começou a mudar
em 2026**.

---

## 5. Confronto com a produção mundial declarada (USGS MCS2026)

Produção e reservas, em milhares de toneladas (USGS, MCS2026, Boron):

| País / material | Produção 2024 | Produção 2025 | Reservas |
|---|---|---|---|
| Turquia, boratos refinados | 1.800 | 1.500 | 950.000 |
| Bolívia, ulexite | 230 | 380 | n.d. |
| Chile, ulexite | 470 | 300 | 35.000 |
| China, equivalente a óxido de boro | 210 | 230 | 9.100 |
| Peru, boratos brutos | 190 | 220 | 4.000 |
| Argentina, minério bruto | 160 | 170 | n.d. |
| Rússia, minério de datolita | 90 | 80 | 40.000 |
| Estados Unidos | n.d. (sigilo) | n.d. (sigilo) | 48.000 |

**Aritmética que vale registrar, porque mede a escala do que o Brasil compra:**
em 2025 o Brasil importou **342.799 t de boratos naturais (NCM 2528)**. A produção
mundial declarada de minério bruto dos quatro países andinos soma, no mesmo ano,
**1.070 kt** (380 + 300 + 220 + 170). A importação brasileira equivale a **cerca
de um terço de todo o minério bruto andino declarado** — e supera isoladamente a
produção da Argentina, do Chile e do Peru, cada um tomado em separado.

*(Ressalva de comparabilidade, não harmonizada: a USGS declara produção por
material e a unidade é milhares de toneladas de produto comercial, com bases de
teor diferentes entre países — "minério bruto", "ulexite", "equivalente a óxido de
boro". A razão acima é de **ordem de grandeza**, e é apresentada como tal.)*

**Interpretação curatorial.** Isto reposiciona o argumento de dependência. O
abastecimento brasileiro não depende do oligopólio turco — depende de **quatro
vizinhos com reservas modestas e produção irregular**, alguns sem reserva
declarada (Argentina, Bolívia: "NA"). A vulnerabilidade não é escassez global: é
**concentração regional com capacidade limitada**. Bolívia cai 170 kt em um ano
enquanto o Brasil cresce; a Turquia preenche a lacuna. A dependência brasileira,
portanto, é real — mas ela se move em direção à Turquia em 2026, e não o contrário.

---

## 6. Estimativa de boro elementar (premissa declarada, não medição)

O ComexStat não informa teor. A conversão abaixo é **estimativa**, construída com
fatores publicados e explícitos; ela serve para ordem de grandeza, não para
afirmação de consumo:

| Produto | Fator de B | Base do fator |
|---|---|---|
| Ácido ortobórico H₃BO₃ | 17,5% | B = 10,81 / 61,83 g/mol |
| Bórax decahidratado | 11,3% | 4 B / 381,4 g/mol |
| Bórax anidro | 21,5% | 4 B / 201,2 g/mol |
| Ulexite / colemanita (minério) | 10–17% | teor mineral, sem correção de ganga |

Aplicando ao total de 2025 (487.339 t de produto), com a faixa 11–17,5%:
**~54 a ~85 mil toneladas de boro elementar** entraram no país em 2025. Para 1997
(111.621 t): ~12 a ~20 kt de B.

**Limite explícito — e uma correção.** A faixa de 11–17,5% **não é teto nem piso
demonstrado**, e aplicá-la ao total mistura produtos de naturezas diferentes:

- o **bórax anidro tem 21,5% de B**, acima do teto de 17,5% usado — o intervalo
  **subestima** essa parcela;
- o **minério bruto** (ulexita, colemanita) carrega ganga, o que puxa para baixo;
- somar NCMs distintos e aplicar um fator único pressupõe composição média que a
  série não informa.

Sem discriminação de produto e teor, os dados oficiais sustentam a **massa
comercial importada** (487.339 t em 2025) — não um intervalo de boro elementar.
A conversão serve para ordem de grandeza, com esta ressalva anexada.

---

## 7. O que esta análise não autoriza concluir

- **Não** autoriza afirmar consumo brasileiro de boro. ComexStat mede **comércio
  declarado**, não consumo aparente nem estoque; parte do minério pode ser
  processada e reexportada.
- **Não** autoriza dividir o total por habitante, por hectare agrícola ou por
  produção de bambu: não há, nesta gaveta, rateio setorial da importação.
  A USGS e o estudo de matérias-primas críticas da UE dão participações
  **mundiais** por segmento (§5 da ficha principal); aplicá-las ao Brasil seria
  transportar valor entre populações diferentes, o que esta gaveta proíbe.
- **Não** autoriza atribuir a alta de 2026 à Turquia a qualquer causa — contrato,
  preço, ruptura de oferta boliviana. É dado de comércio sem explicação custodiada.
- **Não** autoriza dizer que o boro importado vai para preservação de bambu. A
  preservação de madeira é ~8% do consumo **mundial**; a fatia brasileira da
  importação não foi medida.
- **Não** substitui a declaração de produção nacional: a ausência do Brasil na
  tabela da USGS é **ausência na fonte**, não prova de zero produção. A USGS lista
  apenas produtores que reportam.

---

## 8. Como reproduzir

```bash
curl -s -X POST https://api-comexstat.mdic.gov.br/general \
  -H "Content-Type: application/json" \
  -d '{"flow":"import","monthDetail":false,
       "period":{"from":"2025-01","to":"2025-12"},
       "filters":[{"filter":"ncm","values":["25280000","28045000","28100010","28100090",
                   "28401100","28401900","28402000","28403000","28499010","28500010"]}],
       "details":["country"],"metrics":["metricFOB","metricKG"]}'
```

**Atenção ao conjunto de códigos.** A consulta acima traz os **dez** NCMs do
conjunto atual. Para a **série histórica desde 1997** é preciso acrescentar
`25281000` e `25289000`: até 2011 o grupo 2528 vinha fragmentado nesses dois
códigos, e uma consulta só com `25280000` devolve **zero** para os anos antigos.
A série histórica deste documento usa os doze códigos; a composição de 2025 usa
os dez, porque os dois antigos já não têm movimento.

**Armadilhas operacionais verificadas nesta extração:**

1. Pedir `1997-01` a `2026-12` em uma única chamada devolve **HTTP 500**. A
   extração foi feita **ano a ano**.
2. O filtro `ncm` aceita **código de 8 dígitos** (`28100010`); a forma pontuada
   (`2810.00.00`) devolve lista vazia **com HTTP 200** — falha silenciosa.
3. O `GET` no mesmo endpoint devolve os **anos disponíveis**, não os dados.
4. **Um filtro estreito não dá erro: dá número menor.** Somar nove NCMs em vez de
   dez produziu US$ 204,7 M em 2024 em vez de US$ 209,5 M, e ninguém percebeu por
   duas rodadas de auditoria — o total continuava "plausível". É a falha silenciosa
   mais cara desta extração.

Arquivos: `MANIFEST_ComexStat.json` (52 arquivos, SHA-256 por arquivo, corpos de
consulta e observações), quatro CSV derivados e a resposta bruta por ano.

---

## Referências documentais

- **ComexStat / MDIC.** API oficial, `POST https://api-comexstat.mdic.gov.br/general`.
  Consulta direta em 2026-11-24; respostas gravadas em
  `_privado/governanca-operacional/extracoes/boro/fontes_novas/comexstat/raw/`.
- **USGS.** *Mineral Commodity Summaries 2026* — Boron. Brioche, A.S. 2 p.
  Custódia: `fontes_novas/USGS_MCS2026_Boron.pdf`. (Produção, reservas, cinturão
  andino, fontes de importação dos EUA.)
- **Receita Federal / MDIC.** NCM 2528, 2810, 2840 — descrições conforme
  declaradas pela própria API, preservadas sem edição nos CSV.

---

**Controle de fronteiras.** Fato medido (tabelas 1–3) separado de interpretação
(§4 a §6) e de limites (§7). Números declaram base e fonte. A divergência de
nomenclatura do NCM 2528 antes/depois de 2012 foi preservada, não harmonizada.
Bibliografia integral e respostas brutas permanecem na camada privada.
Estado: **em-revisao-documental**; não homologado; não é certificação nem
autorização de publicação.
