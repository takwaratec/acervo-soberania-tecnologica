---
tipo_documental: documento-institucional
estado_documental: em-revisao-documental
data_revisao: 2026-11-26
responsavel_curadoria: Fabio Takwara
titulo: "Handoff de continuidade — sete fichas da homologação"
autor: Fabio Takwara
resumo: "Handoff ao executor: o que a branch entrega, o que declara e o que não pode repetir."
---

# HANDOFF DE CONTINUIDADE — sete fichas da homologação — ao executor da gaveta

```
SCHEMA=TAKWARATEC/HANDOFF/1
PARA=executor da gaveta bambu-estrutural (a quem a frente pertence)
DE=regente (Hermes) — assumiu a execução por ordem do soberano e agora devolve
DATA=2026-11-24
REPO=takwaratec/acervo-soberania-tecnologica
BRANCH=hermes/correcao-amostra6-20261122
HEAD=9c8f4fd
BASE=origin/main 7238b78 (merge do PR #109)
```

## 0. Por que este documento existe

O regente assumiu a execução desta frente — extração, correção de ficha, execução de régua — e **isso não era o
papel dele**. As sete fichas foram levadas até `PASS` por ele. A homologação é sua, e a continuidade a partir
daqui também. Este handoff entrega o que foi feito, onde está, e o que **você** tem de decidir.

Regra do soberano, para não repetir: o regente não corrige ficha. Se você encontrar erro de motor, constituição
do MTCC ou régua, é isso que volta para ele — não a ficha corrigida.

## 1. Onde o trabalho está

| item | valor |
|---|---|
| branch | `hermes/correcao-amostra6-20261122` (worktree `wt-acervo-amostra6`) |
| head | `9c8f4fd` |
| base | `origin/main` `7238b78` |
| push | feito (a branch está no `origin`) |
| PR | **não aberto** — abrir PR é ato seu |
| gate | `gate_fidelidade_fonte.py`, self-test **95** |

**Cinco fichas mudaram nesta branch.** `pdms` e `santos-2024` já estavam na `main` pelo PR #109 e **não** foram
tocadas aqui — o `PASS` delas vem do estado já publicado.

## 2. Blob de cada uma das sete (SHA do arquivo no head)

```
f112340  adier-2023-propriedades-tratamento-bambu.md
038d9a3  ficha-chen-2015-cu-moso-fitorremediacao.md
46701ed  ficha-liu-2015-pb-moso-fitorremediacao.md
59723ef  marcal-2018-normas-internacionais-bambu.md
0b4d060  ficha-heat-treatment-pdms-bamboo.md     (já na main pelo #109)
46fa767  santos-2024-poetica-narrativa-tectonica-bambu.md (já na main pelo #109)
2453291  ficha-acv-bambu-unesp-araujo2025.md
```

## 3. O que foi corrigido, e contra qual fonte

| ficha | correção | procedência |
|---|---|---|
| `adier` | `50–220` é **MOR** (flexão), não compressão; `MOE` saiu por ser colateral | coluna MOR na p. 24, medida por coordenada (x=306,8; valor em x=314,6) |
| `adier` | removidos `1100` (tabela de slivers, p. 13) e `147` (tração, p. 22) | conferido no PDF |
| `marcal` | removido `2011` (ano da dissertação); entrou **maio de 2010** | p. 155, texto literal |
| `acv` | inventário sem página → **Tabela 1, p. 7** | derivado, linha 334 |
| `acv` | cinco resultados sem página: `25%`, `93%`, `91%` (p. 7) e `4%` (p. 8) | derivado, linhas 332/389/393/414 |
| `chen` | histórico de versão deixou de ser lido como resultado | marcador `<!-- tipo: histórico -->` na tabela |
| `liu` | idem; 12 resultados (as 6 doses de `µmol/L` são protocolo) | idem |
| `pdms` | página em coluna própria da tabela passa a valer | 49 de 102 itens estavam sem página |

## 4. Estado medido — e o que ele NÃO significa

> **VENCIDO em 26/11/2026.** A medição desta seção é a de 24/11, com o instrumento anterior (`54691508`, self-test
> 95). Ela não descreve o corpus de hoje: depois do #135, as sete saem **seis `PASS` e uma `NAO_VERIFICAVEL`**
> (`pdms`), com 864 números, 694 afirmações de resultado e 859 aprovadas — ver §9. O texto abaixo fica como
> registro do que se mediu em 24/11, não como estado vigente.

Corpus 74 no head **em 24/11**: `PASS 12 · PARCIAL 45 · SEM_FONTE 2 · NAO_VERIFICAVEL 5 · FAIL 1` (soma 74).

