---
schema: ACERVO_MAPA_REPROCESSAMENTO_R1
gaveta: cobre
frente: COBRE
aberta_em: 2026-11-24T13:59:13Z
ledger_commit: a37861ff8015e76b70e1a8e38773dc56e4befce9
titulo: "Cobre — mapa de reprocessamento do que já está custodiado"
estado_documental: em-revisao-documental
homologacao_automatica: false
versao: 1
data_revisao: 2026-11-24
responsavel_curadoria: Fabio Takwara
assistencia_documental: agente de IA, sujeito a revisao humana
bootstrap_de_origem: docs/analyses/boro/BOOTSTRAP_COBRE_20261124.md
bootstrap_sha256_16: 948b91110de0acc4
fonte_primaria: seis fichas com PDF integral conferido; NR-15 e NR-6 custodiadas
funcao_na_serie: capitulo 2 dos tratamentos convencionais do bambu
tipo_documental: instrumento-de-pesquisa
---
# Cobre — mapa de reprocessamento

> **Síntese.** A frente COBRE não começa do zero: começa com **seis fichas
> prontas**, **seis PDFs de fonte** e um **pacote de 38 PDFs** de saúde
> ocupacional que nunca passou pela régua de curadoria atual. O reprocessamento
> destes três conjuntos — feito aqui, antes de qualquer pesquisa nova — muda duas
> coisas no plano. Primeiro, o material brasileiro de CCA é mais forte do que o
> esperado: há norma de registro, lixiviado medido e solo medido em campo.
> Segundo, e mais importante: **a NR-15 não tem limite de tolerância para cobre,
> nem para arsênio, nem para poeira de madeira**, e a sílica que ela regula é o
> **quartzo**, não o fitólito amorfo do bambu. O buraco regulatório que a gaveta
> do boro só intuía está agora **verificado no texto normativo custodiado**.

---

## 1. O que este documento é, e o que ele não é

**É** o passo 8 do bootstrap executado: o inventário verificado do que existe, a
síntese do que as seis fichas já provam, as divergências que não podem ser
harmonizadas, o que os normativos brasileiros efetivamente dão, e a lista do que
o roteiro planejou mas **não** está custodiado.

**Não é** pesquisa nova, não é ficha de fonte, não é homologação. Nada aqui foi
promovido de estado. As seis fichas continuam `ficha-em-revisao`; esta gaveta
continua `em-revisao-documental`.

**Frente.** `COBRE` foi aberta no ledger R4 em 2026-11-24T13:59:13Z, commit
`a37861ff`, com escopo de escrita em `docs/analyses/cobre` e
`_privado/governanca-operacional/extracoes/cobre`. O material pré-existente
(`_privado/fichas/ago_28_CCA_CCB`, `_privado/fontes-documentais/ago_28_CCA_CCB`,
`_privado/fontes-documentais/ago_27_VOCs`) está **fora** desse escopo: foi lido,
não alterado.

---

## 2. Inventário verificado (contagem conferida no disco, não presumida)

| Conjunto | Caminho | Arquivos | PDFs | Bytes |
|---|---|---|---|---|
| Fichas prontas | `_privado/fichas/ago_28_CCA_CCB/` | 6 | — | 94.801 |
| Fontes CCA/CCB | `_privado/fontes-documentais/ago_28_CCA_CCB/` | 22 | 6 | 9.623.117 |
| Pacote de ocupacional/voláteis | `_privado/fontes-documentais/ago_27_VOCs/` | 45 | 38 | 137.180.781 |

**Conferência contra o bootstrap:** o bootstrap declarava 45 arquivos e 38 PDFs
para `ago_27_VOCs`; o disco confirma **45 e 38**. A contagem anterior (46/26)
estava errada e já foi corrigida no bootstrap.

**Armadilha de sistema de arquivos confirmada:** **16 dos 45 nomes** de
`ago_27_VOCs` estão em **NFD** (Unicode decomposto, padrão do macOS). `ls` mostra
igual; comparação de string com path literal falha. Nesta rodada todo acesso foi
feito por `os.listdir()` e `unicodedata.normalize('NFC', …)`.

