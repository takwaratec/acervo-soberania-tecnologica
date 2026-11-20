# MAPA DE RESTAURAÇÃO R1 — reerguer a operação TakwaraTec numa máquina nova

STATUS=PROPOSTA · NÃO VIGENTE
DATA=2026-11-20
FRENTE=INTEGRACAO_MIDIAS_SOCIAIS
AUTORIDADE=FABIO_SOBERANO, 2026-11-20: "o Git é a fonte da verdade; os binários ficam no drive; se eu precisar reconstruir em outra máquina, tenho as fontes e tenho o mapa de como restaurar"

## 0. A frase que este mapa existe para tornar verdadeira

> Perder o Mac não pode significar perder a operação.

Ele só é verdade se **quatro camadas** sobreviverem, e cada uma tem um dono diferente:

| camada | o que guarda | onde | sobrevive à perda do Mac? |
|---|---|---|---|
| **1. Fonte da verdade** | texto, regras, código, manifesto, decisões | **GitHub** (repos `takwaratec/*`) | SIM |
| **2. Bytes** | PDFs originais, artes, lotes cifrados | **Google Drive** (remotos rclone) | SIM, **se a chave existir** |
| **3. Segredo** | chave privada `age`, tokens, senhas | **fora do Git e fora do Mac** | **NÃO — este é o elo frágil** |
| **4. Serviço** | site no ar, Worker servindo arte | **Cloudflare** | derivado: reemite-se pelo deploy |

A camada 3 é a única que o Git não reconstrói e o Drive não abre sozinho. Sem ela, as camadas 1 e 2
existem e não se encontram.

## 1. O que o Git reconstrói sozinho

Com apenas um `git clone` e nada mais, você recupera:

- o Acervo inteiro (`docs/analyses/**`): fichas, artigos, estados documentais
- a esteira de publicação (`ops/midia-publicacao/**`): código, esquema, manuais, exemplos
- o ledger R4 e as decisões (`refs/heads/r4-claims` no repo de governança)
- os manifests de mídia (ponteiro com `sha256`, dimensão e URL de cada slide)
- este mapa

**O que o Git NÃO reconstrói:** os JPEG/PDF, a chave `age`, e qualquer credencial.

## 2. Ordem de restauração (comandos literais)

### Passo 1 — repos

```
git clone git@github.com:takwaratec/acervo-soberania-tecnologica.git
git clone git@github.com:takwaratec/TakwaraTec-Laboratorio-Editorial.git
git clone git@github.com:takwaratec/TakwaraTec-Acervo-Web.git
git clone git@github.com:takwaratec/TakwaraTec-Midia-Editorial.git
```

### Passo 2 — o ref do ledger não é uma branch comum

O registro vivo da governança mora em `refs/heads/r4-claims`, que **não vem no clone padrão**:

```
cd TakwaraTec-Laboratorio-Editorial
git fetch origin +refs/heads/r4-claims:refs/heads/r4-claims
git rev-parse r4-claims          # tem de devolver 40 hex
```

Sem esse `fetch` explícito, `status`/`frentes` do runner leem vazio e parece que a frente não existe.

### Passo 3 — ferramentas

```
python3 --version                # 3.11+ basta; a esteira não tem dependência externa
node --version                   # para o Worker e o site (Astro 7.3.1)
npm install                      # em TakwaraTec-Acervo-Web
brew install rclone age          # custódia
```

A esteira (`montar_lote.py`, `verificar_midia.py`) roda com **biblioteca padrão apenas** — isso é
deliberado: uma VM nova não precisa instalar nada para o gate funcionar, e o gate não quebra por
dependência ausente.

### Passo 4 — provar que a esteira voltou viva

```
cd acervo-soberania-tecnologica/ops/midia-publicacao
python3 montar_lote.py --selftest
python3 verificar_midia.py --selftest
```

Esperado: `{"selftest":"PASS",...}` nos dois, exit 0. Se qualquer um reprovar, **pare** — o gate
voltou quebrado e confiar nele é pior que não tê-lo.

### Passo 5 — credenciais, uma a uma (todas se REEMITEM, nenhuma se copia)

