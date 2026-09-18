# Plano de Transição Acervo 1 → 2 (R1)

> **STATUS:** PROPOSTA_ARQUITETURAL_R1 (conceitual, NÃO implementada)
> **IMPLEMENTACAO:** NAO_AUTORIZADA
> **MIGRACAO:** NAO_AUTORIZADA
> **Origem:** INSIGHT_HUMANO_HOMOLOGADO_POR_FABIO_TAKWARA
> **Missão:** ACERVO_ARQUITETURA_RELACIONAL_R1
> **Versão pública (versão rastreada):** R1 (2026-09-18)
> **Vinculado a:** este diretório `docs/governanca/` é a versão **rastreada e auditável**; original operacional em `_privado/governanca-operacional/`.

---

# PLANO_TRANSICAO_ACERVO_1_PARA_2_R1

> **Status:** CANDIDATO · GOVERNANCE_CAPTURE_REQUIRED=YES
> **Origem:** INSIGHT_HUMANO_HOMOLOGADO_POR_FABIO_TAKWARA
> **Vinculado a:** `adr-acervo-arquitetura-relacional-r1.md`
> **Localização:** `_privado/governanca-operacional/PLANO_TRANSICAO_ACERVO_1_PARA_2_R1.md`
> **Data:** 2026-09-18
> **Escopo:** sequência sugerida de evolução. NÃO IMPLEMENTAR.

## 1. Estado atual (Acervo 1)

- Coleção temática de documentos organizados em gavetas (`docs/analyses/*`).
- Camada de dados das fichas (frontmatter + seções 1–8 do método Cavichiolli adaptado) já tem cobertura ampla (`INVENTARIO_ACERVO.md`: 291 documentos em `analyses`, 27 `homologado-documentalmente`).
- Camada Web (`TakwaraTec-Acervo-Web`) já pratica navegação por dimensões (`/fundamentos/`, `/evidencias/`, `/cadernos/`, `/cartilhas/`, `/metodologia/`).
- Camada probatória (Zenodo, DOIs) é preservada por identificadores públicos quando existem.

## 2. Estado alvo (Acervo 2)

- Grafo relacional de entidades canônicas (PESSOA, DOCUMENT, THEME, TERRITORY, INSTITUTION, TECHNOLOGY) com relações tipificadas.
- Coleções como visões/consultas sobre o grafo.
- Camada 2 (Acervo Web) lê o grafo por meio de identificadores estáveis, sem duplicar fichas.
- Contribuição pública com pipeline auditável e separação `CONTRIBUIR ≠ PUBLICAR`.

## 3. Princípios de transição

1. **MIGRATION_BY_REFERENCE_FIRST**: antes de mover ou renomear qualquer arquivo, criar uma camada relacional por referência (entidades canônicas + identificadores estáveis) que aponta para o corpus existente.
2. **LEGACY_URLS_PRESERVED**: nenhuma URL pública do MkDocs ou do Acervo Web pode quebrar. A camada relacional deve preservar caminhos antigos.
3. **HUMAN_GOVERNED_STATES**: nenhuma transição de estado documental é automática. Toda mudança passa por revisão humana + homologação registrada.
4. **NO_INFLATE_TRL**: regras do AGENTS_BASE.md e da arquitetura curatorial publicada continuam vinculantes — qualquer relação `avalia`/`aplica` exige fonte primária ou institucional, não propaganda comercial.
5. **CONTRIBUTING_NOT_PUBLISHING**: nenhuma contribuição pública altera conteúdo homologado sem passar pelo pipeline completo (CONTRIBUICAO → TRIAGEM → IDENTIFICACAO → PROVENIENCIA → CANDIDATO → REVISAO → HOMOLOGACAO → PUBLICACAO).

## 4. Fases propostas (sequência indicativa, não autorizada)

### Fase 0 — Captura de governança (esta missão R1)

**Status:** em curso com a presente missão.

Artefatos produzidos:
- `adr-acervo-arquitetura-relacional-r1.md`
- `FICHA_CANONICA_PESSOA_R1.md`
- `MATRIZ_ENTIDADES_RELACOES_R1.md`
- `PLANO_TRANSICAO_ACERVO_1_PARA_2_R1.md`
- `AUDITORIA_COMPATIBILIDADE_ARQUITETURA_RELACIONAL_R1.md`
- Patch mínimo ao README.md do repo científico.

