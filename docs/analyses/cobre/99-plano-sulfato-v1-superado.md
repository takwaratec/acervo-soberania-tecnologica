---
schema: ACERVO_PLANO_ESPECIFICO_R1
gaveta: cobre
frente: COBRE
titulo: "Plano específico — SULFATO DE COBRE: o que é, como age, riscos, normas, fiscalização e o problema das duas dosagens"
estado_documental: em-revisao-documental
homologacao_automatica: false
versao: 1
data_revisao: 2026-11-24
responsavel_curadoria: Fabio Takwara
assistencia_documental: agente de IA, sujeito a revisao humana
complementa: 01-plano-de-pesquisa.md (plano do ELEMENTO, sete rodadas E1-E7)
---

# Plano específico — sulfato de cobre

> **Por que este documento existe.** O plano do elemento (E1–E7) cataloga o cobre.
> O soberano apontou o composto que **de fato se usa**: o **sulfato de cobre**, e
> pediu sete perguntas específicas — o que é, de onde vem, como age, riscos,
> literatura, legislação e proibições, o que está fora de conformidade no Brasil, o
> que a Anvisa regula, se há fiscalização, e **qual a diferença entre dosagem de
> remédio e dosagem de veneno**. Este documento responde onde já há dado custodiado
> ou medido, e converte o resto em rodadas.
>
> **O que ele NÃO é.** Não é ficha do sulfato de cobre, nem capítulo. É o plano que
> a auditoria vai julgar — com o que já está verificado separado do que ainda é
> pergunta.

---

## 1. Identidade do composto — o que já se pode afirmar

**CuSO₄·5H₂O** — sulfato cúprico penta-hidratado (o "sulfato de cobre" comercial é
quase sempre este; o anidro existe e é outro NCM). **Teor de cobre: ~25,4% em massa**
(63,55 g/mol de Cu em 249,68 g/mol do sal pentahidratado), e ~39,8% em base anidra.

**NCM brasileiro:** `2833.25` desdobrado em **28332510 (sulfato cuproso)** e
**28332520 (sulfato cúprico)**.

**A conversão que o capítulo inteiro depende:** todo número de sulfato de cobre
precisa declarar se está em **sal** ou em **cobre elementar**. Um número em sal
dividido por ~4 dá o cobre contido. Confundir os dois é erro de fator 4 — e é o mesmo
tipo de erro que a gaveta do boro corrigiu entre DOT e B₂O₃.

---

## 2. Medido nesta rodada — comércio brasileiro de sulfato de cobre

Consulta direta à API ComexStat, NCM 28332510 + 28332520, série 1997–2026.

### 2.1 Série histórica (importação)

| Ano | kg | US$ FOB | US$/kg |
|---|---:|---:|---:|
| 1997 | 1.279.269 | 1.292.541 | 1,01 |
| 2001 | 446.373 | 432.948 | 0,97 |
| 2006 | 118.525 | 222.111 | 1,87 |
| 2010 | 57.040 | 159.170 | 2,79 |
| 2015 | 25.206 | 78.011 | 3,09 |
| 2020 | 9.350 | 95.954 | 10,26 |
| 2022 | 332.456 | 929.708 | 2,80 |
| 2024 | 202.238 | 680.288 | 3,36 |
| 2025 | **177.854** | **370.053** | **2,08** |
| 2026* | 86.640 | 385.145 | 4,45 |

\* parcial (jan–out). **A série é volátil e caiu ~86% entre 1997 e 2020**, com
repiques em 2022 e 2024. Volatilidade dessa magnitude em um único composto sugere
compra por lote/contrato, não consumo estável — **hipótese, não afirmação**.

### 2.2 Origem em 2025

| Origem | t | US$ FOB | % |
|---|---:|---:|---:|
| China | 143,0 | 180 mil | **48,3%** |
| Peru | 27,0 | 70 mil | 20,0% |
| Estados Unidos | 1,3 | 60 mil | 16,6% |
| Itália | 2,0 | 20 mil | 4,7% |
| Polônia | 3,0 | 10 mil | 3,5% |

