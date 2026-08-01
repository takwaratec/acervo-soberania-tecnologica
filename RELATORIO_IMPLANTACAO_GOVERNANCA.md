# RELATÓRIO DE IMPLANTAÇÃO DA GOVERNANÇA — Acervo Soberania Tecnológica

**Data:** 2026-07-31
**Repositório:** takwaratec/acervo-soberania-tecnologica
**Branch de implantação:** `governance/bootstrap-acervo`
**Origem da governança:** takwaratec/mentoria-takwara (versão 1.0.0)
**Responsável:** Fabio Takwara

---

## 1. Perfil

- **Perfis aplicados:** documental, pesquisa, site
- **Módulos obrigatórios:** base, seguranca, documental, publicacao
- **Módulos opcionais:** automacao

## 2. Regras existentes (antes da implantação)

| Arquivo | Conteúdo | Destino |
|---|---|---|
| `AGENTS.md` (56 linhas) | Identidade, regras obrigatórias, estrutura, estados, publicação/integridade, fluxo | Migrado para `AGENTS_LOCAL.md` (regras locais) |
| `GOVERNANCA_DOCUMENTAL.md` | Taxonomia de estados, tipos documentais, homologação | Mantido (referenciado por AGENTS_LOCAL) |
| `.github/workflows/gh-pages.yml` | Deploy GitHub Pages por artifact | Mantido (workflow de produção) |
| Documentos de governança interna (BIBLIOGRAFIA_COMPLEMENTAR, OPERACAO_BAMBU, CONTROLE_ENDPOINTS, POLITICA_RETENCAO, PLANOS) | Instrumentos de construção/sanitização | **Não versionados** (decisão Fabio); cópia em ~/Documents/backups-acervo/2026-07-31/documentos-governanca/ |

## 3. Arquivos criados

| Arquivo | Função | Gerenciado centralmente |
|---|---|---|
| `AGENTS.md` | Índice de precedência e porta de entrada | Não (local, recomposição) |
| `AGENTS_BASE.md` | Regras comuns do ecossistema | **Sim** |
| `AGENTS_LOCAL.md` | Regras específicas do acervo | Não |
| `GOVERNANCA_VERSION.yaml` | Versão instalada, origem, sincronização | Sim (informacional) |
| `REPOSITORY_PROFILE.yaml` | Perfis, módulos, comandos de validação | Não (local) |
| `.github/CODEOWNERS` | Revisores por caminho | Sim (padrão) |
| `.github/pull_request_template.md` | Template de PR | **Sim** |
| `.github/workflows/governance-check.yml` | Checks: inventário, front matter, build, PDFs, segredos | **Sim** |

## 4. Regras preservadas

Todas as 56 linhas do AGENTS.md original foram migradas para AGENTS_LOCAL.md, incluindo:

- regras de não fabricação (citações, autoria, DOI, ISBN, ISSN);
- ingresso de fichas com fonte integral;
- laudos/certificados como tipos técnicos próprios;
- oito seções do método Cavichiolli;
- não completar lacunas por inferência;
- documento interno não é evidência pública;
- não inflar TRL;
- separação visão autoral × achados;
- textos integrais fora de `docs/`;
- fronteira entre projetos irmãos;
- paridade PT/EN;
- integridade de seções e referências;
- prevalência do PT-BR no Zenodo;
- fluxo de publicação com aprovação de Fabio.

## 5. Regras migradas para a governança comum

- Princípios gerais (honestidade técnica, atribuição, evidência pública);
- autoridade dos agentes;
- revisão humana obrigatória;
- fluxo git por pull request.

## 6. Conflitos

Nenhum conflito identificado. O AGENTS.md original não contradizia a governança mestre; apenas não a declarava explicitamente.

## 7. Exceções

- **Documentos de governança interna não versionados:** decisão explícita de Fabio (31/07/2026). Não constam do Git; preservados em backup persistente.
- **Branch gh-pages:** legado do fluxo antigo (mkdocs gh-deploy). O deploy atual usa Pages por artifact. A branch será arquivada após validação pós-merge.

## 8. Checks executados

| Check | Resultado |
|---|---|
| YAML válido (GOVERNANCA_VERSION, REPOSITORY_PROFILE) | ✅ |
| `python3 scripts/inventariar_acervo.py .` | ✅ exit 0 |
| `python3 scripts/validate_frontmatter.py` | ✅ 0 erros |
| `mkdocs build --strict` | ✅ exit 0 |
| `git ls-files \| grep -Ei '\.pdf$'` | ✅ vazio |
| Busca de segredos | ✅ sem ocorrências |
| Comparação com regras anteriores | ✅ nenhuma regra descartada |

## 9. Riscos

- **Baixo:** adoção de AGENTS_BASE composto localmente; a versão mestre ainda não publicou os módulos finais (commit_origem pendente). Próxima sincronização substituirá o cabeçalho e os hashes.

## 10. Pendências

- Registrar `commit_origem` real do repositório mestre quando a governança 1.0.0 for publicada.
- Proteção de branch em `main` (PR obrigatório + checks) — requer ação de Fabio nas configurações do GitHub.
- Arquivar branch `gh-pages` legada após validação pós-merge.

## 11. Recomendação de merge

**Recomendado** após revisão humana do diff. A implantação é reversível (commit-base: `422c362`).
