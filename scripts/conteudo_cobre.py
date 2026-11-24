# -*- coding: utf-8 -*-
"""Conteúdo da peça do cobre, no molde homologado (peça de boro, 2026-11-24).

Cada seção vira <section role="tabpanel" id="p-N" class="active?"> com <h2><span class="num">.
Todo <td> recebe data-l = cabeçalho da coluna, para a tabela virar cartão no celular.
"""

import re, html as _h

def _txt(s):
    """texto puro do cabeçalho, para data-l"""
    return re.sub(r"<[^>]+>", "", s).strip()

def tabela(cols, rows, cls=""):
    """cols: lista de cabeçalhos. rows: lista de listas de células (HTML)."""
    n = len(cols)
    th = "".join(f"<th>{c}</th>" for c in cols)
    labs = [_txt(c) for c in cols]
    corpo = []
    for r in rows:
        assert len(r) == n, f"linha com {len(r)} células, cabeçalho tem {n}: {r[0][:40]}"
        corpo.append("<tr>" + "".join(
            f'<td data-l="{_h.escape(labs[i], quote=True)}">{r[i]}</td>' for i in range(n)
        ) + "</tr>")
    c = f' class="{cls}"' if cls else ""
    return (f'<div class="tabwrap"><table{c}><thead><tr>{th}</tr></thead>'
            f'<tbody>{"".join(corpo)}</tbody></table></div>')

def note(titulo, corpo):
    return f'<div class="note"><strong>{titulo}</strong><p>{corpo}</p></div>'

def okbox(titulo, corpo):
    return f'<div class="okbox"><strong>{titulo}</strong><p>{corpo}</p></div>'

def danger(titulo, corpo):
    return f'<div class="danger"><strong>{titulo}</strong><p>{corpo}</p></div>'

def kpis(pares):
    itens = "".join(f'<div class="kpi"><div class="n">{n}</div><div class="l">{l}</div></div>'
                    for n, l in pares)
    return f'<div class="kpis">{itens}</div>'

def cards(itens):
    """itens: lista de (tag, titulo, corpo)"""
    blocos = "".join(
        f'<div class="card"><div class="tag">{t}</div><h4>{ti}</h4><p>{c}</p></div>'
        for t, ti, c in itens)
    return f'<div class="grid2">{blocos}</div>'

SEP = '<hr class="sep">'

def bq(txt):
    return f"<blockquote>{txt}</blockquote>"

# --------------------------------------------------------------------------- páginas
PAGINAS = []

def pagina(id_, titulo_aba, num, h2, meta, corpo):
    PAGINAS.append(dict(id=id_, aba=titulo_aba, num=num, h2=h2, meta=meta, corpo=corpo))


# ============================== 00 · COMECE AQUI ==============================
pagina("p-1", "Comece aqui", "00", "O que este artigo promete",
       "COMECE AQUI · GAVETA COBRE · 2026-11-24", f"""
<p>Este artigo explica o <strong>sulfato de cobre</strong> para quem <strong>nunca estudou química</strong>.
Não vou supor que você saiba o que é um elemento, um sal, uma fórmula ou um limite legal. Quando um termo
técnico aparecer, ele será explicado na hora — em português comum, com exemplo.</p>

<p>Ele existe para responder <strong>uma pergunta só</strong>, e é uma pergunta que quase ninguém faz:</p>

{bq("<strong>Depois que o bambu sai do tanque de tratamento, o que acontece com a água que sobra?</strong>")}

<p>Ela não é água. É uma solução de metal em concentração alta. E as receitas que circulam por aí
<strong>não dizem onde despejar</strong>.</p>

<p>Há uma segunda promessa, e ela é mais séria: <strong>vou dizer quando não sei</strong>, e vou dizer
também quando o dado <em>contraria</em> a preocupação que motivou o artigo. Isso aconteceu, e está
registrado no capítulo 05. Um texto para leigo que simplifica escondendo as ressalvas não é didático —
é propaganda.</p>

<p>Também vou separar sempre três coisas, e você vai ver essa separação repetida:</p>
<ul>
<li><strong>o que está medido</strong> — alguém mediu, com método e número;</li>
<li><strong>o que é interpretação</strong> — alguém concluiu a partir do medido;</li>
<li><strong>o que é desconhecido</strong> — ninguém mediu ainda.</li>
</ul>

<p>Se no fim você souber distinguir essas três, o artigo cumpriu o objetivo.</p>

{SEP}

<h3>Os quatro números que resumem tudo</h3>
{kpis([("29", "prótons — o que faz o cobre ser cobre"),
       ("25,45%", "é quanto do pó azul é cobre"),
       ("23", "piscinas olímpicas para diluir uma banheira"),
       ("1.800×", "mais concentrado pode ser para beber do que para o rio")])}

{note("Por que esses quatro", "O primeiro explica o que a substância é. O segundo explica por que quase toda "
 "conta de dosagem feita em casa está errada. O terceiro e o quarto são o problema — e a razão de o artigo existir.")}

{SEP}

<h3>Como ler esta peça</h3>
{cards([("se tem pressa", "Leia 06 · O resíduo",
         "É o capítulo que importa. Se você ler um único trecho deste artigo, leia aquele."),
        ("quer entender o produto", "Leia 01, 03 e 04",
         "O que é o cobre, para que serve, e quanto é seguro — na ordem."),
        ("vai usar na oficina", "Leia 07 · Uso doméstico",
         "Traz o que a instrução oficial manda e o que as receitas informais ensinam — e a diferença entre as duas."),
        ("quer conferir", "Leia 08 e Proveniência",
         "Um guia de cinco perguntas para julgar qualquer texto sobre o assunto, e a lista das fontes.")])}

{SEP}
""")

# ============================== 01 · O QUE É ==============================
pagina("p-2", "01 · O que é cobre", "01", "O que é um &quot;elemento químico&quot; — e por que cobre e sulfato de cobre não são a mesma coisa",
       "01 · O QUE É COBRE · GAVETA COBRE · 2026-11-24", f"""
<p>Tudo que você pode tocar é feito de <strong>átomos</strong>. Um átomo é uma peça minúscula. O que define
o tipo de átomo é uma coisa só: <strong>quantos prótons ele tem no centro</strong>.</p>

<p>Próton é uma partícula com carga elétrica positiva, que fica no núcleo do átomo. <strong>O número de
prótons é o &quot;documento de identidade&quot; do átomo.</strong> Um átomo com 6 prótons é carbono. Com 8,
é oxigênio. Com 26, é ferro. Com <strong>29 prótons, é cobre</strong>.</p>

<p>Isso é tudo. O cobre não é uma marca, nem um produto, nem uma receita: é o nome do átomo que tem
exatamente 29 prótons. Por isso dizemos que o cobre é um <strong>elemento químico</strong> — uma das 118
&quot;peças básicas&quot; com que a natureza monta todo o resto.</p>

<p><strong>Onde você já viu esse metal hoje:</strong> no fio elétrico da parede, no fundo da panela, na
tubulação de água, na moeda de dez centavos. É um metal comum, maleável, que conduz eletricidade muito bem.
Nada de exótico.</p>

<p><em>Sobre o &quot;29 prótons&quot;: é o número atômico do cobre, dado elementar de tabela periódica. O acervo
custodia a massa atômica e o teor nos sais em fonte primária; o número atômico fica registrado como
conhecimento de tabela periódica, não como achado custodiado.</em></p>

<h3>Cada átomo tem um peso — e o peso serve para somar receita</h3>

<p>Cada átomo tem um <strong>peso</strong>, medido numa unidade minúscula chamada <strong>massa atômica</strong>.
O carbono tem 12, o oxigênio 16, o hidrogênio 1, e o <strong>cobre tem 63,546</strong>.</p>

<p>Números com vírgula assustam, mas servem a uma função simples: <strong>permitem somar receitas.</strong>
Se você junta átomos numa proporção fixa, as massas se somam como ingredientes de bolo. Guarde isso, porque
é a chave de tudo que vem depois.</p>

{SEP}

<h3>A confusão número um: o pó azul não é o metal</h3>

<p>Aqui está o erro que <strong>muda a dose por um fator de quase quatro</strong>, e que quase todo texto
informal comete.</p>

<p>O cobre, sozinho, não é o que se compra na loja. Na prática ele aparece <strong>combinado com outros
átomos</strong>, formando substâncias diferentes. Uma substância feita de dois ou mais elementos ligados
chama-se <strong>composto</strong>. Sais e ácidos são tipos de composto.</p>

<p>O que você compra é o <strong>sulfato de cobre</strong>: um sal azul, em pó ou em cristal. E ele carrega
cobre junto com outras coisas — enxofre e água.</p>

{tabela(["O que a pessoa compra", "O que é de verdade", "Quanto é cobre dentro"],
 [["<strong>cobre</strong> (Cu)", "o metal, o átomo de 29 prótons", "100% (é ele mesmo)"],
  ["<strong>sulfato de cobre</strong> (CuSO₄·5H₂O)",
   "cobre + enxofre + oxigênio + água", "<strong>25,45%</strong>"],
  ["<strong>sulfato de cobre anidro</strong> (CuSO₄)", "o mesmo, <strong>sem</strong> a água do cristal",
   "<strong>39,81%</strong>"]])}

<p><strong>Leia a terceira coluna com calma.</strong> Um quilo do pó azul <strong>não</strong> contém um quilo
de cobre: contém <strong>254 gramas</strong> de cobre e 746 gramas de outras coisas.</p>

<p>Agora o problema prático. Se uma receita pede &quot;1 quilo de sulfato de cobre&quot;, a pessoa está
colocando 254 gramas de metal na água. Se ela achar que está colocando 1 quilo de cobre, <strong>vai errar
toda conta que fizer a partir daí</strong> — inclusive a conta do que fazer com a água depois.</p>

{note("A analogia que resolve", "Imagine que você compra um saco de farinha com fermento já misturado. "
 "Se a receita pede fermento, você não joga o saco inteiro — você calcula quanto de fermento tem ali dentro. "
 "Com o sulfato de cobre é igual: <strong>o pó azul é farinha com fermento</strong>. Só um quarto dele é cobre.")}

<h3>O detalhe que parece firula e não é: o &quot;anidro&quot;</h3>

<p>Você notou que a tabela tem duas linhas de sulfato de cobre, uma com 25,45% e outra com 39,81%, sendo
que as duas são basicamente as mesmas peças? A diferença é <strong>água</strong>.</p>

<p>O sulfato de cobre comum carrega <strong>cinco moléculas de água dentro da própria estrutura</strong> —
não molhada por fora, mas encaixada como parte do cristal. Isso se chama <strong>água de hidratação</strong>.
Quando um nome vem com &quot;anidro&quot;, significa <strong>sem essa água</strong>. Sem a água, a mesma massa
contém muito mais cobre: 39,81% em vez de 25,45%.</p>

<p>Parece detalhe de químico. Na verdade é a diferença entre comprar a coisa certa e a errada no balcão —
e entre uma dose e uma dose <strong>1,56 vezes maior</strong> usando o mesmo peso de pó.</p>

{SEP}

<h3>Resumo do capítulo</h3>
<p><strong>Estabelecido:</strong> o cobre é o elemento de 29 prótons; não se usa cobre puro, mas compostos;
o conteúdo de cobre muda conforme o composto (25,45% no sulfato hidratado, 39,81% no anidro); um quilo do
pó azul carrega 254 gramas de metal.</p>
<p><strong>Interpretação:</strong> por isso toda conta de dosagem feita em casa, sem converter a base, está
errada — e erra para baixo, o que subestima a quantidade de metal que vai para a água.</p>
<p><strong>Desconhecido:</strong> qual produto exato — hidratado ou anidro — está na prateleira que o
usuário doméstico compra. As embalagens nem sempre dizem.</p>

{SEP}
""")

