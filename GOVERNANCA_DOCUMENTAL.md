# Governança e estados documentais do Acervo

Este documento define os estados usados no **Acervo Soberania Tecnológica**. O estado descreve a maturidade documental; ele não é uma nota de mérito científico nem uma declaração de validação tecnológica.

## Gavetas lógicas aprovadas (2026-07-31)

Estrutura de organização do Acervo, aprovada por Fabio Takwara. As gavetas
públicas correspondem à árvore `docs/analyses/` e ao `nav` do MkDocs. As
gavetas de quarentena e privadas ficam fora da árvore pública (`docs/`).

### Públicas (9)

| Código | Gaveta | Diretório |
|--------|--------|-----------|
| FND | Fundamentos | `docs/analyses/fundamentos/` |
| BAM | Bambu estrutural | `docs/analyses/bambu-estrutural/` |
| POL | Polímeros vegetais | `docs/analyses/pu-vegetal/` |
| SOC | Habitação social (percepção, APO, política) | `docs/analyses/percecao-social/`, `avaliacao-pos-ocupacao/`, `politica-habitacional/` |
| BIO | Bioeconomia amazônica | `docs/analyses/bioeconomia-amazonica/`, `grandes-obras-amazonia/` |
| RAA | Reforma agrária e agrofloresta | `docs/analyses/reforma-agraria-agrofloresta/` |
| TT | Tecnologia Takwara | `docs/analyses/tecnologia-takwara/` |
| AUT | Visão do autor | `docs/analyses/visao-do-autor/` |
| PER | Perfis acadêmicos | `docs/analyses/respaldo-academico/` |

### Quarentena (4)

| Código | Gaveta | Destino |
|--------|--------|---------|
| QDOI | Sem DOI | `_quarentena/_sem_doi/` |
| Q+BAM/Q+POL/Q+SOC | Fontes auxiliares por área | `_quarentena/` (por área) |
| Q+TT | Visão autoral Takwara | `_quarentena/` |
| DEL | Para deleção autorizada | `_quarentena/_para_delecao_autorizada/` |

### Privadas (4)

| Código | Gaveta | Destino |
|--------|--------|---------|
| PRE | Pré-curadoria autoral | `_privado/acervo-autoral-fabio-takwara/pre-curadoria/` |
| FAP | Fontes acadêmicas protegidas | `_privado/` |
| DUP | Duplicatas | `_privado/` |
| STB | Stubs | `_privado/` |

**Regra de fronteira:** conteúdo de quarentena e privado nunca entra em
`docs/`; `_privado/`, `_quarentena/` e `_acervo_completo/` estão fora do
build e da indexação.

## Princípios

- O PDF original é a fonte primária da ficha.
- Artigos e trabalhos acadêmicos só ingressam como ficha quando a fonte integral e a identidade documental são verificáveis. DOI, ISBN, ISSN, Handle e outros identificadores devem ser registrados quando existirem, mas não são requisitos absolutos para teses, dissertações, trabalhos de evento, relatórios ou documentos históricos com autoria, título, instituição, data e proveniência confirmados no original.
- Laudos, certificados de ensaio e fichas de produto não precisam possuir DOI, ISBN ou ISSN. Para ingressar como documento técnico, devem informar emissor, produto ou amostra, data ou versão quando existente e um identificador técnico verificável, como número do laudo, certificado, ordem de serviço, norma de ensaio ou código oficial do produto.
- A ausência de DOI em documento técnico não o transforma em publicação científica e não autoriza seu uso como prova pública além do escopo efetivamente ensaiado.
- As oito seções do método Cavichiolli devem estar preenchidas a partir da leitura integral.
- Documento interno não é evidência pública.
- Ficha, perfil, índice, estado da arte, visão autoral e documento histórico são tipos diferentes e entram em contagens separadas.
- Licença do texto curatorial não altera os direitos da obra analisada.
- A ficha pública apresenta a curadoria consolidada. Histórico de erros, versões anteriores, quarentena, correções e decisões de triagem pertence aos relatórios privados e não deve aparecer na redação destinada à publicação.

## Taxonomia de estados

