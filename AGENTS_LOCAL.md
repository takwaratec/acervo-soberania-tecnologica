# AGENTS_LOCAL.md — Acervo Soberania Tecnológica

## Identidade

Repositório de curadoria documental idealizado por Fabio Takwara. Reúne fichas científicas, resenhas, estados da arte e textos autorais sobre materiais renováveis, construção, habitação, território e bioeconomia.

## Objetivo

Infraestrutura pública de curadoria e conexão do conhecimento: transformar literatura científica, documentação técnica e memória de pesquisa em referências rastreáveis, comparáveis e utilizáveis na formulação de novos estudos, projetos, experimentos e políticas.

## Roteamento de modelos e execução

Antes de executar qualquer GOAL, agentes devem obedecer `GOVERNANCA_ROTEAMENTO_MODELOS_TAKWARATEC_R1.md`.

## Estrutura do repositório

```text
docs/
├── index.md
├── sobre.md
├── metodologia.md
├── assets/stylesheets/
└── analyses/
    ├── fundamentos/
    ├── bambu-estrutural/
    ├── pu-vegetal/
    ├── tecnologia-takwara/
    ├── percecao-social/
    ├── avaliacao-pos-ocupacao/
    ├── politica-habitacional/
    ├── bioeconomia-amazonica/
    ├── grandes-obras-amazonia/
    ├── reforma-agraria-agrofloresta/
    ├── respaldo-academico/
    └── visao-do-autor/
scripts/                    # inventário e validação
INVENTARIO_ACERVO.md        # contagem reproduzível
GOVERNANCA_DOCUMENTAL.md    # estados e taxonomia
```

## Artefatos permanentes por eixo

Cada eixo consolidado deve produzir cinco artefatos permanentes (regra de governança aprovada por Fabio em 2026-08-01):

1. **Fichas documentais** — a base, com fonte integral conferida;
2. **Estado da Arte** — subtítulo "Síntese Curatorial Baseada em Evidências"; tipo documental permanece `estado-da-arte` (sem novo tipo na taxonomia);
3. **Mapa de Evidências** — tema × nível de confiança × nº de estudos;
4. **Agenda de Pesquisa** — lacunas → perguntas → métodos → prioridades;
5. **Mapa de Conhecimento** — conexões com outros eixos, quando houver 3-4 eixos consolidados.

Regras derivadas:
- O Estado da Arte inclui: Resumo Executivo (✓/⚠/✗), tabela-resumo de evidências, níveis de confiança (escala curatorial inspirada no GRADE, sem adoção formal), linha do tempo e convergências + controvérsias.
- Controvérsias internas da gaveta devem ser **resolvidas** (verificar PDF original + Crossref; distinguir falha da curadoria de divergência real de fonte) antes de serem registradas como controvérsia.
- A rede de citações ("relaciona_se_com") pertence à camada de dados das fichas, não ao Estado da Arte; será explorada no Acervo Web.

## Regras locais obrigatórias

- Nunca fabricar citações, autoria, DOI, ISBN, ISSN ou resultados.
- Ficha científica ou acadêmica só ingressa com fonte integral e identidade documental verificável. DOI, ISBN e ISSN devem ser registrados quando existirem, mas sua ausência não impede o ingresso de tese, dissertação, trabalho de evento, relatório ou outro documento cuja autoria, título, instituição, data e proveniência possam ser confirmados no original.
- Laudos, certificados de ensaio e fichas de produto podem ingressar sem DOI/ISBN como tipos técnicos próprios, desde que tenham emissor, produto/amostra e identificador técnico verificável; nunca entram na contagem de fichas científicas.
- Toda ficha científica publicada deve possuir as oito seções do método Cavichiolli adotado pelo Acervo.
- Não completar lacunas por inferência. A ausência de identificador persistente deve ser declarada, nunca preenchida por aproximação. Alertar Fabio quando faltar fonte, autoria ou metadado essencial.
- Documento interno não serve como evidência pública.
- Não inflar TRL nem apresentar proposta laboratorial como tecnologia aplicada.
- Visão autoral deve ser declarada e separada dos achados das fontes.
- Textos integrais protegidos, dados pessoais, contratos, normas e materiais brutos ficam fora de `docs/`.
- Não misturar documentos de projetos irmãos. O Acervo pode conter a referência científica, mas não atas, perfis de equipes, propostas ou operação de outras frentes.

## Conferência de afirmação — quem liga o instrumento, e quando

Esta seção existe porque um texto declarou no método uma conferência que não houve. A regra não é
sobre redigir melhor: é sobre separar **afirmação de conferência**, e sobre a conferência ser
medida, registrada e auditável.

