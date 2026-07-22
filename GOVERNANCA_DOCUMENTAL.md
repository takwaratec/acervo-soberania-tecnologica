# Governança e estados documentais do Acervo

Este documento define os estados usados no **Acervo Soberania Tecnológica**. O estado descreve a maturidade documental; ele não é uma nota de mérito científico nem uma declaração de validação tecnológica.

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

## Regra de publicação

- `docs/` é a árvore pública do MkDocs.
- `_privado/`, `_acervo_completo/`, `_quarentena/` e extrações integrais não podem ser copiados para `docs/`.
- O build deve falhar quando houver link inválido ou arquivo protegido na árvore pública.
- Mudanças de README, página inicial, navegação e deploy exigem aprovação de Fabio nesta etapa.