# ============================== 02 · DE ONDE VEIO ==============================
pagina("p-3", "02 · De onde veio", "02", "De onde vem o cobre do seu quintal",
       "02 · DE ONDE VEIO · GAVETA COBRE · 2026-11-24", f"""
<p>Aqui o cobre é diferente do boro, e a diferença importa para o argumento deste artigo.</p>

<p><strong>Cobre não é raro.</strong> É um metal de base, extraído em dezenas de países, reciclado em
escala industrial há mais de um século. Não existe escassez de cobre no mundo, nem risco de faltar.</p>

<p>O que existe é outra coisa, e é o ponto deste capítulo: <strong>o Brasil não produz o sulfato de cobre
que consome. Ele importa.</strong> E os números da importação dizem algo sobre o preço — e o preço diz algo
sobre o descarte.</p>

<h3>O dado oficial, em 2025</h3>

<p>O órgão do governo brasileiro que registra comércio exterior (ComexStat) classifica o sulfato de cobre
sob um código chamado <strong>NCM 2833.25</strong> — um número que funciona como &quot;código de barras
alfandegário&quot; da substância. Em 2025:</p>

{kpis([("177,9 t", "importadas no ano"),
       ("US$ 370 mil", "total pago"),
       ("US$ 2,08", "preço médio por quilo"),
       ("80,4%", "do peso vem da China")])}

{tabela(["Origem", "Fatia do peso", "Fatia do valor", "Preço por quilo"],
 [["<strong>China</strong>", "<strong>80,4%</strong>", "<strong>48,3%</strong>", "US$ 1,25"],
  ["Estados Unidos", "—", "—", "US$ 45,57"],
  ["Reino Unido", "—", "—", "US$ 148,43"]])}

{danger("O erro que quase todo texto comete aqui", "Misturar <strong>peso</strong> com <strong>valor</strong>. "
 "A China responde por 80,4% do peso e por 48,3% do valor. Se alguém disser &quot;a China domina 80% do "
 "mercado&quot;, está falando de tonelada; se disser &quot;48%&quot;, está falando de dinheiro. "
 "São duas frases diferentes, e as duas aparecem na mesma tabela.")}

<h3>O número mais estranho: o mesmo produto custa 119 vezes mais</h3>

<p>Olhe os preços por quilo de novo: <strong>US$ 1,25</strong> vindo da China, <strong>US$ 45,57</strong>
dos Estados Unidos, <strong>US$ 148,43</strong> do Reino Unido.</p>

<p>O maior dividido pelo menor dá <strong>119 vezes</strong> — dentro do <strong>mesmo código alfandegário</strong>,
ou seja, oficialmente o &quot;mesmo produto&quot;.</p>

<p><strong>O que isso significa?</strong> Provavelmente que o código junta coisas diferentes: pó técnico
de grau agrícola, reagente de laboratório, produto já formulado. Mas <strong>isso é hipótese minha</strong> —
a fonte de comércio não distingue. O que está medido é a dispersão; a explicação não está.</p>

<p>E por que isso importa para o artigo? Porque mostra que <strong>o produto que chega ao balcão não é
uma coisa só</strong>. Quem compra &quot;sulfato de cobre&quot; pode estar comprando purezas muito diferentes —
e a receita informal não pede pureza nenhuma.</p>

<h3>A série histórica: o consumo brasileiro caiu 86%</h3>

<p>Somando a série desde 1997, o volume importado caiu de <strong>1.279 toneladas</strong> para
<strong>9,3 toneladas em 2020</strong> — uma queda de <strong>86%</strong> — com repiques em 2022 e 2024.</p>

<p><strong>A conclusão que o dado sustenta:</strong> a escala brasileira desse produto é modesta e oscilante,
e o preço é baixo. <strong>Não existe pressão econômica para economizar nem na compra nem no descarte.</strong>
A barreira não é dinheiro.</p>

<p><strong>A conclusão que o dado NÃO sustenta:</strong> dizer que o Brasil &quot;usa muito&quot; ou
&quot;usa pouco&quot; sulfato de cobre em bambu. A importação é do país inteiro, somando agricultura,
indústria, laboratório e tratamento de madeira. <strong>Quanto disso vai para bambu, ninguém mediu.</strong></p>

{SEP}

<h3>Resumo do capítulo</h3>
<p><strong>Estabelecido:</strong> 177,9 t e US$ 370 mil em 2025; China com 80,4% do peso e 48,3% do valor;
dispersão de preço de 119× dentro do mesmo código; queda de 86% entre 1997 e 2020; preço médio baixo.</p>
<p><strong>Interpretação:</strong> a dispersão de preço sugere graus de pureza diferentes sob o mesmo código;
o preço baixo significa que a barreira ao descarte correto não é econômica.</p>
<p><strong>Desconhecido:</strong> quanto do volume importado vai para tratamento de bambu; e qual grau de
pureza está no produto que o usuário doméstico compra.</p>

{SEP}
""")

# ============================== 03 · PARA QUE SERVE ==============================
pagina("p-4", "03 · Para que serve", "03", "Para que serve: o que o cobre faz e o que ele não faz",
       "03 · PARA QUE SERVE · GAVETA COBRE · 2026-11-24", f"""
<p>Cobre é <strong>fungicida</strong>. Isso quer dizer que ele combate fungo.</p>

<p>Não é força de expressão: o cobre desmonta a membrana e as enzimas da célula do fungo. É por isso que
ele é usado há mais de um século na agricultura — a mistura de sulfato de cobre com cal, chamada
<strong>calda bordalesa</strong>, é um dos fungicidas mais antigos que existem e ainda é usada em videira
e fruticultura.</p>

<h3>O que ele NÃO faz — e isso muda tudo</h3>

<p>Aqui está a informação que quase nunca aparece nos textos informais:</p>

<p><strong>O cobre não mata cupim, não mata broca, não mata besouro.</strong> Ele é fungicida, não é
inseticida.</p>

{note("A frase está na literatura técnica", "Na tabela de preservantes do estudo de Gauss (2020), a combinação "
 "de cloreto de zinco com sulfato de cobre aparece descrita como <em>&quot;good fungicide&quot;</em> — bom "
 "fungicida — e, no mesmo campo, <em>&quot;ineffective for termites and insects&quot;</em> — ineficaz para "
 "cupim e inseto.")}

<h3>Então por que a receita mistura três coisas?</h3>

<p>Porque ninguém resolve o problema inteiro com um produto só. É a mesma lógica de um remédio para gripe
que junta três princípios ativos.</p>

{tabela(["Ingrediente", "O que ele faz", "Por que está ali"],
 [["<strong>boro</strong> (ácido bórico e bórax)", "mata inseto: cupim, broca, besouro",
   "cobre o que o cobre não cobre"],
  ["<strong>cobre</strong> (sulfato de cobre)", "mata fungo", "o fungicida da mistura"],
  ["<strong>cromo</strong> (dicromato)", "<strong>fixa</strong> os outros dois no bambu",
   "funciona como cola, para não saírem na primeira chuva"]])}

<p>Essa mistura de três tem nome: <strong>CCB</strong> — <em>borato de cobre cromatado</em>. A sigla é só
a junção das iniciais de cada um.</p>

<p>E aqui um dado que reorganiza a dosagem, e que só existe porque alguém mediu: na formulação descrita
pela norma brasileira (NBR 6232) e usada no ensaio de Rusch (2023), o CCB é composto de
<strong>26% de sulfato de cobre</strong>, <strong>63,5% de dicromato de potássio</strong> e
<strong>10,5% de ácido bórico</strong>.</p>

<p><strong>Leia de novo:</strong> na mistura, mais de <strong>seis em cada dez partes</strong> são de cromo —
e o cobre, que dá nome a metade do artigo, é <strong>um quarto</strong> da formulação.</p>

{okbox("Por que o cromo importa para o resíduo", "Porque o cromo é a parte da mistura que se move no ambiente. "
 "No ensaio de campo de cinco anos que está no capítulo 05, o cobre praticamente não subiu no solo "
 "(+12%, sem significância estatística) — mas o <strong>cromo subiu 86%</strong>. Quem usa CCB não está "
 "usando só cobre: está usando cromo, e é o cromo que aparece no solo.")}

<h3>E na agricultura, qual é a dose?</h3>

<p>Na agricultura o sulfato de cobre é usado como fungicida em pulverização, em concentrações bem menores
que as de um banho de imersão de bambu, e com número de aplicações limitado por norma. A pergunta
&quot;qual é a diferença de dosagem entre a agricultura e o tratamento de bambu&quot; é legítima, e a resposta
honesta é:</p>

<p><strong>Uma é diluída e pulverizada sobre a folha; a outra é concentrada num tanque, e o colmo fica
mergulhado por dias.</strong> São situações diferentes. Mas <strong>não localizei, nas fontes custodiadas,
uma comparação numérica direta entre a dose agrícola e a dose de banho</strong> — e por isso não vou
inventar essa razão.</p>

{SEP}

<h3>Resumo do capítulo</h3>
<p><strong>Estabelecido:</strong> o cobre é fungicida e não é inseticida; o CCB é 26% sulfato de cobre,
63,5% dicromato e 10,5% ácido bórico; o cromo é o elemento que fixa e é o que aparece no solo.</p>
<p><strong>Interpretação:</strong> é por isso que quase toda receita mistura três sais — cada um cobre
uma parte do problema.</p>
<p><strong>Desconhecido:</strong> a razão numérica entre a dose agrícola e a dose de banho de bambu.</p>

{SEP}
""")


