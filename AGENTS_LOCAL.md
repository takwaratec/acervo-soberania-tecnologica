# AGENTS_LOCAL.md — Acervo Soberania Tecnológica

## Identidade

Repositório de curadoria documental idealizado por Fabio Takwara. Reúne fichas científicas, resenhas, estados da arte e textos autorais sobre materiais renováveis, construção, habitação, território e bioeconomia.

## Objetivo

Infraestrutura pública de curadoria e conexão do conhecimento: transformar literatura científica, documentação técnica e memória de pesquisa em referências rastreáveis, comparáveis e utilizáveis na formulação de novos estudos, projetos, experimentos e políticas.

## Estrutura do repositório

```text
docs/
├── index.md
├── sobre.md
├── metodologia.md
├── assets/stylesheets/
└── analyses/
    ├── fundamentos/
    ├── bambu-estrutural/
    ├── pu-vegetal/
    ├── tecnologia-takwara/
    ├── percecao-social/
    ├── avaliacao-pos-ocupacao/
    ├── politica-habitacional/
    ├── bioeconomia-amazonica/
    ├── grandes-obras-amazonia/
    ├── reforma-agraria-agrofloresta/
    ├── respaldo-academico/
    └── visao-do-autor/
scripts/                    # inventário e validação
INVENTARIO_ACERVO.md        # contagem reproduzível
GOVERNANCA_DOCUMENTAL.md    # estados e taxonomia
```

## Regras locais obrigatórias

- Nunca fabricar citações, autoria, DOI, ISBN, ISSN ou resultados.
- Ficha científica ou acadêmica só ingressa com fonte integral e identidade documental verificável. DOI, ISBN e ISSN devem ser registrados quando existirem, mas sua ausência não impede o ingresso de tese, dissertação, trabalho de evento, relatório ou outro documento cuja autoria, título, instituição, data e proveniência possam ser confirmados no original.
- Laudos, certificados de ensaio e fichas de produto podem ingressar sem DOI/ISBN como tipos técnicos próprios, desde que tenham emissor, produto/amostra e identificador técnico verificável; nunca entram na contagem de fichas científicas.
- Toda ficha científica publicada deve possuir as oito seções do método Cavichiolli adotado pelo Acervo.
- Não completar lacunas por inferência. A ausência de identificador persistente deve ser declarada, nunca preenchida por aproximação. Alertar Fabio quando faltar fonte, autoria ou metadado essencial.
- Documento interno não serve como evidência pública.
- Não inflar TRL nem apresentar proposta laboratorial como tecnologia aplicada.
- Visão autoral deve ser declarada e separada dos achados das fontes.
- Textos integrais protegidos, dados pessoais, contratos, normas e materiais brutos ficam fora de `docs/`.
- Não misturar documentos de projetos irmãos. O Acervo pode conter a referência científica, mas não atas, perfis de equipes, propostas ou operação de outras frentes.

## Estados documentais

Usar a taxonomia definida em `GOVERNANCA_DOCUMENTAL.md`. Estados canônicos: `recebido`, `identificacao-pendente`, `protegido-privado`, `duplicata-fonte-auxiliar`, `extracao-preliminar`, `em-revisao-documental`, `homologado-documentalmente`, `visao-autoral`, `historico`, `quarentena`, `retirado-da-publicacao`. Nenhum script pode homologar conteúdo automaticamente.

## Publicação e integridade documental

- **Paridade entre idiomas:** toda publicação com versão em inglês (`-en.md`) deve manter paridade 1:1 de seções, anexos, tabelas e referências com a versão em português.
- **Integridade de seções e referências:** todo manual, cartilha ou ensaio técnico deve conter sua seção de referências bibliográficas e DOIs ao final absoluto do documento.
- **Prevalência da língua portuguesa no Zenodo:** o arquivo principal em português (`01_...-pt-br.pdf` ou `.md`) deve ser o primeiro e configurado em `preview_file`.

## Comandos obrigatórios

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

## Testes

- `mkdocs build --strict` deve terminar com exit 0 antes de qualquer commit.
- Nenhum PDF ou binário pode ser rastreado (`git ls-files | grep -Ei '\.pdf$'` deve ser vazio).
- Nenhum segredo pode aparecer no working tree.

## Dados e privacidade

- Fontes integrais, PDFs e materiais brutos ficam fora do Git, em armazenamento privado e controlado (ver `POLITICA_RETENCAO_CONVERSAO_DESCARTE_PDFS.md` — não versionada).
- Dados pessoais, contratos e documentos sensíveis permanecem privados.
- Documentos de governança interna (planos, políticas, controles de endpoint) não são versionados neste repositório.

## Regras específicas

- O repositório é público; o site é publicado via GitHub Pages por artifact (workflow `gh-pages.yml`).
- A branch `gh-pages` é legado do fluxo antigo e não deve ser usada para publicação.
- Mudanças de README, página inicial, navegação e deploy exigem aprovação de Fabio.
- Commit, push e deploy são autorizações independentes; nada é commitado sem "ok" explícito.

## Exceções autorizadas

- Nenhuma exceção permanente até o momento. Exceções pontuais devem ser registradas.

## Responsáveis

- **Idealização e curadoria:** Fabio Takwara (pesquisador cidadão).
- **Assistência documental:** agentes de IA, sempre sujeitos a revisão humana.
