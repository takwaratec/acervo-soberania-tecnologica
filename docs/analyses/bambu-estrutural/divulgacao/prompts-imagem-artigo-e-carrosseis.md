---
tipo_documental: especificacao-tecnica-autoral
titulo: "Prompts de imagem — artigo de blog e três carrosséis"
autores: Fabio Takwara (curadoria); Hermes Agent (redação)
ano: 2026
estado_documental: em-revisao-documental
fonte_primaria: corpus de 12 PDFs integrais + coleção Advances in Bamboo Science (16 volumes, 240 artigos), custodiados em _privado/
data_revisao: 2026-11-18
nota_versao: "Padrão de front matter e de citação de fontes AINDA NÃO DEFINIDO para material de divulgação do MTCC; está sob escrutínio de auditoria externa. Proveniência declarada em texto corrido no corpo do documento. Não tratar este front matter como formato homologado."
responsavel_curadoria: Fabio Takwara
---

# Prompts de imagem — artigo de blog + 3 carrosséis

**Base visual:** 15 imagens extraídas dos PDFs originais (amostras em `amostras_originais/`).
Nenhum original é reproduzido — cada prompt descreve o **esquema**, não a figura. Os originais servem de referência de geometria e de escala.

## Referências extraídas dos originais

| Amostra | Arquivo | O que é | Serve para |
|---|---|---|---|
| R1 | `springer2026_moso_guadua_dic_05.jpg` | Diagrama de flexão a 4 pontos: colmo dourado horizontal, 2 apoios vermelhos embaixo, 2 cargas vermelhas em cima, cotas de 2600 / 1000 / 800 mm | Geometria de vão e flecha |
| R2 | `springer2026_moso_guadua_dic_06.jpg` | Foto de laboratório anotada: cilindro hidráulico, vigas de distribuição, cintas amarelas, LVDTs no meio do vão e nos apoios | Realismo de bancada |
| R3 | `drury2023_02.jpg` | Quatro colmos em pé, cada um com um nó central visível, diâmetros e paredes diferentes, códigos escritos à mão | Comparação de diâmetro × parede |
| R4 | `drury2023_05.jpg` | Quatro corpos de prova rompidos: fenda longitudinal severa, esmagamento no topo, trinca atravessando o nó | Modos de falha |
| R5 | `springer2026_moso_guadua_dic_04.jpg` | Esquema de pino bipartido + foto real do ensaio de tração perpendicular, luz azulada | Fenda e tração transversal |
| R6 | `springer2026_moso_guadua_dic_01.jpg` | Micrografia da parede do colmo: feixes vasculares pequenos e densos na face externa, grandes e espaçados na interna; barra de escala de 1 mm e ampliação de 0,2 mm | Gradiente da parede (base do carrossel 3) |

**Elementos a preservar em todos os prompts:** colmo oco com parede visível; nó como anel saliente; proporção 4:5 quando for carrossel; fundo limpo; paleta neutra com um único acento.

---

# PARTE 1 — Imagens do artigo de blog

Formato horizontal 16:9, exceto a hero.

## A0 · Hero do artigo

```
Fotografia editorial em ângulo baixo de um único colmo de bambu apoiado sobre dois blocos de concreto, num galpão de laboratório com luz lateral dura. O colmo está visivelmente vergado no meio, formando uma curva suave. Parede oca visível na extremidade cortada. Fundo desfocado em cinza concreto. Paleta: bambu bege-dourado, concreto cinza, uma faixa vermelha fina marcando o centro do vão. Sem texto, sem gente. Profundidade de campo curta, aparência de foto analógica, grão fino.
```

## A1 · A régua do MPa (comparação)

