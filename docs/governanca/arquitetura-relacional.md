# Arquitetura relacional do Acervo (R1 — conceitual)

> **STATUS:** PROPOSTA_ARQUITETURAL_R1 (conceitual, NÃO implementada)
> **IMPLEMENTACAO:** NAO_AUTORIZADA
> **MIGRACAO:** NAO_AUTORIZADA
> **Origem:** INSIGHT_HUMANO_HOMOLOGADO_POR_FABIO_TAKWARA
> **Missão:** ACERVO_ARQUITETURA_RELACIONAL_R1 + R2_CORRECAO_P1
> **Versão pública:** R1 (2026-09-18)
> **Vinculado a:** este diretório `docs/governanca/` é a versão **rastreada e auditável** dos artefatos conceituais. Handoff operacional permanece em `_privado/governanca-operacional/`.

## 1. Resumo

O Acervo de Soberania Tecnológica está evoluindo de uma coleção temática de documentos para uma **infraestrutura pública, coletiva, navegável e reutilizável de investigação**, preservando rigor documental, proveniência e revisão humana. O Acervo passa a ser formalmente modelado como grafo de entidades e relações, com coleções/gavetas reinterpretadas como **visões** sobre o grafo, não coleções paralelas.

Esta página é a porta de entrada da versão **R1 (conceitual)** da arquitetura. Os documentos abaixo formalizam as decisões de R1, auditam compatibilidade com a governança existente e propõem a transição para R2.

## 2. Princípio constitutivo

> O Acervo não é apenas uma coleção temática de documentos. É uma infraestrutura pública de investigação. A arquitetura deve permitir **navegar pelo mesmo corpus por diferentes dimensões** sem duplicar a entidade canônica.
>
> **Gavetas e coleções são VISÕES dessas relações**, não cópias independentes do conhecimento.

## 3. Três camadas

| Camada | Função | Localização |
|---|---|---|
| CAMADA_1 — ACERVO_CIENTIFICO | Registro canônico: fichas, entidades, relações, sínteses, estados documentais, rastreabilidade | este repositório (`acervo-soberania-tecnologica`) |
| CAMADA_2 — ACERVO_WEB | Mediação editorial: descoberta, narrativa, visualização, exploração, mapas, interação | `TakwaraTec-Acervo-Web` (Astro) |
| CAMADA_3 — FONTES_CORPUS | Camada probatória: documentos integrais, DOIs, endpoints, arquivos, repositórios, fontes institucionais | Zenodo, DOI.org, Crossref, OpenAlex, GBIF, INPE, MapBiomas, NASA POWER |

Fluxo público:

```
SITE → FICHA_CANONICA → FONTES_CORPUS
```

## 4. Modelo de entidades (R1, conceitual)

```
DOCUMENTOS ↔ PESSOAS ↔ TEMAS ↔ TERRITORIOS ↔ INSTITUICOES ↔ TECNOLOGIAS
```

Seis entidades canônicas. Para cada entidade serão especificados (em R2) identificador estável, nome/título canônico, aliases, descrição curatorial, relações, fontes, estado documental, proveniência, datas, tags controladas, links internos e externos, revisão, homologação e licença quando aplicável.

## 5. Modelo de relações (R1, conceitual)

Relações tipificadas, com diferenciação semântica obrigatória. Em particular, `MENciona` é distinto de `ESTUDA`/`AVALIA`/`APLICA`. A camada de origem (`FATO_DOCUMENTADO` / `INTERPRETACAO_DE_FONTE` / `SINTESE_CURATORIAL` / `HIPOTESE` / `LACUNA`) é registrada em cada aresta do grafo.

Lista completa em `matriz-entidades-relacoes-r1.md`.

## 6. Identificadores

A correção R2_CORRECAO_P1 fixou dois princípios vinculantes:

**INTERNAL_STABLE_ID — obrigatório.**
- Criado e governado pelo Acervo.
- Persistente; não depende de fornecedor externo; não depende de URL; não depende de nome humano; não muda quando metadados externos mudam.
- É a chave canônica da entidade.
- Convenção conceitual proposta (sintaxe final a ser fixada por ADR_R2):
  - `person:000001`
  - `document:000001`
  - `institution:000001`
  - `theme:000001`
  - `territory:000001`
  - `technology:000001`
- `ID_NAMESPACE_REQUIRED=YES`.
- `ID_FORMAT_FINALIZED=NO` (decisão de sintaxe para ADR_R2).

