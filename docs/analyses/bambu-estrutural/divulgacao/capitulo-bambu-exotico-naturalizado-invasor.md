---
titulo: "Bambu exótico, naturalizado, invasor: a lacuna de nomenclatura que a coleção não fecha"
tipo_documental: material-didatico-institucional
natureza: derivado
frente: BAMBU-SCIENCE
versao: 1
data: 2026-11-18
---

> **Nota de proveniência e limites.** Este arquivo é um derivado didático da coleção *Advances in Bamboo
> Science* custodiada (254 PDFs, 16 volumes). A classificação de origem das espécies é **variável entre
> autores** — este texto não resolve a divergência taxonômica, ele a descreve. Não é homologação, nem
> recomendação de manejo, nem censo da flora brasileira: mede o que a coleção discute. O padrao de front
> matter e de citação de fontes ainda NÃO foi definido pela governança e está sob escrutínio de auditoria
> externa; este formato não deve ser tratado como homologado.

---

# Bambu exótico, naturalizado, invasor

## O problema: a mesma planta tem três nomes e nenhum é neutro

Quando um bambu asiático chega ao Brasil e se espalha sozinho há décadas, ele para de ser apenas "exótico" — a
palavra que descreve uma origem — e passa a ter comportamento de planta estabelecida no território. Aí a
nomenclatura se divide, é a divisão não é acadêmica: ela muda o que a lei manda fazer com a planta.

Três termos são usados para a mesma coisa, e cada um carrega uma consequência diferente:

**Exótica** — a espécie não é daqui. Origem estrangeira, sem juízo sobre comportamento. É o termo mais descritivo e mais frouxo: uma planta exótica num quintal é outra ocupando uma encosta têm o mesmo rótulo.

**Naturalizada** — chegou de fora, mas se reproduz sozinha e se mantém no território sem que ninguém a plante. O termo é técnico, da ecologia de invasões, e descreve um estado, não um veredito. "Naturalizada" é o que a coleção registra para o Bambusa vulgaris onde ela tem observação — e é o exemplo da Tanzânia, não do Brasil.

**Invasora** — o termo mais forte, e o mais mal usado: supõe **dano**, não apenas expansão. Na ecologia de invasões, uma exótica só é invasora quando sua introdução ou dispersão ameaça a diversidade biológica — espalhar-se não basta.

A confusão aparece porque os três são usados como sinônimos na conversa informal. Quem escreve "bambu exótico" costuma querer dizer as três coisas ao mesmo tempo.

> **O que este texto NÃO afirma.** Que "invasora" crie automaticamente obrigação legal: isso depende de norma, jurisdição e listagem oficial, que este texto não cita nem substitui. O que se afirma é mais modesto — a categoria muda **a conversa** (de "planta sem dono" para "planta com comportamento registrado"), e é por aí que passa qualquer política pública.

## O que a coleção mede — e o que ela não mede

A coleção custodiada tem 254 artigos em 16 volumes e é uma das principais revistas abertas da área — não é toda a literatura de bambu do mundo. Varri o texto
integral dos 254 para contar de que gênero cada artigo fala:

- **Bambusa** — 164 artigos (1.982 menções). É o gênero mais discutido da coleção.
- **Phyllostachys** — 159 artigos (1.040 menções).
- **Dendrocalamus** — 146 artigos.
- **Gigantochloa** — 64 artigos.
- **Guadua** — 58 artigos.
- **Chusquea** — 9 artigos.
- **Merostachys** — 6 artigos.

O contraste com as nativas sul-americanas é o achado: **Guadua** aparece em 58 artigos, **Chusquea** em 9 e
**Merostachys** em 6. O gênero mais discutido **nesta coleção** (164 dos 254 artigos) é justamente o que a peça original
tratava como inexistente no Brasil.

> **Método reproduzível.** `_geradores/varrer_generos.py` extrai o texto integral de cada PDF e conta menções de
> gênero com regex de palavra inteira (`\bGenero\b`), registrando artigo por artigo em `generos_por_artigo.json`.
> As contagens **se sobrepõem** — um artigo pode citar vários gêneros — e não somam 254. Menção em lista de
> referências também conta; é por isso que o número mede "em quantos artigos o gênero é discutido", não
> "quantos artigos são sobre o gênero".

