---
tipo_documental: documento-institucional
estado_documental: em-revisao-documental
responsavel_curadoria: Fabio F. Resck
---
# Comece por aqui — pacote de auditoria da gaveta COBRE

Este diretório tem três coisas que se confundem de propósito, e uma que não deve ser confundida.

## A entrada é o manifesto, e ele tem nome de alvo

```
docs/analyses/cobre/AUDITORIA_SOL_COBRE_MANIFEST_R1_<alvo>.json
docs/analyses/cobre/AUDITORIA_SOL_COBRE_HASHES_RESPONSE_R1_<alvo>.json
docs/analyses/cobre/SELOS.md
```

**Não há ponteiro em `ops/command-center/auditoria-atual/`.** Houve uma versão deste documento que
mandava entrar por `COBRE.json`, arquivo que nunca existiu — referência que admite não existir
continua sendo referência a perseguir. Leia nesta ordem:

1. `SELOS.md`, que lista todos os selos da frente com o sha256 de cada par e o commit em que ele vive;
2. o par do alvo que você recebeu — confira `sha256_do_manifesto` contra o byte do arquivo;
3. o `HASHES_RESPONSE` do mesmo alvo — é o par do manifesto, e sai da árvore junto com ele;
4. só então as fontes, no `alvo_commit`.

## A armadilha, declarada

O manifesto **não pode** conter o hash do commit que o publica. Ele nasce depois do conteúdo, num
commit posterior. Consequência: o commit auditado (`alvo_commit`) carrega, dentro de si, a cópia do
manifesto **da rodada anterior**.

Se você abrir "o manifesto que está no commit auditado" — que é o gesto natural — vai ler o
documento errado e os hashes vão parecer divergentes. Já aconteceu, com um auditor sério, e ele
estava certo em reportar.

Por isso, a partir da rodada do alvo `f64ea849`:

- o nome do arquivo carrega o alvo — `..._MANIFEST_R1_<alvo>.json`. Se o nome não é o alvo que você
  está auditando, o arquivo não vale para a sua auditoria;
- o commit-alvo não contém manifesto nenhum. Melhor ausente que enganoso.

## O que o pacote NÃO alcança

O auditor externo lê apenas o publicado em commit fixo. Não vê `_privado/` (gitignored por desenho,
onde ficam as fontes originais e as fichas antes da publicação), não vê runtime, não vê claim nem
lease.

**Nem todo arquivo de fonte está na árvore.** Os PDFs de terceiro saíram do rastreio
(`governance-check.yml` proíbe PDF versionado); cada um continua em `_privado`, com o sha256 do byte
que estava versionado, declarado em `fontes/CUSTODIA_PRIVADA_PDFS.json`. Para essas fontes o auditor
confere o hash pelo registro e pede o arquivo pelo `caminho_privado` — `git show` não se aplica.

**O extrato textual é curado, não integral.** `fontes/md/` guarda de cada obra apenas o que a peça
cita e o que é nosso: o cabeçalho de identificação, os parágrafos que contêm trecho citado nas fichas
ou número com unidade usada no artigo, e no máximo 40 KB por obra. O texto inteiro permanece no PDF
custodiado e no histórico do git. O que saiu e o que ficou, arquivo por arquivo, com bytes antes e
depois, está em `fontes/SANEAMENTO_CUSTODIA_FONTES.json` — a decisão de guardar o histórico é do gate
humano de custódia.

As fontes estão inventariadas em `fontes/INDICE_FONTES.json`, com identificador estável (`id`), sha256,
bytes, estado de custódia e o número da referência bibliográfica como campo legado — o número muda
quando a bibliografia muda, e identificador não pode mudar.

## O que o hash prova, e o que não prova

Hash prova que o arquivo servido é o arquivo listado. **Não prova** que o arquivo diga o que o texto
diz que ele diz. Essa parte é leitura, e é para isso que existe a auditoria.