**EXTERNAL_IDENTIFIERS — opcionais, múltiplos.**
- ORCID, DOI, ROR, Wikidata QID, ISBN, ISSN, VIAF, ISNI e outros identificadores externos são **aliases, crosswalks, links externos, chaves de reconciliação ou fontes auxiliares de identidade**.
- **Nunca** são chave primária canônica da entidade.

**Web × Acervo (P2 futuro, registrado).**
- `WEB_PROFILE_ID != INTERNAL_STABLE_ID`.
- A integração `profile.id` (Acervo Web) ↔ `INTERNAL_STABLE_ID` (Acervo Científico) será objeto de ADR_WEB_R1; **não é implementada nesta rodada**.

## 7. Estados, camadas e governança

- **Estados:** `rascunho`, `em-revisao-documental`, `homologado-documentalmente`, `historico` (cf. `GOVERNANCA_DOCUMENTAL.md`).
- **Camadas epistemológicas:** `FATO_DOCUMENTADO` · `INTERPRETACAO_DE_FONTE` · `SINTESE_CURATORIAL` · `RELACAO_EDITORIAL_TAKWARA` · `HIPOTESE` · `LACUNA`.
- **Princípios:** revisão humana, rastreabilidade, separação `EVIDENCIA != VALIDACAO != CERTIFICACAO`, `INFLUENCIA != ENDOSSO`, `PATENTE != DESEMPENHO`, `PROTOTIPO != TECNOLOGIA VALIDADA`.

## 8. Regra de captura de governança

> INSIGHT_HUMANO_APROVADO → FORMALIZACAO → GOVERNANCE_CAPTURE → ARTEFATO_VERSIONADO → COMMIT_ATOMICO → IMPLEMENTACAO

Princípios vinculantes:

- `CHAT_HISTORY != INSTITUTIONAL_MEMORY`.
- `PRIVATE_HANDOFF != VERSIONED_GOVERNANCE`.
- Toda decisão arquitetural, metodológica ou de taxonomia deve receber `GOVERNANCE_CAPTURE_REQUIRED=YES` e ser registrada em arquivo versionado (este diretório, `README`, `GOVERNANCA_DOCUMENTAL.md`, ADR ou combinação apropriada).

## 9. Convenções de commits atômicos

**UM_INSIGHT_ESTRUTURAL = UM_LOTE_DE_GOVERNANCA.** Não misturar em um mesmo commit:

- governança
- migração
- UI
- fichamento
- conteúdo editorial

Exemplos de convenção (esta missão R2_CORRECAO_P1 segue esse padrão):

```
docs(governance): promover ADRs R1 para área versionada e corrigir identificador interno
docs(schema): definir modelo conceitual de pessoa canônica R1
docs(contribution): definir pipeline público de contribuição
```

## 10. P2 declarado (não implementado nesta rodada)

| P2 | Descrição | Próximo gate |
|---|---|---|
| P2_A | ADR de coexistência `ENTITY_DOCUMENT` × `ENTITY_PERSON` (schemas próprios, estados compatíveis, proveniência própria) | ADR_R2 futuro |
| P2_B | Governança do vocabulário controlado (THEME / TERRITORY / INSTITUTION): namespace, versionamento, política de redirect | ADR_R2 futuro |
| P2_C | Mapeamento entre `WEB_PROFILE_ID` (Acervo Web) e `INTERNAL_STABLE_ID` (Acervo Científico) | ADR_WEB_R1 |

## 11. Não-objetivos desta rodada

- Não implementar schema.
- Não migrar arquivos.
- Não decidir formato final de ID (decisão para ADR_R2).
- Não decidir vocabulários controlados.
- Não abrir a Camada 2 do Acervo Web.
- Não alterar `GOVERNANCA_DOCUMENTAL.md` nem a arquitetura curatorial publicada no Zenodo.

## 12. Documentos desta seção

- `adr-acervo-arquitetura-relacional-r1.md` — ADR raiz R1.
- `ficha-canonica-pessoa-r1.md` — schema conceitual PESSOA_R1.
- `matriz-entidades-relacoes-r1.md` — matriz de entidades e relações.
- `plano-transicao-acervo-1-para-2-r1.md` — sequência de transição R0→R5.
- `auditoria-compatibilidade-arquitetura-relacional-r1.md` — auditoria de compatibilidade com governança atual.

Cada documento declara `STATUS=PROPOSTA_ARQUITETURAL_R1`, `IMPLEMENTACAO=NAO_AUTORIZADA`, `MIGRACAO=NAO_AUTORIZADA` no topo.
