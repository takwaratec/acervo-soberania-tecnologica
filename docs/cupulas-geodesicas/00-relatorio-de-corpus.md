---
schema: ACERVO_RELATORIO_CORPUS_R1
eixo: cupulas-geodesicas
frente: CUP-GEO-CORPUS-20261128-R1
tipo_documental: relatorio-de-corpus
eixo_pai: null
estado_documental: em-revisao-documental
homologacao_automatica: false
release: R4-em-curso
data_apuracao: 2026-11-28
responsavel_curadoria: Fabio Takwara
assistencia_documental: agente de IA, sujeito a revisao humana
---

# Cúpulas Geodésicas — relatório de corpus

**Eixo próprio.** Bambu estrutural é subdivisão do eixo bambu; cúpulas geodésicas é estudo
à parte, com gaveta própria e fichas próprias, e **referência cruzada** ao eixo bambu por
arquivo-stub.

**Fase:** revisão documental. Não é homologação, não é Release 2. A R4 está em curso; o
Release 2 será o congelamento do repositório homologado ao final dela.

**O que este documento é:** apuração de **o que existe** de fato, com nome de arquivo, tamanho e
estado. **O que ele não é:** curadoria — nenhuma ficha foi reescrita, nenhuma fonte foi
reprocessada, nada foi movido.

---

## 1. O achado que redimensiona o corpus

**As fichas de cúpula não estão na gaveta da frente. Estão em `docs/analyses/fundamentos/`.**

A herança `DOM-HAB-R1` tem 10 fichas em `09_fichas/`, mas **a curadoria publicada do acervo as
espalhou por outras gavetas**, sob nomenclatura de autor:

| fonte | onde a ficha vive hoje | nomenclatura |
|---|---|---|
| Fuller 1954 (patente US2682235A) | `docs/analyses/fundamentos/fuller-1954-building-construction.md` | autor–ano–tema |
| South 1979 (patente US4155967A) | `docs/analyses/fundamentos/south-1979-building-structure-method.md` | autor–ano–tema |
| Park et al. 2022 (vento em domos) | `docs/analyses/fundamentos/park-et-al-2022-wind-pressure-spherical-domes.md` | autor–ano–tema |
| Faghih & Bahadori 2011 (térmica) | `docs/analyses/fundamentos/faghih-bahadori-2011-thermal-performance-domed-roofs.md` | autor–ano–tema |
| González-Avilés et al. 2024 (energia) | `docs/analyses/fundamentos/gonzalez-aviles-et-al-2024-energy-benefits-geodesic-domes.md` | autor–ano–tema |
| Mncwango & Allopi 2019 (EPS) | `docs/analyses/fundamentos/mncwango-allopi-2019-expanded-polystyrene-dwellings.md` | autor–ano–tema |
| FEMA P-361 2021 (safe rooms) | `docs/analyses/fundamentos/fema-2021-safe-rooms-tornadoes-hurricanes.md` | **instituição**–ano–tema |
| Santos 2021 (cúpula geodésica, análise numérica) | `docs/analyses/fundamentos/santos-2021-cupula-geodesica-analise-numerica.md` | autor–ano–tema |

**Consequência direta:** o Relatório não propõe "mover 10 fichas para a gaveta nova". Propõe
**criar stubs** na gaveta de cúpulas que apontam para as fichas existentes, e **produzir ficha
própria** só do que ainda não tem nenhuma.

**Duas fichas da herança não foram encontradas em `docs/analyses/`** — precisam ser procuradas
antes de qualquer decisão: Velasco Vega 2023 (que existe em `docs/frentes-documentais/dom-hab-r1/
fichas/`, caminho legado) e a ficha de Park com o código `A03-S1`, que aparece com **nome trocado**
na publicação (`A03-S1` na herança × `Park 2022` no acervo — o mesmo conteúdo, dois nomes).

---

## 2. A herança do Release 1 (DOM-HAB-R1) — inventário real

**917 arquivos, 317 MB.** Estado declarado na governança: *"PESQUISA DOCUMENTAL E PREPARAÇÃO DE
AQUISIÇÃO concluída — PRÓXIMO GATE: aquisição A01–A08, aguarda autorização"*.

### 2.1 Catálogo mestre — 29 fontes, seis blocos

