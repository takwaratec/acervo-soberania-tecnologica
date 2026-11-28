---
tipo_documental: sintese-critica
estado_documental: historico
responsavel_curadoria: Fabio F. Resck
frente: BAMBU-SCIENCE
gaveta: bambu-tratamento
origem_documental: frente absorvida COBRE (2026-11-28)
nota_de_metadado: front matter acrescentado na absorcao; o corpo nao foi reescrito
---

# Auditoria Teco R6 — COBRE-RESIDUO-AUDITORIA-20261124-R6

**Executor:** HERMES_OPENCODE (opencode) · **Auditor:** CODEX_LUNA_MEDIUM (openai, `gpt-6-luna`, `high`)
**Data:** 2026-11-24 · **Commit auditado:** `094e4945a4ea968e348ed334b53a3a7e2eb97df1`
**Objeto:** plano v4 — eixo do resíduo e do alerta (S8–S12)

---

## Veredito

**REPROVA** · `EXECUTAVEL_AGORA: false` · **`RISCO_DE_ADVOCACIA: ALTO`**

| Indicador do parecer | Resultado |
|---|---|
| `CONTA_DILUICAO_OK` | **true** — a aritmética passa |
| `VAO_NORMATIVO_PROCEDE` | **false** — a tese normativa está errada |
| `RISCO_DE_ADVOCACIA` | **ALTO** — S9, S10 e a síntese fixavam conclusão |

**A conta passou nos três primeiros testes e reprovou na conclusão que tirou dela.**

---

## O furo central — e é contra a minha própria tese, que é o pior tipo

### O "vão normativo" não existe. A PNRS inclui líquidos.

A v4 afirmou: *"a solução exaurida não é efluente nem resíduo sólido, logo há vão
normativo"*. **Falso.** Verificado na fonte:

> **Lei 12.305/2010, art. 3º, XVI** — resíduos sólidos: *"material, substância, objeto ou
> bem descartado resultante de atividades humanas em sociedade, a cuja destinação final se
> procede, se propõe proceder ou se está obrigado a proceder, nos estados sólido ou
> semissólido, bem como gases contidos em recipientes e **líquidos cujas particularidades
> tornem inviável o seu lançamento na rede pública de esgotos ou em corpos d'água, ou
> exijam para isso soluções técnica ou economicamente inviáveis em face da melhor
> tecnologia disponível**"*

**A solução exaurida de sulfato de cobre é, com alta probabilidade, resíduo sólido pela
PNRS** — não por ser sólida, mas por ser líquido cujo lançamento é inviável. O vazio que
a v4 anunciou já estava preenchido pela lei desde 2010.

**Por que este é o erro mais grave do capítulo:** o erro falseava **a favor da minha
própria tese**. Um erro que empurra a conclusão na direção que se quer é exatamente o
que a auditoria existe para pegar — e pegou.

**O que sobra como pergunta legítima**, e é melhor que o vazio inventado: a PNRS
*define*, mas **quem classifica, quem fiscaliza e qual destinação é exigida de um
gerador doméstico**? E o banho se enquadra em algum código da **Lista Brasileira de
Resíduos Sólidos (IN Ibama 13/2012)**, que tem entradas para preservação de madeira?

### A segunda correção: "impossibilidade física" era forte demais

A conta está certa — o auditor refez e confirmou 50,9 g de cobre, 5.656 m³ para 9 µg/L e
45.856 m³ para 1,11 µg/L. **Mas a conclusão "é impossibilidade física" não se segue.** A
conta prova que igualar por diluição exige volumes enormes **sob hipótese de mistura
uniforme**. Não prova que diluir seja a única via: há precipitação, adsorção, troca
iônica, confinamento.

**Formulação que fica:** *diluir não é uma estratégia de descarte* — e, no caso
doméstico, nenhuma das alternativas de tratamento está ao alcance. Isso é mais fraco e
**é verdadeiro**, o que basta.

### A terceira: decantação sozinha não resolve

A v4 listava decantação e reuso como as duas destinações defensáveis. **Decantar separa
sólidos suspensos e não remove cobre dissolvido** — o Cu²⁺ continua no líquido. A
sequência tecnicamente correta é **precipitar (alcalinizar) → decantar → destinar o
lodo**, e o lodo exige caracterização e destinação própria.

E o tratamento **não elimina o resíduo**: muda de fase e de regime jurídico. A v4
apresentou como solução o que é transferência de problema.

---

## Advocacia — o defeito que o auditor nomeou e eu aceito

| Onde | O que a v4 escreveu | Por que é advocacia |
|---|---|---|
| **S9** | *"por que o sulfato de cobre é a pior escolha"* | a pergunta contém a resposta |
| **S11** | título *"a receita sem aviso"* | anuncia a omissão antes de ler a instrução |
| **§4** | conclusões fixas ("o descarte direto é insanável por física") | a síntese afirma o que a conta não demonstra |
| **S9** | *"piora o espectro **e** piora a mobilidade"* | a Tabela 2.5 não mede mobilidade comparativa |

**Corrigido:** S9 vira comparação em **três desfechos possíveis** (pior / igual / melhor).
S11 vira **cinco perguntas fechadas** cuja resposta pode ser "sim" — inclusive a resposta
que absolve as instruções. §4 vira **resultado condicional**, cada item capaz de sair
falso.

---

## O que o auditor acertou e eu não discuto

Q1, Q2, Q3 — a conta e as razões (901× e 111×) conferem. Q11 — a cláusula anti-furo
existia, mas era inócua enquanto S9/S10/§4 fixavam conclusão; agora não é. Q6, Q7, Q8,
Q9 — PARCIAL, todos corrigidos em S10.1 e S9.

---

## Ações executadas (plano v5, commit `f64ccd75`)

1. **§1.2** — o erro normativo registrado com a citação da PNRS.
2. **S10 reescrita** como investigação aberta em **quatro perguntas** (enquadramento,
   regime, competência, destinações), com PNRS, Decreto 10.936/2022 e IN Ibama 13/2012
   como fontes obrigatórias.
3. **S10.1** — tabela das destinações com o que cada uma faz e **não faz**.
4. **S9** — de "pior escolha" para comparação em três desfechos; mobilidade declarada
   **não estabelecida**.
5. **S11** — de "receita sem aviso" para cinco perguntas fechadas.
6. **§4** — resultado condicional; **§5** ganhou quatro proibições novas.
7. **Ordem:** S12 (alternativas) sobe para antes de S9 — não se compara sem reunir as
   alternativas.

---

## O que não verifiquei

- **NBR 10004:2024** segue não consultada (paga).
- **Normas estaduais e municipais** de destinação: não levantadas.
- **IN Ibama 13/2012**: identificada como fonte necessária, **não custodiada**.
- **Licenciamento de MG** citado pelo auditor: aponta prática industrial de circuito
  fechado — evidência de prática, não regra doméstica.

**Estado:** parecer registrado; v5 aguarda quarta rodada. Nada homologado.
