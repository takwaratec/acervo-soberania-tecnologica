---
titulo: Thermal Performance of Thin-Shell Concrete Dome Structures
tipo_documental: ficha-academica
estado_documental: ficha-documental-publicada
fonte_primaria: Honors Thesis, Brigham Young University, 2023
identificador: https://scholarsarchive.byu.edu/studentpub_uht/316/
doi: null
source_url: https://scholarsarchive.byu.edu/studentpub_uht/316/
data_revisao: 2026-09-11
proveniencia: BYU ScholarsArchive; registro 316; fonte integral preservada; camada textual parcial
---

# Thermal Performance of Thin-Shell Concrete Dome Structures

## Estado e restrições documentais

A tese possui 51 páginas; a camada textual disponível cobre 47/51 páginas. As páginas 3, 5, 7 e 9 estão sem camada textual. Esta ficha preserva essa limitação. Não foi realizado OCR. O registro BYU confirma autora, título, coleção, data de publicação e identificador institucional. DOI: ausente na fonte.

## Referência primária

Velasco Vega, Daira Sofia. *Thermal Performance of Thin-Shell Concrete Dome Structures*. Undergraduate Honors Thesis, Brigham Young University, Department of Civil and Construction Engineering, 2023. Advisor: Kendrick Monroe Shepherd. BYU ScholarsArchive, Undergraduate Honors Theses, item 316. Publicação: 2023-07-03.
Fonte: https://scholarsarchive.byu.edu/studentpub_uht/316/

## Escopo da ficha

A tese avalia fluxo térmico em uma estrutura experimental de domo de casca fina de concreto isolada, com diferentes espessuras de cobertura de solo, comparando-a a um envelope residencial convencional de estrutura de madeira. O estudo trata de uma seção representativa e de condições do norte de Utah; não é estudo do Sistema Takwara.

## Metodologia

- Análise térmica transiente unidimensional por diferenças finitas; esquema implícito backward Euler no tempo e diferenças centrais no espaço (p. 21).
- Script Python customizado; passo temporal Δt = 10 s e resolução espacial Δx = 10 mils (0,01 in); parâmetros constantes por camada; convergência quando a diferença entre datas sucessivas ficava abaixo de 1e-4 (p. 21).
- Modelo: seção representativa de estrutura experimental isolada de aproximadamente 80 m² (cerca de 850 ft²), no campus da BYU em Provo, Utah; baseline: envelope típico isolado de estrutura de madeira da mesma localidade (pp. 14–16).
- Dados climáticos: estação Utah Climate Center em Lindon, Utah; médias de temperatura e radiação em intervalos de 10 minutos, dados de 2010–2022; estações definidas como inverno dezembro–fevereiro, primavera março–maio, verão junho–agosto e outono setembro–novembro (p. 15).
- Validação experimental: dados de temperatura interior do domo construído, agregados em médias de 10 minutos na superfície interior; comparação experimental detalhada para a primavera (p. 11; resultados p. 24 / Fig. 14 p. 33).

## Parâmetros do modelo

### Perfil do domo de concreto

| Camada | Espessura | Densidade | Condutividade térmica | Calor específico | Fonte |
|---|---:|---:|---:|---:|---|
| Concreto | 3 in / 0,0762 m | 2215 kg/m³ | 2,711 W·m⁻¹·K⁻¹ | 1000 J·kg⁻¹·K⁻¹ | Tabela 1, p. 16 |
| SPF | 3 in / 0,0762 m | 38,4 kg/m³ | 0,022 W·m⁻¹·K⁻¹ | 2100 J·kg⁻¹·K⁻¹ | Tabela 1, p. 16 |
| Membrana PVC | 0,02 in / 0,000508 m | 1300 kg/m³ | 0,23 W·m⁻¹·K⁻¹ | 970 J·kg⁻¹·K⁻¹ | Tabela 1, p. 16 |
| Solo argilo-arenoso | variável | 1400 kg/m³ | 2,45 W·m⁻¹·K⁻¹ | 1459 J·kg⁻¹·K⁻¹ | Tabela 1, p. 16 |

### Interpretação dos parâmetros materiais

A tabela evidencia o papel distinto de cada camada no envelope analisado. O concreto apresenta elevada densidade e capacidade térmica volumétrica, contribuindo principalmente para armazenamento de calor e amortecimento temporal. O SPF, por outro lado, possui condutividade térmica muito inferior à dos demais materiais e atua como a principal camada de resistência à condução térmica. A membrana de PVC é muito delgada e sua contribuição à resistência térmica global é pequena. O solo possui maior condutividade que o SPF, mas sua grande espessura e massa térmica permitem modificar fortemente a dinâmica de propagação do calor ao longo do tempo.

Essa interpretação refere-se ao sistema concreto–SPF–solo estudado na tese e não deve ser transferida diretamente ao Sistema Takwara.

### Perfil de madeira