```
Ilustração vetorial limpa dividida ao meio. Esquerda: um selo postal quadrado de 1 cm² sobre fundo branco, com um peso de academia de 20 kg equilibrado em cima, sombra dura. Direita: o mesmo selo, agora com um carro popular inteiro apoiado sobre ele em escala absurda, rodas no ar. Números grandes em tipografia sem serifa, discretos: "6 kg → 0,6 MPa" à esquerda e "612 kg → 60 MPa" sobre o carro. Traço fino, paleta branco, cinza grafite e um único acento vermelho. Sem gradientes.
```

## A2 · Tensão não é carga (comparação — a figura central)

```
Comparação lado a lado de dois colmos de bambu em corte, apoiados em pé sobre base branca. Esquerda: colmo fino, diâmetro pequeno, parede fina, curvatura elegante, etiqueta "88 MPa". Direita: colmo grosso, diâmetro grande, parede espessa, etiqueta "60 MPa". Sobre cada colmo, uma pilha de blocos de concreto: poucos blocos no colmo fino, muitos no grosso. Um traço vermelho mostra a diferença de altura das pilhas com a anotação "6,7 t" e "10,7 t". Fotografia de produto, luz difusa, fundo cinza claro, profundidade real.
```

## A3 · Flecha (o termo que ninguém conhece)

```
Sequência de três quadros horizontais, mesma cena, mesma câmera. Uma tábua de madeira apoiada entre dois cavaletes, num galpão. Quadro 1: tábua reta, sem peso. Quadro 2: um homem adulto em pé no centro, tábua levemente curvada. Quadro 3: três homens no centro, tábua visivelmente arqueada, com uma cota vertical vermelha no centro indicando a descida, anotada "57 mm". A tábua tem textura de bambu laminado, não madeira comum. Luz natural lateral, fundo desfocado.
```

## A4 · Vão (o termo que ninguém conhece)

```
Fotografia aérea oblíqua de um pequeno riacho estreito numa paisagem rural brasileira. Sobre ele, uma passarela simples de bambu apoiada nas duas margens. Uma linha tracejada branca com setas nas duas pontas mede o vazio entre as margens, anotado "vão livre". Nenhuma pessoa. Verde contido, céu nublado, textura de terra vermelha. Estilo documental.
```

## A5 · Rigidez × resistência (comparação)

```
Dois gráficos de linha sobrepostos em um único plano, fundo branco. Eixo horizontal "flecha (mm)", eixo vertical "carga (kN)". Curva A: sobe rápido e para cedo, mais inclinada, rótulo "Guadua — rígida, rompe antes". Curva B: sobe devagar, alonga-se muito para a direita, rótulo "Moso — mole, verga mais". As duas cruzam uma linha tracejada horizontal rotulada "limite de flecha aceitável". Traço grosso, duas cores quentes distintas, tipografia técnica. Sem textura, sem sombra.
```

## A6 · O ponto cego — ligação

```
Maquete física em escala reduzida de uma treliça de bambu montada sobre bancada, parcialmente desmontada. Os colmos diagonais estão no lugar; o nó central está aberto, com parafusos soltos ao lado e uma peça faltando. Iluminação dura de cima, sombra marcada da treliça sobre a bancada. Paleta: bambu cru, metal escuro, fundo cinza. A peça faltando é o único elemento vermelho da imagem.
```

## A7 · Modos de falha (comparação, referência R4)

```
Quatro colmos curtos de bambu, em pé, lado a lado, sobre fundo branco infinito, cada um com um modo de falha diferente: (1) fenda longitudinal que abre uma tira inteira da parede; (2) esmagamento no topo com fibras dobradas; (3) trinca vertical atravessando a região do nó; (4) ruptura no nó com descolamento interno. Iluminação de estúdio, sombra suave, textura real de fibra, cor natural bege-dourada. Rótulos discretos abaixo de cada peça.
```

## A8 · Isométrico das três camadas

