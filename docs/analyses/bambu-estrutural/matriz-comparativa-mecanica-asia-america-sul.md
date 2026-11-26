---
tipo_documental: sintese-critica
estado_documental: em-revisao-documental
fonte_primaria: 12 PDFs integrais conferidos, com texto extraído página a página
titulo: "Matriz Comparativa — Propriedades Mecânicas de Bambu Lenhoso: Ásia × América do Sul"
data_revisao: 2026-11-18
responsavel_curadoria: Fabio Takwara
---

# Matriz Comparativa: Propriedades Mecânicas de Bambu Lenhoso — Ásia × América do Sul

## O que este documento responde

Este documento testa uma hipótese específica: **existe um comparativo mecânico entre continentes na literatura, e o que ele mostra sobre o bambu sul-americano?**

Ele não é um estado da arte e não substitui as fichas do eixo. É uma matriz de leitura construída sobre 12 PDFs integrais, com as três colunas que a comparação exige — **espécie estudada, país do experimento e origem nativa da espécie** — porque sem as três não se distingue "estudar uma nativa no Brasil" de "estudar uma asiática no Brasil".

Todo número aqui foi lido do PDF, com página indicada. Interpretações curatoriais estão marcadas como tal. Os limites estão declarados na seção 7.

---

## 1. Corpus efetivamente lido

Doze PDFs, todos com bytes verificados (`%PDF` válido, SHA-256 registrado) e texto extraído com marcador de página.

| # | Documento | Origem do arquivo | Páginas |
|---|---|---|---|
| 1 | Drury, Padfield, Russo, Swygart, Spalton, Froggatt & Mofidi (2023). *Assessment of the Compression Properties of Different Giant Bamboo Species for Sustainable Construction.* Sustainability 15(8):6472 | Repositório Brock University | 17 |
| 2 | Franck, Bletz-Mühldorfer, Bathon, Luippold, Mrzljak & Walther (2026). *Comparative evaluation of the mechanical properties of Phyllostachys edulis and Guadua angustifolia applying digital image correlation.* Discover Applied Sciences 8:1048 | Springer Nature | 21 |
| 3 | Lorenzo, Godina, Mimendi & Li (2020). *Determination of the physical and mechanical properties of moso, guadua and oldhamii bamboo assisted by robotic fabrication.* Journal of Wood Science 66:20 | Springer Nature | 11 |
| 4 | Panti, Cañete, Navarra, Rubinas, Garciano & López (2024). *Establishing the Characteristic Compressive Strength Parallel to Fiber of Four Local Philippine Bamboo Species.* Sustainability 16(9):3845 | MDPI | 21 |
| 5 | Scharfenberg et al. (2024). *The Flexural Strength of Three Bamboo Species from Brazil.* Forests 15(4):580 | MDPI | 15 |
| 6 | Rincon & Choque (2025). *Comparative mechanical characterization of Guadua angustifolia Kunth from Villavicencio and other regions.* Advances in Bamboo Science 10:100120 | Acervo (`_privado`, Vol10) | 8 |
| 7 | Rodríguez-Sotelo et al. (2023). *Propiedades físicas y mecánicas de Guadua lynnclarkiae, Guadua weberbaueri y Guadua superba en Ucayali, Perú.* Ciência Florestal 33(1):e68029 | Periódico UFSM | 23 |
| 8 | Rocha & Kikuti (2024). *Caracterização física e mecânica do bambu Guadua chacoensis segundo a ABNT NBR 16.828/2020.* Caderno Pedagógico 21(5) | Editora Studies | 27 |
| 9 | Poblete, Cuevas & Diaz-Vaz (2009). *Property characterization of Chusquea culeou, a bamboo growing in Chile.* Maderas 11(2):129–138 | SciELO Chile | 10 |
| 10 | Guiotoku, Pangrácio, Hansel & Lacerda (2024). *Physico-chemical properties of Brazilian native bamboo species.* Advances in Bamboo Science 7:100075 | Repositório Embrapa (Alice) | 7 |
| 11 | *Physical and mechanical properties of bamboo reconstituted* (2025). Advances in Bamboo Science, Vol10 | Acervo (`_privado`, Vol10) | — |
| 12 | *A feasibility study on bamboo–PLA composite lamina* (2025). Advances in Bamboo Science, Vol10 | Acervo (`_privado`, Vol10) | — |

