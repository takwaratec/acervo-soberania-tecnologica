# INSTRUÇÃO DE AUDITORIA EXTERNA — EIXO BAMBU ESTRUTURAL

**Pacote:** `docs/analyses/bambu-estrutural/` no repositório `acervo-soberania-tecnologica`
**Branch de referência:** `hermes/mtcc-auditoria-pacote-20261118-r1`
**Commit:** `e7120b1`
**Arquivos no escopo:** 113 (inventário com sha256 em `divulgacao/_geradores/INVENTARIO_PACOTE_SOL.json`)

---

## Antes de começar: o que você tem e o que você não tem

**Você tem:** todo o texto derivado, as fichas, a matriz comparativa, a peça HTML, os geradores que produzem cada
número, os JSON de saída das varreduras, os recibos de auditoria interna (6 rodadas) e a instrução de cada rodada.

**Você não tem:** os PDFs de origem. Eles estão em `_privado/fontes-documentais/`, que não é versionado — não por
descuido, por decisão de licença. Portanto **você não pode conferir um número contra o artigo original.** Isso é
limite declarado, e este pacote foi construído para que o limite não bloqueie a auditoria: veja a seção
"Rastreabilidade sem os PDFs".

---

## O que este material é

Material de divulgação derivado de duas famílias de fonte:

1. **A coleção *Advances in Bamboo Science*** — 254 PDFs, 16 volumes, custodiados localmente. Desta coleção derivam
   a matriz comparativa mecânica Ásia × América do Sul, a ficha Scharfenberg, a varredura de gêneros e os produtos
   de divulgação.
2. **Fontes primárias brasileiras e internacionais** — estudos publicados, planos de manejo de unidades de
   conservação, portarias estaduais e listas de espécies exóticas invasoras. Destas derivam o artigo didático, os
   carrosséis e a página de bambu exótico.

O material se destina a **pessoa leiga**: quem tem um bambuzal, quem vai construir, quem viu um post. A exigência
declarada é simples, claro, informativo, sem rodeio.

**O material não é:** homologação, parecer jurídico, recomendação de uso estrutural, nem laudo técnico. Ele declara
isso em cada peça.

---

## As sete afirmações centrais do eixo, e onde cada uma vive

Audite estas. Se uma delas cai, o eixo cai.

| # | Afirmação | Onde está | Como conferir sem o PDF |
|---|---|---|---|
| 1 | O bambu varia de 55 a 90 MPa em compressão, acima do concreto comum e muito abaixo do aço | `divulgacao/artigo-didatico-bambu.md`, `carrossel-5` slide 6 | A tabela de proveniência do artigo liga cada valor a autor e ano; `_geradores/numeros.json` traz o número cru e a conversão |
| 2 | O mesmo bambu que dá 100 MPa de média no ensaio cai para 17,8 MPa admissível (5,6×) | `artigo-didatico-bambu.md`, `carrossel-5` slides 8–9 | `numeros.json` → `controles.reducao_media_admissivel` = 5.62 com a fonte declarada no campo `_fonte` |
| 3 | Guadua verga 2,99× menos que o moso no mesmo vão, por rigidez (MOE 1,89×) | `artigo-didatico-bambu.md`, `carrossel-5` slides 10–11 | `numeros.json` → `franck.razao_deflexao` = 2.99 e `franck.razao_MOE` = 1.89, com os pares ao lado |
| 4 | Não há classificação nacional de bambu como exótica invasora; só listas estaduais, e elas divergem (PR categoria I × RS categoria 2) | `bambu-exotico-invasor-brasil-fontes.md`, `carrossel-6` slide 9 | As duas portarias são citadas por número, ano e efeito; a divergência é o achado, não um erro |
| 5 | Controle mecânico reduz 84% dos colmos em 120 dias e não erradica a espécie | `carrossel-6` slides 4–5, `artigo-didatico-bambu.md` | DOI 10.5902/1980509837089 conferível em `https://doi.org/...` — a conclusão está no resumo do artigo |
| 6 | A L21 (lacuna 21 do mapa de lacunas) pede campanha NBR 16828 em nativas amazônicas, e permanece aberta | `mapa-de-lacunas.md` seção L21, `carrossel-7`, aba L21 do HTML | O original está versionado — você pode comparar o resumo do material com o texto da lacuna, linha a linha |
| 7 | Bambusa é o gênero mais mencionado da coleção (164 de 254 artigos), e menção não é estudo | `bambu-exotico-invasor-brasil-fontes.md`, `capitulo-bambu-exotico-naturalizado-invasor.md` | `_geradores/generos_por_artigo.json` traz a contagem por artigo, com sha256 e tamanho de cada PDF |

