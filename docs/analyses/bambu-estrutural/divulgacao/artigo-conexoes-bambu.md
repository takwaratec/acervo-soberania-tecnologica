---
titulo: "As conexões: onde o bambu para de ser material e vira problema"
subtitulo: "O primeiro texto falou do bambu. Este fala do ponto onde ele se encontra com outra coisa"
tipo_documental: material-didatico-institucional
estado_documental: em-revisao-documental
responsavel_curadoria: pendente — nao designado
material: didatico
publico: leigo
versao: 3
nota_de_padrao: "Rodapé, citação e formato de front matter ainda não têm padrão definido. Não trate este arquivo como modelo."
---


# As conexões: onde o bambu para de ser material e vira problema

## Antes de começar

O primeiro texto respondeu "quanto o bambu aguenta". Ele mediu resistência à compressão, à flexão, quanto um colmo
suporta, por que a média engana. Aquele texto era sobre o material.

Este é sobre **o encontro**. O momento em que dois bambus precisam virar uma estrutura. E ali a conversa muda de
assunto, porque o bambu tem uma vantagem e uma desvantagem que são a mesma coisa: ele é um tubo de fibra longa. A fibra
corre de ponta a ponta. No sentido da fibra ele é excelente; atravessado, é um feixe de canais que não segura quase nada.

Muitas conexões obrigam a força a sair do sentido da fibra — e é aí que começa o problema. A exceção é a conexão que
trabalha por compressão ao longo da fibra, apoiando a ponta de um colmo na outra: essa não fura nem atravessa nada.

O que este texto faz: mostra o que já foi medido sobre conexões de bambu, com números, e onde a medição ainda não
chegou. Não é revisão científica nem manual de projeto — é leitura para quem quer entender por que a conexão é o
ponto difícil, e o que se sabe de fato a respeito.

Uma ressalva de abrangência, e ela vale: isto **não é uma varredura sistemática da literatura**. Os estudos aqui
citados foram encontrados por leitura dirigida e por referências que se repetem entre artigos — não por busca formal
em base indexada, com critérios, datas e filtros declarados. Existe literatura sobre conexões de bambu que este texto
não leu, em chinês e em espanhol, em periódicos que não apareceram. O que está escrito aqui se sustenta pelo que foi
lido; o que não foi lido não está coberto.

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
- **Momento**: força aplicada a uma distância, tentando girar a peça. É o que você faz com uma chave de roda: força
  na ponta vezes o comprimento da chave. Não toda ligação é dimensionada para resistir a momento — algumas só
  transmitem força direta, e se apoiam em outro elemento para o resto.
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
- **Curva característica**: a curva de resposta (momento-rotação, carga-flecha) já corrigida para baixo pela margem
  estatística. É a curva da tabela, não a do ensaio.
- **PGA** (aceleração de pico do solo): a maior aceleração que o chão atinge durante um terremoto, medida em
  múltiplos de g (a gravidade). PGA 0,4g é quatro décimos da gravidade.
- **Confiança de 75%**: é uma propriedade do **procedimento**, não desta amostra. Diz que, se você repetisse esse
  mesmo procedimento de cálculo muitas vezes, em cerca de três de cada quatro o valor estimado ficaria abaixo do
  valor real. Não é probabilidade sobre o número que está nesta tabela — é sobre o método que o produziu.
- **Normalização**: corrigir uma medida pelas dimensões da peça (diâmetro, vão), para poder comparar com outra de
  tamanho diferente.
- **Curva de envelope** (ou de esqueleto): a curva que sobra quando você pega o pico de cada ciclo de carga e liga
  um ponto ao outro. É o "formato" da ligação, sem o vai e vem.
- **Erro sistemático**: erro que puxa todos os resultados para o mesmo lado, sempre. Diferente do acaso, que espalha
  para cima e para baixo e some na média.
- **Condições de contorno**: como a peça está presa nas pontas durante o ensaio — apoiada, engastada, livre. Muda o
  resultado mesmo com o mesmo material.
- **Distribuição normal / lognormal**: dois jeitos de descrever como os resultados se espalham. A normal é a curva em
  sino simétrica; a lognormal é assimétrica, com cauda longa de um lado. Quando os dados têm cauda, usar a segunda
  dá valor característico diferente.
