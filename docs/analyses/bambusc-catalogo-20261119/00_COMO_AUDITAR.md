---
tipo_documental: instrumento-de-pesquisa
titulo: "Como auditar este pacote (instruções para o SOL)"
estado_documental: em-revisao-documental
data_revisao: 2026-11-19
responsavel_curadoria: Fabio Takwara
gaveta: bambusc-catalogo-20261119
fonte_primaria: "instrucoes de auditoria do pacote de catalogo BambuSC; o conteudo medido esta nos arquivos de prova deste diretorio"
declaracao_ia: "produção assistida por inteligência artificial; conferência na fonte e responsabilidade de homologação são humanas"
---

# Como auditar este pacote (instruções para o SOL)

```
REPO=takwaratec/acervo-soberania-tecnologica
BRANCH=bambusc/catalogo-20261119-r1
PR=https://github.com/takwaratec/acervo-soberania-tecnologica/pull/99
DIR=docs/analyses/bambusc-catalogo-20261119/
```

Este diretório existe porque o pacote **tem de chegar até você**. O binário das obras não
vem — vai abaixo o motivo e o que isso muda na sua auditoria.

## 1. Rode isso primeiro (três desfechos, nenhum colapsa no outro)

```bash
git clone https://github.com/takwaratec/acervo-soberania-tecnologica.git auditoria
cd auditoria && git checkout bambusc/catalogo-20261119-r1
python3 docs/analyses/bambusc-catalogo-20261119/conferir_pacote.py --repo .
echo "exit=$?"
```

- `exit 0` — os 6 arquivos conferem, sha256 e tamanho.
- `exit 1` — divergiu: o script nomeia o arquivo, o sha esperado e o medido.
- `exit 2` — **não conseguiu medir** (manifesto ausente ou commit não resolvido no clone).
  Não é reprovação do pacote: é ausência de prova, e está dito como tal.

Clone **completo**, não `--depth 1`: o verificador lê do commit que o manifesto declara.

## 2. O que você consegue conferir sem o PDF

| arquivo | o que é | como se confere |
|---|---|---|
| `01_IDENTIDADE_E_CONTRATO.md` | as 11 obras, autores, ano, DOI/ISBN, páginas, licença | resolver cada DOI em `doi.org` / Crossref e comparar título, volume, páginas |
| `02_CONTRATO_DE_LEITURA.md` | por obra: limites e "o que não autoriza concluir", extraído da ficha | confrontar com a obra pela DOI (aberta em qualquer biblioteca) |
| `03_MATRIZ_POR_EIXO.md` | 11 obras × 12 eixos, com território | conferir se cada obra está no eixo que ela de fato mede |
| `04_ESTADO_DA_ARTE_DAS_FICHAS.md` | síntese exploratória com recorte e limite declarados | conferir se as convergências estão sustentadas pelas obras citadas |
| `arquivos-prova/CITACOES_DE_PROVA.md` | **27 trechos literais, com página** | é aqui que cada número se verifica |
| `INDICE_FICHAS.json` | índice legível por máquina + sha256 de cada PDF privado | conferir coerência com o manifesto |
| `PACOTE_AUDITORIA.json` | inventário com sha256 e commit de geração | `conferir_pacote.py` |

**A peça central é `arquivos-prova/`.** Cada número publicado no README tem ali o trecho
literal da fonte e a página. Você confere o número contra a citação (exata) e a citação
contra a obra (pela DOI, que é pública). **Nada neste pacote pede confiança na palavra do
executor — com as duas exceções declaradas abaixo.**

### Exceções ao round-trip "citação → obra pela DOI" (2 de 11)

O round-trip fecha em **9 das 11** obras. Nas duas abaixo ele não fecha do seu lado, e o
motivo é da fonte ou do índice, não do pacote:

| obra | registro | por que não fecha | o que você confere |
|---|---|---|---|
| Jaramillo et al. 2020 (pérgola de bicicletário UFSC) | DOI 10.24133/ciencia.v22i1.1271 | a DOI resolve para **página de login** da Revista CIENCIA, não para o PDF | a citação **contra a citação** e o **metadado** (ISSN 1390-1117, v. 22, n. 1) — não contra o texto integral |
| Reis & Clerici 2019 (broto comestível) | **ISBN 978-65-900237-0-4** (livro, sem DOI) | livro não tem DOI; ISBN não abre texto | a citação contra a citação e o **metadado** (ISBN, editora, ano) — não contra o texto integral |

Atenuantes que não compensam a exceção, mas devem ser ditos: a Jaramillo é a **única das 11
com licença declarada (CC BY)**, e nenhuma citação de **número** vem da Reis & Clerici — o
uso dela é de contexto.

Consequência: para essas duas, `round_trip_doi = NAO_FECHA` em `CITACOES_DE_PROVA.json`, e a
frase "nada pede confiança na minha palavra" vale **com essa exceção ao lado**.

## 3. O que você NÃO consegue conferir, e por quê

**Os 11 PDFs e as fichas completas ficam em custódia privada.** Dois motivos declarados:

1. `_privado/` é ignorado pelo git (`.gitignore` linha 28) — decisão de arquitetura do acervo.
2. **10 das 11 obras não declaram licença.** Republicar o PDF seria presumir direito que a
   fonte não dá. A única com licença explícita é Jaramillo et al. 2020 (CC BY).

Consequência para a auditoria: o `sha256` de cada PDF está publicado em `INDICE_FICHAS.json`
e é conferível **por quem tem a custódia** (o soberano), não por você. Trate-os como
declaração da fonte com custódia privada — nunca como conformidade medida por mim.

## 4. Números que eu quero que você ataque

1. **Ostapiv 2018** — 38× e 0,86 são de **maquetes** de barras de 3 mm (bambu mossô) e 1 mm
   (aço), um ensaio cada, carregamento hidráulico, 1,6 litros. A recusa de "bambu 44× mais
   resistente que o aço" está ancorada ou é retórica?
2. **Carbonari 2017** — Tabela 01 com 9 espécies, 9 CP cada, ISO/TC165 N314, faixa 38–75 MPa,
   e a conclusão de que o nó não afeta a compressão. Bate com as citações?
3. **Acosta 2017** — os 30 kN pertencem à laje **a meia cana**; a segunda laje teve a carga
   **omitida na própria fonte** (erro tipográfico). A ficha diz isso, ou inventou o número?
4. **Sánchez Quintero 2016** — 32 kN à tração e 19 kN à compressão, 204,5% e 121,2% contra a
   NSR-10. Confere?
5. **Geiss 2018** — 192,63% e R$ 4.592,73, e a recusa de tratar isso como comparação contra
   alvenaria ou concreto.
6. **O estado da arte** afirma que *nenhuma das 11 obras ensaia estrutura completa em escala
   real*. É uma afirmação negativa sobre 11 obras: verifique obra a obra.

## 5. Achados que já sei que existem (não são novos)

- `_privado` fora do GitHub e binários não redistribuídos (seção 3).
- Duas obras são **resumos** (3 e 2 páginas): não sustentam síntese de método.
- **Nenhuma obra é amazônica** — 8 do Sul, 2 do Sudeste, 1 do Equador.
- Critério original do contrato previa 3 elegíveis; entreguei 11, por decisão do soberano
  registrada em adendo (2026-11-19).

## 6. O que eu não vou fazer sem ordem do soberano

Promover qualquer ficha a `docs/analyses/bambu-estrutural/`. Nenhuma foi homologada.
