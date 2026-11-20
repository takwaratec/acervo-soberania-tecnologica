# MAPA DE RESTAURAÇÃO — reerguer a operação numa máquina nova

STATUS=PLANO_NAO_TESTADO
VERSAO=R2 (2026-11-20) — sequência corrigida após reconciliação da auditoria externa
DATA=2026-11-20
FRENTE=INTEGRACAO_MIDIAS_SOCIAIS
AUTORIDADE=FABIO_SOBERANO, 2026-11-20: "o Git é a fonte da verdade; os binários ficam no drive; se eu precisar reconstruir em outra máquina, tenho as fontes e tenho o mapa de como restaurar"

**O que mudou da R1:** a R1 estava correta em conteúdo e frágil em ordem — mandava rebaixar binários
antes de ter a chave e listava credenciais no meio do caminho de dados. A R2 passa a ser uma
**sequência executável**, com entrada, saída e critério de verificação por passo.

## 0. A frase que este mapa existe para tornar verdadeira

> Perder o Mac não pode significar perder a operação.

Quatro camadas, cada uma com dono diferente:

| camada | guarda | onde | sobrevive à perda do Mac? |
|---|---|---|---|
| **1. Fonte da verdade** | texto, código, regras, manifestos, decisões | **GitHub** (`takwaratec/*`) | SIM |
| **2. Bytes** | artes, lotes, PDFs originais | **Google Drive** (custódia `.age`) | SIM, **se a chave existir** |
| **3. Segredo** | chave privada `age` | **fora do Git e fora do Mac** | **NÃO — é o elo frágil** |
| **4. Serviço** | site no ar, Worker | **Cloudflare** | derivado: reemite-se por deploy |

## 0.1 A sequência obrigatória

```
ACESSO → CLONE → CREDENCIAIS → CUSTÓDIA → DESCRIPTOGRAFIA
       → CONFERÊNCIA DE HASH → RECONSTRUÇÃO DOS ASSETS → BUILD → VERIFICAÇÃO LOCAL
```

Não pule para o passo seguinte sem verificar o anterior. **A ordem não é estética:** descriptografar
sem chave não acontece; reconstruir assets sem hash confere nada; e a verificação local é o único
sinal de que a operação voltou viva — o clone ter terminado não é sinal nenhum.

### Passo 1 — ACESSO

```
git config --global user.name  "takwaratec"
git config --global user.email "takwaratec@gmail.com"
ssh-keygen -t ed25519 -C "vm-restauracao"
cat ~/.ssh/id_ed25519.pub      # autorizar em github.com/settings/keys
ssh -T git@github.com          # espera "Hi <usuario>! You've successfully authenticated"
```

**Saída:** `ssh -T` autentica. **Se falhar, nada adiante funciona** — resolva aqui.

### Passo 2 — CLONE

```
mkdir -p ~/Takwara/repos && cd ~/Takwara/repos
git clone git@github.com:takwaratec/acervo-soberania-tecnologica.git
git clone git@github.com:takwaratec/TakwaraTec-Laboratorio-Editorial.git
git clone git@github.com:takwaratec/TakwaraTec-Acervo-Web.git
```

**O ref do ledger não vem no clone.** O registro vivo mora em `refs/heads/r4-claims`:

```
cd TakwaraTec-Laboratorio-Editorial
git fetch origin +refs/heads/r4-claims:refs/heads/r4-claims
git rev-parse r4-claims          # tem de devolver 40 hex
```

Sem esse `fetch`, `status`/`frentes` do runner leem vazio e parece que a frente não existe.

**Saída:** três clones + `r4-claims` resolvendo.

### Passo 3 — CREDENCIAIS

**Nenhuma credencial se copia; todas se reemitem.** Nenhum valor entra neste documento.

| credencial | como reemitir | teste mínimo |
|---|---|---|
| GitHub SSH | `ssh-keygen` (passo 1) | `ssh -T git@github.com` |
| Cloudflare | dashboard → API Tokens (Workers Scripts:Edit) ou `npx wrangler login` | `npx wrangler whoami` |
| Meta / Instagram | App Dashboard → novo token de usuário | chamada de teste à Graph API |
| Google Drive | `rclone config reconnect <remoto>:` — exige navegador nesta máquina | `rclone lsd gdrive-custodia:` |
| Zenodo | zenodo.org → Applications | `curl` autenticado ao endpoint |
| GPT Maker | painel do agente Bambusa | widget carregando no site |

### Passo 4 — CUSTÓDIA

```
brew install rclone age
rclone lsd  gdrive-custodia:
rclone ls   gdrive-custodia: --max-depth 2 | head -50
```

