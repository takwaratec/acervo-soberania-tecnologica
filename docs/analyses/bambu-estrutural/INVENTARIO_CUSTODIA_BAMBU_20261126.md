---
tipo_documental: instrumento-de-pesquisa
estado_documental: em-revisao-documental
data_revisao: 2026-11-26
responsavel_curadoria: Fabio Takwara
titulo: "Inventário de custódia da coleção Bambu — fichas, fontes em disco e as 254 obras de Advances in Bamboo Science"
autor: Fabio Takwara
resumo: "Medição do que o acervo tem versionado, do que está custodiado em _privado e no Drive, e da ligação — hoje quebrada em 31 de 38 casos — entre a ficha e o PDF da fonte."
---

# INVENTÁRIO DE CUSTÓDIA — coleção Bambu

**Data da medição:** 26/11/2026 · **Medido por:** executor da frente Bambu Science
**Regra deste documento:** número sem comando ao lado é número não medido. Cada bloco traz o comando.

---

## 0. Por que este inventário existe

O roteiro anterior (`ROTEIRO_GAVETAS_BAMBU_20261126.md`) contou **74 arquivos** e o soberano corrigiu: 74 é o
tamanho de **uma gaveta**, não do acervo. Este documento mede o que existe de fato — fichas publicadas,
obras custodiadas e obras sem ficha — porque o plano das gavetas depende desse denominador.

---

## 1. O que está versionado no acervo público

```bash
gh api repos/takwaratec/acervo-soberania-tecnologica/git/trees/main?recursive=1 --jq '.tree[].path'
```

| medida | main hoje | corte do release 2026.1 (`b383b4d5`) |
|---|---|---|
| arquivos versionados | 827 | 459 |
| `.md` | 515 | 308 |
| `.md` em `docs/analyses` | **441** | 263 |

**Fichas por gaveta na main** (`git ls-files docs/analyses | cut -d/ -f3 | sort | uniq -c`): cobre 154 · bambu-estrutural 74 ·
reforma-agraria-agrofloresta 71 · pu-vegetal 41 · boro 31 · fundamentos 22 · bioeconomia-amazonica 18 ·
tecnologia-takwara 18 · visao-do-autor 18 · politica-habitacional 15 · cooperacao-brasil-china 14 ·
respaldo-academico 14 · percecao-social 9 · arquitetura-vernacular 7 · habitacao-social 7 ·
avaliacao-pos-ocupacao 5 · grandes-obras-amazonia 4.

**Tipo documental declarado** (`grep '^tipo_documental:'` sobre os 441 `.md`): **217** são `ficha-*`
(49 em bambu-estrutural, 64 em reforma-agrária, 33 em pu-vegetal, 24 na pasta `fichas/`); o resto são
índices, estados da arte, instrumentos e visões autorais.

**Lacunas de campo, medidas:**

- **99 de 441** declaram `doi:` — 342 não declaram;
- **38 de 441** declaram `pacote_fonte_privado:` — ou seja, **403 fichas não dizem onde está o PDF da fonte**;
- **264 de 441** declaram `fonte_primaria:` com texto livre ("PDF integral conferido" é o valor mais comum).
  Isso é declaração de conferência, não ponteiro: não há como abrir a fonte a partir da ficha.

---

## 2. O que está custodiado em disco (privado)

**`_privado/` do acervo** (`find _privado -name '*.pdf' | wc -l`):

| árvore | PDFs | extrações/txt | grupos |
|---|---|---|---|
| `fontes-academicas/` | 118 | 90 | 72 |
| `fontes-documentais/` | 833 | 355 | 49 |
| `fontes-cientificas/` | 20 | 15 | 4 |
| `fontes-externas-triagem-2026-08-21/` | 10 | 10 | — |
| **total** | **981** | **470** | **125 grupos** |

Entre os 125 grupos de fonte: **71 têm `extracao.md`**, **88 têm PDF**, e **52 não têm `metadados.json`**.
Grupo sem PDF são pastas de lote (normas, filas, agregados) — declaradas como tal, não como falha.

**`CustodiaAcervo/` no Drive** (conta `takwaratec@gmail.com`, escopo de custódia):

```bash
rclone lsjson -R gdrive-custodia: > inventario.json   # 385 objetos, 369 arquivos
rclone size gdrive-custodia:CustodiaAcervo/bambu-science-r1/pdf   # 254 objetos, 1.340 GiB
```

