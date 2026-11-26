---
tipo_documental: instrumento-de-pesquisa
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

**77 arquivos `.md`** contados em 26/11/2026 — dos quais **49 são fichas** (`ficha-cientifica` 29,
`ficha-academica` 20) e **28 não são** (instrumentos, estados da arte, mapas, índices, patentes, normas,
visão autoral). A contagem é reproduzível:

```bash
python3 docs/analyses/bambu-estrutural/scripts/contar_gaveta.py .   # imprime total, por tipo e a lista
```

*A versão anterior deste roteiro publicou uma tabela cujas linhas somavam 77 sob um total declarado de 74,
e que chamava de "74 arquivos" o que era 74 antes dos três documentos desta rodada. O auditor mediu 77 e a
soma errada — está corrigido aqui, com a lista nominal no script em vez de contagem digitada.*

**Partição por objeto — próxima do que a coleção precisa, longe de resolvida.** Classificados pelo que o
**título** e o tipo declaram, não pelo nome da pasta:

| família | nº | o que entra |
|---|---|---|
| **estrutural** — material, propriedades, tratamento, densificação, painéis, norma, ACV, sistemas | **42** | propriedade e material, tratamento térmico, densificado, painéis e compósitos, norma (NBR, NSR-10), ACV, sistemas estruturais e revisões de conexões |
| **síntese e registro da própria gaveta** | **15** | `estado-da-arte` (+`-en`,`-es`), `maturidade-tecnologica` (+`-en`,`-es`), `mapa-de-lacunas`, `mapa-de-evidencias`, `agenda-de-pesquisa`, `index`, os cinco `00-*` |
| **extrato pirolenhoso / licor / bi-óleo** | **5** | `embrapa-2007`, `martins-2017`, `laroque-2022`, `resenha-beraldo`, `silva-2011` |
| **fitossanidade** — inseto, fungo, deterioração, patologia de obra | **4** | `bjb-2023-coleobrocas`, `bjb-2023-antimicrobiano`, `silveira-2015`, `contecc-2025-patologias` |
| **biologia e ecologia** — floração, regeneração, propágulo, fenologia, floresta | **4** | `cerne-2021`, `fadrique-2021`, `miranda-silva-2020`, `van-doninck-2020` |
| **fitorremediação de metais** — fora do escopo de material | **2** | `ficha-chen-2015-cu-moso`, `ficha-liu-2015-pb-moso` |
| **cadeia, mercado e conservação** | **2** | `lima-2019-bambus-nativos-cadeia`, `louredo-2025-bambu-materia-prima-mercado` |
| **instrumento da frente** (fora da partição) | **3** | `ROTEIRO`, `INVENTARIO`, `PLANO` desta rodada |
| **total** | **77** | — |

**A tabela acima é a saída do script, não contagem digitada.** Rodar
`python3 docs/analyses/bambu-estrutural/scripts/contar_gaveta.py .` e conferir: 42 + 15 + 5 + 4 + 4 + 2 + 2 + 3 = 77.
A regra de partição está escrita em `familia()` no próprio script, para que a classificação seja auditável linha a
linha — não um adjetivo que eu afirmo.

**A leitura que importa:** a gaveta declarada como estrutural tem **49 fichas e 28 não-fichas**, e **~16
fichas não são do tema** (4 fitossanidade + 4 pirolenhoso + 3 biologia + 2 fitorremediação + 2 cadeia, mais
sobreposições). Não por erro de ninguém: as pastas nasceram por onde a fonte entrou, não pelo que a fonte
mede.

## 2. A partição — oito gavetas, depois do ato de 26/11

**O que mudou por ato do soberano (26/11/2026), e está registrado em `ATO_SOBERANO_BAMBU_20261126.md`:** a
gaveta de tratamento **se divide em convencional e sustentável**, e o **pirolenhoso vai para a sustentável,
separado do `pu-vegetal`**. A partição abaixo já incorpora isso — e revoga a regra anterior que tratava o
extrato como insumo do PU vegetal.

