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
| `INVENTARIO_GAVETA.json` | Estado real de cada fonte: custodiada, indisponível, pendente |

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
```

Os PDFs **não** entram na área versionada. Tabela e figura extraídas de artigo
permanecem custódia privada; do artigo se extrai o dado e se produz tabela
própria.

## Estado

`em-revisao-documental` · `homologacao_automatica: false` · **não homologado**.

As 10 fichas herdadas do pacote `ago_28_Boratos_Cobre` continuam em
`em-revisao-documental` e **não** foram promovidas por esta gaveta. Promoção
exige reprocessamento pelos estágios 3–8 do MTCC e revisão humana nominal.

## Referência rápida — as cinco réguas de dosagem

Nenhuma converte na outra.

| Régua | Unidade | Valor de referência | Fonte |
|---|---|---|---|
| Tópica medicinal (BR) | % do sal | água boricada 3% (2,900–3,200% H₃BO₃) | ANVISA RDC 199/2006 |
| Sistêmica medicinal (UE) | mg B/dia | PDE 10 (adulto) · 7 · 3 · 1 | EMA/CHMP/765436/2012 |
| Suplemento | mg B/cápsula | 0,15–6 — **não ancorado** | pendente: NIH 403 |
| Agricultura | kg/ha de B | carga de micronutriente | 11–15% do consumo |
| Preservação de bambu | kg/m³ de bambu | AWPA 2,7 · IS 401 5 · medido 14,79–21,79 | Gauss 2020 |

## Pendência que define a gaveta

A exposição ocupacional de quem prepara e aplica o banho — Brasil e China —
**não está medida em nenhuma das fontes custodiadas**. É a lacuna que a
regulamentação precisaria fechar primeiro.

## Aviso

Esta gaveta **não** é homologação, certificação, validação experimental nem
autorização de publicação.
