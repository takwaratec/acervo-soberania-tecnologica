# Inventário reproduzível do Acervo — 30/08/2026

> Este documento conta arquivos; não confunde volume documental com validação científica.

## Contagens principais

| Medida | Total | Definição operacional |
|---|---:|---|
| Markdown público | 296 | Arquivos `.md` sob `docs/` incluídos no build |
| Documentos em `analyses` | 291 | Arquivos sob `docs/analyses/`; incluem fichas, perfis e índices |
| Estrutura numerada 1–8 em `analyses` | 200 | Os oito títulos numerados foram detectados; o conteúdo ainda exige revisão humana |
| Identificador público em `analyses` | 135 | DOI, ISBN, ISSN ou Handle detectável no arquivo |

## Distribuição do Markdown público

| Diretório inicial | Arquivos |
|---|---:|
| `analyses` | 291 |
| `raiz-docs` | 5 |

## Estados explicitamente declarados

| Estado encontrado | Arquivos |
|---|---:|
| `curado` | 10 |
| `depositado-no-zenodo` | 1 |
| `edicao-publica-conformada` | 16 |
| `em-revisao-documental` | 236 |
| `homologado-documentalmente` | 17 |
| `publicado-no-acervo` | 1 |
| `publicado-no-zenodo` | 15 |

## Tipos documentais declarados

| Tipo documental | Arquivos |
|---|---:|
| `documento-de-patente` | 2 |
| `documento-historico` | 1 |
| `documento-institucional` | 13 |
| `ensaio-autoral` | 1 |
| `estado-da-arte` | 24 |
| `estado-da-arte-com-agenda-experimental` | 17 |
| `ficha-academica` | 89 |
| `ficha-cientifica` | 89 |
| `ficha-tecnica-de-produto` | 2 |
| `indice` | 12 |
| `indice-tematico` | 2 |
| `instrumento-de-pesquisa` | 7 |
| `laudo-ou-certificado-de-ensaio` | 1 |
| `material-didatico-institucional` | 3 |
| `memoria-historica` | 1 |
| `norma-ou-regulamento` | 1 |
| `perfil` | 12 |
| `periodico-institucional` | 3 |
| `resenha-academica` | 11 |
| `sintese-critica` | 1 |
| `visao-autoral` | 4 |

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
