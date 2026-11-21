# Frente BAMBU-BAMBUSC — catálogo documental BambuSC (rodada 1)

```
FRENTE=BAMBU-BAMBUSC
TASK=BAMBU-BAMBUSC-CATALOGO-20261119-R1
EXECUTOR=HERMES_OPENCODE
AUDITOR=CODEX_LUNA_MEDIUM (auditoria interna) + SOL (auditoria externa, leitura do GitHub)
DATA=2026-11-19
ESTADO=NENHUMA FICHA HOMOLOGADA
```

## O que esta frente fez

Mediu o inventário de publicações da BambuSC e produziu fichas candidatas das obras
que têm registro próprio (DOI ou ISBN). **A BambuSC não é fonte** — é apenas onde os
arquivos foram encontrados. A fonte citável é a obra assinada.

## Regra de elegibilidade aplicada (decisão do soberano)

1. Só entra material com **DOI ou ISBN do próprio documento**, verificado — na capa, com
   resolução no Crossref e título casado, ou `citation_doi` da landing oficial com ISSN da
   revista conferida.
2. Material autoral **sem registro é ignorado**.
3. A fonte citada é o **artigo assinado**, com autores e ano. Nunca "segundo a BambuSC".
4. Fichas ficam em **`em-revisao-documental`** até a auditoria final e homologação.
5. Extração e ficha passam por **auditoria interna**, com auditor ≠ executor.

## Números medidos

- **67 obras** listadas em `/recomendacoes/`, em 7 seções.
- **41 endpoints** de arquivo medidos: **20 íntegros**, **21 mortos**, 4 links locais
  inválidos — o site publica caminhos locais de máquina, do tipo `file:///C:/Users/arqui/...`,
  transcrito aqui como achado e **não** como caminho desta máquina — nenhum link morto foi promovido a inexistente.
- **52 links mortos varridos** depois: **10 recuperados** (8 pela migração da revista MIX
  Sustentável de `nexos.ufsc.br` para `ojs.sites.ufsc.br`, 2 que só falhavam por acento
  não codificado na URL).
- **11 elegíveis** → **11 fichas candidatas**, todas em `em-revisao-documental`.
- Custódia: **11 pacotes** com `original.pdf`, `extracao.md`, `paragrafos.md`,
  `metadados.json`, `PROVENIENCIA.md`; **SHA-256 conferido 11/11**.

## O defeito de extração que esta frente encontrou e corrigiu

A extração plana de PDF entregava páginas de **duas colunas** com a coluna **direita antes
da esquerda**, e as fichas citavam trechos por essa ordem. Medição em Salamon & Ostapiv,
p. 2: parágrafos da coluna direita (`x0=322`) vinham antes dos da esquerda (`x0=70`).

Correção em três camadas, a partir do método MTCC já existente:

| camada | origem no MTCC | o que faz |
|---|---|---|
| parágrafo | `ops/command-center/metodo/extrair_holdout.py` | `pymupdf4llm` devolve parágrafo, não caixa de layout |
| remontagem | `motor/remontar.py` | fragmento que continua a frase é absorvido |
| ordem por coluna | **camada nova** | o MTCC declarava o campo `layout` mas não reordenava; aqui se separa por coluna e concatena esquerda→direita |

**Limite declarado:** a reconstrução por coluna às vezes perde palavra na junção. Por isso
todo número foi conferido também contra a extração plana **e** contra a imagem renderizada
do PDF.

## Por que os PDFs e o texto integral não estão aqui

`_privado/` é **ignorado pelo git** (`.gitignore` linha 28). Direitos de 10 das 11 fontes
não são declarados, e o acervo privado não se publica por padrão. O que está publicado
neste diretório é o **registro auditável**: identidade de cada obra, hashes, método,
números conferidos, limites e o que cada fonte não autoriza concluir.

Quem audita recebe os hashes (`SHA256SUMS` do pacote de auditoria) e a declaração de
custódia; o binário fica sob custódia privada e é entregue por solicitação do soberano.

## Fichas (11)

