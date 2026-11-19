---
titulo: "As conexões: onde o bambu para de ser material e vira problema"
subtitulo: "O primeiro artigo falou do bambu. Este fala do ponto onde ele se encontra com outra coisa"
tipo_documental: material-didatico-institucional
estado_documental: em-revisao-documental
responsavel_curadoria: pendente — nao designado
fonte_primaria: 254 PDFs da coleção Advances in Bamboo Science; inventário e sha256 em
  takwaratec/TakwaraTec-Laboratorio-Editorial, branch bambu-science/decupagem-20261118-r1,
  ops/command-center/task-results/BAMBU-SCIENCE/MANIFESTO_CUSTODIA_PDFS.txt
material: didatico
publico: leigo
versao: 1
nota_de_padrao: "Rodapé, citação e formato de front matter ainda não têm padrão homologado. Não trate este arquivo como modelo."
---

# As conexões: onde o bambu para de ser material e vira problema

## Antes de começar: o que este artigo não repete — e o que ele não é

O primeiro artigo respondeu "quanto o bambu aguenta". Ele mediu resistência à compressão, à flexão, quanto um
colmo suporta, por que a média engana. Aquele texto é sobre o material.

Este texto é sobre **o circunstante**: o momento em que dois bambus precisam virar uma estrutura. E ali a conversa
muda de assunto, porque o bambu tem uma vantagem e uma desvantagem que são a mesma coisa — ele é um tubo de fibra
longa. A fibra corre de ponta a ponta. No sentido da fibra, ele é excelente. No sentido atravessado, é uma matriz
que não segura quase nada.

Toda conexão obriga a força a sair do sentido da fibra. Começa aí o problema.

**Uma separação necessária.** O Acervo tem um boletim técnico autoral sobre conexões — *Solda Vegetal: Conexões
Estruturais e Biocompósitos em Bambu* — que descreve uma **proposta** de sistema de fixação com poliuretano vegetal,
declarado ali como especificação autoral com desempenho a verificar. Este artigo é outra coisa: ele **não descreve
nem avalia aquele sistema**, não o repete e não o contradiz. Ele reporta **o que a literatura científica mediu sobre
conexões de bambu**. Onde este texto diz "a ligação varia 0,47", é medição publicada; onde o boletim diz "propõe-se
a resolver o gargalo", é proposta declarada como proposta. As duas camadas não se misturam.

---

## As palavras deste artigo, antes de elas aparecerem

Este texto usa um punhado de termos técnicos. Explico todos aqui, uma vez, para não interromper a leitura depois.

- **COV** (coeficiente de variação): o quanto um conjunto de medidas se espalha. COV 0,28 significa que o desvio
  típico é 28% da média. Quanto maior, menos previsível é o material.
- **MPa** (megapascal): unidade de tensão — força dividida por área. **1 MPa = 1 N/mm² = 10,2 kgf/cm²**. Ou seja:
  1 MPa é a pressão de cerca de dez quilos apoiados em um centímetro quadrado.
- **N** (newton): força. **10 N ≈ 1 kgf**. Um quilo de peso apoiado na mão é cerca de 10 N.
- **kN** (quilonewton): mil newtons, ou cerca de 100 kgf.
- **N·m** (newton-metro): momento — a força multiplicada pela distância. É o que você faz ao apertar um parafuso com
  uma chave: força na ponta vezes o comprimento da chave.
- **Momento**: o mesmo que "torque" em linguagem comum. Uma ligação que resiste ao vento ou ao peso de um telhado
  resiste a momento.
- **Rigidez**: o quanto a peça resiste a se deformar. Peça rígida dobra pouco; peça flexível dobra muito sob a mesma
  força.
- **N/mm** e **N·m/rad**: rigidez — quantos newtons são precisos para deslocar um milímetro, e quantos newtons-metro
  para girar um radiano.
- **Flecha**: o quanto a peça se desloca ou dobra quando carregada.
- **Escoamento**: o ponto em que a peça deixa de se comportar como mola e passa a se deformar de vez.
- **Cisalhamento**: força que tenta "deslizar" uma camada do material sobre a outra — como passar manteiga.
- **Histerese**: o caminho de ida diferente do caminho de volta quando a peça é carregada e descarregada. É a
  assinatura de que algo já se deformou.