O baseline contém placa de concreto reforçado com fibra, barreira de fibra de polietileno de alto desempenho, OSB, alternância entre isolamento de fibra de vidro e madeira de pinus, e drywall. Os valores completos permanecem na Tabela 2, p. 16; a tese observa que o valor real do baseline exigiria média ponderada entre montantes (aprox. 10%) e espaços isolados (aprox. 90%) (p. 23).

## Condições de contorno e variáveis

- Equação de condução transiente por camadas (Eq. 1, p. 15).
- Na superfície interior, condição convectiva com coeficiente hᵢ = 2,2 W·m⁻¹·K⁻¹ (Eq. 2, p. 19).
- Na superfície exterior, condição combinada de convecção e radiação; hₒ = 21,6 W·m⁻¹·K⁻¹ (Eq. 3, p. 19).
- Temperatura sol-air: temperatura exterior dependente do tempo mais parcela de radiação solar e absortividade, com superfície cinza e absortividade igual à emissividade (Eq. 4, p. 19).
- Temperatura interior prescrita como 20 °C, exceto no inverno, quando a análise usa 13 °C para coincidir com a média experimental (pp. 19, 29).
- Variáveis calculadas: temperatura, fluxo térmico interior qᵢ, fluxo médio, fluxo absoluto médio, atraso de fase Φ e fator de decremento DF (pp. 19–20).
- Radiação considerada: contribuição média de radiação solar de onda curta; radiação de onda longa não foi considerada (p. 15).

## Siglas, símbolos e unidades

- **SPF** — *Spray Polyurethane Foam*; espuma de poliuretano aplicada por aspersão.
- **PVC** — *Polyvinyl Chloride*; policloreto de vinila.
- **OSB** — *Oriented Strand Board*; painel estrutural de tiras orientadas de madeira.
- **Δt** — passo temporal utilizado no modelo numérico.
- **Δx** — resolução espacial da malha numérica.
- **hᵢ** — coeficiente convectivo na superfície interna.
- **hₒ** — coeficiente convectivo na superfície externa.
- **qᵢ** — fluxo térmico na superfície interna.
- **q̄ᵢ** — fluxo térmico médio na superfície interna.
- **TW** — *Wooden Studs*; componente correspondente aos montantes de madeira do envelope de referência.
- **TI** — *Insulated Space between the Studs*; espaço isolado entre os montantes do envelope de referência.
- **Φ (phi)** — atraso de fase térmica, em horas.
- **DF** — fator de decremento, relação entre a amplitude térmica transmitida através do envelope e a amplitude térmica de excitação.

Os valores de **q̄ᵢ** e de seu valor absoluto médio na Tabela 3 são expressos em W·m⁻²·°K⁻¹, conforme a unidade indicada pela própria tabela da fonte (p. 23). A ficha conserva a notação e a unidade tal como aparecem na tese.

## Resultados quantitativos

A Tabela 3 da fonte (p. 23) apresenta, para o domo de concreto com SPF externo, solo de 0–36 in, atraso Φ, DF, fluxo médio q̄ᵢ e fluxo absoluto médio. Valores abaixo são transcritos da tabela; não são estimativas.

| Estação | Solo | Φ (h) | DF | q̄ᵢ | q̄ᵢ absoluto | Localizador |
|---|---:|---:|---:|---:|---:|---|
| Inverno | 0 in | 2,05 | 0,00196 | -0,05 | 0,05 | Tabela 3, p. 23 |
| Inverno | 12 in | 7,96 | 0,00069 | -0,04 | 0,04 | Tabela 3, p. 23 |
| Inverno | 24 in | 15,3 | 0,00012 | -0,04 | 0,04 | Tabela 3, p. 23 |
| Primavera | 0 in | 1,92 | 0,00202 | -0,00 | 0,05 | Tabela 3, p. 23 |
| Primavera | 12 in | 8,13 | 0,00073 | -0,00 | 0,01 | Tabela 3, p. 23 |
| Primavera | 24 in | 15,1 | 0,00013 | -0,00 | 0,00 | Tabela 3, p. 23 |
| Verão | 0 in | 2,02 | 0,00200 | 0,07 | 0,07 | Tabela 3, p. 23 |
| Verão | 12 in | 8,21 | 0,00075 | 0,06 | 0,06 | Tabela 3, p. 23 |
| Verão | 24 in | 15,1 | 0,00013 | 0,06 | 0,06 | Tabela 3, p. 23 |
| Outono | 0 in | 2,14 | 0,00200 | -0,01 | 0,05 | Tabela 3, p. 23 |
| Outono | 12 in | 7,96 | 0,00072 | -0,01 | 0,01 | Tabela 3, p. 23 |
| Outono | 24 in | 15,1 | 0,00013 | -0,01 | 0,01 | Tabela 3, p. 23 |

A tabela completa também apresenta 3, 6 e 36 in e os componentes do baseline (montantes TW e espaço isolado TI); esses valores permanecem na fonte, Tabela 3, p. 23.

### Interpretação dos resultados da Tabela 3