- **Flexão de quatro pontos**: ensaio em que a peça é apoiada em dois pontos e carregada em outros dois, entre eles.
  Assim o trecho do meio fica sob momento constante, sem força de corte atrapalhando.
- **Teoria de Timoshenko**: modelo de cálculo de viga que leva em conta que a peça também se deforma por cisalhamento
  ao dobrar — não só por alongamento das fibras.

Com isso, o texto pode usar os termos sem parar para explicá-los.

---

## 1. O problema em uma frase: um tubo oco que não gosta de ser furado


Quando você fura um bambu para passar um parafuso, está cortando fibra longa. A fibra resiste muito no comprimento;
no furo, ela se rompe antes do que se esperaria, porque não há fibra atravessada costurando o material de volta.

Barrile e Genovese (2024) enumeram por que a ligação é o ponto fraco. Vale ler devagar, porque cada item é uma
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

**Hong e colegas (2019) abrem com exatamente este diagnóstico.** Em *Review on connections for original bamboo
structures* (*Journal of Renewable Materials*, v. 7, n. 8), eles registram que a geometria tubular, a parede
relativamente fina, a anisotropia e a variabilidade dos colmos dificultam a transferência confiável de esforços e a
padronização de componentes. É o problema estrutural central das conexões, e não é uma descoberta deste texto.

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

Para alguns tipos bem estabelecidos, a norma traz requisito específico (cláusulas 10.10 a 10.12). Para as demais, a
norma manda **qualificar a ligação** — e oferece duas vias: o ensaio completo (10.2) ou capacidades de componente
corroboradas por ensaio (10.3). O que ela não permite é usar a ligação sem qualificação.

Isso tem uma consequência prática que o artigo original não esconde: **a norma diz o que fazer quando a ligação não
está na tabela.** Ela não proíbe a ligação nova. Ela exige que você a qualifique. 


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

### O que a revisão de 2019 mediu

Hong e colegas (2019) organizam o mesmo assunto por outra via: duas famílias tradicionais (encaixes e amarrações) e quatro grupos de soluções modernas — juntas parafusadas;
juntas com perfis ou chapas de aço; juntas reforçadas por preenchimento; e outras soluções, incluindo reforços
poliméricos, componentes de madeira e peças personalizadas. É uma taxonomia vizinha à da norma, não idêntica, e
serve para conversar com a literatura mais antiga.

E ela traz cinco números que este artigo não teria como produzir:

| O que foi comparado | Ganho relatado |
|---|---:|
| Rigidez, três juntas com componentes de aço frente às tradicionais | mínimo **29%** |
| Resistência, no mesmo conjunto | mínimo **250%** |
| Resistência ao cisalhamento, reforço com fibra de carbono (CFRP) | **18,4%** |
| Capacidade, juntas com braçadeiras de madeira | aprox. **40%** |
| Massa, em certas juntas preenchidas com argamassa | **≥ 2,5 vezes** |

Duas ressalvas dos próprios autores, e que valem repetir: os números pertencem a estudos específicos compilados na
revisão e **não se generalizam** para outra espécie, geometria ou sistema; e a revisão conclui que **nenhuma solução
reúne plenamente** capacidade, rigidez, durabilidade, facilidade construtiva e baixo custo. Aquele último número —
massa 2,5 vezes maior — é o preço escondido do preenchimento: enche o vazio e resolve o cisalhamento, mas a peça
deixa de ser leve.

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
projeto, com margem estatística. Para **amostra de 40**, o fator é 1,834.

**Atenção à unidade de `n`, porque é aqui que quase todo mundo se perde.** O `n = 40` do artigo é o número de
**curvas de envelope** — uma por sentido de carregamento —, não o número de ligações físicas. As ligações físicas são
**20**. Quando este texto falar em `n`, é sempre **curva**. E a fonte registra mais um número que importa: a ISO 16670
recomenda **mínimo de seis réplicas**. Mas atenção à comparação — **seis réplicas servem para estimar a MÉDIA** das
propriedades mecânicas, não o valor característico. São grandezas diferentes, e o número 6 não valida a conta de valor
característico usada aqui. O que ele mostra é só isto: a norma de ensaio admite amostras bem menores que as 40 curvas
deste programa — e é essa distância que faz o efeito do tamanho de amostra, mostrado adiante, pesar tanto.

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

