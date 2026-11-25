PARECER R11 — AUDITORIA DO SUJEITO (BORO)
AUDITOR: CODEX_LUNA (gpt-6-luna, reasoning xhigh), sandbox read-only
OBJETO: 61 afirmacoes aprovadas pelo gate de fidelidade em 2026-11-25
VEREDITO: 48 SUJEITO_CONFERE · 4 SUJEITO_DIVERGENTE · 9 INDETERMINADO

NOTA DE TRANSCRICAO
O auditor rodou em sandbox somente-leitura e nao pode gravar o arquivo: o parecer foi
emitido no stdout e transcrito aqui pelo executor, sem edicao, do log /tmp/teco_r11.log.
Parecer de auditor reaproveitado por terceiro nao pode ter passado pela mao de quem foi
auditado sem que isso esteja escrito — esta e a declaracao.

---
# Parecer R11 — Auditoria do sujeito

- **SUJEITO_CONFERE:** 48
- **SUJEITO_DIVERGENTE:** 4
- **INDETERMINADO:** 9
- **Total:** 61

## SUJEITO_DIVERGENTE

- **ID 99 — 80 mL/min.** Frase: “diferença de filtração glomerular entre humanos e ratos (144 contra 80 mL/min)”. A OMS p. 22 descreve 80 mL/min como a taxa de filtração duas unidades de desvio-padrão abaixo da média entre mulheres grávidas; não como taxa de ratos. O artigo atribui o valor a outro sujeito.
- **ID 170 — 40.** Frase: hastes tratadas com CCB a 1% e 3% tiveram índices de degradação de 40 e 0. Na p. 2, o trecho com 40 integra a coordenada “27°21’33” S e 53°23’40” W”, não um índice de degradação.
- **ID 171 — 0.** Mesma frase. Na p. 2, o 0 identifica a concentração do grupo-controle (“0 (totalmente imerso em água)”), não o índice de degradação do tratamento a 3%.
- **ID 252 — 1,8.** Frase: “1,8 vem da diferença de filtração glomerular entre humanos e ratos (144 contra 80 mL/min)”. A OMS p. 22 calcula o valor usando a média de mulheres grávidas e a taxa duas unidades de desvio-padrão abaixo dessa média, para representar variabilidade em cerca de 95% da população; não apresenta uma comparação de filtração entre humanos e ratos.

## INDETERMINADO

- **ID 151 — 1.** Frase: “larvas [...] deixando furos de 1 a 2 mm”. A p. 13 de Kaminski é uma página de referências e não traz contexto sobre diâmetro de furos. O trecho pertinente está na p. 2; a página declarada não permite decidir.
- **ID 152 — 2 mm.** Mesma frase e motivo do ID 151: a p. 13 de Kaminski é bibliográfica, sem contexto sobre diâmetro. A passagem pertinente está na p. 2.
- **ID 217 — 5 kg.** Frase: banho de “100 L de água com 5 kg de bórax e 5 kg de ácido bórico”. A p. 14 de Araújo é bibliografia e não contextualiza a quantidade como receita. O método está na p. 4; a página declarada não permite decidir o sujeito do número.
- **ID 218 — 5 kg.** Mesma frase e motivo do ID 217: a p. 14 de Araújo é bibliográfica; o contexto da receita está na p. 4.
- **ID 219 — 5%.** Frase: “5% de cada soluto”. A p. 14 de Araújo é bibliografia e não contextualiza a concentração do banho. O método está na p. 4; a página declarada não permite decidir.
- **ID 220 — 10%.** Frase: “10% de sólidos ao todo”. Mesma limitação: a p. 14 de Araújo é bibliográfica; falta contexto de concentração nessa página. O método está na p. 4.
- **ID 233 — 2 anos.** Frase: “2 a 6 anos no interno, menos que isso no externo”. A p. 13 de Kaminski é bibliográfica, sem contexto de vida útil. A tabela pertinente está na p. 7; a página declarada não permite decidir.
- **ID 234 — 6 anos.** Mesma frase e motivo do ID 233: a p. 13 de Kaminski não contém a tabela de vida útil; ela está na p. 7.
- **ID 263 — menos de 1 ano.** Frase: “Boro não resolve contato com solo: menos de 1 ano de vida útil”. A p. 13 de Kaminski é bibliográfica, sem contexto de vida útil. A tabela pertinente está na p. 7; a página declarada não permite decidir.

## SUJEITO_CONFERE

IDs: 21, 66, 98, 100, 103, 122, 123, 124, 125, 126, 128, 129, 130, 131, 153, 161, 162, 163, 165, 166, 167, 168, 169, 172, 173, 174, 175, 176, 177, 178, 196, 200, 201, 202, 203, 204, 205, 206, 207, 208, 214, 221, 232, 250, 251, 253, 254, 269.

## ACHADO MATERIAL

**OMS [1], p. 22 — IDs 99 e 252.** O artigo transforma um valor de variabilidade entre mulheres grávidas em comparação entre espécies. A OMS descreve “the glomerular filtration rate at two standard deviations below the mean (80 ml/min) to address variability for approximately 95% of the population”. Assim, 80 mL/min não é uma taxa de ratos, e o valor 1,8 deriva dessa variação humana descrita na página.

**Rusch [25], p. 2 — IDs 170 e 171.** A página atribui 40 à coordenada “27°21’33” S e 53°23’40” W” e descreve 0 como concentração do controle: “0 (totalmente imerso em água)”. Esses números não são índices de degradação nessa página. A tabela de resultados que associa 40 ao tratamento de 1% e 0 ao de 3% está na p. 5; portanto, o achado é de atribuição à página citada, não de contradição com os resultados do estudo.
EXIT=0
