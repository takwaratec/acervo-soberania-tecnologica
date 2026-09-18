# Ficha Canônica de Pessoa R1

> **STATUS:** PROPOSTA_ARQUITETURAL_R1 (conceitual, NÃO implementada)
> **IMPLEMENTACAO:** NAO_AUTORIZADA
> **MIGRACAO:** NAO_AUTORIZADA
> **Origem:** INSIGHT_HUMANO_HOMOLOGADO_POR_FABIO_TAKWARA
> **Missão:** ACERVO_ARQUITETURA_RELACIONAL_R1
> **Versão pública (versão rastreada):** R1 (2026-09-18)
> **Vinculado a:** este diretório `docs/governanca/` é a versão **rastreada e auditável**; original operacional em `_privado/governanca-operacional/`.

---

# FICHA_CANONICA_PESSOA_R1

> **Status:** CANDIDATO · GOVERNANCE_CAPTURE_REQUIRED=YES
> **Origem:** INSIGHT_HUMANO_HOMOLOGADO_POR_FABIO_TAKWARA
> **Missão de captura:** ACERVO_ARQUITETURA_RELACIONAL_R1
> **Vinculado a:** `adr-acervo-arquitetura-relacional-r1.md`
> **Localização:** `_privado/governanca-operacional/FICHA_CANONICA_PESSOA_R1.md`
> **Data:** 2026-09-18
> **Escopo:** schema conceitual; NÃO IMPLEMENTAR.

## 1. Princípio

A ficha canônica de PESSOA é uma única ficha por entidade canônica, navegada por todas as gavetas/coleções que a referenciam. A entidade canônica é única; o que muda é a relação semântica (ex.: Montaigne aparece em `Fundamentos` como autor; em `Ciência no Mundo` como influenciador da epistemologia moderna; em `Personagens Históricos` como referência do humanismo).

## 2. Laboratório conceitual

Os **sete mestres** da camada de Fundamentos são o laboratório para o primeiro ciclo de teste do schema:

- Michel de Montaigne
- R. Buckminster Fuller
- Florestan Fernandes
- Edgar Morin
- Paulo Freire
- Darcy Ribeiro
- Milton Santos

**Mollison e Holmgren** permanecem como referências complementares de método e serão usados como casos de interoperabilidade entre schema canônico (pessoa) e schema de tecnologia (Mollison/Holmgren articulam método, não tecnologia Takwara).

## 3. Campos mínimos propostos (R1, conceitual)

| Campo | Tipo | Origem provável | Observação |
|---|---|---|---|
| **INTERNAL_STABLE_ID** | **string estável** | **curadoria (obrigatório)** | **Chave canônica da entidade.** Não depende de fornecedor externo, não depende de URL, não depende de nome humano. Convenção conceitual proposta: `person:000001`. Sintaxe final pendente de ADR_R2. |
| **EXTERNAL_IDENTIFIERS** | **objeto (opcional, múltiplo)** | **fontes externas** | **Aliases, crosswalks, links externos, chaves de reconciliação.** ORCID, Wikidata QID, VIAF, ISNI. **Nunca** é a chave primária canônica da entidade. |
| NOME_CANONICO | string | fonte primária / fontes autorais | nome público principal |
| ALIASES | array<string> | fontes secundárias controladas | apelidos, grafias alternativas, nomes em outras línguas |
| NASCIMENTO | data ou parcial (ano) | fonte autoral/institucional | nunca inferido a partir de secundária |
| FALECIMENTO | data ou parcial ou null | fonte autoral/institucional | null para pessoas vivas |
| PAIS | string controlada | fonte autoral/institucional | controlada por tabela |
| TERRITORIOS | array<ID território> | fonte autoral/institucional | nunca inferido |
| AREAS | array<vocabulário controlado> | curadoria | vocabulário controlado mantido pela curadoria |
| INSTITUICOES | array<ID instituição> | fonte autoral/institucional | vinculação por relação PESSOA ↔ INSTITUICAO |
| BIOGRAFIA_DOCUMENTADA | texto curado | fonte autoral/institucional + ficha documental | texto verificável, não hagiografia |
| CONTRIBUICOES | array<objeto> | fonte autoral/institucional | cada contribuição com fonte e tipo |
| OBRAS_CHAVE | array<ID documento> | ficha documental | cada obra é uma entidade DOCUMENTO canônica |
| DOCUMENTOS_NO_ACERVO | array<ID documento> | ficha documental | documentos que esta pessoa produziu ou coautorou |
| TEMAS_RELACIONADOS | array<ID tema> | curadoria com base em fichas | vocabulário controlado |
| TECNOLOGIAS_RELACIONADAS | array<ID tecnologia> | curadoria com base em fichas | só com relação verificável |
| FONTES_PRIMARIAS | array<objeto> | fonte autoral/institucional | site autoral, depoimentos, entrevistas, autobiografia |
| FONTES_INSTITUCIONAIS | array<objeto> | fonte institucional | biografias acadêmicas, verbetes oficiais, prêmios |
| FONTES_SECUNDARIAS | array<objeto> | literatura revisada por pares | artigos, livros, entrevistas publicadas |
| MIDIA | array<objeto> | curadoria com licença verificada | imagens/vídeos com autoria, licença, origem |
| DIREITOS_MIDIA | string controlada | licença verificada | CC BY, CC BY-SA, domínio público, autorização documentada |
| ESTADO_DOCUMENTAL | enum | curadoria | em-revisao-documental / homologado-documentalmente / historico |
| LIMITES | array<texto> | curadoria | tudo que esta ficha NÃO pode sustentar |
| REVISAO | objeto | curadoria | data, agente, decisão |
| HOMOLOGACAO | objeto | curadoria | data, autoridade humana |
| URL_MKDOCS | URL relativa | ficha documental | rota pública no site MkDocs do Acervo |
| URL_SITE | URL relativa | ficha documental | rota pública na camada Web (Acervo Web) |