**O pacote de fontes CCA/CCB é mais completo do que “seis PDFs”:** cada fonte tem
`.pdf`, `.canonical.txt` e `.md` (três representações), mais
`manifest/manifest_sha256.csv`, `logs/extracao.log` e
`Contrato_extração pdf_SHA-256.md`. Isso significa que a extração de texto das
seis fontes **já foi feita e conferida** — não precisa ser refeita.

---

## 3. O que as seis fichas já provam

Todas são `ficha-em-revisao`, com `fonte_primaria: PDF integral conferido`.
Nenhuma foi homologada.

### 3.1 IBAMA 2024 — Tanalith 60% CCA-C (fonte regulatória brasileira)

É a fonte mais forte da gaveta, porque é norma, não artigo:

- Composição declarada: **CrO₃ 28,70% · CuO 11,17% · As₂O₅ 20,54%** (60,41% de
  ingrediente ativo).
- **Uso exclusivamente industrial, por autoclave.** Proibido em ambiente
  domiciliar e em contato com alimento humano ou animal, água potável, colmeias.
- ANVISA **Categoria 3**; IBAMA **Classe I — Alto Risco Ambiental**; produto
  corrosivo; potencial cancerígeno e teratogênico.
- Bula exige **EPI no manuseio da madeira recém-tratada por até 7 dias** e
  permanência em galpão para evitar lixiviação por chuva.
- Máscara específica para arsênio inorgânico quando o nível é desconhecido ou
  acima de **10 µg/m³** (média de 8 h).
- Retenções normativas declaradas: postes **9,6 kg/m³** (NBR 8456, UC4), mourões
  **6,5 kg/m³** (NBR 9480), dormentes **9,6 kg/m³** (NBR 7511), imersão em água
  salgada **24,0 kg/m³** (UC5).

**Ponto de curadoria:** a bula brasileira já operacionaliza o que o capítulo do
boro teve de deduzir — que a exposição relevante continua **depois** do
tratamento, no manuseio e no corte.

### 3.2 Ferrarini 2012 — classificação de resíduo (DOI 10.1590/S0100-40422012000900010)

- Lixiviação NBR 10005 em seis postes CCA retirados de serviço: **As 2,7–9,2
  mg/L**, contra limite de **1,0 mg/L** → **todos os seis reprovados**; resíduo
  **Classe I — perigoso**.
- Cromo: 0,6–6,1 mg/L, contra limite 5,0 → **só um** dos seis reprovou.
- Comparação alburno × cerne+alburno: o arsênio continua acima do limite em
  **todas** as amostras — a diluição por cerne não salva a classificação.
- Madeira retratada com **boro/flúor**: flúor lixiviado 2–61 mg/L (limite 150 →
  passa), mas **flúor solubilizado 24 e 27 mg/L contra padrão de potabilidade de
  1,5** → **Classe II-A, não inerte**. Ou seja: não é perigoso, mas **não pode ir
  para aterro inerte**.
- Ressalva metodológica registrada na ficha: pelo critério TCLP-EPA (As 5 mg/L),
  só duas amostras seriam perigosas. **Critério mais restritivo é o brasileiro.**

### 3.3 Eloy 2025 — solo sob moirões CCA, 880 dias de campo (UFSM)

- Madeira: As **−55,0%**, Cr −44,7%, Cu −52,0%.
- Solo da base: **As +129,2%** (20,2 → 46,3 mg/kg); Cr e Cu **caíram**.
- As no solo a **+32,3% acima do valor de investigação agrícola** da CONAMA
  420/2009 (46,3 contra 35 mg/kg) e +208% acima do de prevenção (15).
- Solo imediatamente sob o moirão: As **190,5% maior** que nas laterais (0–20 cm).
- Dose aplicada: **CCA-C 6,5 kg/m³**.

### 3.4 Rusch 2023 — CCB em *Dendrocalamus asper*, 5 anos de campo

A única fonte da gaveta que mede **bambu** com preservante de cobre:

- CCB **3%**: **zero** degradação biológica em 5 anos; CCB 1%: 40%; controles:
  80–100%.
- Retenção-alvo declarada: **6,5 kg/m³** (NBR 6232).
- Lixiviação nos colmos: porção **inferior (em contato com solo)** lixiviou mais
  Cu e Cr que a aérea — exceto uma anomalia em CCB 3% que os autores atribuem a
  intempérie e ao fato de analisarem só ao final.
