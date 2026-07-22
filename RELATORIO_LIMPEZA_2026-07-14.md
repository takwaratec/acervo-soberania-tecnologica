# Relatório de limpeza preparatória — 14/07/2026

## Objetivo

Preparar o Acervo Soberania Tecnológica para uma atualização pública coerente com suas regras de autoria, privacidade, fronteira entre projetos e integridade científica.

Nenhum arquivo foi apagado. Todo item retirado da árvore pública foi preservado em diretório ignorado pelo Git.

## Resultado público

- Markdown sob `docs/`: **19**
- Documentos sob `docs/analyses/`: **16**
- Fichas com oito seções e identificador conferido nesta revisão: **5**
- Índices e páginas curatoriais: **11**
- Duplicatas binárias públicas: **0**
- PDFs, DOCX, ODT ou fontes integrais sob `docs/`: **0**
- Build `mkdocs build --strict`: **aprovado**

As cinco fichas permanecem com estado `em-revisao-documental`; a limpeza não as promoveu automaticamente a homologadas.

## Conteúdo preservado fora da publicação

### Limpeza de escopo e infraestrutura

Foram preservados **927 arquivos** — aproximadamente **30,2 MB** — em `_quarentena/limpeza-repositorio-2026-07-14/`:

| Categoria | Arquivos | Motivo |
|---|---:|---|
| Ativos não utilizados | 704 | Imagens sem referência pública, identidade MQTF e grafismos de outra frente |
| Fora de escopo | 32 | ECOSALA, perfis de parceiros e cadastro comunitário de teste |
| Fundamentos em revisão | 15 | Texto original e análises com citações/metadados ainda não auditados |
| Infraestrutura obsoleta | 9 | Vercel, formulário de teste, instruções antigas e script inseguro |
| Legado público | 161 | Diretórios duplicados, documentos pessoais, prompts e levantamentos incompletos |
| Perfis em revisão | 6 | Perfis biográficos sem auditoria bibliográfica suficiente |

### Revisão científica

Foram movidos **147 documentos candidatos** para `_quarentena/revisao-cientifica-2026-07-14/`. O manifesto local registra caminho original, destino, classe da auditoria e motivo.

Esses documentos não foram rejeitados definitivamente. Eles retornarão por ordem cronológica quando houver:

1. fonte integral disponível;
2. autoria e identificador confirmados;
3. oito seções substantivas;
4. distinção entre achado da fonte e interpretação curatorial;
5. revisão de citações, direitos e links.

## Itens críticos identificados

- Cadastro comunitário contendo endereço `exemplo.com`, texto truncado e alegação de consentimento: mantido fora da publicação.
- Script de formulário que acrescentava dados não fornecidos pelo participante: retirado.
- `clean_unlisted.py` usado pelo Vercel removia arquivos durante o build: fluxo abandonado.
- Documentos fiscais e societários: preservados em `_privado/`.
- Página “sobre-o-autor” com 143 documentos de triagem e projetos: retirada da árvore pública.
- Conteúdo ECOSALA e perfis de parceiros: separado do Acervo conforme regra de fronteira entre repositórios.
- Identidade e ativos MQTF: retirados deste repositório.

## Estrutura pública resultante

```text
docs/
├── index.md
├── sobre.md
├── metodologia.md
├── assets/stylesheets/extra.css
└── analyses/
    ├── index.md
    ├── fundamentos/index.md
    ├── bambu-estrutural/        # quatro fichas verificadas + índice
    ├── bioeconomia-amazonica/  # uma ficha verificada + índice
    ├── pu-vegetal/              # índice de revisão
    ├── tecnologia-takwara/      # índice de revisão
    ├── percecao-social/         # índice de revisão
    ├── avaliacao-pos-ocupacao/  # índice de revisão
    ├── politica-habitacional/   # índice de revisão
    ├── grandes-obras-amazonia/  # índice de revisão
    └── visao-do-autor/          # índice de revisão
```

## Publicação

O repositório está preparado para revisão do diff, mas nenhum commit, push ou deploy foi executado. A grande quantidade de exclusões rastreadas é esperada: corresponde à retirada do Git de arquivos preservados localmente em quarentena.