Nomes de pasta seguem o padrão já vivo na árvore (kebab, objeto antes do qualificador). A renomeação é
**operação auditada** (§5), nunca `mv` solto.

| # | gaveta | objeto | o que ela cataloga | o que fica FORA |
|---|---|---|---|---|
| 1 | `bambu-estrutural` | o colmo e o material como elemento resistente | propriedades mecânicas e físicas, densificação, painéis/CLB/compósitos, normas, ACV de material, desempenho sísmico, sistemas construtivos | tratamento (que tem gaveta própria), biologia, inseto, mercado |
| 2 | `bambu-biologia` | a planta e a floresta | floração, regeneração, propágulo e minijardim, fenologia, distribuição e dinâmica de florestas dominadas por bambu, genética e anatomia do colmo | desempenho mecânico, preservante, obra |
| 3 | `bambu-fitossanidade` | o organismo que ataca e a defesa | coleobrocas, coleópteros, *Dinoderus*, fungos e deterioração, patologias de obra por ataque biológico, controle e manejo pós-colheita | o tratamento em si (é da 4 ou da 5), toxicidade do preservante (idem) |
| 4 | **`bambu-tratamento`** | **a rota convencional** | preservante químico convencional (CCB, CCA, boro), imunização, impregnação sob pressão, secagem como etapa de processo | **vapor saturado com agente de origem biológica** (é da 5), **termorretificação** (é da 5), extrato pirolenhoso (é da 5) |
| 5 | **`bambu-tratamento-sustentavel`** | **a rota sem aditivo de síntese** | **vapor saturado com pirolenhoso, com tanino ou com sal**; **só vapor**; **termorretificação** (só calor, sem aditivo); extrato pirolenhoso, licor, bi-óleo; ação antifúngica e inseticida do extrato; toxicidade e resíduo | resina e adesivo de PU (é da 6) — link, não cópia; preservante convencional (é da 4) |
| 6 | `pu-vegetal` | poliuretano de origem vegetal | **gaveta existente**, 41 arquivos — resina, adesivo, poliol e carga de origem vegetal | o extrato como tratamento do bambu, que é da 5 |
| 7 | `bambu-carbono` | carbono do bambu: sequestro, estoque, biochar e cinzas | estoque e balanço de carbono, biochar, cinzas como pozolana, ciclo de vida do carbono | ACV de material (é da 1) e polpa (é da 8). **Fronteira ainda a decidir pelo soberano** |
| 8 | `bambu-alimentacao-e-outros-usos` | o que sobra | broto e alimentação, polpa e celulose, forno e fogão a biomassa, microreator, cadeia e mercado | material estrutural, biologia, fitossanidade, tratamento |

**Fronteira 2 x 3 — a que mais vai ser disputada.** Se o objeto da ficha é **a planta** (floração,
regeneração, floresta, genética), vai para a 2. Se é **o dano** (quem ataca, quanto come, como se defende),
vai para a 3. `silveira-2015` mede controle de *Dinoderus* → 3. `bjb-2023-antimicrobiano` mede extrato contra
fungo → 3 pelo objeto do dano **e** a fonte vai para a 5 pelo objeto do extrato: são duas perguntas, e a ficha
mora em uma só; a outra entra por link.

**Fronteira 4 x 5 — o critério é O QUE SATURA, não a temperatura.** Decidido pelo soberano em 26/11/2026:

> "O vapor saturado, dependendo de qual é o elemento de saturação, passa a ser tratamento orgânico. Se é vapor
> saturado com pirolenhoso, com tanino, ou só vapor, ou vapor com sal. A termorretificação também entraria num
> tratamento biológico — ela não tem aditivos, então é só o calor, pode ser uma das vias do biológico."

