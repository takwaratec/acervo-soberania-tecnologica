# ADR Acervo Arquitetura Relacional R1

> **STATUS:** PROPOSTA_ARQUITETURAL_R1 (conceitual, NÃO implementada)
> **IMPLEMENTACAO:** NAO_AUTORIZADA
> **MIGRACAO:** NAO_AUTORIZADA
> **Origem:** INSIGHT_HUMANO_HOMOLOGADO_POR_FABIO_TAKWARA
> **Missão:** ACERVO_ARQUITETURA_RELACIONAL_R1
> **Versão pública (versão rastreada):** R1 (2026-09-18)
> **Vinculado a:** este diretório `docs/governanca/` é a versão **rastreada e auditável**; original operacional em `_privado/governanca-operacional/`.

---

# ADR_ACERVO_ARQUITETURA_RELACIONAL_R1

> **Status:** CANDIDATO · GOVERNANCE_CAPTURE_REQUIRED=YES
> **Origem:** INSIGHT_HUMANO_HOMOLOGADO_POR_FABIO_TAKWARA
> **Missão de captura:** ACERVO_ARQUITETURA_RELACIONAL_R1
> **Localização:** `_privado/governanca-operacional/ADR_ACERVO_ARQUITETURA_RELACIONAL_R1.md`
> **Data:** 2026-09-18
> **Escopo:** formalização conceitual. NÃO IMPLEMENTAR; NÃO MIGRAR.

## 1. Contexto

O Acervo de Soberania Tecnológica vem sendo construído como uma coleção temática de documentos organizados em gavetas (`docs/analyses/*`). O insight homologado por Fabio Takwara é que essa forma é uma **primeira camada**, e que a missão pública do Acervo exige evoluir para uma **infraestrutura pública, coletiva, navegável e reutilizável de investigação**, sem que isso signifique descartar a curadoria já feita ou reescrever URLs que a comunidade já referencia.

A camada pública (`TakwaraTec-Acervo-Web`) já pratica o princípio: o mesmo corpus é navegado por `/fundamentos/`, `/evidencias/`, `/cadernos/`, `/cartilhas/`, `/metodologia/`. O desafio é fazer o **acervo científico** (`acervo-soberania-tecnologica`) alcançar o mesmo nível relacional sem migrar fisicamente centenas de arquivos.

## 2. Decisão

O Acervo passa a ser formalmente modelado como **grafo de entidades e relações** com:

- **entidades canônicas** (uma única ficha por pessoa, documento, tema, território, instituição e tecnologia);
- **relações semânticas** tipificadas (estuda, menciona, avalia, aplica, documenta, hipotetiza, corrobora, contradiz);
- **visões/gavetas** como **consultas** sobre essas entidades, não como coleções paralelas.

Essa evolução é feita por **camada relacional SOBRE o corpus atual**, não por migração física. As gavetas existentes permanecem; o que muda é a forma como o Acervo se descreve e o que ele promete ao leitor.

## 3. Princípio constitutivo

> O Acervo de Soberania Tecnológica não deve ser concebido apenas como coleção temática de documentos. Seu objetivo é evoluir para uma infraestrutura pública, coletiva, navegável e reutilizável de investigação, preservando rigor documental, proveniência e revisão humana.
>
> A arquitetura deve permitir **navegar pelo mesmo corpus por diferentes dimensões** sem duplicar a entidade canônica.
>
> **Gavetas e coleções são VISÕES dessas relações**, não cópias independentes do conhecimento.

## 4. Modelo de entidades (R1, conceitual)

```
DOCUMENTOS
     ↕
PESSOAS
     ↕
TEMAS
     ↕
TERRITORIOS
     ↕
INSTITUICOES
     ↕
TECNOLOGIAS
```

Para cada entidade serão especificados, sem implementação ainda:

- identificador estável;
- nome/título canônico;
- aliases;
- descrição curatorial;
- relações;
- fontes;
- estado documental;
- proveniência;
- datas;
- tags controladas;
- links internos (Acervo) e externos (fontes primárias);
- revisão, homologação;
- licença quando aplicável (mídia, fontes externas).

## 5. Modelo de relações (R1)

Relações muitos-para-muitos, com tipificação semântica. Exemplos:

| Origem | Relação | Destino |
|---|---|---|
| PESSOA | produziu | DOCUMENTO |
| PESSOA | vinculada_a | INSTITUICAO |
| PESSOA | atua_em | TEMA |
| DOCUMENTO | estuda | TEMA |
| DOCUMENTO | menciona | TERRITORIO |
| DOCUMENTO | avalia | TECNOLOGIA |
| INSTITUICAO | localizada_em | TERRITORIO |
| INSTITUICAO | pesquisa | TEMA |
| TECNOLOGIA | relacionada_a | DOCUMENTO |
| TECNOLOGIA | aplicada_em | TERRITORIO |

