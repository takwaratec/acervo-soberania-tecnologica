# Conflito de registro — a frente CÁLCULADORA já existe, com outro repositório e outro escopo

**Data:** 28/11/2026 · **Estado:** bloqueio declarado, aguardando decisão do soberano
**Motivo:** antes de abrir frente/gaveta, o protocolo exige ler o registro. O registro tem conflito.

---

## 1. O que o registro declara hoje

`MAPA_DE_FRENTES_R4.json`, entrada `CALCULADORA`:

```
id:           CALCULADORA
nome:         "Calculadora de Domos — reparo e aprimoramento"
escopo:       "aplicativo de cálculo de domos geodésicos: geometria, quantitativos,
               consumo de cabo, PU vegetal, PU expansivo e conectores; coerência entre
               interface e backend"
nao_faz:      "não publica número que não reproduz; não altera memorial nem proposta;
               não inventa coeficiente sem fonte"
repo:         Resck/Takwara-Tech          ← repositório DIFERENTE
write_scope:  overrides/**, docs/**, Chatbot_Takwara/backend-api/**
prioridade:   P2
bootstrap:    CONSOME_NAO_ELABORA
```

E ela também está em `REGISTRO_FRENTES.json` (portal), com declaração em
`portal/declaracoes/CALCULADORA.json` — **arquivo que não existe no `origin/main`** (a entrada aponta
para uma declaração ausente).

## 2. O que a aponta para o material de hoje

O contrato `CALC-CALCULADORA-DOMOS-SEGMENTO-20261118-R1`, no ledger, declara
`repository: takwaratec/TakwaraTec-Acervo-Web` e `front: CALCULADORA`.
Ou seja: **o material desta semana foi escrito sob o rótulo `CALCULADORA`, num terceiro repositório**
que não é nem o do mapa (`Resck/Takwara-Tech`) nem o do acervo.

## 3. Três conflitos, e cada um bloqueia um passo diferente

| # | conflito | efeito |
|---|---|---|
| **C1** | `CALCULADORA` já tem dono (`Resck/Takwara-Tech`) e escopo declarado (`overrides/`, `docs/`, `Chatbot_Takwara/backend-api/`) | abrir gaveta do acervo sob o mesmo nome **duplica dono**; o gate A9.2 recusa sobreposição |
| **C2** | o catálogo de gavetas `GAVETAS_R4.json` **não tem** `cupulas-geodesicas` — nem em vigentes nem em declaradas-sem-conteúdo | o runner **recusa** o escopo `docs/analyses/cupulas-geodesicas` até a gaveta entrar no catálogo, no mesmo ato |
| **C3** | a frente que hoje se chama `CALCULADORA` no contrato é, na prática, **outro objeto**: cálculo de geometria e quantitativos x corpus científico de cúpulas | nome de frente descrevendo dois objetos é exatamente o defeito que o protocolo bane |

**Consequência:** não posso abrir frente nem escopo enquanto o soberano não decidir qual frente é dona
da gaveta `cupulas-geodesicas`. Abrir por conta própria seria criar a quarta porta de autoridade.

## 4. O que eu já medi e não bloqueia

| item | estado |
|---|---|
| worktree nova a partir de `origin/main` (`a34d427`) | **feita** — `hermes/cupulas-geodesicas-corpus-20261128-r1`, isolada, sem tocar no cobre |
| relatório de corpus | **entregue** em `docs/cupulas-geodesicas/00-relatorio-de-corpus.md` (commit `2a05127`, branch publicada) |
| prefixo `CALCULADORA` no conjunto fechado | **existe** — mas com o escopo do app, não do corpus |
| runner e catálogo | localizados no worktree `r4-transicao-20261102-r1`; catálogo vigente lido |

**Nota sobre a árvore:** o relatório foi escrito em `docs/cupulas-geodesicas/` **antes** de o catálogo
ser conferido. Pelo `validar_gaveta`, o escopo correto para o acervo é `docs/analyses/<gaveta>/`. Se o
soberano confirmar a gaveta, o caminho tem de **migrar** para `docs/analyses/cupulas-geodesicas/` no
mesmo ato em que a gaveta entra no catálogo — três coisas juntas, senão o gate recusa o escopo certo.

## 5. As duas saídas, com o custo de cada uma

### Saída A — frente nova, nome novo: `CUPULAS-GEODESICAS`

- Abre frente própria com `repo: takwaratec/acervo-soberania-tecnologica` e escopo
  `docs/analyses/cupulas-geodesicas` + `_privado/governanca-operacional/extracoes/cupulas-geodesicas`.
- `CALCULADORA` continua sendo o app (`Resck/Takwara-Tech`) — **sem alteração**, sem emenda, sem dono duplicado.
- Exige **emenda de um valor** no conjunto fechado de prefixos (entra `CUPULAS-GEODESICAS`), declarada
  no mesmo ato, com a linha antes e depois.
- Exige entrada da gaveta no `GAVETAS_R4.json` na lista `GAVETAS_DECLARADAS_SEM_CONTEUDO_MEDIDO`
  (a gaveta ainda não tem conteúdo publicado).
- **Custo:** uma emenda de registro + uma entrada de catálogo + migrar o relatório de pasta.

### Saída B — reusar `CALCULADORA` e ampliar o escopo dela

- Emenda o `write_scope` de `CALCULADORA` para incluir `docs/analyses/cupulas-geodesicas/**` e troca o
  `repo` para o acervo — ou mantém dois repos, que o protocolo desaconselha explicitamente.
- **Custo:** altera frente existente (que é de outro repo e outro propósito), e "cálculo de domos" passa
  a significar também "corpus científico de cúpulas" — nome que descreve dois objetos.
- **Não recomendo.** O protocolo diz que frente nomeada pela ferramenta vira duplicata da frente que
  trata o objeto.

---

## 6. Dois pedidos de decisão, e um alerta sobre a árvore errada

1. **Qual saída.** Recomendo a **A**: frente nova `CUPULAS-GEODESICAS`, `CALCULADORA` intocada.
2. **Confirmação do nome da gaveta em disco:** `docs/analyses/cupulas-geodesicas` (slug) com o rótulo
   humano **"Cúpulas Geodésicas"** no NAV. O slug é o que o gate compara; o rótulo é o que o leitor vê.

**Alerta operacional, e é meu erro:** o commit da apuração de migração (`8d58185f`) foi gravado no
worktree `_worktrees/r4-transicao-20261102-r1`, que é uma worktree do **Laboratório-Editorial** e está
numa branch de outra frente (`hermes/gaveta-soberania-social-catalogo-r1`). A apuração é documento de
trabalho e não contaminou nada versionado de outra frente, mas **o lugar estava errado**. Pergunto se o
senhor quer que eu o mova para o repositório de governança correto (`ops/command-center/task-results/`
do Laboratório, em branch própria) antes de qualquer outra ação.

Nada mais será escrito até a decisão. O que já existe de escrito está publicado na branch
`hermes/cupulas-geodesicas-corpus-20261128-r1` do acervo, e é só o relatório.
