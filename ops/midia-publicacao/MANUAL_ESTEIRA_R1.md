# Esteira de publicação do Acervo — manual operacional R1

STATUS=PROPOSTA · NÃO VIGENTE
DATA=2026-11-20
FRENTE=INTEGRACAO_MIDIAS_SOCIAIS
DECISÃO_REGISTRADA=FABIO_SOBERANO 2026-11-20 (critério de homologação e cadeia ficha→peça editorial→mídia)

## 1. O que esta esteira faz e o que ela não faz

**Faz**: recebe peças de mídia que derivam de peças editoriais homologadas, monta um lote,
ordena uma fila com canal/data/hora, e **recusa** tudo que não cumpra os portões.

**Não faz**: não publica. Não fala com a Meta. Não abre rede. Não decide formato. Não cria conteúdo.

Quem publica, na fase 1, é o soberano, à mão. Na fase 2 será um executor no Cloudflare — que
ainda não existe e depende de credencial no Meta App.

## 2. A cadeia (e por que ela tem quatro elos)

```
ficha (docs/analyses/<gaveta>/*.md)      INSUMO — não publicável
   ↓
peça editorial                            CAMADA HOMOLOGÁVEL
(estado da arte | artigo didático | artigo científico Zenodo)
   ↓
peça de mídia                             ESTA ESTEIRA
(carrossel | vídeo curto | estático)
   ↓
lote aprovado                             ATO DO SOBERANO
   ↓
fila de publicação                        item = peça + canal + data + hora
```

O elo que existe para impedir o erro caro é o segundo. **A ficha não vira mídia.** Uma ficha
científica declara limites, ressalvas e condições que uma legenda de 2.200 caracteres não comporta;
traduzi-la direto para post transforma ressalva em afirmação. A peça editorial — estado da arte da
coleção, artigo didático ou artigo científico publicado — é o que já passou por esse trabalho de
síntese, e é a única coisa que pode alimentar mídia.

## 3. Critério de homologação (literal do soberano)

> "trabalharemos apenas com material homologado que tenha pelo menos um estado da arte de uma
> coleção e um artigo, um artigo didático, no mínimo. Podem haver casos em que um artigo de cunho
> científico seja produzido e publicado no Zenodo."

Operacionalmente: a peça editorial precisa declarável em frontmatter

- `estado_documental` entre os aceitos: `homologado-documentalmente`, `publicado-no-zenodo`,
  `depositado-no-zenodo`, `publicado-no-acervo`, `edicao-publica-conformada`, `edicao-revisada-para-acervo`,
  `curado`, `revisado-com-fonte-integral` — os dois últimos porque `GOVERNANCA_DOCUMENTAL.md:86/88` os
  declara equivalentes a homologado
- na peça de mídia, bloco `colecao` com `estado_da_arte` (caminho) e `artigos` (lista, mínimo um), **e cada
  ponteiro tem de resolver** no disco ou no ref declarado

**Por que o bloco, e não um booleano.** A versão anterior aceitava `tem_artigo: sim` — e um booleano é
declaração de quem escreve, não prova de nada: quem digita `sim` não precisa ter artigo nenhum. A
auditoria TECO de 2026-11-20 demonstrou isso com uma origem mínima (três linhas) que passou.

**E por que existência não bastava.** A rodada 2 da mesma auditoria mostrou dois furos: o mesmo arquivo
podia ocupar os dois papéis (estado da arte *e* artigo), e o caminho podia escapar da raiz
(`../../etc/hosts`). Agora o gate lê o frontmatter de cada ponteiro e exige: caminho dentro do
repositório, `estado_documental` homologado, papéis distintos (por caminho resolvido — `art.md` e `./art.md` são o
mesmo arquivo), e cada documento declara seu papel: o estado da arte com `tipo_documental` iniciando em
`estado` ou `e_estado_da_arte: sim`; o artigo com `tipo_documental` iniciando em `artigo` ou
`e_artigo: sim`. Bloco `colecao` malformado gera recusa nomeada, não exceção. Não é cerimônia: é a diferença entre "o arquivo existe" e "o critério do
soberano foi cumprido".

`em-revisao-documental` **não** passa. Medido em 2026-11-20 (comandos no fim desta seção): **238 de 338 fichas** do corpus estão
nesse estado. Isso não é defeito do corpus, é o retrato do terreno em preparação.

**Como reconferir a contagem:** os números mudam com o acervo, então o comando importa mais que o valor:
o parser de frontmatter sobre `docs/analyses/**/*.md`, **num checkout limpo** — árvore com arquivo não rastreado infla a contagem, e `grep` literal subconta valores entre aspas (medido: 98 aceitos pelo parser contra 43 do grep).

## 4. Os sete portões (P0 a P6)

