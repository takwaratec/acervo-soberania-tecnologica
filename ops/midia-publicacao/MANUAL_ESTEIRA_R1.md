# Esteira de publicação do Acervo — manual operacional R2

STATUS=VIGENTE (reconciliado pela auditoria externa de 2026-11-20)
DATA=2026-11-20
FRENTE=INTEGRACAO_MIDIAS_SOCIAIS
DECISÃO_REGISTRADA=FABIO_SOBERANO 2026-11-20 (critério de homologação, cadeia editorial e desburocratização)

**Princípio operacional:** homologar uma vez, produzir muitas vezes, rastrear automaticamente,
aprovar somente o que exige decisão humana.

## 1. O que esta esteira faz e o que ela não faz

**Faz:** recebe peças de mídia que derivam de peças editoriais, verifica tudo o que é verificável por
máquina, herda a rastreabilidade da base e monta a fila do que foi **liberado**.

**Não faz:** não publica, não fala com a Meta, não abre rede, não cria conteúdo, não homologa e não
decide formato.

Quem homologa e quem libera é o soberano. Publicar é ato autorizado, separado.

## 2. A cadeia

```
ficha (docs/analyses/<gaveta>/*.md)      INSUMO — não publicável
   ↓
peça editorial                            BASE HOMOLOGÁVEL
(estado da arte | artigo didático | artigo científico)
   ↓
peça de mídia                             ESTA ESTEIRA (produção verificada)
(carrossel | vídeo curto | estático)
   ↓
liberação                                 ATO HUMANO, ÚNICO
(revisão editorial + autorização + destino)
   ↓
fila de publicação                        item = peça + canal + data + hora
   ↓
publicação                                ATO AUTORIZADO
```

**A ficha não vira mídia.** Uma ficha científica declara limites e ressalvas que uma legenda de 2.200
caracteres não comporta; traduzi-la direto para post transforma ressalva em afirmação. A peça
editorial é o que já passou por essa síntese.

**Produzir não exige homologação; publicar exige.** Os agentes podem elaborar artigos, roteiros e
peças enquanto a coleção está em preparação. Só a liberação final depende de homologação documental.
Antes, um `em-revisao-documental` derrubava a peça — isso transformava homologação em pedágio de
produção, exatamente o que a reconciliação R1 mandou corrigir.

## 3. Duas homologações, e não se confundem

| | documental | editorial |
|---|---|---|
| **o que é** | estado do documento no Acervo (`estado_documental`) | ato do soberano que libera a peça para publicação |
| **quem faz** | curadoria, pelos estados de `GOVERNANCA_DOCUMENTAL.md` | `FABIO_SOBERANO` |
| **onde aparece** | frontmatter do documento | bloco `liberacao` da peça de mídia |
| **o que bloqueia** | a liberação | a fila |

Estados documentais aceitos: `homologado-documentalmente`, `publicado-no-zenodo`, `depositado-no-zenodo`,
`publicado-no-acervo`, `edicao-publica-conformada`, `edicao-revisada-para-acervo`, `curado`,
`revisado-com-fonte-integral` — os dois últimos porque `GOVERNANCA_DOCUMENTAL.md:86/88` os declara
equivalentes a homologado.

Critério editorial de liberação: a coleção tem **estado da arte E ao menos um artigo**, didático ou
científico, cada ponteiro resolvendo dentro do repositório, apontando para arquivos distintos e
declarando o próprio papel no frontmatter.

**Medição de 2026-11-20 (checkout limpo, parser de frontmatter do gate):** 338 arquivos `.md`;
238 em `em-revisao-documental`; 44 no estado canônico; 98 no conjunto aceito; **13 estado da arte;
0 artigos**. Consequência: nenhuma coleção tem o par completo — falta artigo, não falta tudo.

**Como reconferir:** o número vale pelo comando. `grep` literal subconta (43 contra 98) e PyYAML
rejeita o frontmatter de 3 `index.md` que o gate aceita (235/97 contra 238/98). Vale o parser do gate.

## 4. Os portões

Sete verificações automáticas, sem etapa administrativa nova. Cada uma responde a uma pergunta
diferente; nenhuma delas é aprovação.

