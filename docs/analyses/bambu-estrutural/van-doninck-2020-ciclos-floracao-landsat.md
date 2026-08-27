---
tipo_documental: ficha-cientifica
estado_documental: homologado-documentalmente
fonte_primaria: PDF integral conferido
identificador: https://doi.org/10.1016/j.jag.2020.102196
doi: 10.1016/j.jag.2020.102196
titulo: "Dating flowering cycles of Amazonian bamboo-dominated forests by supervised Landsat time series segmentation"
autores:
  - Jasper Van doninck
  - Jan Westerholm
  - Kalle Ruokolainen
  - Hanna Tuomisto
  - Risto Kalliola
instituicoes:
  - "Department of Geography and Geology, University of Turku, 20014 Turku, Finland"
  - "Åbo Akademi University, Faculty of Science and Engineering, Agora, Vattenborgsvägen 3-5, 20500 Åbo, Finland"
  - "Department of Biology, University of Turku, 20014 Turku, Finland"
periodico: "International Journal of Applied Earth Observation and Geoinformation"
ano: 2020
volume: 93
artigo: "102196"
licenca: "CC BY 4.0, conforme declarada na fonte"
data_revisao: "2026-08-27"
responsavel_curadoria: "Fabio Takwara"
idioma_fonte: EN
paginas_fonte: 11
---

# 1. Dados gerais

| Campo | Registro da fonte |
|---|---|
| Título | *Dating flowering cycles of Amazonian bamboo-dominated forests by supervised Landsat time series segmentation* |
| Autores | Jasper Van doninck; Jan Westerholm; Kalle Ruokolainen; Hanna Tuomisto; Risto Kalliola |
| Periódico/evento | *International Journal of Applied Earth Observation and Geoinformation* |
| Publicação | 2020, volume 93, artigo 102196 |
| DOI/identificador | 10.1016/j.jag.2020.102196 |
| Licença | CC BY 4.0, conforme declarada na fonte |
| Escopo | Florestas dominadas por bambu no sudoeste amazônico; segmentação supervisionada de séries temporais Landsat |


O artigo apresenta um método supervisionado de segmentação de séries temporais Landsat para identificar florestas dominadas por bambu e estimar o ano de início de eventos de mortalidade associados ao ciclo fenológico. A área estudada fica no sudoeste da Amazônia, em torno da região de tríplice fronteira entre Brasil, Peru e Bolívia. A fonte informa temperatura média anual de 24–26 °C, precipitação anual geralmente entre 1.400 e 2.200 mm e precipitação do mês mais seco entre 15 e 40 mm (p. 2).

Os autores são Jasper Van doninck, Jan Westerholm, Kalle Ruokolainen, Hanna Tuomisto e Risto Kalliola. As afiliações visíveis são a University of Turku e a Åbo Akademi University, na Finlândia. A fonte não atribui individualmente um país de nacionalidade aos autores; portanto, essa informação não é completada. O artigo foi publicado em 2020 no *International Journal of Applied Earth Observation and Geoinformation*, volume 93, artigo 102196. O DOI visível é 10.1016/j.jag.2020.102196. A licença declarada é CC BY 4.0.

O trabalho focaliza principalmente *Guadua sarcocarpa* e *Guadua weberbauerii*, tratadas conjuntamente como bambu em grande parte do texto. A fonte estima aproximadamente 160.000 km² de florestas dominadas por bambu no sudoeste amazônico (de Carvalho et al., 2013), enquanto o procedimento aplicado neste estudo identifica aproximadamente 118.000 km² com a banda SWIR1 (infravermelho de ondas curtas 1; p. 1 e p. 7). Esses números têm bases metodológicas diferentes e não devem ser tratados como uma comparação direta de estimativas equivalentes.

# 2. Estrutura e organização

O texto está organizado em introdução; descrição do local de estudo e dos dados; metodologia; resultados; discussão; conclusões; declaração de conflito de interesses; agradecimentos; dados suplementares; e referências. A metodologia é subdividida em composição anual das imagens Landsat, dados de calibração e validação, detecção e remoção de valores atípicos, ajuste não supervisionado, calibração do classificador, ajuste supervisionado e seleção da segmentação final, pós-processamento espacial e cálculo da razão sinal-ruído da perturbação.