| pasta | conteúdo |
|---|---|
| `bambu-science-r1/pdf/` | **254 PDFs**, `BAM-001`…`BAM-254`, 1,34 GiB — nenhum fichado |
| `saneamento-mtcc-20261118/pdf/` | 50 PDFs (saneamento — outra frente) |
| `gaveta-graeber-wengrow/` | 15 originais + 6 em quarentena + manifesto SHA-256 |
| `motor-amostra6-20261121/` | 6 fichas, 3 pacotes de fonte, instrumento, pareceres |
| raiz | **7 lotes `.age`** (B1–B5, A-S1, C-S3) = 608,6 MB cifrados, **conteúdo não inventariável sem chave** |

**Isto é o achado do inventário:** a maior parte do material custodiado está em **`.age` cifrado** — 608 MB
que nenhum inventário pode abrir sem a chave de custódia. Declarado aqui como limite, não como zero.

---

## 3. A coleção Advances in Bamboo Science (254 obras)

**Estado:** custodiada, **zero fichada**. É o maior bloco de obra nova disponível ao motor.

Medido no exemplar `BAM-001`:

```bash
rclone copy gdrive-custodia:CustodiaAcervo/bambu-science-r1/pdf/BAM-001.pdf ./amostra/
python3.13 -c "import fitz;print(fitz.open('amostra/BAM-001.pdf')[0].get_text())"
# → "An overview of bamboo cultivation in Southern Italy", ScienceDirect
# → https://doi.org/10.1016/j.bamboo.2022.100002
```

- **camada de texto presente** — o PDF extrai texto (PyMuPDF), não precisa de OCR;
- **DOI impresso na página 1** — cada arquivo diz o próprio DOI, o que permite conferir identidade contra
  Crossref **sem** depender do nome do arquivo;
- Crossref resolve o DOI e devolve título, ano e licença (`tdm` do editor + `CC BY-NC-ND 4.0` neste caso).
  **Licença de leitura ≠ licença de republicação:** NC-ND impede uso derivado comercial e adaptação.

**Consequência para o plano:** o fichamento das 254 pode ser feito em regime de lote, com identidade
conferida por DOI impresso e por Crossref — que é justamente o protocolo que a
`acervo-descoberta-fontes-externas` exige.

---

## 4. Ligação ficha ↔ fonte custodiada — o número que mais importa

**38 fichas** declaram `pacote_fonte_privado`. Desse total:

- **7 resolvem exatamente** para um grupo que existe em disco;
- **31 apontam para um nome de pasta que não existe** (por exemplo `marcal-2018-normas-bambu` quando o
  grupo real é `2018-marcal-normas-internacionais-bambu`).

Isso não é fonte perdida: é **ponteiro quebrado**. A fonte existe; o caminho declarado na ficha é que não
resolve. É exatamente a classe de defeito que a auditoria de integridade da R4 tem de pegar — e explica
por que a ficha "íntegra" hoje não é verificável por quem não conhece a árvore de cor.

**Cobertura por DOI** (cruzando `doi:` da ficha com o DOI indexado em `metadados.json` dos grupos
custodiados): **35 de 99** fichas com DOI encontram o grupo correspondente. Em bambu-estrutural,
**16 de 36**.

---

## 5. O que este inventário NÃO mediu

1. **O conteúdo dos 608 MB cifrados** (`lote-*.age`) — exige chave; declarado como limite.
2. **A integridade dos 981 PDFs** — presença medida, `sha256` e `%%EOF` não. Integridade é trabalho da
   fase de reauditoria, não deste inventário.
3. **A identidade das 254 BAM uma a uma** — só a `BAM-001` foi aberta. As outras 253 estão medidas por
   quantidade, não por conteúdo.
4. **A cobertura temática das 254** — não há índice por tema; para saber quantas são de carbono, de
   estrutural ou de fitossanidade é preciso ler a página 1 de cada uma. É o primeiro passo do lote.
5. **O grau de novidade** — o que foi publicado depois destas 254 e não está no acervo é busca de
   atualização, prevista na fase 3 do plano, não medida aqui.

---

## 6. Vocabulário corrigido que este documento adota

- **seis fichas** foram o teste do motor; a PDMS é a sétima **da gaveta** e a única com ato de homologação;
- **74** é o tamanho de `bambu-estrutural`, não do acervo;
- **441** fichas `.md` em `docs/analyses` na main, das quais **217** são `ficha-*`;
- **254** obras de *Advances in Bamboo Science* custodiadas e não fichadas;
- **981** PDFs em `_privado/` + **254** no Drive + 7 lotes cifrados.

**Universo de curadoria declarado:** 217 fichas tipadas + 254 obras a fichar + 240 `.md` não-ficha que
também precisam de estado documental declarado = **~711 objetos** que o motor precisa alcançar.