| bloco | fontes | tema |
|---|---|---|
| `A_HISTORIA_PATENTES` | 3 | Fuller 1954, South 1979, primeiro domo monolítico 1976 |
| `B_ENGENHARIA_ESTRUTURAL` / `B_TERMICA` / `B_ENERGIA_GEODESICA` / `B_THIN_SHELL` | 5 | Montes & Fernandez 2001, Faghih 2011, González-Avilés 2024, Velasco Vega 2023 |
| `C_EVENTOS_EXTREMOS` | 4 | FEMA P-361 2021, Dome of a Home 2004-05, Aso Farm Land 2016 (Kumamoto), FEMA HMGP |
| `D_MATERIAIS` (EPS, Japão, fogo, PU vegetal) | 5 | Japan Dome House, DOE/ORNL 30 anos, IBC cap. 26 + ASTM E84, **gavetas PU vegetal** |
| `E_REGULACAO` | 6 | Freddie Mac 5601.12, Fannie Mae B4-1.3, IRC 2018 Apêndice, Banks County GA, Burleigh County ND, HUD/RVIA |
| `F_MIDIA` | 7 | imagens históricas, Fuller Fly's Eye, vídeos de montagem |

**A cobertura regulatória é o ativo mais forte da herança** — seis fontes sobre financiamento
imobiliário e zoneamento norte-americano, tema que a frente de hoje **não tocou**.

### 2.2 Binários em disco — 12 arquivos com extensão `.pdf`, dos quais **10 são PDF e 2 não**

| arquivo | tamanho | estado |
|---|---|---|
| `A01_US2682235A_Fuller_Building_construction.pdf` | 1,41 MB | ok |
| `A02_US4155967A_South_Building_structure.pdf` | 0,89 MB | ok |
| `A03-S1_Jiang_2022_Numerical_Wind_Spherical_Structures.pdf` | 9,76 MB | ok |
| `A04-S1_Faghih_Bahadori_2011_WREC_Thermal_Performance_Domed_Roofs.pdf` | 1,58 MB | ok |
| `A05_Gonzalez-Aviles_2024_Energy_Benefits_Geodesic_Domes.pdf` | 2,54 MB | ok |
| `A06-S1_Velasco_Vega_2023_Thermal_Performance_Thin_Shell_Concrete_Domes.pdf` | 41,62 MB | ok |
| `A07_Mncwango_2019_Laboratory_Investigation_Appraisal.pdf` | 3,63 MB | ok |
| `A08_FEMA_P361_2021_Safe_Rooms_Tornadoes_Hurricanes.pdf` | 22,69 MB | ok |
| `P03-01_Castor_Oil_PU_Bamboo_Charcoal_Polymers_2018.pdf` | 2,98 MB | ok |
| `P03-02_Bamboo_Fibre_PU_Foam_BioResources_2026.pdf` | 0,90 MB | ok |
| **`P01-01_ICC_500_2020_Highlights_FEMA.pdf`** | **481 bytes** | **ARQUIVO VAZIO** — não é PDF |
| **`P02-02_Burleigh_County_Zoning_Ordinance_2016.pdf`** | **95 bytes** | **ARQUIVO VAZIO** — não é PDF |

**Os dois últimos são placeholders de uma coleta que falhou e foram contados como se fossem fonte.**
Isso é o tipo de defeito que a custódia de binários da R4 existe para pegar: **hash de arquivo de
95 bytes "passa" em qualquer contagem e não é fonte.**

### 2.3 Fichas na herança — 10 em `09_fichas/`, 2 também em `12_sintese/` como candidatas V2

Nomenclatura da herança: `FICHA_A01_Fuller_US2682235A.md`, `FICHA_P03-02_Bamboo_Fibre_PU_Foam.md` —
**prefixo de código de endpoint**, não sobrenome de autor. É exatamente o padrão que o protocolo R4
substitui.

### 2.4 O que a herança produziu além das fichas (58 arquivos em `12_sintese/`, ~1,9 MB)

| família | arquivos | o que são |
|---|---|---|
| **artigo de revisão** | 5 versões + `PUBLICATION_ARCHITECTURE.md` | `PUBLICATION_MASTER_R2` (72 KB) é a mais avançada |
| **estado da arte** | `ESTADO_DA_ARTE_DOMOS_BAMBU_PU_FINAL` (53 KB) + candidata V2 | consolidado |
| **resenha autoral** | 4 versões (21 a 41 KB) | `RESENHA_AUTORAL_EXECUTIVA…V3_FINAL_CANDIDATE` (41 KB) |
| **ensaio autoral** | `ENSAIO_AUTORAL_DOMOS_BAMBU_PU_TAKWARA_FINAL` (41 KB) | texto assinado |
| **governança editorial** | `DO_NOT_SAY_REGISTER`, `CLAIM_STATUS_SUMMARY`, `EDITORIAL_FACTCHECK_MATRIX` (18 KB), `ESTADO_DA_ARTE_EVIDENCE_MATRIX` | **matrizes de rastreabilidade** |
| **história** | `HISTORICAL_GENEALOGY_DOMES_V1`, `HISTORICAL_DOME_SOURCE_REGISTER_V1`, `HISTORICAL_CLAIM_MATRIX_V1`, `ANEXO_SUPORTE_HISTORICO_DOMOS_V1` | genealogia e registro de fontes |
| **Zenodo** | `ZENODO_BIBLIOGRAPHIC_AUDIT_V1` (**26,8 KB**), `ZENODO_NORMATIVE_AUDIT_V1`, metadados V1/V2, appendices, gate checklist, 5 matrizes de traceabilidade | **aparelho de publicação completo** |
| **lacuna declarada** | `RIPPER_LILD_SOURCE_GAP_REGISTER.tsv` | 4 lacunas P0 do LILD |
| **normas** | `TAKWARA_STANDARDS_REVIEW.tsv` | revisão de normas |