# ============================== 04 · FAZ BEM OU MAL ==============================
pagina("p-5", "04 · Faz bem ou mal", "04", "O cobre faz bem ou faz mal? A resposta exige uma ferramenta nova",
       "04 · FAZ BEM OU MAL · GAVETA COBRE · 2026-11-24", f"""
<p>Esta é a pergunta que todo mundo faz, e ela <strong>não tem resposta</strong> do jeito que é formulada.
&quot;Faz bem ou mal&quot; é pergunta de remédio. Para substâncias, a pergunta correta é outra: <strong>quanto</strong>.</p>

<p>Existe uma frase que parece piada e é a base de toda a toxicologia: <strong>&quot;a dose faz o veneno&quot;</strong>.
Qualquer substância — água, sal, ferro, vitamina — é inofensiva em certa quantidade, benéfica em outra e
letal em outra.</p>

<h3>Primeiro: o corpo precisa de cobre?</h3>

<p><strong>Precisa.</strong> E aqui o cobre é <strong>diferente do boro</strong>: o boro não é reconhecido como
nutriente essencial para humanos; o cobre é. Seu corpo usa cobre em enzimas que participam do metabolismo
do ferro e da proteção das células.</p>

<p>A quantidade é pequena: cerca de <strong>1 miligrama por dia</strong> — a ordem de grandeza de uma pitada
de sal.</p>

{danger("A conclusão errada que sai daí", "&quot;Se é essencial, é seguro.&quot; <strong>Não.</strong> "
 "Água é essencial e afoga. Ferro é essencial e intoxica criança que engole as pastas do armário. "
 "Vitamina é essencial e em excesso faz mal. <strong>Essencial não é sinônimo de inofensivo</strong> — "
 "o que separa o remédio do veneno é sempre a mesma coisa: quanto, e por quanto tempo.")}

{SEP}

<h3>As três réguas — e por que elas não se contradizem</h3>

<p>Quando se fala em quanto cobre é seguro, aparecem números diferentes. Eles <strong>medem coisas
diferentes, para populações diferentes</strong>. Confundi-los é a maior fonte de erro nesta matéria.</p>

{tabela(["Régua", "Valor", "Para que serve"],
 [["<strong>Água de beber</strong> (OMS)", "<strong>2 mg/L</strong>",
   "proteger a população inteira, todos os dias, pela vida toda"],
  ["<strong>Efluente</strong> (CONAMA 430/2011)", "<strong>1,0 mg/L</strong>",
   "o que uma atividade pode lançar na rede ou no corpo receptor"],
  ["<strong>Água doce Classe 1</strong> (CONAMA 357/2005)", "<strong>0,009 mg/L</strong>",
   "o rio protegido — a água onde se espera vida aquática"],
  ["<strong>Invertebrado aquático, crônico</strong>", "<strong>0,00111 mg/L</strong>",
   "o nível em que a vida do rio começa a sofrer"]])}

<p><strong>Um número mais baixo não é &quot;mais rigoroso&quot;</strong> — é um número que protege outro
objeto. Quem compara 2 mg/L com 0,009 mg/L e conclui que &quot;um dos dois está errado&quot; não entendeu
que os dois estão certos e falam de coisas diferentes.</p>

<h3>O detalhe que quase ninguém sabe sobre os 2 mg/L</h3>

<p>Os <strong>2 mg/L</strong> da água de beber são o número mais citado de todos. E ele é
<strong>provisório</strong> — a própria Organização Mundial da Saúde diz que o valor é provisório
<em>&quot;as a result of uncertainties in the dose–response&quot;</em>, isto é, por causa de incertezas
na relação entre dose e efeito.</p>

<p>Também vale saber de onde ele saiu: de um estudo com <strong>61 voluntários</strong>, que identificou
como efeito agudo a <strong>náusea</strong> a partir de 4 mg/L (o LOAEL), com 2 mg/L como o nível em que
não se observou efeito (o NOAEL).</p>

{note("Provoca uma pergunta: então o problema é o estômago?", "Não é o principal. A náusea é o efeito "
 "<strong>agudo</strong>. O efeito <strong>crônico</strong> — o que importa para exposição repetida — é "
 "<strong>hepático</strong>: o cobre se acumula no fígado. A própria OMS registra que o cobre "
 "<em>&quot;accumulates in the liver, brain and eyes&quot;</em>. Quem trata 2 mg/L como fronteira universal "
 "entre remédio e veneno está promovendo um número provisório a definitivo — e trocando o órgão do efeito.")}

<h3>E em dose por peso de corpo?</h3>

<p>Para quem precisa comparar exposições, existe a dose por quilo de peso. Em estudo de duas semanas com
ratos:</p>

{tabela(["Via", "Dose", "Efeito observado"],
 [["água de beber", "<strong>LOAEL 10 mg/kg/dia</strong> (machos)", "gotas proteicas no túbulo do rim"],
  ["água de beber", "NOAEL 26 mg/kg/dia (fêmeas)", "sem efeito renal"],
  ["dieta", "<strong>sem efeito a 23 mg/kg/dia</strong>", "—"],
  ["dieta", "46 mg/kg/dia (machos)", "hiperplasia e hiperqueratose no estômago"]])}

<p><strong>O achado que vale reter:</strong> o cobre é <strong>menos</strong> tóxico pela dieta que pela
água. A <strong>matriz muda a dose efetiva</strong>. Isso sustenta uma regra que vale para o artigo inteiro:
<strong>grandeza sem via e sem meio não significa nada.</strong> &quot;2 mg&quot; de quê, em quê, por qual
caminho?</p>

{SEP}

<h3>A razão que resume o problema</h3>

<p>Agora coloque os dois números que mais importam lado a lado:</p>

<ul>
<li>o cobre é <strong>potável</strong> até <strong>2 mg/L</strong>;</li>
<li>o cobre começa a prejudicar a <strong>vida do rio</strong> em <strong>0,00111 mg/L</strong>.</li>
</ul>

<p>Dois dividido por 0,00111 dá <strong>1.802</strong>.</p>

{bq("<strong>O mesmo cobre é seguro para você beber numa concentração mil e oitocentas vezes maior do que aquela que prejudica um bichinho de água.</strong>")}

<p>Não é exagero de militante. É a divisão de dois números oficiais, cada um com sua fonte.</p>

{SEP}

<h3>Duas frases que circulam — e as duas estão erradas</h3>

<p><strong>&quot;O cobre é cancerígeno.&quot;</strong> Não é o que as fontes dizem. O cobre não está
classificado como carcinogênico, e os estudos de longo prazo não apontam aumento de tumores. Dizer isso é
falso.</p>

<p><strong>&quot;Então o cobre é seguro.&quot;</strong> Também não. O efeito crítico do cobre é outro:
<strong>acúmulo no fígado</strong> em exposição repetida, e <strong>toxicidade para a vida aquática</strong>
em concentração muito baixa. O caso extremo documentado é a <strong>doença de Wilson</strong>, uma condição
genética rara em que o corpo não consegue eliminar cobre — e que mostra, de forma dramática, o que o excesso
crônico faz ao fígado.</p>

{note("A distinção que resolve a confusão", "<strong>Carcinogênico</strong> = capaz de causar câncer. "
 "<strong>Tóxico para o fígado</strong> = prejudica o órgão em exposição repetida. "
 "<strong>Tóxico para a vida aquática</strong> = prejudica organismos na água em concentração baixíssima. "
 "São três coisas diferentes, e uma não autoriza a outra — em nenhuma direção.")}

<h3>Por que a criança aparece em toda norma de cobre</h3>

<p>Porque o cobre é <strong>essencial e necessário ao desenvolvimento</strong>, e ao mesmo tempo
<strong>o excesso é hepático</strong>. A margem entre o que o corpo precisa e o que o prejudica é mais estreita
do que parece — e é por isso que existe recomendação de ingestão, e existe também limite.</p>

{SEP}

<h3>Resumo do capítulo</h3>
<p><strong>Estabelecido:</strong> o cobre é nutriente essencial (~1 mg/dia); os 2 mg/L da OMS são
<strong>provisórios</strong>; o efeito crônico é hepático; o cobre é menos tóxico pela dieta que pela água;
2 ÷ 0,00111 = 1.802.</p>
<p><strong>Interpretação:</strong> comparar limites de objetos diferentes (água de beber × rio protegido) é
o erro mais comum nesta matéria.</p>
<p><strong>Desconhecido:</strong> qual é a exposição real do usuário doméstico que manipula sulfato de cobre
sem proteção — ninguém mediu.</p>

{SEP}
""")