| portão | o que verifica | como falha |
|---|---|---|
| P0 | o tipo de cada campo da peça e de cada item das listas | recusa nomeada em vez de exceção (peça/`deriva_de`/`itens`/`aprovacao`/`agendamento` malformados) |
| P1 | `deriva_de.tipo` é editorial publicável **e** `deriva_de.path` fica dentro do repositório | recusa se `tipo=ficha`/desconhecido ou se o caminho escapa da raiz |
| P2 | a origem resolve (bytes no worktree **ou** `git cat-file` no ref) e o `sha256` confere | recusa se não resolver ou o hash divergir |
| P3 | origem homologada **e** bloco `colecao` com `estado_da_arte` + `artigos` (≥1): cada ponteiro tem de **resolver dentro do repositório**, ter `estado_documental` homologado, apontar para **arquivo distinto** do outro (comparação por caminho resolvido, não por texto) e **declarar o próprio papel** | recusa estado não homologado, coleção sem estado da arte, coleção sem artigo, mesmo arquivo nos dois papéis, caminho fora da raiz e documento que não é artigo |
| P4 | formato coerente com a contagem de itens | carrossel exige 2 a 20 |
| P5 | toda `fonte` citada aparece literalmente no corpo da origem | recusa fonte inventada; é verificação de string, não de sentido |
| P6 | `sha256_da_peca` é o hash **calculado** do conteúdo (não um valor declarado), a aprovação registra esse mesmo hash, com autoridade registrada e data ISO | recusa hash arbitrário, conteúdo alterado após a aprovação, aprovador inventado e data inválida |

## 4A. As duas vias de P2 — e por que a segunda não afrouxa o gate

Publicar exige a fonte rastreável, não exige cerimônia de mescla.

- **Via BYTES**: a peça editorial está no worktree. O `sha256` é calculado dos bytes presentes.
- **Via PONTEIRO**: a peça editorial está homologada e publicada em outro branch/remoto — que é o
  caso normal, porque homologado no Git já é fonte. O lote declara
  `deriva_de.sha256` **e** `deriva_de.ref` (ex.: `origin/hermes/mtcc-auditoria-pacote-...`), e o gate
  confere o hash por `git cat-file` naquele ref, no próprio clone, sem rede.

O que a via PONTEIRO **não** faz: assumir. Ref inexistente é recusa nomeada
(`ref '...' não resolve '...'`), sha divergente é recusa, e origem ausente sem ref é recusa.

Consequência prática: **nenhum lote real falha por a peça não estar mesclada na main.** Foi o defeito
medido no ensaio com a BAMBU-SCIENCE em 2026-11-20.

## 5. Como o operador usa (comandos literais)

```
cd <raiz-do-repositorio>

# prova que o gate está ligado (controle negativo embutido)
python3 ops/midia-publicacao/montar_lote.py --selftest

# monta um lote real
python3 ops/midia-publicacao/montar_lote.py --lote <caminho-do-lote.json> --raiz .
```

Saída esperada: `{"selftest": "PASS", "modo": "EM_MEMORIA", "controles_negativos": 51, "controles_positivos": 6, "falhas": 0}`, exit 0.
Para o verificador de mídia: `{"selftest": "PASS", ..., "controles_negativos": 9, "controles_positivos": 2, "falhas": 0}`.
Os contadores são **calculados**, não digitados: contador escrito à mão já divergiu do código real em
auditoria, então o número sai do tamanho da lista de controles executados.
Se vier `FAIL`, o gate está desligado e **nada** deve ser publicado.

Os dois selftests rodam **sem diretório gravável** (memória + `git cat-file` no próprio clone). Isso é
deliberado: o auditor executa em sandbox read-only, e um selftest que exige escrita não pode ser executado
por quem audita — foi assim que a auditoria de 2026-11-20 não conseguiu rodar três das dez perguntas.

`montar_lote.py` sai com código 1 quando qualquer peça é recusada — recusa é resultado, não erro.

## 6. O que fazer quando a esteira recusa

Leia o erro. Cada linha nomeia o portão e o motivo. Os quatro casos reais:

- **P1 tipo=ficha** → a peça tentou publicar ficha. Precisa produzir estado da arte ou artigo antes.
- **P3 em-revisao-documental** → o terreno daquela coleção ainda não está preparado. Aguardar homologação.
- **P5 fonte não encontrada** → o texto da mídia afirma algo que a origem não contém literalmente. Corrigir o texto ou a fonte; **nunca** soltar o portão.
- **P6 hash divergente** → a peça mudou depois de aprovada. Reaprovar os bytes novos.

## 7. Pendências declaradas (com dono e bloqueio)

| # | pendência | estado | dono | bloqueia |
|---|---|---|---|---|
| 1 | modo desenvolvedor **não** cria gaveta invisível no Instagram | NÃO VERIFICADO no App real | Fábio | ensaio invisível antes do destravamento |
| 2 | `instagram_business_content_publish` ausente no app | NÃO VERIFICADO | Fábio | fase 2 |
| 3 | imagem tem de estar em URL pública (Meta baixa, não aceita upload) | requisito conhecido | a definir | fase 2 |
| 4 | relógio da fase 2 precisa sobreviver ao Mac desligado — cron no Mac não serve | requisito conhecido | a definir | fase 2 |
| 5 | auditoria do Release 1 pode revelar divergências | ABERTA | MTCC | primeiro lote com material do Release 1 |

## 8. Limites declarados

- **P5 é verificação de string, não de sentido.** Garante que a fonte citada existe; não garante
  que a peça a interpretou corretamente. Esse julgamento continua humano ou de auditor.
- **A esteira não protege contra publicação manual fora dela.** Só garante que o que passa por ela
  é rastreável.
- **A arte não é validada por pixel.** A rastreabilidade da arte é por `prompt_usado` + `confere_com`,
  porque conferir imagem exige olho, não hash.
