---
schema: ACERVO_PLANO_ESPECIFICO_R2
gaveta: cobre
frente: COBRE
titulo: "Plano específico — SULFATO DE COBRE: identidade, mecanismo, riscos, normas, fiscalização e as três curvas da dosagem"
estado_documental: em-revisao-documental
homologacao_automatica: false
versao: 3
substitui_versao: "1 (preservada byte a byte em 99-plano-sulfato-v1-superado.md)"
data_revisao: 2026-11-24
responsavel_curadoria: Fabio Takwara
assistencia_documental: agente de IA, sujeito a revisao humana
complementa: 01-plano-de-pesquisa.md (plano do ELEMENTO, sete rodadas E1-E7)
auditoria_anterior: "R4 = REPLANEJAR (4 furos + 1 omissao) e R5 = REPLANEJAR (4 furos + 3 omissoes); ambos acatados. v2 nao preservada em arquivo: os furos que ela tinha estao listados na §6."
tipo_documental: instrumento-de-pesquisa
---
# Plano específico — sulfato de cobre (v2, pós-auditoria)

> **Pergunta de pesquisa.** O que é o sulfato de cobre, de onde vem, como age sobre o
> organismo que combate, que risco cria para quem aplica e para a água, o que a norma
> permite e proíbe, quem fiscaliza no Brasil — e por que a mesma substância é remédio
> numa dose e veneno em outra?
>
> **Nível do objeto.** Este documento cataloga o **COMPOSTO**. O **ELEMENTO** cobre
> está em `01-plano-de-pesquisa.md`. O **produto tratado** (madeira ou bambu com
> preservante) é das fichas de produto, etapa posterior — aqui aparece apenas como
> contexto de aplicação, nunca como objeto de medição.
>
> **O que mudou da v1 e por quê.** A v1 foi reprovada com veredito `REPLANEJAR`.
> Quatro furos, todos acatados; o primeiro é grave e está na §1. A v1 fica preservada
> byte a byte em `99-plano-sulfato-v1-superado.md`.

---

## 1. O erro da v1 que esta versão corrige — e é o mais grave

A v1 escreveu: *"o NOAEL de 2 mg Cu/L na água é a linha entre 'tolerável' e 'efeito'.
O número não é do remédio nem do veneno — é o ponto onde a curva vira."*

**Está errado, e é transporte entre meios — o erro que a mesma página proibia.**
2 mg Cu/L é um **NOAEL de exposição oral em água de beber**, de estudo controlado com
61 voluntários. É **uma** referência de **um** meio para **um** endpoint (irritação
gastrintestinal aguda). Não é fronteira universal entre remédio e veneno, e o **efeito
crítico crônico do cobre é hepático** — fígado, não estômago.

**A resposta à pergunta do soberano não é um número: é a separação de três curvas que
nunca se comparam diretamente** (§3, S7). E a razão de o cobre ter dois lados não é
"existe um limiar": é que **a absorção é ativamente regulada** — homeostase. Remédio
e veneno, no cobre, são o mesmo íon em estados diferentes de um sistema que tenta se
manter no meio.

---

## 2. Identidade do composto — com a verificação cruzada nova

**CuSO₄·5H₂O** — sulfato cúprico penta-hidratado. **Teor de cobre 25,45%** em massa
(63,546 g/mol de Cu em 249,682 g/mol do sal); anidro, **39,81%**. Fator sal→cobre =
**3,93**. Toda cifra deste capítulo declara se está em **sal** ou em **cobre contido**.

**NCM:** `2833.25` → **28332510** (sulfato cuproso) e **28332520** (sulfato cúprico).

### 2.1 A composição do CCA confere entre duas fontes custodiadas independentes

Verificação que a v1 não tinha, e vale mais que a citação isolada:

| Fonte custodiada | CrO₃ | CuO | As₂O₅ |
|---|---|---|---|
| **Ibama 2024** — Tanalith 60% CCA-C (absolutos; 60,41% de parte ativa) | 28,70 | 11,17 | 20,54 |
| mesmos valores **normalizados à parte ativa (=100%)** | **47,51** | **18,49** | **34,00** |
| **Gauss 2020**, Tabela 2.5 (declara a composição percentual) | **47,5** | **18,5** | **34** |
| **divergência** | 0,01 pp | 0,01 pp | 0,00 pp |