## 4. Separação semântica obrigatória (camadas)

Cada item textual da ficha deve declarar, em texto ou em metadado estruturado, a qual camada pertence:

- **FATO_DOCUMENTADO** — afirmação verificável na fonte.
- **INTERPRETACAO_DE_FONTE** — leitura interpretativa do autor a partir da fonte (sempre com referência).
- **SINTESE_CURATORIAL** — articulação do Acervo.
- **RELACAO_EDITORIAL_TAKWARA** — relação do autor com a Tecnologia Takwara (sempre com limite explícito: não valida, não endossa).
- **HIPOTESE** — hipótese ainda não confirmada.
- **LACUNA** — ausência de fonte para item esperado.

A distinção **FATO_DOCUMENTADO × INTERPRETACAO × SINTESE × VISAO_AUTORAL** já é norma do Acervo (cf. `arquitetura-curatorial-acervo-soberania-tecnologica.md`). Este ADR a reforça e exige que a ficha explicite, por item, a qual camada a afirmação pertence.

## 5. Modelo de ID (R1, vinculante)

`INTERNAL_STABLE_ID` é o campo canônico de identidade. Ele substitui o antigo campo `ID` (slug) como chave primária da entidade.

Requisitos vinculantes para `INTERNAL_STABLE_ID`:

- é criado e governado pelo Acervo;
- é persistente;
- não depende de fornecedor externo (DOI/ORCID/ROR/Wikidata);
- não depende de URL;
- não depende de nome humano;
- não muda quando metadados externos mudam.

Convenção conceitual proposta (sintaxe final pendente de ADR_R2):

```
INTERNAL_STABLE_ID = person:000001
EXTERNAL_IDENTIFIERS:
  ORCID: 0000-0000-0000-0000
  Wikidata: Q12345
  VIAF: 12345678
  ISNI: 0000000123456789
```

Regras adicionais:

- `ID_NAMESPACE_REQUIRED=YES` — cada tipo de entidade tem namespace próprio (`person:`, `document:`, `institution:`, `theme:`, `territory:`, `technology:`).
- `ID_FORMAT_FINALIZED=NO` — a sintaxe final (comprimento, separador, leading zeros, alfabético vs numérico) será fixada em ADR_R2.
- O slug humano-legível (`montaigne-1533`) pode coexistir como `HUMAN_SLUG` opcional, secundário, **derivado** do `INTERNAL_STABLE_ID` ou do `NOME_CANONICO`, mas nunca substitui o `INTERNAL_STABLE_ID`.

## 6. Web × Acervo (registrado como P2 futuro)

`WEB_PROFILE_ID != INTERNAL_STABLE_ID`.

A integração entre `profile.id` (Camada 2 — Acervo Web) e `INTERNAL_STABLE_ID` (Camada 1 — Acervo Científico) será decidida em ADR_WEB_R1. **Não é implementada nesta rodada.**

Até lá:

- A Camada 2 pode continuar usando `profile.id` como antes.
- A Camada 1 não pode tratar `WEB_PROFILE_ID` como sinônimo de `INTERNAL_STABLE_ID`.

## 7. Documento × Pessoa — registrado como P2 futuro

`ENTITY_DOCUMENT != ENTITY_PERSON`.

Cada uma terá identidade, schema, relações tipadas, estados compatíveis e proveniência próprias. O ADR_R2 futuro decidirá a coexistência detalhada.

## 5. Critérios de aceitação da ficha_R1 (sem implementação)

A ficha R1 só é considerada apta se cumprir cumulativamente:

- pelo menos uma fonte primária OU institucional citada por campo verificável (nascimento, falecimento, país, territórios, instituições);
- distinção explícita por camada para todas as afirmações factuais;
- `LIMITES` preenchido, não vazio;
- `ESTADO_DOCUMENTAL` declarado;
- `URL_MKDOCS` e/ou `URL_SITE` presentes se houver exposição pública;
- licença de mídia verificada por campo `DIREITOS_MIDIA`.

## 6. Estados e transições

| Estado | Quando | Próximo passo possível |
|---|---|---|
| `rascunho` | entidade identificada, dados insuficientes | revisão humana |
| `em-revisao-documental` | dados básicos coletados; checagem cruzada em curso | revisão humana ou homologação |
| `homologado-documentalmente` | todas as camadas marcadas, fontes primárias checadas, limites declarados | publicação |
| `historico` | desatualizada ou substituída | arquivamento ou deprecação |

Transições exigem agente + autoridade humana + data. Nenhuma transição automática.

## 7. Não-objetivos

- Não implementar schema agora.
- Não migrar fichas existentes.
- Não substituir o frontmatter de `docs/analyses/fundamentos/` (que já existe e é usado em produção).
- Não reescrever GOVERNANCA_DOCUMENTAL.md.