```
Ilustração isométrica limpa, fundo creme. Três blocos empilhados verticalmente, separados por espaço: base "MATERIAL" com um corpo de prova cilíndrico pequeno; meio "ELEMENTO" com um colmo longo como viga; topo "SISTEMA" com uma treliça de bambu montada. Os dois blocos de baixo estão preenchidos; o de cima está apenas em contorno tracejado, vazado, com uma linha "0 de 240". Traço fino, paleta marrom-bambu e cinza, um único acento vermelho no bloco vazio.
```

## A9 · Encerramento — três regras

```
Composição tipográfica sobre fundo creme texturizado de papel. Três linhas numeradas em tipografia grande, sem serifa, alinhadas à esquerda: "1. Compare carga, não tensão", "2. Use valor de projeto, não média", "3. A ligação vem antes do colmo". À direita, um único colmo em corte transversal ocupando metade da altura, parede visível. Tinta marrom-escura, sem imagens adicionais.
```

---

# PARTE 2 — Carrossel 1 · "Quanto aguenta um bambu?"

Formato **1080×1350 (4:5)**. Fundo consistente em todos os slides: creme quente, tipografia sem serifa grande, um acento vermelho.

## S1 · Capa
```
Slide vertical 4:5. Fundo creme texturizado. No centro, um colmo de bambu em corte transversal, visto de frente, preenchendo 60% da altura, parede oca bem visível, nó aparecendo na borda inferior. Sobre ele, tipografia preta grande em três linhas: "O que significa 60 MPa?". Abaixo, em corpo menor: "uma régua em três imagens". Sem outros elementos.
```

## S2 · MPa não é peso
```
Slide vertical 4:5, fundo creme. À esquerda, um quadrado branco de 1 cm² desenhado com régua visível ao lado. Sobre ele, um peso de academia de 10 kg em ilustração vetorial. À direita, o texto "1 MPa = 10 kg apertando 1 cm²". Seta fina ligando o peso ao quadrado. Paleta: creme, grafite, acento vermelho no peso.
```

## S3 · A régua visual
```
Slide vertical 4:5. Metade superior ocupada por um selo postal quadrado visto de cima, em escala grande; metade inferior, a mesma área com um carro popular em miniatura encaixado exatamente sobre o selo, como se coubesse. Tipografia sobre a imagem: "200 MPa = 2 toneladas por cm²". Fundo creme, imagem em preto e branco com o carro em vermelho.
```

## S4 · O choque
```
Slide vertical 4:5, fundo branco. Uma régua horizontal de 0 a 200, com três marcações destacadas: 40, 90 e 200. A faixa de 40 a 90 preenchida em bege-bambu com o rótulo "bambus estruturais"; a marca de 200 com um X vermelho e o rótulo "não existe bambu aqui". Tipografia grande, minimalista.
```

## S5 · Cinco espécies, mesma norma
```
Slide vertical 4:5. Cinco colmos recortados em pé, alinhados, cada um com diâmetro e tom de casca diferentes, sobre fundo creme. Abaixo de cada um, o nome da espécie em corpo pequeno e o valor em corpo grande. Os cinco valores formam uma diagonal descendente visível. Luz lateral única, sombra projetada para a direita.
```

## S6 · A virada (slide-chave)
```
Slide vertical 4:5, composição em dois blocos. Esquerda: colmo fino com rótulo "88,9 MPa" em tipografia grande e, abaixo, "rompe a 6,7 t" em corpo menor. Direita: colmo grosso com "60,7 MPa" e "rompe a 10,7 t". Um sinal de igual riscado ao meio entre os dois blocos, em vermelho. Fundo creme, fotografias de produto recortadas.
```

## S7 · A explicação
```
Slide vertical 4:5, diagrama. Dois cortes transversais de colmo lado a lado, vistos de frente, com a coroa circular da parede hachurada. Esquerda: coroa fina, área marcada "739 mm²". Direita: coroa espessa, "1.728 mm²". Abaixo de cada uma, uma barra de carga proporcional, curta e longa. Fórmula discreta no rodapé: "carga = tensão × área". Fundo branco, hachura cinza, barras em acento vermelho.
```