**A1. Quem abre a frente liga o instrumento.** O executor da frente roda a conferência e é quem
responde pelo número. O regente não roda, não mede por conta própria nem entrega resultado pronto no
lugar do executor: ele lê o que foi registrado e aponta inconsistência. Instrumento ligado pelo
regente não ensina a frente e cria segunda direção — a regra é uma só.

**A2. Texto que afirma garantia de conferência é afirmação sobre o próprio trabalho, e entra na
conferência.** A frase de método — "toda afirmação numérica foi conferida contra a fonte primária",
"todas as fontes foram lidas integralmente", ou equivalente — não é enfeite: é declaração de
medição. Só pode constar se houver registro que a sustente. Na ausência do registro, a frase sai ou
passa a relatar o que de fato ocorreu ("N de M conferidas; as demais marcadas como não conferidas").
Documento que declara verificação não realizada não é publicável, ainda que todo o resto esteja
correto.

**A3. O denominador é fixado antes da medição, por escrito.** O que conta como "uma afirmação" é
regra declarada **antes** de rodar o gate. Contagem escolhida depois do resultado não mede nada, e
percentual sem denominador e sem regra não é dado. Duas contagens divergentes do mesmo texto são
indício de regra implícita, não de erro de um dos lados.

**A4. Nenhuma afirmação fica sem veredito.** Cada afirmação numérica e cada parágrafo de prosa recebe
um veredito registrado. `NAO_MEDIDO` é veredito válido e conta no denominador — o proibido é o
silêncio: ausência de veredito somada a uma frase de método que afirma conferência integral. Fonte
inacessível, sem extração ou sob paywall: `NAO_MEDIDO` com o motivo declarado, nunca herança do
veredito de rodada anterior.

**A5. Corrigir é restaurar fidelidade à fonte; o gate mede e não decide.** Proibido ajustar texto
para o gate passar. Quando o gate aponta divergência, corrige-se a afirmação contra a fonte; quando a
fonte não sustenta a afirmação, a afirmação sai.

**A6. Leitura parcial não é conferência.** Resumo, busca por trecho e leitura dirigida são triagem e
devem ser declarados como tal. Chamar de "conferido" o que foi triado é a mesma falha que a A2
proíbe, aplicada ao método.

**A7. O escopo do diff é medido antes de abrir, e `git add -A` é proibido em branch de frente.**
Numa branch de frente, `git add -A` e `git add .` estão proibidos: adiciona-se **caminho declarado**.
Foi assim que uma branch atrás da `main` acumulou 300 arquivos num diff que devia ter 184 — e o PR
teria apagado o teste de um gate e uma página publicada, além de reverter fichas de seis gavetas
para versões antigas.

Antes de abrir a PR, a frente mede e reporta, com número:

- `git diff --name-only origin/main | wc -l` — o total;
- a classificação por gaveta, separando o que é da frente do que não é;
- **as deleções listadas uma a uma** (`git diff --name-status origin/main | grep '^D'`). Deleção é o
  sinal mais caro do diff: quase sempre significa branch desatualizada, não remoção pretendida;
- **as modificações fora da gaveta da frente**, que são regressão de conteúdo de outra frente.

A escopo é aprovado quando o diff fora da gaveta da frente está **vazio**. Não "pequeno": vazio.
Branch desatualizada se corrige trazendo a frente para uma branch cortada da `main` com caminhos
declarados — nunca por `git add -A`, nunca por rebase de branch publicada.

**A gaveta não é digitada: é lida do registro (A9).** A lista de caminhos permitidos de uma PR vem do
`write_scope` da frente no registro vivo (`frentes_abertas/<FRENTE>.json` no ref `r4-claims`), e não de
um `--permitir` escrito à mão no workflow. Lista própria é segunda direção: em 25/11/2026 o gate rodava
com `--permitir docs/ scripts/` enquanto a gaveta do bambu era `docs/analyses/bambu-estrutural`, e foi
assim que uma PR do bambu levou 25 arquivos do cobre e 6 scripts do cobre sem nenhum gate piscar. PR
que não declara `FRENTE=<nome>` não é medida: sai `NAO_MEDIDO`, nunca `PASS`.

**A8. O achado se classifica pelo efeito, e só dois efeitos impedem homologação.** Gravidade mede o
tamanho do erro; efeito mede o que ele obriga a fazer. Classificar por gravidade faz divergência de
índice ter o mesmo peso de afirmação científica contrariada pela fonte, e transforma governança em
trabalho independente — que é o oposto do que ela serve.

Três classes, e nada fora delas:

- **BLOQUEIA_HOMOLOGACAO** — a fonte não sustenta a afirmação, ou a conclusão é mais ampla que o
  corpus examinado. Corrige-se o texto e reconfere-se **o trecho afetado e as afirmações que dele
  dependem**. Não se refaz a auditoria do pacote.