A cadeia analítica tem duas etapas. Primeiro, uma segmentação não supervisionada procura mudanças compatíveis com a biologia do bambu. Depois, os resultados dessa etapa e a interpretação visual de uma área de calibração alimentam uma máquina de vetores de suporte, ou SVM (*Support Vector Machine*), usada na segmentação supervisionada. Os resultados por pixel são posteriormente combinados com regras espaciais e uma unidade mínima de mapeamento.

# 3. Problema e perguntas de pesquisa

O problema é mapear, em escala regional, florestas dominadas por bambu e o momento de sua mortalidade quando há poucos dados de campo, acesso difícil, heterogeneidade espacial, cobertura de nuvens e respostas espectrais sutis. Os autores perguntam, em termos operacionais:

- É possível diferenciar florestas dominadas por bambu de florestas sem domínio de bambu usando séries temporais Landsat?
- Qual banda infravermelha — NIR, SWIR1 ou SWIR2 — oferece melhor desempenho para essa diferenciação?
- O método consegue estimar o ano de mortalidade e detectar mais de um evento na série temporal?
- Qual duração do ciclo fenológico pode ser observada quando há dois eventos de mortalidade no mesmo pixel?
- As respostas espectrais das bandas infravermelhas ocorrem no mesmo momento ou apresentam defasagens?

# 4. Referencial teórico

O artigo parte da descrição de um ciclo de vida gregário e semélparo: indivíduos de uma população florescem e frutificam uma única vez e depois morrem. “Gregário” indica sincronização em populações espacialmente agregadas; “semélparo” indica uma reprodução seguida de morte do indivíduo. Para as espécies locais consideradas, o ciclo é apresentado como aproximadamente 28 anos (de Carvalho et al., 2013), com sincronização em grandes manchas.

O referencial combina ecologia do bambu, sensoriamento remoto e detecção de mudanças. Sensoriamento remoto é a observação da superfície terrestre por sensores instalados em satélites. As imagens Landsat TM e ETM+ têm resolução espacial de 30 m, isto é, cada pixel representa uma área nominal de aproximadamente 30 m por 30 m. O estudo utiliza as bandas NIR (infravermelho próximo, banda 4), SWIR1 (infravermelho de ondas curtas, banda 5) e SWIR2 (infravermelho de ondas curtas, banda 7).

A razão sinal-ruído da perturbação, DSNR (*disturbance signal-to-noise ratio*), compara a magnitude modelada da mudança com o erro residual do ajuste. Um valor maior representa, dentro desse indicador e dos dados analisados, um sinal de mudança mais separado do ruído; não é uma medida universal de qualidade de mapa nem de desempenho ecológico.

# 5. Metodologia

Foram usadas imagens Landsat 4/5 TM e Landsat 7 ETM+ adquiridas entre 1984 e 2018, com cobertura de nuvens reportada abaixo de 80%. As cenas foram convertidas para reflectância de superfície, corrigidas para efeitos combinados de topografia e geometria sol-sensor (Van doninck & Tuomisto, 2017a) e combinadas em composições anuais (Van doninck & Tuomisto, 2017b). Quando havia somente duas observações, foi usado o critério do maior NDVI; NDVI é o índice de vegetação por diferença normalizada. Cada pixel também recebeu a contagem de observações sem nuvens e sem sombras usadas na composição. Um filtro espacial substituiu cada pixel pela mediana de uma janela de 3 × 3 pixels.

A calibração foi feita em uma área de um grau por um grau. Polígonos de floresta dominada por bambu e de floresta sem domínio de bambu foram desenhados por interpretação visual de séries Landsat; o ano de mortalidade foi estimado visualmente. A validação usou imagens DigitalGlobe de resolução muito alta disponíveis no Google Earth, com áreas de 7.599 km² identificadas como dominadas por bambu e 12.141 km² como não dominadas por bambu (p. 3). A fonte alerta que o bambu pode ficar oculto pelo dossel arbóreo.

Valores atípicos globais foram removidos quando o afastamento da média excedia três desvios-padrão. Depois, valores atípicos locais foram avaliados em relação às observações vizinhas. Os parâmetros definidos manualmente foram limiar crítico τc = 2, constante de decaimento exponencial λ = 0,25 e janela temporal de três anos de cada lado. Pixels com mais de 25% de observações ausentes após filtragem não foram processados.

