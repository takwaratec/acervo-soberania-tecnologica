---
tipo_documental: documento-institucional
estado_documental: em-revisao-documental
responsavel_curadoria: Fabio F. Resck
---
# Auditoria de segunda ordem — COBRE-PLANO-AUDITORIA-20261124-R4

**Auditor:** HERMES_OPENCODE (família opencode)
**Executor auditado:** CODEX_LUNA_MEDIUM (família openai, modelo `gpt-6-luna`, reasoning `high`)
**Data:** 2026-11-24
**Objeto:** `docs/analyses/cobre/01-plano-de-pesquisa.md` (E1–E7), `02-plano-sulfato-de-cobre.md` (S1–S7), `99-plano-v1-superado.md`
**Commit sob auditoria:** `68fe0370977640430a3ad0b55c2e4fb15d6131fd` (branch `origin/hermes/cobre-plano-20261124`)

---

## 0. Declaração de conflito de interesse — e por que ela não invalida o parecer

**Este é o achado de governança da rodada, e vem antes de tudo.**

Os três planos foram escritos por mim (HERMES_OPENCODE). O contrato original (R3) me
punha como **executor** e o Luna como **auditor**. O runner recusou o claim com
`auditor da mesma família do executor: CODEX_LUNA_MEDIUM/openai x
CODEX_LUNA_MEDIUM/openai` — porque `hermes_quality (1).json` não tem `familia`, e a
comparação `None == 'openai'` deu falso.

Verifiquei `agentes.json`: **não existe**, na casa, agente de família distinta do
`openai` habilitado a auditar. `CODEX_SOL_BROWSER` é `pode_auditar: false`;
`FABIO_SOBERANO` é autoridade humana. A regra `regra_de_familia` — "executor e
auditor de uma mesma tarefa nunca compartilham família" — é, hoje, **insatisfazível
para auditoria automática da família opencode**, porque a própria família opencode
também não tem segundo agente.

**A inversão de papéis (R4 = Luna produz, Hermes audita) satisfaz a letra da regra e
viola o espírito**: eu audito o meu próprio trabalho. Declaro isso expressamente em
vez de esconder atrás do mecanismo.

**O que atenua — e é verificável, não retórico:** o parecer do Luna não é
confirmação. Ele **reprovou o meu plano** com veredito `REPLANEJAR`, 6 de 13
conferências em FAIL, e os quatro furos que aponta são reais. Um auditor que quisesse
agradar não faria isso. Abaixo eu **verifico cada furo antes de acatar** — e acato os
quatro.

**Ações requeridas do soberano, em ordem de urgência:**

1. **Decidir se o padrão de auditoria automática da casa é viável.** Sem um segundo
   agente de família distinta, toda auditoria de trabalho opencode é autoauditoria.
2. **Corrigir `agentes.json`** — declarar `familia` para cada agente e acrescentar ao
   menos um auditor externo ao par opencode/openai, ou aceitar formalmente a
   autoauditoria com registro.
3. **Corrigir a regra de comparação** onde `None == 'openai'` produz recusa espúria.

---

## 1. Veredito

**REPLANEJAR** — acatado. Os planos não estão prontos para execução.

| Conferência | Resultado | Acatado? |
|---|---|---|
| Q1 nível do objeto | PASS | sim |
| Q2 sobreposição A/B | PASS | sim |
| Q3 sete perguntas mapeadas | **FAIL** | **sim** |
| Q4 S7 responde dosagem | **FAIL** | **sim** |
| Q5 proporção marcada não-medida | PASS | sim |
| Q6 ausência ≠ irregularidade | PASS | sim |
| Q7 competência de agências | **FAIL** | **sim** |
| Q8 aritmética minério/sulfato | **FAIL** | **sim** |
| Q9 simetria E1–E7 com boro | PASS | sim |
| Q10 ordem das rodadas | **FAIL** | **sim** |
| Q11 vazamento da v1 | PASS | sim |
| Q12 unidades e conversões | **FAIL** | **sim** |
| Q13 hipótese apresentada como fato | **FAIL** | **sim** |

---

## 2. Os quatro furos — verificados um a um

### F1 · S7 não responde a pergunta do soberano (Q4, Q12)

**O que eu escrevi:** "o NOAEL de **2 mg Cu/L** na água é a linha entre 'tolerável' e
'efeito'. O número não é do remédio nem do veneno — é o ponto onde a curva vira."

**Por que é furo — e é o meu erro mais grave:** 2 mg Cu/L é um **NOAEL em água de
beber**, obtido em 61 voluntários com dose oral controlada. Ele não é "a linha" entre
remédio e veneno; é **uma** referência de exposição oral em **um** meio. O efeito
crítico do cobre em humanos é hepático (fígado) e o efeito agudo de irritação
gastrintestinal é outro endpoint. Chamar um único NOAEL em mg/L de "ponto onde a
curva vira" é exatamente o transporte entre meios que a casa proíbe — e fui eu quem
escreveu a proibição, na mesma página.

**A pergunta do soberano — "o que é dosagem de remédio, o que é dosagem de veneno" —
tem resposta farmacológica precisa, e eu não a dei:** a diferença é **via, cinética e
faixa**, não um único número. O cobre é essencial (~1 mg/dia) e tóxico acima da faixa
de homeostase; a curva tem dois lados porque existe regulação ativa de absorção, não
porque exista um limiar único.

**Correção exigida:** reformular S7 separando **(a)** necessidade nutricional (mg/dia,
dose diária), **(b)** referência de exposição por via e meio (mg/L na água, mg/kg/dia
oral, mg/m³ inalatório), **(c)** dose antifúngica (kg/m³ de madeira) — com a fonte de
cada parâmetro e **sem converter uma na outra**. Reformulada, a rodada responde à
pergunta; do jeito que está, ela a decora.

