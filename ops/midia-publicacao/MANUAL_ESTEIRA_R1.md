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
  `depositado-no-zenodo`, `publicado-no-acervo`, `edicao-publica-conformada`, `edicao-revisada-para-acervo`
- `tem_artigo: sim`

`em-revisao-documental` **não** passa. Medido em 2026-11-20: **227 de 348 fichas** do corpus estão
nesse estado. Isso não é defeito do corpus, é o retrato do terreno em preparação.

## 4. Os seis portões

| portão | o que verifica | como falha |
|---|---|---|
| P1 | `deriva_de.tipo` é editorial publicável e o caminho existe dentro do repo | recusa se `tipo=ficha` ou caminho ausente/fora |
| P2 | `sha256` da origem confere — pelos bytes no worktree **ou** por `git cat-file` no ref declarado | recusa se divergir, faltar, ou o ref não resolver |
| P3 | origem homologada **e** `tem_artigo: sim` | recusa `em-revisao-documental` |
| P4 | formato coerente com a contagem de itens | carrossel exige 2 a 20 |
| P5 | toda `fonte` citada aparece literalmente no corpo da origem | recusa fonte inventada; **NAO_VERIFICADO** quando o corpo não está disponível |
| P6 | `aprovacao.hash_da_peca` = `sha256_da_peca` | recusa aprovação de outro bytes |

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

Saída `--selftest` esperada: `{"selftest": "PASS", "aprovadas": 1, "recusadas": 4, "erros": 4, "fila": 1}`.
Exit 0. Se vier `FAIL`, o gate está desligado e **nada** deve ser publicado.

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
