# Protocolo Cavichiolli — Curadoria do Acervo Soberania Tecnológica

Este documento define as diretrizes para criação e revisão de fichas no Acervo Soberania Tecnológica, baseado no método da Dra. Nathalia Cavichiolli (8 seções).

## Estrutura Padrão (8 seções)

1. **Identificação e Contexto** — autor, título, instituição, ano, tipo de documento
2. **Classificação Temática** — eixo, palavras-chave, área de conhecimento
3. **Resumo / Síntese** — descrição concisa do conteúdo
4. **Análise Crítica** — pontos fortes e fragilidades
5. **Dados Extraídos** — informações relevantes do documento
6. **Conexões com o Acervo** — fichas relacionadas
7. **Aplicações Práticas** — usos e desdobramentos
8. **Referências** — fontes consultadas

## Regras Obrigatórias

### 1. Dados completos nas fichas

NUNCA usar notas como "requer consulta ao texto completo" ou "dados não disponíveis nesta ficha" se os dados existem no documento fonte. Todo dado numérico, citação ou parâmetro presente no documento original DEVE ser extraído e inserido diretamente na ficha. A ficha é o ponto de acesso único — o usuário não deve precisar abrir o PDF para encontrar informações básicas.

Exceção: se o dado não existe no documento fonte (não foi publicado), aí sim sinalizar a lacuna.

### 2. Autenticidade das referências

NUNCA fabricar ou inventar referências, DOIs, URLs, autores ou títulos. Qualquer referência citada deve ser verificável. Se não foi possível verificar, sinalizar como "não verificado".

### 3. Linguagem

- Português (PT-BR) com acentuação gráfica correta
- Sem emojis no conteúdo (exceto quando indicado pelo autor)
- Sem codinomes internos (biosoberano, "cozinha") em fichas públicas
- Termos técnicos em inglês mantidos no original quando apropriado

### 4. Direitos autorais

Textos integrais de documentos protegidos (dissertações, teses, artigos) DEVEM ser mantidos em pasta não commitada (`_acervo_completo/transcricoes/`). As fichas contêm apenas resumos, dados extraídos e análises críticas — nunca o texto completo.

### 5. Licenciamento

Todas as fichas são CC BY 4.0. Incluir no frontmatter YAML: `licenca: CC BY 4.0`

### 6. Metadados YAML

Toda ficha deve ter frontmatter YAML com no mínimo:
```yaml
---
tipo: Ficha Cavichiolli (8 seções) — [Tipo de documento]
titulo: [Título completo]
autor: [Autor(es)]
instituicao: [Instituição]
ano: [Ano]
status: Consolidado
licenca: CC BY 4.0
---
```

### 7. Extração de texto integral

Para cada PDF trabalhado extrair o texto completo com PyMuPDF (`fitz`) e salvar em:
`_acervo_completo/transcricoes/[subpasta]/[slug].txt`

O arquivo de texto é para consulta dos agentes. A ficha contém a curadoria.

---
*Protocolo mantido pelo Hermes Agent · Acervo Soberania Tecnológica · 2026*
