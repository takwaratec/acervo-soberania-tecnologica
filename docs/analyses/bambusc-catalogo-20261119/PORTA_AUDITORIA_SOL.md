# PORTA DE AUDITORIA — SOL (auditoria externa, leitura do GitHub)

```
FRENTE=BAMBU-BAMBUSC
TASK=BAMBU-BAMBUSC-CATALOGO-20261119-R1
PR=https://github.com/takwaratec/acervo-soberania-tecnologica/pull/99
OBJETO_AUDITADO=takwaratec/acervo-soberania-tecnologica @ bambusc/catalogo-20261119-r1
ALVO_COMMIT=81b1d480605a90e705b5b8172f29c09e3701f91f
  arquivos nesse commit (este diretorio): 15
  conferir: git ls-tree -r --name-only 81b1d480605a90e705b5b8172f29c09e3701f91f \
              docs/analyses/bambusc-catalogo-20261119 | wc -l   -> 15
NOTA_DE_AUTO_REFERENCIA=esta porta NAO pode citar o proprio sha (impossivel por construcao);
  ela foi corrigida no commit imediatamente posterior ao ALVO_COMMIT, e mede o ALVO_COMMIT.
PONTEIRO_DO_LEDGER=takwaratec/TakwaraTec-Laboratorio-Editorial ref r4-claims
  sha_no_despacho=declarado no registro (queue/BAMBU-BAMBUSC-CATALOGO-20261119-R1.json)
EXECUTOR=HERMES_OPENCODE
AUDITOR_INTERNO=CODEX_LUNA_MEDIUM
AUDITOR_EXTERNO=SOL (le so o GitHub)
```

## 1. O que se audita

O diretório `docs/analyses/bambusc-catalogo-20261119/` no commit `81b1d48…`: **15
arquivos**, 13 deles no inventário do manifesto. É o pacote verificável da rodada 1 de
catalogação documental sobre publicações de bambu.

Nada em `docs/analyses/bambu-estrutural/` foi tocado. Nenhuma ficha foi homologada.

## 2. Quatro âncoras — e a ordem de parar

1. **Branch + commit fixados** acima, em 40 hex. Se o HEAD medido não contiver
   `81b1d480605a90e705b5b8172f29c09e3701f91f`, **pare e reporte** — não audite a ponta.
2. **sha do ref do ledger**: declarado no próprio registro da tarefa
   (`queue/BAMBU-BAMBUSC-CATALOGO-20261119-R1.json`, campo `evidence.commit_no_supersede`). O
   ledger é multi-escritor: outra frente pode publicar no mesmo ref depois do despacho.
3. **Movimento de outra frente no mesmo ref não é delta desta entrega.** Já existe um:
   `R4-BAMBU-SCIENCE-DECUPE-20261117-R1` com claim de HERMES_OPENCODE e lease expirada —
   achado alheio, desta frente não é dona e **não o corrigiu**.
4. Devolva `objeto_medido.head_conferido` no parecer. Sem isso não se sabe se o veredito
   vale para estes bytes.

## 3. Onde está o resto da prova (outro repositório)

O acervo é um repositório; o ledger é outro. O pacote de auditoria (brief do auditor
interno, manifesto de 11 fichas, `SHA256SUMS.txt` com 66 artefatos) está em:

```
takwaratec/TakwaraTec-Laboratorio-Editorial
  branch: hermes/bambu-bambusc-auditoria-20261119
  caminho: ops/command-center/task-results/BAMBU-BAMBUSC-CATALOGO-20261119-R1/
```

E o registro da tarefa (contrato, claim, retorno, evidência com sha e commit):

```
takwaratec/TakwaraTec-Laboratorio-Editorial
  ref: r4-claims
  caminho: queue/BAMBU-BAMBUSC-CATALOGO-20261119-R1.json
```

## 4. O que NÃO se pode conferir do GitHub, e isso é declarado

**Os 11 PDFs e o texto integral estão em custódia privada.** `_privado/` é ignorado pelo
git (`.gitignore` linha 28) e 10 das 11 fontes não declaram licença. Consequência direta
para a auditoria:

- os hashes do `SHA256SUMS.txt` **não são conferíveis** sem os binários;
- o que **é** conferível no GitHub: identidade das obras (DOI/ISBN resolvíveis), coerência
  entre README, manifesto e registro da tarefa, e se cada número declarado tem página e
  fonte nomeada.

Trate os hashes como **declaração da fonte com custódia privada** — não como conformidade
medida. Binário é entregue por solicitação do soberano.

## 5. O que eu quero que seja atacado

1. **A regra de elegibilidade foi aplicada, ou descrita?** 11 fichas para 67 obras listadas:
   as 56 excluídas têm motivo verificável (sem DOI/ISBN do próprio documento)?
2. **O README trava as leituras erradas, ou só as evita?** Os quatro blocos "o que a fonte
   não autoriza concluir" — estão ancorados no texto das obras ou são retórica defensiva?
3. **O defeito de extração de duas colunas** está descrito de modo que outro agente possa
   reproduzir a correção? A camada nova (reordenação por coluna) é atribuída com honestidade
   como algo que o MTCC **não tinha**?
4. **Algum número do README é afirmação sem medição?** 67, 41, 20, 21, 52, 10, 11.
5. **O README afirma conformidade que não existe?** Procure promessa de homologação,
   de build verde ou de auditoria concluída.

## 6. Desvios declarados (não são achados novos)

1. **Critério 3 do contrato dizia 3 elegíveis; entreguei 11.** Registrado em
   `ADENDO_01_BAMBU-BAMBUSC_20261119.md` por decisão do soberano em 2026-11-19 ("o registro
   delta num adendo, não é necessário abrir outra frente").
2. **Critérios 5 e 6 (matriz por eixo, estado da arte) não foram entregues** — o soberano
   decidiu que não são necessários: a juntada das fichas produzirá artigo e estado da arte.
3. **Binários e fichas fora do GitHub** — por `_privado` ignorado e por direitos não
   declarados, não por omissão.

## 7. Veredito

PASS ou FAIL por item da seção 5, com a causa concreta (afirmação, arquivo, linha, o que a
evidência mostra). Veredito do PR e `objeto_medido.head_conferido`. Se algo não for
conferível, diga `NAO_VERIFICAVEL` com o motivo — não converta ausência de prova em PASS.
