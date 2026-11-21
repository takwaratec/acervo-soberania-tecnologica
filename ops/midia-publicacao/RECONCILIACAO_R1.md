# RECONCILIAÇÃO R1 — esteira de publicação de mídia

FRENTE=INTEGRACAO_MIDIAS_SOCIAIS
TASK=RECONCILIACAO_ESTEIRA_R1
DATA=2026-11-20
AUTORIDADE=decisão soberana sobre parecer externo (veredito ADEQUADO COM RESSALVAS)
BASE=commit auditado 05b8ceb0ce653e3fc8583224349fd9f89502e134
RESTRIÇÕES=NO_DEPLOY · NO_META_MUTATION · NO_CLOUDFLARE_MUTATION · NO_GPT_MAKER_MUTATION · NO_PUBLICATION · NO_UNAUTHORIZED_MERGE

## 1. Diretriz aplicada

> Homologar uma vez. Produzir muitas vezes. Rastrear automaticamente. Aprovar somente o que exige decisão humana.

A reconciliação corrigiu um desequilíbrio: a engenharia da esteira havia avançado mais que a produção
editorial disponível para alimentá-la. O resultado era um gate cada vez mais fino sobre uma entrada
vazia. A prioridade passou a ser **provar a cadeia com material real**.

## 2. O que mudou, item por item

### A — Compatibilidade documental

- `tipo_documental` (o que o documento é, no frontmatter dele) passou a ser **fonte de verdade** para P1.
- `papel_editorial` (o papel que a peça de mídia lhe atribui) não substitui o tipo: uma peça pode
  declarar `deriva_de.tipo: estado-da-arte` e apontar para ficha — e é recusada.
- Metadados originais preservados; nenhum documento foi reclassificado para conveniência do gate.

### B — Vínculo entre documentos

- Estado da arte e artigo têm de pertencer à coleção declarada (`colecao.gaveta` + caminhos).
- A relação é determinada pelo **caminho e pelo frontmatter**, não por preenchimento humano novo:
  `colecao.estado_da_arte` e `colecao.artigos` são os identificadores; o resto é lido.
- Papéis distintos comparados por caminho resolvido (`art.md` e `./art.md` são o mesmo arquivo).

### C — Portões P0–P7

| portão | antes | depois |
|---|---|---|
| P1 | conferia o tipo **declarado pela peça** | confere a **natureza efetiva**: `tipo_documental` da origem |
| P3 | exigia homologação documental **para produzir** | homologação é **condição de liberação**; estrutura da coleção continua bloqueio |
| P5 | — | permanece **textual**, declarado como tal: confere existência da string, não sentido |
| P6 | dois campos (`aprovacao.por` + hash) | **ato único** `liberacao` com autoridade, data, canal, destino e hash do conteúdo |
| P7 | uma pergunta | **três**: bytes / coerência do manifesto / disponibilidade pública real |

Nenhum portão novo foi criado. `P8` e `P9` não existem.

### D — Aprovação humana

Um bloco, um ato, quatro informações: identidade declarada, data, conteúdo aprovado, destino autorizado.
`autoriza_publicacao: false` registra revisão **sem** publicação. Sem bloco, a peça é produzida e fica
pronta — pendência declarada, não erro.

**Limite honesto, escrito no schema e no manual:** `sha256` prova integridade, não identidade nem
consentimento. `autoridade` é declaração; `canal_da_aprovacao` aponta onde o ato aconteceu. O sistema
não autentica pessoas e não finge que autentica.

### E — Restauração

Mapa reescrito como sequência executável de nove passos:

```
ACESSO → CLONE → CREDENCIAIS → CUSTÓDIA → DESCRIPTOGRAFIA
       → CONFERÊNCIA DE HASH → RECONSTRUÇÃO DOS ASSETS → BUILD → VERIFICAÇÃO LOCAL
```

Preservados: binários fora do Git, chave `age` fora do repositório. **Não** se declara recuperação
comprovada: o ensaio em VM limpa não foi executado, e o documento diz isso no título, no status e no
§5.

### F — Honestidade documental

- **Oito** rodadas técnicas (TECO) + **uma** auditoria externa = 9 eventos, não "nove rodadas técnicas".
- Contadores de selftest calculados do código: **59 negativos + 8 positivos** (montador), **9 + 2** (verificador).
- P7 tinha sido descrito como pronto quando só existia o verificador de bytes; hoje tem três
  veredictos separados e `--publico` explícito.
- O manual HTML passou a ser **gerado** do Markdown (`gerar_manual_html.py`). Manter dois documentos à
  mão produziu divergência real ("seis portões" num código com sete); gerar resolve a classe do problema.

## 3. Desburocratização aplicada

| regra | como aparece no código |
|---|---|
| 1. Reutilização | uma base homologada serve a muitos derivados; nada é re-homologado por peça |
| 2. Herança de proveniência | `--selar` calcula hashes; saída traz `rastreabilidade` com título, ano, DOI, tipo, estado e gaveta lidos da origem |
| 3. Verificação silenciosa | portões rodam sempre; só bloqueio material interrompe. Pendência de liberação não é erro |
| 4. Aprovação concentrada | um bloco `liberacao`, uma decisão, um destino |
| 5. Exceções explícitas | divergência não é resolvida por inferência: é pendência nomeada |
| 6. Sem infraestrutura nova | nenhum serviço, fila ou banco novo; stdlib apenas |
| 7. Proporcionalidade | nenhum P8; nenhum passo administrativo adicional; nenhum campo pedido duas vezes |

## 4. Prova editorial funcional — piloto Bambu Estrutural

Material real, sem invenção de dados:

- base: `docs/analyses/bambu-estrutural/estado-da-arte.md` (555 linhas, `em-revisao-documental`)
- artigo novo: `docs/analyses/bambu-estrutural/artigo-didatico-bambu-estrutural.md` (linguagem de leitor não especialista, cada número atribuído à ficha de origem)
- peça: `ops/midia-publicacao/piloto/LOTE_PILOTO_BAMBU_E1.json` (carrossel de 8 slides)
- produto: `ops/midia-publicacao/piloto/PILOTO_BAMBU_E1.html` (6 seções, sem links externos, gerado por script)

Resultado dos portões no piloto:

```
verificadas            1
liberadas              0
prontas_para_liberacao 1
erros                  0
pendencias             base em revisão (2 ponteiros) + nenhum ato de liberação
```

É exatamente o desenho: **produção verificada, publicação não autorizada.** O piloto demonstra a
cadeia e não finge aprovação.

## 5. O que continua pendente

| # | pendência | dono |
|---|---|---|
| 1 | homologação da base Bambu (estado da arte + artigo) | Fábio |
| 2 | ato de liberação do carrossel | Fábio |
| 3 | hospedagem pública Opção A (credencial Cloudflare) | Fábio |
| 4 | chave `age` fora do Mac verificada | Fábio |
| 5 | ensaio de restauração em VM limpa | ambos |
| 6 | arte renderizada (Canva) para os 8 slides | a definir |

## 6. O que este documento não afirma

- Não afirma que a esteira está homologada: ela está **reconciliada** e verificável.
- Não afirma que o corpus está pronto: 0 artigos homologados na medição de 2026-11-20.
- Não afirma recuperação de desastre comprovada.
- Não afirma que a publicação é segura: ela ainda não aconteceu nenhuma vez.
