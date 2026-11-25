# Gerador do pacote de auditoria externa

Um pacote que vai a auditor externo não é uma pasta com os artigos. É um **par selado** — manifesto com o alvo fixado, e resposta de hashes ao lado — mais as instruções que o auditor executa sem depender de quem escreveu.

O gerador nasceu do molde do COBRE, depois que a auditoria **R19** derrubou aquele molde com quatro defeitos. Cada um virou uma checagem que **recusa gerar**, não um aviso.

## As seis recusas

| Código | Defeito que originou | O que o gerador faz |
|---|---|---|
| **R19-A** | O manifesto dizia que os 33 sha256 foram lidos com `git show`, quando 6 são PDFs fora do rastreio — método declarado **impossível** para 6 dos 33. | Declara o método por fonte e o **executa**. Fonte fora do rastreio sem `caminho_privado` que exista em disco: recusa. Hash que não confere com o declarado: recusa. |
| **R19-B** | O manifesto mandava entrar por `ops/command-center/auditoria-atual/COBRE.json`, arquivo que **não existia**. | Toda fonte e toda `referencias_resolviveis` é resolvida contra o commit alvo, ou contra o histórico. Não resolve: recusa. |
| **R19-C** | O selo não era par: o manifesto antigo saía, a resposta de hashes ficava. | Emite os dois no mesmo ato. Mas commit é ato humano — o gerador diz qual par commitar junto. |
| **R19-D** | O `como_reproduzir` mandava abrir `fontes/pdf/`, diretório **esvaziado** pela própria frente. | Extrai todo caminho das instruções e confere no commit alvo. Diretório só existe se tiver arquivo dentro. Não existe: recusa. |
| **A2** | Texto que declara conferência que não houve. | `nao_medido_declarado` é campo obrigatório: sem ele o pacote não sai. O limite vai escrito, não escondido. |
| **BASE** | Escopo e selo válidos só para um commit. | O alvo entra no nome do arquivo e na saída. Selo de ontem não se confunde com o de hoje. |

## Uso

```bash
python3 scripts/pacote_auditoria/gerar.py \
  --frente cobre --alvo origin/hermes/cobre-pr-20261125-r2 --repo . \
  --cfg configs/pacote_cobre.json --check    # valida, não escreve
```

Sem `--check`, escreve `AUDITORIA_SOL_<FRENTE>_MANIFEST_R1_<alvo>.json` e `..._HASHES_RESPONSE_R1_<alvo>.json` na pasta da frente, e imprime o que commitar junto.

Saída típica:

```
FRENTE=cobre ALVO=d7ab7764 FONTES=33
  por metodo: {'git_show_no_commit': 27, 'registro_custodia_privada': 6}
  selos no historico: 30 manifestos / 30 respostas
  R19-A metodo por fonte: OK · R19-B referencias: OK · R19-D instrucoes: OK
```

## Contagem de selos: por caminho, nunca por mensagem

O índice do cobre dizia **19** selos quando o repositório guardava **28** — o gerador da frente lia `git log` filtrando a **mensagem de commit**, e selos anteriores à convenção de mensagem ficaram invisíveis. `contar_selos()` varre `git log --all --name-only`, que vê o caminho, e revela órfãos (só manifesto, ou só resposta).

## Configuração por frente

`configs/pacote_<frente>.json`. Campos obrigatórios: `frente`, `pasta`, `manifest_id`, `autoridade`, `alvo_branch`, `aviso_de_leitura`, `o_que_esta_auditoria_e`, `pedido_do_soberano`, `objeto`, `estado_declarado`, `pergunta`, `parte_1_perguntas`, `criterios`, `severidade`, `formato_resposta`, `limites`, `nao_homologa`, `como_reproduzir`, `nao_medido_declarado`, `como_ler` e `fontes`.

Em `fontes`, cada item: `path`, `papel`, `no_repositorio` e — quando `false` — `caminho_privado` (e `sha256` se o registro de custódia já o tiver, para conferência).

## Fronteira

O gerador **mede e recusa**; não decide o que o auditor vai achar, não homologa e não autoriza merge. A pergunta que ele não responde — se a fonte sustenta a conclusão — é exatamente a pergunta do auditor externo, e nenhum instrumento desta casa a mede.