Olhe os dois números de variação: **0,27** na compressão do bambu e **0,47** no escoamento da ligação.

Um aviso para não parecer contradição: aparecem **dois** valores de variação para o escoamento em tabelas diferentes —
**0,48** para a carga de escoamento F<sub>y</sub> (em newtons) e **0,47** para o momento de escoamento
M<sub>y</sub> (em newton-metro). São a mesma ligação medida em duas grandezas; a pequena diferença é do cálculo de
momento, que multiplica a carga pela distância de cada corpo de prova. A ligação
varia cerca de 1,7 vez mais que o material.

Uma ressalva honesta sobre essa comparação: são **grandezas diferentes** medidas em **corpos de prova diferentes** —
a compressão vem de 6 a 7 amostras de bambu, o escoamento de 40 curvas de envelope. Os dois números não provam por si que "a
ligação multiplica a dispersão"; mostram que, neste programa, a ligação apresentou variação maior. A explicação
intuitiva — dois colmos que variam, um conector que varia, um furo que varia — é plausível, e o artigo não a testa.
Plausível não é medido.

E há um segundo ponto, ainda mais incômodo, sobre **tamanho de amostra**.

O valor característico sai de uma conta simples: **média × (1 − k × variação)**, onde `k` é um fator que depende do
tamanho da amostra — quanto **menos curvas**, maior o `k`. Para `n` = 40 curvas, `k` = 1,834; para 10, `k` = 2,088;
para 5, `k` = 2,484.

Agora veja o que acontece quando `k × variação` passa de 1: **o resultado fica negativo** — e valor característico
negativo não existe. A norma, nesse caso, devolve zero.

Para a variação de 0,47 do momento de escoamento, isso acontece quando `k` passa de 2,13 — ou seja, com **9 curvas
ou menos**. No programa deste artigo, com a mesma média e a mesma variação, **o momento característico cairia a zero
se `n` fosse menor que 10 curvas**. E se a amostra fosse maior que 2.000 curvas, o mesmo parâmetro subiria 55%, para
101 N·m.

Voltando à unidade: 9 curvas são **cerca de 5 ligações físicas** — porque cada ligação gera duas. O quadro é pior do
que parece à primeira vista.

Traduzindo: **quem ensaia poucas ligações de bambu não obtém um número conservador — obtém nenhum número.** A norma
não devolve um valor pequeno. Devolve zero. E zero obriga a repensar o projeto inteiro.

Como ensaiar duas mil curvas é impraticável, a conclusão do artigo é direta: **o que sobra é reduzir o erro
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
os casos em que essa correlação não é confiável.

---

## 7. O que acontece com a ligação quando a estrutura balança


O ensaio do Harries é cíclico justamente porque ligação de bambu não trabalha só parada. Um artigo de 2023 da
Universidade do Sudeste, em Nanjing, avaliou o comportamento sísmico de um pórtico de **três pavimentos** — e aqui é
preciso ser preciso sobre o material, porque ele **não** é colmo roliço. 

O estudo é de **bambu laminado colado**: tiras cortadas do colmo, secas e coladas em **seção retangular**. A ligação
pilar-viga é feita com **chapas de aço em T parafusadas**, com chapas de reforço atrás. Ou seja: não é a mesma família
do bambu roliço dos outros artigos deste texto. É bambu transformado em material de seção regular, ligado com peça de
aço. Isso tem duas consequências para quem lê: a **restrição do colmo roliço** que abriu este texto — circular e oco,
difícil de apoiar conector — **não se aplica a esse material**, porque a seção é retangular e maciça; e aparece um
componente novo que precisa ser dimensionado, o aço.

O que eles fizeram: modelaram numericamente, e para a ligação pilar-viga propuseram um método simplificado usando um
modelo histerético do tipo *Pinching4* — o nome vem de **pinçamento**, o fenômeno que ele descreve — implementado num
programa de cálculo estrutural chamado OpenSEES. Pinçamento é a
perda de rigidez que aparece no ciclo de volta, quando a ligação já se deformou e não volta pelo mesmo caminho. É a
assinatura de uma ligação que folgou.