Duas fontes de casas diferentes — rótulo regulatório brasileiro e tese acadêmica —
convergem a **um centésimo de ponto percentual**. Isso valida de uma vez a leitura do
rótulo do Ibama e a Tabela 2.5, e faz do CCA-C ponto de ancoragem confiável para o
resto do capítulo. **Não é homologação** — é consistência entre duas fontes
custodiadas, declarada como tal.

---

## 3. As sete rodadas — versão corrigida

### S1 · O que é, de onde vem, como age — e **por que o cúprico**

**Pergunta:** qual é a química do sulfato de cobre e qual é o **fundamento da escolha
de um agente cúprico** como preservante?

**Ataca:** a v1 respondia "como age" e deixava sem resposta a pergunta literal do
soberano — *por que utilizam ele no tratamento do bambu?* Rodada que descreve
mecanismo e não justifica a escolha decora a resposta.

**O que a gaveta já tem custodiado** (`_privado/fontes-academicas/2020-gauss-tratamento-preservativo-modificacao-quimica/extracao.md`,
Tabela 2.5, L2262–2290):

- **CCA** (47,5% CrO₃ · 18,5% CuO · 34% As₂O₅) — *"fixable, broad spectrum biocide"*;
  desvantagem declarada: *"contains harmful chromium and arsenic"*.
- **ZnCl₂ / CuSO₄** — *"hygroscopic, good fungicide, can retard fire as well"*;
  desvantagens: *"not effective in outdoor applications, ineffective for termites and
  insects"*.
- **DOT** (bórax/ácido bórico) — *"self-diffusing, effective against fungi, insects
  and termites"*; desvantagem: *"highly leachable, not suitable for outdoor
  application"*.

**Isso é o que a fonte custodiada sustenta, e nada além:** o cúprico é fungicida
solúvel em água, com boa ação contra fungos, **ineficaz contra térmitas e insetos** e
**ineficaz em aplicação exterior** — e é justamente a solubilidade que o torna
lixiviável. A Tabela 2.5 registra, na mesma linha, a qualidade e o defeito.

**O que a Tabela 2.5 NÃO diz, e a v2 não pode afirmar sem outra fonte:** que o cúprico
seja *barato* ou de *menor toxicidade mamífera*. A v1 afirmava as duas coisas; a tabela
não as contém. Se o argumento de menor toxicidade for importante para o capítulo (e é,
porque é o argumento comercial), ele precisa de fonte própria — vai para S2.

**Fontes:** literatura de proteção de madeira (AWPA, IRG) e de fungicidas cúpricos;
especiação do Cu²⁺ (o cobre só é tóxico como íon disponível).

**Mede:** mecanismo (desnaturação de proteínas e enzimas pelo Cu²⁺ livre, dano de
membrana); a diferença **fungistático × fungicida**; e a razão de ser do cúprico
frente a arsênico e crômio — **se** o argumento de menor toxicidade mamífera existe
como argumento comercial, e com que fonte; e por que, ainda assim, ele é lixiviável.

**Critério de fracasso:** se a rodada não separar "mata o fungo" de "impede o fungo de
crescer", falhou.

**O que a rodada não entrega:** eficácia em bambu. A Tabela 2.5 é de preservantes
comerciais em geral; nenhuma fonte da gaveta mede eficácia do cúprico puro em bambu.

### S2 · Riscos — humano, ambiental, ocupacional

**Já ancorado:** LD₅₀ oral rato 790/450 mg/kg; irritação ocular até 21 dias; NOAEL
oral em água 2 mg Cu/L, LOAEL 4 (náusea), vômito ≥6; invertebrado aquático agudo 2,05
e crônico 1,11 µg/L; CONAMA 357 9 µg/L; efluente CONAMA 430 1,0 mg/L; potabilidade
2 mg/L; NIOSH 1 mg Cu/m³; **NR-15 sem limite de tolerância para cobre**.

**Falta:** cadeia toxicológica completa (E3) e dependência de matriz da ecotoxicidade
(E4) — sem elas o risco fica em números soltos. **Efeito crítico crônico: hepático.**

### S3 · Literatura — **iniciada cedo, sintetizada ao fim**

**Pergunta:** o que a literatura consolidada diz do sulfato de cobre como preservante
e como fungicida agrícola?

