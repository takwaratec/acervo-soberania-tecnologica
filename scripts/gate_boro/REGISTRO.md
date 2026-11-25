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


---

## Os cards sem cifra — a causa era o CSS, não o texto (2026-11-25)

O soberano apontou segunda vez, e com razão: **nos cards**, o número aparecia sem dizer do que
era. A primeira correção (cabeçalho da tabela) não resolvia, porque **a tabela não existe como
tabela na tela estreita**.

**Causa medida**, no CSS da peça: `thead{display:none}` e o rótulo de cada célula vem de
`td::before{content:attr(data-l)}`. O conversor markdown→HTML marca **parte** das células com
`data-l`; contei **570 de 705**. As **135 sem rótulo** viravam card sem unidade — e são
justamente as colunas numéricas que o leitor precisa ler.

**Correção:** o gerador passou a preencher `data-l` em **todas** as células, tirando o rótulo do
`<th>` da própria coluna. Agora são **705 de 705**.

**E a redundância que a correção criou, e foi corrigida também:** rótulo `Massa importada (mil t)`
com célula `200,7 mil` lê como "mil mil t". As células passaram a trazer o número por extenso
(`200.700`) e o rótulo a dizer a unidade inteira (`Massa importada (toneladas)`).

**Verificado no navegador em largura de celular** (420 px), não no HTML cru: os cards mostram
`ORIGEM`, `PARTICIPAÇÃO POR PESO (MASSA)` e `MASSA IMPORTADA (TONELADAS)` acima dos números.

**Lição que fica:** conferir o HTML não é conferir o que o leitor vê. `thead{display:none}` faz
metade da conferência mentir. Toda revisão de tabela desta frente passa a ser feita **com a
página renderizada em tela estreita**, não no arquivo.

---

## Histórico datado pelo commit — não pela lembrança (2026-11-25)

Cada linha abaixo é uma rodada e o commit que a representa. Data sem commit não é histórico:
é lembrança, e esta frente já pagou caro por lembrança.

| Rodada | Data | Commit | O que decidiu |
|---|---|---|---|
| R8 residual | 2026-11-24 22:06 | `3e98a27` | separa efluente da atribuição dos 91% |
| Sol, 2 impedimentos | 2026-11-24 23:10 | `f6bca78` | correções da auditoria externa |
| R9 (Teco) | 2026-11-24 23:41 | `96b850f` | 8 achados, 8 confirmados no disco |
| R10 (Teco) | 2026-11-25 08:09 | `ff2070d` | 6 achados; §19 escrita |
| Gate ligado | 2026-11-25 09:34 | `304e9e6` | 58 de 327, registro por afirmação |
| Estatutos A/B/C | 2026-11-25 10:20 | `c8fcbfe` | 61 de 287; emenda v1→v2 |
| R11 (Teco) | 2026-11-25 10:32 | `fb9f785` | eixo do sujeito; o `1,8` corrigido |
| Devolutiva do soberano | 2026-11-25 12:09 | `3b688c5` | páginas, reconciliação 58→61→65, nota ComexStat |
| PARECER_R6 | 2026-11-25 12:19 | `cb7c97c` | bytes idênticos, provado por blob |
| Contagem do diff | 2026-11-25 12:19 | `2e50945` | 21 → 22 arquivos |
| R12 (Teco) | 2026-11-25 12:44 | `0fb6353` | 3 páginas erradas corrigidas |
| Cifra nas tabelas | 2026-11-25 13:00 | `11ddd0d` | unidade em 9 tabelas; M 283→286 |
| Cards sem cifra | 2026-11-25 13:12 | `560815d` | causa era o CSS; `data-l` 705/705 |
| OS B-04/B-03 | 2026-11-25 | *este commit* | corpus delimitado; quatro estados por referência |

**Por que este quadro existe:** o parecer B-02 apontou que o histórico estava datado sem o
commit. Data sozinha não permite reconstruir o estado do arquivo naquele dia; o commit permite.