**Diferenciação semântica obrigatória:** mera **menção** em um documento não é **evidência** nem **validação**; é preciso distinguir `MENciona`, `ESTUDA`, `AVALIA`, `APLICA`, `DOCUMENTA`, `HIPOTETIZA`, `CORROBORA`, `CONTRADIZ`. A regra de não inflar TRL (TRL_BASE.md) e a regra de não promover proposta autoral como tecnologia aplicada (AGENTS_BASE.md) permanecem vinculantes.

## 6. Coleções como visões

Coleções (atuais e futuras) deixam de ser tratadas como coleções independentes e passam a ser tratadas como **consultas editoriais** sobre o grafo:

- `Ciência no Brasil` ↔ consulta por PESSOA com `nacionalidade=BR` ∧ relação produziu/vinculada_a DOCUMENTO.
- `Ciência no Mundo` ↔ mesma consulta sem filtro de nacionalidade.
- `Personagens Históricos` ↔ consulta por PESSOA com `categoria=histórica` ou `intervalo` definido.
- `Antiguidade` ↔ consulta por TEMAS / TERRITORIOS / PESSOAS com `intervalo` histórico.
- `Fundamentos`, `Bambu`, `PU Vegetal`, `Habitação`, `Agrofloresta` ↔ consultas por TEMA/TECNOLOGIA.

Uma mesma PESSOA canônica (ex.: Miguel Nicolelis) pode aparecer em múltiplas coleções sem duplicar ficha.

## 7. Três camadas do "Segundo Cérebro"

| Camada | Função | Localização |
|---|---|---|
| CAMADA_1 — ACERVO_CIENTIFICO | Registro canônico: fichas, entidades, relações, sínteses, estados documentais, rastreabilidade | `acervo-soberania-tecnologica/docs/` + `_privado/` (operacional) |
| CAMADA_2 — ACERVO_WEB | Mediação editorial: descoberta, narrativa, visualização, exploração, mapas, interação | `TakwaraTec-Acervo-Web/` (Astro) |
| CAMADA_3 — FONTES_CORPUS | Camada probatória: documentos integrais, DOIs, endpoints, arquivos, repositórios, fontes institucionais | Zenodo, repositórios externos, DOI.org, Crossref, OpenAlex, GBIF, INPE, MapBiomas, NASA POWER |

Fluxo público:

```
SITE → FICHA_CANONICA → FONTES_CORPUS
```

A camada 2 deve refletir a camada 1 sem importar nem duplicar; a camada 1 deve permitir que a camada 3 seja localizada com identificador estável (DOI/URL canônica).

## 8. Colaboração pública

Pipeline formalizado:

```
CONTRIBUICAO
     ↓
TRIAGEM
     ↓
IDENTIFICACAO
     ↓
PROVENIENCIA
     ↓
CANDIDATO
     ↓
REVISAO
     ↓
HOMOLOGACAO
     ↓
PUBLICACAO
```

Princípio: `CONTRIBUIR != PUBLICAR`. Contribuições futuras preveem: sugerir fonte, corrigir metadado, indicar pesquisador, indicar território, propor relação, enviar documento para triagem, contestar interpretação, complementar ficha. Nenhuma contribuição altera conteúdo homologado sem passar pelo pipeline.

## 9. Utilidade pública derivada do grafo

O Acervo deve permitir progressivamente:

- **LOCALIZAR** fontes por tema, território, material, método, autor, instituição;
- **COMPARAR** achados, métodos, limitações;
- **RELACIONAR** documentos, autores, tecnologias;
- **MAPEAR** territórios, instituições, redes;
- **IDENTIFICAR_LACUNAS** por cruzamento;
- **FORMULAR_PERGUNTAS** que o corpus responde e que ele deixa em aberto;
- **CRIAR_BIBLIOGRAFIAS** fundamentadas;
- **PROPOR_PESQUISA** a partir de lacunas;
- **ENCONTRAR_PESQUISADORES / INSTITUICOES / TERRITORIOS**;
- **CONTRIBUIR** com trilha auditável.

Objetivo público do grafo:

```
DOCUMENTO → COMPREENSÃO → RELAÇÃO → LACUNA → PERGUNTA → COLABORAÇÃO → NOVA_PESQUISA
```

## 10. Decisão sobre migração

**MIGRATION_BY_REFERENCE_FIRST** precede qualquer `MIGRATION_BY_MOVE`. Nenhuma migração física nesta missão. Nenhum arquivo renomeado. Nenhum diretório movido. Nenhuma URL pública quebrada. Nenhuma `nav` do MkDocs alterada. O que muda nesta missão é **documentação arquitetural** (este ADR e os três artefatos de suporte), não o corpus.

## 11. Consequências

### Positivas

- O Acervo pode expressar sua estrutura real sem reescrever centenas de arquivos.
- Coleções futuras podem ser geradas a partir de consultas, não de cópias.
- A camada Web pode refletir o grafo sem duplicar fichas.
- Contribuições públicas passam a ter lugar formal no pipeline.