Os parâmetros do modelo foram **calibrados com resultados de ensaio**. Com isso rodaram uma **análise dinâmica não
linear no tempo** — simulação em que a estrutura responde passo a passo a cada instante de um terremoto, admitindo que
ela já se deformou e não volta pelo mesmo caminho — com **vinte sismos** em três intensidades.

As conclusões dos autores:

1. O modelo calibrado reproduziu razoavelmente a histerese da ligação, inclusive o pinçamento e a degradação.
2. Sob os sismos das diferentes **probabilidades de excedência em 50 anos** — o artigo usa três níveis, com aceleração
   de pico correspondentes às chances de 63,2%, 10% e 2% de serem superados em meio século — o pórtico atendeu aos
   estados-limite alvo. Para comparação: a intensidade máxima usada é ordem de grandeza de sismo forte.
   *(Divergência interna da fonte, declarada: o texto diz PGA de 0,07g, 0,1g e 0,4g; a legenda da figura 6 e a tabela
   4 dizem 0,07g, **0,2g** e 0,4g para o nível intermediário. Não é possível decidir qual vale sem os autores.)*
3. A distorção entre pavimentos ficou bem distribuída na altura — padrão de deformação razoável. 

O ponto para o leitor leigo: no modelo sísmico, **o material entra com suas propriedades e a ligação entra com
parâmetros calibrados em ensaio** — porque a ligação não se deduz da resistência do bambu. O estudo modela as duas
coisas, não só uma. Quem projeta bambu para sismo precisa de dados de ligação, não só de resistência de colmo.

---

## 8. A tradição já sabia — e a norma deu nome ao que ela fazia


Um artigo de revisão de 2024 sobre arquitetura de bambu organiza as ligações tradicionais em **três modos**, e cada
um tem o seu defeito, declarado com honestidade.

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

### O que aconteceu de fato nas obras brasileiras

Aqui há dado de campo, não de laboratório. Bussinger (2024) examinou **16 obras construídas no estado de São Paulo
entre 2003 e 2023** com colmo como elemento estrutural principal. Quatro achados mudam a conversa:

- **Mais de um conector por estrutura, sem correlação com a forma.** A autora observa o uso frequente de mais de um
  tipo de conexão para montar um conector, e mais de um tipo de conector em cada estrutura, **sem relação clara entre
  a forma da estrutura e o detalhe escolhido**. Ou seja: na prática, a escolha do conector não seguiu um critério
  geométrico explícito. As estruturas de colmo, conclui ela, **não são naturalmente padronizáveis**.
- **O conector "boca-de-peixe" foi abandonado.** Desaparece progressivamente das obras a partir de 2003,
  possivelmente por incompatibilidade com as espécies usadas no Brasil, propensão a fissuras e dificuldade de
  execução. É um sistema que saiu de uso **nas obras paulistas estudadas** — por acumulação de problemas, não por decreto. O
recorte é São Paulo, 2003–2023; o artigo não afirma que o abandono tenha acontecido no mundo.
- **Fissura em todas as varas de todos os casos.** Não é exceção: é regra. O que reforça a tese deste artigo — o
  colmo fissura, e a ligação é onde a fissura tem consequência estrutural.
- **Nível tecnológico médio.** A maioria dos projetos usa conectores de nível tecnológico médio; nenhum caso no nível
  baixo e apenas dois no nível alto.

O estudo usa como referência a **ABNT NBR 16828**, a **ABNT NBR 17043:2023** (classificação de varas, com conicidade
≤ 1% e encurvamento L/100) e a **ISO 22156:2021**. É a ponte entre a norma que este texto discute e a obra que existe
no Brasil.

---

## 9. O que a ligação faz com a estrutura inteira: o dado mais duro


Um artigo de 2026 da PUC-Rio mediu vigas estruturais feitas de ripas de bambu em três espécies — *Dendrocalamus
asper*, *Phyllostachys edulis* e *Phyllostachys reticulata*. Capacidade entre **9 kN e 16 kN**; melhor média com o
*D. asper*, **14,4 kN** contra 12,2 kN do *P. edulis*. 

O número que importa para este artigo está na revisão de literatura que eles fazem, citando Zhou e colegas (2022):
naquele ensaio, vigas com **ligações longitudinais** apresentaram **redução de 63,87% na capacidade máxima de carga
em flexão**. 