---

## Os quatro estados por referência (B-03) — 2026-11-25

O artigo afirmava que **só a [22]** não estava custodiada. Era falso. O medido, por comando, é:

| Estado | Quantas de 32 | Quais |
|---|---:|---|
| **Identificada** (nomeada na bibliografia) | **32** | todas |
| **Arquivo custodiado** (arquivo + sha256) | **27** | faltam [14], [16], [22], [30]; [10] é derivação, não documento |
| **Texto utilizável** (texto conferível no arquivo) | **26** | [15] custodiada e ilegível; [16] sem arquivo aqui |
| **Leitura integral confirmada** (artefato de leitura arquivado) | **0** | nenhuma |

**Os quatro estados não se convertem.** Custódia não implica legibilidade — a [15] tem hash
válido e 36 caracteres de muro Cloudflare. Legibilidade não implica leitura — nenhuma das 32
tem artefato de leitura integral arquivado, e por isso a contagem é zero mesmo sabendo que
páginas específicas foram lidas para conferir afirmações.

Correções de medição que esta rodada obrigou:

- **[4] não falta.** O mapa de citação (`MAPA` no `rodar.py`) aponta para um PDF que não existe,
  mas a custódia do ComexStat é outra: `MANIFEST_ComexStat.json` mais `raw/ncm_2024.json` e os
  CSV. Fonte de API não se custodia como PDF. Contá-la como ausente seria erro de instrumento.
- **[10] não é documento.** É derivação de massas atômicas; uma das duas entradas (USDA AMS
  TR-2022) não está custodiada. Por isso entra como `n/a`, e não como "não custodiada".
- **[32] parecia ilegível e não é.** Meu primeiro contador só lia `[A-Za-z]` e dava 370
  caracteres em 8 páginas; o documento é chinês. Com `\w` Unicode são 3.222 caracteres em 8
  páginas. **Métrica que não lê a língua da fonte produz número falso** — e este quase entrou.
- **[16] existe fora daqui.** A tese de Gauss (2020) está como PDF na branch do cobre, não
  nesta gaveta. Enquanto não for custodiada aqui, o texto não a pode usar como dado — e o
  artigo passou a declarar isso.

---

## Inventário nominal das fichas por tipo e origem (B-06)

**22 fichas**, todas em `docs/analyses/boro/fichas/`, todas com `estado_documental:
em-revisao-documental` — nenhuma declara homologação, e `homologacao_automatica: false` em
todas. Gerei por script lendo o frontmatter; o número anterior de "21 + 4 relacionadas" era
contagem minha, não medida, e não se reproduz.

**Duas ressalvas nominais, declaradas e não corrigidas nesta rodada** (mudar nome de arquivo é
diff fora do escopo desta OS):

- `atsdr-2026-boro-perfil-toxicologico.md` — o ano no nome é **2026**, e o documento é de
  **novembro de 2010**. O corpo da ficha já traz 2010; o nome do arquivo ficou errado.
- `turker-2016-…` e `niosh-mheta-…` não têm campo `instituicao`; a origem está em `autores`.

**`norma-ou-regulamento` — 9 fichas**