Dois corpos literários distintos usam o mesmo sal para fins diferentes: proteção de
madeira e fitopatologia agronômica (calda bordalesa). **A busca começa junto com S1 e
S2 e alimenta as demais rodadas**; só a síntese fica para o fim.

**Critério de fracasso:** cobrir só um dos dois campos e declarar o outro como não
coberto — nunca apresentar um como se fosse o todo.

### S4 · Legislação, regras e proibições — com competência tripartite **correta**

**Correção da v1:** a v1 escreveu "Anvisa e MAPA para agrotóxico", o que sugere dois
registros independentes. **O correto:** no Brasil o **MAPA é o órgão registrante e
coordenador** do agrotóxico, com **avaliação de saúde pela Anvisa** e **avaliação
ambiental pelo Ibama** — três agências, **um** registro. E o **preservante de madeira
é registro do Ibama**, regime separado (foi esse registro que instruiu a ficha do
Tanalith 60% CCA-C).

**Cobertura pretendida:** UE (BPR — biocidas, com o sulfato de cobre como substância
ativa aprovada com restrição por tipo de produto; e CLP para classificação de perigo);
EUA (EPA — pesticida e preservante; OSHA PEL); Austrália (APVMA); Brasil (as três
agências acima, mais MTE para NR-15/NR-6).

**Mede:** onde é **permitido**, **restrito** e **proibido**, e com que fundamento —
separando sempre **classificação de perigo** × **critério de qualidade ambiental** ×
**padrão de potabilidade** × **registro de produto**.

**Critério de fracasso:** se Eur-Lex/ECHA seguirem bloqueados (HTTP 202 por WAF, como
na gaveta do boro), a gaveta **declara o bloqueio por jurisdição** e não preenche por
analogia. **A v1 afirmou "na maioria das jurisdições" sem fonte — isso sai do texto
até S4 medir.**

### S5 · O que está fora de conformidade no Brasil

**Estado: não medido.** Atestar irregularidade exige norma + prática + comparação; a
gaveta tem **nenhuma das três** hoje.

**A distinção que não se pode perder:** a NR-15 não ter limite para cobre **não é
irregularidade — é ausência de parâmetro nacional**. O trabalhador brasileiro exposto
a poeira ou névoa de cobre não tem valor de referência próprio, e o NIOSH de 1 mg/m³
é referência estrangeira. São afirmações diferentes e o capítulo não as confunde.

**Fonte a buscar:** registros do Ibama para preservativos; registros MAPA/Anvisa para
agrotóxicos à base de cobre; autuações publicadas.

**Critério de fracasso:** sem registro nem autuação, declarar "não foi possível
estabelecer conformidade" — nunca "está irregular".

### S6 · Anvisa e fiscalização — quem fiscaliza o quê

**Pergunta:** o que a Anvisa regula no sulfato de cobre e qual é a divisão real de
fiscalização?

**O que a rodada deve estabelecer, com fonte por agência:** Anvisa (saneantes,
antissépticos, água — e **avaliação de saúde** no registro de agrotóxico); Ibama
(**registro** de preservante de madeira e **avaliação ambiental** de agrotóxico);
MAPA (**registro** de agrotóxico e fertilizante); MTE (NR-15/NR-6, fiscalização do
trabalho).

**O achado, se confirmar:** o sulfato de cobre como preservante não está na Anvisa —
está no Ibama; e como agrotóxico tem registro tripartite. **"Vácuo de competência" só
se afirma com a fonte de cada agência**, nunca pela ausência de uma.

### S7 · As três curvas — remédio, veneno e dose de preservação

**Pergunta:** por que a mesma substância é remédio numa dose e veneno em outra, e onde
ficam as fronteiras?

**Correção da v1, integral:** a rodada **não** elege um número como "a fronteira".
Separa três domínios com unidades, meios e vias diferentes:

**(a) Necessidade nutricional.** O cobre é micronutriente essencial; a referência é em
**mg Cu/dia**, e a deficiência produz anemia e neutropenia. Faixa de homeostase, não
limiar de toxicidade. *(A v1 citava ~1 mg/dia sem fonte — vai para S1/S3 como dado a
custodiar, não como número herdado.)*

**(b) Referência de exposição e toxicidade, por via e por meio.** Aqui convivem, e
**não se convertem**:

| Via / meio | Grandeza | Valor ancorado | Endpoint |
|---|---|---|---|
| oral em água | mg Cu/L | NOAEL **2** · LOAEL **4** (náusea) · vômito ≥**6** | agudo gastrintestinal |
| oral em dose | mg Cu/kg/dia | a custodiar (E3) | **crônico hepático** — efeito crítico |
| inalatória | mg Cu/m³ | NIOSH **1**; **NR-15 sem limite** | respiratório |
| aquática | µg/L | invertebrado **1,11** crônico · **2,05** agudo; CONAMA 357 **9** | ecotoxicológico |

**(c) Dose antifúngica.** Medida em **massa de preservante por volume de material** —
grandeza de outra natureza. E **a gaveta já tem os números, custodiados e nunca
usados** (Gauss 2020, Tabela 2.6, L2565–2625):

| Fonte | Espécie | Método | Preservante | Retenção de i.a. (kg/m³) |
|---|---|---|---|---|
| [1] | ***T. siamensis*** | full-cell (vácuo 670 mmHg + pressão 2,5–8,5 bar) | 6% CCB (sal) | **3,9–17,5** |
| [1] | *B. stenostachya* | idem | 6% CCB | 3,5–15,9 |
| [1] | *D. asper* | idem | 6% CCB | 3,4–14,4 |
| [2] | *D. giganteus* | imersão 5–15 dias | 1% CCB (óxido) | 0,60–1,43 |
| [2] | *D. giganteus* | imersão | 3% CCB | 0,63–1,72 |
| [2] | *B. vulgaris* | imersão | 1% CCB | 0,68–2,20 |
| [2] | *B. vulgaris* | imersão | 3% CCB | 1,93–10,80 |
| [2] | *D. giganteus* | Boucherie modificado (0,7 MPa) | 1% CCB | 0,28 |
| [2] | *D. giganteus* | Boucherie modificado | 3% CCB | 1,40 |
| [3] | *B. vulgaris* | full-cell (600 mmHg + 12 kg/cm²) | 2–4% ACQ | 4,33–10,74 |
| [3] | *B. vulgaris* | full-cell | 2–4% CCA | 4,87–14,54 |
| [5] | ***P. edulis*** | full-cell comercial, alvo **4,0** | CCA | **0,88** — **22%** do alvo |
| [5] | ***P. edulis*** | full-cell comercial, alvo **6,4** | CCA | **1,49** — **23%** do alvo |
| [5] | *Pinus* sul (referência do mesmo estudo) | idem | CCA 4,0 / 6,4 | 4,61 (**115%**) / 7,12 (**111%**) |

*Fontes da Tabela 2.6: [1] Kim, Tang & Liese 2011 · [2] Tiburtino et al. 2015b ·
[3] Wahab et al. 2015 · [5] Lee, Chen & Tainter 2001.*

**O achado de S7 já está no disco, e é forte — mas é de UM ensaio, não de uma regra.**
No estudo [5] (Lee, Chen & Tainter 2001), em ***P. edulis*** o alvo de 4,0 kg/m³ rendeu
**0,88** e o de 6,4 rendeu **1,49** — **22% e 23% do alvo**. O *Pinus* sul de
referência, no **mesmo** estudo, rendeu **115% e 111%**. Os demais ensaios da tabela
mostram bambu retendo de 0,28 a 17,5 kg/m³ conforme **espécie e método** — ou seja, a
retenção do bambu é altamente variável, e a comparação direta com madeira existe
**apenas** nesse par *P. edulis* × *Pinus* de um único trabalho.

**O que se pode afirmar:** naquele ensaio, o alvo nominal não foi atingido em *P.
edulis* e foi atingido em *Pinus*. **O que NÃO se pode afirmar:** "o bambu não retém
como a madeira retém", como se fosse propriedade geral do material. Isso excede a
evidência disponível e é o tipo de generalização que a casa proíbe.

**A consequência que se mantém, e é a que importa:** *quando* o alvo nominal não é
atingido, a dose que chega ao fungo é menor que a projetada — e nesse ensaio ele não
foi atingido em bambu. **A dosagem de bula não descreve o que ficou no material** é
conclusão válida **para aquele resultado**, e passa a ser pergunta de S7 para os
demais: por espécie e por método, a retenção medida bate com o alvo?

