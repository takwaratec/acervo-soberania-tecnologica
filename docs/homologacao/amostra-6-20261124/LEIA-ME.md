---
tipo_documental: documento-institucional
estado_documental: em-revisao-documental
data_revisao: 2026-11-26
responsavel_curadoria: Fabio Takwara
titulo: "Amostra 6 — pacote de homologação por leitura humana"
autor: Fabio Takwara
resumo: "Pacote de leitura das sete fichas da gaveta bambu-estrutural submetidas a homologação, atualizado depois do incremento de 25/11."
---

# AMOSTRA 6 — pacote de homologação por leitura humana

## 0-bis. Estado declarado — posterioridade ao #133 **e ao #135**

Este pacote foi montado em 2026-11-24, quando onze fichas da gaveta ainda carregavam o rótulo
`homologado-documentalmente`. Em 2026-11-25 o soberano mandou **rebaixar as onze**, e o acervo as devolveu a
`em-revisao-documental` (PR #133, `a5c6af6`): nenhuma delas tinha `autorizacao_homologacao` no front matter, e
homologação é ato do soberano, não estado que se declara. A única ficha com ato registrado é a PDMS
(`FABIO_SOBERANO`, 21/11/2026, `9e851095`).

**Em 26/11/2026 o #135 entrou na main (`096fc26`) e incrementou as sete fichas**: tabelas transcritas com
página por linha, contagens medidas pelo gate corrigido (A1). Este pacote foi **regerado a partir daquele
commit** — os três agregados HTML e as duas tabelas deste arquivo descrevem o estado que a main tem agora, não o
de 24/11. **Nenhuma ficha mudou de estado por causa disso**: todas seguem `em-revisao-documental`.

```
DATA=2026-11-24 · PACOTE REGERADO=2026-11-26
BASE=acervo main 096fc26 (merge do #135), cortada de a5c6af6 (merge do #133) · branch de integração hermes/bambu-pacote-apos-135-20261126
DOCUMENTO=docs/homologacao/amostra-6-20261124/AMOSTRA6_FICHAS_20261124.html
SHA256=dd8f6bac395013f63bd2bd53acff7c0cd52fecf73a97598829b5302ac696a318
TAMANHO=1.424.131 bytes · 74 fichas em arquivo único, sem requisição de rede
PECA=docs/homologacao/amostra-6-20261124/PECA_SETE_MOLDE_20261125.html · sha256 bb8c09d253cbbbeb… · 135.017 bytes · 10 abas · 864 números · 859 aprovadas
SETE=docs/homologacao/amostra-6-20261124/FICHAS_HOMOLOGACAO_SETE_20261124.html · sha256 7319a245… · 106.846 bytes · 7 artigos · 864 itens
GATE=gate_fidelidade_fonte.py, sha256 do byte a16eb44a, self-test 96 (correção A1, PR #210)
DENOMINADORES=numeros_na_ficha=864 · afirmacoes_resultado=694 · aprovadas=859
```

## 1. O que este documento é

Um arquivo só, com as **74 fichas da gaveta** `docs/analyses/bambu-estrutural/`, geradas do markdown
versionado no commit `096fc26` (main com o #135). Cada título abre a ficha no próprio documento; cada ficha mostra frontmatter, seções numeradas e
tabelas como estão no markdown. **Não homologa nada e não altera nenhuma ficha.**

## 2. As sete da amostra — estado medido pelo gate (26/11/2026, pós-#135)

Duas réguas, dois nomes: `numeros_na_ficha` conta todo número do texto (inclusive referência e página);
`afirmações de resultado` conta só o que o instrumento classifica como resultado.

| ficha | estado | números na ficha | afirmações de resultado | aprovadas |
|---|---|---|---|---|
| `adier-2023` | `PASS` | 210 | 171 | 209 |
| `ficha-chen-2015` | `PASS` | 83 | 62 | 82 |
| `ficha-liu-2015` | `PASS` | 64 | 54 | 64 |
| `marcal-2018` | `PASS` | 27 | 24 | 27 |
| `ficha-heat-treatment-pdms` | **`NAO_VERIFICAVEL`** | 269 | 180 | 266 |
| `santos-2024` | `PASS` | 21 | 19 | 21 |
| `ficha-acv-bambu-unesp-araujo2025` | `PASS` | 190 | 184 | 190 |
| **total** | **6 `PASS` + 1 `NAO_VERIFICAVEL`** | **864** | **694** | **859** |

`pdms` não é `PASS` e não será apresentada como tal: 3 células ficaram `APROVADO_SEM_UNIDADE` porque a fonte
não declara a unidade na ocorrência (2,72%; 0,97%; 0,40% — o percentual está no título da tabela). **`PASS` não
é homologação:** nenhuma destas sete tem `autorizacao_homologacao`.

## 3. O que mudou nas sete, ficha por ficha

**Correções de 24/11** (continuam valendo — foram fidelidade à fonte, não ajuste ao instrumento):

| ficha | correção | procedência |
|---|---|---|
| `adier` | `50–220` era atribuído a compressão; é **MOR** | coluna MOR na p. 24 (x=306,8; valor em x=314,6) |
| `adier` | removidos `1100` (tabela de slivers, p. 13) e `147` (tração, p. 22) — não eram faixa de P. edulis | conferido no PDF |
| `marcal` | removido `2011` (era o ano da dissertação) e acrescentado **maio de 2010** | p. 155, texto literal |
| `acv` | inventário sem página → **Tabela 1, p. 7** | derivado, linha 334 |
| `acv` | cinco resultados sem página: `25%`, `93%`, `91%` (p. 7) e `4%` (p. 8) | derivado, linhas 332/389/393/414 |
| `chen` | histórico de versão deixou de ser lido como resultado | marcador de tipo na tabela |
| `liu` | idem; 12 resultados (as 6 doses de `µmol/L` são protocolo, não resultado) | |
| `pdms` | página em coluna própria da tabela passou a valer | 49 de 102 itens estavam sem página |

**Incremento de 25/11 (#135)** — tabelas novas, com página por linha, e erros de página encontrados ao remedir:

| ficha | o que entrou | o que estava errado e foi corrigido |
|---|---|---|
| `adier` | Tabela 6 (29 referências, p. 24) em duas tabelas: as três atribuições provadas e a transcrição integral sem rótulo de coluna | `226,28` e `423,29` saíam divergentes porque os decimais estavam em negrito; `191.61-423.29` trocou hífen pelo travessão da fonte — 14 valores voltaram a conferir |
| `acv` | Tabela 1 (inventário, coluna `Unity`, p. 7) e Tabela 2 (8 materiais × 7 categorias ReCiPe, p. 9) | a Tabela 2 em bloco literal virou markdown com coluna `Pág.` |
| `chen` | Tabela 2 (biomassa, BAF e TF, cinco doses, p. 3) | 13 valores estavam declarados em `p. 4, 5` e a tabela é da `p. 3` |
| `liu` | concentrações por tecido somadas a TF/BCF, sete tratamentos (p. 126) | 9 valores estavam em `p. 125` e a tabela é da `p. 126` |
| `marcal` | esforços admissíveis e módulos das normas colombiana (p. 132), peruana (p. 138) e equatoriana (p. 139) | flexão admissível de 5 MPa no Peru contra 15 MPa nas outras duas — a tabela que muda decisão de projeto |
| `pdms` | Tabela 1 completa: 5 temperaturas × 3 umidades × 3 direções (p. 43441) | — |
| `santos` | os três casos em tabela, com dimensão e página por linha (p. 84/97/110) | `716m²` colado era lido como símbolo; reescrito por extenso |

**Regra que valeu em todas:** onde a coluna não é provada pela fonte, a célula não recebe atribuição. Nenhuma
coluna foi inferida por posição.

## 4. Limites declarados — onde a régua NÃO confirma

1. **`pdms`: a Tabela 2 (cor em CIELAB, p. 43444) não foi transcrita.** A extração a entrega com colunas
   deslocadas — `b*` do controle sairia −808,86 e `DL*` a 120 °C, 173,98, fora do domínio de um espaço
   cromático em que `b*` varia na casa das dezenas. Fechar exige reextração da página; é pendência de custódia,
   não de curadoria.
2. **`pdms`: 3 células `APROVADO_SEM_UNIDADE`** (2,72%; 0,97%; 0,40%). O percentual está no título da tabela, e
   o instrumento não associa unidade de cabeçalho. Não devolvi a unidade por dedução.
3. **`marcal`: a Tabela 13** (módulos da norma equatoriana) **não foi transcrita** — a extração a entrega fora
   de ordem, e transcrever por posição seria adivinhar coluna.
4. **`adier`: 26 das 29 referências da Tabela 6** ficam com valor literal e **sem atribuição de propriedade**,
   porque a extração não preserva a grade da tabela.
5. **A régua prova presença do valor na página declarada** — não prova que a página sustenta a afirmação.
   Asserções de citação continuam sendo atestação humana, não medida.
6. A reprodução do documento não prova o gerador; o inspetor de DOM não prova o conteúdo.

## 5. O que a leitura humana decide

Este pacote existe porque a homologação **depende da leitura humana**. O gate diz onde o número está e se a
unidade confere; ele não diz se a frase da ficha é a frase da fonte. Quem homologa lê a ficha e diz.

## 6. Reprodução

```bash
# o gate tem de rodar da PRÓPRIA árvore (ops/command-center/metodo/), senão quatro fichas viram SEM_FONTE
cd <governanca>/ops/command-center/metodo
python3 gate_fidelidade_fonte.py --self-test      # 96 asserções, PASS
python3 gate_fidelidade_fonte.py \
  --dir <acervo>/docs/analyses/bambu-estrutural --glob '*.md' \
  --fontes <acervo>/_privado/fontes-academicas,<acervo>/_privado/fontes-documentais,<acervo>/_privado/fontes-cientificas \
  --json
# esperado: 6 PASS + pdms NAO_VERIFICAVEL · 864 numeros_na_ficha · 694 afirmacoes_resultado · 859 aprovadas
```

`SEM_FONTE` na saída significa gate fora da própria árvore, não fonte ausente.

