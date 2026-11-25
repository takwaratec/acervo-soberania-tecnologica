---
schema: ACERVO_PLANO_PESQUISA_R1
gaveta: cobre
frente: COBRE
titulo: "Plano de pesquisa e varredura de repositorio — frente COBRE"
estado_documental: em-revisao-documental
homologacao_automatica: false
versao: 1
data_revisao: 2026-11-24
responsavel_curadoria: Fabio Takwara
assistencia_documental: agente de IA, sujeito a revisao humana
artefato_anterior: 00-mapa-reprocessamento.md
destinacao: "objeto de auditoria interna (Teco/Luna) antes da execucao de P1-P6"
tipo_documental: instrumento-de-pesquisa
---
# Plano de pesquisa e varredura — frente COBRE

> **Síntese.** Este documento existe para ser **atacado**. Ele declara o que a
> frente COBRE pretende pesquisar, em que ordem, com que orçamento, e o que vai
> medir para decidir se a rodada funcionou. Declara também **o que já foi
> varrido** — incluindo as varreduras que o plano anterior não previa e que
> mudaram o resultado (§2). A parte mais desconfortável está na §2.3: o material
> custodiado que o mapa anterior tratou como lacuna parcial está, em parte,
> **errado por três ordens de grandeza**, e isso só foi descoberto porque a
> varredura de quarentena foi feita.

---

## 0. O que este plano NÃO é

Não é pedido de aprovação. Não é homologação. Não é promessa de que as seis
rodadas vão produzir o que se espera delas. É a hipótese de trabalho com data de
validade — e o auditor tem autoridade para dizer que a ordem está errada, que
uma rodada é dispensável, ou que falta a rodada que ninguém propôs.

---

## 1. Onde a frente está, em números verificados

| Conjunto | Estado | Volume |
|---|---|---|
| Fichas herdadas CCA/CCB | `ficha-em-revisao`, nenhuma homologada | 6 fichas, 94.801 B |
| Fontes CCA/CCB | custodiadas com PDF + canonical + md + manifest | 6 PDFs, 9,6 MB |
| Pacote ocupacional/voláteis | custodiado, **não fichado** | 45 arquivos, 38 PDFs, 137,2 MB |
| NR-15 + NR-6 | texto extraído nesta frente | 13 textos, 486.657 B |
| Varredura de repositório (§2) | executada nesta rodada | 1.765 textos, 1.563 com acerto |

---

## 2. Varredura de repositório — executada, com resultado

O bootstrap mandava reprocessar o que existe. O mapa anterior reprocessou as seis
fichas e os normativos, e **parou ali**. Esta rodada varreu também as raízes que o
bootstrap listava como "onde procurar material ignorado", e o resultado foi
desigual em três sentidos:

| Raiz | Existe? | Textos varridos | Com material de bambu/tratamento |
|---|---|---|---|
| `_privado/fontes-documentais/ago_28_Boratos_Cobre` | sim (26 arq.) | 13 | 13 |
| `_privado/fontes-documentais/ago_28_CCA_CCB` | sim (22 arq.) | 15 | 15 |
| `_privado/fontes-documentais/ago_28_Saneamento` | sim (49 arq.) | 27 | 27 |
| `_privado/fontes-academicas/2020-gauss-*` | sim (4 arq.) | 2 | 2 |
| `_privado/FRENTES_AGENDADAS` | sim (281 arq.) | — | 0 relevantes (**falso positivo**: CIMI/povos indígenas acerta "boro" por ruído de OCR) |
| `_privado/acervo-autoral-fabio-takwara` | sim (50 arq.) | — | 0 relevantes |
| `docs/analyses/bambu-estrutural` | sim (74 arq.) | 107 (com `docs/`) | já publicado |
| `_quarentena/` | sim (1.861 arq.) | **1.043** | **1.043** |
| `_quarentena_old/` | sim (168 arq.) | 167 | 167 |
| `arquivo_historico/` | sim (13 arq.) | 11 | 11 |
| **`_privado/governanca-operacional/extracoes/`** | sim (**14.682 arq.**) | **não varrido** | — |

**Total:** 1.765 textos legíveis varridos; 1.563 com acerto de bambu + tratamento.
A raiz maior — 14.682 arquivos de extrações anteriores — **não foi varrida**, e
isso é limite declarado, não omissão silenciosa.

### 2.1 O que a varredura encontrou de substantivo

