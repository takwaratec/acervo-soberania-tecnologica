---
tipo_documental: material-didatico-institucional
estado_documental: em-revisao-documental
data_revisao: 2026-07-14
responsavel_curadoria: Fabio Takwara
---

# Metodologia

## Protocolo de Análise

Cada referência inserida neste repositório passa por um fluxo padronizado de 7 etapas, baseado nos **200+ Prompts para Escrever Artigos Científicos** (Cavichiolli, 2025) e adaptado para análise de trabalhos acadêmicos:

> ⚠️ **REGRAS OBRIGATÓRIAS:** 
> 1. **NUNCA** crie fichas de artigos/teses/PDFs sem que os campos de **autor, DOI, ISBN, ISSN** ou outro meio de identificação estejam preenchidos. Documento sem autoria identificada **não entra no acervo**.
> 2. **NUNCA** referencie documentos incompletos. Se faltam dados essenciais (autor, ano, título completo), a ficha **não é criada** até que o PDF original seja acessado.
> 3. **Sempre que identificar dados faltantes**, alerte o usuário para dar acesso ao original antes de prosseguir.
> 4. Toda ficha deve conter **8 seções obrigatórias** conforme método Cavichioli (2025) — se alguma seção não puder ser preenchida por falta de acesso ao PDF, a ficha não deve ser publicada.

### Etapa 1 — Extração e leitura inicial

- Obtenção do PDF completo
- Extração do texto via PyMuPDF
- **Extração OBRIGATÓRIA de metadados do PDF:**
  - **Autor(es):** extrair nomes completos do PDF (primeira página, cabeçalho do artigo). NUNCA usar "Pesquisadores do...", "Autores diversos" ou "Não identificado" como substituto — se o PDF estiver acessível, os autores estão lá.
  - **DOI:** verificar na primeira página do artigo. Se o periódico tiver DOI, ele DEVE ser capturado.
  - **Título:** usar o título completo do PDF, não versão truncada.
  - **Ano:** verificar na página de publicação.
  - **Páginas:** contar ou extrair do documento. NUNCA usar "Documento original digital".
- **OCR:** quando o PDF for escaneado (imagem), aplicar Tesseract 5 (por+eng) para extrair o texto antes de criar a ficha.
- **TRADUÇÃO:** todo conteúdo extraído de documentos em outros idiomas (inglês, espanhol, etc.) DEVE ser traduzido para o português. O acervo é em português. NUNCA deixar seções em inglês.
- **FORMATAÇÃO:** as seções 4 a 8 devem ter conteúdo limpo, sem cabeçalhos de seção (`## N.`) embutidos no texto. Cada seção deve ser separada por linha em branco.
- Leitura da estrutura: título, autor, instituição, ano, orientador, resumo, palavras-chave
- Identificação do sumário e seções principais

### Etapa 2 — Mapeamento estrutural

- Verificação dos elementos pré-textuais (NBR 14724)
- Identificação da estrutura de capítulos
- Análise da progressão: introdução → referencial → método → resultados → conclusão

### Etapa 3 — Análise do referencial teórico

Identificação de:

- Escola teórica principal (Bourdieu, Weber, Marx, etc.)
- Conceitos-chave operacionalizados
- Autores de referência citados
- Coerência entre teoria e método

### Etapa 4 — Avaliação metodológica

- Abordagem (quali, quanti, mista)
- Técnicas de coleta (entrevistas, questionários, observação)
- Procedimento amostral
- Protocolo de análise dos dados
- Rigor ético (CEP, TCLE, anonimização)
- Limitações metodológicas identificadas

### Etapa 5 — Extração de achados

- Resultados principais (com valores numéricos quando disponíveis)
- Achados secundários relevantes
- Citações ilustrativas (verificadas na fonte original)

### Etapa 6 — Avaliação crítica

- Contribuições originais
- Lacunas e fraquezas
- Qualidade formal (ABNT: NBR 6023, 10520, 6027, 6028)
- Relevância para o repositório

### Etapa 7 — Inserção no estado da arte

- Classificação temática (percepção social, APO, política habitacional)
- Conexão com outras fichas do mesmo eixo
- Identificação de lacunas para pesquisa futura

### Critério de contribuição para a pesquisa Takwara

A contribuição de cada fonte é analisada como parte de um sistema que relaciona recursos materiais, conhecimento, território, trabalho, capacidade produtiva, manutenção e autonomia. O bambu e outros recursos vegetais não são tratados como soluções isoladas: seu valor depende das relações técnicas e sociais que permitem transformá-los com segurança, gerar conhecimento verificável e manter benefícios sob domínio das comunidades.

Quando a fonte não estuda diretamente o bambu ou uma tecnologia Takwara, a ficha não força equivalências. Ela identifica a contribuição metodológica, os requisitos de validação e a parte do sistema que o estudo ajuda a compreender. A análise deve distinguir potencial de aplicação, evidência disponível e lacunas ainda abertas.

### Regra de redação pública

A versão publicada contém a curadoria final. Comentários sobre erros de fichas anteriores, quarentena, reconstrução, etapas de revisão ou decisões internas de triagem ficam restritos aos relatórios privados.

---

## Prompts utilizados

A análise aplica os seguintes prompts do ebook (ver [wiki de prompts](https://fabiotakwara.github.io/Analises-e-escrita-cientifica/prompts/)):

| Seção do ebook | Prompt aplicado |
|----------------|-----------------|
| B1 — Revisão de Literatura | Planejamento de busca, Estado da arte, Mapa de controvérsias |
| B2 — Processo de Publicação | Análise de adequação, Verificação de conformidade, Análise de impacto |
| B3 — Normas Técnicas | Validação ABNT, Consistência terminológica |
| A2 — Metodologia | Prompt de aprimoramento + prompts específicos |

---

## Template da ficha técnica

Cada ficha segue este formato:

```markdown
> **Resumo:** [síntese em 5-6 linhas: objeto, método, achado central, implicação]

## 1. Dados gerais
[Tabela com título, autor, orientador, instituição, ano, páginas, palavras-chave]

## 2. Estrutura e organização
[Seções, capítulos, progressão]

## 3. Problema e perguntas de pesquisa
[Objetivos, tese central]

## 4. Referencial teórico
[Escola, conceitos, coerência]

## 5. Metodologia
[Abordagem, técnicas, amostra, limitações]

## 6. Principais achados
[Tabela de resultados]

## 7. Avaliação crítica
[Contribuições, lacunas, qualidade formal]

## 8. Inserção no estado da arte
[Conexões com outros trabalhos, relevância para o repositório]
```
---
tipo_documental: material-didatico-institucional
estado_documental: em-revisao-documental
data_revisao: 2026-07-14
responsavel_curadoria: Fabio Takwara
---