**Corpus não obtido.** `Analysis of the physical-mechanical properties of Dendrocalamus asper versus two Guadua angustifolia` (Adv. Bamboo Sci., 2024, doi 10.1016/j.bamboo.2024.100057) não pôde ser baixado: o ScienceDirect bloqueou tanto a máquina local (HTTP 403) quanto o dispositivo móvel (referência `a5c6abb20c917df3`, código CPE00001). A ausência é declarada, não suprida por resumo.

---

## 2. Nota metodológica — por que os números brutos não somam

Três obstáculos tornam a soma ingênua de valores uma operação inválida. Estão registrados aqui porque condicionam toda a leitura da matriz.

**(a) Normas diferentes medem objetos diferentes.** O corpus usa pelo menos seis referenciais: ISO 22157:2019 (Drury, Panti, Lorenzo via JG/T 199), NTC 5525 colombiana (Rincon, Rodríguez), NTP peruanas (Rodríguez), ABNT NBR 16828 (Rocha), e procedimentos próprios baseados em ASTM (Poblete). A NBR 16828-2 e a ISO 22157 divergem no corpo de prova e na taxa de carregamento; comparar um valor de uma com o outro sem correção é comparar mensurações distintas.

**(b) A origem geográfica da amostra não é o país do experimento.** Um ensaio feito em Uberaba com *Phyllostachys aurea* produz um número brasileiro sobre uma planta chinesa. Esta coluna é a que falta na maioria das revisões de literatura, e é a que separa as duas coisas que a hipótese original confundia.

**(c) Média, valor característico e tensão admissível são grandezas distintas.** Drury reporta média (69,9 MPa para Moso); Lorenzo reporta valor característico (40 MPa para Moso); Rincon reporta tensão admissível conforme NSR-10 (4,35 MPa em tração para Villavicencio). A razão entre média e admissível chega a uma ordem de grandeza. Colocá-las na mesma tabela sem rótulo produz erro de leitura grave.

Por isso a matriz abaixo **separa o tipo de valor em coluna própria**.

---

## 3. Classificação de origem das espécies

A coluna "origem nativa" não foi inferida do país do estudo. Foi conferida contra *Plants of the World Online* (Kew), registro taxonômico de referência:

| Espécie | Origem nativa (Kew POWO) |
|---|---|
| *Phyllostachys edulis* (Moso) | China |
| *Phyllostachys bambusoides* (Madake) | China, Japão |
| *Phyllostachys aurea* | China (Fujian, Zhejiang) ao Vietnã |
| *Dendrocalamus asper* | Bangladesh a Taiwan e Malesia |
| *Dendrocalamus strictus* | Sul da Ásia |
| *Bambusa vulgaris* | Sul da Ásia (cultivada pantropicalmente) |
| *Bambusa blumeana* | Sudeste Asiático |
| *Bambusa tuldoides* | China (Guangdong, Guangxi) à Península Malaia |
| *Gigantochloa apus* | Java, Indonésia |
| *Gigantochloa atroviolacea* | Java, Indonésia |
| *Guadua angustifolia* | Noroeste da América do Sul (Colômbia, Equador, Venezuela) |
| *Guadua superba* | Amazônia ocidental (Peru, Brasil, Bolívia) |
| *Guadua weberbaueri* | Amazônia (Peru, Brasil) |
| *Guadua lynnclarkiae* | Amazônia peruana |
| *Guadua chacoensis* | Sul do Brasil, Argentina, Paraguai |
| *Chusquea culeou* | Chile, Argentina |
| *Merostachys skvortzovii* | Sul do Brasil |
| *Chusquea meyeriana* | Sul do Brasil |
| *Apoclada simplex* | Sul do Brasil |
| *Chusquea cf. gracilis* | Brasil |