Na segmentação não supervisionada, o ajuste combinou períodos curtos aproximadamente constantes e períodos longos aproximadamente lineares. A significância foi avaliada com a estatística de Chow; valores de p maiores que 0,05 zeravam o escore inicial. Na etapa supervisionada, uma SVM com núcleo de função de base radial usou gamma = 0,5 e custo = 0,25. As variáveis preditoras foram o percentil 90 da série de reflectância (ρ90), a magnitude modelada da perturbação (Md) e o percentil do início da perturbação dentro da série (Pd). A probabilidade estimada pela SVM precisava ser de pelo menos 0,5 para manter o escore final.

O ano da perturbação primária foi restringido a 1987–2014. Um segundo evento podia ser identificado quando permanecia um escore não zero no período 1985–2016 e havia pelo menos 20 anos entre os eventos. O pós-processamento comparou cada pixel ambíguo com os quatro vizinhos mais próximos. A unidade mínima de mapeamento foi de 28 pixels conectados, aproximadamente 2,5 ha, com conectividade pelos quatro vizinhos.

# 6. Principais achados

A segmentação não supervisionada inicial classificou corretamente 57% dos 100.000 pixels amostrados para a banda SWIR1, considerando conjuntamente a classe de floresta e a margem de até dois anos para o ano de mortalidade. Nessa etapa, 67% dos pixels de referência não dominados por bambu foram classificados como bambu. Após a segmentação supervisionada, a proporção de pixels não dominados por bambu atribuídos erroneamente a mudança caiu para 6% na comparação apresentada na fonte (p. 7; Tabela 1 integral preservada na matriz privada).

Na validação com imagens de alta resolução, SWIR1 apresentou PCC de 87,78% e kappa de 0,7333. PCC é a porcentagem de pixels corretamente classificados; kappa é o coeficiente de concordância de Cohen, que considera a concordância esperada ao acaso. NIR apresentou PCC de 78,17% e kappa de 0,5036; SWIR2, PCC de 78,39% e kappa de 0,5082. A fonte informa erro de omissão de 27,62% para SWIR1, contra mais de 50% para NIR e SWIR2, e erro de comissão de 4,3% para SWIR1, 7,8% para NIR e 6,7% para SWIR2 (p. 7; Tabela 2 integral preservada na matriz privada).

A mediana do DSNR foi 0,75 para SWIR1, 0,61 para NIR e 0,55 para SWIR2. A magnitude mediana da perturbação foi −3,82% para NIR, −1,99% para SWIR1 e −0,81% para SWIR2. Assim, NIR teve mudança modelada maior em magnitude, mas também maior ruído relativo; SWIR1 teve o maior DSNR e a maior acurácia de classificação entre as três bandas.

A área identificada como floresta dominada por bambu com SWIR1 foi aproximadamente 118.000 km². A fonte compara esse resultado com uma estimativa anterior de aproximadamente 160.000 km², mas discute que erros de omissão, heterogeneidade dos polígonos e diferenças entre métodos podem explicar a diferença.

Os eventos detectados nas bandas SWIR tenderam a ocorrer depois dos eventos detectados na banda NIR. Entre pixels com dois eventos identificados nas três bandas, o intervalo entre eventos foi de 27–29 anos para a maioria, com 28 anos predominante na análise SWIR2. A série disponível permitia um intervalo teórico máximo de 29 anos e o mínimo foi fixado em 20 anos.

A duração modelada da perturbação foi maior que um ano para a maioria dos pixels. Para os pixels identificados como bambu nas três bandas, o evento foi modelado como tendo apenas um ano em 25% dos pixels com SWIR1, 43% com NIR e 39% com SWIR2. A fonte interpreta a resposta mais prolongada em SWIR como compatível com a permanência e posterior decomposição de material morto no dossel; essa explicação é apresentada como hipótese dos autores, não como medição direta do processo de decomposição.

As figuras mostram mapas de ano de perturbação e duração, distribuições de DSNR, diferenças entre anos estimados pelas bandas e distribuição do comprimento do ciclo. As imagens permitem interpretar padrões espaciais e tendências gerais, mas não substituem os valores tabulados nem autorizam leitura célula a célula dos gráficos.