- **Pinçamento**: perda de rigidez no ciclo de volta da histerese. A ligação folgou.
- **Estado-limite**: a condição a partir da qual a estrutura deixa de cumprir sua função — ou de servir, ou de ser
  segura.
- **Eixo neutro**: a linha dentro de uma peça dobrada que não fica nem esticada nem comprimida.
- **Flambagem**: o colapso de uma peça esbelta por dobra lateral, antes de o material em si quebrar.
- **Anastomose**: em botânica, a união de vasos que se conectam entre si formando rede.
- **ISO**: International Organization for Standardization — organização internacional que publica normas técnicas.
- **TR** (Technical Report): documento técnico informativo da ISO, sem força de norma.
- **Ortotrópico**: material que responde de forma diferente conforme a direção da força. A madeira e o bambu são.
- **Colmo**: o caule do bambu, o tubo em si. É a peça estrutural.
- **Corpo de prova**: o pedaço cortado e ensaiado em laboratório. "Amostra" e "corpo de prova" aparecem como
  sinônimos aqui.
- **Tensão**: força por unidade de área. Não é a força total — é o quanto ela se concentra.
- **Compressão**: força que aperta a peça. **Tração**: força que a estica.
- **Percentil**: onde um valor cai dentro do conjunto. O 5º percentil é o valor abaixo do qual ficam 5% dos
  resultados — ou seja, de cada 20 medidas, uma é pior.
- **Valor característico**: o número que se adota em projeto, calculado a partir da amostra com margem estatística.
  Quase sempre menor que a média.
- **Normalização**: corrigir uma medida pelas dimensões da peça (diâmetro, vão), para poder comparar com outra de
  tamanho diferente.

Com isso, o texto pode usar os termos sem parar para explicá-los.

---

## 1. O problema em uma frase: um tubo oco que não gosta de ser furado

Quando você fura um bambu para passar um parafuso, está cortando fibra longa. A fibra resiste muito no comprimento;
no furo, ela se rompe antes do que se esperaria, porque não há fibra atravessada costurando o material de volta.

Um dos artigos da coleção enumera por que a ligação é o ponto fraco. Vale ler devagar, porque cada item é uma
consequência de geometria, não de má qualidade:

- **Os dois bambus não são iguais.** Diâmetro, espessura de parede e seção variam de colmo para colmo. Você está
  ligando duas peças com medidas diferentes.
- **O perfil é circular e oco.** Uma seção regular, como a madeira serrada ou o perfil de aço, tem face plana para
  apoiar conector. O bambu, não.
- **A superfície externa é lisa e rígida.** Aquilo que protege o colmo da chuva também atrapalha a aderência de
  cola ou resina.
- **A resistência ao cisalhamento é baixa.** Cisalhamento é a força que tenta "deslizar" uma camada sobre a outra.
  A literatura citada pelo artigo registra ordens de grandeza em torno de **12 MPa** nesse modo.
- **O material é ortotrópico.** Palavra difícil para uma coisa simples: ele responde de forma diferente conforme a
  direção da força. A fibra só existe no comprimento. Logo, a distribuição de esforço na ligação sai desigual.

Nada disso se resolve com "usar bambu melhor". São propriedades do colmo, e a ligação tem que ser desenhada em
volta delas.

---

## 2. Existe norma para isso — e ela é recente

Até pouco tempo, cada projeto de bambu inventava sua ligação. O artigo de 2022 assinado por Kent Harries e dois
colegas da Universidade de Pittsburgh diz isso sem rodeio: existem muitos estudos de ligação de bambu, **muitos
sobre conexões patenteadas**, e a maioria é pontual — o comportamento medido não se transporta para outra geometria
nem outra condição. Além disso, poucos estudos têm amostra estatisticamente significativa.

A resposta normativa veio com a **ISO 22156**, a norma internacional de projeto estrutural em bambu-colmo. O trecho
que interessa aqui é a **cláusula 10**, a de ligações. E ela oferece dois caminhos:

1. **Ensaio completo da ligação** (cláusula 10.2): você ensaia a ligação tal como vai usar, em escala real, com a
   mesma geometria, os mesmos conectores, os mesmos detalhes e os mesmos bambus. O resultado do ensaio vira o
   parâmetro de projeto.
2. **Capacidades de componente corroboradas por ensaio** (cláusula 10.3), quando é possível correlacionar com
   segurança o componente com o comportamento da ligação — por exemplo, a capacidade de apoio da ponta do colmo,
   que se liga direto à resistência admissível à compressão.

Para alguns tipos bem estabelecidos, a norma traz requisito específico (cláusulas 10.10 a 10.12). Para **a maioria**
das ligações, o caminho é o ensaio.

Isso tem uma consequência prática que o artigo original não esconde: **a norma diz o que fazer quando a ligação não
está na tabela.** Ela não proíbe a ligação nova. Ela exige que você a ensaie.

---

## 3. Os seis grupos: a norma organiza por caminho da força

Harries lembra que Janssen propôs, em 2000, classificar ligação de bambu pelo **mecanismo de transferência de
força**, e que a classificação foi refinada por Widyowijatnoko e adotada pela ISO 22156 em 2021.

A ideia é engenhosa e simples: em vez de dar nome à peça (parafuso, corda, luva), você pergunta **como a força
entra no colmo**. Três perguntas decidem tudo:

1. **Por qual método a força é transferida?** Compressão ao longo da fibra, compressão atravessada, tração,
   atrito, cisalhamento ou apoio.
2. **Onde o conector está?** Preso por fora do colmo ou dentro da cavidade; paralelo à fibra ou atravessado.
3. **É conexão ou ligação?** Aqui há uma distinção que quase todo mundo usa errado: **conexão** é entre um bambu e
   seu conector, ou entre o bambu e a base de apoio. **Ligação** (o termo técnico é *joint*) é a coleção de
   conexões. Duas ligações de bambu com bambu podem ser uma conexão (bambu 1 direto no bambu 2) ou duas (bambu 1
   ao conector, conector ao bambu 2).

Dessa combinação saem **seis grupos**. O grupo 1 serve principalmente para transmitir compressão; os grupos 2, 3 e
4 para tração. E o artigo registra um número que dá a dimensão do assunto: **dezessete combinações** dos grupos 1 a
4 já foram identificadas em ligações de bambu conhecidas.

Um detalhe que quase ninguém nota: o **grupo 5 não se combina** facilmente com os outros. E o grupo 6, quando
combina, geralmente combina com o grupo 3 — porque o que ele traz é pré-tensão, e pré-tensão serve para aumentar
atrito, que é justamente o que o grupo 3 faz.

---

## 4. O ensaio completo, passo a passo — e por que ele existe

O artigo não fica na teoria: ele pega uma ligação simples, a **junta boca-de-peixe parafusada** (um colmo
recortado em forma de boca de peixe e parafusado contra outro) e roda o processo inteiro de ensaio completo.

Os números do bambu usado, medidos sob a ISO 22157:

- umidade 11,4% (variação 0,02)
- densidade 757 kg/m³
- compressão paralela à fibra **43,0 MPa**, com variação de **0,27**
- módulo de compressão 7.390 MPa
- cisalhamento 11,0 MPa
- compressão perpendicular 9,9 MPa
- módulo na flexão 1.240 MPa, com variação de **0,26**

Os sete valores vêm da Tabela 1 do artigo, medidos em 20 corpos de prova (umidade e densidade) e 6 a 7 nos ensaios
mecânicos. Guarde aquele **0,27**. Ele vai reaparecer.

O ensaio seguiu a **ISO 16670** (método cíclico alternado para ligações com conector mecânico). Antes de explicar
os passos, dois termos: **flecha** é o quanto a peça se desloca quando carregada; **ciclo** é carregar num sentido,
inverter e voltar. Trinta ciclos de acomodação em frações da flecha de controle, depois três ciclos completos em cada
nível de 20% a 100% dessa flecha, com o nível subindo de 20% em 20%.