- Solo da cova: **sem diferença significativa** entre tratado e não tratado (Cu
  CV 14%, Cr CV 66%), e os autores **explicitamente não atribuem** os metais ao
  tratamento — citam background geoquímico regional.

**Ponto de curadoria:** esta é a fonte que impede a frase fácil “CCB contamina o
solo”. O achado dela é durabilidade excelente + lixiviação concentrada na base,
**não** contaminação demonstrada do solo.

### 3.5 Scussel 2020 — lixiviado de cinzas de CCA (UFSC)

- Lixiviado de cinzas de madeira CCA: **As 59,45 mg/L** e **Cr 54,28 mg/L**,
  contra **0,70** e **0,30** nas cinzas de madeira não tratada.
- Cobre presente nas cinzas brutas, mas **não mobilizado** por água ultrapura no
  ensaio — detalhe que impede generalizar “tudo lixivia igual”.
- Toxicidade: *Artemia* CL₅₀ **24,62%** do lixiviado; efeito celular a partir de
  **2%** (MTT e cometa em NIH3T3); efeitos em *A. cepa* e *L. sativa* de 25 a
  100%.

### 3.6 Souza & Demenighi 2016 — preservantes naturais

- CCA: hidrossolúvel, desde 1930, o mais usado no mundo, **banido na UE**,
  controvérsia saúde/ambiente.
- **CCB descrito como CuSO₄ + H₃BO₃ + K₂Cr₂O₇** — ver §4.1, é divergência séria.
- Nove preservantes naturais sintetizados (mamona, neem, tall oil, capsaicina,
  cera de lima-ácida, tanino, canela, citronela/alecrim, EMX), com o veredito dos
  autores: **todos só em laboratório**; nenhum método de laboratório prevê vida
  útil em serviço com segurança; **exceto a cera de lima-ácida, todos têm problema
  de fixação/permanência** — o que a aproxima do problema do boro (§7 da gaveta
  do boro).

---

## 4. Três divergências que não podem ser harmonizadas

### 4.1 “CCB” não é o que o nome sugere

O nome corrente — *borato de cobre cromatado* — sugere borato. A fonte brasileira
custodiada (Souza & Demenighi 2016, p. 978–979) descreve o CCB como **CuSO₄ +
H₃BO₃ + K₂Cr₂O₇**, isto é, **ácido bórico**, não borato, com **dicromato de
potássio** como fonte de cromo.

**Não harmonizar.** As duas descrições circulam na literatura e na prática
comercial, e a diferença não é cosmética: ácido bórico e borato têm teores de
boro diferentes (17,5% contra ~11,3%) e solubilidades diferentes, o que muda
retenção e lixiviação. A gaveta deve **declarar a formulação cada vez que citar
um número de CCB**, e não herdar a média entre fontes.

### 4.2 Existem duas “Classe I”, e elas não medem a mesma coisa

- **Classe I do IBAMA** = risco **ambiental do produto comercial** (o Tanalith é
  Classe I).
- **Classe I da ABNT NBR 10004** = **periculosidade do resíduo** (a madeira
  retirada de serviço foi Classe I por arsênio no lixiviado).

Confundir as duas produz a frase falsa “o produto é Classe I, logo o resíduo é
Classe I”. São classificações de objetos diferentes, por critérios diferentes.

### 4.3 Arsênio no solo: dois resultados que não batem

- Eloy 2025: **As 46,3 mg/kg** sob moirão após 880 dias, **acima** do valor
  agrícola de 35.
- Jankowsky & Takeshita 2011 (citado na própria ficha de Eloy): campo de
  apodrecimento de **30 anos** com As **< 4,0 mg/kg** (uma exceção de 22,0).

Vinte e oito anos a mais de exposição e um décimo do arsênio. Os autores atribuem
a divergência a método, tempo e local. **A gaveta preserva as duas e não elege
vencedora** — mas registra que o resultado depende de método (EDXRF × digestão) e
de solo (argiloso retém), e que uma única medição de campo não fecha a questão.

---

## 5. O que a NR-15 dá — e o buraco que ela deixa

O bootstrap apostou que a NR-15 responderia as duas lacunas que ficaram zero no
boro (EPI e poeira respirável). O reprocessamento mostra que ela responde
**parcialmente**, e o mais útil é justamente o que ela **não** tem. Tudo abaixo
foi verificado no texto consolidado da NR-15 (atualização 2025) e nos anexos
custodiados em `ago_27_VOCs/NR_15/`.

