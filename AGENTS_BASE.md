<!--
ARQUIVO GERENCIADO CENTRALMENTE

Origem: takwaratec/mentoria-takwara
Caminho de origem: governanca/base/AGENTS_BASE.md
Versão: 1.0.0
Commit de origem: <sha-do-commit-mestre>
Última sincronização: 2026-07-31

Não editar diretamente neste repositório.
Proponha alterações no repositório mestre.
-->

# AGENTS_BASE.md — Governança comum do ecossistema Takwara

## Leitura obrigatória

Antes de executar qualquer tarefa, leia nesta ordem:

1. `AGENTS.md` (índice de precedência);
2. `AGENTS_BASE.md` (este arquivo — regras comuns);
3. `AGENTS_LOCAL.md` (regras específicas deste repositório);
4. `GOVERNANCA_VERSION.yaml`;
5. `REPOSITORY_PROFILE.yaml`;
6. documentos específicos indicados por `AGENTS_LOCAL.md`.

## Precedência

Em caso de conflito, aplicar:

1. segurança, privacidade, direitos e integridade;
2. governança central;
3. governança local;
4. instruções específicas da tarefa;
5. convenções implícitas.

Regras locais podem ampliar controles, mas não podem reduzir:

- revisão humana;
- rastreabilidade;
- segurança;
- proteção de dados;
- direitos autorais;
- exigência de pull request;
- bloqueio de publicação automática.

## Princípios gerais

- Honestidade técnica: nunca inflar TRL nem apresentar como aplicado o que é laboratorial.
- Atribuição correta: cada autor com seu crédito; nada fabricado.
- Evidência pública: só artigos com DOI e literatura pública como evidência. Documentos internos nunca são citados como prova.
- Linguagem clara: sem termos metafóricos internos em textos públicos.
- Nunca fabricar citações, autoria, DOI, ISBN, ISSN ou resultados.
- Nunca criar fichas científicas sem autor e identificadores identificados.
- Nunca publicar fichas com seções vazias.
- Sempre alertar o usuário sobre dados faltantes antes de prosseguir.

## Autoridade dos agentes

Agentes podem:

- analisar;
- sugerir;
- criar arquivos candidatos;
- executar testes autorizados;
- abrir branches;
- abrir pull requests;
- produzir relatórios.

Agentes não podem, salvo autorização explícita:

- fazer merge em `main`;
- publicar;
- excluir fontes raras;
- alterar segredos;
- modificar proteção de branches;
- homologar conteúdo;
- assumir autoria ou licença;
- contornar checks.

## Revisão humana

Nenhum script pode homologar conteúdo automaticamente. A homologação documental é decisão humana.

## Fluxo Git

1. Sincronizar com a branch base.
2. Criar branch própria para cada mudança.
3. Executar testes e validações.
4. Abrir pull request.
5. Aguardar revisão humana.
6. Nunca fazer merge ou push direto em `main` sem autorização explícita.