## S8 · O erro do dia
```
Slide vertical 4:5, tipografia dominante. Fundo creme escuro. Texto central em corpo grande entre aspas: "Escolhi a espécie mais resistente." Um carimbo ilustrado em vermelho, girado 12 graus, sobreposto no canto com a palavra "ERRO". Nada mais na imagem.
```

## S9 · Usar a média
```
Slide vertical 4:5, três barras horizontais empilhadas, decrescentes: 57,5 / 37,0 / 17,8 MPa, cada uma com o rótulo ao lado. A terceira barra marcada com uma linha tracejada "limite da norma". Fundo branco, barras em bege-bambu com a última em vermelho suave.
```

## S10 · O que isso significa
```
Slide vertical 4:5. Um colmo único, centralizado, em pé, com três faixas horizontais coloridas marcando alturas diferentes de uma pilha de carga ao seu lado: 10,1 t / 6,5 t / 3,1 t. A pilha mais alta tem um X vermelho; a mais baixa tem um visto. Fundo creme, blocos de concreto em cinza real.
```

## S11 · A terceira surpresa
```
Slide vertical 4:5, comparação de escala. Três colmos do mesmo gênero, lado a lado, com alturas visivelmente diferentes de "resistência" representadas por barras verticais ao lado de cada um: uma muito alta, uma média, uma quase nula. Rótulo superior: "mesmo gênero, mesmo laboratório". Rótulo inferior: "6,1 vezes de diferença". Fundo branco.
```

## S12 · Fechamento
```
Slide vertical 4:5 tipográfico. Fundo creme. Três regras numeradas em corpo médio, alinhadas à esquerda, com espaço generoso entre linhas. No rodapé, em corpo pequeno, a lista de fontes em uma única linha. Um fio horizontal fino separando regras e fontes.
```

---

# PARTE 3 — Carrossel 2 · "240 artigos, um buraco no meio"

## S1 · Capa
```
Slide vertical 4:5. Fundo branco. No centro, uma grade de 240 pequenos retângulos cinza-claro formando um bloco denso, tipo mosaico. Exatamente um dos retângulos está preenchido de vermelho. Tipografia grande sobre o mosaico: "240 artigos. Um buraco no meio." Sem outros elementos.
```

## S2 · Contexto
```
Slide vertical 4:5. Pilha de revistas científicas genéricas vistas de cima, em corte isométrico, 16 volumes com lombadas numeradas em corpo pequeno. Um deles destacado com fita vermelha. Fundo creme, ilustração vetorial com sombra suave.
```

## S3 · As três camadas
```
Slide vertical 4:5, isométrico. Três níveis empilhados com espaço entre eles: base sólida com um cilindro pequeno; meio sólido com um colmo longo; topo apenas em contorno tracejado, vazado. Rótulos à direita de cada nível. Fundo creme, traço fino.
```

## S4 · O que existe de bom
```
Slide vertical 4:5, três pequenas fotografias em grade vertical: um colmo em compressão na prensa, um colmo em flexão sobre apoios, uma viga laminada colada com veios visíveis. Cada foto com um rótulo curtíssimo e o número principal. Fundo branco, margens generosas.
```

## S5 · O que não existe
```
Slide vertical 4:5, tipografia dominante. Quatro linhas, cada uma com um rótulo à esquerda e um número grande à direita: "ligação 1/240", "treliça 0", "pórtico 0", "flambagem de colmo 0". Os três zeros em vermelho. Fundo creme, linhas separadoras finas.
```

## S6 · O único artigo de ligação
```
Slide vertical 4:5. Maquete de ligação boca-de-peixe entre dois colmos, montada sobre bancada, parafusos e chapa metálica visíveis. Ângulo três quartos, luz dura lateral. Rótulo superior discreto: "o único ensaio de ligação da coleção". Fundo cinza concreto.
```