---

## Rastreabilidade sem os PDFs

O pacote resolve o problema de três formas. Verifique se cada uma **funciona na prática**.

**1. Número cru em JSON, gerado por script.** Todo número publicado nasce de `_geradores/derivar_numeros.py` ou
`_geradores/varrer_generos.py`, e a saída fica versionada (`numeros.json`, `generos_por_artigo.json`). O caminho é:
número no texto → campo no JSON → constante no script. **Verifique amostra de pelo menos 10 números** e diga se o
caminho fecha.

**2. Varredura reproduzível com insumo fixado.** `varrer_generos.py` grava sha256 e tamanho de cada um dos 254 PDFs,
a versão de Python e de pypdf, e o diagnóstico de páginas sem camada de texto. Duas execuções independentes estão
versionadas (`generos_por_artigo.json` e `generos_por_artigo_run2.json`) com os logs. **Verifique se as duas batem**
e se o script é determinístico por leitura.

**3. Citação com localizador, não com reprodução.** Trechos literais de terceiros aparecem em bloco de citação, com
autor, veículo, volume, página e DOI. Nunca o texto integral. **Verifique se há reprodução longa** de obra de
terceiro em qualquer arquivo versionado — isso seria falha grave de licença.

---

## O histórico de auditoria interna

Houve **6 rodadas** de auditoria interna antes desta. Os pareceres estão fora do repositório (não são versionados
porque contêm citações de material em revisão), mas o **resíduo** de cada rodada está nos commits e nas mensagens.

O que a auditoria interna encontrou, e o que isso diz sobre o material:

- **Rodada 1:** cascata de redução atribuída à fonte errada; 240 PDFs onde havia 254; glulam com número que exigiria
  material mais forte que o medido.
- **Rodada 2:** as correções da rodada 1 tinham sido aplicadas só no artigo, não no pacote inteiro.
- **Rodada 3:** prompt de imagem fundindo três valores numa sequência só; afirmação de ausência baseada nos 12 lidos
  e não nos 254.
- **Rodada 4:** naturalização atribuída ao Brasil quando a fonte falava da Tanzânia; definição de "invasora" sem o
  requisito de dano.
- **Rodada 5:** **coautores inventados** numa referência; alegação jurídica sobre o que "a lei permite" sem pesquisa
  do ordenamento brasileiro.
- **Rodada 6:** bug real no script (`allen` em vez de `alien`); devolutiva sobre afirmação do interlocutor em vez de
  registro do que a fonte diz.

**Pergunta que este histórico convida:** o material corrigiu o suficiente, ou ainda carrega padrão de erro? A sexta
rodada encontrou um erro de digitação que alterava a medição — se ainda houver, procure por esse tipo: constante
escrita à mão, número que não vem do script, razão entre estudos diferentes.

---

## As perguntas da auditoria externa

Responda cada uma com **PASS**, **FAIL** ou **N/A**, com `arquivo:linha` no caso de FAIL.

### Bloco 1 — Integridade numérica

1.1. Todo número publicado tem caminho rastreável até JSON e script? Faça amostra de 10 e reporte quais fecham.

1.2. Alguma razão entre grandezas é calculada entre **estudos diferentes**? Este foi o erro da rodada 1, e o material
declara ter corrigido. Confira cada razão.

