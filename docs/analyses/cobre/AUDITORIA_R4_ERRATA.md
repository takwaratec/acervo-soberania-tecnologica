---
schema: ACERVO_ERRATA_R1
titulo: "ERRATA — retificação do §0 de AUDITORIA_R4_PARECER.md (achado de governança falso)"
estado: em-revisao-documental
autor: HERMES_OPENCODE
data: 2026-11-24
retifica: "docs/analyses/cobre/AUDITORIA_R4_PARECER.md §0 (sha256 7d04d0dac9abf9faefdca21cafaaad60ae153c6428f8e6f56780e456890d8df2)"
origem_da_correcao: "medição do soberano + verificação do executor contra o runner"
---

# ERRATA — o achado de governança do §0 estava errado

O §0 de `AUDITORIA_R4_PARECER.md` afirma que a regra de família é **insatisfazível na
casa** e que existe **autoauditoria estrutural obrigatória**. **As duas afirmações são
falsas.** A seção não é apagada — é retificada aqui, e os bytes originais permanecem
como evidência do erro.

## 1. O fato, medido

| Contrato | executor | auditor | par válido |
|---|---|---|---|
| R2 | HERMES_OPENCODE (opencode) | CODEX_LUNA_MEDIUM (openai) | **sim** |
| R3 | HERMES_OPENCODE (opencode) | CODEX_LUNA_MEDIUM (openai) | **sim** |
| R4 | CODEX_LUNA_MEDIUM (openai) | HERMES_OPENCODE (opencode) | sim (inversão desnecessária) |

Os três passam em `validate_contract`. O par `opencode × openai` **sempre foi legal** e
foi aceito no R2. **Não falta família distinta na casa.**

## 2. A causa real da recusa — e é minha

O contrato R3 estava correto. A recusa veio do **claim**:

```
claim COBRE-PLANO-AUDITORIA-20261124-R3 --owner CODEX_LUNA_MEDIUM
```

O runner compara, em L579–590, `efetivo = on_behalf_of or owner` contra o **auditor**.
Passando `--owner CODEX_LUNA_MEDIUM`, o reivindicante virou `openai` e colidiu com o
auditor `openai`. Com `--owner HERMES_OPENCODE` o claim teria sido aceito.

**Portanto: não havia impedimento de governança. Havia um flag errado.**

## 3. Por que o erro escalou — e onde o defeito não é meu

A mensagem do runner diz `auditor da mesma família do **executor**`, mas compara o
**reivindicante**. Lendo "executor" e vendo o contrato declarar `opencode × openai`,
a conclusão de que a regra era impossível era a leitura natural do texto.

O erro de mensagem escalou para documento de governança. Registrado como defeito de
motor em `ops/command-center/transicao-r4/ACHADO_DE_MOTOR_EVIDENCIA_E_FAMILIA_R4.md`
(achados D3 e D4), com texto de correção proposto.

**O que continua sendo erro meu, sem atenuante:** eu tinha o contrato na mão, vi que
declarava `opencode × openai`, e **não reconciliei a contradição** entre o que o
contrato dizia e o que a mensagem afirmava. Concluí sobre a casa em vez de conferir o
próprio comando. Um comando de verificação teria custado segundos.

## 4. O que permanece válido no parecer

**Todo o resto do parecer está de pé.** O veredito `REPLANEJAR`, as 6 conferências em
FAIL, os quatro furos verificados (S7/NOAEL hepático, ausência da pergunta do bambu,
"NCM 2603 ≠ cobre contido", competência tripartite) e a omissão do acervo (Gauss 2020,
Tabelas 2.5 e 2.6) **não dependem do §0** e não são afetados por esta errata.

## 5. Ações executadas após a correção

1. R4 **cancelada** com motivo: "papéis invertidos por leitura errada da regra de
   família; o par opencode×openai é válido e foi aceito no R2".
2. `agentes.json` **não alterado** — está correto.
3. Replanejamento de S1–S7 com as quatro correções, preservando a versão atual.
4. R5 submetida com `executor=HERMES_OPENCODE`, `auditor=CODEX_LUNA_MEDIUM`.

---

**Estado:** errata registrada; §0 do parecer dado por retificado; nada homologado.