# ============================== 05 · BAMBU E COBRE ==============================
pagina("p-6", "05 · Bambu e cobre", "05", "O bambu e o cobre: por que uma planta precisa de veneno para durar",
       "05 · BAMBU E COBRE · GAVETA COBRE · 2026-11-24", f"""
<p>Agora a segunda metade do artigo, e a razão pela qual este material foi escrito.</p>

<h3>Bambu não é madeira, e é por isso que ele apodrece</h3>

<p>O bambu é uma <strong>gramínea</strong> — é parente do capim, não do cedro. Cresce rápido e é resistente,
mas tem uma fraqueza estrutural: <strong>é cheio de açúcar e amido</strong>.</p>

<p>A madeira tem <strong>lignina</strong> — uma substância natural que funciona como resina: gruda as fibras,
impermeabiliza e protege. O bambu tem muito menos. Resultado: do ponto de vista de um fungo ou de um inseto,
o bambu é <strong>comida fácil</strong> — rica em nutrientes, macia e úmida.</p>

<p>Se você cortar um colmo e deixá-lo no quintal, em poucos meses ele estará sendo devorado. Não é azar:
é bioquímica.</p>

<h3>Como se protege: encharcar com um veneno solúvel</h3>

<p>A lógica do tratamento é simples de enunciar: <strong>substituir, dentro do colmo, o líquido que já está
lá por uma solução que mate fungo.</strong></p>

<p>Funciona como marinar. O colmo é um canudo cheio de seiva. Se você colocar a ponta numa solução e esperar,
a solução entra. O cobre serve porque é <strong>solúvel em água</strong>: dissolve-se bem e penetra com
facilidade.</p>

<p>E aqui está a propriedade central de todo este capítulo, e ela tem duas faces:</p>

{bq("<strong>A mesma solubilidade que faz o cobre entrar no bambu é a que faz o cobre sair.</strong>")}

<p>O cobre não se <strong>liga</strong> ao bambu — diferente do cromo, que é justamente o que fixa. O cobre
fica depositado dentro, dissolvido ou cristalizado. Enquanto o material está seco, ele fica. Quando a umidade
volta — chuva, solo úmido, condensação — ele pode voltar a se dissolver e migrar para fora.</p>

<p>Isso não é defeito de fabricação. É a natureza do produto. E é por isso que nenhum texto honesto sobre
preservação de bambu com cobre pode prometer durabilidade eterna.</p>

<h3>O nome técnico do problema: lixiviação</h3>

<p>O processo de a água atravessar o material e carregar o produto embora chama-se <strong>lixiviação</strong>.
Não confunda com lavagem: lavagem é de fora para fora. Lixiviação é a água <strong>entrando, dissolvendo o
que está dentro e saindo com ele</strong>.</p>

<p>Uma analogia útil: pense num <strong>saquinho de chá</strong>. Enquanto está seco, o chá fica no saquinho.
Ao mergulhar na água, o sabor sai — e não volta. Bambu tratado com cobre é um saquinho de chá que precisa
ficar seco.</p>

<p>O manual oficial indiano (NMBA 2006) diz isso com clareza: conservantes que não fixam, expostos à chuva,
são lixiviados e com o tempo &quot;lavados&quot; do bambu — e por isso <strong>não são adequados para uso ao
ar livre</strong>.</p>

{SEP}

<h3>Quanto cobre fica no bambu? Menos do que a receita manda</h3>

<p>Esta é uma das medições mais úteis de todo o material, e quase ninguém a conhece: <strong>a dose que se
prepara não é a dose que fica.</strong></p>

<p>Em ensaio com <em>Phyllostachys edulis</em>, quando se mirava uma retenção de <strong>4,0 kg/m³</strong>
de preservante, o bambu reteve <strong>0,88 kg/m³</strong> — <strong>22% do alvo</strong>. Mirando
<strong>6,4 kg/m³</strong>, reteve <strong>1,49</strong> — <strong>23%</strong>.</p>

<p>No <em>Pinus</em>, madeira de referência no mesmo ensaio, os números foram <strong>4,61 e 7,12 kg/m³</strong>
— <strong>115% e 111%</strong> do alvo.</p>

{danger("A conclusão que NÃO se pode tirar", "&quot;Então o bambu não retém nada e o tratamento é inútil.&quot; "
 "<strong>Não.</strong> Este é <strong>um</strong> ensaio, com <strong>uma</strong> espécie, e a faixa de "
 "retenção medida em bambu na literatura vai de <strong>0,28 a 17,5 kg/m³</strong> conforme a espécie, o "
 "método e a concentração. Generalizar a partir de um resultado é exatamente o erro que uma auditoria "
 "anterior pegou neste material.")}

<p><strong>O que o dado sustenta, e é importante:</strong> a dosagem escrita na bula <strong>não descreve
o que ficou no material</strong>. Quem calcula resíduo a partir da dose preparada está superestimando o que
entrou no bambu — e subestimando o que <strong>sobrou na água</strong>.</p>

{SEP}

<h3>O achado que contraria a preocupação — e fica registrado</h3>

<p>Aqui o artigo precisa ser honesto contra si mesmo.</p>

<p>O ensaio de campo de Rusch et al. (2023) deixou bambu tratado com CCB enterrado por <strong>cinco anos</strong>
e depois mediu o solo. O resultado:</p>

{tabela(["O que se mediu", "Controle (água)", "Tratado CCB 3%", "Diferença"],
 [["<strong>cobre no solo</strong>", "24,9 ppm", "<strong>27,9 ppm</strong>",
   "+12% — <strong>sem significância estatística</strong>"],
  ["<strong>cromo no solo</strong>", "33,2 ppm", "<strong>61,7 ppm</strong>", "<strong>+86%</strong>"]])}

<p>Os autores registram que, para o cobre, as concentrações ficaram muito próximas das do local com bambu
sem tratamento.</p>

{okbox("O que isso significa", "A hipótese de que <strong>o cobre do CCB contamina o solo</strong> "
 "<strong>não se confirmou</strong> neste ensaio. O que se moveu, e muito, foi o <strong>cromo</strong>. "
 "Isso não derruba o artigo — derruba <strong>uma parte</strong> dele, e muda o foco para o lugar certo: "
 "o problema não é o que fica no material, é <strong>o que sobra na água</strong>.")}

{SEP}

<h3>Resumo do capítulo</h3>
<p><strong>Estabelecido:</strong> o bambu é rico em amido e pobre em lignina; o cobre não se fixa e é
lixiviável; a retenção medida em uma espécie ficou em 22–23% do alvo; após cinco anos em campo o cobre
<strong>não</strong> elevou o solo de forma significativa, e o cromo subiu 86%.</p>
<p><strong>Interpretação:</strong> por isso a dose preparada não descreve a dose retida, e por isso o
resíduo líquido é o objeto principal.</p>
<p><strong>Desconhecido:</strong> a retenção média por espécie de bambu em condições reais de oficina;
e quanto cobre fica no material quando se usa a receita informal, que é mais concentrada que a testada.</p>

{SEP}
""")