Sessenta e três por cento de perda. Vale delimitar o que é e o que não é: o estudo comparou uma **configuração de
viga conectada** com a **configuração íntegra correspondente**, num arranjo específico. Não é uma lei geral do bambu —
outras configurações estudadas pelos mesmos autores, inclusive vigas de dois colmos, tiveram resultado diferente. O
que o número estabelece é que, **naquele arranjo**, a ligação longitudinal foi o fator dominante — não que toda
ligação custa 63%.

Vale registrar também o que a mesma revisão descreve do lado positivo: arame de aço e reforços equivalentes, quando
bem usados, recuperam desempenho — e Ghavami (1995) relatou **aumento de 400% na carga última** de vigas de concreto
reforçadas com bambu, comparadas às mesmas vigas sem reforço. Ligação ruim destrói; ligação boa não é enfeite, é
estrutura.

### E há o caso brasileiro em que a conexão apareceu como patologia

A inspeção do Quiosque do Coco, no Parque do Tucumã, em Rio Branco-AC,
examinou uma cobertura em bambu nativo (*Guadua* sp.) com cerca de **11 anos** de construída e sem manutenção
programada. O resultado foi severo: **100% das 55 peças estruturais afetadas**, com fissuras em todas (98% do tipo
longa), fotodegradação em todas, fungos manchadores em todas — e, entre as causas apontadas, **2 peças com conexão
incorreta**.

Duas em 55 não é o problema dominante, e o texto não deve sugerir que seja: sol, chuva, umidade e falta de manutenção
fizeram muito mais estrago. Mas o item está na lista, registrado por inspeção técnica em obra real no território de
atuação do Takwara.
Conexão errada não é hipótese de laboratório: apareceu numa inspeção de campo, registrada em trabalho de congresso
com estudo de caso e inspeção visual e tátil — não em laudo pericial.

---

## 10. O nó do colmo: nem sempre ele ajuda


Existe uma confusão comum: "o nó do bambu é o reforço natural, então ligação perto do nó é melhor". A relação não é
automática, e um artigo brasileiro de 2024 mediu isso.

Seixas e colegas ensaiaram *Phyllostachys aurea* em flexão de quatro pontos, comparando modelos de cálculo com e sem
o efeito dos nós. A conclusão: **os nós influenciaram a resposta à flexão, tornando o colmo mais flexível** — e o
modelo que levava os nós em conta (a teoria de Timoshenko, ajustada com uma rigidez rotacional para cada nó) foi o
que descreveu melhor o comportamento real.

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
fibra, e a ligação é um dos pontos em que esse esforço é imposto.** Se a ligação rompe do mesmo modo, este artigo não
mediu — a hipótese segue aberta.

---

## 11. O que fazer, na prática, com o que está medido


Nada aqui é recomendação de projeto — este é material de divulgação. Mas o que a literatura permite afirmar:

**Qualifique a ligação, não só o colmo.** A norma pede qualificação por uma de duas vias. Se a ligação não está na
tabela, ainda há caminho sem ensaiar a ligação inteira: a via 10.3, quando o modo de falha é bem compreendido e a
capacidade do componente se correlaciona com segurança com o comportamento da ligação. O ensaio completo (10.2) entra
quando essa correlação não é confiável — é o caso do exemplo deste artigo, em que quatro mecanismos interagem ao mesmo
tempo.

**Conte as curvas antes de começar.** Com variação alta, amostra pequena não dá número conservador: dá
zero. É a informação mais acionável do artigo do Harries.

**Espere variação maior que a do material.** Se a compressão do colmo varia 0,27 e o escoamento da ligação varia
0,48, a variação da ligação é maior. **Por quê, o artigo não responde.** Ele lista as fontes possíveis de erro
sistemático — controle de ensaio, fabricação do corpo de prova, geometria, condições de contorno — e não elege a
culpada; registra ainda que o controle deste ensaio era muito bom, porque a máquina era servo-hidráulica. Quem
afirmar que a causa é "o encontro" está indo além da fonte.

**Normalize pela geometria antes de comparar estudos.** Diâmetro, espessura e vão mudam o número. Comparar ligações
sem normalizar é comparar medidas de coisas diferentes.