## S7 · O resultado
```
Slide vertical 4:5, duas barras verticais lado a lado por parâmetro. Par 1: barra alta "469 Nm" e barra baixa "65 Nm". Par 2: barra alta "31.390" e barra quase igual "29.050". Uma seta curva vermelha descendo entre a primeira barra alta e a baixa. Fundo branco, tipografia técnica.
```

## S8 · A frase dos autores
```
Slide vertical 4:5 tipográfico. Fundo grafite escuro, texto claro. A citação em inglês em corpo médio, entre aspas, centralizada. Abaixo, separada por fio fino, a tradução em corpo menor. Uma barra vertical vermelha à esquerda da citação. Nada mais.
```

## S9 · O detalhe estatístico
```
Slide vertical 4:5, gráfico. Eixo horizontal "nº de corpos de prova (escala log)", eixo vertical "valor característico". Curva que sobe devagar e dispara à direita. Uma linha tracejada vertical em n=10, com o rótulo "abaixo disto, zero" em vermelho. Ponto destacado em n>2000 com "+55%". Fundo branco.
```

## S10 · Por que trava tudo
```
Slide vertical 4:5. Silhueta de uma treliça de bambu montada, com cada nó circulado em vermelho fino. O nó central ampliado em lupa, mostrando a ligação aberta. Rótulo: "cada círculo é uma ligação". Fundo creme, linha de desenho técnico.
```

## S11 · O que o Brasil cobre
```
Slide vertical 4:5. Mapa estilizado do Brasil em contorno fino, sem fronteiras internas. Um único ponto marcado no sul, com rótulo curto. Resto do mapa vazio. Fundo creme, ponto em vermelho, tipografia pequena. Sem texto sobre regiões não estudadas.
```

## S12 · Fechamento
```
Slide vertical 4:5 tipográfico. Fundo creme. Três itens numerados à esquerda, corpo médio. À direita, miniatura de uma treliça de bambu em traço fino, com apenas o nó central preenchido. Rodapé discreto com as fontes.
```

---

# PARTE 4 — Carrossel 3 · "Bambu não é madeira"

## S1 · Capa
```
Slide vertical 4:5. Macro de uma seção transversal de colmo de bambu, preenchendo todo o quadro, mostrando os feixes fibrosos como pontos escuros distribuídos na parede e o miolo oco. Tipografia branca sobreposta, canto inferior esquerdo: "Bambu não é madeira." Fundo escuro da própria foto, contraste alto.
```

## S2 · Anéis × feixes
```
Slide vertical 4:5, comparação. Esquerda: corte transversal de tronco de madeira com anéis concêntricos claros, desenho vetorial. Direita: corte de colmo com feixes fibrosos radiais e parede oca. Rótulos pequenos: "madeira — anéis" e "bambu — feixes". Fundo branco, traço uniforme, duas cores.
```

## S3 · A fenda é o padrão
```
Slide vertical 4:5. Um colmo curto em pé, com uma fenda longitudinal aberta que separa uma tira da parede, vista de frente. Fotografia de estúdio, fundo branco, luz lateral que mostra a profundidade da fenda. Rótulo numérico discreto sobre a imagem: "49 de 195". Sem mais texto.
```

## S4 · Três camadas de parede
```
Slide vertical 4:5, diagrama em corte. Anel circular representando a parede do colmo, dividido em três faixas concêntricas com hachuras diferentes: externa densa, média, interna porosa. Rótulos à direita com setas. Fundo branco, hachuras em três tons de bege.
```

## S5 · O ensaio da face (slide-chave)
```
Slide vertical 4:5, comparação em dois blocos. Bloco superior: lâmina de bambu com a face externa (casca) para cima, textura brilhante, sobre dois apoios, com carga no centro — rótulo "367 MPa". Bloco inferior: a mesma lâmina invertida, face interna porosa para cima, rótulo "202 MPa". Um "1,8×" grande em vermelho entre os blocos. Fundo creme.
```