### 5.1 Anexo 11 — a tabela de limites: cobre, arsênio, cromo(VI) e poeira de madeira não estão nela

O Quadro 1 do Anexo 11 (agentes químicos com limite de tolerância) foi varrido
inteiro, com normalização de espaço e acento para não perder palavra quebrada por
linha. Resultado verificado:

- **cobre: zero ocorrências.** Não há entrada para cobre, nem para “poeiras e
  névoas de cobre”;
- **arsênio inorgânico e seus compostos: zero.** A única entrada da família é
  **arsina (AsH₃), gás — 0,04 ppm / 0,16 mg/m³**, que é outro agente, outro
  estado físico e outro cenário de exposição;
- **cromo: só uma entrada, e não é a que importa.** Aparece **ácido crômico
  (névoa)**, valor máximo 0,04. Não há Cr(VI) genérico, nem cromato, nem
  dicromato — isto é, não há o agente que entra na formulação do CCA e do CCB;
- **poeira de madeira: zero.** A palavra “poeira” não aparece uma única vez nas
  978 linhas de texto do quadro;
- contraste útil: **chumbo** tem entrada própria (0,1 mg/m³). O quadro é seletivo,
  não omisso por acidente — ele lista o que lista.

Cobre aparece na NR-15 apenas no **Anexo 13** (insalubridade por *atividade*):
fundição e laminação de chumbo, zinco, cobre e latão; cobreagem e anodização de
alumínio. Cromo aparece no Anexo 13 como pigmentos, palitos fosfóricos e
**tanagem a cromo**.

**Consequência dura:** o trabalhador brasileiro que lixa bambu tratado com CCB ou
CCA **não tem, na NR-15, limite de tolerância para o agente químico que maneja**.
Não é que o limite seja alto — é que ele não existe na norma. A referência
quantitativa tem de vir de fora (NIOSH REL de 1 mg Cu/m³, já ancorado no
bootstrap) e ser **declarada como referência estrangeira**, não como norma
brasileira.

### 5.2 Anexo 12 — poeiras minerais: asbesto, manganês e sílica cristalizada

O que existe, com os valores do texto:

| Agente | Limite | Base |
|---|---|---|
| Asbesto | regime próprio (proibição de anfibólios, avaliação semestral, registro por 30 anos) | Anexo 12 |
| Manganês — poeiras | **5 mg/m³** | 8 h/dia |
| Manganês — fumos | **1 mg/m³** | 8 h/dia |
| **Sílica livre cristalizada — poeira respirável** | LT = **8 ÷ (% quartzo + 2)** mg/m³ | impactador, seletor do Quadro 1 |
| Sílica — poeira total | LT = **24 ÷ (% quartzo + 3)** mg/m³ | idem |

Aplicando a fórmula (aritmética conferida): quartzo 100% → **0,078 mg/m³**;
50% → 0,154; 10% → 0,667; 1% → 2,667 mg/m³ respirável.

### 5.3 Anexo 13 — o gancho regulatório do verniz existe, e é o isocianato

O Anexo 13 traz, textualmente, entre as atividades insalubres:

> emprego de **isocianatos** na formação de poliuretanas (lacas de desmoldagem,
> lacas de dupla composição, **lacas protetoras de madeira e metais**, adesivos
> especiais e outros produtos à base de poliisocianetos e poliuretanas).

É o único ponto da NR-15 que alcança diretamente a cadeia de **acabamento** do
bambu: verniz poliuretânico e adesivo PU ficam sob insalubridade **por atividade**,
independentemente de medição. Isso liga o capítulo do cobre ao pacote de voláteis
sem forçar a ligação — o vínculo é normativo, não editorial.

O Anexo 13 também mostra poeira vegetal entrando **por atividade** e não por
limite: “operações com bagaço de cana nas fases de grande exposição à poeira”.

### 5.4 A sílica do bambu não é o quartzo que a norma regula

A NR-15 define, no item 5 do Anexo 12: *“Sempre será entendido que ‘Quartzo’
significa sílica livre cristalizada.”*

A sílica do bambu é **fitólito: sílica biogênica amorfa hidratada**, depositada
na parede celular. Não é quartzo. Portanto:

- a fórmula do Anexo 12 **não se aplica automaticamente** à poeira de bambu
  cortado ou lixado;
- a forma **cristalina** aparece quando o material é **queimado** (cristobalita
  em cinzas e fuligem) — e aí o agente muda junto com o processo.

**Não transportar valor entre meios nem entre formas.** Dizer “bambu tem sílica,
logo vale o LT de quartzo” é exatamente o tipo de transporte que esta casa
proíbe. O que se pode afirmar: há sílica respirável no pó; a fração cristalina é
**questão de medição**, não de inferência.

### 5.5 NR-6 — o que ela exige, em estrutura

A NR-6 (atualização 2025) organiza o EPI em: campo de aplicação (6.2),
responsabilidades da **organização** (6.5), responsabilidades do **trabalhador**
(6.6), treinamentos (6.7), responsabilidades de fabricantes e importadores (6.8) e
**Certificado de Aprovação — CA** (6.9).

**O que isso resolve para a gaveta:** existe regime jurídico de EPI no Brasil, com
CA obrigatório e dever de fornecimento. **O que isso não resolve:** nenhuma
norma diz qual respirador é adequado para poeira de bambu com borato e cobre,
porque o agente não está tabelado (§5.1). A seleção fica no estudo de
risco do PGR (NR-9), não na norma de limite.

### 5.6 O que a NR-15 entrega, em uma frase

Entrega **regime de EPI** (NR-6), **gancho de insalubridade por atividade** para
isocianatos e cromo, e **limites para pó mineral**. Não entrega limite para
cobre, para arsênio inorgânico, para cromo(VI) nem para poeira de madeira ou de
bambu. O que ela tem de mais próximo é **arsina** (gás), **ácido crômico (névoa)**
e o **quartzo** da sílica — três agentes que não são os desta cadeia. **O buraco é
normativo, e agora está demonstrado — não intuído.**

---

## 6. O que o roteiro planejou e ainda não está custodiado

O `roteiro artigo.md` do pacote CCA/CCB (569 linhas, 105 ocorrências de CCA/CCB)
já contém a estrutura do capítulo e uma lista de oito downloads prioritários.
Cruzando com o disco:

| # | Documento | Status real |
|---|---|---|
| 1 | Morais et al. 2021 — revisão CCA (DOI 10.3390/ijerph18115518, CC BY) | **não custodiado** |
| 2 | Ferrarini et al. 2012 | **custodiado e fichado** |
| 3 | Eloy et al. 2025 | **custodiado e fichado** |
| 4 | Rusch et al. 2023 | **custodiado e fichado** |
| 5 | Toxicidade de efluente de cinza de CCA (2022, open access) | **não custodiado** |
| 6 | Ibama 2024 — Tanalith 60% CCA-C | **custodiado e fichado** |
| 7 | UFSC — lixiviado de cinzas (Scussel) | **custodiado e fichado** |
| 8 | Souza & Demenighi 2016 | **custodiado e fichado** |

Além dos oito, o roteiro cita e **não** custodia, e cada um sustenta uma afirmação
que hoje está no texto sem fonte primária nesta gaveta:

- **Khan et al. / estudo de playground em Toronto** — solo sob estruturas
  infantis: média 20,3 µg As/g (12,4–47,5) contra 2,1 µg/g a 1 m;
- **biomonitoramento de trabalhadores uruguaios de CCA** — 96% das amostras
  urinárias abaixo do valor ocupacional, mas associação significativa com
  fatores de risco do trabalho;
- **exposição em marcenarias (joinery shops)** — arsênio no ar de **0,54 a 3,1
  µg/m³** ao redor de máquinas trabalhando madeira impregnada; Cr(VI) não
  detectado nas amostras;
- **queima aberta de CCA** — **11–14% do arsênio** emitido à atmosfera; <1% de Cr
  e Cu; **80–90% do As na cinza volante como As(III)** em partícula respiratória;
- **lixiviação de CCB por meio (2004)** — perda relativa **B 11,2–63,5%** contra
  **Cr 0,02–0,36%**;
- **normas**: ABNT NBR 10004-1/-2:2024 (substituem a edição 2004), PNRS/Decreto
  10.936/2022, Portaria MMA 280/2020 (MTR/SINIR), CONAMA 307/2002, Basileia
  Y5/A4040, EU REACH Anexo XVII, APVMA (Austrália), EPA-NZ.