| portão | pergunta | como falha |
|---|---|---|
| P0 | a peça tem a forma declarada? | recusa nomeada: tipo errado, campo desconhecido, `id` vazio ou repetido, limite estourado |
| P1 | a origem é documento editorial de verdade? | recusa `tipo=ficha`, caminho fora da raiz, ou origem cujo `tipo_documental` **efetivo** não é editorial |
| P2 | a origem é a que foi medida? | recusa origem que não resolve (bytes ou `git cat-file`) e hash divergente |
| P3 | a coleção satisfaz o critério? | recusa coleção sem estado da arte, sem artigo, papéis trocados, mesmo arquivo nos dois papéis |
| P4 | o formato cabe no conteúdo? | carrossel exige 2 a 20 itens |
| P5 | o texto cita o que diz citar? | recusa fonte que não existe literalmente no corpo |
| P6 | o ato de liberação é íntegro? | recusa hash arbitrário, conteúdo alterado, autoridade inventada, data inválida, autorização sem destino |

P7 (`verificar_midia.py`) responde a **três** perguntas separadas: (a) os bytes conferem com hash e
dimensão; (b) o manifesto é internamente coerente; (c) a URL declarada **responde** de fato. As três
são diferentes; a terceira fica `NAO_VERIFICADO` sem rede ou sem URL.

**P1 confere a natureza declarada pela origem, não o que a peça diz que ela é.** Uma peça pode
declarar `deriva_de.tipo: estado-da-arte` e apontar para uma ficha; o frontmatter da ficha é quem
decide.

**P5 é verificação textual, não semântica.** Confere que a string existe no corpo; não julga se a
peça interpretou bem. Esse julgamento é humano.

## 4A. As duas vias de P2 — e por que a segunda não afrouxa nada

- **Via BYTES:** a peça editorial está no worktree; o `sha256` é calculado dos bytes presentes.
- **Via PONTEIRO:** a peça editorial está publicada em outro branch/remoto — caso normal, porque
  homologado e publicado no Git já é fonte. O lote declara `sha256` **e** `ref`, e o gate confere por
  `git cat-file` no próprio clone, sem rede.

O que a via PONTEIRO não faz: assumir. Ref inexistente é recusa nomeada; hash divergente é recusa.
Consequência: **nenhum lote real falha porque a peça não está mesclada na `main`.**

## 5. O ato de liberação — um só

Aprovação concentrada: uma decisão, um bloco, e ele diz tudo o que importa.

```json
"liberacao": {
  "autoridade": "FABIO_SOBERANO",
  "em": "2026-12-01T09:20:00-03:00",
  "canal_da_aprovacao": "telegram:18335",
  "revisao_editorial": "aprovada",
  "autoriza_publicacao": true,
  "destino": ["instagram:@takwaratec"],
  "hash_do_conteudo": "<sha256 calculado por --selar>"
}
```

- **Um ato** registra revisão editorial **e** autorização, quando concedida.
- **Identidade, data, conteúdo e destino** ficam registrados no mesmo lugar.
- **`autoriza_publicacao: false`** não é recusa: é revisão aprovada sem autorização de publicar —
  a peça fica pronta, fora da fila.
- **Sem `liberacao` não há erro**: a peça é produzida e verificada, e a pendência é declarada.

**O que o hash prova e o que não prova.** `sha256` prova que o conteúdo aprovado é o conteúdo
apresentado; **não prova identidade nem consentimento**. `autoridade` é declaração; `canal_da_aprovacao`
aponta para onde o ato aconteceu. O sistema não autentica pessoas — e não finge que autentica.

## 6. Rastreabilidade herdada (o operador não redigita o que a máquina sabe)

A peça declara **origem e coleção**; o restante vem dos arquivos:

```
python3 ops/midia-publicacao/montar_lote.py --selar <lote>.json --raiz .
python3 ops/midia-publicacao/montar_lote.py --lote <lote>.json --raiz .
```

`--selar` preenche `sha256_da_peca` e o hash da liberação. A saída traz `rastreabilidade` com título,
ano, DOI, tipo documental, estado e gaveta **lidos do frontmatter da origem**. DOI, locators, hashes e
referências não são pedidos de novo a cada derivado.

