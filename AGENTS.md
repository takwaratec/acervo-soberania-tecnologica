# AGENTS.md — Acervo Soberania Tecnológica

## Identidade

Repositório de curadoria documental idealizado por Fabio Takwara. Reúne fichas científicas, resenhas, estados da arte e textos autorais sobre materiais renováveis, construção, habitação, território e bioeconomia.

## Regras obrigatórias

- Nunca fabricar citações, autoria, DOI, ISBN, ISSN ou resultados.
- Ficha científica ou acadêmica só ingressa com fonte integral e identidade documental verificável. DOI, ISBN e ISSN devem ser registrados quando existirem, mas sua ausência não impede o ingresso de tese, dissertação, trabalho de evento, relatório ou outro documento cuja autoria, título, instituição, data e proveniência possam ser confirmados no original.
- Laudos, certificados de ensaio e fichas de produto podem ingressar sem DOI/ISBN como tipos técnicos próprios, desde que tenham emissor, produto/amostra e identificador técnico verificável; nunca entram na contagem de fichas científicas.
- Toda ficha científica publicada deve possuir as oito seções do método adotado pelo Acervo.
- Não completar lacunas por inferência. A ausência de identificador persistente deve ser declarada, nunca preenchida por aproximação. Alertar Fabio quando faltar fonte, autoria ou metadado essencial.
- Documento interno não serve como evidência pública.
- Não inflar TRL nem apresentar proposta laboratorial como tecnologia aplicada.
- Visão autoral deve ser declarada e separada dos achados das fontes.
- Textos integrais protegidos, dados pessoais, contratos, normas e materiais brutos ficam fora de `docs/`.
- Não misturar documentos de projetos irmãos. O Acervo pode conter a referência científica, mas não atas, perfis de equipes, propostas ou operação de outras frentes.

## Estrutura pública

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
    └── visao-do-autor/
```

## Estados

Usar a taxonomia definida em `GOVERNANCA_DOCUMENTAL.md`. Nenhum script pode homologar conteúdo automaticamente.

## Publicação

1. executar inventário e auditoria;
2. executar `mkdocs build --strict`;
3. revisar o diff e conteúdo privado;
4. somente após autorização de Fabio: commit, push e deploy.
