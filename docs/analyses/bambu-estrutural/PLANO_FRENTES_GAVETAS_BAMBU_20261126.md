---
tipo_documental: instrumento-de-pesquisa
estado_documental: em-revisao-documental
data_revisao: 2026-11-26
responsavel_curadoria: Fabio Takwara
titulo: "Plano de frentes e gavetas da coleção Bambu — ondas, reauditoria e estado da arte com diretrizes"
autor: Fabio Takwara
resumo: "Plano de execução por ondas por gaveta: reauditoria do publicado pela R4, fichamento do corpus custodiado, atualização e estado da arte por gaveta, com síntese para diretrizes de política nas gavetas que não comportam estado da arte próprio."
---

# PLANO — frentes e gavetas da coleção Bambu

**Decisões do soberano que este plano executa** (26/11/2026): ondas por gaveta, com busca de atualização em
cada uma; estado da arte **por gaveta quando o corpus permitir**, e síntese para diretrizes de política
pública a partir daquelas que não comportarem; **a gaveta de carbono é criada**; inventário do custodiado em
disco **antes** do plano; e o plano começa pela **bambu estrutural**.

**Base medida:** `INVENTARIO_CUSTODIA_BAMBU_20261126.md` (mesma árvore, mesmo commit). Nenhum número aqui é
estimativa — os que faltam estão nomeados como lacuna na §7.

---

## 1. O desenho em uma frase

Cada gaveta percorre quatro fases — **inventariar, reauditar, completar, atualizar** — e só então produz o
produto que o seu corpus sustenta: estado da arte próprio, ou insumo para a síntese de política. A onda
seguinte só abre quando a anterior fecha a **fase 2** de todas as gavetas da coleção, não quando a anterior
está inteiramente pronta. Isso mantém a homogeneidade do release 2 sem congelar a frente.

---

## 2. A arquitetura de qualidade (vale para toda gaveta)

**Regra 1 — o motor mede, o humano homologa.** O gate de fidelidade mede número, página e unidade contra a
fonte custodiada; `PASS` nunca é homologação. O estado máximo que a frente entrega em cada Onda é
`em-revisao-documental` com os achados declarados.

**Regra 2 — a ficha tem ponteiro, não adjetivo.** `fonte_primaria: "PDF integral conferido"` não é
verificável. A partir desta frente, toda ficha declara `pacote_fonte_privado` **que resolve** para um grupo
existente, e o grupo tem `original.pdf` + `metadados.json` + `extracao.md` com âncora de página.

**Regra 3 — integridade antes de conteúdo.** Fonte que não abre, que não extrai ou que não casa com o
título não entra em medição. Reextrai-se; não se mede sobre extração suspeita.

**Regra 4 — duas réguas, dois nomes.** `numeros_na_ficha` ≠ `afirmacoes_resultado` ≠ aprovadas. Nunca
"afirmações" sozinho.

**Regra 5 — auditoria interna antes de sair do executor, auditoria externa depois de publicado.**
Teco (auditor interno, modelo de outra família) a cada entrega; Sol só lê o GitHub, e por isso o pacote
tem de ser legível de fora.

**Regra 6 — onda fecha com registro no LIDIA.** Nada de "a frente está trabalhando": o mapa vivo das frentes
declara estado, e frente que não passa o portal não publica afirmação de conclusão.

---

## 3. A prova de método que precede escalar (Onda 0)

Antes de rodar 254 obras pelo motor, a frente prova o pipeline em **pequeno lote medido**. Escolhidos para
testar exatamente o que vai quebrar em escala:

| item | por que este |
|---|---|
| `BAM-001` (cultivo no Sul da Itália) | já aberto: camada de texto, DOI na p. 1, Crossref resolve — é o controle positivo |
| uma obra de **tabela** (carbono por espécie, biomassa por parcela) | o A1 nasceu de tabela: é onde página por célula falha |
| uma obra de **norma ou revisão** | sem número de resultado: testa o `SEM_AFIRMACAO_DE_RESULTADO` (A7) |
| uma obra em **espanhol ou chinês** | testa idioma e extração fora do inglês |