| Ficha | Origem (autor/instituição) | Ano | Estado |
|---|---|---:|---|
| `anvisa-2006-agua-boricada-3.md` | Agência Nacional de Vigilância Sanitária (ANVISA) | 2006 | em-revisao-documental |
| `atsdr-2026-boro-perfil-toxicologico.md` | Agency for Toxic Substances and Disease Registry (ATSDR) | 2010 | em-revisao-documental |
| `ema-2021-boro-excipientes-pde.md` | European Medicines Agency — Committee for Human Medicinal Products … | 2021 | em-revisao-documental |
| `hongkong-2025-andaime-bambu-nao-tratado.md` | Buildings Department (HKSAR); Labour Department (HKSAR) | 2025 | em-revisao-documental |
| `lei-12305-2010-pnrs-residuo-bambu.md` | Brasil — Lei nº 12.305, de 2 de agosto de 2010 | 2010 | em-revisao-documental |
| `lei-12484-2011-pnmcb-bambu-sem-residuo.md` | Brasil — Lei nº 12.484, de 8 de setembro de 2011 | 2011 | em-revisao-documental |
| `mee-2023-inspecao-qaidam-salares-china.md` | Ministério de Ecologia e Meio Ambiente da China (MEE), 5º Grupo Ins… | 2023 | em-revisao-documental |
| `niosh-2026-boratos-limites-forma.md` | National Institute for Occupational Safety and Health (NIOSH) | 2026 | em-revisao-documental |
| `ue-2023-clp-repr-1b-h360fd.md` | Comissão Europeia | 2023 | em-revisao-documental |

**`ficha-academica` — 5 fichas**