Uma base homologada serve a muitos derivados: carrossel, vídeo, podcast, estático. Não se homologa a
coleção outra vez para cada peça.

## 7. Como o operador usa

```
cd <raiz-do-repositorio>

# prova que o gate está ligado
python3 ops/midia-publicacao/montar_lote.py --selftest

# sela os hashes do lote (a máquina faz o trabalho repetitivo)
python3 ops/midia-publicacao/montar_lote.py --selar <lote>.json --raiz .

# monta
python3 ops/midia-publicacao/montar_lote.py --lote <lote>.json --raiz .

# verifica a arte final (três perguntas)
python3 ops/midia-publicacao/verificar_midia.py --manifesto <manifesto>.json [--sem-bytes] [--publico]
```

Saída esperada do selftest: `{"selftest":"PASS","modo":"EM_MEMORIA","controles_negativos":59,"controles_positivos":8,"falhas":0}`.
Verificador: `9` negativos e `2` positivos. Os contadores são **calculados** do tamanho das listas —
contador digitado já divergiu do código em auditoria.

Os dois selftests rodam **sem diretório gravável** (memória + `git cat-file`). É deliberado: o auditor
executa em sandbox read-only, e um selftest que exige escrita não pode ser executado por quem audita.

`montar_lote.py` sai com código 1 quando há recusa — recusa é resultado, não erro.

## 8. O que fazer quando a esteira recusa

- **P1 tipo=ficha** → a peça tentou publicar ficha. Produza estado da arte ou artigo antes.
- **P1 natureza efetiva** → a origem se declara ficha/instrumento/índice. Não é editorial; declarar outro tipo na peça não muda o documento.
- **P2 origem ausente** → sem bytes e sem `ref` não há prova. Declare o `ref` ou traga os bytes.
- **P3 papéis trocados** → o artefato no papel de estado da arte não se declara estado da arte, ou o artigo não é artigo.
- **P5 fonte não encontrada** → a mídia afirma algo que a origem não contém literalmente. Corrija o texto ou a fonte; **nunca** solte o portão.
- **P6 hash divergente** → a peça mudou depois da liberação. Libere os bytes novos.
- **Liberação pendente** (não é erro) → a coleção está em revisão ou falta o ato humano. Produza e revise; publique não.

## 9. Pendências declaradas (com dono)

| # | pendência | estado | dono |
|---|---|---|---|
| 1 | hospedagem pública (Opção A) não implementada | desenhada | Fábio (credencial Cloudflare) |
| 2 | chave `age` sem cópia verificada fora do Mac | NÃO VERIFICADO | Fábio |
| 3 | nenhum lote publicado: não há arte em URL pública | fato | — |
| 4 | fase 2 (publicação programada) não iniciada | não iniciada | — |
| 5 | modo desenvolvedor não cria gaveta invisível no Instagram | NÃO VERIFICADO no App real | Fábio |
| 6 | `instagram_business_content_publish` | NÃO VERIFICADO | Fábio |

## 10. Limites declarados

- **P5 é verificação de string, não de sentido.** Garante que a fonte citada existe; não garante interpretação correta.
- **A esteira não impede publicação manual fora dela.** Garante que o que passa por ela é rastreável.
- **A arte não é validada por pixel.** A rastreabilidade da arte é por `prompt_usado` + `confere_com`.
- **O hash não autentica pessoas.** Integridade sim, identidade não.
- **Selftest não é prova funcional.** Nove rodadas de auditoria testaram o gate; o que prova a cadeia é o piloto com material real — e ele está em `piloto/`.

## 11. Histórico de auditoria, sem inflar

**Oito rodadas de auditoria técnica (TECO / Luna Medium)**, todas com defeito real, encerradas por
decisão do soberano — auditoria em loop não converge, porque achar defeito é a função do auditor.
**Uma auditoria externa de planejamento e governança** (Sol), veredito `ADEQUADO COM RESSALVAS`, que
produziu esta reconciliação.

A soma correta é **8 + 1**, não "nove rodadas técnicas". Registro completo em `AUDITORIA_TECO_R1.json`.