**Entregável da Onda 0:** cinco fichas medidas com o gate vigente, a taxa de defeito por classe, e o
**custo real por obra** (tokens e minutos). Sem esse número não se promete prazo para 254.

**Critério de fracasso declarado antes:** se a taxa de defeito de extração passar de 20% no lote de prova,
o gargalo não é curadoria — é extração, e a Onda 1 começa por consertar o extrator, não por fichar.

---

## 4. Ondas por gaveta

A ordem da onda não é por gosto: é por **dependência** — a gaveta que sustenta a tese vem primeiro; a que
depende de decisão terminológica vem depois.

### Onda 1 — `bambu-estrutural` (a gaveta em que estamos)

**Por que primeiro:** é a única com corpus próprio já fichado, 25 lacunas declaradas e a tese da frente
depende dela. Fechá-la prova o método em terreno conhecido.

**Fase 1 — inventariar.** 74 arquivos, dos quais 49 são `ficha-*`; 51 pertencem ao tema e 16 a outros
temas (fitossanidade 5, pirolenhoso 4, biologia 3, fitorremediação 2, cadeia 2). Registrar a partição no
`RENOMEACAO_<data>.json` **antes** de mover.

**Fase 2 — reauditar (R4 + integridade).** Para cada uma das 49 fichas:
1. o `pacote_fonte_privado` resolve? Se não, localizar o grupo pelo título/DOI e **corrigir o ponteiro**;
2. o PDF abre, termina em `%%EOF`, e o `extracao.md` tem âncora de página? Se não, **reextrair**;
3. o título e o ano do PDF casam com o front matter? Se não, o achado é de identidade, não de formatação;
4. rodar o gate vigente e registrar `numeros_na_ficha` / `afirmacoes_resultado` / aprovadas.

**Resultado esperado da fase 2:** 49 fichas com ponteiro que resolve, extração ancorada e medida.
Hoje, das 38 que declaram ponteiro em todo o acervo, 31 não resolvem — essa é a dívida a pagar.

**Fase 3 — completar.** As lacunas L1–L25 do `mapa-de-lacunas` viram rodadas com pergunta, medida e
critério de fracasso na `agenda-de-pesquisa`. As cinco primeiras, por impacto na tese: janela térmica (L2),
durabilidade de campo (L1/L3/L6), densificado em serviço (L7), conexões (L14), norma brasileira (L9).

**Fase 4 — atualizar.** Busca de novidade publicada desde 2024 sobre os cinco temas, com o protocolo
Crossref/Unpaywall/DOAJ da skill de descoberta. Candidato que entra vira ficha; candidato que não entra fica
listado com o motivo.

**Produto — e o que ele ainda depende de medir.** A gaveta estrutural tem 42 arquivos de objeto estrutural e 49
fichas, o que sugere que ela cumpre o critério do §5. **Sugere não é cumpre:** dos quatro requisitos, um é
contagem (≥20 fichas), e os outros três — **≥10 fontes primárias conferidas**, mais de um objeto medido, e ao
menos uma divergência medida entre autores — ainda não foram medidos nesta rodada. Ficam como **condição de
elegibilidade pendente**, a ser decidida no fim da fase 2:

- se os quatro se cumprirem → `ESTADO_DA_ARTE_BAMBU_ESTRUTURAL`;
- se não → **nota de campo** (o que existe, o que não existe, por que não fecha) e insumo da síntese.

Este parágrafo é a correção do achado P4 do Teco R1: a versão anterior apresentava o produto como sustentado
("passa de 40 fichas") sem ter aplicado o critério que o próprio plano declara prévio.

### Onda 2 — `bambu-carbono` (a gaveta que nasce)

**Por que aqui:** o soberano apontou que a documentação é forte e o acervo não a tem. E porque ela é a gaveta
onde a política pública realmente decide (crédito de carbono, REDD+, MRV) — o custo de não tê-la é maior.