| rota | gaveta | por quê |
|---|---|---|
| vapor saturado **com pirolenhoso, com tanino ou com sal** | **5 — sustentável** | o agente de saturação é de origem biológica ou mineral natural, não de síntese |
| **só vapor** | **5 — sustentável** | não há aditivo; a rota é física |
| **termorretificação** (só calor, sem aditivo) | **5 — sustentável** | é uma das vias da rota biológica, por ausência de aditivo |
| preservante químico convencional (CCB, CCA, boro), impregnação sob pressão | **4 — convencional** | aditivo de síntese |
| **PDMS** (polidimetilsiloxano) | **caso à parte — decidido pelo soberano** | é aditivo **sintético**, mas de função polimérica e não biocida; não é conservante clássico nem rota sem aditivo. Fica nomeado, não classificado por analogia |

**O critério, em uma frase:** entra na 5 o tratamento cujo **agente é ausente, biológico ou mineral natural**;
entra na 4 o que usa **aditivo de síntese com função biocida**; e o que usa **aditivo de síntese sem função
biocida** é caso à parte — hoje, o PDMS.

**O que o ato revoga nesta seção:** a regra anterior — "o pirolenhoso vai para onde está a fonte que ela extrai,
podendo ir ao PU". O critério "onde está a fonte" continua valendo para dirimir dúvida de partição em geral;
**não vale mais para o pirolenhoso**, que tem gaveta por decisão, não por classificação.

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
6. **Uma gaveta por PR.** Partir os 74 arquivos de conteúdo (77 menos os 3 instrumentos desta rodada) em cinco gavetas num PR só torna a revisão impossível e esconde o
   arquivo que foi para o lugar errado.
7. **Preservar bytes.** `_privado/` não se move nesta operação; a gaveta é o markdown versionado.

**Regra que governa o passo 4:** renomear gaveta sem mapa torna irreconhecível a ficha que já foi lida, e o
manifesto antigo passa a apontar para caminho que não existe. O mapa é o que permite ao auditor conferir.

---

## 6. Ordem dos próximos passos

| # | passo | dono | entrega | condição |
|---|---|---|---|---|
| 1 | fechar a gaveta estrutural: transformar L1–L25 em rodadas na `agenda-de-pesquisa.md`, com pergunta, medida e critério de fracasso | executor | agenda reescrita, auditada pelo Teco | **livre** |
| 2 | Onda 0 do plano — cinco obras de prova, taxa de defeito e custo por obra | executor | medida | **livre** — é medição, não conclusão |
| 3 | criar `bambu-biologia`, `bambu-fitossanidade`, `bambu-carbono` com `index.md` e `agenda-de-pesquisa.md` próprios, **vazias e declaradas** | executor | três gavetas com escopo escrito | depende da decisão sobre a fronteira de carbono |
| 4 | mover as fichas de biologia e fitossanidade, com `RENOMEACAO_<data>.json` (um PR por gaveta) | executor | arquivos movidos + mapa + links | depois do passo 3 |
| 5 | separar em `pu-vegetal` o bambu-carga do bambu-poliol | executor | duas seções ou duas gavetas | **decisão do soberano** |
| 6 | ~~decidir o destino do pirolenhoso~~ | soberano | **DECIDIDO em 26/11**: gaveta `bambu-tratamento-sustentavel`, separada do `pu-vegetal` | — |

**O que "livre" significa e o que não significa.** Passo livre não pede autorização para *medir* — pede-a para
*decidir*. Rodada de pesquisa que apenas mede e registra avança sem consulta. Rodada cujo resultado **derruba a
tese** para, escreve o achado e espera: a conclusão não é do executor. Esta é a correção do achado P5 do
Teco R1, que viu no passo 2 anterior ("rodar R1 e R2 sem pedir autorização entre elas") um compromisso de
execução mais amplo do que o soberano autorizou.

## 7. O que este roteiro NÃO autoriza

- Publicar qualquer gaveta como fechada sem o `index.md` dizer o que ela **não** sabe.
- Chamar de homologação o fecho da gaveta.
- Mover ficha entre gavetas sem o mapa de renomeação e sem consertar os links.
- Abrir rodada nova antes de a agenda da gaveta estar auditada — a frente já pagou o preço de trabalhar sem
  plano escrito, e é o que este documento existe para impedir.