- **SANEAMENTO_DE_CUSTODIA** — obra de terceiro exposta além da fronteira de custódia (o que inclui
  extrato extenso, tabela e figura, não só o PDF), ou pendência de direito. Saneia-se e declara-se o
  novo estado. Não é rodada de auditoria de conteúdo.
- **MANUTENCAO** — registro histórico divergente, contagem, identificador, índice, caminho, forma.
  Corrige-se como manutenção documental, **sem nova rodada** e sem consumir auditor externo.
- **DEFEITO_DE_INSTRUMENTO** — o veredito veio de instrumento defeituoso, e veredito de instrumento
  defeituoso **não é evidência**: a medição se refaz, o objeto não se corrige. Caso real: o selador
  gravava o objeto sem o `\n` final e comparava contra o byte publicado — dois pacotes saíram `FAIL` por
  um byte que não existia no conteúdo; e um verificador estourava com `'list' object has no attribute
  'get'`, reprovando commit por defeito da prova, não do commit. Contornar o instrumento (`--no-verify`,
  `--permitir` mais largo) **não** é a correção: corrige-se o instrumento, e a medição é refeita com ele.

Duas consequências que valem como regra:

1. **Veredito de pacote não é veredito de achado.** Um pacote pode ter `NÃO APROVAR AINDA` por um
   achado bloqueante e, ao mesmo tempo, ter os demais achados resolvidos por manutenção. Escrever
   `FAIL` para todos apaga essa diferença e esconde o que importa.
2. **A correção se confere no ponto, não no conjunto.** Depois de corrigir, confere-se a alteração e
   as afirmações afetadas. Exigir pacote novo inteiro é burocracia: o auditor já leu o resto.

As três garantias que o acervo precisa e às quais todo o resto serve: **a fonte sustenta a
afirmação**; **direitos e custódia são respeitados**; **a homologação é decisão humana informada**.
Instrumento que não serve a uma dessas três é cerimônia.

## A9 — Escopo de frente, registro vivo e trabalho que não se perde

Esta seção existe porque a contaminação entre frentes se repetiu: PR do bambu com 25 arquivos do cobre,
branch do cobre com 176 deleções contra a `main`, worktree de uma frente usado como raiz de outra. Nenhum
desses casos foi má-fé de agente; todos foram **escopo declarado largo** e **endereço emprestado**. A regra
fecha os dois.

**A9.1 — Escopo é gaveta de frente, nunca a família.** `write_scope` declara o caminho da gaveta
(`docs/analyses/bambu-estrutural/**`), não o pai (`docs/analyses`). `docs/analyses` sem subpasta é a
coleção inteira: um escopo assim autoriza escrever na gaveta de todas as outras frentes. O mesmo vale
para `ops/command-center/**`, que contém as gavetas de BAMBU-SCIENCE, MTCC, BAMBU-MOLDE e GAVETA.

**A9.2 — O escopo de uma frente não pode conter o de outra.** O registro recusa abrir, e recusa manter
aberta, frente cujo escopo contenha o de uma frente já aberta. Sobreposição não é alerta: é recusa. Se
duas frentes precisam do mesmo caminho, o caminho é da frente que o abriu e a outra pede emenda — não
herda.

**A9.3 — Cada frente tem o seu worktree, e o registro aponta para ele.** `repo` nomeia a árvore da
própria frente, criada a partir da `main` do acervo. Apontar para a árvore de outra frente, ou para o
checkout principal, é o que produz branch misturada: a frente escreve no diretório onde outra está
trabalhando, e o `git status` de uma passa a mostrar o trabalho da outra.

**A9.4 — Ref de frente não se sobrescreve sem backup publicado.** Antes de qualquer `update-ref`, push
com `--force` ou republicação de ref: `backup/<ref>-<data>` publicado no remoto, e fast-forward
conferido por `git merge-base --is-ancestor <antigo> <novo>`. Ref que não é ancestral do novo não é
avanço: é outra linhagem, e publicar por cima apaga commits que já estavam lá. Caso real: uma abertura
gravou em ref com linhagem dividida e teria apagado dois commits de 25/11 — a executora pegou porque
conferiu antes; a regra existe para quem não conferiria.

**A9.5 — A regra morde, e morder é o resultado esperado.** Quando A9 reprova uma frente já aberta, o
reprova é o achado, não o defeito da regra. O escopo se corrige por emenda na própria frente, com o dono
dela — nunca alargando o gate até passar.

## A10 — O ponteiro de runtime nomeia estado publicado, nunca árvore de trabalho