**Já localizado:** as 254 BAM incluem a frente de carbono com força: estoque em floresta natural de
*Oxytenanthera abyssinica* (Uganda), estoque por altitude em *Dendrocalamus hamiltonii* (Nepal), e uma
revisão sobre **barreiras a iniciativas de crédito de carbono com bambu**. E o periódico mantém coleção
especial sobre **materiais de carbono derivados de bambu** e outra sobre **bambu em clima em mudança**.
Há ainda, na gaveta estrutural, `mendonca-2018` (cinzas como pozolana) e `ficha-rocket-stove-cfd` (fogão),
que são carbono aplicado e hoje não têm casa.

**Fase 1:** criar `docs/analyses/bambu-carbono/` com `index.md` e `agenda-de-pesquisa.md` próprios,
**declarando-se vazia** — gaveta declarada e vazia é informação; gaveta preenchida com ficha fraca é dívida.
Registrar no `GAVETAS_R4.json` (hoje a entrada existe em `GAVETAS_DECLARADAS_SEM_CONTEUDO_MEDIDO`).

**Fase 2:** triagem das 254 por tema, começando por carbono: uma linha por obra, título e DOI lidos da p. 1.

**Fase 3:** fichar o subconjunto de carbono e mover para cá `mendonca-2018` e o fogão, com mapa de
renomeação e links consertados.

**Ponto de decisão do soberano:** a gaveta cobre **estoque e sequestro** (biomassa, solo, MRV) ou também
**produto de carbono** (biochar, materiais de carbono, cinzas)? São dois campos com literatura distinta, e
misturá-los reproduz o defeito que esta partição existe para corrigir.

### Onda 3 — `bambu-fitossanidade` e `bambu-biologia`

**Por que juntas:** são as fronteiras que mais se confundem, e separá-las na mesma onda obriga a régua a ser
escrita uma vez só. Regra já proposta: **a planta** (floração, regeneração, propágulo, floresta, genética) vai
para biologia; **o dano** (quem ataca, quanto come, como se defende) vai para fitossanidade.

**Fase 1:** criar as duas com escopo escrito; mover 5 fitossanidade + 3 biologia da estrutural.
**Fase 2:** reauditar as movidas (mesma régua da Onda 1, fase 2).
**Fase 3:** completar a partir das 254 — o periódico tem coleção especial de **recursos de bambu em clima em
mudança**, que trata explicitamente de suscetibilidade a pragas e doenças.

### Onda 4 — `bambu-pirolenhoso` + `pu-vegetal`

**Por que depois:** depende de decisão de fronteira. O pirolenhoso é extrato de bambu e insumo de PU; a regra
proposta é "a ficha mora onde está a fonte que ela extrai, e a ligação entre gavetas é link, não cópia".
`pu-vegetal` tem 41 arquivos e agenda própria — a primeira rodada dela não é fichar, é **separar** bambu-carga
de bambu-poliol, porque hoje as duas coisas convivem sem distinção.

### Onda 5 — `bambu-alimentacao-e-outros-usos`

Broto, polpa, forno, microreator, cadeia e mercado. É a gaveta que justifica o nome "outros usos" — e a que
só se abre depois que as cinco anteriores mostraram o que sobra. Sem essa ordem, ela vira depósito.

---

## 5. Estado da arte e diretrizes de política — o desenho que o soberano pediu

**Regra de produto:** o estado da arte é **por gaveta** quando o corpus comporta: densidade temática
suficiente, fontes primárias, e pelo menos uma divergência medida entre autores — porque estado da arte sem
divergência é bibliografia anotada, não estado da arte.

**Critério de "comporta", declarado antes de escrever:**

| condição | medida mínima |
|---|---|
| corpus | ≥ 20 fichas na gaveta, ≥ 10 com fonte primária conferida |
| dispersão | a gaveta mede mais de um objeto (ex.: propriedade × norma × sistema) |
| divergência | pelo menos 2 autores medindo o mesmo objeto com resultados diferentes |
| lacuna | ao menos 1 lacuna declarada que a gaveta não pode fechar sozinha |

Gaveta que não cumpre isso **não produz estado da arte**: entrega **nota de campo** — o que existe, o que não
existe, e por que não fecha — e entra como insumo da síntese.