**As sete estavam `PASS` em 24/11. Isso nunca foi homologação.** `PASS` significa que o gate encontrou o número
na página declarada e que a unidade confere. Não significa que a frase da ficha é a frase da fonte.

## 5. Limites que você herda — não são defeitos para consertar

1. **`acv`: 8 itens do inventário** em `NAO_VERIFICAVEL` (6) e `APROVADO_SEM_UNIDADE` (2). A Tabela 1 foi
   achatada na extração: unidade e quantidade caem em linhas separadas. **Não foi anotada coordenada de
   propósito** — anotar 8 valores de inventário só para fechar a ficha seria corrigir para o gate gostar.
   O valor está na ficha, a unidade está na fonte, o vínculo não foi confirmado.
2. **`adier`**: a atribuição da unidade depende de anotação por coordenada no derivado
   (`<!-- coluna: … -->` e `<!-- coluna-usada: … -->`), que **vive na fonte privada**, não no repositório. É
   método auditável, mas fora do repo.
3. **A régua prova presença do valor na página declarada** — não prova que a página sustenta a afirmação.
4. **Asserções de citação são atestação humana**, não medida da régua.

## 6. O pacote de leitura humana

```
docs/homologacao/amostra-6-20261124/AMOSTRA6_FICHAS_20261124.html   1.387.979 bytes · 74 fichas · sha256 e5da90cb…a374
docs/homologacao/amostra-6-20261124/LEIA-ME.md
```

Documento de leitura: não homologa nada, não altera ficha. Foi entregue ao soberano.

## 7. O que é seu agora

1. **Revisar o que foi feito** — os cinco diffs de ficha desta branch. Você é quem responde por elas.
2. **Abrir o PR** desta branch para a `main` se aceitar o estado (o regente não abre PR de ficha).
3. **Homologar** as sete por leitura. É ato seu, não do gate.
4. **Declarar** ao regente, se houver, qualquer coisa que pareça erro de **motor, constituição do MTCC ou
   régua** — inclusive se discordar de alguma das correções acima. Vai como achado de régua, não como ficha
   consertada.

## 8. O que você NÃO deve fazer

- Não reabrir correção para "passar no gate": o gate mede, não manda.
- Não anotar coordenada nos 8 itens do inventário do `acv` para fechar a ficha.
- Não repetir a tentativa que já falhou duas vezes: ler unidade do cabeçalho da ficha aplicou `t` (tonelada) de
  `T (°C)` a 45 valores da `pdms`; ler "o cabeçalho acima" no texto devolveu letras soltas.
- Não tratar `PASS` como homologação.

## 9. Nota de 26/11/2026 — o incremento entrou (PR #135)

Este handoff foi escrito em 24/11, quando as sete estavam no estado medido por um gate que só lia prosa. Em
25/11 o instrumento foi corrigido (A1: a página passou a valer para a **linha** da tabela) e em 26/11 o **#135
entrou na main** (`096fc26`) com as sete incrementadas.

O que mudou para quem lê este handoff:

- **As contagens da §2 do pacote não são mais as de 24/11.** Hoje: `numeros_na_ficha` **864**,
  `afirmações de resultado` **694**, **859 aprovadas**. Seis `PASS`, e o `pdms` em **`NAO_VERIFICAVEL`** por
  3 células cuja unidade a fonte não declara na ocorrência.
- **A lista do §8 continua valendo inteira.** O que era proibido em 24/11 continua proibido: nada de coordenada
  inventada, nada de unidade lida do cabeçalho, nada de `PASS` tratado como homologação.
- **O que este handoff não sabia e agora está declarado como limite:** a Tabela 2 do `pdms` (cor em CIELAB,
  p. 43444) **não foi transcrita** — a extração a entrega com colunas deslocadas (`b*` sairia −808,86), e
  transcrever daria aparência de precisão a extração errada. Fechar exige reextração da página.
- **A homologação continua sendo sua, por leitura.** O gate mediu onde o número está; não mediu se a frase da
  ficha é a frase da fonte. `PASS` não é homologação.
- **Uma das sete já tem ato de homologação, e este pacote não o altera:** a **PDMS** é
  `homologado-documentalmente` desde 21/11/2026 (`FABIO_SOBERANO`, decisão opção 1, governança `9e851095`). As
  outras **seis** seguem `em-revisao-documental`. Corrigido em 26/11: a versão anterior desta nota dizia
  «nenhuma das sete», e isso era falso para a PDMS.
- **Este pacote substitui o PR #134.** Ele nasceu sobre a `main` que já contém o #135 (`096fc26`) e é o que deve
  ser lido; o #134 carrega as fichas em versão anterior ao incremento e não deve ser mergeado.