- **`_quarentena/02_bambu-estrutural-e-tratamentos_04_Tratamentos/`** contém
  quatro documentos de tratamento nunca incorporados à gaveta:
  `BAM_TRA_001--tratamentos-christian-gauss-2023.md` (161 acertos),
  `BAM_TRA_002--effects-heat-treatment-bamboo.md`,
  `BAM_TRA_003--tratamento-termico-integrado-madeira-bambu.md` (253),
  `BAM_TRA_004--embrapa-circular65-2007.md`.
- **`_quarentena/ifb/ifb-boron-greenfacts.md`** e três duplicatas em
  `_quarentena/_duplicatas/` — material de toxicidade do boro em **português**,
  classe de fonte que a gaveta do boro não possui.
- **IARC Volume 62** (*Wood Dust and Formaldehyde*, 1995), 423 páginas,
  custodiado em `ago_27_VOCs` e nunca fichado — ver §4.

### 2.2 Falsos positivos que a varredura produziu, e que não devem ser corrigidos

`_privado/FRENTES_AGENDADAS/ago_29_Povos_Indigenas/` aparece com 46–88 acertos de
"boro" por arquivo. Não é boro químico: é ruído de OCR sobre texto do CIMI.
**Registrar e descartar**, não investigar.

### 2.3 O achado que muda o plano

Em `_quarentena/revisao-cientifica-2026-07-14/tecnologia-takwara/` existe uma ficha
de autoria do próprio acervo — **TT-FT-002, "Crítica Ambiental aos Tratamentos
Químicos do Bambu"** — que trata exatamente do objeto desta gaveta e afirma
números de importação de boro. Esses números, conferidos contra o ComexStat já
custodiado nesta casa, estão errados por **14× a 103×** e a origem geográfica está
**invertida**. A conferência completa está na §5; ela existe aqui porque muda a
prioridade de P5.

---

## 3. Plano de pesquisa — seis rodadas, em ordem de ataque

Cada rodada declara: o que ataca, com que fonte, o que mede, e **qual é o
critério de fracasso** — isto é, o resultado que faria a rodada ser descartada em
vez de contornada.

### P1 · Exposição ocupacional do tratamento de cobre (prioridade máxima)

**Ataca:** a lacuna que ficou zero no boro e que continua zero no cobre —
trabalhador exposto a poeira de madeira/bambu tratado com CCA, CCB ou sulfato de
cobre.

**Fontes a custodiar** (todas de acesso aberto, custódia por `curl` + extração
local):

1. Exposição ocupacional a cromo, cobre e arsênio em marcenarias que trabalham
   madeira impregnada — arsênio no ar de **0,54 a 3,1 µg/m³**, Cr(VI) não
   detectado nas amostras (PubMed 1444070).
2. Biomonitoramento de arsênio em trabalhadores uruguaios de CCA — 96% das
   amostras urinárias abaixo do valor ocupacional, com associação significativa
   a fatores de risco do trabalho (PMC6060846).
3. Morais et al. 2021, revisão *Environmental and Health Hazards of CCA-treated
   wood* (DOI 10.3390/ijerph18115518, CC BY, texto integral em PMC8196618).

**O que mede:** concentração de arsênio/cobre/cromo no ar em ambiente de
beneficiamento; correlação com uso de EPI; se existe algum estudo que meça
**bambu** e não madeira.

**Critério de fracasso:** se as três fontes somadas não contiverem nenhuma
medição de exposição ocupacional em beneficiamento de madeira tratada com dado
numérico de concentração, a rodada falhou e a lacuna continua declarada sem
régua.

**O que a rodada não entrega:** exposição em bambu. Nenhuma das três mede bambu.
A transferência de madeira para bambu é **analogia declarada**, não medição.

### P2 · Norma de resíduo vigente (prioridade alta, risco de bloqueio)

**Ataca:** a classificação de resíduo de madeira tratada está ancorada na ABNT
NBR 10004:**2004**, que foi substituída pela **NBR 10004-1:2024** (requisitos de
classificação) e **NBR 10004-2:2024** (SGCR). Ferrarini 2012 classificou CCA como
Classe I pela edição de 2004.

**Fonte:** ABNT, catálogo oficial.

**Risco declarado:** ABNT é **pago**. Não há via legítima de custódia gratuita. Se
não houver acesso, a rodada **não fecha** e a gaveta passa a declarar
explicitamente: *"a classificação do capítulo usa norma substituída; a norma
vigente não foi consultada"*. Isso é pendência honesta, não contorno.

