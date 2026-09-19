# Governança de Roteamento de Modelos TakwaraTec R1

Status: política vinculante candidata à auditoria independente e à chancela humana.
Escopo: execução de GOALs e tarefas de governança, documentação e engenharia neste repositório.

## 1. Princípios de execução

### SCRIPT_FIRST

Toda tarefa determinística deve verificar primeiro se shell, Python, parser, diff ou hash resolve a necessidade sem LLM. LLM não deve substituir uma transformação ou validação mecanicamente especificável.

### LOWEST_RELIABLE_COST

Usar o menor nível de custo e raciocínio capaz de executar a tarefa com confiabilidade. A economia não autoriza reduzir validação, rastreabilidade, segurança ou revisão humana.

### AGENT != MODEL

`AGENT` identifica o executor operacional. `MODEL` identifica o modelo de inferência utilizado pelo agente. Os campos devem permanecer distintos em toda declaração de GOAL.

### MODEL_ID_VALIDATED_ONLY

Nunca recomendar modelo por alias presumido. `MODEL` deve ser o ID exato previamente validado no provider ou `TO_BE_RESOLVED`.

### PROVIDER_VALIDATION

Provider e modelo devem ser testados antes de entrar como recomendação operacional persistente.

## 2. GOAL_HEADER_OBRIGATORIO

Todo GOAL novo deve declarar, explicitamente:

```text
SESSION_POLICY=
SESSION_REASON=

EXECUTION_CLASS=
EXECUTOR=
PROVIDER=
MODEL=
REASONING=
MODEL_REASON=

FALLBACK_PROVIDER=
FALLBACK_MODEL=
FALLBACK_REASONING=

LLM_REQUIRED=
COST_POLICY=
INDEPENDENT_AUDIT_REQUIRED=
```

Quando o provider, modelo ou fallback ainda não tiver sido validado, usar `TO_BE_RESOLVED`; não preencher por inferência.

## 3. EXECUTION_CLASSES

Os valores permitidos para `EXECUTION_CLASS` são:

- `L0_DETERMINISTIC`: operação resolvida por scripts, parsers, diff, hash ou validação mecânica; `MODEL=NONE`.
- `L1_LOW_COST`: tarefa simples com interpretação limitada; raciocínio `minimal` ou `low`.
- `L2_INTERPRETATIVE`: interpretação ou redação normativa/documental; raciocínio `low` ou `medium`.
- `L3_HIGH_REASONING`: análise complexa, ambígua ou de alto impacto; raciocínio `medium` ou `high`.
- `L4_INDEPENDENT_AUDIT`: auditoria independente; raciocínio `high` quando necessário e executor distinto do produtor.
- `L5_ORCHESTRATION`: coordenação de agentes, gates, dependências e handoffs.

A classe e o nível de raciocínio são orientação de roteamento, não obrigação cega: a escolha deve considerar a capacidade necessária e ser registrada no GOAL. A correspondência entre classe e nível de raciocínio é definida em `REASONING_ROUTING`.

## 4. SESSION_POLICY e SESSION_RECOVERY

Todo GOAL deve declarar `SESSION_POLICY` como `NEW_SESSION_RECOMMENDED` ou `CURRENT_SESSION_OK`, com a razão correspondente em `SESSION_REASON`.

`NEW_SESSION_RECOMMENDED` é preferencial para nova frente, mudança substancial de fase, auditoria independente, mudança de papel, governança transversal, outro repositório ou risco de contaminação contextual.

Antes de restart do gateway ou encerramento operacional, preservar o `SESSION_ID` quando a sessão precisar ser retomada.

## 5. Auditoria independente (PRODUCER != AUDITOR)

Quando `INDEPENDENT_AUDIT_REQUIRED=YES`, o produtor não pode executar a auditoria independente da própria entrega. A auditoria deve ser atribuída a outro agente ou sessão, com escopo e resultado rastreáveis. Para esta política, o auditor futuro indicado é `CODEX`.

## 6. WORKTREE_ISOLATION e DIRTY_WORKTREE

Quando múltiplos agentes escrevem simultaneamente no mesmo repositório, avaliar primeiro o uso de `--worktree`. Preferir worktree isolado em frentes paralelas, `DIRTY_MIXED`, branches diferentes ou qualquer risco de colisão.

Em worktree sujo, nunca executar automaticamente `stash`, `reset`, `restore`, `clean` ou checkout destrutivo. Antes de alterar arquivos, aplicar Gate Zero, custódia, `WRITE_ALLOWLIST` ou worktree isolado. Nenhuma ação deve apagar ou ocultar trabalho não inventariado. (`DIRTY_WORKTREE`).

## 7. QUOTA_AWARE_ROUTING

Antes de escolher modelo, considerar quota disponível, momento do reset, custo, contexto, capacidade necessária e disponibilidade de fallback. Quota baixa exige preservar modelos escassos para tarefas que realmente exigem seu raciocínio.

## 8. SERIALIZATION_POLICY e TRANSFORMATION_POLICY

Dados canônicos não devem ser serializados manualmente por LLM quando script determinístico puder fazê-lo. O padrão é:

```text
FONTE_CANONICA → SCRIPT → VALIDACAO → AUDITORIA
```

LLM pode decidir ou interpretar. Script deve transformar quando a transformação for mecanicamente especificável.

## 9. STOP_GATES e HUMAN_AUTHORITY

Preservar a distinção entre:

```text
FECHADO != HOMOLOGADO != COMMITTED != MERGED != PUBLICADO
```

Homologação, publicação, merge e decisões editoriais continuam sujeitas aos gates humanos já existentes. Nenhum roteamento de modelo autoriza contornar revisão, direitos, privacidade, proteção de branch ou exigência de pull request. (`HUMAN_AUTHORITY`).

## 10. REASONING_ROUTING

O nível de raciocínio segue a classe de execução:

- `L0_DETERMINISTIC`: `MODEL=NONE`.
- `L1_LOW_COST`: `reasoning=minimal` ou `low`.
- `L2_INTERPRETATIVE`: `reasoning=low` ou `medium`.
- `L3_HIGH_REASONING`: `reasoning=medium` ou `high`.
- `L4_INDEPENDENT_AUDIT`: `reasoning=high` quando necessário.
- `L5_ORCHESTRATION`: roteamento conforme a sub-tarefa.

A classificação é orientação, não obrigação cega.

## 11. Critérios mínimos de conformidade

Antes de concluir um GOAL, verificar: cabeçalho completo; provider/modelo validado ou explicitamente `TO_BE_RESOLVED`; classe e custo coerentes; uso de script-first quando aplicável; isolamento e estado do worktree avaliados; auditor independente separado quando exigido; e gates finais preservados.