**A pergunta que isso abre e que a v1 não fazia:** se a retenção real é fração do
alvo, a dose que chega ao fungo é menor que a projetada, e a dose efetiva passa a
depender de espécie, método e posição no colmo. **A dosagem de bula não descreve o que
ficou no material.**

**Conversão entre (c) e (b):** exige massa de material tratado, área exposta, forma
química e via. **É proibida como conta direta** — três curvas, três unidades, três
seções, nenhuma tabela que as emparelhe.

**Critério de fracasso:** se a rodada entregar tabela que compare as três grandezas
sem unidades separadas, falhou por definição.

### S7-ter · Retenção, lixiviação e durabilidade — o material custodiado que faltava

**Pergunta:** como retenção inicial, lixiviação e durabilidade se relacionam em
tratamentos de bambu com preservantes cúpricos?

**Ataca:** a auditoria R5 apontou que este material **está custodiado e o plano não o
consultava** — e ele é o único da gaveta que mede **bambu tratado com CCB em campo**:

| Caminho custodiado | O que contém |
|---|---|
| `_privado/fontes-documentais/ago_28_Boratos_Cobre/md/Rusch_et_al_2023_Bambu_CCB_Lixiviacao.md` | estudo com bambu tratado com CCB, **proporção de sulfato de cobre na formulação**, durabilidade após cinco anos, distribuição e lixiviação de Cu e Cr |
| `_privado/fichas/ago_28_CCA_CCB/rusch-2023-ccb-bambu-durabilidade-lixiviacao.md` | síntese curatorial: resultados delimitados para CCB em *Dendrocalamus asper*, limites e necessidades de pesquisa |
| `_privado/fontes-documentais/ago_28_Boratos_Cobre/md/WHO_2004_Copper-in-Drinking-Water_Background.md` | fonte OMS sobre cobre na água potável — **inclui o estudo dos 61 voluntários e o NOAEL** que S7 usa |

**Por que isso muda S7:** o WHO 2004 é a **fonte primária** do NOAEL de 2 mg Cu/L que
a v1 citava e a v2 contextualiza. Usá-la fecha a corrente: o número deixa de ser
herdado de segunda mão. E Rusch 2023 traz o **teor de sulfato de cobre na formulação
do CCB** — que é o dado que falta para converter `kg/m³ de sal` em `kg/m³ de Cu`.

**Critério de fracasso:** se Rusch 2023 não trouxer a proporção de sulfato de cobre na
formulação, a conversão sal→Cu no CCB continua **não medida**, e a gaveta declara isso
em vez de estimar.

---

### S7-bis · A proporção agricultura × preservante — declarada não medida

**A pergunta do soberano:** qual a proporção do uso agrícola comparada ao uso como
inibidor de fungo?

**Não medido, e está dito aqui, não em nota de pé.** O ComexStat mede comércio, não
destino: não há NCM que diga "este cobre foi para lavoura ou para autoclave".

| Uso | Papel do cobre | Registro / domínio | Proporção |
|---|---|---|---|
| **Agricultura** | fungicida (calda bordalesa), micronutriente | MAPA/Anvisa/Ibama — agrotóxico; MAPA — fertilizante | **a medir** |
| **Preservante** | fungicida | Ibama — preservativo de madeira | **a medir** |
| **Outros** (algicida, reagente, ração) | diversos | diversos | **a medir** |

**O que a rodada faz:** verifica se a proporção é **mensurável** por alguma via —
registros de agrotóxico do MAPA por ingrediente ativo, dados de associação setorial,
volume de preservante registrado no Ibama — e declara **quais limites impedem
estimar**. A fatia mundial de uso (USGS) entra só como **ordem de grandeza global** e
**não** pode ser aplicada ao Brasil como medição nacional.

**Critério de fracasso:** se nenhuma via permitir estimativa, a gaveta declara a
proporção como **não estimável com fontes públicas disponíveis** — o que é resultado,
não desistência.

---

## 4. Comércio brasileiro medido — com a interpretação corrigida

Consulta direta à API ComexStat, NCM 28332510 + 28332520, série 1997–2026.

