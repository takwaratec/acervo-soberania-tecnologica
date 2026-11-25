# RELEITURA MTCC/R38 DO RELEASE 1 — RESULTADO MEDIDO

DATA=2026-11-24
FRENTE=re-CURADORIA do corpus `_privado/fontes-academicas/revisao-89/` pelo motor MTCC/R4
OBJETO=12 documentos importados do Release 1, 211 páginas
MOTOR=`ops/command-center/metodo/motor_r38.py` + `emissor_r38.py` (SHA do commit desta rodada)

## O que foi feito, e por que a extração herdada não servia

O corpus do Release 1 tem `extracao.md` por documento, mas **a extração guarda uma página
inteira por bloco** — 34 blocos para 16 páginas no caso do Araujo 2025. O estágio 6 do MTCC
exige âncora com `pagina`, `bloco_id` e intervalo de caracteres; ancorar sobre aquela extração
daria uma âncora por página e nenhuma afirmação conferível. **A releitura re-extraiu do PDF**
com `PyMuPDF.get_text("blocks")`, que devolve caixa, página e ordem de leitura.

## Corpus lido

| documento | páginas | blocos | corpo | não analisável |
|---|---|---|---|---|
| 2014-beraldo-matsuoka-pirolenhoso | 10 | 179 | 100 | 79 |
| 2014-gutierrez-takeuchi-umidade-guadua | 7 | 57 | 22 | 35 |
| 2017-chung-wang-peeling-steam | 11 | 145 | 44 | 101 |
| 2019-hong-et-al-conexoes-bambu | 18 | 116 | 45 | 71 |
| 2020-bologna-aquino-desmatamento-populacao | 9 | 276 | 43 | 233 |
| 2022-kamaruddin-alkali-lemongrass-composite | 26 | 314 | 104 | 210 |
| 2024-costa-et-al-solo-sistemas-integrados | 14 | 203 | 113 | 90 |
| 2024-hernandez-mena-et-al-bambu-neotropical | 21 | 712 | 384 | 328 |
| 2024-oliveira-villa-covid-his | 26 | 604 | 142 | 462 |
| 2024-otoni-villa-resiliencia-ampliabilidade | 18 | 181 | 109 | 72 |
| 2024-simoes-leder-habitacao-seriada | 35 | 956 | 612 | 344 |
| 2025-araujo-et-al-acv-bambu-amazonia | 16 | 254 | 138 | 116 |
| **total** | **211** | **3.997** | **1.856** | **2.141** |

Nada foi apagado: **os 2.141 blocos não analisáveis têm rótulo e motivo** cada um
(`referencia`, `legenda`, `numeracao`, `nao_analisavel`, `agradecimento`, `fragmento`).

Ordem de leitura: **9 documentos com 0 ambiguidades**; 3 com ambiguidade real, dos quais
**2024-hernandez-mena é duas colunas de fato** (x0 = 48 e x0 = 300) e os outros dois têm
fórmulas quebradas em blocos. O gate `ORDEM_LEITURA_PASS` **não passa** nesses três: exige
resolução descrita, e a resolução honesta é re-extrair por coluna, não declarar aceito.

## O motor, rodado nos 12

| documento | unidades | ACEITA | REVISAR | EXCLUIDA | G3 | G5 |
|---|---|---|---|---|---|---|
| beraldo-matsuoka | 99 | 6 | 91 | 2 | 43 | 23 |
| gutierrez-takeuchi | 22 | 0 | 19 | 3 | 11 | 8 |
| chung-wang | 44 | 3 | 36 | 5 | 26 | 16 |
| hong-et-al | 44 | 2 | 40 | 2 | 42 | 24 |
| bologna-aquino | 42 | 3 | 39 | 0 | 24 | 26 |
| kamaruddin | 104 | 5 | 92 | 7 | 61 | 63 |
| costa-et-al | 113 | 3 | 85 | 25 | 78 | 27 |
| hernandez-mena | 384 | 9 | 294 | 81 | 254 | 61 |
| oliveira-villa | 141 | 4 | 127 | 10 | 110 | 45 |
| otoni-villa | 109 | 0 | 87 | 22 | 90 | 72 |
| simoes-leder | 612 | 20 | 533 | 59 | 103 | 68 |
| araujo-et-al | 138 | 10 | 101 | 27 | 92 | 37 |
| **total** | **1.852** | **65** | **1.544** | **243** | **935** | **470** |

