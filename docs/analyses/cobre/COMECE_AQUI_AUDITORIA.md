---
tipo_documental: sintese-critica
estado_documental: historico
responsavel_curadoria: Fabio F. Resck
frente: BAMBU-SCIENCE
gaveta: bambu-tratamento
origem_documental: frente absorvida COBRE (2026-11-28)
nota_de_metadado: front matter acrescentado na absorcao; o corpo nao foi reescrito
---

# Comece por aqui — pacote de auditoria da gaveta COBRE

Este diretório tem três coisas que se confundem de propósito, e uma que não deve ser confundida.

## A entrada é o ponteiro, e ele fica fora daqui

```
ops/command-center/auditoria-atual/COBRE.json
```

O ponteiro diz, em campos separados, **qual commit** contém o manifesto, **qual commit** contém os
bytes auditados, e o **sha256** de cada uma dessas duas peças. Leia nesta ordem:

1. o ponteiro, no commit da branch que você recebeu;
2. o manifesto, no `manifest_commit` que o ponteiro indica — confira `sha256_do_manifesto`;
3. o `HASHES_RESPONSE`, no mesmo `manifest_commit` — confira `sha256_do_hashes_response`;
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
lease. Tudo o que sustenta as afirmações do artigo está copiado byte a byte em
`docs/analyses/cobre/fontes/` e `docs/analyses/cobre/fichas/`, e o manifesto lista os 28 arquivos
com sha256.

## O que o hash prova, e o que não prova

Hash prova que o arquivo servido é o arquivo listado. **Não prova** que o arquivo diga o que o texto
diz que ele diz. Essa parte é leitura, e é para isso que existe a auditoria.