Um ponto que o artigo faz questão de marcar: **nenhum corpo de prova rompeu fisicamente.** O ensaio parou por
critério de utilidade, não por colapso: **flecha** — o deslocamento da peça — atingiu o vão dividido por 15 (610 mm
÷ 15 ≈ 41 mm). O que se pode afirmar é só isto: **neste ensaio, o limite prático chegou antes da ruptura do
material.** O que não se pode afirmar é que a ligação "falha por deformação em vez de romper" — o ensaio não foi
levado até a ruptura, então não mediu ruptura. Uma ligação que se deforma demais antes de qualquer colapso já é
inutilizável na prática, e foi esse o critério.

A partir das curvas, o artigo extrai os parâmetros pela **ISO TR 21141**:

- carga máxima **1.977 N** (espécime S2)
- rigidez elástica **220 N/mm**
- rigidez pós-pico **14 N/mm**
- ponto de escoamento **1.522 N** com 6,90 mm de flecha

---

## 5. O resultado que assusta: a variação come a capacidade

E aqui está o achado central, e a razão de este artigo existir separado do primeiro.

Os pesquisadores **normalizaram** os dados — converteram carga em momento aplicado, rigidez em rigidez
rotacional, e corrigiram pela geometria do colmo. A normalização melhorou pouco, porque os corpos de prova eram
parecidos (variação de geometria abaixo de 0,10). Melhorou mais na rigidez: cerca de 11% de redução na variação.

Depois calcularam os valores característicos. O valor característico não é a média — é o valor que se adota em
projeto, um piso estatístico. Para amostra de 40, o fator é 1,834.

O que saiu — e aqui é importante separar **dois métodos**, porque o artigo usa os dois:

**Tabela 4 do artigo original — valores normalizados. Para as duas resistências (M<sub>max</sub> e M<sub>y</sub>),
equação do 5º percentil com k = 1,834 (amostra de 40):**

| Grandeza | Média | Variação (COV) | Valor característico |
|---|---|---|---|
| Momento máximo M<sub>max</sub> | 807 N·m | 0,28 | **393 N·m** |
| Momento de escoamento M<sub>y</sub> | 469 N·m | **0,47** | **65 N·m** |
| Rigidez rotacional K<sub>θ</sub> | 31.390 N·m/rad | 0,41 | 29.050 (normal) / 26.740 (lognormal) |

Confira a conta: 807 × (1 − 1,834 × 0,28) = **393**. E 469 × (1 − 1,834 × 0,47) = **65**. As duas batem.

A rigidez é a **exceção da tabela** e usa outro fator: **1,15 ÷ √40 ≈ 0,182** (o artigo arredonda para 0,18). O
motivo está escrito na fonte: para **rigidez** a norma pede média com 75% de confiança, não o 5º percentil. É por
isso que a rigidez cai pouco (31.390 × (1 − 0,182 × 0,41) ≈ 29.050) e as resistências caem muito. **Duas perguntas
diferentes, dois fatores diferentes** — e misturar os dois é o erro clássico nesse tipo de tabela.

**Tabela 3 do artigo original — a curva característica, derivada dos parâmetros de carga e flecha:**

| Grandeza | Média | Curva característica | Queda |
|---|---|---|---|
| Carga máxima F<sub>max</sub> | 1.428 N | **693 N** | 51% |
| Carga de escoamento F<sub>y</sub> | 831 N | **115 N** | 86% |

Aqui a queda não sai de média × fator: sai da **curva característica inteira**, construída a partir da relação
momento-rotação. Note a diferença entre a média e a curva característica na carga máxima — 1.428 contra 693 — e na
carga de escoamento — 831 contra 115.

Olhe o escoamento: cai de 831 para **115 N**, e o momento de escoamento de 469 para **65 N·m**. É queda de 86% e
86%. Não é redução de segurança: é a diferença entre "o que se mediu uma vez" e "o que se pode garantir".

Olhe os dois números de variação: **0,27** na compressão do bambu e **0,47** no escoamento da ligação. A ligação
varia cerca de 1,7 vez mais que o material.

