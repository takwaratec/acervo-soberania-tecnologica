---
schema: ACERVO_RESULTADO_RODADA_R1
gaveta: cobre
frente: COBRE
rodada: S11
titulo: "S11 — Uso doméstico e rural do sulfato de cobre: o que as instruções dizem e o que omitem"
estado_documental: em-revisao-documental
homologacao_automatica: false
versao: 1
data_revisao: 2026-11-24
responsavel_curadoria: Fabio Takwara
assistencia_documental: agente de IA, sujeito a revisao humana
corpus_custodiado: "_privado/fontes-documentais/ago_28_Sulfato_S11/ (5 PDFs, manifest com sha256)"
plano_executado: 03-plano-residuo-e-alerta.md v5
---

# S11 — Uso doméstico: medição das cinco perguntas

> **Resultado em uma frase.** A instrução rural brasileira **avisa** — dá EPI completo, diz
> "não descartar no meio ambiente" e lista os materiais de contenção. **O que ela não diz
> é o que fazer com a solução depois.** E o único documento do corpus que dá a resposta
> completa — "decante e reuse", "não descarte em ralos, rios ou córregos" — é um manual
> **indiano**, não brasileiro.

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

**Dois dos três sais do CCB são controlados pela Polícia Federal.** O sulfato de cobre
**não** está nessa lista. Isso é relevante: quem quer fazer CCB "de receita" no Brasil
esbarra em controle federal para o cromo e o boro — e **não** esbarra no cobre.

---

## 4. O que falta — e é exatamente o que o plano previu

**Nenhum dos cinco documentos mede Q_d (persistência).** Zero ocorrências em 134 páginas.
Nenhum diz que o cobre não se degrada.

**E o destino da solução:** o COT110 diz **o que não fazer** ("não descartar no meio
ambiente", "meios adequados de contenção") mas **não diz o que fazer**. Não menciona
decantação, não menciona reuso, não menciona tratamento.

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

**O contraste que o capítulo tem de carregar:** o Brasil tem instrução de EPI melhor que a
indiana, e **não tem** a instrução de destino da solução que a indiana tem. O país que
produz o manual mais completo sobre preservação de bambu **não é** o que tem a norma de
descarte para ele.

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
| A instrução rural brasileira (Embrapa COT110) **dá** EPI completo e proíbe descarte no ambiente | **estabelecido** |
| Essa instrução **não diz** o que fazer com a solução exaurida | **estabelecido** |
| Nenhum dos 5 documentos mede persistência do cobre | **estabelecido** (0 acertos em 134 p.) |
| O manual oficial indiano prescreve **decantar e reusar** e proíbe descarte em ralos/rios | **estabelecido** |
| Dicromato e ácido bórico estão sob controle da Polícia Federal; o sulfato de cobre não | **estabelecido** (citado pela fonte) |
| Existe receita caseira de CCB circulando sem aviso no Brasil | **NÃO ESTABELECIDO** — nenhum documento deste corpus é uma "receita de bolo" sem aviso |
| A receita caseira omite EPI | **REFUTADO para o corpus custodiado** — o COT110 dá EPI em detalhe |

**Duas afirmações do plano caem, e caem contra a tese do capítulo:**

1. **"Receita sem aviso"** — não é o que o corpus mostra. A instrução rural brasileira
   avisa. Se existe receita irresponsável circulando, ela **não está** neste corpus e a
   gaveta não pode afirmar que existe.
2. **"Sem EPI"** — refutado. O COT110 lista EPI por peça, com o volume do tonel e a
   proibição de descarte.

**O que sobra, e é mais forte que o que caiu:** a instrução avisa sobre EPI e sobre **não
descartar**, mas **não resolve** o problema que ela mesma cria ao mandar usar 200 litros de
solução. "Não descarte no meio ambiente" sem dizer **onde descartar** transfere ao usuário um
problema que ele não tem meio de resolver.

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