# ============================== 06 · O RESÍDUO ==============================
pagina("p-7", "06 · O resíduo", "06", "A parte que importa: o resíduo",
       "06 · O RESÍDUO · GAVETA COBRE · 2026-11-24", f"""
<p><strong>Se você ler um único trecho deste artigo, leia este.</strong></p>

<p>Tratamento não é vacina permanente, e a água que sobra não desaparece. Ela tem metal dissolvido, e alguém
precisa decidir o que fazer com ela. É aqui que o artigo deixa de ser curiosidade e vira problema.</p>

<h3>Primeiro: quanto líquido é isso</h3>

<p>A instrução oficial da Embrapa recomenda um <strong>tonel de 200 litros</strong>. A receita informal manda
preparar <strong>100 litros</strong>. Uma banheira de banho tem mais ou menos 200 litros.</p>

{bq("<strong>A receita é meia banheira de solução azul. O tonel é uma banheira cheia.</strong>")}

<p>É essa a escala doméstica do problema. Não é uma indústria. É <strong>uma banheira</strong>.</p>

<h3>Segundo: quanto cobre tem dentro dela</h3>

<p>Meia banheira (100 litros) a 1% carrega <strong>1 quilo do pó azul</strong>, que são <strong>254 gramas
de cobre</strong>.</p>

<p>É mais ou menos o peso de um celular. De metal puro, <strong>dissolvido</strong> na água do seu quintal.</p>

<h3>Terceiro: meio balde estraga uma piscina</h3>

<p>Aqui vale desfazer uma imagem comum. A ideia que circula é &quot;uma gota contamina uma piscina&quot;.
<strong>Medindo, não é isso</strong> — e o número real é mais forte que a lenda.</p>

<p>Uma gota de 0,05 mL precisaria de <strong>14 litros</strong> de água para chegar ao limite de rio
protegido. Não contamina piscina nenhuma. <strong>É bom dizer isso</strong>, porque um texto que exagera
perde o direito de ser levado a sério no resto.</p>

<p>Mas veja o que de fato acontece:</p>

{tabela(["Quanto de solução", "O que acontece"],
 [["<strong>8,8 litros</strong> (44 copos de água)",
   "<strong>deixa uma piscina olímpica inteira acima do limite</strong> para rio protegido"],
  ["<strong>1 litro</strong> da receita dobrada (9%)",
   "<strong>faz o mesmo</strong> com uma piscina olímpica inteira"]])}

{bq("<strong>Um balde de solução jogado num rio estraga a água de uma piscina olímpica cheia.</strong>")}

<h3>Quarto: a banheira precisaria de 23 piscinas</h3>

<p>Agora a direção contrária, que é a que mostra o absurdo:</p>

{tabela(["O que sobra na sua casa", "Água limpa necessária para diluir até virar água de rio aceitável"],
 [["<strong>Meia banheira</strong> (a receita, 100 L)", "<strong>11 piscinas olímpicas</strong>"],
  ["<strong>Uma banheira</strong> (o tonel, 200 L)", "<strong>23 piscinas olímpicas</strong>"],
  ["<strong>Uma banheira da receita dobrada</strong> (9%)", "<strong>204 piscinas olímpicas</strong>"]])}

{danger("E aqui está o ponto que quase todo mundo erra", "<strong>Diluir não resolve nada.</strong> "
 "O cobre não apodrece, não evapora, não é comido por bactéria. <strong>Cobre não desaparece — ele só muda "
 "de lugar.</strong> Diluir é espalhar o mesmo metal por mais água. O problema continua existindo; ele só "
 "fica mais difícil de ver.")}

<h3>O pH — o número que dispensa explicação</h3>

<p>O estudo que mediu o descarte também mediu a acidez das soluções, na concentração de uso. Acidez se mede
numa escala chamada <strong>pH</strong>: 7 é neutro, abaixo de 7 é ácido. Quanto menor o número, mais ácido.</p>

{tabela(["O que é", "pH"],
 [["<strong>CCB do jeito que se usa</strong>", "<strong>0,22</strong>"],
  ["<strong>cobre + boro do jeito que se usa</strong>", "<strong>1,28</strong>"],
  ["<em>suco de limão (para comparar)</em>", "<em>por volta de 2</em>"],
  ["<em>vinagre (para comparar)</em>", "<em>por volta de 3</em>"]])}

{bq("<strong>A solução de tratamento é mais ácida que suco de limão.</strong> O CCB é mais ácido que limão por mais de dez vezes — na faixa do ácido de bateria de carro.")}

<p>E essas são as concentrações <strong>testadas</strong> — menores que as da receita que circula.</p>

<h3>O teste da alface: o que a água faz com a vida</h3>

<p>Existe um estudo brasileiro que fez exatamente a pergunta certa. É uma dissertação de mestrado da
Universidade Federal do Triângulo Mineiro, de 2020. O autor pegou as soluções usadas no tratamento de bambu
e colocou <strong>sementes de alface</strong> nelas, cada vez mais diluídas. Depois contou quantas nasceram.</p>

<p>Por que alface? Porque é um <strong>detector vivo</strong>: se a alface não nasce, aquela água está
agressiva — e o que é agressivo para a alface costuma ser agressivo para o resto.</p>

{tabela(["A solução estava…", "Nasceu alguma semente?"],
 [["<strong>do jeito que se usa</strong>", "<strong>nenhuma</strong>"],
  ["<strong>diluída 3 vezes</strong>", "<strong>nenhuma</strong>"],
  ["<strong>diluída 5 vezes</strong>", "<strong>nenhuma</strong>"],
  ["<strong>diluída 10 vezes</strong>", "<strong>nenhuma</strong>"],
  ["diluída 20 vezes", "quase nenhuma"],
  ["diluída 50 vezes", "ainda muito pouco"]])}

{bq("<strong>Diluída dez vezes, a solução ainda impediu toda semente de nascer.</strong>")}

<p>E não foi só com o cobre. Aconteceu igual com o CCB e com o boro sozinho.</p>

<h3>A comparação que assusta</h3>

<p>O autor comparou com um herbicida comercial — o <strong>Roundup</strong>, aquele que mata planta daninha
no pasto. No mesmo tipo de teste, com a mesma semente:</p>

{tabela(["O que foi testado", "Quanto nasceu (escala de 0 a 100)"],
 [["<strong>Roundup</strong>", "<strong>acima de 80</strong>"],
  ["<strong>solução de cobre e boro</strong>", "<strong>11 no melhor caso</strong>"]])}

{danger("O que isso significa", "A água que sobra do tratamento de bambu <strong>inibe mais a vida vegetal "
 "do que um herbicida comercial</strong>. Mesma semente, mesma métrica, mesmo laboratório.")}

<p>E a raiz, que é ainda mais sensível: a melhor raiz de qualquer tratamento tinha <strong>0,33 mm</strong>,
contra <strong>2,78 mm</strong> em água limpa — <strong>oito vezes menos</strong>. A semente pode até nascer,
e a raiz não cresce.</p>

{SEP}

<h3>Então o que fazer com essa água?</h3>

<p><strong>A resposta curta: reusar.</strong> As duas instruções oficiais dizem a mesma coisa.</p>

{tabela(["Onde", "O que mandam"],
 [["<strong>Brasil</strong> (Embrapa, 2024)",
   "guardar a solução que sobra em recipiente plástico e <strong>reutilizar no próximo tratamento</strong>"],
  ["<strong>Índia</strong> (governo, 2006)",
   "<strong>nunca</strong> descartar em ralo, rio ou córrego; a solução usada deve ser "
   "<strong>decantada e reutilizada</strong>"]])}

<p><strong>Guardar e reusar. Nunca em ralo, rio ou córrego.</strong></p>

<h3>E a decantação — o que ela faz e o que não faz</h3>

<p><strong>Decantar</strong> é deixar a solução parada para a sujeira ir ao fundo e separar o que está limpo
em cima.</p>

<ul>
<li><strong>Resolve:</strong> tira os pedaços de bambu, a serragem, a sujeira que está suspensa. A solução
volta ao tanque mais limpa.</li>
<li><strong>Não resolve:</strong> o cobre <strong>dissolvido</strong>.</li>
</ul>

{note("A analogia que fecha", "Pense num <strong>copo de água com açúcar</strong>. Deixar parado não separa "
 "o açúcar. Com o cobre dissolvido é igual: <strong>decantar tira a sujeira, não tira o metal</strong>.")}

<p>Se algum dia for preciso tratar para descartar de verdade, a sequência é outra: <strong>transformar o
cobre dissolvido em sólido</strong> (subindo o pH), <strong>decantar</strong> esse sólido e
<strong>destinar o lodo</strong>. E o lodo é resíduo: <strong>o problema muda de forma, não desaparece</strong>.</p>

<h3>O manual indiano acerta o princípio e erra o fim</h3>

<p>O manual do governo indiano diz para não descartar em rio, córrego ou ralo, e manda decantar e reusar.
Até aí, perfeito.</p>

<p>Mas, para o que resta, ele prescreve duas coisas que <strong>não servem para o Brasil</strong>:</p>

<ul>
<li><strong>enterrar o resíduo com serragem</strong> — o que a lei brasileira não admite para resíduo com
metal;</li>
<li><strong>recuperar o lodo com ácido crômico a pH 2,5</strong> — o que é operação de fábrica química, não
de quintal.</li>
</ul>

<h3>A lacuna que sobra, e é o coração do problema</h3>

<p><strong>As duas instruções mandam reusar. Nenhuma diz o que fazer quando o reuso acaba.</strong></p>

<p>E o reuso acaba:</p>
<ul>
<li>quando a obra termina e sobrou solução;</li>
<li>quando o banho satura e perde força;</li>
<li>quando a concentração cai abaixo do que funciona.</li>
</ul>

{bq("<strong>É nesse ponto que a instrução brasileira cala e a indiana manda enterrar. É exatamente aí que o problema começa — e é aí que ninguém está olhando.</strong>")}

<h3>A lei já resolveu isso — e quase ninguém sabe</h3>

<p>A Política Nacional de Resíduos Sólidos (Lei 12.305/2010) diz o que é resíduo sólido:</p>

<blockquote>&quot;material, substância, objeto ou bem descartado […] e <strong>líquidos cujas
particularidades tornem inviável o seu lançamento na rede pública de esgotos ou em corpos d'água</strong>&quot;</blockquote>

<p><strong>A lei inclui líquidos.</strong> Água com um quarto de quilo de cobre numa banheira não pode ir para
o esgoto nem para o rio sem inviabilizar os dois. Então, por definição legal, <strong>ela é resíduo</strong>.</p>

{okbox("Não existe buraco na lei", "A obrigação existe desde 2010, e é de <strong>quem gerou o resíduo</strong> "
 "— inclusive de quem gerou na própria casa. O que a lei não diz é <strong>onde</strong> a pessoa descarta. "
 "E é aí que a instrução e a vida real se separam.")}

{SEP}

<h3>Resumo do capítulo</h3>
<p><strong>Estabelecido:</strong> 100 L a 1% contêm 254 g de cobre; 8,8 L estragam uma piscina olímpica até o
limite de rio; uma banheira precisaria de 23 piscinas para diluir; pH 1,28 na solução de cobre e boro e 0,22
no CCB; germinação zero até diluição 1/10; índice pior que o do Roundup; as duas instruções mandam reusar;
a PNRS inclui líquidos.</p>
<p><strong>Interpretação:</strong> como decantar não remove metal dissolvido, o reuso é a única saída prática
— e ele tem um fim, que nenhuma instrução resolve.</p>
<p><strong>Desconhecido:</strong> o efeito da receita real (4,5% a 9%), que é mais concentrada que a única
testada; e qual código da lista brasileira de resíduos se aplica a essa solução.</p>

{SEP}
""")


