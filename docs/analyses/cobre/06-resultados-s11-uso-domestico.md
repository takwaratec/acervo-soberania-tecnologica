---
schema: ACERVO_RESULTADO_RODADA_R1
gaveta: cobre
frente: COBRE
rodada: S11
titulo: "S11 — Uso doméstico e rural do sulfato de cobre: o que as instruções dizem e o que omitem"
estado_documental: em-revisao-documental
homologacao_automatica: false
versao: 2
data_revisao: 2026-11-24
auditoria: "R7 REPROVA — achou instrucao de reuso no COT110 que o executor declarou ausente. Corrigido nesta versao."
correcao_central: "o COT110 DIZ o que fazer com a solucao excedente (L207-214): armazenar em recipiente plastico e reutilizar no proximo tratamento. A v1 afirmou ausencia total — era falso.
responsavel_curadoria: Fabio Takwara
assistencia_documental: agente de IA, sujeito a revisao humana
corpus_custodiado: "_privado/fontes-documentais/ago_28_Sulfato_S11/ (5 PDFs, manifest com sha256)"
plano_executado: 03-plano-residuo-e-alerta.md v5
---

# S11 — Uso doméstico: medição das cinco perguntas

> **Resultado em uma frase (v2, corrigida).** A instrução rural brasileira **avisa e
> orienta**: dá EPI, proíbe descarte no ambiente e **manda armazenar a solução excedente em
> recipiente plástico e reutilizá-la no próximo tratamento** (L207–214). O que ela **não**
> diz é o destino da solução **quando ela não puder mais ser reutilizada** — e esse é o
> ponto em que o problema de fato começa.
>
> **Correção da v1.** A v1 desta rodada afirmou que o COT110 "não diz o que fazer com a
> solução". **Falso:** o texto custodiado diz, em duas linhas que a varredura não pegou
> porque procurou "decantação/reuso" e não "excedente". A auditoria R7 encontrou. O
> resultado está reescrito e a lacuna, corretamente estreitada.

---

## 1. O corpus custodiado

| ID | Documento | Tipo | Págs | sha256 (12) |
|---|---|---|---:|---|
| **COT110** | Embrapa — *Tratamento da madeira na propriedade rural* (Comunicado Técnico 110) | **instrução rural brasileira** | 13 | `86de88b29be0` |
| **NMBA2006** | NMBA/DST Índia — *Preservation of Bamboo*, Training Manual TM 05 | **manual oficial de governo, 60 p.** | 60 | `1015b54bd005` |
| **CONBEA97** | *Manual de irrigação com bambu* (CONBEA) | manual técnico | 22 | `c6cbdd49b1e0` |
| **UFES** | TCC — tratamento de bambu (UFES) | trabalho acadêmico | 31 | `cad731f98300` |
| **RUSCH** | Rusch et al. 2023, *Pesq. flor. bras.* | artigo científico | 8 | `c394489567bc` |

*(Rusch é o **mesmo PDF** já custodiado em `ago_28_Boratos_Cobre` — sha256 `c394489567bc801a`
confere byte a byte. Custódia duplicada por proveniência de origem, não por descuido.)*

---

## 2. As cinco perguntas, medidas

| Documento | a) EPI | b) destino da solução | c) dose por espécie | d) persistência | e) aviso solo/água |
|---|---:|---:|---:|---:|---:|
| **COT110 Embrapa** | **16** | 4 | 0 | **0** | 4 |
| **NMBA2006 Índia** | 5 | **2** | 2 | **0** | 1 |
| CONBEA97 | 3\* | 3\*\* | 0 | 0 | 0 |
| UFES | 0 | 1\*\*\* | 0 | 0 | 1 |
| RUSCH | 0 | 12\*\*\*\* | 1\*\*\*\*\* | 0 | 1\*\*\*\*\*\* |