**Total 2025: 177,9 t por US$ 370 mil.** O preço médio de **US$ 2,08/kg** é
incompatível com sulfato de cobre técnico a granel (que custa centavos de dólar por
quilo) — o que sugere que a pauta de importação deste NCM concentra **produto
formulado, grau reagente ou embalado**, não commodity. **Hipótese declarada, a
verificar na NCM/Receita.**

### 2.3 O contraste que importa para a pergunta do soberano

Importação de sulfato de cobre em 2025: **177,9 t**.
Importação de **cátodos de cobre refinado** no mesmo ano: **254.300 t** (US$ 2,47
bilhões). Exportação brasileira de **minério de cobre e concentrado (NCM 2603)**:
**1.451.750 t** (US$ 5,01 bilhões).

**Leitura, e ela é grande:** o Brasil **exporta 1,45 milhão de toneladas de minério
de cobre e importa 178 toneladas de sulfato**. A razão entre o que sai como minério e
o que entra como sal pronto é de **~8.000 para 1** em massa. Isso é o padrão
clássico de economia primário-exportadora: **vende a rocha, compra o reagente**. É a
assimetria que a rodada E7 do plano do elemento ia medir — e ela apareceu antes,
como subproduto.

*(Ressalva: o sulfato de cobre consumido no Brasil também pode ser produzido
internamente a partir de cobre metálico ou de sucata; a importação não mede consumo.
Não há, nesta gaveta, dado de produção nacional de sulfato de cobre.)*

---

## 3. As sete perguntas do soberano, convertidas em rodadas

### S1 · O que é, de onde vem, como age

**Pergunta:** qual é a química do sulfato de cobre — solubilidade, dissociação, o que
ele faz no substrato — e de onde vem o cobre que entra nele?

**Ataca:** a §1 acima só dá a fórmula e o teor. Falta o **mecanismo de ação
fungicida**: o Cu²⁺ livre desnatura proteínas e enzimas do fungo, interfere em
processos de membrana, e é **fungistático ou fungicida conforme concentração** — a
mesma dualidade da §6.

**Fonte:** literatura de proteção de madeira e de fungicidas cúpricos; química de
especiação (o cobre só é tóxico como íon disponível, não como sal precipitado).

**Critério de fracasso:** se a rodada não conseguir separar "mata o fungo" de
"impede o fungo de crescer", ela não responde a pergunta do soberano e falhou.

### S2 · Riscos — humano, ambiental, ocupacional

**Pergunta:** qual é o risco real do sulfato de cobre em cada via e em cada meio?

**Já ancorado (plano do elemento §2):** LD₅₀ oral rato **790 / 450 mg/kg**;
irritação ocular grave até 21 dias; NOAEL humano **2 mg Cu/L**; invertebrado
aquático **1,11–2,05 µg/L**; CONAMA 357 **9 µg/L**; efluente **1,0 mg/L**;
potabilidade **2 mg/L**; NIOSH **1 mg Cu/m³**; **NR-15 sem limite para cobre**.

**Falta:** cadeia toxicológica completa (E3) e a dependência de matriz da
ecotoxicidade (E4). **Sem essas duas, o risco fica em números soltos.**

### S3 · Literatura

**Pergunta:** o que a literatura científica consolidada diz do sulfato de cobre como
preservante e como fungicida agrícola?

**Fonte:** revisões indexadas; a base de proteção de madeira (AWPA, IRG) e a base
agronômica (fitopatologia, calda bordalesa) são **corpos literários diferentes** que
usam o mesmo sal para fins diferentes — e é isso que a §5 explora.

**Critério de fracasso:** se a rodada só encontrar literatura de um dos dois campos,
ela declara o outro como não coberto.

