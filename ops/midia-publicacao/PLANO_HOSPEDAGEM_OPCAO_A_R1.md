# Plano de hospedagem pública das artes — Opção A (Assets do Worker)

STATUS=PROPOSTA · NÃO VIGENTE · FASE 2 DO PILOTO
DATA=2026-11-20
FRENTE=INTEGRACAO_MIDIAS_SOCIAIS
DECISÃO=FABIO_SOBERANO 2026-11-20: "prossiga com A para o piloto, uma vez que já está em funcionamento e estamos em fase de teste"

NOTA SOBRE A CITAÇÃO: "já está em funcionamento" refere-se ao SITE institucional (`acervo-web-preview`),
declarado pelo soberano como operante — não ao caminho `/midia/...`, que NUNCA foi medido. O Worker
servindo arte é NÃO VERIFICADO (tabela §5, item 1). A citação não é evidência de que a hospedagem de
mídia funciona: ela registra apenas de onde veio a escolha da opção A.
REPO_DA_HOSPEDAGEM=takwaratec/TakwaraTec-Acervo-Web
WORKER=acervo-web-preview

## 1. Por que a Meta precisa de URL pública

A Graph API **não aceita upload de arquivo**. Ela recebe `image_url` / `video_url` e **baixa a imagem
sozinha**. Consequências que definem o desenho:

- a URL tem de ser alcançável **sem autenticação**, por IP da Meta, fora do seu navegador;
- tem de devolver o **bytes da imagem** diretamente, não uma página HTML com redirect;
- tem de ser **estável** entre a criação do contêiner e a publicação (a Meta pode buscar de novo);
- requisitos de mídia: JPEG, até 8 MB, largura 320–1440 px, proporção entre 4:5 e 1.91:1;
- **carrossel: todos os slides são cortados pela proporção do PRIMEIRO**. O primeiro slide define o
  enquadramento dos outros. Por isso o gate tem de conferir proporção idêntica nos 12/20 slides.

## 2. O desenho A — assets do Worker existente

Medido no repositório em 2026-11-20:

```
wrangler.jsonc
  "name": "acervo-web-preview"
  "main": "worker.js"
  "assets": { "directory": "./dist/", "binding": "ASSETS", "not_found_handling": "404-page" }

worker.js
  l.36  return env.ASSETS.fetch(request);     # tudo que não é /contact cai nos assets
```

Isso significa: **qualquer arquivo publicado em `dist/` vira URL pública** servida pelo Worker.

### 2.1 O problema do `dist/` e por que não se publica ali direto

`dist/` está no `.gitignore` e é **gerado** por `npm run build` (Astro). Três consequências:

- arquivo colocado em `dist/` **desaparece no próximo build**;
- não há histórico Git de quando cada arte subiu;
- dois deploys simultâneos podem apagar arte do outro.

Portanto a arte **não mora em `dist/`**. Ela mora numa pasta-fonte versionada e é **copiada para
`dist/` pelo processo de build**, com manifesto. O `dist/` é artefato, nunca fonte.

### 2.2 Estrutura proposta

```
TakwaraTec-Acervo-Web/
  midia-publicacao/                     ← FONTE, versionada, JSON + manifesto (NUNCA os JPEG)
    <LOTE>/manifesto.json               ← ponteiro de cada slide
    <LOTE>/MANIFESTO_SHA256.txt
  public/                               ← já existe no repo; o Astro copia para dist/
    midia/<LOTE>/01.jpg …               ← os bytes das artes
```

O Astro copia `public/` para `dist/` no build. Então `public/midia/<LOTE>/01.jpg` chega em
`https://acervo-web-preview.<subdominio>.workers.dev/midia/<LOTE>/01.jpg`.

**Mas `public/` é versionado** — e binário em Git é exatamente o que a regra de custódia proíbe
(histórico não encolhe). Aqui está o ponto que precisa da sua decisão:

| variante | onde ficam os JPEG | histórico Git | complexidade |
|---|---|---|---|
| A1 | `public/midia/…` versionado | cresce ~3,6 MB por carrossel de 12 slides | mínima — é o caminho padrão do Astro |
| A2 | `public/midia/…` **ignorado** no Git, servido do disco no deploy | não cresce | média — exige passo de cópia no build e manifesto para saber o que deveria estar lá |
| A3 | bucket R2 separado | não cresce | alta — credencial nova, fora do escopo desta fase |