Uma ressalva honesta sobre essa comparação: são **grandezas diferentes** medidas em **corpos de prova diferentes** —
a compressão vem de 6 a 7 amostras de bambu, o escoamento de 40 curvas de envelope. Os dois números não provam por si que "a
ligação multiplica a dispersão"; mostram que, neste programa, a ligação foi a fonte de variação dominante. A
explicação provável é intuitiva (dois colmos que variam, um conector que varia, um furo que varia), mas provável não
é medido.

E há um segundo ponto, ainda mais incômodo, sobre **tamanho de amostra**.

O valor característico sai de uma conta simples: **média × (1 − k × variação)**, onde `k` é um fator que depende do
tamanho da amostra — quanto menos corpos de prova, maior o `k`. Para 40 amostras, `k` = 1,834; para 10, `k` = 2,088;
para 5, `k` = 2,484.

Agora veja o que acontece quando `k × variação` passa de 1: **o resultado fica negativo** — e valor característico
negativo não existe. A norma, nesse caso, devolve zero.

Para a variação de 0,47 do momento de escoamento, isso acontece quando `k` passa de 2,13 — ou seja, com **9 corpos
de prova ou menos**. No programa deste artigo, com a mesma média e a mesma variação, **o momento característico
cairia a zero se a amostra fosse menor que 10**. E se a amostra fosse maior que 2.000, o mesmo parâmetro subiria 55%,
para 101 N·m.

Traduzindo: **quem ensaia poucas ligações de bambu não obtém um número conservador — obtém nenhum número.** A norma
não devolve um valor pequeno. Devolve zero. E zero obriga a repensar o projeto inteiro.

Como ensaiar duas mil ligações é impraticável, a conclusão do artigo é direta: **o que sobra é reduzir o erro
sistemático**. Controle de ensaio, fabricação do corpo de prova, geometria, condições de contorno. Não é
refinamento acadêmico — é a única alavanca que existe.

---

## 6. Por que não calcular mecanismo por mecanismo

Parece razoável: a norma dá fórmula para cada mecanismo; calcule cada um e some. O artigo testa essa intuição na
prática e conclui o contrário.

A junta boca-de-peixe, mesmo sendo uma das ligações mais simples que existem, mobiliza **quatro** mecanismos de
transferência de força simultaneamente. A norma traz método para calcular cada um **isoladamente**. Mas a interação
entre eles é complexa o bastante para tornar o cálculo por componente **impraticável** — palavra do artigo.

Daí o ensaio completo, que tem exatamente essa função: não olhar cada mecanismo, olhar o conjunto. O que sai é uma
relação momento-rotação (ou carga-deslocamento) que pode entrar na análise, e capacidades que servem para projeto.

É uma inversão de método que vale para o leitor leigo entender: em materiais homogêneos, calcula-se a peça e
confia-se no cálculo. Em bambu, a peça é simples e o **encontro** é o problema.

Mas atenção — a norma **não** obriga a ensaiar toda ligação. Ela abre dois caminhos, e o segundo dispensa ensaio da
ligação inteira: quando a capacidade de um componente pode ser correlacionada com segurança ao comportamento da
ligação (o caso do apoio na ponta do colmo, ligado direto à resistência à compressão). O ensaio completo existe para
os casos em que essa correlação não é confiável — que, segundo o artigo, são a maioria.

---

## 7. O que acontece com a ligação quando a estrutura balança

O ensaio do Harries é cíclico justamente porque ligação de bambu não trabalha só parada. Um artigo de 2023 da
Universidade do Sudeste, em Nanjing, avaliou o comportamento sísmico de um pórtico de bambu de **três pavimentos**.

O que eles fizeram: modelaram numericamente, e para a ligação pilar-viga propuseram um método simplificado usando um
modelo histerético do tipo *Pinching4* no OpenSEES — nome que descreve o fenômeno: **pinçamento**. Pinçamento é a
perda de rigidez que aparece no ciclo de volta, quando a ligação já se deformou e não volta pelo mesmo caminho. É a
assinatura de uma ligação que folgou.