**Trate a ligação como item de projeto, com o mesmo peso da peça.** Uma configuração de viga com ligação longitudinal
registrou 63,87% de perda, **naquele arranjo específico**. Não é lei geral, mas basta para mostrar que a ligação pode
dominar o comportamento.

**Não conte com o nó como reforço automático.** A evidência disponível mostra efeito na rigidez global, não um
reforço simples de ligação.

---

## 12. O que continua faltando


**A amostra.** Ligação de bambu quase nunca tem amostra grande, e o próprio artigo que demonstra o método tem
**vinte ligações físicas**, e o limite é prático, não teórico. O artigo transforma essas vinte em quarenta
resultados porque ensaia cada uma nos dois sentidos — carregando para um lado e para o outro — e trata a curva de
ida e a de volta como dados separados. Confira na seção 5: são 20 ligações e 40 curvas. 

**Ligação padronizada com número publicado.** A maioria dos estudos, como o próprio Harries registra, é de conexão
patenteada ou pontual. Falta catálogo aberto de ligação com capacidade característica publicada, no formato em
que um projetista consiga usar. Hong e colegas (2019) chegam à mesma conclusão por outro caminho: **nenhuma solução reúne plenamente** capacidade,
rigidez, durabilidade, facilidade construtiva e baixo custo.

**Ensaio de ligação em espécie brasileira.** A coleção cobre ligação em Guadua colombiana, em bambu laminado, em
ripa. O que existe de ligação ensaiada sob norma brasileira, em espécie nativa, é bem menos.

**Durabilidade da ligação.** O artigo de arquitetura diz que a amarração solta e não dura; o de monitoramento fala da
necessidade de inspeção por degradação. O que falta é número: quanto uma ligação perde em dez anos, em ambiente
úmido. Bussinger (2024) reforça a mesma necessidade a partir de obra real: inspeção pós-obra é condição de durabilidade, e fissura apareceu em **todas** as varas de
**todos** os 16 casos.

**Preenchimento que não seja friável.** Adier e colegas (2023) apontam, como **principal lacuna da engenharia
contemporânea de bambu**, a falta de preenchimentos sustentáveis **não friáveis** nas conexões, para impedir o
cisalhamento nos nós. É a lacuna mais bem declarada da área, e diz o tamanho do problema. E o preço do preenchimento
convencional já está medido: massa pelo menos 2,5 vezes maior (Hong, 2019).

### Dois números da casa que não se encontram

Aqui vale um aviso fácil de ler errado.

Marçal (2018), ao comparar normas internacionais, registra — **como leitura dele, não como exigência universal** —
que a norma equatoriana pede verificação por estudo científico com **pelo menos 30 ensaios** para ligações
alternativas.

O número **9** que aparece neste artigo em outro lugar **não é um piso normativo**, e a comparação entre os dois
não deve ser feita como se fossem a mesma grandeza. Marçal fala de **exigência de norma**: quantos ensaios a norma
pede para aceitar uma ligação alternativa. O 9 sai de uma **conta estatística** — quantas curvas são
necessários para que o valor característico não caia a zero, dada uma variação medida. São perguntas de naturezas
diferentes:

- **30** responde "a norma aceita?". É requisito documental de uma jurisdição.
- **9** responde "a estatística fecha?". E, como a seção 5 mostra, depende da variação. Com a variação de 0,47
  medida aqui: **com 9 curvas ou menos, o valor característico é zero**; com **10 curvas**, ele deixa de ser zero.
  (Em ligações físicas, metade disso — porque cada ligação gera duas curvas.)
  Nove não é mínimo — é a última contagem em que o resultado ainda é inutilizável.

Nenhum dos dois substitui o outro. Um ensaio com 30 réplicas pode ter variação tão alta que o
característico continua inutilizável; e uma amostra estatisticamente suficiente não vale como qualificação
normativa onde a norma exige outra coisa. O que o leitor precisa saber é que **os dois números existem e medem coisas diferentes** — mas quem citar um sem o
outro vai confundir requisito com estatística.

**Um artigo ficou de fora, e vale dizer qual.**

Rivera-Segura, Moya, Gaitán-Álvarez e Granados-Gamboa (2024) publicaram, na Costa Rica, uma comparação das
propriedades físico-mecânicas do *Dendrocalamus asper* com duas variedades de *Guadua angustifolia*. Confirmei os dados
de publicação e li o resumo; **o texto completo não foi obtido**, porque a editora bloqueou o acesso.