As dezoito primeiras linhas são asiáticas ou sul-americanas segundo esse registro; a classificação sustenta toda a contagem da seção 5.

---

## 4. A matriz

### 4.1 Comparativos que colocam Ásia e América do Sul no mesmo ensaio

Quatro documentos. Em **todos**, a América do Sul comparece com **uma única espécie, sempre *Guadua angustifolia***.

| Estudo | País do experimento | Espécies asiáticas | Espécie sul-americana | Norma | Ensaio | Resultado |
|---|---|---|---|---|---|---|
| Drury et al. 2023 | Reino Unido / Canadá | Moso, Madake (China); Tali, Black Java (Indonésia) | *G. angustifolia* (Colômbia) | ISO 22157:2019 | Compressão paralela, colmo inteiro, n=6/espécie | fc,0: Madake **88,90**; Moso **69,88**; Guadua **60,73**; Tali **59,08**; Black Java **54,62** MPa (médias recalculadas das 30 linhas da Tabela 2, p.7) |
| Franck et al. 2026 | Alemanha | *P. edulis* (Moso) | *G. angustifolia* | Ensaio próprio + DIC (correlação de imagem digital) | Compressão paralela; tração transversal; MOE | fc,0: Moso **66,72 ± 0,54** (internó) / Guadua **66,35 ± 3,24** MPa; MOE: Moso **10,99** / Guadua **20,31** GPa |
| Lorenzo et al. 2020 | Reino Unido (fabricação robótica) | Moso; Oldhamii | *G. angustifolia* | JG/T 199-2007; característico por BS EN 1990 Anexo D | Compressão, cisalhamento, MOE em corpos pequenos | Valor característico fc,k: Oldhamii **50**; Moso **40**; Guadua **38** MPa. Média: Oldhamii 68; Guadua 58; Moso 54 MPa (Tabela 3) |
| Panti et al. 2024 | Filipinas | *B. vulgaris*, *D. asper*, *B. blumeana* | *G. angustifolia* | ISO 22157-1:2017; característico por ISO 12122-1:2014 | Compressão paralela, valor característico | fc,k: *B. blumeana* **46,63**; *B. vulgaris* **40,35**; *D. asper* **40,21**; Guadua **36,99** MPa |

**Fato medido.** Em quatro comparações independentes, realizadas em quatro países (Reino Unido, Alemanha, Reino Unido, Filipinas), a América do Sul é representada por *G. angustifolia* e por mais nenhuma espécie. A razão não é seletiva do corpus: é o desenho dos estudos.

### 4.2 Estudos de espécies nativas sul-americanas

| Estudo | País | Espécies nativas | Norma | Ensaio | Resultado (página) |
|---|---|---|---|---|---|
| Rincon & Choque 2025 | Colômbia (6 sítios) | *G. angustifolia* | NTC 5525 | 193 ensaios: compressão //, ⊥, cisalhamento, tração, flexão | Villavicencio (Tabela 7, p.7): compressão // média **100** MPa; ⊥ **80,2**; cisalhamento **93,3**; flexão **83,6**; tração **89,9**. Tensão admissível em compressão // variou por sítio e por seção do colmo |
| Rodríguez-Sotelo et al. 2023 | Peru (Ucayali) | *G. lynnclarkiae*, *G. weberbaueri*, *G. superba* | NTC 5525 + NTP 251 | Flexão estática, compressão // e ⊥, cisalhamento | MoR em flexão: *G. superba* **84,49** (basal), **73,97** (sobrebasa), **55,15** (cepa); *G. lynnclarkiae* **21,01** média; *G. weberbaueri* **13,77** média. Compressão //: **39,50** MPa média nas três (p.12–13) |
| Rocha & Kikuti 2024 | Brasil | *G. chacoensis* | ABNT NBR 16828 | Tração e compressão paralelas | Compressão **26,19 ± 5,37** MPa; tração **60,14 ± 18,47** MPa; densidade 0,70 g/cm³ (p.24–25) |
| Poblete et al. 2009 | Chile | *Chusquea culeou* | Procedimento próprio (referência ASTM) | Flexão, compressão //, cisalhamento, dureza Janka | Superior ao álamo e inferior ao *Pinus radiata* chileno em todas as propriedades (p.7–8) |
| Guiotoku et al. 2024 | Brasil (PR) | *M. skvortzovii*, *C. meyeriana*, *A. simplex*, *C. cf. gracilis* | — | **Apenas físico-química** (lignina, celulose, extrativos, elementos) | Sem qualquer ensaio mecânico: uma menção a "mechanical" em 7 páginas (p.1–7) |