Os parâmetros do modelo foram **calibrados com resultados de ensaio**. Com isso rodaram análise dinâmica não linear
no tempo, com **vinte sismos** em três intensidades.

As conclusões dos autores:

1. O modelo calibrado reproduziu razoavelmente a histerese da ligação, inclusive o pinçamento e a degradação.
2. Sob os sismos das diferentes probabilidades de excedência em 50 anos, o pórtico atendeu aos estados-limite
   alvo.
3. A distorção entre pavimentos ficou bem distribuída na altura — padrão de deformação razoável.

O ponto para o leitor leigo: **a ligação é o que se modela, não o bambu.** No modelo sísmico, o material entra com
suas propriedades; **a ligação entra com parâmetros calibrados em ensaio**, porque não dá para deduzi-los. Quem
projeta bambu para sismo precisa de dados de ligação, não só de resistência de colmo.

---

## 8. A tradição já sabia — e a norma deu nome ao que ela fazia

Um artigo de revisão de 2024 sobre arquitetura de bambu organiza as ligações tradicionais em **três modos**, e cada
um tem o seu defeito, declarado com honestidade:

**Encaixe.** Imita o encaixe de madeira tradicional, com conexão elegante e aparência limpa. Problema: o colmo é
oco, e **fazer o entalhe destrói a estabilidade da estrutura**. Você abre a peça para encaixar e enfraquece onde
precisava de força.

**Amarração.** Mais trabalhosa, mas se adapta a colmos de diâmetros diferentes e permite formar T, cruz e outras
geometrias. Problema: **a ligação amarra frouxa com o tempo e não tem durabilidade**.

**Envolvimento.** Uma parte do colmo é entalhada e dobrada para abraçar a outra peça por fora. Gera um efeito
estético ordenado, muito usado em arquitetura. Problema: **a peça rasga com facilidade** por causa do esforço
relativo gerado no entalhe.

Repare que os três defeitos são o mesmo problema visto de ângulos diferentes: **cortar ou dobrar o colmo abre o
caminho da ruptura**. A tradição compensa isso com geometria e redundância. A norma compensa com ensaio e fator de
segurança. Nenhuma das duas elimina o problema.

---

## 9. O que a ligação faz com a estrutura inteira: o dado mais duro

Um artigo de 2026 da PUC-Rio mediu vigas estruturais feitas de ripas de bambu em três espécies — *Dendrocalamus
asper*, *Phyllostachys edulis* e *Phyllostachys reticulata*. Capacidade entre **9 kN e 16 kN**; melhor média com o
*D. asper*, **14,4 kN** contra 12,2 kN do *P. edulis*.

O número que importa para este artigo está na revisão de literatura que eles fazem, citando Zhou e colegas (2022):
vigas múltiplas de bambu **com ligações longitudinais** apresentaram **redução de 63,87% na capacidade máxima de
carga em flexão**.

Sessenta e três por cento. Não por causa de defeito no bambu: por causa do **encontro** entre os bambus. É a
quantificação da ideia que este artigo inteiro defende.

Vale registrar também o que a mesma revisão descreve do lado positivo: arame de aço e reforços equivalentes, quando
bem usados, recuperam desempenho — e Ghavami (1995) relatou **aumento de 400% na carga última** de vigas de concreto
reforçadas com bambu, comparadas às mesmas vigas sem reforço. Ligação ruim destrói; ligação boa não é enfeite, é
estrutura.

---

## 10. O nó do colmo: nem sempre ele ajuda

Existe uma confusão comum: "o nó do bambu é o reforço natural, então ligação perto do nó é melhor". A relação não é
automática, e um artigo brasileiro de 2024 mediu isso.

Seixas e colegas ensaiaram *Phyllostachys aurea* em flexão de quatro pontos, comparando modelos de cálculo com e sem
o efeito dos nós. A conclusão: **os nós influenciaram a resposta à flexão, tornando o colmo mais flexível** — e o
modelo que levava os nós em conta (Timoshenko ajustado com rigidez rotacional por nó) foi o que descreveu melhor o
comportamento real.

