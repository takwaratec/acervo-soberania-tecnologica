---
tipo_documental: instrumento-de-pesquisa
titulo: "Registro de estado — frente BAMBU-BAMBUSC / PR #99"
estado_documental: em-revisao-documental
data_revisao: 2026-11-19
responsavel_curadoria: Fabio Takwara
gaveta: bambusc-catalogo-20261119
fonte_primaria: "estado e incidente de extracao registrados na rodada 1 do catalogo BambuSC; o conteudo medido esta nos arquivos de prova deste diretorio"
declaracao_ia: "produção assistida por inteligência artificial; conferência na fonte e responsabilidade de homologação são humanas"
---

# Registro de estado — frente BAMBU-BAMBUSC / PR #99

```
FRENTE=BAMBU-BAMBUSC
TASK=BAMBU-BAMBUSC-CATALOGO-20261119-R1
PR=https://github.com/takwaratec/acervo-soberania-tecnologica/pull/99
BRANCH=bambusc/catalogo-20261119-r1
HEAD=9fee0bef6c4d12cb6781290557dcd7438bf50279
MERGE_DO_PR=AUTORIZADO_POR_FABIO (2026-11-19) — ainda NAO executado
TARGET=SOL (auditoria externa, leitura do GitHub)
```

## O que o PR entrega agora (13 arquivos, 1447 linhas)

Tudo em `docs/analyses/bambusc-catalogo-20261119/`:

| arquivo | conteúdo |
|---|---|
| `00_COMO_AUDITAR.md` | a porta: clone, comando, três desfechos, o que é e não é conferível |
| `01_IDENTIDADE_E_CONTRATO.md` | 11 obras, autores, ano, DOI/ISBN, páginas, licença, sha256 do PDF |
| `02_CONTRATO_DE_LEITURA.md` | por obra: limites e "o que não autoriza concluir" |
| `03_MATRIZ_POR_EIXO.md` | 11 obras × 12 eixos, território, convergências, divergências, método |
| `04_ESTADO_DA_ARTE_DAS_FICHAS.md` | síntese exploratória com recorte e limite declarados |
| `arquivos-prova/CITACOES_DE_PROVA.{md,json}` | **27 citações literais com página** — cada número publicado |
| `INDICE_FICHAS.json` | índice por máquina + sha256 dos 11 PDFs privados |
| `PACOTE_AUDITORIA.json` | inventário com sha256/bytes e commit de geração |
| `conferir_pacote.py` | verificador: exit 0 confere / 1 diverge nomeando / 2 não mediu |
| `gerar_pacote.py` | gerador do manifesto (exclui a si mesmo e ao manifesto, por impossibilidade) |
| `PORTA_AUDITORIA_SOL.md` | âncoras do despacho: commit, sha do ledger, desvios |
| `README.md` | registro auditável da rodada 1 |

## Por que binário não vai junto (decisão de direito, não de conveniência)

`_privado/` é ignorado pelo git (`.gitignore:28`) e **10 das 11 obras não declaram
licença** — a única com licença explícita é Jaramillo et al. 2020 (CC BY). Republicar o PDF
seria presumir direito. O que se publica é o **registro de leitura**: trecho curto com
página (verificação) + sha256 do binário (conferível por quem tem a custódia).

## Provas rodadas no clone do auditor

- Clone completo do remoto, `checkout FETCH_HEAD` no `bambusc/catalogo-20261119-r1`:
  `conferir_pacote.py --repo .` → **exit 0, 7/7**.
- Controle negativo no mesmo clone: injetado `<!-- injecao -->` em `03_MATRIZ_POR_EIXO.md`
  → **exit 1**, nomeando sha esperado `e8b94e2f…` e medido `f516e5cc…`, e o tamanho (5716 B
  vs 5734 B). Restaurado por `git checkout --` → **exit 0, 7/7**.
- `clone --depth 1` NÃO traz o branch da frente e o verificador responde `exit 2`
  (não consegui medir) — motivo pelo qual a porta exige clone completo.

## Incidente declarado — e consertado

Durante o push, o worktree principal do acervo **saltou para outro estado**: o `checkout`
na raiz foi para `main`, o commit `564110cc` (que carrega o pacote) foi criado **em cima de
`main` local**, e o `main` local passou a apontar `564110cc` — commit que **não é ancestral
de `origin/main`** e cuja árvore não tem o conteúdo atual da linha principal (o merge de
teste indicou 89 arquivos e −11.922 linhas).

Medidas:

1. **Nada foi empurrado para `main` do GitHub.** O `push` para a frente foi recusado por
   non-fast-forward exatamente por isso.
2. `main` local foi **revertido** para `origin/main` (`0b6cbd4`) com `update-ref` de CAS
   (`564110cc` → `0b6cbd4`), preservando o argumento antigo.
3. O pacote foi levado ao branch da frente por **`cherry-pick 564110cc`** sobre `23233fa`,
   gerando `9fee0be`, publicado em fast-forward.
4. `564110cc` vive só na zona efêmera (reflog); não é alcançável de `origin/main` nem do
   branch da frente. Nenhum conteúdo se perdeu — o `9fee0be` carrega os mesmos 11 arquivos.
5. **Não houve `push --force` em nenhum momento.**

Efeito no push de merge: o PR **não** é fast-forward de `main` (a base do README é
`0b6cbd4`, e o `main` andou até `0b6cbd4` — na verdade é a mesma base). O merge deve ser
feito pela interface do GitHub ou por `git merge` local; **não** por fast-forward cego.
