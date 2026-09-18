---
tipo_documental: documento-institucional
estado_documental: em-revisao-documental
data_revisao: 2026-09-18
responsavel_curadoria: Fabio Takwara
titulo: "Auditoria de Compatibilidade — Arquitetura Relacional R1"
autor: Fabio Takwara
resumo: "Auditoria de compatibilidade entre a proposta R1 e a governança existente."
---
# Auditoria de Compatibilidade — Arquitetura Relacional R1

> **STATUS:** PROPOSTA_ARQUITETURAL_R1 (conceitual, NÃO implementada)
> **IMPLEMENTACAO:** NAO_AUTORIZADA
> **MIGRACAO:** NAO_AUTORIZADA
> **Origem:** INSIGHT_HUMANO_HOMOLOGADO_POR_FABIO_TAKWARA
> **Missão:** ACERVO_ARQUITETURA_RELACIONAL_R1
> **Versão pública (versão rastreada):** R1 (2026-09-18)
> **Vinculado a:** este diretório `docs/governanca/` é a versão **rastreada e auditável**; original operacional em `_privado/governanca-operacional/`.

---

# AUDITORIA_COMPATIBILIDADE_ARQUITETURA_RELACIONAL_R1

> **Status:** CANDIDATO · GOVERNANCE_CAPTURE_REQUIRED=YES
> **Vinculado a:** `adr-acervo-arquitetura-relacional-r1.md`
> **Localização:** `_privado/governanca-operacional/AUDITORIA_COMPATIBILIDADE_ARQUITETURA_RELACIONAL_R1.md`
> **Data:** 2026-09-18
> **Escopo:** auditoria de compatibilidade da proposta R1 com a governança existente. NÃO RESOLVE CONFLITOS.

## 1. Método

Comparar ponto a ponto cada princípio da proposta R1 com:

- `README.md` (acesso público e princípios de curadoria);
- `GOVERNANCA_DOCUMENTAL.md` (estados e taxonomia);
- `docs/metodologia.md` (método Cavichiolli adaptado);
- `mkdocs.yml` (configuração do site);
- estrutura `docs/analyses/` (organização temática);
- `AGENTS_BASE.md` / `AGENTS_LOCAL.md` (regras do ecossistema);
- `arquitetura-curatorial-acervo-soberania-tecnologica.md` (artigo Zenodo DOI 10.5281/zenodo.21797806).

Classificação por item:
- **COMPATIVEL** — o princípio R1 já está coerente com a prática atual ou apenas a explicita.
- **EXTENSAO** — o princípio R1 amplia sem conflitar; decisão de incorporação fica para ADR futuro.
- **REQUER_REFORMA** — exige mudança em regra atual; precisa de ADR_R2 explícito.
- **CONFLITO** — incompatível; precisa de decisão humana.

## 2. Auditoria ponto a ponto

### 2.1 Princípio constitutivo (grafo de entidades/visões)

- vs. `README.md` "Infraestrutura pública de curadoria e conexão do conhecimento": **EXTENSAO** — R1 explicita o modelo relacional; o README atual fala em infraestrutura sem detalhar o grafo.
- vs. `arquitetura-curatorial-acervo-soberania-tecnologica.md` (Zenodo 21797806): **COMPATIVEL** — o artigo já fala em "infraestrutura pública de conhecimento em desenvolvimento" e em "transforma literatura científica em referências rastreáveis, comparáveis e utilizáveis"; R1 explicita o modelo por trás dessa promessa.
- vs. `GOVERNANCA_DOCUMENTAL.md`: **EXTENSAO** — gavetas lógicas continuam válidas; R1 acrescenta a possibilidade de gavetas dinâmicas por consulta sem invalidar a taxonomia atual.
- vs. `docs/analyses/index.md`: **COMPATIVEL** — a estrutura de eixos temáticos permanece; R1 propõe que cada eixo seja também uma consulta sobre o grafo.

### 2.2 Três camadas do "Segundo Cérebro"