### S4 · Legislação, regras e proibições em outros países

**Pergunta:** onde o sulfato de cobre é **permitido**, **restrito** e **proibido** —
e com que fundamento?

**Ataca:** a pergunta mais bem definida do lote e a de maior risco de bloqueio.
Sulfato de cobre é **agrotóxico registrado** na maioria das jurisdições e **produto
preservante de madeira** em outra classificação — dois regimes, e é comum um país
proibir em um uso e permitir no outro.

**Cobertura pretendida:** União Europeia (o cobre e seus compostos têm status próprio
no BPR — regulamento de biocidas — e o sulfato de cobre é substância ativa aprovada
com restrições por tipo de produto); Estados Unidos (EPA, registro como pesticida e
como preservante); Austrália (APVMA); Brasil (Ibama para preservante de madeira,
Anvisa e MAPA para agrotóxico — **três agências, três registros**).

**Critério de fracasso:** se o acesso a Eur-Lex/ECHA continuar bloqueado (HTTP 202
por WAF, como na gaveta do boro), a gaveta declara **bloqueio por jurisdição** e não
preenche por analogia.

### S5 · O que está fora de conformidade no Brasil

**Pergunta:** onde o uso brasileiro de sulfato de cobre opera **fora** da norma
vigente?

**Estado: não medido — e este é o ponto mais delicado do plano.** Afirmar "está fora
de conformidade" exige (a) a norma, (b) a prática, e (c) a comparação. A gaveta tem
**nenhuma das três** para o sulfato de cobre hoje.

**O que já se pode dizer com fonte:** a NR-15 **não tem limite de tolerância para
cobre** (§2 do plano do elemento) — o que não é "fora de conformidade", é **ausência
de parâmetro nacional**. São coisas diferentes, e a gaveta não pode confundi-las.

**Fonte a buscar:** registros do Ibama para preservativos de madeira (a lista de
produtos registrados, como a que instruiu a ficha Tanalith do CCA); registros do
MAPA/Anvisa para agrotóxicos à base de cobre; autuações publicadas.

**Critério de fracasso:** se não houver acesso a registro nem a autuação, a rodada
declara **"não foi possível estabelecer conformidade"** — e nunca "está irregular".

### S6 · Anvisa e fiscalização

**Pergunta:** o que a Anvisa regula no sulfato de cobre, e quem efetivamente fiscaliza
o quê?

**Fonte:** atos da Anvisa aplicáveis a saneantes, antissépticos e produtos de uso em
água; a divisão de competência com Ibama (preservante de madeira), MAPA (agrotóxico)
e Ministério do Trabalho (NR-15/NR-6).

**O que a rodada deve deixar claro:** **Anvisa não é a agência do sulfato de cobre
como preservante de madeira.** Se isso se confirmar, o achado é que o produto cai em
**vácuo de competência declarada** — e isso é afirmação forte, que exige a fonte de
cada agência, não a ausência de uma.

### S7 · A pergunta central: dosagem de remédio × dosagem de veneno

**Pergunta:** por que a mesma substância é remédio em uma dose e veneno em outra — e
onde exatamente ficam as duas fronteiras no caso do cobre?

**Este é o núcleo do capítulo**, e não é retórica: é farmacologia.

- **Remédio:** o cobre é **micronutriente essencial**. A dose diária recomendada é da
  ordem de **~1 mg/dia** em adulto (a confirmar com fonte); a deficiência causa
  anemia e neutropenia. Existe faixa terapêutica.
- **Veneno:** acima da faixa, o mesmo íon causa náusea (LOAEL **4 mg Cu/L**), vômito
  (≥**6 mg Cu/L**), e em exposição aguda massiva, hemólise e falência hepática.
- **A fronteira:** o NOAEL de **2 mg Cu/L** na água é a linha entre "tolerável" e
  "efeito". O número não é do remédio nem do veneno — é o ponto onde a curva vira.

