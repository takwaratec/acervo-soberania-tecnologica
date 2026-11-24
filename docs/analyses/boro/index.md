# Gaveta — boro

Frente `BORO` (aberta 2026-11-24 no ledger R4, commit `ecaa7153`).
Capítulo introdutório da série **tratamentos convencionais do bambu**.

## Escopo desta gaveta

Entra: **boro** (ácido bórico, borax/tetraborato, DOT, boratos em geral) —
origem, química, toxicologia, dosagem, uso como preservante de bambu,
lixiviação, exposição ocupacional.

**Não entra** (tem gaveta própria):

- **sulfato de cobre** — capítulo específico, ainda por abrir;
- CCA e CCB como objeto — aparecem aqui **apenas como contraste normativo**;
- vernizes voláteis, acabamentos acrílicos, concreto — capítulos seguintes.

## Conteúdo

| Artefato | Função |
|---|---|
| `00-estado-da-questao-boro.md` | Ficha principal — as quatro afirmações submetidas à verificação, as cinco réguas de dosagem, o argumento de lixiviação, o que a ficha não autoriza concluir |
| `01-importacao-brasileira-boro-comexstat.md` | Série de importação 1997–2026 por NCM, composição, origem, confronto com a produção mundial |
| `INVENTARIO_GAVETA.json` | Estado real de cada fonte: custodiada, indisponível, pendente |
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

| Base | Unidade | Valor de referência | Fonte |
|---|---|---|---|
| Tópica medicinal (BR) | % do sal | água boricada 3% (2,900–3,200% H₃BO₃), só adultos | ANVISA RDC 199/2006 |
| Sistêmica medicinal (UE) | mg B/dia | PDE 10 (adulto) · 7 · 3 · **1** | EMA/CHMP/765436/2012 |
| Suplemento | mg B/dose | 0,15–6 usual · UL 20 mg/dia · OMS 1–13 mg/dia | NIH ODS (ancorado 2026-11-24) |
| Agricultura | **participação**, não dose | 11–15% do consumo mundial — **sem kg B/ha nesta gaveta** | USGS / estudo UE |
| Preservação de bambu | kg/m³ | **B₂O₃ eq. 9,98–14,71** (DOT 14,79–21,79) vs. AWPA 2,7 · IS 401 5 | Gauss 2020, p. 88–89 |
| Inalação (ocupacional) | mg B/m³ | MRL agudo 0,3 · irritação ~1,8 · poeira total 1–15 mg/m³ | ATSDR tp26 (2010) |

**Classificação vigente:** ácido bórico é **Repr. 1B, H360FD** no CLP (Reg. Del.
UE 2023/1435, vigente desde fev/2025). O documento EMA de 2021 cita Repr. cat. 2,
que é enquadramento histórico.

## Números de importação — referência rápida

| Ano | Massa importada (t) | Valor FOB | US$/kg |
|---|---|---|---|
| 1997 | 111.621 | US$ 35,9 M | 0,321 |
| 2020 | 270.020 | US$ 88,6 M | 0,328 |
| 2025 | **487.185** | **US$ 225,8 M** | 0,464 |
| 2026* | 372.742 | US$ 205,2 M | 0,551 |

\* jan–out. NCM 2528 + 2810 + 2840. 76,8% do valor vem de Argentina, Bolívia,
Chile e Peru; Turquia salta para 30,9% em 2026. Detalhe e limites em
`01-importacao-brasileira-boro-comexstat.md`.

## O achado central — lixiviação

Ensaio direto na tese Gauss (2020), Tabela 4.7, p. 192–193: bambu tratado
**somente com DOT** perdeu **82,4%** do boro no ciclo de lixiviação (B5), e o
tratamento com tanino/hexamina perdeu **81,7%** (T10HB5). A tese registra que a
lixiviação severa **eliminou a atividade fungicida**. É evidência laboratorial,
não taxa de campo — e é o núcleo do capítulo (§7.1).

## Pendência que define a gaveta

A exposição ocupacional **específica de bambu tratado** (cortar, lixar, serrar) —
Brasil e China — **não está medida em nenhuma das fontes custodiadas**. As réguas
para medi-la agora existem (§9.1–9.3 da ficha), e uma conta de teto (§9.4) mostra
que o risco respiratório dominante é o **particulado/sílica**, não o borato. É a
lacuna que a regulamentação precisaria fechar primeiro.

## Aviso

Esta gaveta **não** é homologação, certificação, validação experimental nem
autorização de publicação.