# ============================== 07 · USO DOMÉSTICO ==============================
pagina("p-8", "07 · Uso doméstico", "07", "O uso doméstico: onde este artigo vira advertência",
       "07 · USO DOMÉSTICO · GAVETA COBRE · 2026-11-24", f"""
<p>Até aqui o artigo descreveu o problema. Este capítulo mostra <strong>como ele chega à mão de uma pessoa
comum</strong> — e o que as instruções que circulam têm, e não têm, de aviso.</p>

<h3>Existem duas instruções, e elas não dizem a mesma coisa</h3>

<p>Esta foi a descoberta que mais surpreendeu a pesquisa: existem <strong>dois circuitos</strong> de
informação circulando ao mesmo tempo sobre a mesma química.</p>

<h4>O circuito oficial: avisa, protege e manda guardar</h4>

<p>A <strong>Embrapa</strong> publicou em 2024 um comunicado técnico ensinando a tratar moirão na propriedade
rural. É detalhista e é responsável. Ele dá EPI por peça — óculos, máscara, luvas de borracha, bota, avental.
Exige <strong>tonel de 200 litros</strong>. Proíbe o descarte <strong>duas vezes</strong>. E manda guardar e
reusar.</p>

<p>Além disso, ele traz um alerta que quase ninguém conhece: o <strong>dicromato e o ácido bórico estão sob
controle da Polícia Federal</strong> (Portaria 240/2019 e Lei 10.357/2001).</p>

{okbox("A instrução oficial não é irresponsável", "Ela dá EPI, proíbe descarte, manda reusar e avisa sobre "
 "controle federal de dois dos três sais. <strong>O problema deste artigo não é a instrução oficial.</strong>")}

<h4>O circuito informal: a receita completa, sem uma palavra de aviso</h4>

<p>Uma página da <strong>Universidade Federal de Minas Gerais</strong> publica a receita:</p>

<blockquote>&quot;Estas substâncias devem ser misturadas na proporção <strong>1kg:1kg:100litros</strong> […]
A imersão dos colmos deve durar de <strong>8 a 10 dias</strong>.&quot;</blockquote>

<p>E, com honestidade que merece registro, acrescenta: <em>&quot;Este tipo de tratamento não foi comprovado
em pesquisas científicas, apesar de amplamente utilizado.&quot;</em></p>

<p>Um <strong>blog de construção sustentável</strong> vai além e ensina a fórmula completa, inclusive com
<strong>dicromato de sódio</strong>:</p>

<blockquote>&quot;<strong>Fórmula (2):</strong> ácido bórico / bórax / dicromato de sódio — proporção de
<strong>2: 2: 0,5</strong>&quot; — e ensina que &quot;se você quiser aumentar, pode chegar até uma concentração
de <strong>9%</strong>, é só dobrar a mistura&quot;.</blockquote>

<p>Um <strong>site que vende construção em bambu</strong> resume, sem alarme: o produto mais utilizado é o
octoborato como inseticida, <em>&quot;e sulfato de cobre como fungicida&quot;</em>.</p>

<h3>A contagem que fecha a questão</h3>

<p>Percorri o texto desses dois últimos documentos procurando as palavras que deveriam estar ali:</p>

{tabela(["Palavra procurada", "No blog", "No site comercial"],
 [["&quot;luvas&quot;", "<strong>nenhuma vez</strong>", "<strong>nenhuma vez</strong>"],
  ["&quot;máscara&quot;", "<strong>nenhuma vez</strong>", "<strong>nenhuma vez</strong>"],
  ["&quot;EPI&quot;", "<strong>nenhuma vez</strong>", "<strong>nenhuma vez</strong>"],
  ["&quot;descarte&quot;", "<strong>nenhuma vez</strong>", "<strong>nenhuma vez</strong>"],
  ["&quot;resíduo&quot;", "<strong>nenhuma vez</strong>", "<strong>nenhuma vez</strong>"],
  ["&quot;tóxico&quot;", "—", "<strong>nenhuma vez</strong>"]])}

{danger("Zero, seis vezes", "O blog ensina a manipular <strong>um quilo de dicromato de sódio</strong> em casa "
 "e <strong>não escreve &quot;luva&quot; uma vez sequer</strong>. A única palavra &quot;CUIDADO!!&quot; que "
 "aparece no texto inteiro é sobre <strong>mancha na casca do bambu</strong>. E a receita manda comprar um "
 "produto controlado pela Polícia Federal — <strong>sem dizer isso</strong>.")}

<h3>A receita é mais forte que o único teste que existe</h3>

<p>O único estudo brasileiro que testou essa solução em bambu usou <strong>ácido bórico de 1% a 2%</strong>
e <strong>sulfato de cobre de 0,5% a 1%</strong>. A receita do blog recomenda <strong>4,5%</strong> e permite
<strong>dobrar para 9%</strong>.</p>

{bq("<strong>A receita que as pessoas usam é de 2 a 18 vezes mais forte que a única que alguém testou.</strong> O que ela faz nessa concentração, ninguém sabe.")}

{SEP}

<h3>O que uma pessoa em casa faz, e por que cada passo tem risco</h3>

<p><strong>1. Manipular o pó sem proteção.</strong> Ácido bórico, bórax e sulfato de cobre são vendidos em pó.
Abrir o saco, medir, misturar — tudo isso levanta poeira. O pó é irritante para vias respiratórias e olhos.</p>

<p><strong>2. Não usar máscara nem luva.</strong> Não é frescura: a via de entrada importa. A poeira entra
pelo pulmão; a solução entra pela pele. E a mesma solubilidade que faz o cobre penetrar no bambu faz ele
atravessar a pele.</p>

<p><strong>3. Tratar em qualquer lugar.</strong> O banho precisa de ventilação. Um quintal fechado, uma
garagem, um galpão sem janela — a poeira e o vapor ficam no ar.</p>

<p><strong>4. Descartar a água em qualquer lugar.</strong> É o que a seção anterior mediu: a água está
contaminada e não existe destino doméstico prescrito para o último lote.</p>

<p><strong>5. Guardar ou usar as aparas como se fossem limpas.</strong> Serragem e ponta de colmo que saem da
oficina <strong>não têm rótulo</strong>. E o uso doméstico típico de serragem é exatamente o que espalha:
compostagem, cama de animal, cobertura de solo, lenha.</p>

<p><strong>6. Achar que &quot;natural&quot; significa &quot;seguro&quot;.</strong> Cobre é um elemento natural.
Arsênico também. &quot;Natural&quot; descreve a origem, não o efeito biológico.</p>

<blockquote><strong>Serragem de bambu tratado com cobre é fisicamente indistinguível de serragem limpa.</strong>
Não muda de cor. Não muda de cheiro. Ninguém olhando para um monte de serragem sabe o que tem ali.</blockquote>

<h3>As regras mínimas que as fontes sustentam</h3>

<p>Isto não é receita — o acervo não produz receita, e <strong>não existe dose segura publicada para
tratamento doméstico</strong>. São as condições que as fontes custodiadas sustentam como necessárias:</p>

<ul>
<li><strong>equipamento de proteção</strong>: máscara para particulado, luvas, óculos;</li>
<li><strong>ventilação</strong>: tratar em área aberta ou ventilada, nunca em ambiente fechado;</li>
<li><strong>controle da água</strong>: não descartar o banho em solo, ralo ou curso d'água; guardar e reusar;</li>
<li><strong>identificar o resíduo</strong>: separar e rotular toda apara, serragem e colmo descartado como
<strong>contaminado com cobre</strong>, porque visualmente eles não se distinguem;</li>
<li><strong>não destinar aparas a compostagem, cama de animal, cobertura de solo ou lenha</strong>;</li>
<li><strong>manter longe de crianças e de animais</strong>.</li>
</ul>

<h3>E o que ninguém sabe ainda</h3>

<p>Sejamos rigorosos até o fim. O acervo registra estas lacunas:</p>

<ul>
<li><strong>não existe medição de exposição</strong> de quem trata bambu com cobre no Brasil — nenhuma fonte
mede o operador dessa cadeia;</li>
<li><strong>não existe dado de poeira</strong> de bambu tratado com cobre;</li>
<li><strong>não se sabe o destino real</strong> das aparas e da serragem no Brasil — se vão para aterro,
compostagem, queima ou solo;</li>
<li><strong>não se sabe o que a pessoa faz na prática</strong> com a solução que sobra. As fontes mostram o
que a instrução manda e o que as receitas ensinam. <strong>Nenhuma mostra o quintal.</strong></li>
</ul>

{danger("Dizer &quot;é desconhecido&quot; é o oposto de dizer &quot;não é problema&quot;", "Numa cadeia onde a "
 "instrução oficial manda reusar e a receita informal ensina a despejar, a ausência de medição é motivo para "
 "cuidado — não para tranquilidade.")}

{SEP}

<h3>Resumo do capítulo</h3>
<p><strong>Estabelecido:</strong> existe instrução oficial que avisa e manda reusar; existem três fontes
informais que ensinam a receita com <strong>zero</strong> menção a EPI, descarte ou resíduo; a receita é 2 a
18 vezes mais concentrada que a única testada; o dicromato é controlado pela Polícia Federal.</p>
<p><strong>Interpretação:</strong> o risco doméstico não é o cobre em si — é a distância entre a instrução
oficial e a receita que circula.</p>
<p><strong>Desconhecido:</strong> exposição do operador, poeira do bambu tratado, destino real das aparas e
prática real de descarte.</p>

{SEP}
""")