| # | obra | registro | pág. | natureza |
|---|---|---|---:|---|
| 1 | Pereira, Carrara, Barata, Valarelli & Azambuja 2012 — pré-fabricação de componentes de bambu | DOI 10.4322/floram.2012.024 | 10 | artigo |
| 2 | Jaramillo, Lisbôa, Goularte & Librelotto 2020 — pérgola de bicicletário | DOI 10.24133/ciencia.v22i1.1271 | 10 | artigo (CC BY) |
| 3 | Ostapiv, Salamon, Stahlschmidt & Ferraz Bett 2018 — cúpulas geodésicas | DOI 10.29183/2447-3073.MIX2018.v4.n1.108-116 | 9 | artigo |
| 4 | Geiss & Damo 2018 — viabilidade econômica de estrutura geodésica | DOI 10.29183/2447-3073.MIX2018.v4.n1.57-65 | 9 | artigo |
| 5 | Salamon & Ostapiv 2017 — planificação de colmos para painéis | DOI 10.29183/2447-3073.MIX2017.v3.n1.73-83 | 11 | artigo |
| 6 | Acosta & Carbonari 2017 — laje mista bambu-concreto leve | DOI 10.29183/2447-3073.MIX2017.v3.n2.48-56 | 9 | artigo |
| 7 | Carbonari et al. 2017 — "Bambu: o aço vegetal" | DOI 10.29183/2447-3073.MIX2017.v3.n1.17-25 | 9 | artigo |
| 8 | Sánchez Quintero & Silveira 2016 — ligação estrutural para Guadua | DOI 10.29183/2447-3073.MIX2016.v2.n1.98-106 | 9 | artigo |
| 9 | Jaramillo & Szücs 2017 — sistema construtivo para HIS com Guadua | DOI 10.29183/2447-3073.MIX2017.v3.n3.158-160 | 3 | **resumo expandido** |
| 10 | Dutra & Pazmino 2016 — mobiliário infantil em bambu | DOI 10.29183/2447-3073.MIX2016.v2.n2.118-119 | 2 | **resumo de TCC** |
| 11 | Reis & Clerici 2019 — broto comestível | **ISBN 978-65-900237-0-4** | 60 | e-book |

## Os números que exigem cuidado — e o que a fonte não autoriza

- **Ostapiv et al. 2018:** "38× o peso próprio" contra "0,86 do aço" são **duas maquetes**
  com barras de diâmetros diferentes (3 mm de bambu mossô × 1 mm de aço), carregamento
  hidráulico com água, **um ensaio cada**. O domo de 4 m é construído, não ensaiado.
  **Este trabalho não autoriza "o bambu é 44× mais resistente que o aço".**
- **Carbonari et al. 2017:** Tabela 01, 9 espécies × 9 corpos de prova (3 base/3 meio/3
  topo), norma ISO/TC165 N314 (1999), faixa **38 a 75 MPa**. A presença do nó **não** afeta
  significativamente a compressão. "Aço vegetal" é **título**, não resultado: nenhum aço foi
  ensaiado no trabalho.
- **Acosta & Carbonari 2017:** a carga máxima publicada de **30 kN** pertence à laje com
  varas **a meia cana**. A segunda laje — a que os autores dizem ter ganho — **teve a carga
  omitida** no texto por erro tipográfico da fonte. A conclusão deles fica como afirmação
  sem número correspondente.
- **Geiss & Damo 2018:** é **orçamento de projeto**, com preços de 2018 em Chapecó/SC —
  não custo realizado, não preço atual, não comparativo contra alvenaria ou concreto.
- **Fontes 9 e 10 são resumos:** não se lhes atribui resultado que as páginas não contêm.

## Estado e pendências

- **Nada homologado.** Nenhuma ficha promovida a `docs/analyses/`.
- Auditoria interna (esteira local): feita — N1 11/11, N2 em 3 de 4 conjuntos numéricos.
- Auditoria externa: **SOL**, pela leitura do GitHub.
- Homologação: ato do soberano.

## Trilha

- Medição e receintos: `takwaratec/TakwaraTec-Laboratorio-Editorial`, ref `r4-claims`,
  tarefa `BAMBU-BAMBUSC-CATALOGO-20261119-R1` (estado RETORNO).
- Pacote de auditoria: `ops/command-center/task-results/BAMBU-BAMBUSC-CATALOGO-20261119-R1/auditoria-luna/`
  no branch `hermes/bambu-bambusc-auditoria-20261119`.
