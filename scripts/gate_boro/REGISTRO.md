# Registro auditável — gate numérico do artigo do boro

Medição de **2026-11-25**. Objeto: `docs/analyses/boro/artigo-o-boro-explicado-do-zero.md`,
corpo das seções 1 a 19. Regra declarada antes da medição em `REGRA_DE_CONTAGEM.md`.
Instrumento: `gate_fidelidade_fonte.py`, sha256 `c9ea56ce909dde98140802770ac4667d4fa8f10322ff5ad0c1c1e175a0ab1ff4`,
obtido de `origin/main` do repositório de governança, self-test **PASS, 92 asserções**.

Reprodução: `python3.11 rodar.py` (venv com PyMuPDF). Registro linha a linha: `registro.jsonl`.

## O número

**58 de 327 afirmações numéricas conferidas pelo instrumento.**

| Veredito | Quantas |
|---|---|
| `CONFERE` | **58** |
| `AUSENTE_NA_PAGINA` | **0** |
| `NAO_MEDIDO` | **269** |
| **M (denominador)** | **327** |

Medida auxiliar, **declarada à parte e não somada**: em **104** das 327 o valor foi
localizado em uma página da fonte citada por busca determinística. Isso é localização, não
conferência — o instrumento não confirmou unidade nessas.

## Por que 269 não foram medidas

| Motivo | Quantas |
|---|---|
| A afirmação não traz citação `[n]`: não há fonte declarada | 190 |
| Unidade fora do vocabulário do instrumento | 44 |
| Arquivo da fonte citada ausente na gaveta | 25 |
| Derivação aritmética declarada no texto | 6 |
| Fonte custodiada sem camada de texto (bloqueio/JS) | 2 |
| Instrumento devolveu `NAO_VERIFICAVEL` | 1 |
| Valor não localizado em nenhuma página | 1 |

**As 190 sem citação são o maior buraco, e não é do instrumento.** Metade do corpo do artigo
afirma números sem apontar fonte no ponto da afirmação: são sínteses, conversões de unidade,
razões entre valores já citados antes. A regra declarada exige `[n]`; sem ele o veredito é
`NAO_MEDIDO`, e essa é a informação — **o texto não permite auditar metade de si mesmo**.

## O limite do instrumento, medido

O gate lê **105 unidades**: `g`, `kg`, `t`, `m³`, `%`, `MPa`, `kN/m²`, `mm/ano`, horas, dias,
anos. **Nenhuma de dose ou concentração.** Medido, uma a uma:

| Forma | O gate lê? |
|---|---|
| `6 g`, `6 kg`, `2 m³`, `84,1%` | **sim** |
| `0,5 mg`, `2,4 mg/L`, `50 mg/m³`, `5 µg/L`, `0,2 mg/kg`, `0,2 mg B/kg/dia` | **não** |
| `3,8 vezes` | não |

Isso não é detalhe: **o objeto deste artigo é dose e concentração.** O instrumento foi
construído sobre fichas de engenharia (bambu estrutural) e não cobre a unidade central da
toxicologia. Para o dono do método, o achado é: **44 das 327 afirmações ficaram fora de
medição porque o vocabulário do gate não alcança `mg`** — e não porque a fonte falte.

## O que o `CONFERE` significa — e o que não significa

**`CONFERE` aqui quer dizer: o número existe na página declarada, com unidade compatível.**
Não quer dizer que a afirmação seja fiel. O instrumento não compara sujeito, e três casos
medidos mostram por quê:

- `40%` da alocação à água de consumo e `40%` de redução de peso de testículo **coexistem na
  p.13** do documento da OMS. O gate aprovou o item na primeira ocorrência, que era a errada.
- `60` como fator de incerteza e `60` como dose na ração **coexistem no mesmo documento**.
- `2,4` da diretriz casou com o item "2.4" do **sumário**, na p.7.

Foi preciso **buscar o documento inteiro** por cada valor e escolher a página pelos números
companheiros da mesma frase para resolver os casos. Depois disso, `AUSENTE` caiu para zero —
ou seja, **o único `AUSENTE` que restava não era ausência na fonte: era citação errada no
artigo.**

## O defeito que o gate encontrou no artigo, e que foi corrigido

`21,8 µg/L` — o efluente de Kırka tratado por wetland — estava citado como **[24]**, que é
Liu et al. 2023, artigo de bambu. O dado é de **Türker 2016**, que não estava na bibliografia.
Corrigido: entrada **[31]** criada, citação trocada, ficha
`fichas/turker-2016-kirka-arsenio-efluente-mina.md` escrita. **31 referências, 31 entradas.**

## Adjudicação manual dos 58

Os 58 foram lidos um a um contra a página. Resultado:

| Classe | Quantas | Observação |
|---|---|---|
| Confere (número, sujeito e unidade) | 51 | inclui os que só fecharam após busca no documento inteiro |
| Derivação aritmética apresentada como valor | 2 | `5%` e `10%` de soluto, calculados de 5 kg em 100 L |
| Página reatribuída | 5 | Rusch 40/0 e 1% (p.5, não p.2), Kaminski 2–6 anos e <1 ano (p.7, não p.13), 1mm–2mm (p.2) |
| **Citação errada, corrigida no texto** | 1 | o `21,8 µg/L` do Kırka |

**Nenhuma afirmação ficou sem veredito.** As 269 `NAO_MEDIDO` têm motivo nomeado, uma a uma,
em `registro.jsonl`.

## O que este registro não prova

- Não prova que as 58 sejam fiéis em **sentido**: prova que o número está na página, com a
  unidade certa. A fidelidade do sujeito foi lida por mim, afirmação por afirmação, e essa
  leitura não é reproduzível por comando — é julgamento registrado, não medição.
- Não cobre o blog, nem o glossário, nem a bibliografia.
- Não mede as 25 afirmações cuja fonte **não está custodiada** ([14], [16], [22], [30] e as
  dezenove páginas de [26] não presentes na gaveta): essas continuam sem fonte para conferir.
- Não transforma o artigo em peça homologada. Homologar é ato humano.