Três tendências são particularmente claras no conjunto transcrito:

1. **Aumento do atraso de fase:** o aumento da espessura de solo desloca progressivamente no tempo a resposta térmica do interior. Nos casos apresentados, Φ passa de aproximadamente 2 horas sem solo para cerca de 15 horas com 24 in de cobertura.
2. **Redução do fator de decremento:** o DF diminui de valores próximos de 0,002 sem solo para cerca de 0,00013 com 24 in, indicando forte atenuação da amplitude térmica transmitida pelo envelope modelado.
3. **Redução do fluxo térmico absoluto em parte dos cenários:** primavera e outono mostram redução expressiva do fluxo absoluto médio com o aumento da cobertura de solo. No verão e no inverno, a variação do fluxo médio é menor, mostrando que atraso de fase, amortecimento e magnitude média do fluxo são métricas distintas e não devem ser interpretadas como equivalentes.

Em conjunto, os resultados indicam que a cobertura de solo atua principalmente sobre a dinâmica temporal da transferência de calor — aumentando o atraso e reduzindo a amplitude — enquanto o SPF externo fornece a maior resistência térmica do envelope.

## Resultados por cenário

- **Efeito da cobertura de solo:** nos quatro cenários sazonais, o aumento da espessura de solo reduz DF e o fluxo absoluto médio e aumenta o atraso Φ (Tabela 3, p. 23).
- **SPF externo versus interno:** a fonte relata que inverter as camadas, colocando SPF no interior do concreto, produz fluxos de magnitude comparável à estrutura tradicional (Figs. 12–13, pp. 31–32; discussão p. 24).
- **Configuração com SPF externo:** a fonte relata fluxo térmico pelo menos uma ordem de grandeza menor que o da estrutura tradicional, atribuindo o resultado principalmente à posição externa do SPF (p. 24).
- **Solo de 18 in:** a discussão indica que um atraso de aproximadamente 12 horas pode ser alcançado com 460 mm (18 in) de solo (p. 24). Essa afirmação é específica do modelo e não deve ser transferida para outros materiais ou climas.
- **Validação experimental:** a temperatura interior experimental da primavera acompanha bem o cálculo; o atraso experimental de inverno é aproximadamente 2,5 horas e é comparado ao caso computacional sem solo (p. 24; Fig. 14, p. 33).
- **Conclusão da autora:** a tese relata que o domo de concreto com SPF externo e solo reduz fluxo e flutuação térmica em comparação com o baseline modelado (Conclusão, p. 34).

## Limitações e incertezas

- O modelo é unidimensional, embora o fluxo real ocorra em três dimensões (p. 29).
- Emissividade e radiação da membrana não foram medidas diretamente; foram adotados valores de literatura; radiação de onda longa não foi incluída (p. 29).
- Propriedades dos materiais foram tratadas como constantes por camada, embora temperatura e umidade possam alterar propriedades (p. 29).
- A geometria curva não foi incorporada ao modelo térmico (p. 29).
- Temperatura interior prescrita implica uso implícito de aquecimento/refrigeração; o caso de inverno foi ajustado para 13 °C com base nos dados experimentais (p. 29).
- A validação experimental apresentada cobre um mês de primavera; não demonstra validação anual completa (p. 11; p. 24).
- O estudo é de uma seção representativa/estrutura experimental em Provo, Utah; não é evidência de desempenho em clima brasileiro ou em habitação genérica.
- A tese não avalia bambu, PU vegetal, interface colmo–espuma, fogo, vento, sismo, durabilidade de longo prazo, custo ou ciclo de vida do Sistema Takwara.
- A camada textual é parcial: 47/51 páginas; quatro páginas sem camada textual. OCR automático não foi realizado.

## Transferibilidade

A tese oferece evidência relacionada para o princípio de modelar massa térmica, isolamento externo, cobertura de solo, atraso de fase e fator de decremento em uma casca de concreto. Não oferece validação direta de bambu, PU vegetal, cavidade acima do solo ou montagem geodésica Takwara. Qualquer uso comparativo deve ser rotulado como hipótese de projeto e exige ensaios específicos.

## Relação com a publicação posterior

Esta tese de 2023 é um trabalho precursor relacionado ao artigo posterior de Velasco Vega et al. (2024). Os dois documentos possuem escopos diferentes: a tese cobre um domo individual com cobertura de solo e um baseline de madeira; não deve receber resultados exclusivos da publicação posterior, como comparadores adicionais ou análise de ciclo de vida. A publicação posterior permanece separada e não foi tratada como fonte integral desta ficha.

## Relação com o artigo Zenodo

Esta ficha integra a base documental utilizada no artigo “Domos, bambu e poliuretano vegetal: genealogia tecnológica, evidências e agenda brasileira para sistemas habitacionais resilientes”. Relação: contextualiza e sustenta parcialmente a discussão térmica. DOI do artigo: ainda não atribuído.

## Proveniência

Esta ficha é uma síntese crítica derivada e não substitui a consulta à tese original.
