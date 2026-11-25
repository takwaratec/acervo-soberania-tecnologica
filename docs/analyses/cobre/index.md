---
estado_documental: em-revisao-documental
responsavel_curadoria: Fabio F. Resck
---
# Gaveta — cobre

Frente `COBRE` (aberta 2026-11-24T13:59:13Z no ledger R4, commit `a37861ff`).
**Capítulo 2** da série *tratamentos convencionais do bambu*; o capítulo 1 é o
**boro** (`docs/analyses/boro/`).

A ligação entre as duas gavetas está em
[`docs/analyses/boro/BOOTSTRAP_COBRE_20261124.md`](../boro/BOOTSTRAP_COBRE_20261124.md),
que é documento de ligação — **não** é homologação nem resultado de pesquisa.

## Escopo

Entra: **sulfato de cobre e sais de cobre** como preservante; **CCA e CCB** como
família de preservantes de cobre (arsênio e cromo entram por serem componentes,
não por serem o objeto); **exposição ocupacional e inalação** na cadeia de
tratamento e acabamento — poeira de bambu cortado/lixado, EPI, e o eixo de
**voláteis, vernizes, acrílicos e isocianatos**.

**Não entra:** o boro como objeto (tem gaveta própria); concreto.

**A cindibilidade dos voláteis é decisão registrada e reversível:** o pacote
`ago_27_VOCs` entra aqui porque a pergunta que une cobre + vernizes + acrílicos é
a mesma — o que se aplica ao bambu e o que isso faz com quem aplica e quem
habita. Se o soberano quiser cindir, o pacote sai inteiro sem quebrar nada.

## Por que é frente separada do boro — toxicologia oposta

| Dimensão | Boro | Cobre |
|---|---|---|
| Papel biológico | sem função essencial estabelecida em humanos | **micronutriente essencial** |
| Efeito crítico | toxicidade do desenvolvimento | efeitos gastrointestinais agudos |
| Ordem do limite | mg B/kg/dia (MRL 0,2) | mg Cu/L na água (NOAEL 2) |
| Toxicidade aquática | dezenas de mg/L | **1–2 µg/L** |
| Classificação UE | Repr. 1B / H360FD | Aquatic Acute 1 / Chronic 1 (H400/H410) |

**Nenhum número atravessa de uma gaveta para a outra.**

## Conteúdo

| Artefato | Função |
|---|---|
| `00-mapa-reprocessamento.md` | Passo 8 do bootstrap executado: inventário verificado, síntese das 6 fichas, divergências preservadas, o buraco da NR-15, o que falta custódia |
| `INVENTARIO_GAVETA.json` | Estado real de cada conjunto de fontes |

## Camada privada

```
_privado/fichas/ago_28_CCA_CCB/                    6 fichas (ficha-em-revisao)
_privado/fontes-documentais/ago_28_CCA_CCB/        6 PDFs + canonical + md + manifest
_privado/fontes-documentais/ago_27_VOCs/           45 arquivos (38 PDFs), inclui NR-15 e NR-6
_privado/governanca-operacional/extracoes/cobre/   escopo de escrita desta frente
```

PDF, extração e tabela derivada de artigo permanecem privados; do artigo se extrai
o dado e se produz tabela própria.

## Achado que define a gaveta (até aqui)

A **NR-15 não tem limite de tolerância para cobre, para arsênio inorgânico, para
cromo(VI) nem para poeira de madeira** — verificado no texto custodiado. O que ela
tem de mais próximo são a **arsina** (gás), o **ácido crômico (névoa)** e o
**quartzo** da sílica, que não são os agentes desta cadeia. Não é limite alto: é
ausência. A referência quantitativa tem de vir de fora (NIOSH/ACGIH) e ser
declarada como estrangeira.

## Estado

`em-revisao-documental` · `homologacao_automatica: false` · **não homologado**.
As seis fichas herdadas seguem `ficha-em-revisao` e **não** foram promovidas.

## Aviso

Esta gaveta **não** é homologação, certificação, validação experimental nem
autorização de publicação.
