# Gaveta limpa HIS/ATHIS — aquisição e custódia (estágio 3)

**Frente:** `hermes/his-athis-r4-gaveta-20261128` · worktree `his-athis-gaveta-r4`
**Data:** 28/11/2026 · **Release 1:** intocado, histórico até a homologação do Release 2.

## 1. O que esta etapa fez

Baixou o **binário de cada obra alcançável** e conferiu que é PDF de verdade (magic bytes `%PDF-`,
>20 KB, páginas contadas). Nada entrou por resumo: o que não tem binário está em
`LACUNAS_AQUISICAO.md` com o código HTTP medido.

## 2. Medição

| Estado | Obras | Páginas |
|---|---|---|
| **Custodiado** | **53** | **7.762** |
| Sem PDF custodiado | 44 | — |
| Total no inventário | 97 | — |

**Correções da auditoria:** quatro arquivos nasceram como `a-<ano>-…` porque o front matter do acervo trazia `autores: a`; o sobrenome passou a sair do slug catalográfico da pasta de origem (`joyce-santos-2009` → `santos`). O `RENOMEACAO.json` casava por prefixo de título e produziu transições falsas (`scotton-2020 → tavares-2023`); agora casa por chave do inventário, com 7 transições conferidas. Divergência de ano no nome: 0 (as duas que pareciam divergir têm sobrenome composto — `magalhaes-neto-2025`, `suassuna-fernandes-2010`).

**Nomes:** 97 arquivos derivados do front matter (`<sobrenome>-<ano>-<tema>`), **zero** com prefixo de
lote ou `sem-autor`. As trocas de nome estão em `RENOMEACAO.json`.

## 3. Rotas que funcionaram — e por que as outras não

O erro da primeira rodada foi tratar todo repositório como "link direto". Cada host publica o binário
por um caminho próprio:

- **UFSC** — a landing está atrás de WAF (`RedeUFSC`); o **OAI-PMH está aberto** e o formato `ore`
  publica a URL do bitstream. Rota: `oai/request?verb=GetRecord&metadataPrefix=ore&identifier=…`.
- **UFMS** — DSpace 7 responde **multipart**; o PDF é recortado dos bytes originais (não reencodado).
- **UnB / Tainacan** — a página publica `10482/<n>`; o DSpace antigo serve o bitstream desse handle.
- **BDTD** — a página do registro não é a obra: o link do repositório está **dentro** dela.
- **UFRGS / UNICAMP / UFV** — handle aponta para outro domínio (Lume, acervo JS, Locus com Anubis).

## 4. Bloqueios declarados (não são ausência de obra)

`locus.ufv.br` (Anubis), `repositorio.ufsc.br` (WAF, contornado por OAI), `guaiaca.ufpel.edu.br` (403),
`repositorio.cruzeirodosul.edu.br` (403), `tede2.pucsp.br` (468), `rima.ufrrj.br` e `bdtd.uerj.br`
(conexão morta), `hdl.handle.net/20.500.12733` (PDF por JS).

## 5. O que ainda falta para o motor

1. **Extração, crivo e âncoras** das 53 (o piloto já tem o pipeline: `mtcc_piloto_r4.py`).
2. **Análise semântica por parágrafo** — sobre parágrafos reconstruídos, não sobre blocos do PDF:
   no piloto, 1.477 blocos deram 410 parágrafos analisáveis.
3. **Fichas** com claims e página.
4. **Auditoria Teco** da mesclagem antes de qualquer ficha.

## 6. Caminho dos binários

`/Users/fabiotakwara/.hermes/cache/scratch/his-athis-r4-r1/obras/custodia/pdf/` — **954 MB**, 53 PDFs.
Não entram no git: o manifesto com sha256, páginas e origem está em `custodia/MANIFESTO_BINARIOS.txt`.
Custódia definitiva no Drive aguarda a reconexão OAuth (`rclone gdrive-pessoal-rw`, `invalid_grant`).