**Fato medido.** O corpus tem dados mecânicos de **cinco** espécies nativas sul-americanas: *G. angustifolia*, *G. lynnclarkiae*, *G. weberbaueri*, *G. superba*, *G. chacoensis* e *C. culeou*. **Quatro das cinco são do gênero *Guadua*.** Fora de *Guadua*, existe exatamente uma espécie com caracterização mecânica no corpus: *Chusquea culeou*, de 2009.

### 4.3 O caso que inverte a hipótese

**Scharfenberg et al. 2024** (*Forests* 15:580) tem por objeto "três espécies de bambu do Brasil" e as declara, duas vezes, **nativas do Brasil**:

> "three bamboo species of the main genera naturally originating in Brazil: Bambusa tuldoides Munro, Dendrocalamus asper (Schult.) Backer, and Phyllostachys aurea Rivière & C. Rivière" (p.2)

> "Native to Brazil, these species were selected due to local availability and construction applicability in structural pa[nel production]" (p.2)

As três espécies **não são nativas do Brasil**. Segundo o Kew POWO: *B. tuldoides* é nativa da China (Guangdong, Guangxi) à Península Malaia; *D. asper*, de Bangladesh a Taiwan e Malesia; *P. aurea*, da China (Fujian, Zhejiang) ao Vietnã. O artigo não usa uma única vez, em 15 páginas, os termos "Asia", "Asian", "introduced", "exotic" ou "non-native".

Resultados do artigo (Tabela 2, flexão estática de 3 pontos): *P. aurea* atingiu a maior tensão última, **367,13 ± 49,25** MPa (grupo com nó, superfície interna); *D. asper*, **260,22 ± 22,34** MPa; *B. tuldoides*, **202,12 ± 26,70** MPa. MOE entre 7,61 e 22,82 GPa conforme espécie e grupo.

**Fato medido.** Um artigo publicado, revisado por pares e com licença CC BY, classifica três espécies asiáticas como nativas do Brasil, e é o único documento do corpus que trata "espécies brasileiras" em bloco.

---

## 5. Contagem — o que a matriz permite afirmar

| Pergunta | Resposta medida no corpus |
|---|---|
| Estudos com ensaio mecânico de nativa sul-americana | **4** (Rincon 2025; Rodríguez-Sotelo 2023; Rocha 2024; Poblete 2009) |
| Espécies nativas sul-americanas com dado mecânico | **6** (*G. angustifolia*, *G. lynnclarkiae*, *G. weberbaueri*, *G. superba*, *G. chacoensis*, *C. culeou*) |
| Dessas, do gênero *Guadua* | **5 de 6** |
| Estudos cross-continentais Ásia × América do Sul | **4** (Drury; Franck; Lorenzo; Panti) |
| Espécies sul-americanas nesses quatro estudos | **1** — *G. angustifolia*, em todos |
| Estudos com ensaio mecânico de gênero nativo não-*Guadua* | **1** (*Chusquea culeou*, 2009) |
| Estudos que declaram nativas brasileiras e usam espécies asiáticas | **1** (Scharfenberg 2024) |
| Espécies de *Merostachys*, *Apoclada*, *Eremocaulon*, *Glaziophyton* com dado mecânico | **0** |
| Documentos identificados como relevantes e **não obtidos** | **1** — *Dendrocalamus asper* vs duas *Guadua* (2024), ScienceDirect bloqueado (403 na máquina local; CPE00001 no dispositivo móvel). Declarado na seção 1 e no limite 2 da seção 7 |

