# Molde homologado — proveniência

`molde.css` e `molde.js` foram extraídos **byte a byte** de uma peça já homologada da casa:

- peça de origem: `O-boro-explicado-do-zero.html` (gaveta boro, 2026-11-24)
- extração: `<style>` -> `molde.css` (7.993 bytes); `<script>` -> `molde.js` (4.031 bytes)

## O que NÃO se altera

- `--barra-h` medido em runtime e publicado no `documentElement`; a folga é
  `calc(var(--barra-h) + 20px)`. **Nunca** número fixo.
- `history.replaceState` em vez de `location.hash` na navegação por clique: com hash, o
  navegador posiciona a seção e o `scrollTo(0,0)` desfaz — dois donos da mesma rolagem.
- barra do celular em **linha única rolável** (`flex-wrap:nowrap`), nunca empilhada.
- `@media print` emite **todas** as seções.

## O que esta peça alterou

Apenas a **paleta de destaque** (verde do boro -> tom do cobre), em bloco `:root` declarado
no fim do CSS da peça. Estrutura, mecânica e JS: intactos.

## Regra de conteúdo

Todo `<td>` carrega `data-l` com o texto do cabeçalho — é o que faz a tabela virar cartão
rotulado no celular. O gerador valida 100% das células.
