# Gaveta — boro

Frente `BORO` (aberta 2026-11-24 no ledger R4).
Capítulo sobre **o elemento boro** — não sobre fichas de tratamento.

## Escopo desta gaveta

Entra: **o elemento boro e seus sais** — ácido bórico, bórax (tetraborato de
sódio), **octaborato dissódico (DOT)**, boratos em geral, colemanita, kernita,
tincal, ulexita. E, sobre ele: identidade química e bases de massa, origem
astronômica e geológica, reservas e suprimento, para que serve (vidro, cerâmica,
fertilizante, medicamento, suplemento, preservante, metalurgia), quanto se usa em
cada uso, quanto o Brasil importa, toxicologia e classificação regulatória.

A **preservação de bambu** entra como **uma das aplicações** do elemento — a que
motivou a investigação e a que concentra o maior risco de uso sem critério.

**Não entra** (tem gaveta própria):

- **sulfato de cobre** — capítulo específico, ainda por abrir;
- CCA e CCB como objeto — aparecem aqui **apenas como contraste normativo**;
- vernizes voláteis, acabamentos acrílicos, concreto — capítulos seguintes.

## Conteúdo

| Artefato | Função |
|---|---|
| `00-estado-da-questao-boro.md` | Peça principal — o elemento, suas formas e bases de massa, origem, reservas, usos, as cinco bases de dosagem, importação, toxicologia, aplicação em preservação e os limites de uso |
| `01-importacao-brasileira-boro-comexstat.md` | Série de importação 1997–2026 por NCM, composição, origem, confronto com a produção mundial |
| `fichas/who-2009-boro-agua-consumo.md` | Ficha — a cadeia de derivação do valor de referência da OMS: BMDL05 10,3 → TDI 0,17 → alocação 40% → **2,4 mg/L** |
| `fichas/who-2022-boro-ficha-quimica.md` | Ficha — a ficha química oficial: valor de 2,4 mg/L, ocorrência < 0,5 mg/L, usos nomeados pela OMS |
| `fichas/liu-2023-bambu-acido-borico-borax.md` | Ficha — eficácia medida: perda de massa por fungo cai de 62,57% para 12,74%, compressão +21,56%. Ensaio de laboratório, **sem lixiviação** |
| `fichas/rusch-2023-ccb-bambu-5-anos-campo.md` | Ficha — CCB em campo por 5 anos: durabilidade **por concentração** (3% índice 0; 1% índice 40, ataque leve) contra **controles distintos** (totalmente imerso em água 100%; parcialmente imerso 80%); solo **sem diferença estatística** (Tukey p>0,05); ressalva dos autores de que **não se pode atribuir lixiviação** |
| `artigo-o-boro-explicado-do-zero.md` | **Artigo didático para leigo** — o boro explicado sem supor conhecimento de química: elemento, compostos, origem cósmica, reservas, usos, toxicologia, o caso do bambu, o resíduo e um guia para ler qualquer número sobre o tema |
| `INVENTARIO_GAVETA.json` | Estado real de cada fontee: custodiada, indisponível, pendente |
| `HANDOFF_BORO_20261124.md` | Handoff de continuidade entre tópicos (não é homologação) |

## Camada privada

Fontes, extrações e manifestos:

```
_privado/governanca-operacional/extracoes/boro/
├── HERANCA_MANIFEST.json       42 arquivos herdados (16 PDFs)
├── FONTES_NOVAS_MANIFEST.json  fontes custodiadas nesta rodada
├── INVENTARIO_FONTES.json      estado por fonte, inclusive as indisponíveis
├── herdado/ago_28_Boratos_Cobre/
├── herdado/ago_28_CCA_CCB/
└── fontes_novas/               USGS MCS2026, EMA, ANVISA RDC 199
    ├── comexstat/               API MDIC 1997–2026: raw/ (47 JSON) + 4 CSV + MANIFEST
    ├── atsdr_tp26/              Toxicological Profile for Boron (248 p.) + 12 capítulos
    └── nih_ods/                 NIH ODS Boron Fact Sheets (HTML + extração)
```

Os PDFs **não** entram na área versionada. Tabela e figura extraídas de artigo
permanecem custódia privada; do artigo se extrai o dado e se produz tabela
própria.

## Estado

`em-revisao-documental` · `homologacao_automatica: false` · **não homologado**.

As 10 fichas herdadas do pacote `ago_28_Boratos_Cobre` continuam em
`em-revisao-documental` e **não** foram promovidas por esta gaveta. Promoção
exige reprocessamento pelos estágios 3–8 do MTCC e revisão humana nominal.

## Referência rápida — as bases de dosagem

As **conversões químicas** entre massa de sal, boro elementar e equivalente B₂O₃
são legítimas (B = 17,5% do H₃BO₃; B₂O₃ = 67,51% do DOT). O que **não** se
substitui são os **limites normativos** de cada base.

**Estado de verificação de cada base.** Esta tabela reúne valores de fontes
custodiadas em `_privado/governanca-operacional/extracoes/boro/`, cada uma com
sha256 registrado. **A auditoria R7 não conferiu esta tabela** porque o pacote de
fontes entregue ao auditor cobria apenas as quatro fichas e as fontes em
`fontes-documentais/boro_r1/`. As bases marcadas ✦ foram conferidas contra a fonte
primária na montagem da gaveta e têm manifesto de custódia; as demais dependem de
reconferência nominal na homologação.