---

## 6. Os três achados

### Achado 1 — A assimetria não é de quantidade, é de objeto

**Fato.** A América do Sul tem literatura mecânica de bambu. Não é escassa em número de estudos: há séries replicadas na Colômbia, no Peru e no Brasil.

**Fato.** Essa literatura é monotemática no objeto: cinco das seis espécies com dado mecânico são *Guadua*, e a sexta tem um único artigo de 2009.

**Interpretação curatorial.** O padrão não é "as Américas estudam mais o bambu asiático". É mais preciso e mais grave: **as Américas estudam o bambu asiático quando estudam o próprio continente, e quando estudam uma nativa, estudam quase sempre a mesma.** O gênero *Guadua* funciona como uma porta única — a espécie que "representa" o continente inteiro.

### Achado 2 — O comparativo entre continentes existe, mas é um monólogo com um convidado

**Fato.** Existem quatro comparações cross-continentais, e em todas a América do Sul comparece com *G. angustifolia* e mais nada.

**Interpretação curatorial.** Não existe, na literatura lida, um comparativo "Ásia × América do Sul". Existe um comparativo **Ásia + *Guadua***. A frase "achados da Ásia versus achados da América do Sul" descreve um estudo que ainda não foi feito — e essa é a lacuna, não um capítulo a resumir.

### Achado 3 — A variação dentro do gênero *Guadua* supera qualquer diferença entre continentes

**Fato.** Em flexão estática, sob a mesma norma e no mesmo laboratório, três espécies de *Guadua* foram ensaiadas
juntas (Rodríguez-Sotelo 2023, p.12–13): *G. superba* **84,49** MPa na base do colmo, *G. lynnclarkiae* **21,01** MPa
na média e *G. weberbaueri* **13,77** MPa na média. Comparando **as duas médias** — mesma região do colmo — a razão é
**1,53×**. Comparando os extremos do estudo (84,49 basal contra 13,77 média) a razão seria **6,1×**, mas aí se divide
base por média, o que não é comparação válida.

**Fato.** Na comparação mais controlada do corpus (mesmo protocolo ISO 22157, mesmo laboratório), Guadua e Moso diferem em **9 MPa** na média de compressão (60,73 contra 69,88; Drury 2023) e ficam **praticamente idênticos** no ensaio alemão (66,35 contra 66,72; Franck 2026).

**Fato.** Onde a diferença é grande e consistente é na **rigidez**: Guadua tem MOE de compressão **20,31** GPa contra **10,99** GPa do Moso — quase o dobro (Franck 2026, p.11).

**Interpretação curatorial.** A pergunta "bambu asiático é mais resistente que sul-americano?" é mal formada. A
variação intra-gênero (1,53× em comparação de mesma região; e 1,53× dentro de *G. superba* só mudando a posição do
colmo) já supera qualquer diferença intercontinental medida (1,15× — moso 69,88 contra *G. angustifolia* 60,73 na
mesma norma, Drury 2023). O eixo com sinal real não é resistência, é **rigidez e variabilidade**: Guadua é mais rígida, e o gênero tem dispersão interna que domina qualquer média continental.

---

## 7. O que este documento não conclui