## S6 · O nó é troca
```
Slide vertical 4:5, duas balanças simples estilo placa antiga. Balança esquerda pendendo para o lado "estático" com um peso; balança direita pendendo para "impacto". No centro, um nó de bambu em corte servindo de fulcro. Tipografia curta abaixo: "ganha rigidez, perde impacto". Fundo creme, ilustração vetorial.
```

## S7 · Química do colmo
```
Slide vertical 4:5, três barras horizontais com rótulos: lignina, celulose, silício. Cada barra com faixa de valor em vez de número único, mostrando o intervalo. Fundo branco, barras em bege e cinza, tipografia técnica pequena. Três minúsculas amostras de colmo no rodapé para ancorar.
```

## S8 · Silício muda com a idade
```
Slide vertical 4:5. Dois colmos lado a lado: à esquerda, jovem, mais claro, parede fina; à direita, adulto, mais escuro, parede espessa. Sob cada um, uma barra horizontal de silício: curta e longa. Rótulo: "1.643 → 4.333 mg/kg". Fundo creme, fotografia recortada.
```

## S9 · Química não dimensiona
```
Slide vertical 4:5 tipográfico. Fundo branco. Duas colunas: à esquerda, cabeçalho "a química responde" com três itens curtos; à direita, cabeçalho "a química não responde" com três itens curtos. Uma barra vertical vermelha separando as colunas. Tipografia sem serifa, corpo médio.
```

## S10 · O nó na ligação
```
Slide vertical 4:5. Detalhe aproximado de um nó de bambu em corte, mostrando o diafragma interno e a fibra mudando de direção. Um parafuso atravessando o nó, com linhas de tensão irradiando. Iluminação dura, fundo escuro. Rótulo discreto no canto.
```

## S11 · O que a cola enfrenta
```
Slide vertical 4:5, macro. Superfície de bambu vista muito de perto, textura lisa e brilhante com pontos de sílica visíveis, uma gota de adesivo no centro formando uma bolha que não molha a superfície. Fundo creme. Rótulo: "15,45 MPa de aderência". Fotografia macro real, não ilustração.
```

## S12 · Fechamento
```
Slide vertical 4:5 tipográfico. Fundo creme. Quatro itens numerados em corpo pequeno, alinhados à esquerda, com espaço generoso. Ao lado de cada item, um ícone linear mínimo correspondente. Rodapé discreto com fontes. Nenhuma fotografia.
```

---

# PARTE 5 — Notas de geração

**Consistência entre slides.** Fixe três decisões antes de gerar: (1) fundo — creme quente `#F4EFE6`; (2) tipografia — uma família sem serifa, dois pesos; (3) acento único — vermelho `#C0392B`. Slide que foge disso quebra a leitura em sequência.

**Comparações são o formato mais forte.** Todos os slides-chave dos três carrosséis são comparações de pares: fino × grosso (C1-S6), dentro × fora da norma (C1-S9), existe × não existe (C2-S5), face externa × interna (C3-S5). Se for gerar apenas uma imagem por carrossel, gere a comparação.

**O que não pedir ao gerador.** Não peça texto longo dentro da imagem — modelos erram acentuação e números. Gere a imagem sem texto e componha a tipografia depois. Os rótulos nos prompts acima são âncoras de composição, não instruções para o modelo desenhar letras.

**Originais como referência de proporção, não de cópia.** As amostras R1–R5 mostram geometria verdadeira (colmo de 80 mm, vão de 2.600 mm, nó a cada 30 cm). Use-as para calibrar proporção; o desenho é novo.

**Nenhuma imagem gerada entra no artigo sem revisão de escala.** Figura que exagera a resistência do bambu — ou que o desenha mais parecido com madeira — contradiz o texto e derruba a peça. A comparação tensão × carga (A2) é a que mais precisa de exatidão: se o colmo fino parecer do mesmo diâmetro que o grosso, a imagem ensina o contrário do texto.