Em 27/11/2026 o ponteiro de runtime do R4 declarava o hash correto e apontava para o **worktree de uma
frente** (`_worktrees/r4-transicao-…`, parado em branch `hermes/r4-g2-promocao-…`). O caminho servia
`8b0ce094`, 1.109.716 bytes; o publicado em `main` era `7e4c3ebc`, 1.110.310 bytes. A diferença era uma
linha: a promoção dos contratos CALC. As três camadas de autoridade concordavam porque **nenhuma
verificava o caminho** — só o hash, e o hash era de um arquivo que mudava de baixo do ponteiro.

**A10.1 — Cópia de runtime é o formato, e ela é selada.** O ponteiro lê uma cópia fora de repositório,
byte a byte igual ao blob do commit declarado, com `ledger_registry_sha256` (bytes da cópia) e
`ledger_origem_path` (caminho no commit). Cópia fora do repo sem origem declarada é `NAO_MEDIDO`: não há
contra o que comparar.

**A10.2 — Arquivo dentro de árvore git é `FAIL`, mesmo com hash certo.** Ali o conteúdo muda por
`git switch`, e o ponteiro passa a declarar hash de outro arquivo sem que ninguém toque no ponteiro.

**A10.3 — Readback é gate, não cortesia.** `scripts/verifica_ponteiro_runtime.py --repo <governança>`
mede: hash declarado × lido, cópia × blob do commit, `COUNTS.TOTAL` × número de entradas, ids únicos, e
cada contrato no **seu** `contract_commit`. Exit 2 é `NAO_MEDIDO` — não é verde, e não se declara
regularizado com exit 2.

**A10.4 — Contrato sem documento não carrega caminho nem hash.** Entrada com `contrato_documento:
AUSENTE` e `contract_path` preenchido é hash órfão ao contrário: `git show` devolve vazio, `shasum`
devolve `e3b0c442…`, e os dois parecem sucesso.

**A10.5 — Cada contrato é medido no commit em que nasceu.** Contrato R3 nasce em commit de submissão, não
no commit de governança; medir contra a governança acusou 43 contratos "sem arquivo" que existiam.
Entrada sem `contract_commit` é `NAO_MEDIDO` — e registro sem esse campo é dívida, não dispensa.

## Estados documentais

Usar a taxonomia definida em `GOVERNANCA_DOCUMENTAL.md`. Estados canônicos: `recebido`, `identificacao-pendente`, `protegido-privado`, `duplicata-fonte-auxiliar`, `extracao-preliminar`, `em-revisao-documental`, `homologado-documentalmente`, `visao-autoral`, `historico`, `quarentena`, `retirado-da-publicacao`. Nenhum script pode homologar conteúdo automaticamente.

## Publicação e integridade documental

- **Paridade entre idiomas:** toda publicação com versão em inglês (`-en.md`) deve manter paridade 1:1 de seções, anexos, tabelas e referências com a versão em português.
- **Integridade de seções e referências:** todo manual, cartilha ou ensaio técnico deve conter sua seção de referências bibliográficas e DOIs ao final absoluto do documento.
- **Prevalência da língua portuguesa no Zenodo:** o arquivo principal em português (`01_...-pt-br.pdf` ou `.md`) deve ser o primeiro e configurado em `preview_file`.

## Comandos obrigatórios

```bash
# Inventário
python3 scripts/inventariar_acervo.py . \
  --markdown INVENTARIO_ACERVO.md \
  --json INVENTARIO_ACERVO.json

# Validação de front matter
python3 scripts/validate_frontmatter.py

# Build
mkdocs build --strict
```

## Testes

- `mkdocs build --strict` deve terminar com exit 0 antes de qualquer commit.
- Nenhum PDF ou binário pode ser rastreado (`git ls-files | grep -Ei '\.pdf$'` deve ser vazio).
- Nenhum segredo pode aparecer no working tree.

## Dados e privacidade

- Fontes integrais, PDFs e materiais brutos ficam fora do Git, em armazenamento privado e controlado (ver `POLITICA_RETENCAO_CONVERSAO_DESCARTE_PDFS.md` — não versionada).
- Dados pessoais, contratos e documentos sensíveis permanecem privados.
- Documentos de governança interna (planos, políticas, controles de endpoint) não são versionados neste repositório.

## Regras específicas

- O repositório é público; o site é publicado via GitHub Pages por artifact (workflow `gh-pages.yml`).
- A branch `gh-pages` é legado do fluxo antigo e não deve ser usada para publicação.
- Mudanças de README, página inicial, navegação e deploy exigem aprovação de Fabio.
- Commit, push e deploy são autorizações independentes; nada é commitado sem "ok" explícito.

## Exceções autorizadas

- Nenhuma exceção permanente até o momento. Exceções pontuais devem ser registradas.

## Responsáveis

- **Idealização e curadoria:** Fabio Takwara (pesquisador cidadão).
- **Assistência documental:** agentes de IA, sempre sujeitos a revisão humana.