- vs. `README.md`: **EXTENSAO** — o README menciona site + repositório + Zenodo, mas não explicita camada probatória distinta da camada científica.
- vs. `arquitetura-curatorial-acervo-soberania-tecnologica.md`: **COMPATIVEL** — o artigo já fala em "fonte original ao projeto" e identifica o papel do Zenodo como camada de depósito.
- vs. `mkdocs.yml`: **COMPATIVEL** — MkDocs publica apenas a camada 1 (científica) + camada 2 (Web) indiretamente via redirect_maps; a camada 3 é externa.
- vs. `GOVERNANCA_DOCUMENTAL.md` (estados): **COMPATIVEL** — os estados `em-revisao-documental` / `homologado-documentalmente` / `historico` permanecem como governança interna da camada 1; R1 não propõe substituí-los.

### 2.3 Entidades e modelo relacional

- vs. `docs/analyses/fundamentos/index.md`: **EXTENSAO** — o índice já referencia perfis (Montaigne, Fuller, Florestan, Morin, Freire, Darcy, Milton Santos, Mollison, Holmgren) que são candidatos óbvios a PESSOA_R1.
- vs. `docs/metodologia.md`: **REQUER_REFORMA** — o método atual é centrado em fichas de documentos (8 seções do método Cavichiolli adaptado); a introdução de fichas de PESSOA exige decisão sobre convivência com o método atual, sem substituí-lo. ADR_R2 deve explicitar.
- vs. `arquitetura-curatorial-acervo-soberania-tecnologica.md`: **EXTENSAO** — o artigo fala em "cinco camadas epistemológicas" (evidência científica externa, evidência empírica autoral documentada, síntese curatorial, hipótese ou arquitetura autoral, validação científica própria delimitada); R1 reusa essas camadas como rótulo por aresta do grafo, o que é coerente e ganha uma camada explícita para pessoas.

### 2.4 Vocabulários controlados (THEME / TERRITORY / INSTITUTION)

- vs. `docs/analyses/`: **REQUER_REFORMA** — os eixos atuais são pastas físicas; a transição para vocabulário controlado exige decisão sobre convivência entre pasta e tag. ADR_R2.
- vs. `GOVERNANCA_DOCUMENTAL.md`: **COMPATIVEL** — não há vocabulário controlado atualmente; a introdução é extensão, não conflito.
- vs. `mkdocs.yml`: **EXTENSAO** — a navegação atual pode coexistir com vocabulário controlado se a navegação continuar espelhando a estrutura física.

### 2.5 Identificadores estáveis

- vs. `docs/metodologia.md`: **COMPATIVEL** — DOI, ISBN, ISSN, Handle já são exigidos quando existentes.
- vs. `arquitetura-curatorial-acervo-soberania-tecnologica.md`: **COMPATIVEL** — o artigo cita DOI e identificadores persistentes como camada de proveniência.
- vs. `GOVERNANCA_DOCUMENTAL.md`: **COMPATIVEL** — a exigência de identificador público já é regra.
- vs. camada 2 (Acervo Web): **REQUER_REFORMA** — o Acervo Web hoje ancora perfis por `profile.id` em `foundations.ts`; a introdução de ORCID/ROR/Wikidata QID exige decisão sobre fonte canônica entre os dois repositórios. ADR_R2 + decisão Maestro.

### 2.6 Pipeline de contribuição

- vs. `AGENTS_LOCAL.md` "Regras locais obrigatórias": **EXTENSAO** — o AGENTS_LOCAL já cita "sugerir fonte, corrigir metadado, indicar pesquisador" como vetores de contribuição; R1 formaliza o pipeline com gates.
- vs. `AGENTS_BASE.md` "revisão humana, rastreabilidade, exigência de pull request": **COMPATIVEL** — o pipeline R1 é explicitamente humano-gated e rastreável.
- vs. `arquitetura-curatorial-acervo-soberania-tecnologica.md`: **EXTENSAO** — o artigo menciona revisão progressiva e abertura à colaboração; R1 explicita o pipeline e a separação `CONTRIBUIR ≠ PUBLICAR`.

### 2.7 Migrations: MIGRATION_BY_REFERENCE_FIRST