**Critério de fracasso:** não conseguir nem o texto da norma nem a declaração de
que ela existe e o que mudou. Nesse caso o capítulo **não pode afirmar
classificação de resíduo** e passa a citar a classificação apenas como resultado
de Ferrarini sob a norma de 2004.

### P3 · Mecanismo de lixiviação do CCB (prioridade alta)

**Ataca:** o número que sustenta "boro móvel, cromo fixo" no CCB está no roteiro
intelectual do pacote (`roteiro artigo.md`, §9) e **não está custodiado** nesta
gaveta. O roteiro cita perda relativa de **B 11,2–63,5%** contra **Cr 0,02–0,36%**
em ensaio com água ultrapura, água de chuva e água de solo (PubMed 15559284).

**Fonte:** estudo de lixiviação de CCB por meio, 2004.

**Critério de fracasso:** se o estudo não tiver os percentuais por elemento e por
meio, o mecanismo fica **sem número** e a gaveta passa a descrevê-lo
qualitativamente, sem a tabela.

### P4 · Exposição real em oficina de bambu (prioridade média — provável
lacuna persistente)

**Ataca:** poeira respirável, sílica e metais em beneficiamento de **bambu
tratado** — o que a §9.4 da gaveta do boro tratou por conta de teto.

**Fonte:** busca dirigida em base indexada por estudos de poeira em
beneficiamento de bambu, com e sem tratamento.

**Critério de fracasso:** não encontrar nenhum estudo com medição de poeira
respirável em oficina de bambu — o que é o desfecho **provável**. Nesse caso a
lacuna é declarada como **lacuna de campo**, não de literatura, e a gaveta passa a
recomendar medição própria em vez de citar análogo.

**Nota de custódia:** a sílica do bambu é fitólito amorfo; o limite da NR-15 é de
quartzo cristalino. Medir uma e citar a outra é o transporte que a casa proíbe.

### P5 · Importação brasileira de cobre e de madeira tratada (prioridade média)

**Ataca:** a lacuna 7 do bootstrap. Reaproveita o método ComexStat já custodiado
na gaveta do boro (API oficial, extração ano a ano, `metricKG` = peso de produto,
não de elemento).

**Escopo:** NCM de sulfato de cobre e de compostos de cobre; NCM de madeira
tratada. **Não** repete a extração de boro.

**Critério de fracasso:** se os NCM de madeira tratada não isolarem madeira
tratada de madeira comum, a rodada entrega importação de **químico**, não de
**produto tratado**, e o número não pode ser usado para estimar volume tratado.

### P6 · Voláteis e isocianatos (prioridade baixa nesta gaveta — candidata a cisão)

**Ataca:** o eixo de acabamento. Material já custodiado: 38 PDFs, incluindo NR-15
Anexo 13 (isocianatos em lacas protetoras de madeira), OSHA, IARC, biomonitoramento
de diisocianatos.

**Estado do material após varredura:** a IARC Volume 62 (*Wood Dust and
Formaldehyde*, 1995) está custodiada e é a **única classificação carcinogênica de
poeira de madeira** que a gaveta possui — Grupo 1, com adenocarcinoma de cavidade
nasal em trabalhadores de mobiliário. Isso é material de **P1**, não de P6.

**Recomendação de cisão:** os voláteis são **outro agente**. Manter na gaveta do
cobre só se a pergunta for "o que a cadeia de acabamento faz com quem aplica" —
que é pergunta legítima, mas de outro capítulo. **Recomendo cisão**, e a decisão é
do soberano.

**Critério de fracasso de P6 nesta gaveta:** se a rodada não conseguir articular
o isocianato ao objeto *cobre* sem mudar de assunto, então a cisão está provada
por construção e não por opinião.

---

## 4. O que a varredura mudou no plano

Quatro achados que **não estavam** no mapa anterior:

1. **IARC Volume 62 (*Wood Dust and Formaldehyde*, 1995) está custodiada** em
   `ago_27_VOCs` e nunca foi fichada. É a classificação Grupo 1 para poeira de
   madeira — a régua que faltava para P1. O mapa anterior tratou `ago_27_VOCs`
   como "ocupacional/voláteis"; ele contém a monografia clássica de poeira de
   madeira.