| Ano | kg | US$ FOB | US$/kg |
|---|---:|---:|---:|
| 1997 | 1.279.269 | 1.292.541 | 1,01 |
| 2001 | 446.373 | 432.948 | 0,97 |
| 2006 | 118.525 | 222.111 | 1,87 |
| 2010 | 57.040 | 159.170 | 2,79 |
| 2015 | 25.206 | 78.011 | 3,09 |
| 2020 | 9.350 | 95.954 | 10,26 |
| 2022 | 332.456 | 929.708 | 2,80 |
| 2024 | 202.238 | 680.288 | 3,36 |
| 2025 | **177.854** | **370.053** | **2,08** |
| 2026* | 86.640 | 385.145 | 4,45 |

\* parcial. **Queda de ~86% entre 1997 e 2020**, com repiques em 2022 e 2024.

**Origem 2025 — massa e valor são participações DIFERENTES, e a v1 confundiu as duas:**

| Origem | t | % da massa | US$ FOB | % do valor |
|---|---:|---:|---:|---:|
| China | 143,000 | **80,4%** | 178.777 | **48,3%** |
| Peru | 27,000 | 15,2% | 73.908 | 20,0% |
| Polônia | 3,000 | 1,7% | 13.096 | 3,5% |
| Itália | 2,000 | 1,1% | 17.370 | 4,7% |
| Estados Unidos | 1,357 | 0,8% | 61.433 | 16,6% |
| demais (7 países) | 1,497 | 0,8% | 25.469 | 6,9% |
| **Total** | **177,854** | 100% | **370.053** | 100% |

**A v1 escreveu "China 143,0 t (48,3%)" — misturando a coluna de massa com o
percentual de valor.** Na massa, a China é **80,4%**; no valor, **48,3%**. A
divergência entre as duas não é ruído: significa que o quilo chinês entra a
**US$ 1,25/kg** enquanto o americano entra a **US$ 45,57/kg** — quase **37×**. A
pauta deste NCM mistura produto a granel com produto de alto valor agregado, e é
**por isso** que o preço médio de US$ 2,08/kg não descreve nada. *(Hipótese a
verificar na NCM/Receita; a razão de preços é medida.)*

**Hipóteses declaradas como hipóteses, não como achado:** (i) a dispersão de preço
por origem (US$ 1,25 a 45,57/kg) **sugere** pauta que mistura granel e produto
formulado ou grau reagente; (ii) volatilidade dessa magnitude na série **sugere**
compra por lote, não consumo estável. Ambas se verificam na NCM/Receita ou não se
afirmam.

### 4.1 O contraste com o minério — dado comercial, e só isso

Em 2025 o Brasil **exportou 1.451.750 t de minério e concentrado de cobre** (NCM
2603, US$ 5,01 bi) e **importou 177,9 t de sulfato**: razão de **~8.000:1 em massa de
produto**.

**A v1 concluiu daí "vende a rocha, compra o reagente" e chamou de padrão
primário-exportador. A conclusão saiu, porque excede o que o NCM mede:**

- **massa de minério não é massa de cobre contido** — teor típico de 0,3–1%;
- importação de sulfato **não mede consumo** — pode haver produção nacional, que esta
  gaveta não mediu;
- não há, aqui, dado de produção interna de refinado nem de sulfato.

**O que fica:** o contraste físico, como dado comercial reproduzível. **O que sai:** a
inferência econômica, até que E7 (elemento) meça cobre contido, refino e produção
interna. Confirmada a assimetria depois da medição, ela volta ao texto com o número
certo; antes disso, seria conclusão com aparência de achado.

---

## 5. Ordem proposta — por dependência, não por dramaticidade

**S1 → S2 → S7 → S7-ter → S7-bis → S4 → S5 → S6 → S3**

A v1 punha S7 primeiro para "atacar a pergunta do soberano de frente". **Errado:** S7
depende da química (S1) e dos riscos (S2) para separar as curvas — sem eles, separa
nada. S7 vai em terceiro. **S7-ter logo depois, porque é leitura de material já
custodiado** (Rusch 2023, WHO 2004): custo quase zero, e fecha a corrente do NOAEL e
da conversão sal→Cu. S7-bis em seguida, para declarar de uma vez o que não é
mensurável. S4 antes de S5/S6 porque sem a norma não há como medir conformidade nem
competência. **S3 começa junto com S1** e sintetiza ao fim.

---

## 6. Os furos da auditoria e o que foi feito de cada um

