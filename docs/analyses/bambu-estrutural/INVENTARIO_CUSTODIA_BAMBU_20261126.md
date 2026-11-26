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
**Regra deste documento, e como ela se cumpre:** todo número traz (a) o comando que o reproduz **neste clone**,
ou (b) a marca **`[EXTERNO]`** quando o comando depende do Drive, de `_privado/` ou da chave de custódia — que
não estão versionados e por isso **não são verificáveis por um auditor externo**. A distinção não é retórica:
no primeiro caso o auditor refaz a conta; no segundo ele só pode registrar que a medição é afirmada pelo
executor. (Correção do achado P3 do Teco R1: a versão anterior prometia comando para todo número e não cumpria.)

---

## 0. Por que este inventário existe

O roteiro anterior (`ROTEIRO_GAVETAS_BAMBU_20261126.md`) contou **74 arquivos** e o soberano corrigiu: 74 é o
tamanho de **uma gaveta**, não do acervo. Este documento mede o que existe de fato — fichas publicadas,
obras custodiadas e obras sem ficha — porque o plano das gavetas depende desse denominador.

---

## 1. O que está versionado no acervo público

**Reprodutível neste clone:**

```bash
# a) inventário versionado no commit medido (main = d0bc531)
git -C <repo> ls-tree -r --name-only d0bc531 | grep -c '\.md$'
git -C <repo> ls-tree -r --name-only d0bc531 | grep '^docs/analyses/.*\.md$' | wc -l

# b) fichas por gaveta e por tipo, na gaveta estrutural — com a regra de classificação no próprio script
python3 docs/analyses/bambu-estrutural/scripts/contar_gaveta.py <repo>

# c) quantas fichas declaram cada campo (a regra é o regex, escrito aqui, não um adjetivo)
git -C <repo> grep -h '^tipo_documental: ficha' d0bc531 -- docs/analyses | wc -l
git -C <repo> grep -h '^doi:' d0bc531 -- docs/analyses | wc -l
git -C <repo> grep -h '^pacote_fonte_privado:' d0bc531 -- docs/analyses | wc -l
git -C <repo> grep -h '^fonte_primaria:' d0bc531 -- docs/analyses | wc -l
```

| medida | main hoje (`d0bc531`) | corte do release 2026.1 (`b383b4d5`) |
|---|---|---|
| arquivos versionados | 827 | 459 |
| `.md` | 515 | 308 |
| `.md` em `docs/analyses` | **441** | 263 |
| `tipo_documental: ficha*` em `docs/analyses` | **217** | — |
| declaram `doi:` | **99** | — |
| declaram `pacote_fonte_privado:` | **38** | — |
| declaram `fonte_primaria:` | **264** | — |

**Fichas por gaveta na main** — comando: `git ls-tree -r --name-only d0bc531 | grep '^docs/analyses/' | cut -d/ -f3 | sort | uniq -c`
→ cobre 154 · bambu-estrutural **74** · reforma-agraria-agrofloresta 71 · pu-vegetal 41 · boro 31 · fundamentos 22 ·
bioeconomia-amazonica 18 · tecnologia-takwara 18 · visao-do-autor 18 · politica-habitacional 15 ·
cooperacao-brasil-china 14 · respaldo-academico 14 · percecao-social 9 · arquitetura-vernacular 7 ·
habitacao-social 7 · avaliacao-pos-ocupacao 5 · grandes-obras-amazonia 4.

*Medido em `d0bc531` — o commit em que este documento entrou na `main`: **74** arquivos na gaveta. O número
**77** é a contagem do worktree de trabalho, que inclui os três instrumentos desta rodada (`ROTEIRO`,
`INVENTARIO`, `PLANO`) ainda não mergeados. 74 + 3 = 77. Quem repetir a medição depois do merge deste PR verá
77 e o motivo está aqui, não é divergência.*

**O que os campos dizem, e o que não dizem.** `fonte_primaria: "PDF integral conferido"` (o valor mais comum
entre os 264) é **declaração de conferência**, não ponteiro: não permite abrir a fonte a partir da ficha. Só
`pacote_fonte_privado` aponta para uma pasta — e apenas 38 fichas o declaram.

## 2. O que está custodiado em disco (privado)

**`_privado/` do acervo — `[EXTERNO]`, não versionado, medido pelo executor:**

```bash
find _privado -name '*.pdf' | wc -l                                   # 981
find _privado/<sub> -maxdepth 1 -type d | wc -l                        # grupos por árvore
find _privado/<sub> -maxdepth 2 -name 'extracao.md' | wc -l            # grupos com extração
find _privado/<sub> -maxdepth 2 -name 'metadados.json' | wc -l         # grupos com metadados
```

| árvore | PDFs | extrações/txt | grupos |
|---|---|---|---|
| `fontes-academicas/` | 118 | 90 | 72 |
| `fontes-documentais/` | 833 | 355 | 49 |
| `fontes-cientificas/` | 20 | 15 | 4 |
| `fontes-externas-triagem-2026-08-21/` | 10 | 10 | — |
| **total** | **981** | **470** | **125 grupos** |

Entre os 125 grupos de fonte: **71 têm `extracao.md`**, **88 têm PDF**, e **52 não têm `metadados.json`**.
Grupo sem PDF são pastas de lote (normas, filas, agregados) — declaradas como tal, não como falha.

**`CustodiaAcervo/` no Drive — `[EXTERNO]`** (conta `takwaratec@gmail.com`, escopo de custódia; exige `rclone` com
credencial que só o executor tem):

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
