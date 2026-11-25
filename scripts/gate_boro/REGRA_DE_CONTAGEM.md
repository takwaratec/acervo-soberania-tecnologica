# Regra de contagem — gate numérico do artigo do boro

Declarada em 2026-11-25, **antes** de qualquer medição, porque o denominador é a regra e
não o palpite. Arquivo congelado junto com o registro: mudar a regra exige nova rodada
com número novo, e o número antigo passa a declarar a regra antiga.

## Objeto medido

- `docs/analyses/boro/artigo-o-boro-explicado-do-zero.md`, corpo do texto: seções 1 a 19.
- `docs/analyses/boro/blog-o-boro-ninguem-regula.md`, corpo do texto: dez seções.

**Fora do denominador, e por quê:** frontmatter (identificador), Glossário (definição, não
afirmação sobre o mundo), Bibliografia (entrada identifica obra, não afirma medida),
seção "Como este texto foi feito" (relato de processo), sumário e cabeçalhos de seção.

## O que conta como UMA afirmação numérica

**Um par (sujeito, valor) em que o valor quantifica uma propriedade do sujeito**, em prosa
ou em célula de tabela. Cada valor gera uma linha no registro, com sujeito, unidade,
parágrafo de origem e citação `[n]` quando houver.

Conta:

1. **Valor com unidade** — `0,2 mg B/kg/dia`, `49 µg/L`, `0,159 mPt`.
2. **Valor sem unidade com sujeito expresso** — em `629 de 676 trabalhadores`, **duas**
   afirmações: 629 (estudados) e 676 (universo).
3. **Cada elemento de uma enumeração** — `78,8% / 70,7% / 57,9% / 84,1%` são **quatro**
   afirmações, não uma. Somar apaga a série, que é o dado.
4. **Faixa** — `1 a 4 mg/m³` são **dois** valores (extremos), uma afirmação de faixa cada.
5. **Múltiplo ou razão** — `3,8 vezes`, `1,62×` = uma afirmação.
6. **Célula de tabela com valor** = uma afirmação, e a página da legenda vale para ela.

**Não conta, e o motivo:**

| Não conta | Por quê |
|---|---|
| Ano (`1983`, `2023`) | marca temporal, não medida — exceto quando o ano é o objeto medido |
| `[n]` de citação | identificador de referência |
| Número de seção, `§N`, `p. N` | localizador |
| Código NCM (`28045000`) | identificador de mercadoria, não medida |
| DOI, ISSN, ISBN, volume | identificador bibliográfico |
| Contagem de fichas/referências (`30 referências`) | metadado do próprio documento |
| `1 kg`, `1 m³` em exemplo hipotético | unidade de normalização, não medida observada |

## Veredito por afirmação

| Veredito | Significa |
|---|---|
| `CONFERE` | valor, unidade e sujeito encontrados na página declarada da fonte |
| `DIVERGENTE` | valor existe na fonte com outro número, unidade ou sujeito |
| `AUSENTE_NA_PAGINA` | a página foi lida e o valor não está nela |
| `NAO_MEDIDO` | a fonte não permite conferir — com motivo declarado por item |

`NAO_MEDIDO` cobre, no mínimo: fonte sem extração em texto; fonte fechada (paywall,
bloqueio técnico); afirmação sem `[n]` (não há fonte a conferir). **Herança de veredito da
rodada anterior é proibida**: cada afirmação é medida de novo, ou é `NAO_MEDIDO` com motivo.

## Como a página é obtida (e a circularidade declarada)

O texto de cada fonte custodiada é reextraído do PDF **com marcador de página**. A página de
uma afirmação é a página em que o valor ocorre no texto extraído, localizada por busca
determinística. **Isso não é o gate concordando consigo mesmo**: a busca dá a página, e o
gate então verifica se, naquela página, o número existe com a unidade e o sujeito que a
afirmação declara. Valor certo em página errada cai; unidade trocada cai.

## Denominador e reprodutibilidade

- `M` = número de linhas do registro.
- `N` = linhas com veredito `CONFERE`.
- Publicar sempre `N de M`, com as duas parcelas ao lado e a contagem de cada veredito.
- **Zero afirmação com parágrafo sem veredito.**
- O registro é um comando: `python3.11 scripts/gate_boro/rodar.py`. Quem roda obtém o mesmo M.
