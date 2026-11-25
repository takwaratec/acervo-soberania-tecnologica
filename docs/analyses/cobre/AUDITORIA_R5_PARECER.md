---
tipo_documental: documento-institucional
estado_documental: em-revisao-documental
responsavel_curadoria: Fabio F. Resck
---
# Auditoria Teco R5 — COBRE-PLANO-AUDITORIA-20261124-R5

**Executor:** HERMES_OPENCODE (opencode) · **Auditor:** CODEX_LUNA_MEDIUM (openai, `gpt-6-luna`, reasoning `high`)
**Data:** 2026-11-24 · **Commit auditado:** `2dd82b05ba6738eef7fca8d32a6c5a9520a7eaf3`
**Objeto:** plano do COMPOSTO sulfato de cobre, v2 (segunda rodada de auditoria)

---

## Veredito

**REPLANEJAR** · `EXECUTAVEL_AGORA: false`

| Correção exigida na R4 | Situação na v2 |
|---|---|
| S7/NOAEL — 2 mg Cu/L não é fronteira universal | **CORRIGIDA** |
| Por que o cúprico no bambu | **PARCIAL** |
| "vende a rocha, compra o reagente" | **CORRIGIDA** |
| Competência tripartite | **CORRIGIDA** |
| Omissão do acervo (Gauss 2.5/2.6) | **PARCIAL** |

**Cinco de treze conferências em PASS pleno.** Quatro furos novos, todos reais.

---

## Os quatro furos da R5 — verificados antes de acatar

### F1 · Origem 2025: massa e valor confundidos — **erro meu, confirmado**

Escrevi na v2: *"China 143,0 t (48,3%)"*. Medido no ComexStat custodiado:

- China na **massa**: 143,000 t de 177,854 t = **80,4%**
- China no **valor**: US$ 178.777 de US$ 370.053 = **48,3%**

**Misturei a coluna de toneladas com o percentual de valor.** O auditor refez e achou.
Corrigido com tabela separando massa e valor — e a dispersão de preço por origem
passa a ser o achado: China **US$ 1,25/kg**, EUA **US$ 45,57/kg**, Reino Unido
**US$ 148,43/kg**. Razão de até **119×** dentro do mesmo NCM.

### F2 · Tabela 2.6: espécies atribuídas errado — **erro meu, confirmado**

Escrevi *"CCB 6%, full-cell — *B. stenostachya*, *D. asper*: 3,9–17,5"*. Na tabela
original (`extracao.md` L2566–2578), o intervalo **3,9–17,5 está na linha de
*T. siamensis***; *B. stenostachya* é 3,5–15,9 e *D. asper* é 3,4–14,4.

Corrigido: tabela reescrita **uma linha por espécie**, com a fonte numerada [1]–[5]
como no original.

### F3 · Generalização indevida sobre retenção — **confirmado**

Escrevi *"O bambu não retém o preservante como a madeira retém"*. A comparação
bambu × madeira existe **num único ensaio** — [5] Lee, Chen & Tainter 2001, *P.
edulis* contra *Pinus* sul. O resto da tabela mostra bambu retendo **0,28 a 17,5
kg/m³** conforme espécie e método: variação enorme, não uma propriedade do material.

Corrigido: conclusão **restrita àquele ensaio**; a generalização é proibida
explicitamente na §7.

### F4 · "barato" e "menor toxicidade mamífera" sem fonte — **confirmado**

A Tabela 2.5 diz do ZnCl₂/CuSO₄: *"hygroscopic, good fungicide, can retard fire as
well"*, com desvantagens *"not effective in outdoor applications, ineffective for
termites and insects"*. **Não diz barato nem menos tóxico** — eram afirmações minhas,
herdadas da v1.

Corrigido: removidas da afirmação; voltam como **pergunta** de S2 ("se o argumento de
menor toxicidade existe como argumento comercial, e com que fonte").

---

## As três omissões do acervo — nova rodada S7-ter

A R5 encontrou material custodiado que v2 não consultava. É o mais grave dos achados,
porque **a frente tem a fonte e não a usa**:

| Caminho | O que contém |
|---|---|
| `_privado/fontes-documentais/ago_28_Boratos_Cobre/md/Rusch_et_al_2023_Bambu_CCB_Lixiviacao.md` | **proporção de sulfato de cobre na formulação do CCB**, durabilidade em 5 anos, distribuição e lixiviação de Cu e Cr |
| `_privado/fichas/ago_28_CCA_CCB/rusch-2023-ccb-bambu-durabilidade-lixiviacao.md` | síntese curatorial, *D. asper*, com limites declarados |
| `_privado/fontes-documentais/ago_28_Boratos_Cobre/md/WHO_2004_Copper-in-Drinking-Water_Background.md` | **fonte primária do NOAEL de 2 mg Cu/L e do estudo dos 61 voluntários** |

**Por que importa mais do que o parecer disse:** o WHO 2004 é a origem do número que
S7 usa — citá-la fecha a corrente e NÃO deixa o NOAEL em segunda mão. E Rusch 2023
traz a proporção de sulfato de cobre no CCB, que é exatamente o que falta para
converter `kg/m³ de sal` em `kg/m³ de Cu` (a tabela 2.6 só dá massa de sal).

---

## O que a R5 acertou e eu não vou discutir

Q1 (NOAEL), Q3 ("vende a rocha" retirado), Q4 (tripartite), Q8 (proporção não
medida), Q9 (ordem), Q10 (hipóteses marcadas) — PASS. A correção estrutural de S7
foi aceita como **CORRIGIDA**, que é o ponto mais importante: o erro de transporte
entre meios saiu do plano.

---

## Ações executadas

1. Plano **v3** publicado: origem com massa e valor separados; Tabela 2.6 por espécie
   com fonte numerada; generalização restrita; afirmações sem fonte removidas; nova
   rodada **S7-ter** com as três omissões.
2. Ordem atualizada: **S1 → S2 → S7 → S7-ter → S7-bis → S4 → S5 → S6 → S3**.
3. Novo limite na §7: **não generalizar retenção de um ensaio para "o bambu"**.
4. §6.1 documenta os quatro furos da R5 com o erro nomeado de cada um.

**Commit:** `b93a70f3293df0a6a30166641c2ffc2fc45dfa33`

---

## O que este parecer NÃO verifica

- **Não reexecutei a API ComexStat.** Os valores vêm de consulta minha, guardada em
  `_privado/governanca-operacional/extracoes/cobre/` — e o próprio auditor declarou o
  mesmo limite.
- **Não auditei fonte primária externa** de toxicologia, legislação ou registro.
- **A pesquisa substantiva não começou.** Audita-se o plano.

---

**Estado:** parecer registrado; replanejamento executado; v3 aguarda terceira rodada.
Nada homologado.
