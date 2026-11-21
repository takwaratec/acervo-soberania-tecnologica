---
tipo_documental: documento-institucional
estado_documental: em-revisao-documental
data_revisao: 2026-09-18
responsavel_curadoria: Fabio Takwara
titulo: "ADR — Sintaxe do INTERNAL_STABLE_ID (R1)"
autor: Fabio Takwara
resumo: "ADR normativo da sintaxe do INTERNAL_STABLE_ID para as seis entidades canônicas do Acervo (PERSON, DOCUMENT, THEME, TERRITORY, INSTITUTION, TECHNOLOGY)."
---

# ADR — Sintaxe do INTERNAL_STABLE_ID (R1)

> **Status:** CANDIDATO_NORMATIVO_R1 (conceitual; sem implementação ainda)
> **IMPLEMENTACAO:** NAO_AUTORIZADA
> **MIGRACAO:** NAO_AUTORIZADA
> **Origem:** INSIGHT_HUMANO_HOMOLOGADO_POR_FABIO_TAKWARA
> **Vinculado a:** `adr-acervo-arquitetura-relacional-r1.md`
> **Escopo:** decidir a sintaxe normativa do `INTERNAL_STABLE_ID` antes da implementação de PESSOA_R1.
> **Não-objetivos:** não atribuir IDs a pessoas reais nesta missão; não implementar banco/API/schema executável; não tocar o Acervo Web; não migrar corpus.

## 1. Princípios obrigatórios

`INTERNAL_STABLE_ID` deve ser:

- **interno ao Acervo** — governado pelo Acervo, sem dependência de terceiros;
- **persistente** — emitido uma vez, válido por todo o tempo de vida da entidade;
- **imutável após emissão** — nome humano, URL, posição em pasta, identificadores externos podem mudar; o ID interno não;
- **independente de nome humano** — alteração de grafia ou nome social não altera o ID;
- **independente de URL** — mudança de rota ou caminho MkDocs não altera o ID;
- **independente de posição em pasta** — migração de diretório não altera o ID;
- **independente de ORCID, DOI, ROR, Wikidata etc.** — provedores externos podem sair do ar sem afetar o ID interno;
- **legível o suficiente para auditoria** — humano pode inspecionar, citar e transcrever sem ambiguidade;
- **adequado a Git, MkDocs, JSON, CSV, URL, API futura** — uma única sintaxe suporta todos os meios;
- **seguro para uso como chave de relação** — aparece como `from`/`to` em arestas do grafo, como índice, como chave estrangeira;
- **sem informação mutável embutida** — não codifica data de criação, autor da emissão, geografia, língua ou categoria (essas informações vivem em metadados, não no ID).

## 2. Entidades R1

Seis entidades canônicas. Os prefixos abaixo são **fixos, imutáveis e reservados** desde R1 — nenhum prefixo pode ser criado, alterado ou reutilizado por ADR posterior sem reescrever todas as referências.

| Entidade | Prefixo canônico |
|---|---|
| PERSON | `person:` |
| DOCUMENT | `document:` |
| THEME | `theme:` |
| TERRITORY | `territory:` |
| INSTITUTION | `institution:` |
| TECHNOLOGY | `technology:` |

### Justificativa dos prefixos longos (vs formas curtas)

| Forma curta | Avaliação | Decisão |
|---|---|---|
| `per:`, `doc:`, `the:`, `ter:`, `ins:`, `tec:` | Mais compactos, mas `per:` e `par:` colidem em leitura humana; `doc:` e `doi:` confundem com o domínio DOI; `the:` e `tem:` confundem com artigo definido; `ter:` e `ter:` colidem com a forma `territory:` em abreviação. Risco elevado de leitura ambígua em auditoria. | **REJEITADO** |
| `pessoa:`, `documento:`, `tema:`, `territorio:`, `instituicao:`, `tecnologia:` | Aparentemente mais legíveis, mas misturam idioma natural com sintaxe de identificador; quebra invariantes YAML/JSON em ambientes multilíngues (acentos, capitalização variável). | **REJEITADO** |
| `person:`, `document:`, `theme:`, `territory:`, `institution:`, `technology:` | Forma única, em inglês (idioma neutro), sem acentos, sem colisões. Cada prefixo tem pelo menos 6 caracteres distintos, evitando ambiguidade com prefixos externos comuns (`doc:`, `doi:`, `geo:`, `org:`, `pub:`, `rec:`). | **APROVADO** |