\* os "acertos de EPI" do CONBEA97 são **falsos positivos**: "luva de borracha" ali é
conexão de tubulação, não equipamento de proteção.
\*\* idem: "lixiviação" ocorre como **propriedade química do CCB**, não como instrução de descarte.
\*\*\* ocorrência única, e é **recomendação bibliográfica de terceiro** (Barboza et al. 2008), não instrução.
\*\*\*\* todas são o objeto do artigo ("lixiviação"), não orientação de descarte.
\*\*\*\*\* "species" aparece em **referência bibliográfica**.

**Correção de método declarada:** a varredura por termo produz falsos positivos de dois
tipos — homônimo ("luva" como conexão) e objeto de pesquisa ("lixiviação" como tema). Só
as contagens do **COT110** e do **NMBA2006** sobrevivem à leitura do contexto. Todas as
demais foram qualificadas acima e **não contam**.

---

## 3. O que a instrução brasileira diz — e diz bem

**Embrapa, Comunicado Técnico 110** — *Tratamento da madeira na propriedade rural*:

> *"Equipamentos de proteção individual (EPIs) como: óculos de proteção, máscara de
> proteção, luvas de borracha, vestimenta que [proteja]"*

> *"Insumos e materiais necessários: Luva de borracha · Óculos de proteção · Máscara de
> proteção · Bota de borracha · Avental ou roupa que proteja os braços e pernas · Tonel
> plástico (recomenda-se com capacidade mínima de 200 litros) · Balança · Sacos plásticos
> ou de papel · Balde graduado de 10 litros · Ácido bórico · Dicromato de potássio/sódio ·
> Sulfato de cobre"*

> *"Não descartar no meio ambiente. Utilizar meios adequados de contenção para evitar
> contaminação ambiental."*

> *"A roupa de trabalho contaminada não pode sair do local de trabalho. Lavar antes de
> usá-la novamente."*

**Isso é instrução boa e responsável.** Ela nomeia EPI, EPI por peça, o volume do tonel
(200 L), os reagentes, e proíbe o descarte no ambiente. **A rodada não encontrou omissão
de EPI na instrução rural brasileira — encontrou o contrário.**

**E um achado normativo que a fonte traz e que muda o quadro jurídico:**

> *"O Dicromato de Potássio ou de Sódio e o Ácido Bórico estão atualmente sob o controle
> da Polícia Federal, conforme a Portaria número 240, de 12 de março de 2019, e a Lei
> número 10.357 de 27 de dezembro de 2001."*

**Dois dos três sais do CCB estão declarados como controlados pela Polícia Federal pela
fonte.** O sulfato de cobre **não figura entre os dois que a fonte nomeia** — o que é
diferente de "não é controlado": a fonte não afirma que a lista seja exaustiva, e esta
gaveta não verificou a norma na íntegra.

**A formulação correta, e é mais fraca que a da v1:** a fonte declara cromo e boro
controlados e **não menciona** o cobre. Se a lista for exaustiva, quem tenta fazer CCB "de
receita" encontra controle federal no cromo e no boro e nenhum no cobre — mas isso é
**inferência**, e vai marcada assim ao capítulo.

---

## 4. O que falta — e é exatamente o que o plano previu

**Nenhum dos cinco documentos mede Q_d (persistência).** Zero ocorrências em 134 páginas.
Nenhum diz que o cobre não se degrada.

**E o destino da solução — corrigido em v2.** A v1 afirmou que o COT110 "não menciona
reuso". **Falso.** O COT110 manda, literalmente (L207–214):

> "A solução preservativa excedente deve ser armazenada em recipiente plástico, sendo
> reutilizada no próximo tratamento."

> "Os produtos químicos utilizados no tratamento e a solução excedente devem ser mantidos
> em local livre de umidade e fechado, sem acesso a crianças e animais."