Mais flexível, não mais rígido. Para o desenho de ligação, isso significa que "colocar o conector junto ao nó" não é
garantia. O nó traz anastomose de vasos e reforço local, sim — mas a resposta global do colmo muda, e mudar a
rigidez muda como a força chega à ligação.

O mesmo artigo descreve o modo de ruptura do colmo, e ele é relevante para conexão: o bambu **não se dobra como aço,
madeira ou compósito polimérico**. Ele fratura de forma frágil ao longo do eixo neutro, por uma combinação de
cisalhamento e tração perpendicular à fibra perto do ponto de aplicação da carga, podendo vir antes amassamento e
flambagem local com lascas.

Leia de novo: **tração perpendicular à fibra**. É o esforço que uma ligação provoca quando fura ou aperta o colmo.

A coincidência é sugestiva, mas precisa de ressalva: o ensaio de ligação descrito neste artigo **não levou os corpos
de prova à ruptura** — parou no limite de flecha. Então não há, ali, observação direta do modo de ruptura da ligação
para comparar. O que se pode dizer é mais modesto e continua útil: **o colmo rompe por fragilidade fora do sentido da
fibra, e é exatamente esse o esforço que a ligação impõe.** Se a ligação rompe do mesmo modo, este artigo não mediu.

---

## 11. O que fazer, na prática, com o que está medido

Nada aqui é recomendação de projeto — este é material de divulgação. Mas o que a literatura permite afirmar:

**Ensaie a ligação, não só o colmo.** O caminho da cláusula 10.2 existe porque o cálculo por componente é
impraticável na interação. Se o projeto não tem ligação de catálogo, o ensaio completo é o caminho normativo.

**Conte os corpos de prova antes de começar.** Com variação alta, amostra pequena não dá número conservador: dá
zero. É a informação mais acionável do artigo do Harries.

**Espere variação maior que a do material.** Se a compressão do colmo varia 0,27 e o escoamento da ligação varia
0,48, a hipótese mais provável é que a variação nasça do encontro, não da medição. Não é conclusão fechada: o artigo
lista controle de ensaio, fabricação do corpo de prova, geometria e condições de contorno como fontes possíveis de
erro sistemático — e num ensaio servo-hidráulico bem controlado, as duas últimas pesam mais.

**Normalize pela geometria antes de comparar estudos.** Diâmetro, espessura e vão mudam o número. Comparar ligações
sem normalizar é comparar medidas de coisas diferentes.

**Trate a ligação como item de projeto, com o mesmo peso da peça.** Sessenta e três por cento de perda em viga com
ligação longitudinal não é detalhe construtivo. É o comportamento dominante.

**Não conte com o nó como reforço automático.** A evidência disponível mostra efeito na rigidez global, não um
reforço simples de ligação.

---

## 12. O que continua faltando

**A amostra.** Ligação de bambu quase nunca tem amostra grande, e o próprio artigo que demonstra o método tem
quarenta corpos de prova. O limite é prático, não teórico.

**Ligação padronizada com número publicado.** A maioria dos estudos, como o próprio Harries registra, é de conexão
patenteada ou pontual. Falta catálogo aberto de ligação com capacidade característica publicada, no formato em que
um projetista consiga usar.

**Ensaio de ligação em espécie brasileira.** A coleção cobre ligação em Guadua colombiana, em bambu laminado, em
ripa. O que existe de ligação ensaiada sob norma brasileira, em espécie nativa, é bem menos.

**Durabilidade da ligação.** O artigo de arquitetura diz que a amarração solta e não dura; o de monitoramento fala da
necessidade de inspeção por degradação. O que falta é número: quanto uma ligação perde em dez anos, em ambiente
úmido.

O **não obtido** desta frente continua valendo, mas agora com o contorno certo.

O artigo é: **Rivera-Segura, R.; Moya, R.; Gaitán-Álvarez, J.; Granados-Gamboa, M. (2024).** *Analysis of the
physical-mechanical properties of Dendrocalamus asper (Schult.) versus two Guadua angustifolia (Kunth) varieties,
South and Caribe in the Atlantic Region of Costa Rica.* Advances in Bamboo Science **6**, 100057. DOI
10.1016/j.bamboo.2024.100057.

