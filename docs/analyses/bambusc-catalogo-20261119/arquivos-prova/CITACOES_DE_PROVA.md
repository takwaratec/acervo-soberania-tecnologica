---
tipo_documental: instrumento-de-pesquisa
titulo: "Citações de prova — verificação sem confiança (com a exceção declarada)"
estado_documental: em-revisao-documental
data_revisao: 2026-11-19
responsavel_curadoria: Fabio Takwara
gaveta: bambusc-catalogo-20261119
fonte_primaria: "citacoes extraidas das obras do catalogo; cada trecho com pagina na fonte"
declaracao_ia: "produção assistida por inteligência artificial; conferência na fonte e responsabilidade de homologação são humanas"
---

# Citações de prova — verificação sem confiança (com a exceção declarada)

Cada linha traz o trecho **literal** com página e, ao lado, o **argumento** — o que a
citação sustenta e o que ela impede de concluir. O argumento vai em texto próprio, fora
das aspas, porque alongar a citação seria redistribuir mais obra do que se pode.

Medição: **27 de 27** citações conferem contra o parágrafo
e a página declarados. `round_trip_doi` diz se a obra é alcançável pela DOI a partir do
GitHub.

## Exceção declarada — 2 de 11 obras

- **`2020-jaramillo-lisboa-goularte-librelotto-pergola-bicicletario`** — a DOI 10.24133/ciencia.v22i1.1271 resolve para pagina de login da Revista CIENCIA, nao para o PDF. Consequência: o auditor confere a citacao contra a citacao e contra o METADADO (ISSN 1390-1117, v. 22, n. 1), nao contra o texto integral. e a UNICA das 11 obras com licenca declarada (CC BY).
- **`2019-reis-clerici-bambu-broto-comestivel`** — e livro, sem DOI; o registro e o ISBN 978-65-900237-0-4. Consequência: o auditor confere a citacao contra a citacao e contra o METADADO (ISBN, editora, ano), nao contra o texto integral. nenhuma citacao de numero desta obra entra no README; o uso e de contexto.

Nessas duas, o auditor confere a citação contra a citação e o metadado, **não** contra o
texto integral. A frase "nada pede confiança na minha palavra" vale com essa exceção.

## Citações