| serviço | como reemitir | o que precisa existir antes |
|---|---|---|
| GitHub | chave SSH nova → `ssh-keygen -t ed25519` → colar em github.com/settings/keys | acesso à conta |
| Cloudflare | `npx wrangler login` (ou token escopado no dashboard) | acesso à conta |
| Google Drive | `rclone config reconnect <remoto>:` — **exige navegador nesta máquina** | acesso à conta Google |
| Meta / Instagram | App Dashboard → gerar novo token de usuário | papel no App |
| chave `age` | **copiar do cofre onde ela está** (ver §3) | — |

Nenhum valor de credencial vive neste documento, e nenhum deve passar a viver.

### Passo 6 — site e serviço

```
cd TakwaraTec-Acervo-Web
npm run build                     # gera dist/
ls dist/midia/                    # as artes de mídia precisam estar aqui
npx wrangler deploy
curl -sI https://<worker>/midia/<LOTE>/01.jpg    # esperar 200 + image/jpeg
```

**Sem as artes no disco, o deploy REMOVE do ar as artes de lotes anteriores** (o `dist/` é
reconstruído). Por isso o passo 7 vem antes de qualquer deploy em máquina nova.

### Passo 7 — rebaixar os binários do Drive

```
rclone copy '<remoto>:<base>/midia/<LOTE>' ./public/midia/<LOTE> --checksum
shasum -a 256 ./public/midia/<LOTE>/*.jpg     # comparar com o manifesto no Git
```

Aqui está o ciclo fechando: o **manifesto no Git** diz qual `sha256` cada arte deve ter; o **Drive**
tem os bytes; se os dois baterem, a reconstrução é fiel e não uma aproximação.

## 3. A chave `age` — o elo que não está no Git

Os lotes custodiados são `.tar.zst.age`: só abrem com a **chave privada** X25519. Ela não pode ir
para o Git (vazaria) e não pode existir só no Mac (que é o que pode ser perdido).

Estados possíveis, e o que fazer em cada um:

- **chave só no Mac** → situação atual e é a mais frágil. Criar cópia física (papel dobrado em
  cofre) ou cópia em gerenciador de senhas, e **registrar aqui onde ela está**, não o valor.
- **chave num cofre/gerenciador** → registrar o nome do item, não a senha do cofre.
- **chave perdida e nenhuma cópia** → os `.age` são irrecuperáveis. Se isso acontecer, o registro
  honesto é: "binário custodiado existe e não abre"; o original precisa vir de outra fonte.

**Pendência declarada, com dono:** `FABIO_SOBERANO` — decidir e executar a cópia da chave fora do
Mac, e preencher a linha abaixo.

```
CHAVE_AGE: PENDENTE — localização da cópia de segurança não declarada
```

## 4. O que NÃO é reconstruível, e o mapa tem de dizer isso

- **Histórico de publicação no Instagram.** Se a conta for perdida, nenhum clone a recupera.
- **Tokens antigos.** Todos valem só até expirar; a restauração pressupõe reemissão.
- **Estado local não commitado.** Worktree sujo, stub, arquivo em `dist/`: tudo isso morre com a máquina. Por isso a regra "Git é a fonte da verdade" exige commit antes de considerar algo salvo.
- **Conversas.** Decisão que existe só em chat não está preservada; para valer, precisa virar arquivo no repositório — que é a razão de existir a `DECISAO_ESTEIRA_PUBLICACAO_R1_20261120.md`.

## 5. Ensaio de restauração (o que ainda não foi feito)

Este mapa é **plano, não prova**. Ninguém restaurou de fato numa máquina limpa, e um mapa nunca
testado é um mapa que pode estar errado em qualquer linha.

Ensaio proposto, quando houver VM disponível: clonar os quatro repos numa máquina limpa, rodar os
dois selftests, e reportar **em qual passo parou**. Enquanto esse ensaio não acontecer, o status
honesto deste documento é `PLANO_NAO_TESTADO`.

| # | item | estado | dono |
|---|---|---|---|
| 1 | chave `age` copiada fora do Mac | PENDENTE | Fábio |
| 2 | remotos `drive` / `gdrive-pessoal-*` com token válido | VENCIDO (expiry 2026-11-19) | Fábio |
| 3 | ensaio real de restauração em máquina limpa | NÃO FEITO | ambos |
| 4 | artes de mídia existentes no Drive | NÃO EXISTE AINDA (nenhum lote publicado) | — |