Os prefixos longos são **case-sensitive, lowercase, sem acentos, sem caracteres especiais**. Nenhum prefixo pode começar com dígito. Nenhum prefixo pode conter `:` (reservado como separador entre prefixo e sequência).

## 2.1. Regra: `ENTIDADE_PESSOA != FICHA_CIENTIFICA`

A futura entidade `PERSON` é um **nó relacional canônico**, **não** uma ficha documental. Esta distinção é vinculante e precede qualquer decisão sobre atribuição de IDs.

| Princípio | Conteúdo |
|---|---|
| `ENTIDADE_PESSOA != FICHA_CIENTIFICA` | a entidade PERSON não substitui fichas científicas existentes |
| `NAO_SUBSTITUI_FICHA` | uma PERSON pode referenciar fichas, mas não absorver ou duplicar seu conteúdo |
| `NAO_RECRIA_FICHAMENTO` | implementar PERSON não recria o fichamento já realizado pela Camada 1 |
| `NAO_DUPLICA_ANALISE` | implementar PERSON não duplica análise documental nem resumo crítico |
| `NAO_COPIA_CONTEUDO_PARA_NOVO_REGISTRO` | nenhuma seção de ficha é duplicada apenas para preencher um novo registro PERSON |
| `PERSON_COMO_NO_RELACIONAL` | PERSON funciona como nó relacional canônico |
| `PERSON_APONTA_PARA_REGISTROS_EXISTENTES` | PERSON aponta para fichas, documentos, obras, instituições, territórios, temas, tecnologias e páginas já existentes |
| `REUSE_EXISTING_RECORDS_FIRST` | YES — reuso de registros existentes é a estratégia prioritária |
| `DUPLICATE_SCIENTIFIC_RECORDS` | NO — duplicação de registros científicos é proibida |

Em particular:

- Uma `PERSON` (ex.: `person:000001`) **referencia** documentos (ex.: `document:000001`) por aresta tipificada `produziu` ou `co-produziu` — não **reescreve** a análise documental já existente na Camada 1.
- Uma `PERSON` pode listar `OBRAS_CHAVE` e `DOCUMENTOS_NO_ACERVO` por identificadores canônicos (`document:`) — não por cópia de texto.
- Uma `PERSON` **não substitui** uma ficha científica: a ficha vive em `documents/` com sua estrutura de 8 seções do método Cavichiolli adaptado; a PERSON vive em `INTERNAL_STABLE_ID` namespace `person:`.
- Quando uma PERSON for alvo de `ficha-canonica-pessoa-r1.md`, esse schema **não** duplica o conteúdo das fichas — ele apenas referencia os IDs canônicos.

Consequência para a sintaxe do ID: a sintaxe do §3 é suficiente — não há conflito entre "PERSON como nó relacional" e a sintaxe `<prefix>:<sequence>`. Não é necessário sub-namespace para distinguir "PERSON-ficha" de "PERSON-relacional" porque a regra acima garante que PERSON nunca é ficha.

## 3. Formato recomendado

```
<prefix>:<sequence>
```

Componentes:

| Componente | Decisão | Justificativa |
|---|---|---|
| CASE | lowercase | uniforme, evita ambiguidade entre case-sensitivity diferente em Git/JSON/CSV |
| SEPARATOR | `:` (dois pontos) | separador único, reservado; não conflita com `/` de URLs, `-` de slugs, `.` de versão; YAML/JSON toleram `:` como string |
| PREFIX_POLICY | fixo e enumerado por entidade (tabela §2) | prefixo é namespace, não informação |
| SEQUENCE_POLICY | inteira positiva com zero-padding a 6 dígitos | auditável, citável, ordenável, fácil de escrever à mão |
| ZERO_PADDING | 6 dígitos (`000001` a `999999`) | cobre até 999.999 entidades por namespace; expandível por prefixo composto se necessário |
| CHECK_DIGIT | nenhum | simplicidade, auditabilidade; risco de typo mitigado pelo uso como string textual em citações e por checksum externo quando necessário |
| RANDOMNESS | nenhuma no ID | aleatoriedade exigiria coordenação adicional; o sequencial já oferece unicidade dentro do namespace e separação por prefixo entre namespaces |
| TIMESTAMP_COMPONENT | nenhum | tempo de criação não pertence ao ID; vive em metadado |
| GEOGRAPHIC_COMPONENT | nenhum no ID | geografia não pertence ao ID; vive em metadado |

Exemplos (placeholders, sem atribuição a pessoas reais):

```
person:000001
document:000001
theme:000001
territory:000001
institution:000001
technology:000001
```

Forma expandida (caso o namespace ultrapasse 999.999): a sequência vira `0000001` (7 dígitos) sem mudar prefixo. O prefixo composto (`person-br-000001`, `document-es-000001`) é **rejeitado** nesta versão porque introduz sub-namespace sem governança clara; se necessário, será objeto de ADR_R2.

### Restrições de formato (vinculantes)

- Apenas caracteres ASCII `[a-z0-9:-]`.
- Prefixo sempre em minúsculas, sem acentos.
- Sequência sempre inteira com zero-padding mínimo de 6 dígitos.
- Total máximo recomendado por linha de registro: 24 caracteres (ex.: `technology:000000001` com 9 dígitos), para preservar legibilidade e evitar truncamento em terminais.
- O ID **nunca** termina com `\n`, `\r`, `;` ou espaço — esses caracteres são reservados para delimitar o ID em citações.

## 4. Imutabilidade

Regras vinculantes (não podem ser quebradas por nenhum ADR posterior sem reescrever todas as referências):

- `ENTITY_RENAMED` ⇒ `ID_UNCHANGED`.
- `ENTITY_MOVED` ⇒ `ID_UNCHANGED`.
- `EXTERNAL_ID_CHANGED` ⇒ `ID_UNCHANGED`.
- `WEB_SLUG_CHANGED` ⇒ `ID_UNCHANGED`.
- `MERGED_ENTITY` ⇒ política conceitual: quando duas entidades canônicas se fundem (ex.: mesma pessoa com grafias diferentes), uma entidade absorve a outra; o ID da absorvida é preservado como **alias** em `external_identifiers` da entidade resultante, com a marca explícita `merged_into: <id_absorvedora>`. O ID da absorvida **nunca** é reutilizado para outra entidade.
- `DELETED_ENTITY` ⇒ política conceitual: o ID é preservado em estado `tombstone` com `replaced_by: <novo_id>` se houver substituição, ou sem `replaced_by` se for retirada definitiva. O ID tombstone **nunca** é reutilizado para outra entidade.

`ID_REUSE=NO` é vinculante.

## 5. Colisões

Mecanismo recomendado: **sequência central por namespace** (uma sequência por entidade), atribuída por autoridade emissora central (ver §6). Avaliação das alternativas:

| Mecanismo | Avaliação | Decisão |
|---|---|---|
| UUID v4 (aleatório de 122 bits) | Não auditável (sem ordem cronológica); difícil de citar em texto corrido; não legível. | REJEITADO |
| ULID (26 chars, lexicográfico, com timestamp) | Auditável e ordenável, mas mistura timestamp no ID; adiciona informação mutável relativa ao instante de emissão; reduz legibilidade. | REJEITADO (pode ser revisitado como alias opcional em ADR_R2) |
| Hash determinístico (SHA-256 do conteúdo) | Não estável: muda quando metadados mudam; não legível. | REJEITADO |
| Contador por entidade (escolhido) | Auditável, ordenável, simples, offline-friendly, sem coordenação externa. Risco de colisão resolvido pelo **prefixo por entidade**: dois agentes que emitam `person:000007` no mesmo namespace colidem, mas `person:000007` e `document:000007` não colidem (namespaces distintos). | APROVADO |
| Contador global único | Resolve qualquer colisão entre entidades, mas mistura namespaces — IDs de naturezas distintas compartilham a mesma sequência. Perde a legibilidade por tipo. | REJEITADO |

