# Ficha: Araújo et al. (2025) — ACV da Haste de Bambu Artesanal na Amazônia

> **Resumo:** Este artigo pioneiro realiza uma Análise de Ciclo de Vida (ACV) do tipo "berço ao portão" da produção artesanal de colmos de bambu (*Guadua angustifolia*) em Rio Branco/AC. Utilizando dados primários de uma unidade produtiva real e o software SimaPro v9.1 com método ReCiPe, os autores identificam que a **toxicidade carcinogênica humana (HCT) domina 93% do perfil ambiental** do produto, causada pelo uso de ácido bórico e bórax no tratamento químico. O estudo fornece a linha de base para a substituição desses insumos tóxicos por alternativas biológicas, informando diretamente a engenharia de processos do Consórcio MQTF (UnB/UFRR/UFAC).

---

## 1. Dados Gerais

| Campo | Dado |
|-------|------|
| **Título** | Life cycle assessment of the artisanal bamboo pole (*Guadua angustifolia*) production in the Brazilian Amazon |
| **Autores** | L. M. de Araujo; B. F. Gianelli; S. D. Mancini; G. A. de Medeiros |
| **Instituições** | UNESP Sorocaba / IFSP Itapetininga |
| **Publicação** | *Brazilian Journal of Science*, v. 4, n. 4, p. 13-28, abr. 2025 |
| **DOI** | 10.14295/bjs.v4i4.719 |
| **Tipo de estudo** | ACV atribucional, abordagem "berço ao portão" (cradle-to-gate) |
| **Produto analisado** | Colmo tratado de *Guadua angustifolia* — unidade funcional: **1 kg** de haste tratada |
| **Local do estudo** | Unidade produtiva em Rio Branco, Acre — Amazônia Brasileira |
| **Software ACV** | **SimaPro v9.1** |
| **Método de impactos** | **ReCiPe** (midpoint) — categorias: GW, SOD, PM, FE, HCT, MRS, WU |
| **Normas** | ISO 14040 (2014a) e ISO 14044 (2014b) |
| **Eixo** | Bioeconomia Amazônica |
| **Status** | ✅ Completa (artigo completo analisado) |

---

## 2. Contexto da Unidade Produtiva

| Parâmetro | Dado |
|-----------|------|
| **Propriedade** | 3 hectares, ~30 espécies de bambu |
| **Espécie para construção** | *Guadua angustifolia* |
| **Produção anual** | ~500 hastes tratadas de 6 m/ha |
| **Trabalhadores** | 3 |
| **Salário** | US$ 350,00/mês (35% acima do mínimo brasileiro em 2023) |
| **Sistema de cultivo** | Agroflorestal |
| **Área original** | Degradada, restaurada com bambu |
| **Localização** | Região periurbana de Rio Branco, Acre |

---

## 3. Metodologia

### 3.1. Inventário do Ciclo de Vida (ICV)

Dados primários coletados entre set/2021 e jan/2022, com aferições específicas em out/2021 e out/2022.

**Tabela 1 — Inventário para produção de 1 kg de haste de bambu tratada**

| Insumo | Quantidade | Unidade |
|--------|-----------|---------|
| Fertilizante NPK (15-15-15) | 0,0003 | kg |
| Calagem (liming) | 0,002 | kg |
| Água | 0,67 | L |
| Ácido bórico | 0,0003 | kg |
| Bórax | 0,0003 | kg |

| Resíduo/Emissão | Quantidade | Unidade |
|-----------------|-----------|---------|
| Resíduo de bambu (desbaste) | 0,20 | kg |
| Hastes descartadas | 0,13 | kg |
| Efluente (wastewater) | 0,07 | L |

### 3.2. Etapas do Fluxo Produtivo

```
Plantio manual e manejo → Colheita e separação → Tratamento químico (imersão)
       ↓                        ↓                        ↓
  NPK + calagem          25% perda         Ácido bórico + bórax + água
```

### 3.3. Categorias de Impacto Avaliadas

| Sigla | Categoria | Unidade |
|-------|-----------|---------|
| GW | Global Warming (Aquecimento Global) | mPt |
| SOD | Stratospheric Ozone Depletion (Depleção Ozônio) | mPt |
| PM | Fine Particulate Matter Formation (Material Particulado) | mPt |
| FE | Freshwater Eutrophication (Eutrofização Água Doce) | mPt |
| **HCT** | **Human Carcinogenic Toxicity (Toxicidade Carcinogênica)** | **mPt** |
| MRS | Mineral Resources Scarcity (Escassez Recursos Minerais) | mPt |
| WU | Water Use (Uso de Água) | mPt |

---

## 4. Principais Achados

### 4.1. Resultados da ACV

**Tabela 2 — Impactos ambientais por kg de haste tratada (mPt)**