**A segunda fronteira, que o soberano não pediu e é a que importa para o bambu:** a
dose que **inibe fungo** não é a dose que **mata fungo**, e nenhuma das duas é a dose
que **mata o operador**. São **três curvas diferentes** na mesma substância:

1. **Dose fungistática** — inibe o crescimento (kg/m³ de madeira);
2. **Dose fungicida** — mata o fungo (kg/m³ de madeira);
3. **Dose tóxica ao humano** — mg Cu/kg de massa corporal.

**A conversão entre (1)/(2) e (3) exige passar por massa de madeira tratada, área
exposta, forma química e via.** É exatamente o transporte entre meios que esta casa
proíbe — e é por isso que o capítulo precisa das três separadas, não de uma tabela
única.

**Critério de fracasso:** se a rodada entregar uma tabela que compare as três
grandezas sem unidades separadas, falhou por definição.

---

## 4. Uso agrícola × uso preservante — a proporção que o soberano perguntou

**A pergunta:** o sulfato de cobre é usado na agricultura? Em que proporção, comparado
ao uso como inibidor de fungo em madeira?

**Estado: não medido, e é medível.** O que se sabe e o que falta:

| Uso | Papel do cobre | Registro/domínio | Proporção |
|---|---|---|---|
| **Agricultura** | fungicida (calda bordalesa), micronutriente | MAPA / Anvisa — agrotóxico e fertilizante | **a medir** |
| **Preservante de madeira** | fungicida e inseticida | Ibama — preservativo | **a medir** |
| **Outros** (algicida em água, reagente, alimentação animal) | diversos | diversos | **a medir** |

**Como medir sem inventar:** o consumo brasileiro de cobre por segmento **não é
publicado por NCM** — o ComexStat mede comércio, não destino. As vias reais são
(a) dados de associação setorial (Andrada, Abisolo, sindicatos de preservação de
madeira), (b) registros de agrotóxico do MAPA por ingrediente ativo, (c) relatórios
da USGS sobre uso final **mundial** do cobre — que dão a fatia de "agricultura" e de
"preservante de madeira" no mundo, e por isso são **ordem de grandeza global**, não
fato brasileiro.

**Proibição de transporte:** a fatia mundial **não pode** ser aplicada ao Brasil como
se fosse medição nacional. É a mesma regra que a gaveta do boro aplicou à USGS.

---

## 5. O que este plano não autoriza

- **Não** autoriza afirmar proporção de uso agrícola vs preservante no Brasil: não
  foi medido e o ComexStat não mede destino.
- **Não** autoriza dizer que há uso "fora de conformidade" no Brasil: ausência de
  limite na NR-15 **não é** irregularidade — é ausência de parâmetro (S5).
- **Não** autoriza atribuir à Anvisa a regulação do sulfato de cobre como preservante
  de madeira sem fonte por agência (S6).
- **Não** autoriza comparar dose de remédio, dose de veneno e dose de preservação em
  uma tabela única (S7).
- **Não** autoriza converter sal em cobre elementar sem declarar o fator (§1).
- **Não** autoriza estender ao **bambu** nada do que se medir em madeira: a etapa de
  fichas de produto é outra.
- **Não** é homologação.

---

## 6. Ordem proposta

**S7 → S1 → S2 → S4 → S5 → S6 → S3**

S7 primeiro porque é a pergunta que o soberano fez e porque estrutura o capítulo.
S1 e S2 dão química e risco. S4 antes de S5/S6 porque sem a norma não há como medir
conformidade. S3 por último: literatura consolida o que as outras acharam.

---

**Controle de fronteiras.** Medido (§2) separado de plano (§3–§4) e de limite (§5).
Todo número de §2 vem da API oficial com consulta reproduzível. As hipóteses sobre
pauta de importação estão marcadas como hipóteses. Estado: **em-revisao-documental**;
não homologado.