**Não implementação:** nenhum arquivo movido; nenhuma schema implementada; nenhuma migração física.

### Fase 1 — Homologação humana e revisão independente Codex

**Não iniciada.**

- Codex revisa os 5 artefatos da Fase 0.
- Fabio homologa R1 ou pede ajustes.
- Decisão humana sobre ir para Fase 2.

### Fase 2 — Schema mínimo + camada relacional por referência (R2)

**Não autorizada nesta missão.**

- Decidir formato do schema (YAML, JSON, SQLite, RDF — decisão para ADR_R2).
- Mapear as fichas atuais para entidades canônicas por referência, sem mover arquivos.
- Implementar o pipeline `CONTRIBUICAO → TRIAGEM → ... → PUBLICACAO` (mínimo viável).
- Definir vocabulários controlados (THEME, TERRITORY).

### Fase 3 — Visões como consultas (R3)

**Não autorizada nesta missão.**

- Reexpressar as gavetas atuais como consultas sobre o grafo, mantendo URLs antigas.
- Camada Web passa a ler do grafo (em vez de duplicar narrativas em arquivos `.astro`).
- Implementar pelo menos uma coleção-exemplo (ex.: `Ciência no Brasil`) como consulta efetiva.

### Fase 4 — Contribuição pública e descoberta (R4)

**Não autorizada nesta missão.**

- Abrir o pipeline de contribuição para o público, com fila, curadoria e SLA documentado.
- Implementar utilidades públicas (LOCALIZAR, COMPARAR, RELACIONAR, MAPEAR, IDENTIFICAR_LACUNAS, FORMULAR_PERGUNTAS, CRIAR_BIBLIOGRAFIAS, PROPOR_PESQUISA, ENCONTRAR_PESQUISADORES / INSTITUICOES / TERRITORIOS, CONTRIBUIR).

### Fase 5 — Camada 3 probatória (R5)

**Não autorizada nesta missão.**

- Sincronização com Zenodo, DOI.org, Crossref, OpenAlex, GBIF, INPE, MapBiomas, NASA POWER.
- Cache de citações e metadados públicos.
- Validação automática de identificadores quando possível.

## 5. Critérios de promoção entre fases

Cada transição R→R+1 exige, cumulativamente:

- ADRs_R homologados por Fabio;
- revisão independente Codex com P0=0, P1≤2 (não bloqueantes);
- testes de paridade (camada 1 ↔ camada 2 ↔ camada 3) verificados;
- nenhuma URL pública quebrada;
- nenhuma migração física silenciosa;
- nenhum TRR/TRL inflacionado por migração.

## 6. Marcos verificáveis (sem implementação)

- R0 (atual): contagem reproduzível (`scripts/inventariar_acervo.py`) preservada.
- R1 (esta missão): artefatos de governança arquivados em `_privado/governanca-operacional/`.
- R2: schema + camada relacional por referência implementados; paridade verificada por hash contra corpus atual.
- R3: pelo menos uma gaveta expressa como consulta sobre o grafo; URLs antigas 100% preservadas.
- R4: pipeline de contribuição pública com fila e curadoria ativas; pelo menos um canal público.
- R5: camada 3 com pelo menos 3 endpoints sincronizados.

## 7. Riscos

- **Risco de migração física prematura:** mitigado pela regra §3.1 + §3.2.
- **Risco de inflar TRL por migração:** mitigado pela regra §3.4 e por checagem humana de toda relação `avalia` / `aplica`.
- **Risco de perda de URLs públicas:** mitigado pela regra §3.2 e por checagem automatizada de paridade entre fases.
- **Risco de acoplamento prematuro entre camadas:** mitigado pela separação §3.3 e por paridade verificável.

## 8. Não-objetivos

- Não implementar nada nesta missão.
- Não decidir formato de schema nesta missão.
- Não decidir vocabulários controlados nesta missão.
- Não mexer em `docs/`, MkDocs, ou URLs públicas nesta missão.