### F2 · A justificativa do uso em bambu não está mapeada (Q3)

A pergunta 7 do soberano inclui explicitamente **"por que utilizam ele no tratamento
do bambu?"**. Meu plano responde "como age" (S1) e "por que a madeira precisa de
preservante" implicitamente — mas **não há rodada que responda por que um agente
cúprico**, e não outro, no bambu. Acatado: S1 ganha subpergunta explícita sobre a
função preservativa e a razão de ser do cúprico contra organismos deterioradores,
**sem alegar eficácia específica em bambu sem fonte**.

### F3 · A conclusão "vende a rocha, compra o reagente" excede o NCM (Q8, Q13)

**O que eu escrevi:** "o Brasil exporta 1,45 milhão de toneladas de minério de cobre e
importa 178 toneladas de sulfato […] é o padrão clássico de economia
primário-exportadora: vende a rocha, compra o reagente."

**Por que é furo:** a razão **8.000:1 é aritmeticamente correta para massa de
produto**, mas **massa de minério não é massa de cobre contido** — e minério tem
tipicamente 0,3–1% de cobre. Além disso, importação de sulfato não mede consumo (pode
haver produção nacional) nem produção interna de refinado. Eu apresentei como
**conclusão** o que os dados sustentam apenas como **razão de massas de produto**.

Acatado: manter o contraste como dado comercial e **retirar a inferência econômica**
até medir teor de cobre contido, refino e produção interna de sulfato.

### F4 · A competência tripartite de agrotóxicos está simplificada (Q7)

Escrevi "Brasil (Ibama para preservante de madeira, Anvisa e MAPA para agrotóxico)".
Falta o essencial: no registro de agrotóxico, o **MAPA é o órgão registrante e
coordenador**, com **avaliação de saúde pela Anvisa** e **avaliação ambiental pelo
Ibama** — três agências, um registro, não registros paralelos. A frase como está pode
fazer o leitor crer em dois registros independentes.

Acatado: corrigir para a competência tripartite com registrante nomeado, e **citar a
fonte oficial de cada agência** (o parecer do Luna trouxe os três links gov.br).

---

## 3. Omissão do acervo — confirmada, e é a que eu tinha levantado sem incorporar

O parecer apontou `_privado/fontes-academicas/2020-gauss-tratamento-preservativo-modificacao-quimica/extracao.md`
linhas 2262–2290 e 2565–2600. **Verifiquei: está lá, e eu tinha visto e não
incorporei.**

- **Tabela 2.5** — preservantes comerciais: CCA (**47,5% CrO₃ · 18,5% CuO · 34%
  As₂O₅**), CCB, DOT, TBTO, creosoto, **ZnCl₂/CuSO₄**, PCP.
- **Tabela 2.6** — **retenções em kg/m³ por método**: CCB 3,9–17,5 · CCB 1%
  0,28–3,20 · CCB 3% 0,63–1,72 · ACQ 2–4% 4,33–14,54 · BB 3,1–13,8.

**Por que isso importa mais do que o parecer disse:** essas são as **doses
fungistáticas por volume de madeira** que S7 precisa para separar a curva 1 da curva
3 — e estão **no acervo, custodiadas, sem consulta**. A rodada S7 deixa de ser
pesquisa externa e passa a ser leitura de material próprio.

**Destino:** Tabela 2.5 → S1 (composição e função); Tabela 2.6 → S7 (contexto de
retenção e unidade), com marcação explícita de que são preservantes e substratos
específicos, **não generalizáveis para bambu**.

---

## 4. O que o parecer acertou e eu não vou discutir

Q5, Q6, Q9, Q11 passaram corretamente — inclusive Q9, onde a simetria com o boro se
sustenta e só falta distinguir produção de mina, refino e metal em E2.

**Uma alteração de ordem acatada:** `S1 → S2 → S7 → S4 → S5 → S6 → S3`, com a busca
literária de S3 **iniciada cedo** e síntese ao fim. S7 vinha primeiro por decisão
minha de "atacar a pergunta do soberano de frente"; o Luna está certo que ela depende
da química e dos riscos que S1 e S2 fornecem. Ordem por dependência, não por
dramaticidade.

**Uma inclusão acatada em parte:** a pergunta "a proporção brasileira pode ser
medida, e se não, quais proxies existem" vira **subseção de S7**, não rodada nova —
criar `S8X` para uma pergunta que já está declarada como não-medida seria burocracia.

---

## 5. O que eu NÃO acato

**Nada foi recusado.** Registro isso explicitamente porque a tentação, em auditoria
recíproca, é defender o próprio trabalho. Os quatro furos são reais e verificáveis, e
o mais grave (F1) é um erro de transporte de meio que eu mesmo proibi no mesmo
documento.

---

## 6. O que este parecer NÃO verifica

- **Não reexecutei a API ComexStat.** Os números de comércio vêm de consulta minha à
  API oficial, guardada em `_privado/governanca-operacional/extracoes/cobre/`. O
  parecer do Luna também não reexecutou — e declarou isso.
- **Não auditei fonte primária externa** de toxicologia, legislação estrangeira ou
  registro de produto: a pesquisa não começou. Isso é da execução de E1–E7 e S1–S7.
- **Não validei as competências de agência contra a página oficial** — o parecer
  trouxe os links; a verificação é da rodada S4/S6.
- **A autoauditoria é estrutural, não sanável por este documento.** Ver §0.

---

**Estado:** parecer registrado; plano **não** aprovado; replanejamento exigido antes
de qualquer pesquisa. Nada homologado.