> **Aviso de leitura.** Isso mede o que a coleção *discute*, não o que cresce no Brasil, nem autoriza falar de "literatura mundial": a coleção é uma revista, com 254 artigos. A coleção é dominada por
> autores da Ásia e da África e não tem um artigo de censo da flora brasileira. Dizer "o Brasil tem X de bambu
> exótico" com base aqui seria inventar denominador.

## As sete menções que decidem o assunto

O corpus trata exótico, naturalizado e invasivo em textos pontuais, e são esses que sustentam o que se pode
afirmar:

**O que é naturalizado, dito com nome e lugar.** O artigo sobre bambus da Tanzânia classifica as 25 espécies do país: cinco indígenas, vinte exóticas (80%). E fecha o critério com precisão — *"Bambusa bambos and B. vulgaris have become naturalized"*. É o exemplo mais limpo de como se escreve o termo: a espécie chegou de fora **e** se estabeleceu.

**O que é naturalizado, dito com ressalva de disputa.** O artigo sobre três espécies comerciais das Filipinas descreve *D. asper*, *B. spinosa* e *G. levis* como naturalizadas — e registra a divergência: há autor que considera *G. levis* nativa das Filipinas, contra suspeitas anteriores de introdução. Ou seja, "naturalizada" também é uma classificação em disputa, não um fato datado.

**O que é potencial invasor, dito com mecanismo.** O artigo sobre rizomas descreve o *Phyllostachys edulis* invadindo florestas vizinhas: forma camada única de folhagem, alcança o dossel das árvores é as supera por competição. O mecanismo apontado é o rizoma — a mesma estrutura que faz o bambu ser bom de propagar é a que faz ele ser difícil de conter.

**O que é invasor, dito com número — e com ceticismo.** O artigo sobre restauração no Himalaia cita Canavan et al. (2016): **232 espécies foram introduzidas fora da sua área nativa é apenas 12 foram identificadas como invasoras**. O texto registra que, para esses autores, *"fears of its invasiveness are exaggerated"*. E propõe a saída que interessa para o manejo: *"invasiveness can be managed by regular harvesting and utilizing the benefits"*.

**O que é impossível: naturalizado a partir de origem.** O único artigo sobre bambus nativos do Brasil (Vol 7, n. 100075) não usa "exótica" nem "naturalizada" em nenhum momento. Ele classifica as quatro espécies nativas — *Merostachys skvortzovii*, *Chusquea meyeriana*, *Apoclada simplex* e *Chusquea* cf. *gracilis*. **Duas das nativas são tratadas como invasoras no próprio estudo**: *M. skvortzovii* e *C. meyeriana* são descritas como *"dominant invasive species"*. A coleção diz isso de planta brasileira, sem importar nada.

**O que a coleção diz sobre o "bambu brasileiro".** Sobre *Bambusa vulgaris* 'Vittata' há um artigo inteiro (Vol 7, n. 100068) — e ele abre chamando a planta de *"a woody bamboo species of Asian origin"*. A coleção não reconhece o 'Vittata' como brasileiro. Registra a origem asiática e discute o florescimento de um exemplar cultivado na Argentina.

**O que a coleção diz sobre Phyllostachys no Brasil.** Nada substantivo. O gênero aparece 1.040 vezes, em 159 artigos, e nenhum deles trata da expansão do gênero em território brasileiro. Onde a coleção toca o Brasil, é para falar de adequação agroclimática com *Bambusa vulgaris* como referência — não de invasão.

## O que isso significa para a catalogação

A divergência não é desleixo de catalogador. É que a classificação depende de três perguntas que a coleção
responde em lugares diferentes e nem sempre no mesmo artigo:

1. **De onde veio?** — resolvida por botânica e história da introdução. É a parte mais estável.
2. **Já se reproduz sozinha aqui?** — resolvida por observação de campo, e é onde "naturalizada" entra. Muda com o tempo: uma espécie exótica hoje pode ser naturalizada em trinta anos.
3. **Causa dano mensurável?** — resolvida por ecologia de invasão, e é a que quase ninguém mediu. Daí os 232 introduzidos contra 12 invasores: a maioria das exóticas não vira invasora, e chamar todas de invasora esvazia o termo.

**Consequência para quem cataloga:** registrar as três informações em campos separados, não numa etiqueta única. "Exótica naturalizada, sem registro de invasão no Brasil" é uma classificação útil. "Exótica" sozinho é uma classificação que não decide nada.

## O bambuzal que ninguém cuida