### Riscos

- O ADR pode ser interpretado como autorização para mover arquivos. Mitigação: §10 explícita; auditoria de compatibilidade (ADR `AUDITORIA_COMPATIBILIDADE_ARQUITETURA_RELACIONAL_R1`).
- O modelo pode ser confundido com banco de dados operacional. Mitigação: §3 explicita que gavetas continuam sendo visões, não cópias; nenhum schema é implementado nesta missão.

## 12. Não-objetivos

- Não implementar schema.
- Não migrar arquivos.
- Não reescrever o MkDocs.
- Não abrir a camada 2 do Acervo Web sem ADR separado.
- Não substituir GOVERNANCA_DOCUMENTAL.md.
- Não introduzir dependências externas.

## 5. Identificadores — INTERNAL_STABLE_ID e EXTERNAL_IDENTIFIERS

Esta seção foi corrigida em R2_CORRECAO_P1 para fixar dois princípios vinculantes.

**INTERNAL_STABLE_ID — obrigatório.**

- É criado e governado pelo Acervo.
- É persistente.
- Não depende de fornecedor externo (DOI, ORCID, ROR, Wikidata, ISBN, etc.).
- Não depende de URL.
- Não depende de nome humano.
- Não muda quando metadados externos mudam.
- É a **chave canônica da entidade**.

Convenção conceitual proposta (sintaxe final a ser fixada por ADR_R2):

```
person:000001
document:000001
institution:000001
theme:000001
territory:000001
technology:000001
```

- `ID_NAMESPACE_REQUIRED=YES`.
- `ID_FORMAT_FINALIZED=NO` — a sintaxe final pode ser ajustada por ADR posterior, mas a **existência do ID interno é vinculante** desde R1.

**EXTERNAL_IDENTIFIERS — opcionais, múltiplos.**

ORCID, DOI, ROR, Wikidata QID, ISBN, ISSN, VIAF, ISNI e outros identificadores externos são formalizados como:

- `aliases`
- `crosswalks`
- `links externos`
- `chaves de reconciliação`
- `fontes auxiliares de identidade`

Eles **nunca** são a chave primária canônica da entidade. Em particular:

- `ORCID` é chave externa de pessoa, não chave primária.
- `DOI` é chave externa de documento, não chave primária.
- `ROR` é chave externa de instituição, não chave primária.
- `Wikidata QID` é chave externa de qualquer entidade, não chave primária.

**Web × Acervo (registrado como P2 futuro).**

`WEB_PROFILE_ID != INTERNAL_STABLE_ID`. A integração entre `profile.id` (Acervo Web) e `INTERNAL_STABLE_ID` (Acervo Científico) será objeto de ADR_WEB_R1; **não é implementada nesta rodada**.

**Documento × Pessoa — registrado como P2 futuro.**

`ENTITY_DOCUMENT != ENTITY_PERSON`. Cada uma terá identidade, schema, relações tipadas, estados compatíveis e proveniência próprias. O ADR_R2 futuro decidirá a coexistência detalhada.

## 6. Regra de captura de governança

> INSIGHT_HUMANO_APROVADO → FORMALIZACAO → GOVERNANCE_CAPTURE → ARTEFATO_VERSIONADO → COMMIT_ATOMICO → IMPLEMENTACAO

Princípios vinculantes registrados nesta seção (R2_CORRECAO_P1):

- `CHAT_HISTORY != INSTITUTIONAL_MEMORY`.
- `PRIVATE_HANDOFF != VERSIONED_GOVERNANCE`.

Toda decisão arquitetural, metodológica ou de taxonomia deve receber `GOVERNANCE_CAPTURE_REQUIRED=YES` e ser registrada em arquivo versionado — por exemplo, `docs/governanca/`, `README.md`, `GOVERNANCA_DOCUMENTAL.md`, ADR ou combinação apropriada.

## 7. Convenções de commits atômicos

**UM_INSIGHT_ESTRUTURAL = UM_LOTE_DE_GOVERNANCA.** Não misturar em um mesmo commit:

- governança
- migração
- UI
- fichamento
- conteúdo editorial

Exemplos de convenção:

```
docs(governance): promover ADRs R1 para área versionada e corrigir identificador interno
docs(schema): definir modelo conceitual de pessoa canônica R1
docs(contribution): definir pipeline público de contribuição
```

---

**Anexos deste ADR:**
- `FICHA_CANONICA_PESSOA_R1.md` — schema conceitual de PESSOA_R1.
- `MATRIZ_ENTIDADES_RELACOES_R1.md` — matriz entidades × relações.
- `PLANO_TRANSICAO_ACERVO_1_PARA_2_R1.md` — sequência sugerida de evolução (R0 → R1 → R2 → ...).
- `AUDITORIA_COMPATIBILIDADE_ARQUITETURA_RELACIONAL_R1.md` — auditoria de compatibilidade com governança atual.