| Estado canônico | Uso | Pode ser publicado? | Critério de saída |
|---|---|---:|---|
| `recebido` | Arquivo ainda não triado | Não | Identificar natureza, autoria, direitos e vínculo temático |
| `identificacao-pendente` | Faltam autoria, fonte integral ou dados essenciais de identidade documental | Não | Confirmar os dados na fonte original ou registro oficial |
| `protegido-privado` | Livro, norma integral, contrato, dado fiscal ou material de circulação restrita | Não | Permanece privado; só metadados e análise própria podem ser públicos |
| `duplicata-fonte-auxiliar` | Tradução, cópia ou versão do mesmo documento | Não como ficha autônoma | Vincular à ficha principal e registrar proveniência |
| `extracao-preliminar` | Texto extraído para leitura, ainda não convertido em ficha | Não | Conferência com o PDF e elaboração das oito seções |
| `em-revisao-documental` | Ficha completa, aguardando conferência editorial e bibliográfica | Sim, apenas se explicitamente marcada e sem material protegido | Verificar metadados, fidelidade, links e classificação temática |
| `homologado-documentalmente` | Fonte, identidade documental, oito seções e redação foram conferidas | Sim | Nova revisão somente quando houver correção ou atualização da fonte |
| `visao-autoral` | Interpretação ou formulação de Fabio Takwara | Sim, quando identificada como autoral | Não deve ser apresentada como consenso científico |
| `historico` | Registro de trajetória ou documento contextual | Conforme consentimento e sensibilidade | Remover dados pessoais desnecessários; atribuir corretamente |
| `quarentena` | Documento inconsistente, fora de escopo ou legado ainda não auditado | Não | Corrigir, reclassificar ou descartar por decisão registrada |
| `retirado-da-publicacao` | Conteúdo removido da árvore pública por privacidade, direito autoral ou erro | Não | Só retorna após autorização e saneamento documentado |

### Valores em uso no acervo (levantamento 2026-07-31) e equivalência

Alguns arquivos ainda usam valores anteriores à formalização da taxonomia.
Eles permanecem válidos e são mapeados conforme abaixo. Na próxima revisão
de cada ficha, o front matter deve ser atualizado para o estado canônico.

| Valor encontrado | Contagem | Equivale a | Ação na próxima revisão |
|---|---|---|---|
| `em-revisao-documental` | 98 | `em-revisao-documental` | Manter |
| `edicao-publica-conformada` | 16 | `homologado-documentalmente` | Atualizar para `homologado-documentalmente` |
| `publicado-no-zenodo` | 12 | `homologado-documentalmente` | Atualizar para `homologado-documentalmente` |
| `curado` | 11 | `homologado-documentalmente` | Atualizar para `homologado-documentalmente` |
| `edicao-revisada-para-acervo` | 10 | `homologado-documentalmente` | Atualizar para `homologado-documentalmente` |
| `revisado-com-fonte-integral` | 1 | `homologado-documentalmente` | Atualizar para `homologado-documentalmente` |
| `depositado-no-zenodo` | 1 | `homologado-documentalmente` | Atualizar para `homologado-documentalmente` |
| `publicado-no-acervo` | 1 | `homologado-documentalmente` | Atualizar para `homologado-documentalmente` |

Observação: a publicação no Zenodo é um evento de depósito, não um estado
de maturidade documental. Após a atualização do estado para
`homologado-documentalmente`, o depósito pode ser registrado em campo
próprio do front matter (`zenodo_doi:`), preservando o rastreio sem
duplicar o conceito de estado.

## Tipos documentais

Cada arquivo deve declarar também um tipo, independente do estado:

- `ficha-cientifica`
- `ficha-academica`
- `resenha-academica`
- `estado-da-arte`
- `perfil`
- `indice`
- `documento-institucional`
- `documento-historico`
- `visao-autoral`
- `fonte-primaria-privada`
- `laudo-ou-certificado-de-ensaio`
- `ficha-tecnica-de-produto`
- `norma-ou-regulamento`
- `periodico-institucional`
- `material-didatico-institucional`
- `documento-de-patente`

Patentes documentam uma invenção, suas reivindicações e os exemplos apresentados pelo depositante. Entram como fonte tecnológica primária, separadas da contagem de fichas científicas. Concessão patentária não equivale a revisão por pares, certificação de desempenho ou replicação independente.