| Ficha | Origem (autor/instituição) | Ano | Estado |
|---|---|---:|---|
| `araujo-2025-acv-bambu-acre-93-hct.md` | Araujo, Letícia Medeiros de; Gianelli, Bruno Fernando; Mancini, San… | 2025 | em-revisao-documental |
| `kaminski-2016-durabilidade-bambu-tabela.md` | Kaminski, Sebastian; Lawrence, Andrew; Trujillo, David; King, Charl… | 2016 | em-revisao-documental |
| `liese-preservacao-bambu-em-servico.md` | Liese, Walter | null | em-revisao-documental |
| `liu-2023-bambu-acido-borico-borax.md` | Hunan City University, College of Arts and Design (Yiyang, China) | 2023 | em-revisao-documental |
| `rusch-2023-ccb-bambu-5-anos-campo.md` | UFSM — Departamento de Engenharia Florestal e de Química (Frederico… | 2023 | em-revisao-documental |

**`ficha-tecnica-de-produto` — 6 fichas**

| Ficha | Origem (autor/instituição) | Ano | Estado |
|---|---|---:|---|
| `aga-khan-2010-green-school-manutencao.md` | Shim, Brigitte | 2010 | em-revisao-documental |
| `inbar-2019-bambu-economia-circular.md` | van der Lugt, Pablo; King, Charlotte | 2019 | em-revisao-documental |
| `nih-ods-2026-boro-suplemento.md` | National Institutes of Health — Office of Dietary Supplements | 2026 | em-revisao-documental |
| `usgs-2026-boro-commodity-summary.md` | Brioche, Amanda S. (U.S. Geological Survey) | 2026 | em-revisao-documental |
| `who-2009-boro-agua-consumo.md` | World Health Organization (WHO) | 2009 | em-revisao-documental |
| `who-2022-boro-ficha-quimica.md` | World Health Organization (WHO) | 2022 | em-revisao-documental |

**`ficha-cientifica` — 1 fichas**

| Ficha | Origem (autor/instituição) | Ano | Estado |
|---|---|---:|---|
| `turker-2016-kirka-arsenio-efluente-mina.md` | TÜRKER, Onur Can (Universidade de Aksaray) | 2016 | em-revisao-documental |

**`manual-tecnico` — 1 fichas**

| Ficha | Origem (autor/instituição) | Ano | Estado |
|---|---|---:|---|
| `niosh-mheta-80-109-borax-boron-california-1983.md` | NIOSH / University of Southern California | 1983 | em-revisao-documental |

---

## R13 — auditoria do conteúdo, e sete afirmações que não se sustentavam (2026-11-25)

Escopo: o conteúdo da main em `ffac50b6`, não o selo (declaradamente órfão na ocasião).
Veredito do auditor: **a seção 19 foi delimitada com honestidade e a tabela dos quatro estados
passa sem divergência**; o que ele achou foram afirmações gerais e rastreabilidade de corpus.

**Corrigidas neste commit, uma por uma, com o motivo:**

| # | Onde | O que afirmava | Por que caiu | Como ficou |
|---|---|---|---|---|
| 1 | §1, l. 119 | "a origem de **metade** dos números errados" | quantificador sem corpus definido | virou o fator que se mede: **erro por quase seis vezes (100 ÷ 17,5)** |
| 2 | §6, l. 270 | "**Toda** substância tem uma dose…" | universal sem atribuição | atribuído ao **princípio de Paracelso**, e declarado princípio, não medição desta gaveta |
| 3 | §4, l. 214 | "**Não há escassez** de boro" | ampliava a frase do USGS, que fala de níveis atuais de consumo | "**aos níveis atuais de consumo** (…) e não uma projeção para outro horizonte" |
| 4 | §5, l. 46 | resíduo fora da lista perigosa de "**Brasil, China, Índia, Vietnã, Indonésia**" | não há norma de Índia, Vietnã e Indonésia na gaveta | reduzido à PNRS, à PNMCB e à inspeção do MEE; **as três ficaram declaradas como não lidas** |
| 5 | §14, l. 815 | "**cinco países** examinados" | mesmo defeito, sem lista | "países examinados nesta gaveta" |
| 6 | §19, l. 996 | "o boro **quase nunca** é o motivo de uma mina existir" | o USGS registra produção de borato (ulexita, colemanita) onde o boro **é** o produto | virou "na maior parte das cadeias examinadas", **com a exceção declarada e citada** |
| 7 | §19, l. 1019 | "**não existe** mineração de boro nos Andes" | o USGS lista produção andina; o que falta é o estudo de impacto, não a extração | "não localizei **o estudo**"; a diferença entre "não há extração" e "não achei o estudo" está escrita |

**Dois defeitos de citação, que valem mais que os sete de redação:**

- **NBR 10004 atribuída a [14].** A [14] é documentação da Environmental Bamboo Foundation — não
  é a norma. E a NBR 10004 **não tem cópia custodiada** nesta gaveta: nenhuma entrada
  bibliográfica, nenhum arquivo. O texto passou a dizer que **a NBR não foi examinada**, e a §19
  deixou de listá-la entre os instrumentos examinados. *Norma não lida não sustenta afirmação
  sobre o que ela lista.*
- **"Duas de oito lidas integralmente".** Esta frase, no método, contradizia o `0 de 32` que o
  próprio texto agora mede. Foi substituída pela medição, e o resumo de **Gao et al.** — que ela
  nomeava — **não está na bibliografia**: quem quiser usá-lo precisa custodiá-lo e citá-lo como
  [33], com ficha. Não criei a entrada; não há fonte na gaveta.

**Um achado de integridade na custódia, que era real:**

O R13 mediu o manifesto do ComexStat contra os 52 arquivos que ele mesmo lista: **48 conferiam,
4 não** — os quatro CSV. Não era corrupção: os CSV foram regerados quando a série de dez NCMs
foi derivada (§7-bis), e o manifesto ficou com o hash velho. **Verifiquei antes de rehashar:**
a coluna `fob_usd`/`kg` de 2024 nos CSV fecha exatamente com os JSONs brutos —
**209.462.631 e 459.722.221**. O manifesto foi atualizado com data, com o hash anterior
preservado e com a razão; recontado: **52 de 52 conferem**.

**E um defeito de instrumento:** `reproduzir_comexstat.py` só achava o bruto relativo à raiz do
repo, e a gaveta vive fora do worktree — o comando falhava no primeiro uso de quem clonasse.
Passou a resolver por `--bruto`, por `$ACERVO` e por caminho absoluto do acervo, nessa ordem.

**Denominador depois destas correções:** M **287 → 289**, `CONFERE` **62**, `DERIVACAO_DECLARADA`
**6 → 8** (as duas contas que substituíram quantificadores vagos), `NAO_MEDIDO` **207**,
`TABELA_COM_NOTA` **10**, `RESUMO` **2**, `AUSENTE` **0**.