**A síntese para política pública** é documento próprio, de outra natureza: não mede o que existe, escolhe
entre alternativas com critério e risco declarados. As duas camadas andam separadas e rotuladas. Ele se
compõe de:

1. **o que a evidência sustenta** — por gaveta, com página e limite;
2. **o que a evidência não sustenta** — a lista das afirmações que circulam e não se sustentam (é a parte
   que evita política pública baseada em "bambu é X vezes mais resistente que o aço");
3. **o que decide** — instrumento, custo, quem paga, quem executa, em que prazo;
4. **o que fiscaliza** — MRV, norma aplicável, órgão competente.

O insumo geoeconômico entra aqui, **como insumo declarado**, não como conclusão. Ele é de outra frente e o
plano não o substitui.

---

## 6. Cronograma por dependência, não por data

| # | entrega | depende de | quem audita |
|---|---|---|---|
| 1 | Onda 0 — 5 fichas de prova e a taxa de defeito | — | Teco |
| 2 | `RENOMEACAO_<data>.json` da partição da estrutural | 1 | Teco |
| 3 | 49 fichas da estrutural com ponteiro e extração medidos | 2 | Teco + gate |
| 4 | gaveta `bambu-carbono` criada e declarada vazia | 3 (método provado) | Teco |
| 5 | triagem das 254 por tema (1 linha por obra) | 1 | Teco |
| 6 | estado da arte da estrutural | 3, 5 | Teco + Sol |
| 7 | fitossanidade e biologia criadas e reauditadas | 3 | Teco |
| 8 | síntese para política (primeira versão) | 6 + as outras gavetas | Teco + Sol |
| 9 | release 2 | 3, 6, 7 | verificação de publicação |

**Não há data** porque o custo por obra só existe depois da Onda 0 — prometer prazo antes disso seria
inventar. O que há é ordem e critério.

---

## 7. O que este plano não sabe, e não finge saber

1. **O custo por obra.** Não medido. Sai da Onda 0.
2. **O tema das 254.** Medido só na `BAM-001`. A triagem dirá quantas são de carbono, estrutura, praga e
   biologia — e essa contagem pode mudar a ordem das ondas.
3. **O conteúdo dos 608 MB cifrados** (`lote-*.age`). Precisa da chave de custódia; pode conter obra que
   muda o recorte.
4. **A integridade dos 981 PDFs de `_privado/`.** Presença medida, hash e trailer não. Junto com isso: a
   **proveniência** de cada grupo (URL, data, rota de aquisição), a **licença** e as condições de acesso
   (NC/ND muda o que se pode publicar) e a **duplicidade** entre grupos — o mesmo artigo pode estar em duas
   árvores com nome diferente. São quatro conferências distintas que o inventário não fez (achado do Teco R1).
5. **O protocolo da R4/LIDIA** para reauditoria de ficha publicada — a frente precisa que o releia e diga
   qual é o rito vigente: o que eu encontrei no repositório de governança é o portal de verificação
   (`portal.py`, contrato `R4-PORTAL-VERIFICACAO-R1`) e o mapa de frentes, e **a frente Bambu não está
   registrada nele** (as frentes listadas são SISTEMA, CC, MTCC, FABRICA, ALMANAKE, COCKPIT, CALCULADORA).
   Registro dessa ausência: o `MAPA_DE_FRENTES_R4.json` está marcado `PROPOSTA_NAO_VIGENTE`.
6. **O que é "recente"** na busca de atualização: última safra publicada, dois últimos anos, ou desde o
   último release? A proposta é "desde 2024 até a data da rodada", mas é decisão sua.

---

## 8. O que precisa da sua decisão, e não é minha

- **a fronteira de `bambu-carbono`** — estoque/sequestro apenas, ou também produto de carbono?
- **a janela de "recente"** na busca de atualização;
- **quem executa a reauditoria da R4** — se é a própria frente com o portal, ou rito próprio da R4;
- **o destino do pirolenhoso** — gaveta própria ou seção da estrutural;
- **a separação de `pu-vegetal`** entre bambu-carga e bambu-poliol.