**Veredicto por documento: `FAIL` em todos os 12, `READINESS=NAO_READY`.** Exit ≠ 0 em todos.

## As três causas, medidas e separadas

### 1. Falso alarme fechado — locale (era 100% das unidades com número)

`LOCALE_POR_DOC` tinha 6 entradas e o `documento_id` chega como `"slug.pdf"`; o dicionário é
indexado por slug, então `locale` era `None` em tudo e todo decimal de três casas virava
`AMBIGUO`. Corrigido com os 12 slugs e `.removesuffix(".pdf")`. **Isto era defeito do
emissor**, não do corpus.

### 2. Falso alarme fechado — referência cruzada (14 de 106 no piloto)

Número que é citação (`Pieter; Utomo, 2020`), lista de citações (`11,12,13`) ou numeral de
figura/seção não afirma quantidade. O G3 exigia variável dele e reprovava a frase por um
número que ela não usa como dado. Corrigido com `_so_referencia_cruzada`, declarada no gate.

### 3. O que permanece, e é legítimo — 935 reprovações do G3

Número real cujo bloco **não declara a variável**. Exemplo do próprio achado central da obra:

> *"HCT accounted for approximately 93% of the total estimated environmental impact"*

→ `valor_tipado = {tipo: PERCENTUAL, valores: ["93"], variavel: null}`. A frase diz *quanto*
(93%) e *de quê* (impacto total estimado), mas nomear a variável como "toxicidade
carcinogênica humana, categoria ReCiPe, normalizada" **exige leitura**, e o emissor não lê
sentido. `_VAR_MARCAS` tem 12 marcadores, todos de sensoriamento remoto e silvicultura
(NDVI, biomassa, diâmetro, parcelas) — o domínio em que foi calibrado.

**Isto não é defeito a consertar com heurística.** É o modelo funcionando: G3 exige que a
variável esteja estabelecida, e o honesto é `REVISAR`, nunca `ACEITA` nem `SEM_NUMERO`.

## O que este resultado autoriza e o que não autoriza

- **Não autoriza** nenhuma ficha derivada deste lote. Nenhum documento está `PASS`.
- **Não autoriza** tratar as 65 `ACEITA` como curadoria concluída: são 3,5% de 1.852, e o
  selo do MTCC declara `publicaveis: []` enquanto não houver revisão independente registrada.
- **Autoriza** dizer que o corpus foi lido inteiro, com âncora por bloco, rótulo com motivo e
  reprovação por causa declarada — que é o estado honesto de uma releitura em andamento.

## Caminho para fechar, em ordem

1. **Ordem de leitura dos 3 documentos ambíguos** — re-extrair por coluna e provar a ordem
   antes de qualquer análise daquelas páginas.
2. **As 935 unidades do G3** — leitura humana da variável, documento por documento. É o
   trabalho de curadoria de verdade, e não tem atalho determinístico que não invente dado.
3. **As 470 do G5** — mesma natureza.
4. Só então: ficha por documento, com `ACEITA` sustentada por revisão independente.

## Arquivos

- `scripts/mtcc_reler_release1.py` — re-extração do PDF, crivo de rótulos, âncoras
- `_privado/governanca-operacional/mtcc-release1/<slug>/{ANCORAS,CRIVO}.json` — 12 × 2
- `_privado/governanca-operacional/mtcc-release1/LOTE.json` — inventário do lote
- `_privado/governanca-operacional/mtcc-release1/lotes/<slug>/` — saída do emissor por documento
- `ops/command-center/metodo/motor_r38.py` — `_so_referencia_cruzada` no G3
- `ops/command-center/metodo/emissor_r38.py` — locale por slug, via da unidade de medida,
  exceção de referência cruzada
