# Matriz Entidades × Relações R1

> **STATUS:** PROPOSTA_ARQUITETURAL_R1 (conceitual, NÃO implementada)
> **IMPLEMENTACAO:** NAO_AUTORIZADA
> **MIGRACAO:** NAO_AUTORIZADA
> **Origem:** INSIGHT_HUMANO_HOMOLOGADO_POR_FABIO_TAKWARA
> **Missão:** ACERVO_ARQUITETURA_RELACIONAL_R1
> **Versão pública (versão rastreada):** R1 (2026-09-18)
> **Vinculado a:** este diretório `docs/governanca/` é a versão **rastreada e auditável**; original operacional em `_privado/governanca-operacional/`.

---

# MATRIZ_ENTIDADES_RELACOES_R1

> **Status:** CANDIDATO · GOVERNANCE_CAPTURE_REQUIRED=YES
> **Origem:** INSIGHT_HUMANO_HOMOLOGADO_POR_FABIO_TAKWARA
> **Vinculado a:** `adr-acervo-arquitetura-relacional-r1.md`
> **Localização:** `_privado/governanca-operacional/MATRIZ_ENTIDADES_RELACOES_R1.md`
> **Data:** 2026-09-18
> **Escopo:** schema conceitual; NÃO IMPLEMENTAR.

## 1. Entidades canônicas (R1)

| Código | Entidade | Definição operacional | Identificador |
|---|---|---|---|
| PERSON | Pessoa | Pessoa física (autor, pensador, liderança, personagem histórico) com ficha documental | slug estável, ex.: `person:montaigne-1533` |
| DOCUMENT | Documento | Documento com fonte primária verificável: artigo, tese, livro, relatório, norma, página autoral | DOI/ISBN/ISSN quando existir; senão slug interno |
| THEME | Tema | Tópico de investigação, eixo curatorial, categoria temática | slug controlado pelo vocabulário curatorial |
| TERRITORY | Território | Lugar físico, recorte geográfico, bioma, município, estado, país, região cultural | código IBGE/ISO quando aplicável |
| INSTITUTION | Instituição | Organização pública, privada, acadêmica, comunitária, governamental | ROR / CNPJ / Wikidata QID |
| TECHNOLOGY | Tecnologia | Tecnologia, técnica, método, processo, material com cadeia de evidência rastreável | slug curatorial |

## 2. Tipos de relação (R1)

Cada relação é um verbo semântico. Cada ocorrência carrega evidência (fonte) e proveniência (camada: FATO_DOCUMENTADO / INTERPRETACAO_DE_FONTE / SINTESE_CURATORIAL / HIPOTESE / LACUNA).

### 2.1 Relações de PESSOA

| Origem | Relação | Destino | Notas |
|---|---|---|---|
| PESSOA | `produziu` | DOCUMENT | autoria ou coautoria |
| PESSOA | `co-produziu` | DOCUMENT | coautoria secundária ou institucional |
| PESSOA | `vinculada_a` | INSTITUTION | filiação institucional ou vínculo declarado |
| PESSOA | `formada_por` | INSTITUTION | formação acadêmica formal |
| PESSOA | `orientada_por` | PESSOA | relação acadêmica explícita |
| PESSOA | `influenciada_por` | PESSOA | declarada pelo próprio autor ou por fonte autoral |
| PESSOA | `influenciou` | PESSOA | declarada por fonte autoral |
| PESSOA | `atua_em` | THEME | eixo declarado pelo próprio autor |
| PESSOA | `nascida_em` | TERRITORY | verificável em fonte autoral/institucional |
| PESSOA | `atuou_em` | TERRITORY | atuação principal declarada |
| PESSOA | `falecida_em` | TERRITORY | verificável em fonte autoral/institucional |

### 2.2 Relações de DOCUMENT

| Origem | Relação | Destino | Notas |
|---|---|---|---|
| DOCUMENT | `estuda` | THEME | tema central da obra |
| DOCUMENT | `menciona` | THEME | citação sem centralidade |
| DOCUMENT | `menciona` | TERRITORY | citação sem centralidade |
| DOCUMENT | `menciona` | PERSON | citação sem centralidade |
| DOCUMENT | `documenta` | TERRITORY | foco documental do trabalho |
| DOCUMENT | `avalia` | TECHNOLOGY | ensaio, revisão, normalização |
| DOCUMENT | `aplica` | TECHNOLOGY | aplicação direta |
| DOCUMENT | `corrobora` | DOCUMENT | confirmação por outro documento |
| DOCUMENT | `contradiz` | DOCUMENT | divergência declarada |
| DOCUMENT | `hipotetiza` | TECHNOLOGY | hipótese ainda não confirmada |
| DOCUMENT | `produzido_por` | INSTITUTION | autoria institucional |