| Base | Unidade | Valor de referência | Fonte | Manifesto |
|---|---|---|---|---|
| Tópica medicinal (BR) | % do sal | água boricada 3% (2,900–3,200% H₃BO₃), só adultos | ANVISA RDC 199/2006 | ✦ `CUSTODIA_CORPO.json` |
| Sistêmica medicinal (UE) | mg B/dia | PDE 10 (adulto) · 7 · 3 · **1** | EMA/CHMP/765436/2012 | ✦ `CUSTODIA_CORPO.json` (1,3 MB) |
| Suplemento | mg B/dose | 0,15–6 usual · UL 20 mg/dia · OMS 1–13 mg/dia | NIH ODS | ✦ `CUSTODIA_R4.json` |
| Agricultura | **participação**, não dose | 11–15% do consumo mundial — **sem kg B/ha nesta gaveta** | USGS / estudo UE | ✦ `CUSTODIA_CORPO.json` |
| Preservação de bambu | kg/m³ | **B₂O₃ eq. 9,98–14,71** (DOT 14,79–21,79) vs. AWPA 2,7 · IS 401 5 | Gauss 2020, p. 88–89 | ✦ `CUSTODIA_R4.json` |
| Inalação (ocupacional) | mg B/m³ | MRL agudo 0,3 · irritação ~1,8 · REL NIOSH por forma: 5 (deca) e 1 (anidro/penta) mg/m³ | ATSDR tp26 · NIOSH | ✦ `INDEX_TP26.json` (12 cap. + PDF 248 p.) |

**Classificação vigente:** ácido bórico é **Repr. 1B, H360FD** no CLP (Reg. Del.
UE 2023/1435, vigente desde fev/2025). O documento EMA de 2021 cita Repr. cat. 2,
que é enquadramento histórico.

## Números de importação — referência rápida

**Estado de verificação.** Série construída por consulta à API do ComexStat
(POST em `api-comexstat.mdic.gov.br/general`, NCM 2528 + 2810 + 2840) e custodiada em
`MANIFEST_ComexStat.json` — **52 arquivos, 41.305.590 bytes**, soma conferida. **A
auditoria R7 não reconferiu estes números**, por não ter recebido esse pacote.

| Ano | Massa importada (t) | Valor FOB | US$/kg |
|---|---|---|---|
| 1997 | 111.621 | US$ 35,9 M | 0,321 |
| 2020 | 270.020 | US$ 88,6 M | 0,328 |
| 2025 | **487.185** | **US$ 225,8 M** | 0,464 |
| 2026* | 372.742 | US$ 205,2 M | 0,551 |

\* jan–out. NCM 2528 + 2810 + 2840. 76,8% do valor vem de Argentina, Bolívia,
Chile e Peru; Turquia salta para 30,9% em 2026. Detalhe e limites em
`01-importacao-brasileira-boro-comexstat.md`.

## A aplicação que concentra o problema — lixiviação

Ensaio direto na tese Gauss (2020), Tabela 4.7, p. 192–193. As colunas são
distintas — perda de massa, retenção de B₂O₃ antes e depois, e perda de boro:

| Tratamento | B₂O₃ antes | B₂O₃ depois | Perda de boro |
|---|---|---|---|
| **B5** (DOT isolado) | 4,66 kg/m³ | 0,82 kg/m³ | **82,4%** |
| **T10HB5** (tanino+hexamina+boro) | 3,01 kg/m³ | 0,55 kg/m³ | **81,7%** |

Apesar da perda alta, a tese registra que **as formulações com tanino mantiveram
resultado fúngico satisfatório** após o ensaio — a perda de boro não se converte
automaticamente em perda de proteção. É evidência laboratorial, não taxa de campo
(§7.1).

## O ponto crítico medido — resíduo, não banho

A única ACV brasileira da cadeia artesanal (Araujo et al. 2025, *Guadua
angustifolia*, Rio Branco/AC) mede onde o impacto se concentra:

- **93%** do impacto potencial normalizado está em **toxicidade carcinogênica
  humana**;
- **91%** do impacto total vem de **resíduos contaminados** — aparas, cortes e
  colmos descartados;
- o banho observado foi 100 L de água com **5 kg de bórax + 5 kg de ácido bórico**;
- por quilo de colmo tratado: **0,20 kg de resíduo**, **0,13 kg de colmo
  descartado**, **0,07 L de efluente**;
- **25%** da matéria-prima se perde no processo; **~13%** dos colmos são
  descartados após o tratamento, já impregnados; **~10%** da água do banho é
  descartada direto no solo.

**A consequência de política:** o operador ao menos pode usar EPI; **a aparagem sai
da oficina sem rótulo, sem rastreio e sem destinação**. Serragem de bambu tratado
é indistinguível de serragem limpa — e o uso doméstico comum (compostagem, cama de
animal, cobertura de solo, lenha) é justamente o que a dispersa.

**Limite que não se apaga:** são 93% de *impacto potencial normalizado*, em uma
unidade produtiva, com escopo até o portão. O estudo **não mediu** exposição, dose
nem desfecho clínico. ACV não se converte em incidência de câncer (§9.6).

## Pendência que define a gaveta

A exposição ocupacional **específica de bambu tratado** (cortar, lixar, serrar) —
Brasil e China — **não está medida em nenhuma das fontes custodiadas**. As réguas
para medi-la existem (§9.1–9.3); a conta de teto (§9.4) indica que o boro em
suspensão tende a ficar abaixo dos níveis de triagem **na premissa adotada**, mas
não há medição de poeira de bambu, e portanto **não se pode afirmar qual
componente domina** o risco respiratório dessa ocupação. É a lacuna que a
regulamentação precisaria fechar primeiro.

## Aviso

Esta gaveta **não** é homologação, certificação, validação experimental nem
autorização de publicação.
