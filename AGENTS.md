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

## Publicação e Integridade Documental

- **Paridade entre Idiomas:** Toda publicação que possua versão em inglês (`-en.md`) deve obrigatoriamente manter paridade 1:1 de seções, anexos, tabelas e referências em relação à versão em português. Nunca publicar um resumo sintético na versão em português se a versão em inglês contiver a monografia expandida (ou vice-versa).
- **Integridade de Seções e Referências:** Todo manual, cartilha ou ensaio técnico deve conter sua Seção de Referências Bibliográficas e DOIs ao final absoluto do documento. É proibido inserir blocos bibliográficos no meio de capítulos ou permitir que interpolações automatizadas quebrem a numeração sequencial das seções.
- **Prevalência da Língua Portuguesa no Zenodo:** Em todos os depósitos do Zenodo, o arquivo principal em português (`01_...-pt-br.pdf` ou `01_...-pt-br.md`) deve ser posicionado em primeiro lugar e configurado explicitamente no parâmetro `preview_file` dos metadados para garantir que a pré-visualização padrão abra sempre em Português (PT-BR).

## Fluxo de Publicação

1. Executar inventário, verificação de paridade PT/EN e auditoria de seções/referências;
2. Executar `mkdocs build --strict`;
3. Revisar o diff e conteúdo privado;
4. Somente após autorização de Fabio: commit, push e deploy.