1. **Não conclui exaustão.** Doze documentos não esgotam a literatura de mecânica de bambu. A busca foi por mecanismo de citação e repositório, não por varredura sistemática de bases indexadas (Scopus, Web of Science). Uma revisão sistemática exigiria protocolo de busca declarado e contagem de triagem.
2. **Não conclui sobre o que não leu.** O artigo *Dendrocalamus asper* × duas *Guadua* (2024) não foi obtido; sua ausência pode afetar a contagem de comparações cross-continentais em uma unidade.
3. **Não compara valores de normas diferentes como se fossem iguais.** Os números da seção 4.1 são apresentados com a norma de origem porque a conversão entre ISO 22157, NTC 5525 e NBR 16828 não é linear e não foi feita aqui.
4. **Não afirma que os autores de Scharfenberg 2024 erraram por má-fé.** O registro é factual: a classificação de origem no artigo diverge do Kew POWO. A explicação provável — uso de "nativo" no sentido de "cultivado e adaptado no país", corrente na literatura agronômica brasileira — não foi confirmada com os autores e fica como hipótese.
5. **Não sustenta a formulação ampla da hipótese original.** A afirmação de que a *Guadua* seria "o único bambu endêmico da América do Sul estudado no mundo inteiro" não se sustenta: *Chusquea culeou* tem caracterização mecânica publicada, e *Merostachys*, *Chusquea* e *Apoclada* têm caracterização físico-química publicada em 2024.
6. **Não é homologação.** Documento em revisão documental; não substitui ficha com fonte conferida nem passa por gate de homologação.

---

## 8. Consequência para a L21 do mapa de lacunas

A lacuna L21 ("Caracterização mecânica própria de espécies nativas amazônicas") **permanece ABERTA**. Este documento não a fecha, e o motivo é preciso: a L21 pede, textualmente, **campanha de ensaios mecânicos e físicos (NBR 16828-1/2)** das espécies nativas, com identificação botânica e procedência. As seis espécies aqui reunidas são **valores de literatura**, produzidos sob normas distintas (NTC 5525, NTP, NBR 16828, ISO 22157) e em campanhas isoladas — não constituem a campanha que a lacuna descreve. Reunir literatura não é executar campanha.

O que a matriz acrescenta à L21 é outra coisa: a redação atual nomeia *Guadua weberbaueri* como exemplo do que falta, e *G. weberbaueri* já tem ensaio mecânico publicado (Rodríguez-Sotelo 2023), ainda que sob normas peruana e colombiana, não brasileira. Ou seja, a L21 acerta o diagnóstico e erra o alvo: o que falta não é conhecimento da espécie, é **ensaio na norma brasileira** — e, para os gêneros fora de *Guadua*, é conhecimento de qualquer natureza.

O achado 3 muda a forma da lacuna: o mapa hoje trata o risco como geográfico; o dado indica que o risco é **intra-gênero** (1,53× dentro de *Guadua* na mesma região do colmo, contra 1,15× entre continentes). Dimensionar uma nativa com propriedades de outra espécie do mesmo gênero é extrapolação não verificada — e é o risco que o número sustenta.

A reescrita da L21 é matéria de documento próprio e será feita em separado, conforme decisão do soberano. Este documento entrega as três distinções que aquela reescrita precisa carregar: **cobertura de espécie** (o que existe além de *Guadua*), **cobertura normativa** (quem tem norma de projeto, não apenas ensaio) e **comparabilidade** (o que pode ser somado sem correção).

---

## 9. Custódia dos documentos

Os 12 PDFs estão sob custódia local em `_privado/fontes-documentais/comparativo-mecanica-2026-11/`, com SHA-256 por arquivo registrado em manifesto próprio. Cinco dos doze são de acesso aberto obtidos de repositórios institucionais (Brock, Embrapa, UFSM, SciELO Chile, Springer); três são cópias dos originais já custodiados do Vol10; três foram obtidos do editor sob CC BY 4.0; um foi fornecido pelo soberano a partir do dispositivo móvel.

Nenhum PDF de terceiro é publicado neste repositório. O que se publica é esta matriz, com locator de página.