**Prevenção operacional de colisão**: autoridade emissora central mantém um registro (não necessariamente um banco) com a última sequência emitida por namespace. Emissão offline (por agente autônomo) só é permitida com **reserva de intervalo** (ver §6).

**Detecção de colisão pós-fato**: como todo ID é único dentro do `(prefixo, sequência)`, colisões aparecem imediatamente como duplicatas. Resolução: a segunda emissão é rejeitada; se o conflito for detectado após publicação, prevalece a emissão mais antiga (a segunda é marcada `tombstone`).

## 6. Emissão — autoridade e política

```
WHO_MINTS_ID=Autoridade de Curadoria do Acervo (papel humano, não implementação).
WHEN_ID_IS_MINTED=No momento de homologação documental da entidade, ou antes, com reserva.
CAN_AGENT_MINT_AUTONOMOUSLY=Sim, dentro de um intervalo de sequência reservado pela Autoridade de Curadoria.
CAN_HUMAN_OVERRIDE=Sim — a Autoridade de Curadoria pode reemitir, emitir fora de ordem ou reservar intervalos; cada override é registrado em log de governança (sem expor o ID emitido no log — apenas o motivo e o intervalo).
CAN_ID_BE_REUSED=NO (vinculante).
```

Política operacional (conceitual, sem implementação):

1. A Autoridade de Curadoria reserva intervalos de sequência por namespace. Exemplo: `person:000001`–`person:001000` para a fase de teste; `person:001001`–`person:010000` para a fase de homologação aberta; `person:010001`–`person:999999` para produção.
2. Um agente (humano ou assistido por IA) pode emitir dentro do intervalo reservado.
3. Após a emissão, o agente registra o ID em uma tabela local de uso (não em banco, no R1 conceitual).
4. A Autoridade de Curadoria audita periodicamente o uso, detecta lacunas (não é obrigatório preencher todos os IDs de um intervalo) e reconcilia.
5. Emissões offline (sem rede) seguem o mesmo princípio, mas com reconciliação obrigatória antes da publicação.
6. `ID_REUSE=NO`: um ID tombstone nunca é reatribuído.

## 7. Identificadores externos

`EXTERNAL_IDENTIFIERS != INTERNAL_STABLE_ID`. Os identificadores externos são **aliases, crosswalks, chaves de reconciliação, links externos e fontes auxiliares de identidade**. Modelo conceitual (não executar):

```yaml
internal_stable_id: person:000001
external_identifiers:
  orcid: 0000-0000-0000-0000
  wikidata: Q12345
  viaf: 12345678
  isni: 0000000123456789
```

Em particular:

- `ORCID` é chave externa de pessoa, não chave primária.
- `DOI` é chave externa de documento, não chave primária.
- `ROR` é chave externa de instituição, não chave primária.
- `Wikidata QID` é chave externa de qualquer entidade, não chave primária.
- `VIAF`/`ISNI` são chaves externas de pessoa, não chave primária.

Para cada entidade, `external_identifiers` é um **mapa aberto** (não enumeração fechada): provedores podem ser adicionados sem mudar o ID interno.

## 8. Relação com `WEB_PROFILE_ID`

`WEB_PROFILE_ID != INTERNAL_STABLE_ID`. O Acervo Web pode usar `profile.id` (ex.: `montaigne-1533`) como chave própria da Camada 2. O crosswalk é:

```
WEB_PROFILE_ID  ──→  INTERNAL_STABLE_ID
profile.id              internal_stable_id
(Acervo Web)            (Acervo Científico)
```

Princípios:

- O `INTERNAL_STABLE_ID` é a fonte canônica de identidade.
- O `WEB_PROFILE_ID` é slug humano-legível derivado de metadados (nome, datas) — não pode ser usado como chave primária na Camada 1.
- A integração `profile.id` ↔ `INTERNAL_STABLE_ID` é objeto de ADR_WEB_R1; não é implementada nesta rodada.
- `WEB_PROFILE_ID` pode mudar (ex.: para refletir uma nova grafia); o `INTERNAL_STABLE_ID` permanece.

## 9. Legibilidade e exemplos

Placeholders para as seis entidades (não atribuem IDs a pessoas reais):

```
person:000001        # pessoa fictícia: "Person Alfa"
person:000002        # pessoa fictícia: "Person Beta"
document:000001      # documento fictício: "Document Alfa"
document:000002      # documento fictício: "Document Beta"
theme:000001         # tema fictício: "Theme Alfa"
territory:000001     # território fictício: "Territory Alfa"
institution:000001   # instituição fictícia: "Institution Alfa"
technology:000001    # tecnologia fictícia: "Technology Alfa"
```

Exemplos negativos (rejeitados):

- `montaigne-1533` — contém nome humano e data (informação mutável).
- `person:1533` — sem prefixo; ambiguidade entre entidades.
- `person:br:000001` — sub-namespace geográfico sem governança.
- `https://acervo.example/person/1533` — ID contém URL.
- `PERSON:000001` — caixa diferente quebra invariante.
- `person:1` — sem zero-padding; ordem lexicográfica diverge da numérica em sistemas que ordenem por string.

**PROIBIDO** atribuir IDs aos sete mestres (Montaigne, Fuller, Florestan, Morin, Freire, Darcy, Milton Santos) ou a Mollison/Holmgren nesta missão. A atribuição real virá apenas após implementação, por ADR_R2 ou missão subsequente.

## 10. Compatibilidade

| Meio | Compatibilidade | Notas |
|---|---|---|
| YAML front matter | YAML_COMPAT=YES | string entre aspas ou sem aspas; `:` exige aspas em alguns parsers; recomenda-se aspas duplas |
| Markdown | MARKDOWN_COMPAT=YES | string pura, não requer escapagem |
| JSON | JSON_COMPAT=YES | string com aspas; `:` é literal |
| CSV | CSV_COMPAT=YES | string pura, sem vírgula, aspas ou quebra de linha |
| URL | URL_COMPAT=YES com codificação | `person%3A000001`; o `:` precisa ser codificado como `%3A` em URLs |
| MkDocs | MKDOCS_COMPAT=YES | navegação e referências funcionam como qualquer string |
| Git filenames | GIT_FILENAME_COMPAT=YES com adaptação | `person-000001.md` ou `person_000001.md`; Git em si aceita `:` mas alguns sistemas de arquivo não — usar substituição local |
| API futura | API_FUTURE_COMPAT=YES | ID é string ASCII puro, fácil de serializar |
| Grafo de relações | GRAPH_COMPAT=YES | ID aparece como `from`/`to` em arestas; legível e citável |
| Exportação RDF/JSON-LD futura | RDF_FUTURE_COMPAT=YES | pode ser mapeado para `acervo:ID` ou usado como `skos:notation` |

`RDF_FUTURE_COMPAT=YES` é declarado apenas como compatibilidade potencial; **nenhum mapeamento para SKOS, Dublin Core ou schema.org é fixado nesta missão**. A fixação de prefixos RDF é objeto de ADR_R2.

## 11. Decisão normativa

### Recomendação única

`INTERNAL_STABLE_ID_SYNTAX = <prefixo>:<sequência de 6 dígitos>`

com:

- `prefixo` ∈ `{person, document, theme, territory, institution, technology}`
- `sequência` ∈ `{000001, ..., 999999}`, zero-padding a 6 dígitos
- case-sensitive, lowercase, apenas ASCII `[a-z0-9:-]`
- independente de nome, URL, posição em pasta, identificadores externos
- `ID_REUSE=NO` (tombstone)
- autoridade emissora central com reserva de intervalos por namespace