**Recomendação: A2**, porque mantém a promessa "artes não entram no Git" sem inventar bucket agora,
e o manifesto resolve a pergunta "quais artes deveriam estar no ar". O custo é que **artes
ignoradas no Git não sobrevivem a um clone limpo** — quem clonar não reproduz o site com as artes.
Isso é uma limitação real e precisa estar escrita, não escondida.

Se você preferir simplicidade sobre pureza, A1 (versionar) é defensável para piloto de 1 carrossel:
3,6 MB uma vez. O erro seria versionar 20 carrosséis e descobrir depois.

## 3. O portão novo que esta fase exige

O montador atual (`montar_lote.py`) não valida imagem — está declarado no schema. Para a Opção A ele
precisa de um portão **P7 — mídia servível**, que só roda quando o lote declara `hospedagem`:

| checagem | como | falha |
|---|---|---|
| arquivo existe na pasta-fonte | `Path.is_file()` | recusa |
| extensão e magic bytes são JPEG | `FF D8 FF` nos 3 primeiros bytes | recusa |
| bytes ≤ 8 MB (`8388608`) | `len()` | recusa |
| proporção entre 4:5 e 1.91:1 | lida dos bytes do JPEG (sem Pillow) ou declarada no manifesto | recusa |
| **todos os slides com a mesma proporção do primeiro** | comparação contra o slide 1 | recusa — é o corte do carrossel |
| `sha256` do slide confere com o manifesto | recomputa | recusa |
| URL declarada corresponde ao caminho | comparação literal | recusa |
| nenhum JPEG rastreado no Git (variante A2) | `git ls-files --error-unmatch` | recusa |

O ponto crítico é o **quinto**: se os slides tiverem proporções diferentes, a Meta corta todos pelo
primeiro e os demais perdem conteúdo **sem erro nenhum**. O defeito aparece no post publicado, não no
lote. Esse é o tipo de falha que o portão existe para impedir.

## 4. Ordem de execução do piloto

1. **Hoje, sem credencial**: implementar P7 no montador + selftest com controle negativo; escrever
   `manifesto.json` de exemplo com um JPEG sintético de teste gerado localmente.
2. **Quando você estiver na base**: `npx wrangler login` no `TakwaraTec-Acervo-Web`, `npm run build`,
   conferir que `dist/midia/<LOTE>/01.jpg` existe, `npx wrangler deploy`.
3. **Verificação pública** — a única prova que vale, executada por `curl` de fora:
   `curl -sI <url>` → `200`, `content-type: image/jpeg`, `content-length` igual ao local.
   Worker responde 200 para arquivo que ele não tem? Não — `not_found_handling: 404-page` devolve 404.
   Mas **confirme**, não presuma.
4. **Só então** criar o contêiner na Meta e publicar — que é a fase seguinte e depende de permissão.

## 5. O que ainda não está provado

| # | o que | estado | dono |
|---|---|---|---|
| 1 | o Worker `acervo-web-preview` está no ar e serve `/midia/...` | NÃO VERIFICADO (sem credencial Cloudflare) | Fábio |
| 2 | o deploy do Worker não apaga arte de lotes anteriores | NÃO VERIFICADO — `dist/` é reconstruído a cada build | Fábio/eu no piloto |
| 3 | limites de cache/banda do `workers.dev` para servir 12 JPEG por publicação | NÃO MEDIDO | eu, no piloto |
| 4 | a Meta consegue alcançar url de `workers.dev` (não bloqueada) | NÃO VERIFICADO — primeiro teste real é o contêiner | eu, no piloto |
| 5 | proporção lida sem Pillow (parser de header JPEG) funciona nos 12 slides reais | A IMPLEMENTAR | eu |

## 6. Riscos declarados

- **Arte em URL pública vaza antes da hora.** Enquanto o lote está em `Fases 1`, qualquer pessoa com
  a URL acessa. Mitigação: nome opaco por lote (`<LOTE>` não deve conter o título do post) e só
  publicar a arte no deploy imediatamente anterior à publicação. Não há autenticação possível — a Meta
  não autentica.
- **Deploy é destrutivo por natureza em `dist/`.** Se o build rodar sem as artes no disco, o deploy
  **remove do ar** as artes dos lotes anteriores. Por isso A2 precisa de manifesto e de um passo que
  confira "todas as artes do manifesto existem em `public/`" **antes** do deploy.
- **Não há rollback automático.** Voltar exige redeploy da versão anterior no Cloudflare.

## 7. Fora de escopo desta fase

`NO_DEPLOY` até autorização na base · `NO_META_APP_MUTATION` · `NO_SECRET` · nenhuma alteração em
`worker.js` · nenhuma alteração em `wrangler.jsonc` sem contrato próprio.