# ============================== 08 · COMO LER · RESUMO ==============================
pagina("p-9", "08 · Como ler · Resumo", "08", "Como ler qualquer texto sobre cobre — e o resumo do artigo",
       "08 · COMO LER · RESUMO · GAVETA COBRE · 2026-11-24", f"""
<p>Esta é a seção mais útil do artigo, porque ela sobrevive a mim.</p>

<h3>Cinco perguntas para julgar qualquer afirmação sobre cobre</h3>

<p>Quando você encontrar uma afirmação sobre cobre — num vídeo, numa bula, numa conversa, num texto como
este — faça cinco perguntas:</p>

<p><strong>1. &quot;Cobre&quot; de qual coisa?</strong> Cobre elementar, sulfato de cobre hidratado, anidro,
ou óxido de cobre? Sem isso o número não significa nada. Um &quot;1 quilo&quot; pode ser 1 quilo de sal
(254 g de cobre) ou 1 quilo de cobre.</p>

<p><strong>2. Qual é a base do número?</strong> Massa do sal, massa de cobre puro, ou concentração em
solução (mg/L)? São três grandezas e <strong>não se convertem livremente</strong>.</p>

<p><strong>3. Isso foi medido, ou inferido?</strong> &quot;Mediu-se germinação zero em laboratório&quot; é
diferente de &quot;mata a vida do rio&quot;. &quot;A fonte diz que o metal está no solo&quot; é diferente de
&quot;o metal veio do tratamento&quot;.</p>

<p><strong>4. Qual é o limite que o autor reconhece?</strong> Texto honesto sobre cobre sempre tem limites,
porque as fontes têm. Se não tem nenhum, desconfie.</p>

<p><strong>5. Isso é desfecho ou indicador?</strong> &quot;Índice de germinação 0&quot; é um
<strong>indicador medido em laboratório</strong>. &quot;A lavoura morreu&quot; é um <strong>desfecho no
campo</strong>. Trocar um pelo outro é o erro mais comum nesta matéria.</p>

{SEP}

<h3>Os quatro erros que este material cometeu e corrigiu</h3>

<p>Registro isso porque um texto didático que só mostra acertos é propaganda. Durante a construção deste
material, auditorias independentes encontraram erros reais:</p>

{cards([("erro 01", "Declarar ausente o que estava na fonte",
         "Afirmei que a instrução oficial da Embrapa não dizia o que fazer com a solução. Dizia — e manda "
         "guardar e reutilizar. A varredura procurou a palavra &quot;reuso&quot; e o texto usava "
         "&quot;excedente&quot;. O auditor encontrou varrendo por conceito."),
        ("erro 02", "Inventar um vazio na lei",
         "Afirmei que a legislação não previa resíduo líquido. A PNRS, de 2010, inclui líquidos na definição "
         "de resíduo sólido desde o primeiro artigo. O erro era <strong>a favor da minha própria tese</strong> "
         "— o pior tipo."),
        ("erro 03", "Transformar inferência em fato",
         "Escrevi que o sulfato de cobre não é controlado pela Polícia Federal. A fonte nomeia o cromo e o "
         "boro e <strong>não afirma</strong> que a lista seja exaustiva. Hoje isso aparece marcado como "
         "inferência."),
        ("erro 04", "Dobrar a dose por erro de unidade",
         "Publiquei um número de piscinas com a unidade errada. A conta estava certa, a grandeza não. "
         "Reconferida e corrigida com o valor exato.")])}

<p>Cada um desses foi encontrado por auditoria e corrigido. <strong>É assim que deve funcionar</strong> — e
é uma boa razão para desconfiar de qualquer texto sobre este tema que não tenha passado por verificação.</p>

{SEP}

<h3>Se você só levar isto, leve isto</h3>

<ol>
<li>O cobre é o elemento de <strong>29 prótons</strong>, um metal comum — não é raro nem escasso.</li>
<li>O que se compra é o <strong>sulfato de cobre</strong>, e só <strong>25,45%</strong> dele é cobre. Um quilo
do pó azul carrega 254 gramas de metal.</li>
<li>O sulfato <strong>anidro</strong> tem 39,81% de cobre — a mesma massa, mais metal.</li>
<li>O Brasil <strong>importa</strong> o que consome: 177,9 t em 2025, com 80,4% do peso vindo da China.</li>
<li>O preço é baixo e o volume é pequeno: <strong>não há pressão econômica</strong> para descartar errado.</li>
<li>O cobre é <strong>fungicida</strong> e <strong>não</strong> é inseticida. Quem mata inseto é o boro.</li>
<li>No CCB, só <strong>26%</strong> é sulfato de cobre; <strong>63,5%</strong> é dicromato — e é o
<strong>cromo</strong> que aparece no solo.</li>
<li>O cobre é <strong>nutriente essencial</strong> (~1 mg/dia) — e isso <strong>não</strong> significa que
seja inofensivo.</li>
<li>Os <strong>2 mg/L</strong> da água de beber são um valor <strong>provisório</strong>, e o efeito crônico
do cobre é <strong>hepático</strong>.</li>
<li>A razão que resume tudo: <strong>1.800×</strong>. O cobre é potável numa concentração mil e oitocentas
vezes maior do que a que prejudica a vida do rio.</li>
<li>O bambu é rico em amido e pobre em lignina — é <strong>comida fácil</strong> para fungo e inseto.</li>
<li>O cobre funciona porque é <strong>solúvel</strong> — e a mesma solubilidade que o faz entrar é a que o faz
<strong>sair</strong> sob umidade.</li>
<li>Esse processo de saída chama-se <strong>lixiviação</strong>.</li>
<li>A retenção medida em uma espécie de bambu ficou em <strong>22–23% do alvo</strong>: a dose preparada não
descreve a dose retida.</li>
<li><strong>O dado contra a tese:</strong> após cinco anos em campo, o cobre <strong>não</strong> elevou o solo
de forma significativa (+12%, sem significância) — o cromo subiu <strong>86%</strong>.</li>
<li>Uma receita doméstica é <strong>meia banheira</strong> de solução com <strong>254 gramas de cobre</strong>.</li>
<li><strong>8,8 litros</strong> dessa solução deixam uma <strong>piscina olímpica</strong> acima do limite de
rio protegido.</li>
<li>Para diluir <strong>uma banheira</strong> até virar água aceitável, seriam <strong>23 piscinas
olímpicas</strong>. Diluir <strong>não</strong> é destinar: cobre não se degrada.</li>
<li>A solução de cobre e boro tem <strong>pH 1,28</strong> — mais ácida que suco de limão. O CCB tem
<strong>0,22</strong>.</li>
<li>No teste com sementes de alface, a solução <strong>diluída dez vezes</strong> ainda impediu
<strong>toda</strong> germinação, com índice <strong>pior que o do Roundup</strong>.</li>
<li><strong>As duas instruções oficiais mandam reusar</strong> e proíbem o descarte em ralo, rio ou córrego.</li>
<li><strong>Decantar não remove cobre dissolvido</strong> — tira a sujeira, não o metal.</li>
<li><strong>A lacuna:</strong> nenhuma instrução diz o que fazer quando o reuso acaba.</li>
<li>Pela lei brasileira (PNRS, art. 3º, XVI), essa água <strong>é resíduo</strong> desde 2010 — a lei inclui
líquidos.</li>
<li>A instrução oficial <strong>avisa</strong> (EPI, tonel, proibição, reuso). A receita informal
<strong>não</strong>: zero menção a EPI, descarte ou resíduo em 19 mil caracteres.</li>
<li>A receita informal recomenda <strong>dicromato</strong>, que é controlado pela Polícia Federal, e ensina a
<strong>dobrar</strong> a concentração.</li>
<li>A receita que circula é <strong>2 a 18 vezes</strong> mais concentrada que a única testada.</li>
<li><strong>Serragem tratada é indistinguível de serragem limpa</strong> — e o uso doméstico típico a espalha
no ambiente.</li>
<li><strong>Não existe medição</strong> de exposição de quem trata bambu com cobre, nem de poeira do material
tratado, nem do destino real das aparas.</li>
<li><strong>&quot;Natural&quot; não significa seguro</strong>; &quot;não é cancerígeno&quot; não significa
seguro.</li>
</ol>

{SEP}
""")