- vs. `arquitetura-curatorial-acervo-soberania-tecnologica.md`: **COMPATIVEL** — o artigo não trata de migração física; a regra R1 evita introduzir essa decisão unilateral.
- vs. `mkdocs.yml` (redirect_maps): **COMPATIVEL** — redirects já existem para migrações pontuais; R1 apenas exige o mesmo cuidado para todas as transições.
- vs. `GOVERNANCA_DOCUMENTAL.md`: **COMPATIVEL** — a governança atual não obriga migração física; R1 explicita a proibição.

### 2.8 Commits atômicos (um insight estrutural = um lote de governança)

- vs. `AGENTS_BASE.md` "exigência de pull request": **COMPATIVEL** — PRs são o canal de homologação humana.
- vs. `AGENTS_LOCAL.md` (estrutura): **COMPATIVEL** — não há regra contrária; R1 explicita a convenção de commits atômicos.
- vs. `GOVERNANCA_DOCUMENTAL.md`: **COMPATIVEL** — não trata de commits; R1 é aditiva.

### 2.9 GOVERNANCE_CAPTURE_REQUIRED=YES

- vs. `AGENTS_BASE.md` "ARQUIVO GERENCIADO CENTRALMENTE não deve ser alterado diretamente": **COMPATIVEL** — reforça o princípio.
- vs. `AGENTS_LOCAL.md` "Regra de fronteira: conteúdo de quarentena e privado nunca entra em `docs/`": **COMPATIVEL** — esta missão produz artefatos em `_privado/governanca-operacional/`, fora do build.
- vs. `README.md`: **EXTENSAO** — o README atual não menciona o ciclo de captura de governança; o patch mínimo desta missão adiciona uma frase.

### 2.10 Contribuição pública não altera homologado

- vs. `AGENTS_BASE.md` "merge_humano_obrigatorio, publicacao_humana_obrigatoria": **COMPATIVEL** — pipeline R1 é humano-gated.
- vs. `AGENTS_LOCAL.md` "revisão humana, rastreabilidade": **COMPATIVEL**.
- vs. `arquitetura-curatorial-acervo-soberania-tecnologica.md`: **COMPATIVEL** — o artigo cita "revisão progressiva e abertura à colaboração humana com rastreabilidade".

## 3. Conflitos identificados

**Nenhum CONFLITO direto** entre a proposta R1 e a governança atual. Os pontos REQUER_REFORMA listados em §2.3, §2.4 e §2.5 não são conflitos — são decisões adiadas para ADR_R2:

- Convivência entre ficha-de-documento (método Cavichiolli adaptado, 8 seções) e ficha-de-pessoa (PESSOA_R1).
- Convivência entre pasta-física-eixo (estrutura `docs/analyses/`) e vocabulário controlado (THEME).
- Convivência entre `profile.id` do Acervo Web e identificadores externos (ORCID/ROR/Wikidata QID).

Cada uma dessas decisões é explicitamente diferida para ADR_R2 ou para decisão do Maestro. A presente missão R1 não toma nenhuma dessas decisões.

## 4. Compatibilidade cumulativa

| Componente | Classificação |
|---|---|
| Princípio constitutivo (grafo/visões) | COMPATÍVEL com `arquitetura-curatorial`; EXTENSÃO para README/governança |
| Três camadas | COMPATÍVEL com Zenodo + MkDocs; EXTENSÃO para README |
| Entidades + relações | EXTENSÃO em quase todos os pontos; REQUER_REFORMA pontual em metodologia |
| Vocabulários controlados | REQUER_REFORMA (decisão para ADR_R2) |
| Identificadores estáveis | COMPATÍVEL em quase todos os pontos; REQUER_REFORMA no Acervo Web (decisão para Maestro) |
| Pipeline de contribuição | COMPATÍVEL com AGENTS_BASE + AGENTS_LOCAL |
| MIGRATION_BY_REFERENCE_FIRST | COMPATÍVEL com tudo |
| Commits atômicos | COMPATÍVEL |
| GOVERNANCE_CAPTURE_REQUIRED | COMPATÍVEL com princípio de arquivos gerenciados centralmente |
| Contribuição não altera homologado | COMPATÍVEL com merge humano |

## 5. Não-objetivos desta auditoria

- Não resolve os REQUER_REFORMA. Eles ficam para ADR_R2 ou para decisão humana.
- Não altera nada no repo científico além do patch mínimo proposto ao README.
- Não toca na camada Web.
