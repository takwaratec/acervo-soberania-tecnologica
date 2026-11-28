---
schema: ACERVO_README_GAVETA_R1
gaveta: soberania-social
frente: SOBERANIA-SOCIAL
aberta_em: 2026-11-26T18:57:55Z
ledger_commit: 0ddb2d4e94614febfed7037ce65d211a1a38177d
titulo: "Soberania Social — desigualdade, território e política pública"
estado_documental: em-revisao-documental
homologacao_automatica: false
versao: 1
data_revisao: 2026-11-28
responsavel_curadoria: Fabio Takwara
assistencia_documental: agente de IA, sujeito a revisao humana
---

# Soberania Social

Gaveta do eixo social da coleção Soberania Tecnológica. Existe para tratar **desigualdade,
território e política pública** com o mesmo rigor documental que as gavetas técnicas tratam
material e norma.

## O que esta gaveta é

O objeto não é "temas sociais do acervo". É uma pergunta com consequência prática: **por que a
desigualdade brasileira se reproduz apesar de tudo que já se escreveu sobre ela, e o que uma
política pública pode fazer que ainda não foi tentado.**

A obra de Graeber & Wengrow entra como **conteúdo absorvido** — não como frente irmã. A gaveta-mãe
(`projetos/gaveta-graeber-wengrow`) continua existindo como origem histórica, e nada dela é
apagado. O que muda é que a curadoria passa a ser feita aqui, pela régua atual.

## Pilares

Já custodiados, sujeitos a re-curadoria no schema `MTCC/FICHA/2`:

- Darcy Ribeiro — *O povo brasileiro* (1995) e *Teoria do Brasil* (2014)
- Milton Santos — *Por uma outra globalização* (2001)
- Florestan Fernandes — *A revolução burguesa no Brasil* (1976)
- Paulo Freire — *Pedagogia do oprimido*, manuscrito autógrafo de 1968 (CC BY-SA 4.0, Acervo Paulo Freire)
- Maricato (2003, 2011), Rolnik (1999), Bonduki (1999) — homologados documentalmente

Aquisição nova declarada: Bauman, Zuboff, Christophers, Dean, Varoufakis. Contraditório obrigatório:
Scheidel, *The Great Leveler* — sustenta a tese contrária e é citado pela obra central.

## Recorte aprovado

**192 fichas do eixo social**, não as 422 da coleção. Dentro delas:

| classe | quantidade |
|---|---|
| com PDF custodiado | 96 |
| sem PDF localizado | 82 |
| artefato interno (não é fonte externa) | 14 |
| **fontes reais** | **178** |

As fichas que hoje vivem em outras gavetas entram aqui **depois** de reprocessadas pelo
`MTCC/FICHA/2` — com `claims` tipados e `cobertura_materiais` calculada. Ficha sem claims reprova
por cobertura, não por opinião de revisor.

## O que esta gaveta NÃO é

Declarado com nome, porque foi exatamente a proximidade que produziu o defeito de escopo corrigido
em 2026-11-28:

- **não é** `docs/analyses` — a coleção é catálogo, não gaveta
- **não é** `cobre` — sulfato de cobre, CCA/CCB e exposição ocupacional são de outra frente
- **não é** `bambu-estrutural`, `bambu-tratamento`, `bambu-fitossanitario` nem `bambu-carbono`
- **não é** `pu-vegetal`
- **não é** `boro` — e nada do boro pode ser transportado para cá

A frente declara escopo em `docs/analyses/soberania-social` e
`_privado/governanca-operacional/extracoes/soberania-social`. Nada além disso.

## Estado

`SEM_FICHAS_MEDIDAS` — esta gaveta nasce com este README e nenhuma ficha medida. Declarar o
contrário seria inventar cobertura. A primeira leva de fichas entra quando passar pelo motor no
protocolo atual, com vínculo ficha→arquivo provado por `sha256`.

## Entregáveis previstos

Três, com a mesma base factual e réguas opostas:

1. artigo científico denso — prova, controvérsia, limite
2. artigo de blog — sucinto, enfático, pragmático
3. peça para o legislativo — frentes parlamentares de direitos humanos, igualdade e gênero

## Registro

- frente aberta: `refs/heads/r4-claims` → `frentes_abertas/SOBERANIA-SOCIAL.json`
- escopo corrigido em 2026-11-28: commit `0ddb2d4e` (os valores anteriores ficam em `correcoes[]`,
  nada é apagado)
- gaveta declarada no catálogo: `ops/command-center/transicao-r4/GAVETAS_R4.json`
