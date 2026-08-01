# AGENTS.md — Acervo Soberania Tecnológica

## Leitura obrigatória

Antes de executar qualquer tarefa, leia nesta ordem:

1. `AGENTS_BASE.md` (governança comum — gerenciado centralmente);
2. `AGENTS_LOCAL.md` (regras específicas deste repositório);
3. `GOVERNANCA_VERSION.yaml` (versão instalada da governança);
4. `REPOSITORY_PROFILE.yaml` (perfil e módulos aplicáveis);
5. `GOVERNANCA_DOCUMENTAL.md` (taxonomia de estados documentais).

## Precedência

Em caso de conflito, aplicar:

1. segurança, privacidade, direitos e integridade;
2. governança central;
3. governança local;
4. instruções específicas da tarefa;
5. convenções implícitas.

Regras locais podem ampliar controles, mas não podem reduzir: revisão humana, rastreabilidade, segurança, proteção de dados, direitos autorais, exigência de pull request ou bloqueio de publicação automática.

## Autoridade

Agentes podem: analisar, sugerir, criar arquivos candidatos, executar testes autorizados, abrir branches, abrir pull requests e produzir relatórios.

Agentes não podem, salvo autorização explícita: fazer merge em `main`, publicar, excluir fontes raras, alterar segredos, modificar proteção de branches, homologar conteúdo, assumir autoria ou licença, ou contornar checks.

## Arquivos gerenciados centralmente

Arquivos marcados com o cabeçalho "ARQUIVO GERENCIADO CENTRALMENTE" não devem ser alterados diretamente. Mudanças devem ser propostas no repositório mestre e propagadas por pull request:

- `AGENTS_BASE.md`
- `.github/workflows/governance-check.yml`
- `.github/pull_request_template.md`
