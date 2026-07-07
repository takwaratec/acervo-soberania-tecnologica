---
tipo: Ficha Técnica de Tecnologia Social
tecnologia: Especificações Técnicas para Domos Geodésicos
autor: Fabio Takwara
instituicao: Tecnologia Takwara
data: 2026-06-27
status: Consolidado
licenca: CC BY 4.0
---

# Ficha Técnica: Especificações Técnicas para Domos Geodésicos

## 1. Identificação

**Título:** Especificações Geométricas Detalhadas para Cúpulas Geodésicas  
**Campo de Aplicação:** Projeto e construção de domos geodésicos (bambu, aço, madeira, outros materiais)  
**Base Teórica:** Sólidos Platônicos (Icosaedro, Cubo, Octaedro, Dodecaedro, Tetraedro), frequências V1–V6, truncagens  
**Escopo:** Coeficientes de comprimento de vareta, quantidades, ângulos de vértice e variância para diferentes frequências

## 2. Descrição

Compilação de dados geométricos para projeto de cúpulas geodésicas baseadas em sólidos platônicos. Inclui coeficientes de comprimento de vareta (normalizados para raio = 1.000), ângulos de dobra, total de varetas, tipos de varetas e variância para frequências V1 a V6.

### Escolha do Poliedro Base

- **Icosaedro:** O mais versátil e eficiente; baixa variância de vareta; recomendado para maioria dos projetos
- **Cubo:** Variância mais alta; adequado para frequências altas com variantes concatenadas (2V.3V reduz variância)
- **Octaedro:** Simplicidade em baixas frequências; variância deteriora rapidamente com frequência
- **Dodecaedro:** Variantes L1/L2 com boa uniformidade; L2T com variância extrema (113%)
- **Tetraedro:** Maior variância (L3T: 126%); uso prático limitado

## 3. Parâmetros Técnicos (Icosaedro — Principais Configurações)

| Frequência | Truncagem | Total Varetas | Tipos | Variância | Altura (% Diâmetro) |
|:----------|:----------|:-------------|:-----|:---------|:-------------------|
| V1 | 2/3 | 25 | 1 | 0% | 72,36% |
| V2 | 1/2 | 65 | 2 | 13,1% | 50,00% |
| V3 | 3/8 | 120 | 3 | 18,3% | 41,42% |
| V3 | 5/8 | 165 | 3 | 18,3% | 59,38% |
| V4 (L3) | 1/2 | 250 | 5 | 17,8% | 50,00% |
| V4 | 1/2 | 250 | 6 | 28,3% | 50,00% |
| V5 | 7/15 | 350 | 9 | 32,1% | 44,78% |
| V5 | 8/15 | 425 | 9 | 32,1% | 55,56% |
| V6 (2V.3V) | 1/2 | 555 | 10 | 18,9% | 50,00% |
| V6 | 1/2 | 555 | 9 | 33,2% | 50,00% |

### Conceitos Essenciais

- **Frequência (nV):** Nível de subdivisão das faces triangulares (quanto maior, mais esférica)
- **Variância da Vareta:** Indica uniformidade dos comprimentos; menor = triângulos mais regulares
- **Truncagem:** Porção da esfera (1/1, 1/2, 3/8, 5/8)
- **Escala Linear:** Coeficientes × raio desejado = comprimento real da vareta
- **Ângulos de Vértice:** Dobras nas extremidades para conexão adequada e curvatura esférica

## 4. Aplicações

- Dimensionamento de domos geodésicos em bambu, aço ou madeira
- Projeto de coberturas, pavilhões, abrigos, estufas e habitações
- Cálculo de quantitativos (varetas, conectores, painéis)
- Otimização estrutural (escolha de frequência e poliedro base)
- Fabricação de componentes com cortes precisos

## 5. Referências

- Documento original: Takwara-Tech/docs/A4. Domos Geodésicos/a3.2 Especificações técnicas.md
- Domos geodésicos — Referências online: simplydifferently.org, domerama.com, sonostarhub.com
- Buckminster Fuller. Synergetics: Explorations in the Geometry of Thinking.
- ISO 22156:2021 — Projeto estrutural de bambu