O achado prático do corpus é uma inversão de sinal. Se a espécie é naturalizada e tem comportamento oportunista, o manejo **é** a colheita: cortar o colmo é o que a planta responde, e uso é o que contém a expansão. O artigo do Himalaia nomeia essa lógica ("regular harvesting and utilizing the benefits"), e ela importa aqui porque desloca o problema de "como erradicar" para "como usar antes que se espalhe mais".

E há um contraexemplo que fecha o raciocínio: o único estudo brasileiro da coleção sobre bambus nativos descreve duas espécies **nativas** do sul do país como invasoras dominantes. O problema de dominância não é privilégio de planta estrangeira, é a solução tampouco pode ser só "voltar ao nativo".

**O que fazer com um bambuzal abandonado que está se alastrando:**

- **Não queime nem aplique herbicida em área grande.** Rizoma sobrevive e rebrota; o custo ambiental não fecha a conta.
- **Corte rente, todo ano, no mesmo período.** É o manejo que a própria planta recompensa — e cada corte é matéria-prima.
- **Transforme o corte em cadeia produtiva.** Colmo cortado vira cerca, tutor, artesanato, briquete, carvão, painel. Os usos conhecidos do bambu vão de cerca a painel — a cartilha de bioeconomia do Acervo reúne essa lista e, quando publicada, é a referência desta frase. Hoje ela é **premissa**, não medição deste texto: nenhum artigo da coleção faz o censo dos usos, e nada garante que toda espécie sirva a algum deles.
- **Organize quem corta.** Cooperativa de manejo de exótica invasora junta três coisas que normalmente competem: controle, renda e rastreabilidade.

Este é um alerta prático, não uma receita técnica de erradicação: erradicação exige diagnóstico de espécie e de sítio, e projeto de responsável técnico. O que se afirma aqui é mais simples — **bambuzal abandonado que se alastra é, antes de tudo, matéria-prima sem uso.**

## O que falta, e é honesto dizer

- A coleção não tem censo de bambu exótico no Brasil. Qualquer número nacional de área ocupada por *Bambusa* ou *Phyllostachys* no país **não sai daqui**.
- A distinção exótica/naturalizada/invasora é usada na coleção sem definição formal única — cada artigo escolhe o critério e nem sempre o declara.
- "Naturalizada" com data de introdução é dado de herbário e de literatura histórica, não de artigo experimental.
- A cartilha de bioeconomia com os usos do bambu ainda precisa ser referenciada aqui; quando estiver publicada, entra como link próprio, não como citação indireta.

## Proveniência

| Afirmação | Fonte (coleção custodiada) |
|---|---|
| 25 espécies na Tanzânia, 5 indígenas e 20 exóticas; *B. bambos* e *B. vulgaris* naturalizados | *Palms and bamboos of Tanzania*, ABS 16 (2026) 100250, p. 4–5 |
| *D. asper*, *B. spinosa*, *G. levis* naturalizadas nas Filipinas; disputa sobre *G. levis* | *Morphological and mechanical properties of three commercially important bamboo species…*, ABS 11 (2025) 100160, DOI 10.1016/j.bamboo.2025.100160, p. 6 e 8 |
| *P. edulis* invade florestas vizinhas; rizoma como mecanismo | *Unlocking the hidden power of bamboo rhizomes*, ABS 10 (2025) 100122, p. 8 |
| 232 espécies introduzidas, 12 invasoras; medo "exagerado"; manejo pela colheita | *Ecological restoration of fragile Eastern Himalayan lands…*, ABS 13 (2025) 100203, p. 10–11 — que cita **Canavan, S., Paterson, J., Lambertini, C., Kumar, R., Meyerson, L.A., 2017.** *AoB PLANTS* 9(1), plw078, DOI 10.1093/aobpla/plw078 (a referência primária; o ano 2016 é do aceite) |
| Quatro nativas do sul do Brasil; *M. skvortzovii* e *C. meyeriana* como invasoras dominantes | Guiotoku et al., ABS 7 (2024) 100075, resumo e p. 1 |
| *B. vulgaris* 'Vittata' descrita como de origem asiática | *Flowering of Bambusa vulgaris 'Vittata'*, ABS 7 (2024) 100068, p. 1 |
| Menção por gênero nos 254 PDFs | Varredura de texto integral por `pypdf`, 254/254 arquivos |

> **Nota sobre citação.** Sem formato de citação homologado, a proveniência acima vai em tabela com volume,
> artigo e página. Quando o padrão for definido pela governança, esta seção é reconvertida — o conteúdo não muda.