# 7. Avaliação crítica

**Limitações e qualidade da evidência.** A referência de calibração foi obtida principalmente por interpretação visual das próprias séries Landsat, e não por uma base extensa de observações de campo. Os autores estimam que as datas atribuídas ficaram dentro de dois anos do evento real, mas reconhecem que a qualidade dessa digitalização não pôde ser avaliada diretamente. Os polígonos eram espacialmente mais grosseiros que a resolução de 30 m, podendo atribuir pixels ao polígono errado.

A cobertura de dados é irregular. Nuvens, aerossóis, falta de observações sem nuvens e lacunas históricas são particularmente importantes antes de 1999. A regra do método não permite mais de uma observação ausente durante o segmento da perturbação; áreas com duas ou mais observações anuais consecutivas ausentes podem ser classificadas como não bambu. O DSNR permanece baixo nas três bandas, indicando que o sinal é relativamente ruidoso.

**Comparação interna.** Dentro da mesma validação, SWIR1 teve melhor PCC, kappa e DSNR que NIR e SWIR2. Isso sustenta uma escolha operacional para o mapeamento apresentado, mas não prova superioridade universal de SWIR1 em outros sensores, biomas, períodos, resoluções ou configurações de treinamento.

**Escala.** O estudo combina pixels nominais de 30 m, polígonos de calibração e validação de milhares de quilômetros quadrados e uma unidade mínima de aproximadamente 2,5 ha. Esses níveis não são equivalentes: um polígono de validação pode conter áreas de densidade variável de bambu, e nem todo pixel em uma área chamada “dominada por bambu” terá dossel dominado por bambu.

**Transferência.** A transferência para outras regiões exige compatibilidade ambiental, espécies e ciclo fenológico, disponibilidade de séries Landsat, qualidade atmosférica, cobertura sem nuvens, parâmetros do classificador e referência local. Não é autorizado converter os resultados em recomendação de manejo, previsão de incêndio, garantia de acurácia em outra área, certificação ou desempenho estrutural.

**Variantes e cautelas.** A área de aproximadamente 118.000 km² e a estimativa de aproximadamente 160.000 km² aparecem em contextos metodológicos distintos. A diferença deve permanecer como comparação entre estimativas, não como erro corrigível. A fonte também indica que SWIR1 pode localizar melhor a presença de bambu, mas não necessariamente o ano exato de mortalidade, pois a resposta SWIR pode ser defasada.

# 8. Inserção no estado da arte

O artigo amplia trabalhos anteriores baseados em interpretação visual Landsat e em séries MODIS ao aplicar segmentação supervisionada à série Landsat de 1984–2018. Sua contribuição específica é combinar uma segmentação inicial baseada na ecologia do bambu com calibração local e SVM, permitindo mapear manchas em resolução nominal de 30 m e estimar anos de perturbação em uma área de difícil acesso.

A contribuição é metodológica e regional. O próprio artigo limita a interpretação pela escassez de referências de campo, pela qualidade variável das séries e pela resposta temporal diferente entre NIR, SWIR1 e SWIR2. A duração de aproximadamente 28 anos é consistente com o ciclo apresentado para *Guadua* no sudoeste amazônico dentro da janela temporal observada, mas não constitui uma regra universal para todos os bambus.

Para políticas públicas e sustentabilidade, o estudo pode contribuir como referência para monitoramento remoto e planejamento de levantamentos, desde que os mapas sejam tratados como produtos dependentes de validação local. Direitos territoriais, consentimento, governança de áreas protegidas e efeitos sociais não foram objeto de avaliação empírica no artigo. A agenda indicada pelos resultados inclui levantamentos de campo adicionais, observações repetidas de alta resolução e combinação criteriosa de informações de bandas distintas; essas são agendas de pesquisa, não resultados validados por este Acervo.

# 9. Relações

Relaciona-se a estudos de distribuição e ciclo de vida de *Guadua*, sensoriamento remoto de florestas amazônicas, detecção de mudanças em séries Landsat e normalização de reflectância (de Carvalho et al., 2013; Dalagnol et al., 2018; Van doninck & Tuomisto, 2017a, 2017b).