**O Brasil, portanto, TEM orientação de reuso — e é boa.** A lacuna real é mais estreita:
o documento pressupõe que sempre haverá "próximo tratamento" e **não diz o que fazer quando
o reuso já não é possível** — fim da obra, saturação do banho, queda de concentração.

**Verificação de vocabulário da ausência** (para não ser acusada de leitura parcial outra
vez — foram contadas no texto extraído do COT110): "destinação" **0** ocorrências;
"saturação"/"saturado" **0**; "fim do tratamento" **0**; "resíduo" **2**, ambas em
**primeiros socorros** ("eliminar qualquer resíduo do material" nos olhos, "evitar que
aspire resíduos" na ingestão) e nenhuma em destinação de resíduo. A ausência é do **caso
final**, não da orientação de reuso.

### 4.1 O manual indiano responde — e é o único

**NMBA 2006, *Preservation of Bamboo*, p. 46–47** — manual oficial do *National Mission on
Bamboo Applications*, Department of Science and Technology, Governo da Índia:

> *"**Preservative solutions should not be disposed of in drains, rivers/streams.** Used
> solution may be **decanted and reused**. Residues may be mixed with saw dust and buried
> in the ground."*

> *"**Sludge generated during treatment should be reclaimed for chemicals and reused** by
> adding Chromic acid and bringing the pH to 2.5."*

> *"Collect the drained solution for reuse."*

> *"Always use protection during spraying — masks, gloves, goggles, etc."*

**É a resposta completa à pergunta do soberano, e ela vem de um governo:** a solução
exaurida **se decanta e se reusa**; o que não se reusa vai para resíduo controlado; o lodo
se recupera quimicamente. **Não vai para ralo, rio ou córrego.**

**Correção da comparação (a v1 afirmou superioridade que as fontes não medem):**

A v1 escreveu que "o Brasil tem instrução de EPI melhor que a indiana". **Não há métrica
para isso.** O COT110 é mais detalhado em EPI por peça; o NMBA é mais detalhado em controle
de área (ventilação, direção do vento, proibição de comida e bebida, recipientes fora do
alcance de crianças). **Quem protege melhor o operador depende de critério que nenhuma das
duas fontes define.**

**O que as fontes permitem comparar, item por item:**

| Item | COT110 Brasil | NMBA Índia |
|---|---|---|
| EPI por peça | **sim, lista detalhada** | sim, lista |
| Volume do recipiente | **sim (200 L)** | não |
| Proibição de descarte no ambiente | **sim** | **sim, mais específica** (ralos, rios, córregos) |
| **Reuso da solução excedente** | **sim (L207–214)** | **sim** ("decanted and reused") |
| Destino quando o reuso acaba | **não** | "buried in the ground" — inadequado no Brasil |
| Fórmula de preparo | não (não localizada) | **sim** Q=(C×V)/S |
| Recomendação de pré-mistura | não | **sim** |

**A conclusão correta:** **ambas orientam reuso; nenhuma das duas resolve o descarte final
de forma aceitável no Brasil** — a brasileira por não tratar o caso, a indiana por prescrever
enterro, incompatível com a PNRS.

### 4.2 Nota de honestidade sobre o próprio manual indiano

A instrução *"buried in the ground"* para resíduos **não é boa prática ambiental** — enterrar
resíduo com cromo e cobre é destinação inadequada sob a PNRS brasileira. E o método de
recuperação do lodo (acidificar a pH 2,5 com ácido crômico) é **rota industrial**, não
caseira: ninguém faz isso num quintal.

**Portanto o manual indiano resolve metade:** ele reconhece que a solução é resíduo e
prescreve reuso — mas a destinação final que oferece não é transferível ao Brasil nem à
escala doméstica.

---

## 5. O que a S11 estabeleceu, e o que não estabeleceu

| Afirmação | Estado |
|---|---|
| A instrução rural brasileira (COT110) **dá** EPI por peça, exige tonel de 200 L e proíbe descarte no ambiente | **estabelecido** |
| A instrução rural brasileira **manda armazenar a solução excedente e reutilizá-la** (L207–214) | **estabelecido** — correção da v1 |
| A instrução rural brasileira **não diz** o destino da solução quando o reuso já não é possível | **estabelecido** |
| Nenhum dos 5 documentos mede persistência do cobre | **estabelecido** (0 acertos em 134 p.) |
| O manual indiano prescreve **decantar e reusar** e proíbe descarte em ralos/rios | **estabelecido** |
| O manual indiano prescreve **enterrar resíduos** — inadequado sob a PNRS | **fato da fonte** (a inadequação jurídica é **interpretação do executor**, não da fonte) |
| O manual indiano recomenda **CCA/CCB como pré-mistura**, não misturar sais | **estabelecido** |
| Dicromato e ácido bórico **estão declarados** sob controle da Polícia Federal pela fonte | **estabelecido** |
| O sulfato de cobre **não está** sob controle da PF | **INFERÊNCIA do executor** — a fonte nomeia os dois controlados e não afirma que a lista seja exaustiva |
| "O Brasil tem melhor EPI que a Índia" | **NÃO SUSTENTADO** — sem critério comparativo; ver tabela §4.1 |
| Existe receita caseira de CCB circulando sem aviso no Brasil | **NÃO DEMONSTRADO** — nenhum documento do corpus é receita sem aviso; **uma instrução oficial não prova nada sobre outras** |
| A receita caseira omite EPI | **não demonstrado** — o COT110 **não é** receita caseira, é instrução oficial; a v1 tratou um pelo outro |

**Duas afirmações do plano caem — e a v1 errou ao dizer que caíam "por refutação":**

1. **"Receita sem aviso"** — **NÃO DEMONSTRADO neste corpus**, não "refutado". O COT110 é
   **instrução oficial da Embrapa**, não receita caseira: uma não prova nada sobre a outra.
   A v1 tratou as duas como o mesmo objeto. O que se pode dizer: *nenhum documento deste
   corpus é uma receita caseira sem aviso*, e isso **não** autoriza afirmar nem negar que
   elas existam.
2. **"Sem EPI"** — **não demonstrado** para receita caseira, pela mesma razão. Que a
   Embrapa dê EPI **não diz** o que a receita que circula em grupo de WhatsApp diz.

**Uma afirmação do plano CAI de verdade, e é contra a tese:**

3. **"A instrução não diz o que fazer com a solução"** — **falso.** O COT110 manda guardar
   e reutilizar (L207–214). A v1 afirmou ausência total e errou.

**O que sobra, e é mais estreito e mais forte:** as duas instruções — brasileira e indiana —
**mandam reusar**. Nenhuma das duas diz o que fazer quando **o reuso acaba**: a brasileira
silencia, a indiana manda enterrar (incompatível com a PNRS). **A lacuna não é "não há
instrução"; é "as instruções param exatamente onde o resíduo final começa".**

---

## 6. A pergunta que a S11 deixa para o capítulo

> Se a instrução oficial manda preparar 200 litros de solução com sulfato de cobre, cromo e
> boro, proíbe descartar no ambiente e **não diz o que fazer com ela** — o que o usuário
> rural faz na prática?

**Essa pergunta é empírica e não está respondida por nenhuma fonte desta gaveta.** Ela
exige: (a) entrevista/observação de campo, ou (b) documento de extensão que descreva a
prática, ou (c) registro de fiscalização. **Nenhum dos três está neste corpus.**

**Portanto o capítulo não pode afirmar o que o usuário faz. Pode afirmar o que a instrução
manda e o que ela deixa em aberto — e isso é medido.**

---

**Controle de fronteiras.** Medido (§2–4) separado do que caiu (§5) e do que permanece como
pergunta (§6). Falsos positivos da varredura estão qualificados e não contam. Estado:
**em-revisao-documental**; não homologado.
