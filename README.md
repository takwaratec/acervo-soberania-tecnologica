# Acervo Soberania Tecnológica

Infraestrutura pública de curadoria e conexão do conhecimento sobre materiais renováveis, construção, território, agroecologia e tecnologias regenerativas — construída por um pesquisador cidadão, com métodos explícitos, revisão progressiva e abertura à colaboração.

## Acesso público

**Site:** https://takwaratec.github.io/acervo-soberania-tecnologica/

O site é a experiência pública principal. Este repositório guarda a infraestrutura e o histórico da curadoria.

## Por que este repositório existe

A literatura relevante para tecnologias regenerativas encontra-se dispersa entre artigos, teses, relatórios, normas, documentos institucionais e experiências territoriais. Localizar uma fonte é relativamente fácil; compreender como ela se relaciona com outras fontes, quais métodos utilizou, quais limites apresenta e onde ainda existem lacunas exige um trabalho adicional de curadoria.

O Acervo existe para tornar esse trabalho cumulativo e público. Não se trata de guardar PDFs, mas de organizar relações e condições de uso do conhecimento.

## Utilidade

O Acervo permite:

- localizar fontes por tema, território, material e método;
- comparar achados e limitações;
- identificar lacunas de pesquisa;
- montar bibliografias fundamentadas;
- apoiar projetos, TCCs, dissertações e teses;
- estruturar agendas experimentais;
- relacionar tecnologias, políticas públicas e territórios;
- distinguir evidência científica, síntese curatorial e formulação autoral.

### Para quem

- estudantes e orientadores;
- pesquisadores;
- profissionais de arquitetura e engenharia;
- organizações comunitárias;
- agricultores e agentes agroflorestais;
- formuladores de políticas;
- instituições de ensino;
- parceiros interessados em P&D;
- pessoas que desejam contribuir com revisão e fontes.

### Como começar

1. Leia um [estado da arte](docs/analyses/reforma-agraria-agrofloresta/estado-da-arte.md).
2. Abra as fichas que sustentam a síntese.
3. Confira o estado documental de cada ficha.
4. Consulte a fonte original pelo DOI ou endpoint.
5. Verifique as lacunas indicadas.
6. Envie correções ou referências complementares.

## Eixos

O conteúdo público está em `docs/analyses/`:

- [Fundamentos](docs/analyses/fundamentos/index.md);
- [Bambu estrutural e tratamentos](docs/analyses/bambu-estrutural/index.md);
- [Poliuretano vegetal](docs/analyses/pu-vegetal/index.md);
- [Habitação social — percepção, APO e política](docs/analyses/percecao-social/index.md);
- [Bioeconomia amazônica e grandes obras](docs/analyses/bioeconomia-amazonica/index.md);
- [Reforma agrária e agrofloresta](docs/analyses/reforma-agraria-agrofloresta/index.md);
- [Perfis acadêmicos e técnicos](docs/analyses/respaldo-academico/index.md);
- [Visão autoral](docs/analyses/visao-do-autor/index.md).

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

## Estados e níveis de evidência

O acervo usa estados explícitos como `identificacao-pendente`, `extracao-preliminar`, `em-revisao-documental`, `homologado-documentalmente`, `visao-autoral`, `historico`, `protegido-privado` e `quarentena`.

Esses estados indicam maturidade documental. Não indicam TRL, eficácia aplicada, reconhecimento institucional ou consenso científico.

## Estrutura do repositório

```text
docs/
├── index.md            # página inicial
├── sobre.md
├── metodologia.md
└── analyses/           # fichas, estados da arte e análises por eixo
scripts/                # inventário e validação
INVENTARIO_ACERVO.md    # contagem reproduzível
GOVERNANCA_DOCUMENTAL.md
```

Fontes integrais, PDFs e materiais brutos permanecem fora do Git, em armazenamento privado e controlado.

## Como contribuir

Pesquisadores, estudantes, profissionais, autores e organizações podem contribuir indicando fontes, corrigindo metadados, revisando interpretações, propondo relações entre eixos ou apresentando documentos para triagem.

Nenhuma contribuição é publicada automaticamente: todas passam por identificação, rastreabilidade e revisão humana.

## Reproduzir e validar

```bash
# Inventário
python3 scripts/inventariar_acervo.py . \
  --markdown INVENTARIO_ACERVO.md \
  --json INVENTARIO_ACERVO.json

# Validação de front matter
python3 scripts/validate_frontmatter.py

# Build
mkdocs build --strict
```

## Direitos

Os textos curatoriais originais de Fabio Takwara podem receber licença própria quando isso estiver indicado. Artigos, livros, normas, imagens, marcas, citações e demais conteúdos de terceiros permanecem sob os direitos de seus titulares. O repositório não redistribui deliberadamente obras integrais protegidas.

## Governança e responsabilidade

**Idealização e curadoria:** Fabio Takwara — pesquisador cidadão e autodidata.

**Assistência documental:** ferramentas computacionais e agentes de IA, sempre sujeitas a revisão humana e sem autoria atribuída indevidamente às fontes analisadas.

O objetivo não é construir a maior coleção de documentos. É criar condições para que outras pessoas encontrem evidências, compreendam limites e formulem novas pesquisas sem precisar reiniciar todo o percurso bibliográfico. O êxito do Acervo será medido menos pelo número de fichas e mais pelas perguntas, projetos, revisões e colaborações que ele conseguir tornar possíveis.
