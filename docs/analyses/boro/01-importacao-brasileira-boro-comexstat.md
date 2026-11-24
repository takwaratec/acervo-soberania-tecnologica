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

> **Síntese.** O Brasil importou **487.185 t** de produtos de boro em 2025, por
> **US$ 225,8 milhões** FOB — cerca de **4,4 vezes a massa e 6,3 vezes o valor de
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

| Ano | 2528 boratos naturais (t) | 2810 ácidos e óxidos (t) | 2840 boratos refinados (t) | Total (t) | Total (US$ FOB) | US$/kg |
|---|---|---|---|---|---|---|
| 1997 | 72.642 | 16.446 | 22.533 | **111.621** | 35,9 M | 0,321 |
| 1998 | 74.673 | 17.964 | 25.475 | **118.112** | 39,9 M | 0,338 |
| 1999 | 78.291 | 18.924 | 29.059 | **126.273** | 41,8 M | 0,331 |
| 2000 | 99.024 | 21.546 | 25.771 | **146.340** | 42,3 M | 0,289 |
| 2001 | 93.837 | 20.161 | 24.598 | **138.596** | 37,1 M | 0,268 |
| 2002 | 104.838 | 25.086 | 20.864 | **150.787** | 34,8 M | 0,231 |
| 2003 | 143.068 | 28.272 | 19.619 | **190.958** | 38,9 M | 0,203 |
| 2004 | 169.422 | 28.173 | 22.113 | **219.708** | 43,5 M | 0,198 |
| 2005 | 103.958 | 29.452 | 21.268 | **154.678** | 38,5 M | 0,249 |
| 2006 | 107.224 | 29.371 | 18.219 | **154.814** | 37,2 M | 0,240 |
| 2007 | 141.037 | 34.404 | 20.661 | **196.102** | 48,6 M | 0,248 |
| 2008 | 117.630 | 36.937 | 22.757 | **177.324** | 78,4 M | 0,442 |
| 2009 | 108.113 | 22.487 | 15.333 | **145.933** | 53,1 M | 0,364 |
| 2010 | 136.938 | 35.179 | 20.867 | **192.984** | 70,7 M | 0,366 |
| 2011 | 163.448 | 39.691 | 19.453 | **222.592** | 98,3 M | 0,442 |
| 2012 | 176.462 | 42.784 | 15.105 | **234.351** | 104,8 M | 0,447 |
| 2013 | 160.991 | 35.965 | 14.416 | **211.372** | 91,1 M | 0,431 |
| 2014 | 146.503 | 33.238 | 17.576 | **197.316** | 81,9 M | 0,415 |
| 2015 | 129.118 | 36.011 | 15.733 | **180.862** | 72,0 M | 0,398 |
| 2016 | 125.805 | 33.994 | 16.634 | **176.432** | 61,5 M | 0,348 |
| 2017 | 167.673 | 47.196 | 21.677 | **236.545** | 78,4 M | 0,332 |
| 2018 | 149.013 | 45.352 | 28.497 | **222.862** | 85,4 M | 0,383 |
| 2019 | 172.394 | 41.648 | 26.295 | **240.337** | 81,2 M | 0,338 |
| 2020 | 197.770 | 42.451 | 29.798 | **270.020** | 88,6 M | 0,328 |
| 2021 | 268.179 | 51.540 | 34.140 | **353.859** | 117,6 M | 0,332 |
| 2022 | 244.241 | 59.183 | 29.687 | **333.112** | 157,8 M | 0,474 |
| 2023 | 300.351 | 55.558 | 26.848 | **382.758** | 154,3 M | 0,403 |
| 2024 | 327.964 | 82.617 | 48.975 | **459.556** | 204,7 M | 0,445 |
| 2025 | 342.799 | 82.687 | 61.700 | **487.185** | 225,8 M | 0,464 |
| 2026* | 260.600 | 72.181 | 39.960 | **372.742** | 205,2 M | 0,551 |

\* janeiro a outubro de 2026 (dez meses).

**Três fatos que a tabela sustenta, e um que ela não sustenta.**

1. A massa importada **quadruplicou** entre 1997 (111,6 kt) e 2025 (487,2 kt).
2. O valor cresceu **mais rápido que a massa** (6,3× contra 4,4×): o produto
   importado está mais refinado e mais caro por quilo em 2025 (US$ 0,464/kg)
   do que em 1997 (US$ 0,321/kg).
3. O crescimento é **recente e abrupto**: 270 kt em 2020 → 487 kt em 2025, quase
   80% em cinco anos. O patamar de 1997–2016 estava entre 110 e 235 kt.
4. A tabela **não** sustenta que o Brasil "consome" essa massa: parte do minério
   entra para ser processada e reexportada, e o ComexStat mede comércio, não
   consumo aparente. Ver §7.