O ponto que importa: **pelo resumo, ele não trata de conexões.** Compara propriedades do colmo — umidade, densidade,
flexão, tração, diâmetro, espessura de parede — de três materiais plantados no mesmo sítio. Então a lacuna não é de
ligação; é de propriedade do material. Fica registrada assim, como limitação, sem fingir que foi lida.

A referência completa está na lista de fontes, no fim.

---

## 13. As perguntas que valem para qualquer sistema novo


Existe hoje uma linha de pesquisa que propõe substituir o chumbamento cimentício e os conectores metálicos rígidos
por fixação flexível com poliuretano vegetal. Este texto não avalia essa proposta — nem a recomenda, nem a reprova.

O que se pode fazer, sem sair do que foi medido, é listar as perguntas que o caminho percorrido até aqui deixa em
aberto. Elas valem para qualquer sistema novo que chegue com a mesma pretensão, e é assim que devem ser lidas:

- **Por qual via a ligação seria qualificada?** Por componente (10.3), com correlação demonstrada, ou por ensaio
  completo (10.2), com campanha própria. Duas referências de naturezas diferentes orientam o tamanho: a conta
  estatística deste artigo indica que **abaixo de 10 curvas** o valor característico cai a zero com a
  variação medida; a leitura de Marçal da norma equatoriana pede **30 ensaios**.
- **Qual a variação esperada?** A ligação ensaiada neste artigo variou 0,47 — e é essa variação que decide o quanto a
  amostra precisa ser grande. Sem COV declarado, não há como dimensionar a campanha. A conta é feita em **curvas**, e
o artigo de referência tem 20 ligações físicas gerando 40 curvas.
- **Qual o modo de ruptura?** Flexível não significa seguro. O ensaio do Harries parou no limite de flecha e não viu
  ruptura; é a lacuna que qualquer sistema novo teria de preencher com observação do seu próprio modo de falha.
- **E o cisalhamento no nó?** A lacuna segue aberta: o que falta, segundo a literatura, é preenchimento sustentável
  **não friável**. Um sistema flexível que se apresente como preenchimento é julgado exatamente aí.
- **E a durabilidade?** Persiste para todos: quanto uma ligação perde em dez anos, em ambiente úmido. Uma proteção
  com ácido pirolenhoso é proposta como hipótese, e Silva (2011) registra resultado inconclusivo sobre ela — ensaio,
  não recomendação de fabricante.

Nenhuma dessas perguntas é objeção. São a régua que este artigo construiu, aplicada a qualquer sistema novo — e é
exatamente o padrão que essa linha de pesquisa declara: uma proposta, com desempenho ainda a verificar.

---

## Fontes

Para quem quiser ir ao original. Todas foram lidas integralmente, com o texto extraído página a página.

**Harries, K.; Rogers, C.; Brancaccio, M. (2022).** *Bamboo joint capacity determined by ISO 22156 'complete joint
testing' provisions.* Advances in Bamboo Science, v. 1, 100003. Universidade de Pittsburgh. — É o artigo que sustenta
a maior parte deste texto: classificação por mecanismo, os seis grupos, as dezessete combinações, o ensaio completo,
as tabelas de valores característicos e o efeito do tamanho de amostra.

**Barrile, V.; Genovese, E. (2024).** *Bamboo structures: innovative methods and applications for structural health
monitoring and dissemination.* Advances in Bamboo Science, v. 7, 100079. — Os cinco motivos de a ligação ser ponto
fraco e o valor de cisalhamento em torno de 12 MPa.

**Ding, D.; Xian, M. (2024).** *Research trends and design strategies for bamboo architecture.* Advances in Bamboo
Science, v. 8, 100094. — Os três modos tradicionais (encaixe, amarração, envolvimento) e o defeito de cada um.

**Zhao, J.-C.; Qiu, H.-X. (2023).** *Seismic performance assessment of a multi-story bamboo frame structure.*
Advances in Bamboo Science, v. 2, 100011. Universidade do Sudeste, Nanjing. — Bambu laminado colado, ligação de aço
em T, vinte sismos em três intensidades.