Perfis documentam trajetórias, vínculos e campos de atuação. Devem usar fontes institucionais ou curriculares públicas, evitar dados pessoais desnecessários e distinguir vínculo atual de função histórica. A presença de uma pessoa no Acervo não significa endosso, parceria formal, autoria conjunta ou validação de tecnologia. Perfis acadêmicos, profissionais e históricos entram em contagem própria.

## Metadados mínimos recomendados

```yaml
---
tipo_documental: ficha-cientifica
estado_documental: em-revisao-documental
fonte_primaria: PDF integral conferido
identificador: https://doi.org/...
# Quando a obra não possuir identificador persistente:
# identificador: ausente-na-fonte
# proveniencia: dados catalograficos conferidos no original integral
data_revisao: AAAA-MM-DD
responsavel_curadoria: Fabio Takwara
---
```

## Homologação documental

Uma ficha só recebe `homologado-documentalmente` quando uma revisão humana confirma:

1. título e autoria na fonte original;
2. identificador público, quando existente, e referência bibliográfica; na ausência do identificador, proveniência e dados catalográficos suficientes para individualizar a obra;
3. leitura integral do documento;
4. preenchimento substantivo das oito seções;
5. distinção entre achado dos autores e interpretação curatorial;
6. ausência de transcrição extensa ou redistribuição indevida;
7. classificação temática e links internos válidos.

Homologação documental não significa replicação experimental, revisão por pares do texto curatorial, reconhecimento institucional ou elevação de TRL.

## Fluxo de solicitação de fontes

Para fontes com paywall ou não localizadas, o fluxo é:

1. **Solicitação legítima** ao autor/instituição/biblioteca (minutas em _privado; envio pelo titular; o agente NÃO envia mensagens em nome do autor).
2. **Recebimento**: arquivar o PDF/HTML em `_privado/fontes-*`, calcular SHA-256, registrar URL, data e condição de acesso (licença/uso).
3. **Leitura integral** do texto; conferir espécie, órgão, contaminante, concentração, unidade, método, tabela e página.
4. **Matriz de alegações** atualizada com o status do valor (confirmado / divergente / não localizado / não aplicável).
5. **Ficha candidata** (somente com fonte integral): `tipo_documental: ficha-cientifica`, `estado_documental: em-revisao-documental`, declaração de limites, DOI/URL verificável, nenhum valor sem correspondência primária.
6. **Revisão humana cruzada** antes de qualquer PR.
7. **Homologação** documental apenas após matriz final e decisão explícita.

NUNCA contornar paywall, CAPTCHA ou autenticação. Fontes não localizadas permanecem "não confirmado" — não substituir referências por aproximação.

## Classificação de fichas parciais

| Classe | Definição | Ação |
|---|---|---|
| Pública e completa | Fonte primária lida integralmente; valores com correspondência par a par | Merge em docs/ (fluxo normal) |
| Secundária divergente | Revisão/compilação com valores não reconciliados com a fonte primária | Privada até reconciliação (ex.: Nemenyi 2022) |
| Texto integral pendente | Fonte primária identificada (DOI) mas paywall/sem texto | Solicitação legítima; nenhum valor fixado |
| Fonte não localizada | Sem DOI e sem texto em bases indexadas | CNKI/revistas/bibliotecas/solicitação; status "não confirmado" |
| Não verificada | Referência sem confirmação documental (ex.: Torres 2008) | Investigação manual; NÃO substituir por obra correlata sem prova de equivalência |

## Regra de fonte primária integral

- Nenhum valor numérico é fixado como fato sem leitura integral da fonte primária com correspondência exata: espécie × órgão × contaminante × concentração × unidade × método × tabela/página.
- Revisões secundárias (ex.: Nemenyi 2022) servem apenas para rastreabilidade e localização da fonte primária — NÃO substituem a fonte primária.
- Se a fonte primária divergir da secundária, registrar AMBOS os valores e não escolher por inferência.

## Protocolo de reconciliação de valores

1. Identificar o valor alegado (fonte secundária/cartilha).
2. Localizar a fonte primária (DOI/URL ou título).
3. Ler integralmente; extrair: espécie, órgão, metal, concentração, unidade, método, condições experimentais (hidroponia/solo, duração, níveis), tabela e página.
4. Comparar par a par com o valor alegado.
5. Classificar: confirmado (igual), divergente (diferente — registrar ambos), em aberto (sem fonte), não aplicável.
6. Só então atualizar a matriz de alegações e, posteriormente, tabelas das cartilhas (com espécie+órgão+metal+método+unidade+contexto).

