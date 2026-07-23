# Inventário reproduzível do Acervo — 23/07/2026

> Este documento conta arquivos; não confunde volume documental com validação científica.

## Contagens principais

| Medida | Total | Definição operacional |
|---|---:|---|
| Markdown público | 94 | Arquivos `.md` sob `docs/` incluídos no build |
| Documentos em `analyses` | 91 | Arquivos sob `docs/analyses/`; incluem fichas, perfis e índices |
| Estrutura numerada 1–8 em `analyses` | 69 | Os oito títulos numerados foram detectados; o conteúdo ainda exige revisão humana |
| Identificador público em `analyses` | 29 | DOI, ISBN, ISSN ou Handle detectável no arquivo |

## Distribuição do Markdown público

| Diretório inicial | Arquivos |
|---|---:|
| `analyses` | 91 |
| `raiz-docs` | 3 |

## Estados explicitamente declarados

| Estado encontrado | Arquivos |
|---|---:|
| `curado` | 9 |
| `em-revisao-documental` | 85 |

## Tipos documentais declarados

| Tipo documental | Arquivos |
|---|---:|
| `documento-de-patente` | 2 |
| `documento-institucional` | 3 |
| `ficha-academica` | 6 |
| `ficha-cientifica` | 42 |
| `ficha-tecnica-de-produto` | 2 |
| `indice` | 10 |
| `laudo-ou-certificado-de-ensaio` | 1 |
| `material-didatico-institucional` | 3 |
| `norma-ou-regulamento` | 1 |
| `perfil` | 11 |
| `periodico-institucional` | 3 |
| `resenha-academica` | 9 |
| `visao-autoral` | 1 |

## Limites da contagem

- Uma ficha só é considerada documentalmente homologada após conferência humana do PDF, da autoria, do identificador e das oito seções.
- A presença automática das seções 1–8 não atesta qualidade, fidelidade ou validade científica.
- Índices, perfis, textos institucionais e estados da arte são documentos do acervo, mas não devem ser anunciados como fichas científicas.
- PDFs privados, quarentena, extrações integrais e materiais ignorados pelo Git não entram nesta contagem pública.
- Cadernos aguardando DOI e a gaveta Tecnologia Takwara em revisão são excluídos da contagem enquanto permanecerem fora do build.

## Reprodução

```bash
python3 scripts/inventariar_acervo.py . --markdown INVENTARIO_ACERVO.md --json INVENTARIO_ACERVO.json
```