**Nenhuma dessas seis primeiras pode ser citada como fato ancorado** nesta gaveta
até ser custodiada. Hoje elas são pista de busca, não fonte.

---

## 7. Ordem de ataque recomendada

O reprocessamento muda a prioridade. Em ordem:

1. **Custodiar os três ocupacionais** que são o núcleo das lacunas 1 e 2 do
   bootstrap: exposição em marcenaria (arsênio no ar de 0,54–3,1 µg/m³),
   biomonitoramento uruguaio e revisão Morais 2021 (CC BY, texto integral). São
   acesso aberto — custódia por `curl` + extração local.
2. **Fechar a norma de resíduo**: ABNT NBR 10004-1/-2:2024 substituiu a edição
   de 2004 usada por Ferrarini. Sem isso, toda afirmação de classificação do
   capítulo fica presa a norma revogada. (Acesso ABNT é pago — declarar como
   bloqueio se não houver via legítima.)
3. **Custodiar o CCB por meio** (lixiviação 2004) — é o número que sustenta o
   mecanismo “B móvel, Cr fixo” do roteiro §9, hoje sem fonte nesta gaveta.
4. **Só depois** importação brasileira de cobre e de madeira tratada por NCM
   (lacuna 7 do bootstrap), reaproveitando o método ComexStat já validado e
   custodiado na gaveta do boro.
5. **Por último** o eixo de voláteis/isocianatos como capítulo próprio — o
   material está custodiado, mas o objeto é outro agente e merece régua própria.

---

## 8. O que este mapa não autoriza concluir

- **Não** autoriza dizer que o CCB contamina o solo: Rusch 2023 **não** encontrou
  diferença significativa e explicitamente não atribui os metais ao tratamento.
- **Não** autoriza dizer que madeira CCA é Classe I: a classificação de um resíduo
  concreto depende da NBR 10004-1/-2:2024 e de caracterização. O que há é
  evidência experimental forte (Ferrarini) de que **pode** ser.
- **Não** autoriza transportar o limite de sílica cristalizada para poeira de
  bambu (§5.4).
- **Não** autoriza tratar “isocianato é insalubre por atividade” como se
  quantificasse exposição: o Anexo 13 dispensa medição, o que é o oposto de
  medi-la.
- **Não** autoriza afirmar nada sobre exposição de trabalhador **de bambu** com
  cobre: as fichas custodiadas medem madeira, solo, cinza e lixiviado — nenhuma
  mede trabalhador.
- **Não** é homologação: as seis fichas seguem `ficha-em-revisao`.

---

## 9. Referências documentais e custódia

- **Fichas** (privadas, integralmente conferidas contra PDF):
  `_privado/fichas/ago_28_CCA_CCB/` — seis arquivos, 94.801 bytes.
- **Fontes CCA/CCB** (privadas): `_privado/fontes-documentais/ago_28_CCA_CCB/` —
  seis PDFs com `.canonical.txt`, `.md` e `manifest/manifest_sha256.csv`.
- **NR-15** (consolidada 2025) e **anexos 1, 2, 5, 6, 11, 12, 13, 13-A, 14**;
  **NR-6** (atualização 2025) — `_privado/fontes-documentais/ago_27_VOCs/NR_15/`.
  Texto extraído nesta rodada para
  `_privado/governanca-operacional/extracoes/cobre/textos_nr/` (13 arquivos).
- **Roteiro intelectual do capítulo**: `roteiro artigo.md` (569 linhas) no pacote
  CCA/CCB — é planejamento, **não** fonte.
- **Bootstrap de origem**: `docs/analyses/boro/BOOTSTRAP_COBRE_20261124.md`
  (sha256 948b91110de0acc4), que permanece na gaveta do boro como documento de
  ligação entre as duas frentes.

---

**Controle de fronteiras.** Inventário medido no disco, separado de síntese das
fichas (§3), de divergências preservadas (§4) e de limites (§8). Números citados
têm fonte nomeada; nenhum foi transportado do capítulo do boro. Onde a norma não
tem valor, está escrito que não tem. Estado: **em-revisao-documental**; não
homologado; não é certificação nem autorização de publicação.