## Critérios de promoção de estado documental (complemento)

Além dos 7 critérios da seção Homologação (título/autoria, identificador, leitura integral, oito seções, distinção achado×curadoria, sem transcrição indevida, links válidos), a promoção de `em-revisao-documental` para `homologado-documentalmente` exige:

1. Matriz de alegações com status final (sem valores "em aberto" fixados como fatos).
2. Fontes primárias confirmadas para todos os valores numéricos publicados.
3. Divergências de fontes secundárias resolvidas ou declaradas como divergentes (não escolhidas por inferência).
4. Decisão humana explícita (revisão cruzada final + autorização verbal/escrita do titular).
5. Nenhum paywall contornado; todas as fontes com proveniência (SHA-256, URL, data, condição de acesso).

A homologação NÃO significa validação experimental, certificação de desempenho ou prova de patenteabilidade.

## Identificação por natureza documental

| Natureza | Identificação mínima |
|---|---|
| Artigo científico | Autoria, título, periódico e ano; DOI ou outro registro público quando existente; sem identificador, exige original integral e proveniência documentada |
| Tese ou dissertação | Autoria, título, instituição, programa, natureza do grau e ano; registro institucional ou dados catalográficos do original integral quando disponíveis |
| Laudo ou certificado de ensaio | Laboratório emissor, cliente quando publicável, amostra, número do documento ou ordem de serviço, norma/método, período e assinatura/responsável quando presentes |
| Ficha técnica de produto | Fabricante, denominação/código do produto, versão ou data quando declarada, propriedades e condições de ensaio explicitadas |
| Relatório autoral | Autoria declarada, data/versão, método e fontes; permanece `visao-autoral` até eventual publicação científica |
| Perfil | Nome, categoria do perfil, vínculo ou atuação verificável e fontes públicas; relações com projetos devem ser declaradas sem presumir endosso institucional |

Laudos e fichas de produto sustentam apenas as propriedades e condições que documentam. Alegações comerciais sem método, norma ou relatório associado devem ser apresentadas como declaração do fabricante.

## Metadados e paridade multilíngue

Regras para versões em outros idiomas (EN/ES) e metadados:

1. **Tradução histórica versus tradução da versão corrente.** Uma tradução que corresponde a uma edição antiga publicada (ex.: PT 2.1) é classificada como `historico` — NÃO como `em-revisao-documental` (isso sugeriria que a tradução nunca foi publicada). A `nota_traducao` deve declarar a correspondência e que a versão PT atual está em revisão sem tradução correspondente.

2. **Uso de `historico`.** Aplicável a versões antigas publicadas, preservando o fato da publicação sem promovê-las ao estado da versão corrente.

3. **Distinção estado × natureza × depósito.** `estado_documental` (grau de conferência), `tipo_documental`/`natureza_documental` (tipo) e depósito Zenodo (evento, campo `zenodo_doi`/`identificador`) são atributos distintos e não devem ser confundidos no front matter.

4. **Paridade obrigatória entre idiomas.** Quando a tradução corresponde à MESMA edição, `version`, `identifier` e `data_revisao` devem espelhar a versão PT. Traduções de edições diferentes declaram a própria versão via `nota_traducao`.

5. **Proibição de promoção automática.** Uma tradução antiga NÃO é promovida automaticamente à versão PT atual; cada idioma/versão corresponde ao depósito correto.

6. **Correção de metadados sem alterar conteúdo científico.** Identificadores duplicados, campos ausentes e formatos inconsistentes são corrigidos sem tocar no conteúdo — sempre em PRs pequenos agrupados por problema.

7. **Cadernos EN podem espelhar os metadados PT** somente quando forem traduções da mesma edição (paridade verificada arquivo a arquivo).

## Regra de publicação

- `docs/` é a árvore pública do MkDocs.
- `_privado/`, `_acervo_completo/`, `_quarentena/` e extrações integrais não podem ser copiados para `docs/`.
- O build deve falhar quando houver link inválido ou arquivo protegido na árvore pública.
- Mudanças de README, página inicial, navegação e deploy exigem aprovação de Fabio nesta etapa.
