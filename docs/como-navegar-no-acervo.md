---
tipo_documental: documento-institucional
estado_documental: em-revisao-documental
data_revisao: 2026-08-10
responsavel_curadoria: Fabio Takwara
---

# Como navegar no Acervo

O **Acervo Soberania Tecnológica** reúne documentos de pesquisa, síntese e proposta sobre bambu, bioeconomia, tecnologias sociais e soberania tecnológica — produzidos por Fabio Takwara (Núcleo Takwara) e por autores de referência, com curadoria documental própria.

Nem todo documento sustenta a mesma coisa. Antes de citar ou usar um material, vale entender **o que ele pode e o que não pode sustentar**.

---

## Estados, natureza e situação de depósito

Cada documento público tem três atributos distintos. Eles **não** devem ser confundidos:

| Atributo | O que é | Valores |
|---|---|---|
| **Estado** | Grau de conferência da curadoria | `em-revisao-documental`, `homologado-documentalmente`, `historico` |
| **Natureza** | Tipo documental / classificação | `ficha-cientifica`, `estado-da-arte`, `visao-autoral`, `documento-institucional`, cartilha |
| **Situação de depósito** | Publicação no Zenodo | Zenodo publicado (com DOI) ou não publicado |

> `visao-autoral` é **natureza** (interpretação ou formulação autoral), não um estado de publicação. Um documento de natureza `visao-autoral` pode estar em `em-revisao-documental` ou `homologado-documentalmente`.

### Estados

| Estado | O que significa | Pode ser citado como evidência? |
|---|---|---|
| `em-revisao-documental` | Em curadoria ativa; conteúdo conferido, mas não homologado | Com cautela; hipóteses marcadas como tais |
| `homologado-documentalmente` | Revisão humana completa; versão editorial estável | Como documento conferido; não como validação experimental |
| `historico` | Registro de trajetória ou contexto | Como contexto, conforme sensibilidade |

> **Observação:** a publicação no Zenodo é um **evento de depósito**, não um estado de maturidade. Um documento depositado continua sujeito aos estados acima. Documentos em situação `protegido-privado`, `quarentena` ou `retirado-da-publicacao` **não** aparecem na árvore pública.

## As camadas do Acervo

| Camada | Exemplos | Pode sustentar | Não pode sustentar |
|---|---|---|---|
| **Visão geral / índices** | index.md das gavetas | Localização e orientação | Nada factual |
| **Estado da arte** | estado-da-arte.md (por gaveta) | Síntese curatorial com data de corte e corpus declarado | Novidade ou patenteabilidade |
| **Cadernos** | Cadernos 01–07 (visão do autor) | Rastreabilidade, hipóteses, propostas | Validação experimental |
| **Fichas científicas** | ficha-* (ex.: Chen 2015 Cu; Liu 2015 Pb) | O que o estudo primário reporta (com DOI e condições) | Generalização além do estudo |
| **Cartilhas autorais** | Bioeconomia 005; Fitorremediação 004 | Síntese, proposta, divulgação | Certificação, validação tecnológica, prova de patenteabilidade |
| **Documentos em revisão** | candidatas, rascunhos | Leitura crítica | Citação como fato |

## Percurso 1 — Leitor geral

Quer entender o que é o Acervo e a proposta da Plataforma Amazônia Regenerativa:

1. [Visão geral](index.md) — o que é o Acervo.
2. [Estado da arte do bambu estrutural](analyses/bambu-estrutural/estado-da-arte.md) — o que a literatura (corpus declarado) sustenta.
3. [Cadernos de Soberania Ecológica](analyses/visao-do-autor/index.md) — a visão autoral, com DOIs.

> Trate cartilhas e cadernos como **propostas autorais em revisão**, não como resultados validados.

## Percurso 2 — Leitor técnico

Quer verificar dados, métodos e fontes primárias:

1. [Estado da arte](analyses/bambu-estrutural/estado-da-arte.md) — ponto de partida, com data de corte e corpus.
2. [Fichas científicas](analyses/bambu-estrutural/index.md) — fichas com DOI, método, condições experimentais e proveniência.
3. Fontes primárias — acessíveis pelo DOI/URL citado na ficha.

> Confira **cada valor na fonte primária** (espécie × órgão × metal × unidade × método × tabela/página). Fichas em `em-revisao-documental` podem ter valores ainda não reconciliados com a fonte primária.

## Percurso 3 — Leitor autoral / propositivo

Quer usar o material como base para propostas, projetos ou redação:

1. [Cartilhas autorais](analyses/tecnologia-takwara/index.md) — propostas e sínteses (com ressalvas declaradas).
2. Declarações de limites — leia antes de replicar.
3. Hipóteses — identificadas como "hipótese/proposta", nunca como fato.
4. Documentos relacionados — cadernos e fichas citados.

> Marque como **hipótese** o que for hipótese e não afirme validação onde não existe. Parâmetros reservados (avaliação de propriedade intelectual) não estão na árvore pública.

## Limites da curadoria

O Acervo **não é**:

- certificação experimental, laudo técnico homologado ou reconhecimento institucional;
- prova de patenteabilidade — decisões de propriedade intelectual são tratadas em contrato próprio;
- revisão por pares do texto curatorial.

Homologação documental **não** significa replicação experimental nem elevação de TRL. Fontes não localizadas ou em paywall são marcadas como "não confirmado" — não há inferência por aproximação.

## Glossário rápido

| Termo | Significado |
|---|---|
| BAF | Bioaccumulation factor (conforme a fonte; não normalizar por inferência) |
| BCF | Bioconcentration factor |
| FT / TF | Fator de translocação / translocation factor |
| FBC | Fator de bioconcentração (equivalente em português, quando usado pela fonte) |
| TRL | Technology Readiness Level (nível de maturidade tecnológica) |