| obra | pág. | round-trip | citação literal | o que sustenta |
|---|---:|---|---|---|
| `2018-ostapiv-salamon-stahlschmidt-ferraz` | 1 | FECHA | *trução e ensaio de carregamento de duas maquetes* | Sustenta que o ensaio de carga ocorreu em DUAS MAQUETES, não no domo construído. Sem esta citação, os números seguintes seriam lidos como desempenho do domo de 4 m. |
| `2018-ostapiv-salamon-stahlschmidt-ferraz` | 1 | FECHA | *38 vezes o seu peso próprio* | É a origem do '38×'. Note que o sujeito é o domo de bambu em escala reduzida e a carga é o peso próprio do modelo — não uma comparação com resistência de material. |
| `2018-ostapiv-salamon-stahlschmidt-ferraz` | 1 | FECHA | *o domo de aço resistiu apenas 0,86* | É a origem do '0,86 do aço'. O valor foi redigido como 86% do peso próprio; fica claro que o denominador é peso próprio do modelo de aço, não tensão admissível. |
| `2018-ostapiv-salamon-stahlschmidt-ferraz` | 7 | FECHA | *carregamento hidráulico na estrutura* | Sustenta o método: carregamento hidráulico (água), não prensa instrumentada. Um ensaio desses mede deslocamento global, não tensão local. |
| `2018-ostapiv-salamon-stahlschmidt-ferraz` | 7 | FECHA | *no carregamento final o recipiente continha 1,6 litros de água* | Fecha o método: o carregamento final foi de 1,6 litros de água. Confirma que houve UM carregamento por maquete, sem série nem repetição. |
| `2018-ostapiv-salamon-stahlschmidt-ferraz` | 5 | FECHA | *Barras de bambu mossô feitas a partir de espetinhos de bambu obtidas do comércio* | Sustenta que as barras do modelo são espetinhos comerciais de bambu mossô, de 3 mm — material de mercado, não colmo estrutural selecionado. |
| `2018-ostapiv-salamon-stahlschmidt-ferraz` | 5 | FECHA | *Barras de aço baixo carbono, cobreado de 1mm de diâmetro* | Sustenta a assimetria do comparativo: o modelo de aço usa barra de 1 mm contra 3 mm do bambu. É o que impede tratar a razão entre cargas como propriedade de material. |
| `2017-carbonari-et-al-bambu-aco-vegetal` | 3 | FECHA | *Resistência a compressão (MPa)* | É o cabeçalho da Tabela 01: fixa a UNIDADE. Extração sem cabeçalho já fez número de tabela ser lido em outra unidade — por isso esta citação vem antes dos valores. |
| `2017-carbonari-et-al-bambu-aco-vegetal` | 3 | FECHA | *Dendrocalamus Asper 51,15±5,2% 49,84±4,5%* | Primeira linha da tabela, com as duas colunas (com nó / sem nó). Sustenta a leitura de que o desvio entre as colunas é pequeno — a diferença percentual é menor que o próprio erro. |
| `2017-carbonari-et-al-bambu-aco-vegetal` | 3 | FECHA | *Bambusa Tulda 75,18±7,0% 72,75±4,8%* | Maior valor da tabela (B. Tulda). Confirma o topo da faixa declarada no texto e desmonta a ideia de que haveria um único valor de resistência para bambu. |
| `2017-carbonari-et-al-bambu-aco-vegetal` | 3 | FECHA | *Arundinaria Amabilis 38,35±5,4% 38,20±6,7%* | Menor valor da tabela (A. Amabilis). Com a linha anterior, fecha a faixa 38–75 MPa — é variação de ESPÉCIE, não de método. |
| `2017-carbonari-et-al-bambu-aco-vegetal` | 4 | FECHA | *de 38 MPa até 75 MPa* | É a frase do artigo que resume a faixa. Serve para conferir que o texto e a tabela dizem a mesma coisa: síntese coerente com os dados, não arredondamento de conveniência. |
| `2017-carbonari-et-al-bambu-aco-vegetal` | 4 | FECHA | *a presença ou não do nó não afeta significati* | É a conclusão dos autores sobre o nó na COMPRESSÃO do colmo. Não pode ser transferida para aderência ou para laje mista — é outro objeto. |
| `2017-carbonari-et-al-bambu-aco-vegetal` | 3 | FECHA | *ISO/TC165 N314* | Sustenta a norma adotada por ausência de norma nacional. Sem ela, os valores não são comparáveis a ensaios feitos sob outra referência. |
| `2017-carbonari-et-al-bambu-aco-vegetal` | 4 | FECHA | *A Figura 4 apresenta um dos corpos de prova após realização do ensaio de compressão* | Contexto de amostragem e de realização do ensaio de compressão. A contagem de 9 CP por espécie (3 base, 3 meio, 3 topo) está no texto que acompanha esta figura. |
| `2017-acosta-carbonari-laje-mista-bambu-c` | 5 | FECHA | *suportando uma carga máxima de 30KN* | A segunda laje NÃO tem carga publicada: o texto traz 'até a carga de , a partir do qual'. Esta citação é a da laje 1 justamente para mostrar o que a fonte publica e o que omitiu. |
| `2017-acosta-carbonari-laje-mista-bambu-c` | 5 | FECHA | *até 22KN foi linear* | A segunda laje NÃO tem carga publicada: o texto traz 'até a carga de , a partir do qual'. Esta citação é a da laje 1 justamente para mostrar o que a fonte publica e o que omitiu. |
| `2017-acosta-carbonari-laje-mista-bambu-c` | 5 | FECHA | *suportando uma carga máxima de 30KN* | A segunda laje NÃO tem carga publicada: o texto traz 'até a carga de , a partir do qual'. Esta citação é a da laje 1 justamente para mostrar o que a fonte publica e o que omitiu. |
| `2018-geiss-damo-viabilidade-economica-es` | 6 | FECHA | *192,63% superior no valor* | Sustenta o percentual comparativo entre as duas técnicas de conexão. É diferença de ORÇAMENTO entre soluções, não economia contra outro sistema construtivo. |
| `2018-geiss-damo-viabilidade-economica-es` | 8 | FECHA | *R$4.592,73* | Sustenta o valor total da configuração com corda. Preço de 2018 em Chapecó/SC: não é preço corrente nem custo realizado. |
| `2016-sanchez-quintero-silveira-ligacao-e` | 1 | FECHA | *à tração acima dos 32 kN e à compressão acima de 19kN* | Sustenta o desempenho da ligação desenvolvida. É a única obra desta amostra que ensaia a CONEXÃO como objeto central — o que apoia o eixo 'conexão é o gargalo'. |
| `2016-sanchez-quintero-silveira-ligacao-e` | 1 | FECHA | *204,5% e 121,2%* | Sustenta a comparação dos autores contra a NSR-10. Percentual sobre tensão admitida da norma colombiana: não é fator de segurança medido. |
| `2016-sanchez-quintero-silveira-ligacao-e` | 1 | FECHA | *feitos na Universidade Nacional da* | Sustenta o desempenho da ligação desenvolvida. É a única obra desta amostra que ensaia a CONEXÃO como objeto central — o que apoia o eixo 'conexão é o gargalo'. |
| `2012-pereira-carrara-barata-valarelli-az` | 1 | FECHA | *conexões metálicas* | Sustenta que a obra executada no Brasil depende de conexão metálica — reforça o eixo de que a ligação concentra o risco de projeto. |
| `2020-jaramillo-lisboa-goularte-librelott` | 1 | NAO_FECHA | *Dendrocalamus asper and Phyllostachys aurea* | Sustenta quais espécies foram usadas na pérgola executada. Serve para não generalizar o resultado de montagem para outras espécies. |
| `2017-salamon-ostapiv-planificacao-colmos` | 1 | FECHA | *equipamento protótipo* | Sustenta que o processamento primário está em PROTÓTIPO. É a base da afirmação de que a cadeia industrial não existe — e o que a impede de ser lida como 'indústria instalada'. |
| `2017-carbonari-et-al-bambu-aco-vegetal` | 1 | FECHA | *aço vegetal* | Sustenta que 'aço vegetal' aparece como TÍTULO/retórica. Não há ensaio de aço no trabalho: a expressão não é resultado comparativo. |