### 2.3 Relações de TECHNOLOGY

| Origem | Relação | Destino | Notas |
|---|---|---|---|
| TECHNOLOGY | `relacionada_a` | DOCUMENT | bibliografia primária |
| TECHNOLOGY | `aplicada_em` | TERRITORY | caso de aplicação verificado |
| TECHNOLOGY | `desenvolvida_por` | INSTITUTION | autoria institucional |
| TECHNOLOGY | `vinculada_a` | TECHNOLOGY | cadeia técnica |
| TECHNOLOGY | `desenvolvida_por` | PERSON | autoria individual explícita |

### 2.4 Relações de INSTITUTION

| Origem | Relação | Destino | Notas |
|---|---|---|---|
| INSTITUTION | `localizada_em` | TERRITORY | sede ou base principal |
| INSTITUTION | `pesquisa` | THEME | linha declarada |
| INSTITUTION | `produz` | DOCUMENT | autoria institucional |
| INSTITUTION | `responsável_por` | TECHNOLOGY | detentora formal ou desenvolvedora |

### 2.5 Relações de TERRITORY

| Origem | Relação | Destino | Notas |
|---|---|---|---|
| TERRITORY | `contém` | TERRITORY | relação hierárquica |
| TERRITORY | `estudado_em` | DOCUMENT | documento dedicado |
| TERRITORY | `aplicação_de` | TECHNOLOGY | aplicação territorial verificada |

## 3. Princípio de diferenciação semântica

A escolha do verbo é vinculante. Em particular:

- **`menciona`** é diferente de **`estuda`**, **`documenta`**, **`avalia`**, **`aplica`**. Uma citação incidental não é evidência; é contexto.
- **`corrobora`** é diferente de **`contradiz`**. Confirmação declarada e divergência declarada são ambas evidências, mas exigem leitura crítica diferente.
- **`hipotetiza`** exige etiqueta explícita: a ficha deve indicar que aquela relação é HIPOTESE, não FATO.
- **`aplicada_em`** exige verificação documental: não basta aparecer em propaganda comercial, tem de aparecer em ficha documental ou em laudo com fonte primária.

A camada de origem (FATO_DOCUMENTADO / INTERPRETACAO_DE_FONTE / SINTESE_CURATORIAL / HIPOTESE / LACUNA) é registrada para cada aresta do grafo, não só para os nós.

## 4. Cardinalidades

- PESSOA ↔ DOCUMENT: muitos-para-muitos (uma pessoa produz/co-produz vários documentos; um documento tem vários co-autores).
- PESSOA ↔ INSTITUTION: muitos-para-muitos (uma pessoa pode estar vinculada a várias instituições; uma instituição tem várias pessoas).
- PESSOA ↔ THEME: muitos-para-muitos.
- DOCUMENT ↔ THEME: muitos-para-muitos (um documento estuda um tema central e menciona outros; um tema é estudado por muitos documentos).
- DOCUMENT ↔ TERRITORY: muitos-para-muitos.
- DOCUMENT ↔ TECHNOLOGY: muitos-para-muitos.
- TECHNOLOGY ↔ TERRITORY: muitos-para-muitos.
- INSTITUTION ↔ TERRITORY: muitos-para-muitos (uma instituição pode estar em vários lugares; um lugar tem várias instituições).
- INSTITUTION ↔ THEME: muitos-para-muitos.
- TECHNOLOGY ↔ TECHNOLOGY: muitos-para-muitos (relacionada_a, vinculada_a).

## 5. Identificadores estáveis — política

A prioridade de identificador é:

1. **DOI** quando existir (documento).
2. **ORCID** quando existir (pessoa).
3. **ROR** quando existir (instituição).
4. **Wikidata QID** quando existir (qualquer entidade).
5. **ISBN / ISSN / Handle** quando existir (documento).
6. **Slug curatorial** próprio do Acervo, como fallback.

O slug curatorial deve ser estável: nunca reaproveitado para entidade diferente. Mudança de slug implica migração rastreável e não silenciosa.

## 6. Cardinalidade mínima para uma ficha PESSOA R1 apta

Para que uma ficha PESSOA_R1 seja aceita como entidade canônica no grafo, ela deve ter:

- pelo menos uma `produziu` ou `vinculada_a` registrada;
- pelo menos uma fonte primária ou institucional em `FONTES_PRIMARIAS` ou `FONTES_INSTITUCIONAIS`;
- a camada de origem marcada para todas as arestas factuais.

Caso contrário, a entidade entra como `rascunho` e não é navegável por coleções.

## 7. Não-objetivos

- Não implementar schema.
- Não migrar dados.
- Não decidir nomes de vocabulários controlados nesta missão (próximo ADR_R2).
