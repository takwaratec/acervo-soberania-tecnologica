---
tipo_documental: instrumento-de-pesquisa
titulo: "Régua de julgamento — os cinco critérios que as rodadas R6–R10 produziram"
versao: 1
data: 2026-11-25
responsavel_curadoria: Fabio Takwara
assistencia_documental: agente de IA, sujeito a revisao humana
estado_documental: em-revisao-documental
homologacao_automatica: false
gaveta: boro
frente: BORO
---

# Régua de julgamento

Esta régua não veio de um protocolo: **veio do erro**. Cada critério é o resíduo de uma
rodada de auditoria adversarial em que o texto foi reprovado. Ela existe para ser aplicada
**nesta ordem** — porque os critérios de baixo só fazem sentido depois que os de cima
passaram.

Aplicar fora de ordem é o erro mais comum: corrigir a unidade de um número cujo sujeito está
trocado produz um número mais bem formatado e igualmente falso.

---

## 1. O sujeito é o que a fonte diz, não o que o parágrafo precisa

**Pergunta:** o número está na fonte medindo **aquilo** que a frase diz que ele mede?

**Por que primeiro:** é a falha que o gate nunca pega. O instrumento confirma que o número
existe na página, com a unidade certa. Ele não lê o sujeito. Um texto pode ser 100% aprovado
no gate e 100% errado no sentido.

**Casos que este critério pegou:**

- O `90%` do USGS: na mesma página, `90%` é a fatia turca das **importações** e `90%` é a
  fatia dos **quatro minerais** no uso industrial. Duas afirmações diferentes, mesmo número,
  mesma página.
- O `40%` da OMS: na **p.13**, `40%` é redução de peso de testículo; o `40%` que interessa é
  a alocação à água de consumo, na **p.22**.
- O `60` da OMS: dose na ração na p.13; fator de incerteza total na p.22.
- O `2,4` da diretriz: casou com o item "2.4" do **sumário**.

**Regra operacional:** quando um valor aparece mais de uma vez na fonte, **a página escolhida
é a que traz os números companheiros da mesma frase** — não a primeira ocorrência.

---

## 2. Dose não se soma

**Pergunta:** a frase juntou duas condições experimentais diferentes numa conclusão única?

**Por que segundo:** apagar a dose é a forma mais silenciosa de transformar um resultado
verdadeiro numa afirmação falsa. Nenhum número fica errado; o que desaparece é o que dava
sentido a eles.

**Casos que este critério pegou:**

- Rusch 2023: CCB a **1% → índice de deterioração 40** (ataque leve) e a **3% → índice 0**.
  A frase original dizia "o bambu tratado não apresentou degradação" — verdadeira a 3%,
  falsa a 1%. Somar as duas apagou exatamente o dado que informa a dose.
- O mesmo artigo, no cobre e cromo: os autores descrevem **comportamento aleatório**, e a
  ficha dizia "a parte inferior tem maior teor" — o que só vale numa das concentrações.
- Araujo 2025: as sete categorias de impacto **não se somam**; 93% é do total normalizado
  entre elas, não do HCT.

---

## 3. Inferência não se escreve como leitura

**Pergunta:** esta frase descreve a fonte, ou descreve o que eu concluí a partir dela?

**Por que terceiro:** é a fronteira entre curadoria e autoria. Uma inferência declarada é
trabalho intelectual; uma inferência vestida de citação é falsificação — mesmo quando está
certa.

**Casos que este critério pegou:**

- "o efluente não entra naquela atribuição": a fonte diz "aparas e cortes, colmos descartados
  e água residuária". **Não discrimina** quanto pesa cada um. Eu escrevi como se ela
  excluísse o efluente.
- A versão corrigida errou de novo, no outro sentido: passou a dizer que a fonte "não
  decompõe" — e a **Tabela 2 decompõe**, com o efluente em 1,5% do HCT. Duas inferências
  erradas, opostas, sobre a mesma tabela.
- "quem bebe cisterna está exatamente na rota": a cisterna capta **chuva**, não lençol.

**Regra operacional:** quando a fonte não discrimina, a frase diz **que ela não discrimina**.
Quando discrimina, a frase traz o número — não a impressão.

---

## 4. Indicador não é probabilidade

**Pergunta:** o número é um **resultado medido** ou um **índice normalizado** entre
categorias?

**Por que quarto:** os dois usam a mesma notação de percentual, e a diferença muda o que o
leitor pode concluir. Percentual de impacto normalizado **não é** percentual de risco.

**Casos que este critério pegou:**

- "93%": é a participação do HCT no total normalizado das sete categorias de uma ACV. **Não**
  é "93% de probabilidade de câncer", e a diferença não é de ênfase — é de natureza.
- "superior a 80%" de inibição fúngica: só **uma** das duas espécies passa de 80%.
- "maior parte do mundo abaixo de 0,5 mg/L": atribuído ao documento de 2009, quando o dado
  é do de 2022.

---

## 5. A página é parte da afirmação

**Pergunta:** a afirmação traz página, e a página traz o número **com aquele sujeito**?

**Por que último:** sem os quatro critérios anteriores, exigir página só produz precisão
aparente — um número localizado com todo o cuidado no lugar errado. A página fecha o
trabalho; não o substitui.

**Casos que este critério pegou:**

- Rusch 40 e 0 estão na **Tabela 1, p.5** (escala de classificação), não na p.2 (métodos),
  onde o `40` que aparece é a coordenada `53°23'40"`.
- Kaminski: "2 a 6 anos" e "menos de 1 ano" estão na **tabela da p.7**; a p.13 é a lista de
  referências.
- O `21,8 µg/L` de Kırka citado como [24] — artigo de bambu. O dado é de **Türker 2016**.
  Citação errada encontrada só porque o gate exigiu localizar o número na fonte citada.

---

## Como aplicar, em uma frase por passo

1. **Quem é o sujeito?** — se a fonte tem o mesmo número para dois sujeitos, a página decide.
2. **A dose sobreviveu?** — se a frase soma condições, separe e refaça.
3. **É leitura ou inferência?** — se é inferência, escreva que é, ou tire.
4. **É medida ou índice?** — se é índice, diga de quê.
5. **A página fecha?** — número, sujeito e unidade na mesma página, senão não fecha.

## O que esta régua não faz

Não substitui o gate, e o gate não a substitui. **O gate mede presença; a régua julga
sentido.** Nesta peça, o gate conferiu **58 de 327** afirmações numéricas e a régua foi
aplicada à mão sobre essas 58 — inclusive para descobrir que o instrumento não lê `mg/L`,
`mg/m³` nem `mg B/kg/dia`, que são as unidades do assunto.
