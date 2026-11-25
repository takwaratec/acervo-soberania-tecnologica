# AGENTS.md — Acervo Soberania Tecnológica

## Leitura obrigatória

Antes de executar qualquer tarefa, leia nesta ordem:

1. `AGENTS_BASE.md` (governança comum — gerenciado centralmente);
2. `AGENTS_LOCAL.md` (regras específicas deste repositório);
3. `GOVERNANCA_VERSION.yaml` (versão instalada da governança);
4. `REPOSITORY_PROFILE.yaml` (perfil e módulos aplicáveis);
5. `GOVERNANCA_DOCUMENTAL.md` (taxonomia de estados documentais).

## Texto que declara conferência

Todo texto entregue por agente — ficha, artigo, resenha, blog, relatório — que afirme no método,
frontmatter ou rodapé ter conferido afirmações, fontes ou números **declara uma medição** e está
sujeito a `AGENTS_LOCAL.md` § "Conferência de afirmação". Sem registro auditável, a frase sai ou
passa a relatar o que de fato ocorreu. Quem abre a frente roda a conferência; o regente lê o registro
e aponta inconsistência — não roda por conta própria.

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