### Justificativa (RATIONALE)

- Auditabilidade: sequência ordenada é citável e transcrita sem ambiguidade.
- Simplicidade: sem timestamp, sem hash, sem ULID — fácil de implementar quando a Camada 2 ler o grafo.
- Estabilidade: prefixo + sequência são imutáveis; mudanças externas não afetam o ID.
- Uso offline: agentes podem emitir IDs localmente desde que dentro de intervalo reservado pela autoridade central; a reconciliação é periódica e não bloqueia o trabalho.
- Baixo risco de colisão: namespaces separados por entidade + sequência por namespace + autoridade central.
- Compatibilidade multi-meio: ASCII puro, lowercase, sem caracteres especiais além de `:`.

### Tradeoffs reconhecidos (TRADEOFFS)

- **Não-ordenação entre namespaces**: não é possível afirmar que `person:000001` foi emitido antes ou depois de `document:000001` sem metadado adicional. Aceitável porque a ordem entre naturezas diferentes não é semanticamente relevante.
- **Capacidade limitada por namespace**: 999.999 IDs por entidade. Aceitável em R1; expansível para 9.999.999 com zero-padding de 7 dígitos, ou para namespace composto em ADR_R2.
- **Risco operacional humano**: autoridade central pode errar ao reservar intervalo, levando a colisão dentro do namespace. Mitigação: detecção por duplicação + tombstone da emissão mais recente.

### Alternativas rejeitadas (REJECTED_ALTERNATIVES)

- `person:01H...` (ULID): mistura timestamp; reduz legibilidade; rejeitado.
- `person:000001-uuid` (UUID v4 como sequência): não auditável; rejeitado.
- `person:br:000001` (sub-namespace geográfico): adiciona informação mutável (geografia política pode mudar); sem governança clara para sub-namespaces; rejeitado.
- `person:1533` (slug derivado de nome e data): contém nome humano; quebra princípio de independência; rejeitado.
- `person:000001@v1` (sufixo de versão): sugere versionamento semântico; versionamento de entidade não cabe no ID — vive em metadado; rejeitado.
- `person:000001:br` (geografia como sufixo): mesma objeção do sub-namespace geográfico; rejeitado.
- `PERSON:000001` (caixa alta/mista): quebra invariante de case-sensitivity uniforme; rejeitado.
- ID como hash do conteúdo (SHA-256 ou similar): não estável; muda com metadados; rejeitado.
- ID derivado de URL (`/person/000001`): URL é mutável; quebra princípio de independência; rejeitado.

## 12. Não-objetivos

- Não atribuir IDs a pessoas reais nesta missão.
- Não implementar banco de dados, API ou schema executável.
- Não alterar o Acervo Web.
- Não migrar corpus.
- Não decidir prefixos RDF (objeto de ADR_R2).
- Não decidir vocabulário controlado (objeto de ADR_R2).

## 13. P2 declarado (referências cruzadas)

| P2 | Status | Próximo gate |
|---|---|---|
| P2_D (sintaxe do ID) | ESTE ADR (candidato) | CODEX_REVIEW |
| P2_A (coexistência documento × pessoa) | DEFERRED | ADR_R2 |
| P2_B (governança do vocabulário controlado) | DEFERRED | ADR_R2 |
| P2_C (mapeamento Web × Acervo) | DEFERRED | ADR_WEB_R1 |

## 14. Artefatos relacionados

- `arquitetura-relacional.md` — visão geral da arquitetura R1.
- `adr-acervo-arquitetura-relacional-r1.md` — ADR raiz R1 (define `INTERNAL_STABLE_ID` como conceito, sem fixar sintaxe).
- `ficha-canonica-pessoa-r1.md` — schema PESSOA_R1 (onde o ID aparece como campo-chave).
- `matriz-entidades-relacoes-r1.md` — entidades e relações tipificadas.

## 15. Anexos

- Anexo A: tabela de prefixos e exemplos (resumo de §2 e §9).
- Anexo B: política de colisão e tombstone (resumo de §4 e §5).