| Furo (parecer R4) | Correção nesta versão |
|---|---|
| S7 elege 2 mg Cu/L como fronteira universal; efeito crítico é hepático, não gástrico | §1 e S7 reescritos: três domínios separados, endpoint hepático nomeado, proibição de tabela única |
| Falta a pergunta "por que o cúprico no bambu" | S1 ganha a subpergunta, com a Tabela 2.5 como base custodiada |
| "vende a rocha, compra o reagente" excede o NCM | §4.1: contraste mantido como dado de comércio; **inferência econômica retirada** |
| Competência tripartite simplificada | S4 e S6: MAPA registrante, Anvisa saúde, Ibama ambiente **e** registro de preservante — um registro, três avaliações |
| Omissão do acervo: Gauss 2020, Tabelas 2.5 e 2.6 | incorporadas: §2.1 (composição, com verificação cruzada) e S7 (retenções em kg/m³) |
| Ordem inadequada | §5: S7 move para terceiro; S3 inicia junto |

### 6.1 Segunda auditoria (R5) — quatro furos novos, todos corrigidos

A R5 auditou a v2 e deu `REPLANEJAR` outra vez. **Ela estava certa nos quatro, e dois
são erros meus de leitura de tabela:**

| Furo (parecer R5) | O que eu fiz de errado | Correção na v3 |
|---|---|---|
| **Origem 2025: "China 143,0 t (48,3%)"** | misturei a coluna de **massa** com o percentual de **valor**. Na massa a China é 80,4%; no valor, 48,3% | tabela com **massa e valor separados**; a dispersão de preço (US$ 1,25 a 148,43/kg) passa a ser o achado |
| **Tabela 2.6: espécies atribuídas errado** | dei "3,9–17,5" como conjunto de *B. stenostachya* e *D. asper* — na tabela, esse intervalo é de ***T. siamensis*** | tabela reescrita **por espécie**, com a fonte numerada [1]–[5] |
| **Generalização "o bambu não retém como a madeira"** | a comparação existe **num único ensaio** (*P. edulis* × *Pinus*, fonte [5]) | conclusão **restrita àquele ensaio**; o resto da tabela mostra variação de 0,28 a 17,5 kg/m³ |
| **"barato" e "menor toxicidade mamífera"** | a Tabela 2.5 **não diz isso** — foi afirmação minha, herdada da v1 | removidas; voltam como **pergunta** de S2, com fonte própria |
| **3 omissões de acervo** (Rusch 2023, ficha Rusch, WHO 2004) | material custodiado, não consultado | nova rodada **S7-ter**, que também fecha a corrente do NOAEL |

**Pendência aceita e não executada nesta versão:** a auditoria R4 sugeriu que E2 (plano
do elemento) distinga **produção de mina, refino e metal**. Fica registrada para a
próxima revisão de `01-plano-de-pesquisa.md` — não foi feita aqui para não misturar o
escopo dos dois planos.

---

## 7. O que este plano não autoriza

- **Não** autoriza afirmar proporção agrícola × preservante no Brasil: não medida
  (S7-bis).
- **Não** autoriza dizer que há uso irregular no Brasil: ausência de parâmetro ≠
  irregularidade (S5).
- **Não** autoriza atribuir à Anvisa o preservante de madeira nem sugerir registros
  paralelos de agrotóxico (S4, S6).
- **Não** autoriza comparar as três curvas numa tabela única nem converter kg/m³ de
  material em mg/kg de corpo (S7).
- **Não** autoriza a inferência "vende a rocha, compra o reagente" sem medir cobre
  contido (§4.1).
- **Não** autoriza converter sal em cobre elementar sem declarar o fator (3,93).
- **Não** autoriza generalizar retenção de um ensaio para "o bambu" como material
  (§6.1): a comparação com *Pinus* existe num único trabalho.
- **Não** autoriza estender ao bambu o que se medir em madeira — nem o inverso.
- **Não** autoriza publicar antes da auditoria interna e da revisão humana nominal.
- **Não** é homologação.

---

**Controle de fronteiras.** Medido (§2.1, §4) separado de plano (§3) e de limite (§7).
Toda hipótese está marcada como hipótese. A v1 superada está preservada em
`99-plano-sulfato-v1-superado.md`. Estado: **em-revisao-documental**; não homologado.