# ============================== 09 · GLOSSÁRIO ==============================
_GLOSS = [
 ("Ácido bórico", "composto de boro, hidrogênio e oxigênio. Contém <strong>17,5%</strong> de boro. É o "
  "terceiro ingrediente do CCB, ao lado do sulfato de cobre e do dicromato."),
 ("Anidro", "&quot;sem água&quot;. Sais que normalmente carregam água dentro do cristal, quando seca, ficam "
  "mais concentrados: o sulfato de cobre anidro tem <strong>39,81%</strong> de cobre, contra 25,45% do "
  "hidratado."),
 ("Átomo", "a menor peça de um elemento. O tipo de átomo é definido pelo número de prótons no núcleo."),
 ("Boro", "elemento de 5 prótons. No tratamento de bambu, é o que mata inseto (cupim, broca, besouro). "
  "O cobre não faz isso."),
 ("Calda bordalesa", "mistura de sulfato de cobre com cal, usada como fungicida na agricultura há mais de "
  "um século."),
 ("CCB", "borato de cobre cromatado. Preservativo de três sais — boro, cobre e cromo — em que o cromo serve "
  "para fixar os outros dois no material."),
 ("CCA", "arseniato de cobre cromatado. Preservativo parecido com o CCB, mas com <strong>arsênico</strong> no "
  "lugar do boro. Restrito em vários países."),
 ("Composto", "substância formada por dois ou mais elementos ligados. Sais e ácidos são compostos."),
 ("Concentração", "quanto de uma substância existe num volume de líquido. <strong>mg/L</strong> significa "
  "miligrama por litro; <strong>µg/L</strong>, micrograma por litro (mil vezes menos)."),
 ("Cromo", "elemento usado no CCB para <strong>fixar</strong> o cobre e o boro no bambu. Foi o elemento que "
  "de fato subiu no solo no ensaio de campo de cinco anos."),
 ("Cobre", "elemento de <strong>29 prótons</strong>, metal, essencial ao corpo humano em dose muito pequena "
  "(~1 mg/dia)."),
 ("CuSO₄·5H₂O", "fórmula do sulfato de cobre hidratado — o pó azul. A parte depois do ponto é a água que "
  "fica dentro do cristal."),
 ("Decantação", "deixar a solução parada para a sujeira ir ao fundo e separar o líquido limpo de cima. "
  "<strong>Não remove o que está dissolvido.</strong>"),
 ("Dicromato", "sal de cromo usado no CCB. No Brasil, o dicromato de potássio e de sódio estão sob "
  "<strong>controle da Polícia Federal</strong> (Portaria 240/2019)."),
 ("Efluente", "o líquido que sai de um processo e precisa de destinação. A água do banho de tratamento é um "
  "efluente."),
 ("Elemento químico", "uma das 118 &quot;peças básicas&quot; da matéria. O cobre é a de número 29."),
 ("Fitotoxicidade", "capacidade de prejudicar plantas. É o que o teste com sementes de alface mede."),
 ("Fungicida", "que mata fungo. É a função do cobre."),
 ("Fungistático", "que impede o fungo de crescer, sem necessariamente matá-lo."),
 ("Germinação (índice de)", "quantas sementes nascem, numa escala de 0 a 100, comparadas a um controle. "
  "No estudo citado, <strong>abaixo de 30</strong> já é considerado muito tóxico."),
 ("Hidratação (água de)", "água encaixada dentro da estrutura do cristal, não apenas molhando por fora."),
 ("Inseticida", "que mata inseto. <strong>O cobre não é inseticida.</strong>"),
 ("Lignina", "substância natural da madeira que age como resina, impermeabilizando e protegendo. O bambu tem "
  "muito menos que a madeira — e é por isso que apodrece mais fácil."),
 ("Lixiviação", "processo em que a água entra no material, dissolve o que está dentro e sai carregando "
  "embora. É o problema central do bambu tratado com sais solúveis."),
 ("Massa atômica", "o &quot;peso&quot; de um átomo. Carbono 12, oxigênio 16, <strong>cobre 63,546</strong>."),
 ("Miligrama e micrograma", "um miligrama (mg) é um milésimo de grama — mais ou menos o peso de um grão de "
  "sal. Um micrograma (µg) é um milésimo do miligrama."),
 ("Minério", "rocha com concentração suficiente de um elemento para valer a pena extrair."),
 ("NCM", "código alfandegário que classifica a mercadoria no comércio exterior. O sulfato de cobre é "
  "<strong>2833.25</strong>."),
 ("pH", "escala de acidez: 7 é neutro, abaixo de 7 é ácido. Suco de limão fica por volta de 2; a solução de "
  "cobre e boro, em 1,28."),
 ("PNRS", "Política Nacional de Resíduos Sólidos (Lei 12.305/2010). Define como resíduo sólido também os "
  "<strong>líquidos</strong> que não podem ir para a rede de esgoto nem para corpo d'água."),
 ("Precipitação", "transformar o que está dissolvido em sólido, geralmente subindo o pH, para depois separar "
  "por decantação."),
 ("Preservante", "produto aplicado ao material para impedir que fungos e insetos o destruam."),
 ("Próton", "partícula de carga positiva no núcleo do átomo. O número de prótons é a identidade do elemento."),
 ("Resíduo sólido", "pela lei brasileira, inclui líquidos cuja destinação em rede de esgoto ou corpo d'água "
  "seja inviável. A solução de tratamento se enquadra."),
 ("Solubilidade", "capacidade de uma substância se dissolver em água. É a propriedade que permite o cobre "
  "entrar no bambu — e sair dele."),
 ("Toxicidade crônica", "efeito que aparece por exposição repetida ao longo do tempo, não de uma vez."),
 ("Toxicidade hepática", "dano ao fígado. É o efeito crônico do excesso de cobre."),
]

_itens = "".join(f"<p><strong>{t}</strong> — {d}</p>" for t, d in _GLOSS)

pagina("p-10", "Glossário", "09", "Glossário — para voltar quando esquecer um termo",
       f"GLOSSÁRIO · {len(_GLOSS)} TERMOS · GAVETA COBRE · 2026-11-24", f"""
<p>Termos em ordem alfabética. Todos aparecem explicados no corpo do texto; este é o lugar de consulta.</p>

{_itens}

{SEP}
""")


# ============================== 10 · PROVENIÊNCIA ==============================
pagina("p-11", "Proveniência", "10", "Para saber mais, e como este texto foi feito",
       "PROVENIÊNCIA · GAVETA COBRE · 2026-11-24", f"""
<p>Este artigo não inventa dados. Ele reorganiza, em linguagem simples, o conteúdo de uma frente de pesquisa
do <strong>Acervo Soberania Tecnológica</strong> dedicada ao cobre, que custodia as fontes com verificação de
integridade por assinatura digital.</p>

<h3>As fontes que sustentam cada número</h3>

{tabela(["O que você quer conferir", "De onde vem"],
 [["O que a instrução oficial manda (EPI, tonel, reuso, controle federal)",
   "Embrapa, Comunicado Técnico 110 — Tonini &amp; Oliveira, 2024"],
  ["A receita da universidade e o aviso de que não foi comprovada",
   "página do MOM/FAU — Universidade Federal de Minas Gerais"],
  ["A fórmula com dicromato e a instrução de dobrar a concentração",
   "blog &quot;Materiais e técnicas para construção sustentável&quot;, 2016"],
  ["&quot;Sulfato de cobre como fungicida&quot; no padrão de mercado",
   "espaconaturalmente.eco.br"],
  ["O teste da alface, o pH e as raízes",
   "Scharfenberg 2020 — dissertação de mestrado, UFTM, 101 páginas"],
  ["O cobre que não subiu no solo e o cromo que subiu 86%",
   "Rusch et al. 2023 — Pesquisa Florestal Brasileira"],
  ["&quot;Decantar e reusar&quot; e &quot;não descartar em ralo, rio ou córrego&quot;",
   "NMBA 2006 — manual do governo da Índia, páginas 46–47"],
  ["Os limites de cobre na água", "CONAMA 430/2011 e CONAMA 357/2005"],
  ["Os 2 mg/L da água de beber e a ressalva de provisório", "OMS, <em>Copper in Drinking-Water</em>, 2004"],
  ["A definição legal que inclui líquidos", "Lei 12.305/2010, art. 3º, XVI"],
  ["A composição do CCB (26% de sulfato de cobre)", "NBR 6232, conforme descrita em Rusch et al. 2023"],
  ["A importação brasileira e os preços", "ComexStat, NCM 2833.25, série 1997–2026"],
  ["&quot;Good fungicide&quot; e &quot;ineffective for termites&quot;", "Gauss 2020, Tabela 2.5"]])}

<h3>Como o material foi verificado</h3>

<p>A rodada de uso doméstico passou por <strong>cinco auditorias independentes</strong>, com veredito
registrado uma a uma. Três reprovaram, e cada reprovação produziu correção material — inclusive a correção
do erro que <strong>favorecia a tese do próprio material</strong>. As correções estão registradas no acervo,
não apagadas.</p>

{okbox("O que a auditoria confirmou", "Integridade das fontes conferida por assinatura digital; "
 "<strong>todas</strong> as citações literais verificadas palavra por palavra contra o documento original; "
 "e as declarações de &quot;não sei&quot; mantidas como declarações, sem virar afirmação no meio do texto.")}

<h3>Estado deste documento</h3>

<p><strong>Em revisão documental, aguardando homologação humana.</strong> Nenhuma afirmação aqui foi
homologada por pessoa humana, e a homologação automática está desativada — homologar é ato humano.</p>

<p><strong>Sobre a linguagem:</strong> este texto foi escrito para ser entendido sem formação em química ou em
metodologia científica. Se algum trecho falhou nisso, é falha do texto, não do leitor.</p>

<h3>Autoria, assistência e responsabilidade</h3>

<p><strong>Autor:</strong> Fabio Takwara.</p>

<p><strong>Apoio de IA:</strong> ferramenta de inteligência artificial foi utilizada para localizar relações
entre fontes, estruturar o comparativo, conferir consistência interna, apoiar a redação e executar os cálculos
de diluição. <strong>A seleção interpretativa, a perspectiva e a responsabilidade pela versão publicada
permanecem com o autor.</strong></p>

<p><strong>Natureza:</strong> artigo de divulgação — adaptação pública em linguagem não especializada.</p>

<p><strong>Conflitos de interesse:</strong> declarados inexistentes.</p>
""")

# alias público para o gerador
GLOSSARIO = _GLOSS