### 2.5 Três achados de alto valor que a frente de hoje **não tinha**

1. **`DO_NOT_SAY_REGISTER.md`** — nove formulações proibidas, com a substituição correta de cada
   uma: *"FEMA certified domes for 250 mph"* → proibido; *"domes are hurricane-proof"* → proibido;
   *"Takwara system is structurally validated"* → proibido, porque `TAKWARA_SYSTEM_VALIDATED=NO`.
   **A frente de hoje reescreveu artigos sem consultar este registro.**
2. **`RIPPER_LILD_SOURCE_GAP_REGISTER.tsv`** — quatro lacunas P0 do LILD, com o item exato a
   obter: IASS-SLTE 2014 (Ripper et al., *Puc-Rio Bamboo Domes*, pp. 1-12), a tese de **Lucas
   Alves Ripper 2015** (230 f.), e o artigo de Moreira et al. sobre domos geodésicos do LILD.
   **A varredura de ontem chegou perto disso pelo ResearchGate e parou; a lacuna já estava
   registrada há três meses.**
3. **`ZENODO_BIBLIOGRAPHIC_AUDIT_V1.tsv`** — **69 referências auditadas**, e
   **`ZENODO_NORMATIVE_AUDIT_V1.tsv`** — 22 normas. **A varredura de normas de ontem cobriu campo
   que já tinha auditoria.**

---

## 3. O que a frente desta semana acrescenta

| bloco | artefatos | estado |
|---|---|---|
| **geometria** | série V1–V6 (8 células), icosaedro truncado medido, nomenclatura V/L/T, plano de corte da V5 | **medido e com gate** (16/16) — não depende de fonte externa |
| **calculadora** | `CALCULADORA_DOMOS_ALMANAQUE_R1.html`, `calc_domos.py`, gate | artefato de revisão humana — **vai para o acervo, não para o Web** |
| **varredura de normas** | 5 blocos, vigência conferida, respostas a 5 perguntas | 28/11/2026, com [V]/[S] |
| **varredura de ACV** | ~30 estudos com DOI resolvido no Crossref | 28/11/2026 |
| **varredura de conexões** | 20 achados; Ripper/LILD, patente 1994, Seixas/HFC, Barth 2016 | 28/11/2026 |
| **protocolos de ensaio** | empuxo de colmo (150 corpos), PU vegetal (E-A/E-B/E-C), fogo e junta amortecida | três documentos, gate 77/77 no do empuxo |
| **artigos** | denso (3.037 palavras), blog (1.311), gabinete (1.269) | **rascunho**, auditado pelo Teco com veredito REPLANEJAR |
| **achados novos** | Barth 2016 (12 m / 105 m² / < 5 h / conector flexível); Salcido 2016 (ACV de domo reticulado); NBR 17043:2023; NSR-10 G.9.3(c) | **não estavam na herança** |

---

## 4. Sobreposição — o que é ficha própria e o que é stub

| fonte/tema | já tem ficha publicada? | decisão |
|---|---|---|
| Fuller, South, Park, Faghih, González-Avilés, Mncwango, FEMA, Santos 2021 | **sim**, em `fundamentos/` | **stub** na gaveta nova |
| Velasco Vega 2023 | **sim**, em `frentes-documentais/dom-hab-r1/fichas/` (legado) | stub + migrar para `fundamentos/` |
| Ostapiv 2018, Geiss 2018 (cúpulas geodésicas) | **não** em `docs/analyses/`; existem em `_privado/fontes-documentais/bambusc-20261119/` como pacote | **ficha própria** — é fonte de cúpula, não de bambu genérico |
| Seixas 2024 (HFC), Moreira, Barth 2016, Salcido 2016, Gaffuri 2023, van Wassenhove 2021 | **não** | **ficha própria** |
| Ripper / LILD (IASS-SLTE 2014, tese 2015, patente PI9403412-5) | **não** — e é lacuna P0 registrada | **ficha própria**, com a lacuna mantida até obter |
| normas (NBR 16828-1/-2, NBR 17043, NBR 6123, E.100, NSR-10, ISO 22157, ISO/WD 26546) | **não** | **ficha por norma** |
| boro, PU vegetal, bambu estrutural (conteúdo) | **sim**, nas gavetas `boro/`, `pu-vegetal/`, `bambu-estrutural/` | **stub** — cúpula não duplica conteúdo de bambu |

