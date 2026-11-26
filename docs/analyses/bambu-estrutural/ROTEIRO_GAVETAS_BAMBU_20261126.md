---
tipo_documental: roteiro-de-frente
estado_documental: em-revisao-documental
data_revisao: 2026-11-26
responsavel_curadoria: Fabio Takwara
titulo: "Roteiro de gavetas temáticas da coleção Bambu — e o fecho da gaveta estrutural"
autor: Fabio Takwara
resumo: "Inventário medido do que hoje mora em uma única gaveta de bambu, proposta de partição em gavetas temáticas, e o plano de fecho da gaveta estrutural a partir das lacunas já declaradas."
substitui_versao: "não substitui plano vigente; a gaveta bambu-estrutural mantém o plano próprio em agenda-de-pesquisa.md"
---

# ROTEIRO — gavetas temáticas da coleção Bambu

**Ordem de quem manda:** o soberano, em 26/11/2026, no fecho da rodada de teste do motor.
**Base medida:** acervo `main` = `d0bc531` (merge do #136). Todo número deste documento saiu de `ls` e
`grep '^titulo:'` nesse commit — não de memória.

---

## 0. O que esta rodada encerrou, e o que ela muda no vocabulário

As **seis fichas** de `bambu-estrutural` mais a PDMS foram o **teste do motor**, não uma amostra de
homologação. O que ficou provado e o que não ficou:

- **provado:** o gate mede onde o número está, na página declarada, com unidade compatível — e a correção do A1
  tornou o placar comparável entre fichas com e sem tabela;
- **não provado:** que a ficha é homologável. O gate não lê a fonte; quem lê é o humano, e a leitura humana não
  aconteceu;
- **estado:** as **seis seguem `em-revisao-documental`**. A PDMS é `homologado-documentalmente` por ato de
  21/11/2026 e é a exceção — a única ficha de todo o conjunto com `autorizacao_homologacao`.

**Correção de vocabulário que o roteiro adota daqui em diante:** o conjunto de teste são **seis fichas**; a
PDMS é a sétima da gaveta apenas por vizinhança de pasta. Documento que somar «as sete» em matéria de estado
documental está errado, e foi por isso que quatro rodadas de auditoria reprovaram.

---

## 1. Inventário medido — o que a gaveta `bambu-estrutural` contém hoje

**74 arquivos `.md`**, mais este roteiro (75 no momento da escrita). Classificados pelo objeto que o **título**
declara (`grep '^titulo:'`), não pelo nome da pasta — que é justamente o que este roteiro corrige.

| família | nº | arquivos |
|---|---|---|
| **estrutural** — material, propriedades, tratamento, densificação, painéis, norma, ACV, sistemas | **48** | `adier-2023`, `bussinger-2024`, `marcal-2018`, `alves-2025`, `reghin-2018`, `ficha-acv-…-araujo2025`, `nsr10-titulo-g-guadua`, `ficha-desempenho-sismico-puma-2014`, `rusch-2019`, `tarverdi-2024`, `sa-2022`, `godoy-junior-2024`, `santos-2020`, `rmat-2024`, `chung-wang-2017`, `ficha-efecto-humedad-gutierrez-2014`, `ficha-heat-treatment-pdms`, `ficha-effects-heat-treatment-scrimber`, `ficha-high-temperature-saturated-steam`, `costa-2015`, `oliveira-2025`, `gauss-2020`, `gauss-2023`, `pimentel-bi-oleo`, `moreira-silva-2022`, `martins-2021`, `ruggiero-2021`, `cordero-1990`, `pereira-2012`, `contecc-2025-especies-nativas`, `santos-2024-poetica`, `maturidade-tecnologica` (+`-en`,`-es`), `china-bamboo-connections-review-2019`, `neotropical-bamboo-review-2024`, `inbar-bru-v6n2-2025`, `revista-bambu-rbb-2022`, `ferreira-kalliola-2020` |
| **síntese e registro da própria gaveta** | **10** | `estado-da-arte.md` (+`-en`, `-es`), `mapa-de-lacunas.md`, `mapa-de-evidencias.md`, `agenda-de-pesquisa.md`, `index.md`, `00-inventario-corpus-autoral`, `00-matriz-rastreabilidade…`, `00a-linha-do-tempo…`, `00-relatorio-auditoria-epistemica`, `00-lista-afirmacoes-para-revisao` |
| **fitossanidade** — inseto, fungo, deterioração, patologia de obra | **5** | `bjb-2023-coleobrocas`, `bjb-2023-antimicrobiano-guadua`, `silveira-2015-controle-dinoderus`, `silva-2011-tratamento-pirolenhoso`, `contecc-2025-patologias-quiosque` |
| **extrato pirolenhoso / licor / bi-óleo** | **4** | `embrapa-2007-extrato-pirolenhoso`, `martins-2017-licor-pirolenhoso`, `laroque-2022-liquido-pirolenhoso-pinus`, `resenha-beraldo-bambu-pirolenhoso` |
| **biologia e ecologia** — floração, regeneração, propágulo, fenologia, floresta | **3** | `cerne-2021-minijardim-clonal`, `miranda-silva-2020-floracao-regeneracao`, `van-doninck-2020-ciclos-floracao-landsat` |
| **fitorremediação de metais** — fora do escopo de material | **2** | `ficha-chen-2015-cu-moso`, `ficha-liu-2015-pb-moso` |
| **cadeia, mercado e conservação** | **2** | `lima-2019-bambus-nativos-cadeia`, `louredo-2025-bambu-materia-prima-mercado` |
| **total** | **74** | — |

*Cada arquivo entra em **uma** família, para o total fechar em 74. As versões `-en`/`-es` de `estado-da-arte` e
`maturidade-tecnologica` contam como arquivo próprio (são arquivos distintos no disco). As fichas de fronteira
(`pimentel-bi-oleo`, `silva-2011`, `silveira-2015`, `carvalho-2013`, `fadrique-2021`) foram atribuídas à família
do **objeto medido**, e a fronteira está discutida na §2 — é decisão de partição, não de contagem.*

**Leitura honesta do número:** dos 74 arquivos, **16 não pertencem à gaveta estrutural** — 5 de fitossanidade,
4 de pirolenhoso, 3 de biologia, 2 de fitorremediação, 2 de cadeia —, e mais `ficha-rocket-stove-cfd` (fogão),
`pandoli-ghavami-sa-2023` (microreator), `mendonca-2018` (cinzas), `santos-2023` (polpa) e `ficha-efecto-humedad`
(higroscopicidade, que fica), que não têm casa hoje. Não por erro de alguém: as pastas nasceram por onde a fonte
entrou, não pelo que a fonte mede. É a primeira razão para partir a coleção em gavetas temáticas.

**Leitura honesta do número:** a gaveta estrutural já não é só estrutural. Dos 74 arquivos, **~19 não pertencem
a ela** (5 fitossanidade + 5 pirolenhoso + 4 biologia + 2 fitorremediação + 2 cadeia, com sobreposições
declaradas). Não por erro de alguém: as pastas nasceram por onde a fonte entrou, não pelo que a fonte mede. É a
primeira razão para partir a coleção em gavetas temáticas.

## 2. A partição proposta — sete gavetas

Nomes de pasta seguem o padrão já vivo na árvore (kebab, objeto antes do qualificador). A renomeação é
**operação auditada** (§5), nunca `mv` solto.

| # | gaveta | objeto | o que ela cataloga | o que fica FORA |
|---|---|---|---|---|
| 1 | `bambu-estrutural` | o colmo e o material como elemento resistente | propriedades mecânicas e físicas, tratamento preservante, densificação, painéis/CLB/compósitos, normas, ACV de material, desempenho sísmico, sistemas construtivos | biologia, inseto, mercado, cadeia |
| 2 | `bambu-biologia` | a planta e a floresta | floração, regeneração, propágulo e minijardim, fenologia, distribuição e dinâmica de florestas dominadas por bambu, genética e anatomia do colmo | desempenho mecânico, preservante, obra |
| 3 | `bambu-fitossanidade` | o organismo que ataca e a defesa | coleobrocas, coleópteros, *Dinoderus*, fungos e deterioração, patologias de obra por ataque biológico, controle e manejo pós-colheita | tratamento térmico/químico (é da 1), toxicidade do preservante (é da 1) |
| 4 | `bambu-pirolenhoso` | o extrato como objeto químico e produto | produção do licor/extrato, caracterização, ação antifúngica e inseticida, bi-óleo, toxicidade e resíduo do extrato | pirolenhoso como insumo de PU vegetal (é da 5) e a ficha do fogão/forno (é da 7) |
| 5 | `pu-vegetal` | poliuretano de origem vegetal | **gaveta existente**, 41 arquivos — recebe o que for PU e não bambu | avaliação de bambu como carga, que fica na 1 |
| 6 | `bambu-carbono` | carbono do bambu: sequestro, estoque, biochar e cinzas | estoque e balanço de carbono, biochar, cinzas como pozolana, ciclo de vida do carbono | ACV de material (é da 1) e polpa (é da 7) |
| 7 | `bambu-alimentacao-e-outros-usos` | o que sobra | broto e alimentação, polpa e celulose, forno e fogão a biomassa, microreator, cadeia e mercado | material estrutural, biologia, fitossanidade |

**Gaveta 2 x 3 — a fronteira que mais vai ser disputada.** Regra: se o objeto da ficha é **a planta** (floração,
regeneração, floresta, genética), vai para a 2. Se o objeto é **o dano** (quem ataca, quanto come, como se
defende), vai para a 3. `silva-2011` e `silveira-2015` medem controle de *Dinoderus* → 3. `bjb-2023-antimicrobiano`
mede extrato contra fungo → 3, e o extrato como insumo vai para a 4 sem duplicar a ficha.

**Gaveta 4 x 5 — a segunda disputa.** O pirolenhoso é extrato de bambu (4) *e* insumo em formulação de PU (5).
A regra: a ficha vai para onde está **a fonte que ela extrai**; a ligação entre gavetas é link, não cópia.

---

## 3. PU vegetal, carbono e alimentação — o que já existe

| gaveta | hoje | lacuna que o roteiro nomeia |
|---|---|---|
| `pu-vegetal` | 41 arquivos, `agenda-de-pesquisa.md` própria | o bambu entra como **carga** ou como **fonte de poliol**? A gaveta hoje mistura os dois — separar é a primeira rodada |
| `bambu-carbono` | **não existe** | cinzas (`mendonca-2018`) e fogão/forno (`ficha-rocket-stove-cfd`) estão em `bambu-estrutural`; carbono e biochar não têm casa |
| `bambu-alimentacao` | **não existe** | broto não tem ficha na árvore; polpa (`santos-2023`) está na estrutural |

**Não inventar ficha para preencher gaveta.** Gaveta vazia declarada é informação; gaveta preenchida com ficha
fraca é dívida.

---

## 4. A primeira gaveta a fechar é a estrutural — e o plano já está escrito

O soberano disse: *«nós ainda não fechamos a parte estrutural, nós iniciaremos por ela»*. O plano de fecho
**não começa do zero**: `mapa-de-lacunas.md` (29.783 bytes, 25 lacunas, L1–L25) já as declarou e já aponta as
fichas que as evidenciam. O que falta é transformar lacuna em **rodada com pergunta, medida e critério de
fracasso** — e isso é o que a `agenda-de-pesquisa.md` da gaveta tem de passar a conter.

### 4.1 As cinco primeiras rodadas, na ordem de impacto na tese

| ordem | rodada | lacuna | por que primeiro |
|---|---|---|---|
| R1 | **Janela térmica** — existe limite defensável de temperatura × tempo, por espécie? | L2 | é a controvérsia central da gaveta: quatro fontes divergem e uma delas tem um corpo de prova por condição. Qualquer uso normativo da rota depende disto |
| R2 | **Durabilidade de campo** — o tratamento resiste em serviço por anos? | L1, L3, L6 | a decisão de uso estrutural é de campo, e a gaveta só tem bancada (21 dias, 12 meses) |
| R3 | **Densificado em serviço** — durabilidade e higroscopicidade sob umidade real | L7 | é a rota com melhor perspectiva industrial e a de menor dado de envelhecimento |
| R4 | **Conexões** — protocolo de ensaio e preenchimento não friável | L14 | o colmo não é o gargalo: a ligação é. hoje a revisão de conexões não tem protocolo declarado |
| R5 | **Norma brasileira** — o que existe além da NBR 16828 e o que o PNMCB regulamenta | L9 | fecha ou abre o uso normativo, e a lacuna está entre duas normas (lei-quadro × política do material) |

**Recorte que o roteiro impõe a essas cinco:** a gaveta estrutural mede **o colmo e o material**. A rodada que
cair em produto tratado (madeira/bambu com preservante em obra) é ficha de produto, etapa posterior; a que cair
em planta é da gaveta 2; a que cair em inseto é da 3. Sem essa frase no topo do plano, ele escorrega de nível —
e o escorregão já custou rodadas nesta frente.

### 4.2 O que o fecho da estrutural NÃO inclui

- **Não homologa nada.** Fechar a gaveta é declarar o que ela sabe e o que não sabe, com as lacunas nomeadas —
  não é carimbar ficha. A homologação é sessão própria, por leitura humana, e não tem data marcada.
- **Não promove as seis.** Elas seguem `em-revisao-documental`, e o teste do motor não mudou isso.
- **Não decide a tese do capítulo.** Rodada que derruba conclusão é decisão do soberano.

---

## 5. Procedimento da renomeação — operação auditada, não `mv`

1. **Derivar o destino do front matter** (`titulo`, `palavras_chave`), não do nome da pasta de origem, e do
   **objeto medido**, não do título bonito.
2. **Gravar `RENOMEACAO_<data>.json`** com `nome_antigo`, `nome_novo`, `sha256_antes`, `sha256_depois`, e a
   família declarada por ficha.
3. **Conferir colisão antes de mover** — dois autores no mesmo ano e tema não podem cair no mesmo slug.
4. **Reescrever as referências cruzadas no mesmo commit**: `index.md` da gaveta, `index.md` de `docs/analyses`,
   links em `estado-da-arte.md`, `mapa-de-evidencias.md`, `mapa-de-lacunas.md` e nos geradores de HTML.
5. **Rodar o verificador de links e declarar quantos quebraram** — e quantos foram consertados.
6. **Uma gaveta por PR.** Partir 74 arquivos em cinco gavetas num PR só torna a revisão impossível e esconde o
   arquivo que foi para o lugar errado.
7. **Preservar bytes.** `_privado/` não se move nesta operação; a gaveta é o markdown versionado.

**Regra que governa o passo 4:** renomear gaveta sem mapa torna irreconhecível a ficha que já foi lida, e o
manifesto antigo passa a apontar para caminho que não existe. O mapa é o que permite ao auditor conferir.

---

## 6. Ordem dos próximos passos

| # | passo | dono | entrega |
|---|---|---|---|
| 1 | fechar a gaveta estrutural: transformar L1–L25 em rodadas na `agenda-de-pesquisa.md`, com pergunta, medida e critério de fracasso | executor da frente | agenda reescrita, auditada pelo Teco |
| 2 | rodar R1 (janela térmica) e R2 (campo) — em sequência, sem pedir autorização entre elas | executor | resultado + fichas, por `producao-lote-documental` |
| 3 | criar `bambu-biologia`, `bambu-fitossanidade`, `bambu-carbono` com `index.md` e `agenda-de-pesquisa.md` próprios, **vazias e declaradas** | executor | três gavetas com escopo escrito |
| 4 | mover as fichas de biologia e fitossanidade para as gavetas novas, com `RENOMEACAO_<data>.json` (um PR por gaveta) | executor | arquivos movidos + mapa + links consertados |
| 5 | separar em `pu-vegetal` o bambu-carga do bambu-poliol | executor | duas seções ou duas gavetas, decidido com o soberano |
| 6 | decidir com o soberano o destino do pirolenhoso: gaveta própria (4) ou seção da estrutural | **soberano** | decisão escrita no `index.md` |

---

## 7. O que este roteiro NÃO autoriza

- Publicar qualquer gaveta como fechada sem o `index.md` dizer o que ela **não** sabe.
- Chamar de homologação o fecho da gaveta.
- Mover ficha entre gavetas sem o mapa de renomeação e sem consertar os links.
- Abrir rodada nova antes de a agenda da gaveta estar auditada — a frente já pagou o preço de trabalhar sem
  plano escrito, e é o que este documento existe para impedir.