Os metadados foram confirmados em registro público (fev. 2024) e o resumo foi lido. **O texto completo não foi
obtido** — o ScienceDirect bloqueou o acesso nesta máquina e no celular.

E aqui está o ponto que importa para este artigo: **pelo resumo, ele não trata de conexões.** Ele compara
propriedades físico-mecânicas do colmo — umidade, densidade, flexão, tração, diâmetro, espessura de parede — em três
materiais plantados no mesmo sítio, na Costa Rica. Uma das conclusões é que as duas variedades de *G. angustifolia*
quase não diferem entre si.

Ou seja: essa lacuna **não é deste artigo**. Ela pesa na matriz comparativa de propriedades do colmo, que é o
primeiro texto. Aqui fica registrada como limitação declarada, e não como dado faltante de ligação.

---

## Fontes deste artigo, em ordem de uso

- **Harries, K.; Rogers, C.; Brancaccio, M. (2022).** *Bamboo joint capacity determined by ISO 22156 'complete joint
  testing' provisions.* Advances in Bamboo Science 1, 100003. Universidade de Pittsburgh. — classificação por
  mecanismo, seis grupos, dezessete combinações, ensaio completo, tabela de parâmetros característicos, efeito do
  tamanho de amostra.
- **Barrile, V.; Genovese, E. (2024).** *Bamboo structures: innovative methods and applications for structural health
  monitoring and dissemination.* Advances in Bamboo Science 7, 100079. — os cinco motivos de a ligação ser ponto
  fraco; cisalhamento em torno de 12 MPa; necessidade de inspeção por degradação.
- **Ding, D.; Xian, M. (2024).** *Research trends and design strategies for bamboo architecture.* Advances in Bamboo
  Science 8, 100094. — os três modos tradicionais (encaixe, amarração, envolvimento) e o defeito de cada um.
- **Zhao, J.-C.; Qiu, H.-X. (2023).** *Seismic performance assessment of a multi-story bamboo frame structure.*
  Advances in Bamboo Science 2, 100011. Universidade do Sudeste, Nanjing. — ligação pilar-viga, Pinching4, vinte
  sismos, três intensidades.
- **Vasconcelos, P.Q.F.; Paciornik, S.; Silva, F.A. (2026).** *Mechanical behaviour of bamboo slat structural beams.*
  Advances in Bamboo Science 15, 100228. PUC-Rio. — 9 a 16 kN; *D. asper* 14,4 kN e *P. edulis* 12,2 kN; cita a
  perda de 63,87% com ligações longitudinais (Zhou et al. 2022) e o ganho de 400% com reforço (Ghavami 1995).
- **Seixas, M.; Cardoso, D.; Moreira, L.E.; Paciornik, S. (2024).** *Influence of elastic properties and nodes on the
  flexural behaviour of bamboo culms.* Advances in Bamboo Science 9, 100100. PUC-Rio e UFMG. — nós tornam o colmo
  mais flexível; ruptura frágil por cisalhamento e tração perpendicular à fibra.

Todas as citações são de artigos da coleção *Advances in Bamboo Science*, lidos integralmente com texto paginado.
**Onde conferir:** os 254 PDFs estão custodiados no Drive, em `CustodiaAcervo/bambu-science-r1/pdf/` (remoto
`gdrive-custodia:`), nomeados `BAM-001.pdf` a `BAM-254.pdf`. O manifesto com `sha256`, volume e tamanho de cada
um está no repositório de governança — `takwaratec/TakwaraTec-Laboratorio-Editorial`, branch
`bambu-science/decupagem-20261118-r1`, arquivo `ops/command-center/task-results/BAMBU-SCIENCE/MANIFESTO_CUSTODIA_PDFS.txt`
— e **não** neste repositório, onde não há binário. Cruze manifesto e Drive pelo ID do arquivo; título de artigo
de coleção é truncado e quase idêntico entre irmãos.