1.3. Razão declara a grandeza? "5,6×" de quê — média até admissível. "2,99×" de quê — flecha medida. "1,89×" de
quê — módulo.

1.4. Conversão de unidade correta e nomeada dos dois lados? (1 MPa = 10,1972 kgf/cm².)

1.5. Número de ensaio aparece em algum lugar como se fosse número de projeto?

### Bloco 2 — Ausência declarada

2.1. Toda afirmação de ausência tem denominador explícito ("0 em N", "não aparece entre os N lidos")?

2.2. A ausência é sustentada pela medição feita? O material distingue **varredura por título** de **varredura de
texto**? A rodada 3 reprovou por isso.

2.3. O material declara o que não sabe? Procure a seção "o que não se pode afirmar" em cada peça.

### Bloco 3 — Fonte e ato

3.1. Autoria e identificador conferem com o que se afirma? A rodada 5 achou coautores inventados — verifique
**cada referência completa** do material contra o registro público (DOI resolve, autor confere).

3.2. Lei e norma estão caracterizadas corretamente? O material afirma que o Paraná proíbe plantio e uso (categoria I)
e que o RS admite uso consagrado (categoria 2). Verifique nas portarias citadas.

3.3. O material alega efeito jurídico no Brasil sem ter pesquisado o ordenamento? A rodada 5 reprovou exatamente isso.

### Bloco 4 — Legibilidade

4.1. Um leitor sem formação técnica entende o artigo e os carrosséis? Aponte o parágrafo mais difícil de cada peça.

4.2. Todo termo técnico aparece explicado na primeira menção? (MPa, rizoma, leptomorfo, corpo de prova, MoR,
admissível.)

4.3. Há rodeio? Frases de cerimônia, recapitulação, percurso antes da afirmação?

### Bloco 5 — Distinção entre medição e proposta

5.1. Toda proposta do material está marcada como proposta, e não como resultado de estudo? (Teste de campo em 30
segundos; ciclo de corte repetido; cooperativa de manejo.)

5.2. O material afirma algo que o corpus não sustenta? Procure especificamente: "mais resistente que aço",
"solução", "resolve", "erradica", "garante".

### Bloco 6 — A peça HTML

6.1. A peça é arquivo único, offline, sem recurso externo? Verifique `src=` e `href=` com `http`.

6.2. Toda página é alcançável e legível no celular? O material declara 19 páginas verificadas em 390 px e 1280 px
com zero overflow.

6.3. O conteúdo do HTML está coerente com os `.md` que o originam? A peça é **gerada** por
`_geradores/gerar_peca.py` — verifique se editar o HTML à mão contradiria o gerador.

### Bloco 7 — Escopo e honestidade do pacote

7.1. O pacote declara o que o auditor não pode verificar (os PDFs)? É honesto sobre isso?

7.2. Há arquivo no repositório que **não deveria** estar versionado? PDF de terceiro, texto integral de obra alheia,
dado pessoal.

7.3. O pacote afirma PASS em algum lugar sem que o escopo daquele PASS cubra o que está na tela?

---

## O que NÃO pedir

- **Não peça os PDFs.** Não estão versionados por decisão de licença, e o pacote foi construído para auditar sem
  eles.
- **Não peça fonte por linha.** A convenção declarada: tabela de proveniência ao fim do artigo, `Fonte:` no rodapé
  de cada slide, `> **Fonte:**` ao fim de seção. Audite se é cumprida.
- **Não invente número.** Se algo depende de conferência contra PDF, diga "não verificável com o pacote" e siga.

---

## Como fechar

1. **Veredito por pergunta**, em tabela.
2. **FAILs ordenados por gravidade**, com `arquivo:linha` e a correção mínima.
3. **Uma frase final**: o material pode ser publicado com as correções da lista, ou há defeito estrutural que exige
   reescrita?
4. **O que você não conseguiu auditar**, e por quê.
