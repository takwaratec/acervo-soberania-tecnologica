---
tipo_documental: documento-institucional
estado_documental: em-revisao-documental
data_revisao: 2026-11-24
responsavel_curadoria: Fabio Takwara
titulo: "Amostra 6 — pacote de homologação por leitura humana"
autor: Fabio Takwara
resumo: "Pacote de leitura das sete fichas da gaveta bambu-estrutural submetidas a homologação."
---

# AMOSTRA 6 — pacote de homologação por leitura humana

## 0. Estado declarado — posterioridade ao PR #133

Este pacote foi montado em 2026-11-24, quando onze fichas da gaveta ainda carregavam o rótulo
`homologado-documentalmente`. Em 2026-11-25 o soberano mandou **rebaixar as onze**, e o acervo as
devolveu a `em-revisao-documental` (PR #133, `a5c6af6`): nenhuma delas tinha `autorizacao_homologacao`
no front matter, e homologação é ato do soberano, não estado que se declara. A única ficha com ato
registrado é a PDMS (`FABIO_SOBERANO`, 21/11/2026, `9e851095`).

O `AMOSTRA6_FICHAS_20261124.html` foi regerado com esse rebaixamento refletido: o índice mostrava 12
fichas como homologadas e agora mostra 74 em revisão. **Rótulo no front matter não é homologação.** Nenhuma
das sete submetidas neste pacote recebeu ou perdeu estado por esta nota — elas continuam `em-revisao-documental`,
e o que este pacote oferece ao soberano é a leitura, não o carimbo.

```
DATA=2026-11-24
BASE=acervo, branch hermes/bambu-7fichas-rebase-a5c6af6-20261125, base a5c6af6 (com o rebaixamento do #133)
DOCUMENTO=docs/homologacao/amostra-6-20261124/AMOSTRA6_FICHAS_20261124.html
DOCUMENTO_REGERADO=2026-11-25, so o estado das fichas no indice (12 homologado-documentalmente -> 74 em-revisao-documental)
SHA256=9caf11f48fbc88d497f4678ac851524c9e8c8cb3ced3bda4be40fd93920866bb
TAMANHO=1.387.787 bytes · 74 fichas em arquivo único, sem requisição de rede
GATE=gate_fidelidade_fonte.py, self-test 95 (main do portão 917886f2 + O5 + O3)
```

## 1. O que este documento é

Um arquivo só, com as **74 fichas da gaveta** `docs/analyses/bambu-estrutural/`, geradas do markdown
versionado. Cada título abre a ficha no próprio documento; cada ficha mostra frontmatter, seções numeradas e
tabelas como estão no markdown. **Não homologa nada e não altera nenhuma ficha.**

## 2. As seis da amostra — estado medido pelo gate

| ficha | estado | itens | afirmações de resultado |
|---|---|---|---|
| `adier-2023` | `PASS` | 5 | 5 |
| `ficha-chen-2015` | `PASS` | 28 | 12 |
| `ficha-liu-2015` | `PASS` | 22 | 12 |
| `marcal-2018` | `PASS` | 3 | 2 |
| `ficha-heat-treatment-pdms` | `PASS` | 90 | 41 |
| `santos-2024` | `PASS` | 12 | 11 |
| `ficha-acv-bambu-unesp-araujo2025` | `PASS` | 12 aprovados + 8 não confirmados | 4 |

## 3. O que mudou nas seis, ficha por ficha

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

## 4. Limites declarados — onde a régua NÃO confirma

1. **`acv`: 8 itens do inventário** em `NAO_VERIFICAVEL` (6) e `APROVADO_SEM_UNIDADE` (2). A Tabela 1 foi
   achatada na extração: unidade e quantidade caem em linhas separadas. **Não anotei coordenada** — seria
   corrigir para o gate gostar. O valor está na ficha, a unidade está na fonte, e a régua não confirma o
   vínculo.
2. **`ficha-chen-2015` / `ficha-liu-2015`**: 12 afirmações de resultado cada, conferidas **na página
   declarada**. Isso prova que o valor existe ali; **não** prova que a página sustenta a afirmação.
3. **Asserções de citação são atestação humana**, não medida da régua.
4. A reprodução do documento não prova o gerador; o inspetor de DOM não prova o conteúdo.

## 5. O que a leitura humana decide

Este pacote existe porque a homologação **depende da leitura humana**. O gate diz onde o número está e se a
unidade confere; ele não diz se a frase da ficha é a frase da fonte. Quem homologa lê a ficha e diz.

## 6. Reprodução

```
cd docs/analyses/bambu-estrutural
python3 gate_fidelidade_fonte.py --dir . --glob '*.md' --fontes <raiz-privada> --json
```

`<raiz-privada>` = `_privado/fontes-academicas,_privado/fontes-documentais,_privado/fontes-científicas`.

## 7. Re-medição em 2026-11-25, com o gate corrigido (A1)

O gate desta frente foi corrigido hoje: a página passou a valer para a **linha** da tabela, e não só
para a primeira célula (PR #210 no laboratório de governança). Medido com ele, o estado das sete:

| ficha | estado | afirmações de resultado | com página | sem página |
|---|---|---|---|---|
| `adier-2023` | `PASS` | 9 | 9 | 0 |
| `ficha-acv-bambu-unesp-araujo2025` | `PARCIAL` | 9 | 8 | 1 |
| `ficha-chen-2015` | `PASS` | 12 | 12 | 0 |
| `ficha-heat-treatment-pdms` | `PASS` | 41 | 41 | 0 |
| `ficha-liu-2015` | `PASS` | 12 | 12 | 0 |
| `marcal-2018` | `PASS` | 2 | 2 | 0 |
| `santos-2024` | `PASS` | 11 | 11 | 0 |

A tabela do §2 acima é a medição de 24/11 com o gate anterior e **não deve ser lida como estado atual**.
A única que ainda cai é a ACV, e por um item só: continua `PARCIAL` porque a Tabela 2 foi transcrita como
bloco literal — o formato que o gate antigo premiava. O conteúdo está lá; o que falta é a transcrição em
formato de tabela, que é trabalho de ficha, não de pacote.