2. **`_quarentena/` tem 1.043 arquivos** com material de tratamento de bambu, 22
   com cinco ou mais menções a boro — inclusive uma **ficha crítica do próprio
   acervo** (TT-FT-002) sobre tratamentos químicos do bambu, com números de
   importação e de volume de químicos.
3. **Essa ficha em quarentena está errada por ordens de grandeza**, e isso é
   verificável contra o ComexStat já custodiado nesta casa (§5).
4. **`_quarentena_old/` (167 arquivos) e `arquivo_historico/` (13) nunca foram
   varridos** pela gaveta do boro nem por esta.

---

## 5. Controle negativo: os números da ficha TT-FT-002 contra o ComexStat

A ficha em quarentena (`_quarentena/revisao-cientifica-2026-07-14/
tecnologia-takwara/ficha-critica-tratamento-quimico-bambu.md`) é material **do
próprio acervo**, não fonte externa. Ela afirma:

| Afirmação da ficha | Medido no ComexStat custodiado | Razão |
|---|---|---|
| "Bórax 35.408 t (2000–2025)" | bórax importado 2000–2025: **520.071 t** | ficha é **14,7× menor** |
| "Ácido bórico 23.606 t (2000–2025)" | ácido ortobórico importado: **1.025.894 t** | ficha é **43,5× menor** |
| "Total 59.014 t de químicos" | importação total de produtos de boro: **6.077.383 t** | ficha é **103× menor** |
| "Turquia 78% / EUA 15% / Chile-Argentina 7%" | Argentina 34,2 · Bolívia 22,8 · Chile 16,7 · **Turquia 14,1** · EUA 5,9 | origem **invertida** |
| "Importação US$ 45,6 M/ano (MDIC 2023)" | só NCM de boro em 2023: **US$ 154,3 M** | universo da ficha é menor |
| "Brasil não possui reservas de boro" | USGS não lista o Brasil — ausência na fonte ≠ zero | indevido |

**O que isso significa para o plano:** se essa ficha for publicada sem correção,
o acervo afirma um número de contaminação por boratos que é **1/103 do volume
realmente importado** — e uma origem geográfica invertida. O erro não é pequeno e
não é conservador: ele **subestima** a importação e **inverte** a dependência. É
o tipo de número que, corrigido, muda a conclusão do capítulo.

**Consequência para P5:** a rodada de importação deixa de ser "lacuna 7,
prioridade média" e passa a ser **necessária para não herdar erro do próprio
acervo**. Recomendo elevá-la a prioridade alta.

---

## 6. Orçamento e ordem proposta

| Rodada | Fontes a custodiar | Custo estimado | Bloqueio provável |
|---|---|---|---|
| P1 | 3 (acesso aberto) | 1 rodada de custódia | nenhum |
| P2 | 1 (ABNT, pago) | 0 se sem acesso | **acesso pago** |
| P3 | 1 (PubMed) | 1 rodada | nenhum |
| P4 | busca dirigida | 1 a 2 rodadas | provável ausência de literatura |
| P5 | API ComexStat | 1 rodada | nenhum (método pronto) |
| P6 | já custodiado | 1 rodada de fichamento | decisão de cisão |

**Ordem que eu proponho:** P1 → P5 → P3 → P2 → P4 → P6.
P5 sobe de posição por causa da §5. P2 vai depois porque o bloqueio é conhecido e
não impede as outras.

---

## 7. O que este plano não autoriza

- **Não** autoriza publicar nada do cobre: nenhum resultado, nenhuma ficha, nenhum
  número novo.
- **Não** autoriza tratar a analogia madeira→bambu como medição.
- **Não** autoriza corrigir a ficha TT-FT-002 por conta própria: ela está em
  `_quarentena/`, fora do escopo de escrita desta frente. A correção exige ato
  próprio.
- **Não** autoriza concluir que a varredura de repositório está completa: 1.765
  textos foram varridos; `_privado/governanca-operacional/extracoes/` tem 14.682
  arquivos e **não** foi varrido integralmente.
- **Não** é homologação.

---

**Controle de fronteiras.** Varredura medida (§1, §2, §4) separada de plano
declarado (§3) e de limite (§7). Todo número de §5 vem de arquivo custodiado nesta
casa com caminho nomeado; a comparação é aritmética reproduzível. Estado:
**em-revisao-documental**; não homologado; sujeito a auditoria interna.