**Vasconcelos, P.Q.F.; Paciornik, S.; Silva, F.A. (2026).** *Mechanical behaviour of bamboo slat structural beams.*
Advances in Bamboo Science, v. 15, 100228. PUC-Rio. — Capacidades de 9 a 16 kN; cita a perda de 63,87% com ligações
longitudinais (Zhou e colegas, 2022)[^z] e o ganho de 400% com reforço (Ghavami, 1995)[^g].

**Seixas, M.; Cardoso, D.; Moreira, L.E.; Paciornik, S. (2024).** *Influence of elastic properties and nodes on the
flexural behaviour of bamboo culms.* Advances in Bamboo Science, v. 9, 100100. PUC-Rio e UFMG. — Nós tornam o colmo
mais flexível; ruptura frágil por cisalhamento e tração perpendicular à fibra.

**Hong, C.; Li, H.; Lorenzo, R.; Wu, G.; Corbi, I.; Corbi, O.; Xiong, Z.; Yang, D.; Zhang, H. (2019).** *Review on
connections for original bamboo structures.* Journal of Renewable Materials, v. 7, n. 8, p. 713–730. — Taxonomia das
conexões, os cinco indicadores quantitativos e a conclusão de que nenhuma solução reúne tudo.

**Bussinger, M. (2024).** *Sistemas estruturais contemporâneos em bambu* (dissertação, Universidade de São Paulo). —
16 obras paulistas de 2003 a 2023: conectores em uso, abandono do boca-de-peixe, fissuras e controle de qualidade.

**Adier, D. C. e colegas (2023).** *Properties, Treatment and Standardization of Bamboo: a systematic review.*
*Buildings*, v. 13, n. 10, 2449. DOI 10.3390/buildings13102449. — A lacuna do preenchimento sustentável não friável.

**Marçal, V. H. S. (2018).** *Comparação de normas internacionais para o bambu-colmo* (dissertação, Universidade de
Brasília). — A leitura de ~30 ensaios na norma equatoriana e a genealogia normativa (ISO, Colômbia, Peru, Equador,
Índia).

**Afonso (2025).** *Patologias em estrutura de cobertura em bambu: o Quiosque do Coco, Parque do Tucumã, Rio Branco-AC.*
Trabalho apresentado em congresso de engenharia civil. — As 55 peças estruturais, 11 anos de construção sem
manutenção programada e 2 conexões executadas incorretamente.

**Silva (2011).** *Tratamento pirolenhoso em bambu laminado colado* (dissertação, Universidade Estadual de Campinas).
— O ensaio que não demonstrou eficácia contra brocas em condição de campo.

**Normas citadas.** ABNT NBR 16828 — projeto de estruturas de bambu (2020); ABNT NBR 17043:2023 — classificação de
varas de bambu; ISO 22156:2021 — *Bamboo structures: structural design*; ISO 22157-1:2017 — determinação das
propriedades físicas e mecânicas do colmo; ISO 16670:2003 — ensaio cíclico de ligações com conector mecânico; ISO
12122-1:2014 e ISO 12122-5:2018 — determinação de valores característicos; ISO/TR 21141 — documento técnico sobre
determinação de propriedades de ligações.

[^g]: Ghavami, K. (1995). *Ultimate load behaviour of bamboo-reinforced lightweight concrete beams.* Cement and
    Concrete Composites, v. 17, n. 4. — O ganho de 400% na carga última.

[^z]: Zhou e colegas (2022) — estudo citado na revisão de Vasconcelos e colegas, não lido diretamente para este texto.
    O valor de 63,87% é reportado como está na revisão, e é assim que deve ser lido: número de segunda mão.

**Rivera-Segura, R.; Moya, R.; Gaitán-Álvarez, J.; Granados-Gamboa, M. (2024).** *Analysis of the physical-mechanical
properties of Dendrocalamus asper (Schult.) versus two Guadua angustifolia (Kunth) varieties, South and Caribe in the
Atlantic Region of Costa Rica.* Advances in Bamboo Science, v. 6, 100057. DOI 10.1016/j.bamboo.2024.100057. — Lido
apenas no resumo; texto completo bloqueado pela editora. Não fornece número a este artigo e, pelo resumo, não trata de
conexões.