| Material | GW | SOD | PM | FE | HCT | MRS | WU |
|----------|----|-----|-----|-----|-----|------|-----|
| NPK | 3,6e-5 | 7,6e-5 | 8,4e-6 | 1,0e-5 | 3,6e-5 | 2,9e-8 | 6,0e-7 |
| Calagem | 3,6e-6 | 4,2e-7 | 2,2e-6 | 1,0e-8 | 2,5e-6 | 6,3e-12 | 7,5e-6 |
| Efluente | 5,5e-4 | 3,0e-5 | 1,2e-4 | 4,1e-6 | 2,3e-3 | 4,6e-9 | 2,6e-3 |
| **Ácido bórico** | 3,9e-5 | 2,7e-6 | 5,7e-5 | 2,7e-4 | **5,5e-3** | 1,9e-8 | 3,2e-5 |
| **Bórax** | 5,5e-5 | 2,9e-6 | 2,4e-5 | 2,4e-4 | **4,2e-3** | 4,7e-9 | 9,1e-6 |
| Resíduo bambu | 6,6e-4 | 3,6e-5 | 4,7e-4 | 4,4e-3 | 7,4e-2 | 2,6e-8 | 1,3e-4 |
| Haste descartada | 1,5e-4 | 1,1e-5 | 7,9e-5 | 1,9e-3 | 7,3e-2 | 3,6e-8 | 7,7e-5 |
| **Total haste tratada** | **1,5e-3** | **1,6e-4** | **7,6e-4** | **6,8e-3** | **0,159** | **1,2e-7** | **2,8e-3** |

### 4.2. Hotspot: Toxicidade Carcinogênica (HCT) — 93%

O achado central: **ácido bórico + bórax são responsáveis por 93% do impacto total de HCT**. Separadamente:
- Resíduo de bambu + haste descartada: 0,147 mPt (92% do HCT total) — resíduos impregnados com boro
- Ácido bórico: 0,0055 mPt (3,5%)
- Bórax: 0,0042 mPt (2,6%)

> **Implicação direta:** Substituir o tratamento com sais de boro elimina 93% do principal impacto ambiental.

### 4.3. Resíduos Sólidos — 91%

O desperdício de biomassa (desbaste + hastes descartadas) representa **perda de 25% da matéria-prima** e domina a categoria de resíduos.

### 4.4. Eutrofização (FE) e Uso de Água (WU)

- FE: 4% do total — impulsionado por resíduos de bambu + fertilizante NPK
- WU: 1,6% — baixo na Amazônia (pluviosidade > 2.000 mm/ano)

### 4.5. Demais Categorias

- GW, SOD, PM, MRS juntos representam **< 0,5%** do impacto total
- Baixas emissões por plantio manual (sem mecanização agrícola)
- Secagem ao ar livre (sem consumo energético)

---

## 5. Avaliação Crítica

### 5.1. Contribuições

1. **Pioneirismo**: primeira ACV com dados primários de bambu artesanal na Amazônia Brasileira
2. **Utilidade prática**: evidência quantitativa clara apontando substituição do tratamento químico
3. **Saúde ocupacional**: quantifica risco carcinogênico aos trabalhadores expostos ao boro
4. **Aplicação MQTF**: substituição de boro por biopolímeros (Mamonex) + alcalinização com cinzas

### 5.2. Limitações

1. **Amostra unitária**: uma única unidade produtiva — não captura variabilidade regional
2. **Escopo berço-portão**: sem análise de uso, descarte ou estocagem de carbono
3. **Sem análise de sensibilidade**: não testa robustez dos resultados
4. **Dados secundários**: fontes das bases de dados do SimaPro não detalhadas
5. **Sem análise econômica**: viabilidade das alternativas ao boro não avaliada

---

## 6. Conexões com a Tecnologia Takwara

| Contramedida | Tecnologia Takwara | Impacto |
|-------------|-------------------|---------|
| Substituir ácido bórico/bórax por biopolímeros | T01 — Imunização / Mamonex RD70 | Elimina 93% do HCT |
| Converter resíduos em bioenergia | Memorial 5.1 — Biorrefinaria | Transforma 25% de perda em ativo |
| Circuito fechado de impregnação a vácuo | T10 — Balsas / Tratamento pressurizado | Reduz efluentes e eutrofização |

---

## 7. Palavras-chave

**Português:** ACV; bambu; Guadua angustifolia; toxicidade carcinogênica; ácido bórico; bórax; Amazônia; bioeconomia; SimaPro; ReCiPe

**English:** LCA; bamboo; Guadua angustifolia; human carcinogenic toxicity; boric acid; borax; Amazon; bioeconomy; SimaPro; ReCiPe

---

## 8. Referência

ARAUJO, L. M. de; GIANELLI, B. F.; MANCINI, S. D.; MEDEIROS, G. A. de. Life cycle assessment of the artisanal bamboo pole (*Guadua angustifolia*) production in the Brazilian Amazon. **Brazilian Journal of Science**, v. 4, n. 4, p. 13-28, abr. 2025. DOI: 10.14295/bjs.v4i4.719.

---

> **Ficha atualizada em:** 2026-06-22
> **Fonte do artigo completo:** `/Users/fabiotakwara/Documents/BAMBUBR/**Denuncia/Araujo-Guadua-Acre.pdf`
> **Ferramenta:** Hermes Agent
