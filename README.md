# Acervo Soberania Tecnológica

Curadoria documental de Fabio Takwara sobre bambu estrutural, poliuretano vegetal de mamona, habitação social, bioeconomia amazônica e tecnologias regenerativas.

**Site:** https://takwaratec.github.io/acervo-soberania-tecnologica/

## Finalidade

O Acervo organiza referências públicas e leituras críticas que apoiam as frentes de pesquisa cidadã do ecossistema Takwara. Ele documenta uma trajetória autodidata de cerca de quatro décadas com rastreabilidade, atribuição e distinção clara entre:

- achados publicados pelos autores das fontes;
- análise e síntese curatorial;
- formulações autorais de Fabio Takwara;
- documentos históricos ou institucionais;
- fontes privadas usadas apenas no trabalho interno.

O repositório é uma prova conceitual de capacidade de curadoria e articulação documental. Não substitui revisão por pares, replicação experimental, certificação, vínculo acadêmico formal ou validação de tecnologia em campo.

## Como o conteúdo é organizado

O número real do acervo é gerado por script e publicado no arquivo [`INVENTARIO_ACERVO.md`](INVENTARIO_ACERVO.md). A contagem separa arquivos Markdown, candidatos a análise, documentos com oito seções detectáveis e documentos com identificador público. Índices, perfis, estados da arte e textos institucionais não são somados como se fossem fichas científicas.

Os principais eixos públicos estão em `docs/analyses/`:

- bambu estrutural e tratamentos;
- poliuretano vegetal;
- tecnologia Takwara;
- habitação social e avaliação pós-ocupação;
- bioeconomia amazônica e grandes obras;
- fundamentos e perfis de referência.

As sínteses transversais são publicadas na série `docs/cadernos-revisao-ecologica/`. A coleção pública reúne, nesta etapa, cinco manuscritos em revisão: preservação socioecológica do bambu; transformação de componentes e equipamentos em capacidade produtiva territorial; rota do protótipo à conformidade normativa; passagem do componente conforme ao habitar, mediante diagnóstico, assistência técnica, adaptabilidade e avaliação pós-ocupação; e uso em cascata dos resíduos limpos por pirólise, com biochar, energia e coprodutos. As versões atuais ainda não possuem DOI.

## Método documental

As fichas usam uma adaptação do método Cavichiolli em oito seções:

1. dados gerais;
2. estrutura e organização;
3. problema e perguntas;
4. referencial;
5. metodologia;
6. achados;
7. avaliação crítica;
8. inserção no estado da arte.

Uma ficha só pode ser homologada documentalmente quando a fonte integral foi conferida, a autoria e o identificador público foram verificados quando existentes — ou a proveniência acadêmica/técnica foi confirmada quando não há DOI, ISBN ou ISSN —, e as oito seções têm conteúdo substantivo. Consulte [`GOVERNANCA_DOCUMENTAL.md`](GOVERNANCA_DOCUMENTAL.md) e [`docs/metodologia.md`](docs/metodologia.md).

## Estados documentais

O acervo usa estados explícitos como `identificacao-pendente`, `extracao-preliminar`, `em-revisao-documental`, `homologado-documentalmente`, `visao-autoral`, `historico`, `protegido-privado` e `quarentena`.

Esses estados indicam maturidade documental. Não indicam TRL, eficácia aplicada, reconhecimento institucional ou consenso científico.

## Reproduzir a contagem

```bash
python3 scripts/inventariar_acervo.py . \
  --markdown INVENTARIO_ACERVO.md \
  --json INVENTARIO_ACERVO.json
```

## Direitos e atribuição

Os textos curatoriais originais de Fabio Takwara podem receber licença própria quando isso estiver indicado. Artigos, livros, normas, imagens, marcas, citações e demais conteúdos de terceiros permanecem sob os direitos de seus titulares. O repositório não redistribui deliberadamente obras integrais protegidas.

## Responsabilidade

**Idealização e curadoria:** Fabio Takwara — pesquisador cidadão e autodidata.

**Assistência documental:** ferramentas computacionais e agentes de IA, sempre sujeitas a revisão humana e sem autoria atribuída indevidamente às fontes analisadas.