---

## 3. Composição — o que exatamente entra (2025)

| NCM | Produto | Massa (t) | Valor (US$ FOB) | % do valor | US$/kg |
|---|---|---|---|---|---|
| 25280000 | Boratos naturais e concentrados | 342.799 | 102,8 M | 45,53% | 0,300 |
| 28100010 | Ácido ortobórico | 82.492 | 69,0 M | 30,57% | 0,837 |
| 28401900 | Bórax refinado (outros tetraboratos dissódicos) | 47.136 | 33,4 M | 14,77% | 0,708 |
| 28402000 | Outros boratos | 14.246 | 19,2 M | 8,48% | 1,345 |
| 28100090 | Óxidos de boro e outros ácidos bóricos | 195 | 0,7 M | 0,30% | 3,428 |
| 28401100 | Tetraborato dissódico anidro | 199 | 0,3 M | 0,15% | 1,712 |
| 28403000 | Peroxoboratos (perboratos) | 119 | 0,5 M | 0,20% | 3,797 |

**Leitura.** Sete de cada dez quilos importados são **minério bruto** (2528), mas
o minério responde por menos da metade do valor. O **ácido bórico refinado** é o
item de maior valor unitário entre os de volume relevante (US$ 0,84/kg) e o
segundo em valor total. O Brasil compra, portanto, **rocha barata em quantidade**
e **química refinada em valor** — perfil de país que é consumidor industrial, não
produtor.

---

## 4. Origem — de quem o Brasil compra

Acumulado 2010–2026, valor FOB:

| Origem | US$ FOB | Massa (t) | % do valor | US$/kg |
|---|---|---|---|---|
| Argentina | 677,3 M | 1.519.670 | 34,2% | 0,446 |
| Bolívia | 450,8 M | 1.833.596 | 22,8% | 0,246 |
| Chile | 330,8 M | 619.666 | 16,7% | 0,534 |
| Turquia | 279,7 M | 518.022 | 14,1% | 0,540 |
| Estados Unidos | 117,1 M | 156.026 | 5,9% | 0,751 |
| Peru | 60,8 M | 78.476 | 3,1% | 0,774 |
| Guatemala | 27,7 M | 36.580 | 1,4% | 0,757 |
| China | 17,5 M | 8.599 | 0,9% | 2,038 |

**Argentina, Bolívia, Chile e Peru somam 76,8% do valor importado.** As quatro
são, exatamente, as quatro economias que a USGS lista como produtoras de borato
no **cinturão andino** — o mesmo cinturão que a fonte institucional aponta como
uma das três maiores concentrações econômicas de boro do mundo (§5).

**Movimento recente (valor FOB, % do total do ano):**

| Origem | 2024 | 2025 | 2026 (10 meses) |
|---|---|---|---|
| Argentina | 26,9% (117 kt) | 30,0% (151 kt) | 33,4% (126 kt) |
| Bolívia | 25,2% (201 kt) | 22,6% (170 kt) | 17,7% (80 kt) |
| Chile | 20,7% (68 kt) | 16,0% (48 kt) | 11,6% (24 kt) |
| Turquia | 12,0% (38 kt) | 17,3% (78 kt) | **30,9% (127 kt)** |
| Estados Unidos | 8,0% (21 kt) | 7,6% (22 kt) | 1,7% (5 kt) |

**A Turquia dobrou a massa embarcada ao Brasil entre 2025 e os dez primeiros meses
de 2026** (78 kt → 127 kt), e no mesmo intervalo a Bolívia caiu de 170 kt para
80 kt. Isso é dado de comércio observado, não projeção. Não há, nesta gaveta,
fonte custodiada que explique a causa (contrato, nova rota, reabertura de mina) —
e portanto **não se afirma causa**. O que se afirma: a concentração sul-americana,
que era estável por quinze anos, **começou a mudar em 2026**.

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

Aplicando ao total de 2025 (487.185 t de produto), com a faixa 11–17,5%:
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
comercial importada** (487.185 t em 2025) — não um intervalo de boro elementar.
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
       "filters":[{"filter":"ncm","values":["25280000","28100010","28100090",
                   "28401100","28401900","28402000","28403000"]}],
       "details":["country"],"metrics":["metricFOB","metricKG"]}'
```

**Armadilhas operacionais verificadas nesta extração:**

1. Pedir `1997-01` a `2026-12` em uma única chamada devolve **HTTP 500**. A
   extração foi feita **ano a ano**.
2. O filtro `ncm` aceita **código de 8 dígitos** (`28100010`); a forma pontuada
   (`2810.00.00`) devolve lista vazia **com HTTP 200** — falha silenciosa.
3. O `GET` no mesmo endpoint devolve os **anos disponíveis**, não os dados.

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