---

## 5. O ensaio autoral e o DOI Zenodo — situação verificada

**Não existe DOI Zenodo.** O soberano supôs que o ensaio autoral já está publicado; verifiquei:
`ZENODO_METADATA_DRAFT_V2.md` declara textualmente
`PUBLICATION_STATUS=CANDIDATE_ONLY (Não submetido / Não publicado / Sem DOI gerado)`, e a busca
por `10.5281/zenodo.*` em **todos os 58 arquivos de `12_sintese/`** não retornou nenhuma
ocorrência.

**O que existe é o aparelho de publicação pronto:** metadados V1 e V2 em esquema InvenioRDM (título,
subtítulo, autor com ORCID `0009-0002-6044-2583`, contribuidor de IA), dois appendices de links
públicos, gate checklist e cinco matrizes de traceabilidade. **Falta o depósito.**

**Consequência:** a frase do soberano — *"a gente vai republicar"* — vira, na prática, **publicar
pela primeira vez**, o que é mais simples e mais exigente: o `PUBLICATION_MASTER` ainda precisa de
reconciliação com o que a frente desta semana apurou.

---

## 6. O que o corpus **não** tem — lacunas com escopo declarado

| lacuna | escopo da busca | estado |
|---|---|---|
| **ACV de estrutura espacial de bambu efêmera** berço-ao-túmulo, com desmontagens declaradas | PT/EN/ES, ~30 estudos, DOI via Crossref | **não localizada** — a de Salcido é cenário, berço ao portão |
| **norma de domo geodésico de bambu como sistema** | ABNT, ISO, ASTM, EN, GB, IS, NEC, NSR-10, E.100 | **não localizada**; a NSR-10 G.9.3(c) cobre cúpula geodésica genérica |
| **ensaio de empuxo de colmo oco** | idem | **não localizado**; só ISO/WD 26546 em rascunho |
| **norma brasileira de incêndio para bambu** | ABNT | **não existe**; NBR 16828-1 remete a outros materiais |
| **ciclagem de montagem em colmo inteiro** | PT/EN/ES | melhor publicado: **4 ciclos**, fadiga fora do escopo |
| **IASS-SLTE 2014, tese de Lucas Ripper 2015, Moreira et al.** | registrados como P0 em setembro | **ainda não adquiridos** |
| **artigo chinês** | CNKI inacessível | **não localizado — limitação, não ausência** |

---

## 7. O que o reprocessamento pela R4 vai ter de resolver

Ordem sugerida, e cada item depende do anterior:

1. **Triagem das 29 fontes do catálogo mestre** — quais viram ficha própria de cúpula, quais viram
   stub, quais já estão publicadas em outra gaveta.
2. **Custódia dos binários** — os 10 PDFs válidos ganham hash; os **2 placeholders são marcados
   como falha de coleta** e não entram como fonte.
3. **Regeração das 10 fichas da herança** no molde R4 (sobrenome de autor), com reconciliação
   contra as que já estão publicadas em `fundamentos/`.
4. **Fichas novas** do que a frente desta semana trouxe e não tem ficha (Seixas, Barth, Salcido,
   Ripper/LILD, normas).
5. **Stubs de referência cruzada** para as gavetas de bambu, boro e PU vegetal.
6. **Reconciliação do aparelho editorial** — `DO_NOT_SAY_REGISTER`, `EDITORIAL_FACTCHECK_MATRIX` e
   `ZENODO_BIBLIOGRAPHIC_AUDIT_V1` são a régua que os artigos novos têm de passar.
7. **Só então** a reescrita do artigo e o depósito Zenodo.

---

## 8. Três decisões que este relatório pede

1. **Velasco Vega e Park têm dois nomes** (código de endpoint na herança, autor–ano no acervo).
   Padronizo pelo autor–ano e registro o código como sinônimo, ou mantenho os dois?
2. **Os dois PDFs vazios** (481 e 95 bytes) — recolo na lista de aquisição pendente, ou o senhor
   quer que eu tente baixar de novo agora?
3. **As 4 lacunas P0 do LILD** já registradas em setembro e ainda não adquiridas: entram no
   programa de aquisição da R4 como prioridade, ou o senhor tem os arquivos em algum lugar?