**Saída:** contêineres `.age` de nome opaco. **Limite:** sem a chave do passo 5, isto prova
existência, não conteúdo.

### Passo 5 — DESCRIPTOGRAFIA

```
age --version
age -d -i ~/chave-age.txt arquivo.age > arquivo.jpg
```

**Saída:** bytes em claro. **Regra:** a chave nunca entra no repositório, no chat ou em nuvem sem
cifra própria. **Sem a chave, os `.age` são irrecuperáveis** — ver §3.

### Passo 6 — CONFERÊNCIA DE HASH

```
cd acervo-soberania-tecnologica/ops/midia-publicacao
shasum -a 256 -c MANIFESTO_SHA256.txt
python3 verificar_midia.py --manifesto <manifesto-do-lote>.json --raiz-public <dir-dos-bytes>
```

**Saída:** `11/11 OK` no manifesto. Hash divergente = arquivo errado ou corrompido: rebaixe de novo,
não "ajuste" o manifesto.

### Passo 7 — RECONSTRUÇÃO DOS ASSETS

```
rclone copy '<remoto>:<base>/midia/<LOTE>' ./public/midia/<LOTE> --checksum
shasum -a 256 ./public/midia/<LOTE>/*.jpg     # comparar com o manifesto no Git
```

O manifesto é a autoridade sobre caminho e hash — não a memória de quem restaura.

### Passo 8 — BUILD

```
cd TakwaraTec-Acervo-Web && npm install && npm run build
ls dist/midia/                                 # as artes precisam estar aqui
cd ../acervo-soberania-tecnologica/workers/instagram-automation-takwaratec
npm ci && npm test                             # espera 24/24
npx wrangler deploy --dry-run
```

**Atenção:** `dist/` é reconstruído a cada build. **Sem as artes no disco, o deploy REMOVE do ar as
artes de lotes anteriores.** Por isso o passo 7 vem antes de qualquer deploy em máquina nova.

### Passo 9 — VERIFICAÇÃO LOCAL

```
cd acervo-soberania-tecnologica/ops/midia-publicacao
python3 montar_lote.py --selftest        # 59 negativos + 8 positivos
python3 verificar_midia.py --selftest     # 9 + 2
python3 montar_lote.py --lote piloto/LOTE_PILOTO_BAMBU_E1.json --raiz ../..
python3 piloto/gerar_piloto_html.py --raiz ../..
```

A esteira roda com **biblioteca padrão apenas** — deliberado: a VM não instala nada para o gate
funcionar, e o gate não quebra por dependência ausente.

**Saída:** selftests PASS, piloto montado, HTML gerado.

## 3. A chave `age` — o elo que não está no Git

Os lotes são `.tar.zst.age`: só abrem com a chave privada X25519.

- **chave só no Mac** → situação atual, a mais frágil. Criar cópia física (papel em cofre) ou em
  gerenciador de senhas, e **registrar aqui onde ela está** — não o valor.
- **chave em cofre/gerenciador** → registrar o nome do item, nunca a senha do cofre.
- **chave perdida** → os `.age` são irrecuperáveis; o original precisa vir de outra fonte.

```
CHAVE_AGE: PENDENTE — localização da cópia de segurança não declarada
```

**Pendência com dono:** `FABIO_SOBERANO`.

## 4. O que NÃO é reconstruível

- **Histórico de publicação no Instagram.** Perdida a conta, nenhum clone a recupera.
- **Tokens antigos.** Valem até expirar; a restauração pressupõe reemissão.
- **Estado local não commitado.** Worktree sujo, stub, `dist/`: morre com a máquina. É a razão da regra "Git é a fonte da verdade".
- **Conversas.** Decisão que existe só em chat não está preservada; para valer, precisa virar arquivo no repositório.

## 5. Ensaio de restauração (pendente)

Este mapa é **plano, não prova**. Para valer como prova, o ensaio precisa de:

1. VM limpa, sem resíduo do Mac;
2. apenas os quatro insumos: acesso, Drive, chave, este mapa;
3. cronômetro e log por passo;
4. falha registrada, não escondida;
5. ao final, selftests PASS e o piloto gerando HTML.

Até lá, a afirmação honesta é: **o plano está escrito, os comandos existem, o ensaio não foi feito.**

| # | item | estado | dono |
|---|---|---|---|
| 1 | chave `age` copiada fora do Mac | PENDENTE | Fábio |
| 2 | remotos `drive` / `gdrive-pessoal-*` com token válido | VENCIDO (expiry 2026-11-19) | Fábio |
| 3 | ensaio real de restauração em máquina limpa | NÃO FEITO | ambos |
| 4 | artes de mídia existentes no Drive | NÃO EXISTE AINDA (nenhum lote publicado) | — |
