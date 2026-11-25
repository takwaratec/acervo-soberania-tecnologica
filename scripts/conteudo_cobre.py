# -*- coding: utf-8 -*-
"""Conteúdo da peça do cobre, no molde homologado (peça de boro, 2026-11-24).

Cada seção vira <section role="tabpanel" id="p-N" class="active?"> com <h2><span class="num">.
Todo <td> recebe data-l = cabeçalho da coluna, para a tabela virar cartão no celular.
"""

import re, html as _h

def _txt(s):
    """texto puro do cabeçalho, para data-l"""
    return re.sub(r"<[^>]+>", "", s).strip()

def cit(*chaves):
    """Citação numerada clicável: cit("scharfenberg2020") -> [3] ligado a #ref-3."""
    from referencias_cobre import NUMERO
    return "".join(f'<a class="cite" href="#ref-{NUMERO[k]}">[{NUMERO[k]}]</a>'
                   for k in sorted(chaves, key=lambda x: NUMERO[x]))


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

Ele existe para responder **uma pergunta só** — e é uma pergunta que os textos informais que esta
frente leu não fazem:

{bq("<strong>Depois que o bambu sai do tanque de tratamento, o que acontece com a água que sobra?</strong>")}

<p>Ela não é água. É uma solução de metal em concentração alta. E as receitas informais que esta
frente leu <strong>não dizem onde despejar</strong> — nas que eu li, nenhuma diz.</p>

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

<p>Aqui está o erro que <strong>muda a dose por um fator de quase quatro</strong> — e que aparece nas
receitas informais que esta frente leu. Não medi frequência em texto nenhum; digo onde eu vi.</p>

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
de cobre: contém <strong>254 gramas</strong> de cobre e 746 gramas de outras coisas. {cit("rusch2023")}</p>

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
sob um código chamado <strong>NCM 2833.25</strong>{cit("comexstat")} — um número que funciona como &quot;código de barras
alfandegário&quot; da substância. Em 2025:</p>

{kpis([("177,9 t", "importadas no ano"),
       ("US$ 370 mil", "total pago"),
       ("US$ 2,08", "preço médio por quilo"),
       ("80,4%", "do peso vem da China")])}

{tabela(["Origem", "Fatia do peso", "Fatia do valor", "Preço por quilo"],
 [["<strong>China</strong>", "<strong>80,4%</strong>", "<strong>48,3%</strong>", "US$ 1,25"],
  ["Estados Unidos", "—", "—", "US$ 45,57"],
  ["Reino Unido", "—", "—", "US$ 148,43"]])}

{danger("O erro que aparece nos textos informais que li aqui", "Misturar <strong>peso</strong> com <strong>valor</strong>. "
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
e o preço é baixo. <strong>O preço do produto é baixo</strong> — é o que o dado mostra: volume,
valor e dispersão de preço por código. O que ele <strong>não</strong> mede é conduta: se preço baixo
inibe ou não o descarte correto, este número não responde, porque ele conta importação e valor, não
o que o usuário faz com a sobra. Também não mede o custo de dar destino ao resíduo.</p>

<p><strong>A conclusão que o dado NÃO sustenta:</strong> dizer que o Brasil &quot;usa muito&quot; ou
&quot;usa pouco&quot; sulfato de cobre em bambu. A importação é do país inteiro, somando agricultura,
indústria, laboratório e tratamento de madeira. <strong>Quanto disso vai para bambu, ninguém mediu.</strong></p>

{SEP}

<h3>Resumo do capítulo</h3>
<p><strong>Estabelecido:</strong> 177,9 t e US$ 370 mil em 2025; China com 80,4% do peso e 48,3% do valor;
dispersão de preço de 119× dentro do mesmo código; queda de 86% entre 1997 e 2020; preço médio baixo.</p>
<p><strong>Interpretação:</strong> a dispersão de preço sugere graus de pureza diferentes sob o mesmo código.
O preço baixo do produto diz que comprar não desestimula; sobre o custo de <em>destinar</em> o resíduo,
estes dados não falam — e é por isso que eles não provam que dinheiro não seja barreira.</p>
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

<p>Aqui está a informação que não aparece nos textos informais que esta frente leu:</p>

<p><strong>O cobre não mata cupim, não mata broca, não mata besouro.</strong>{cit("gauss2020")} Ele é fungicida, não é
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
pela norma brasileira (NBR 6232){cit("nbr6232")} e usada no ensaio de Rusch (2023){cit("rusch2023")}, o CCB é composto de
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
 [["<strong>Água de beber</strong> (OMS)" + cit("oms2004"), "<strong>2 mg/L</strong>",
   "proteger a população inteira, todos os dias, pela vida toda"],
  ["<strong>Efluente</strong> (CONAMA 430/2011)" + cit("conama430"), "<strong>1,0 mg/L</strong>",
   "o que uma atividade pode lançar na rede ou no corpo receptor"],
  ["<strong>Água doce Classe 1</strong> (CONAMA 357/2005)" + cit("conama357"), "<strong>0,009 mg/L</strong>",
   "o rio protegido — a água onde se espera vida aquática"],
  ["<strong>Invertebrado aquático, crônico</strong>", "<strong>0,00111 mg/L</strong>",
   "o nível em que a vida do rio começa a sofrer"]])}

<p><strong>Um número mais baixo não é &quot;mais rigoroso&quot;</strong> — é um número que protege outro
objeto. Quem compara 2 mg/L com 0,009 mg/L e conclui que &quot;um dos dois está errado&quot; não entendeu
que os dois estão certos e falam de coisas diferentes.</p>

<h3>O detalhe que quase ninguém sabe sobre os 2 mg/L</h3>

<p>Os <strong>2 mg/L</strong> da água de beber são o número mais citado de todos. E ele é
<strong>provisório</strong>{cit("oms2004")} — a própria Organização Mundial da Saúde diz que o valor é provisório
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


<h3>E o cobre é cancerígeno?</h3>

<p>Esta é a pergunta em que os textos informais que eu li erram — para os dois lados. E aqui é preciso fazer o que
o resto do artigo faz: separar o que está medido do que não está.</p>

{danger("Limite declarado, antes de qualquer conclusão", "A <strong>monografia da IARC</strong> para "
        "o cobre e a <strong>ficha toxicológica da ATSDR</strong> para o cobre <strong>não estão no "
        "corpus desta frente</strong>. Portanto este artigo <strong>não afirma</strong> que o cobre "
        "seja cancerígeno, nem que não seja. Dizer qualquer das duas coisas sem a monografia em mãos "
        "seria inventar — e é justamente o que este artigo critica nos outros.")}

<p><strong>O que o corpus sustenta sobre o desfecho do cobre:</strong> o documento de base da
Organização Mundial da Saúde trata o cobre pelo efeito <strong>agudo gastrointestinal</strong>
(náusea a partir de 4 mg/L, em estudo com 61 voluntários) e pelo <strong>acúmulo hepático</strong> na
exposição prolongada — &quot;o cobre se acumula no fígado, no cérebro e nos olhos&quot;.{cit("oms2004")}
Câncer não é o desfecho que esses documentos usam para fixar limite. Isso <strong>não</strong>
significa que o cobre seja inofensivo: significa que o desfecho documentado é outro.</p>

<p><strong>Agora a informação recente que não pode ser ignorada.</strong> Em 2025, quatro
pesquisadores publicaram, com revisão por pares, uma avaliação de ciclo de vida da produção artesanal
de colmo de bambu no Acre.{cit("araujo2025")} Concluíram que a <strong>toxicidade carcinogênica
humana (HCT) representou 93% do impacto potencial</strong> daquela cadeia.</p>

<p><strong>Isso não é boato e não deve ser tratado como boato.</strong> É publicação recente, com
método declarado, inventário e tabela.</p>

<p><strong>E também não é sentença.</strong> &quot;HCT&quot; é o nome de uma <strong>categoria do
método ReCiPe</strong> — não um diagnóstico. O valor sai em milipontos, depois de normalizado entre
as sete categorias que os autores selecionaram. <strong>&quot;93%&quot; quer dizer &quot;esta foi a
categoria que mais pesou no modelo&quot;</strong>, não &quot;93% de chance de câncer&quot;.</p>

<p><strong>Por que, então, o termo importa para esta gaveta?</strong> Porque o estudo mediu uma
cadeia tratada com <strong>bórax e ácido bórico</strong> — e as receitas brasileiras de cobre são
ternárias, ou seja, <strong>levam bórax junto</strong>. A carga de resíduo que carrega o boro carrega
o cobre no mesmo saco. A categoria que mais pesou naquela cadeia é a mesma que este artigo está
discutindo.</p>

<p><strong>A leitura honesta, então, é esta:</strong></p>

<ul>
<li>o desfecho <strong>documentado</strong> do cobre é gastrointestinal e hepático;{cit("oms2004")}</li>
<li>a classificação de <strong>carcinogenicidade</strong> do cobre <strong>não foi verificada</strong>
nesta frente — e o artigo diz isso;</li>
<li>o estudo brasileiro de 2025 mede <strong>impacto potencial de cadeia</strong>, e o maior
contribuinte é o <strong>resíduo</strong>, não a aplicação;{cit("araujo2025")}</li>
<li>e <strong>&quot;93%&quot; não é probabilidade de câncer</strong> — é o peso de uma categoria
num modelo.</li>
</ul>

<p>Quem disser que o cobre do tratamento causa câncer está extrapolando. Quem disser que é inofensivo
porque &quot;não é cancerígeno&quot; está extrapolando igual — e ignora os dois desfechos que
<em>estão</em> documentados.</p>

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

{danger("E aqui está o ponto em que os textos informais que li erram", "<strong>Diluir não resolve nada.</strong> "
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

<p>O autor{cit("scharfenberg2020")} comparou com um herbicida comercial — o <strong>Roundup</strong>, aquele que mata planta daninha
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
 [["<strong>Brasil</strong> (Embrapa, 2024)" + cit("tonini2024"),
   "guardar a solução que sobra em recipiente plástico e <strong>reutilizar no próximo tratamento</strong>"],
  ["<strong>Índia</strong> (governo, 2006)" + cit("nmba2006"),
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

<p><strong>As duas instruções mandam reusar. Nenhuma diz o que fazer quando o reuso acaba.</strong>
E isso não é descuido delas: elas ensinam o <em>banho</em>, não o descarte. Quem diz o descarte é
outra peça do sistema — a <strong>bula do produto registrado</strong>, por exigência do item VIII da
IN Ibama 5/92, de 1992. O problema é que a instrução que ensina o banho caseiro não vem com bula —
não nas fontes que eu li — e a norma que exigiria a bula é a mesma que dispensa de registro o produto
de uso domissanitário.</p>

<p>E o reuso acaba:</p>
<ul>
<li>quando a obra termina e sobrou solução;</li>
<li>quando o banho satura e perde força;</li>
<li>quando a concentração cai abaixo do que funciona.</li>
</ul>

{bq("<strong>É nesse ponto que a instrução de tratamento cala — e onde o sistema brasileiro delega o descarte à bula de um produto registrado. Quem trata em casa não tem produto registrado — e, nos sete documentos que eu li, não há bula para produto dispensado de registro. Se existe, eu não a encontrei.</strong>")}

<h3>A lei já resolveu isso — e quase ninguém sabe</h3>

<p>A Política Nacional de Resíduos Sólidos (Lei 12.305/2010){cit("pnrs2010")} diz o que é resíduo sólido:</p>

<blockquote>&quot;material, substância, objeto ou bem descartado […] e <strong>líquidos cujas
particularidades tornem inviável o seu lançamento na rede pública de esgotos ou em corpos d'água</strong>&quot;</blockquote>

<p><strong>A lei inclui líquidos — sob condição.</strong> O texto diz "cujas particularidades tornem
inviável o seu lançamento na rede pública de esgotos ou em corpos d'água". Se a água com um quarto de
quilo de cobre numa banheira satisfaz essa condição é <strong>questão jurídica, e este artigo não a
decide</strong>. O que está medido é o número: como sai do tonel, ela não pode ser lançada (seção 8).
Chamem de resíduo ou não — o ralo continua fechado.</p>

{okbox("O ralo não aceita, com ou sem nome", "Se o que sobra do banho é resíduo — e a lei admite essa "
 "leitura, sob a condição acima —, a obrigação é de <strong>quem gerou</strong>, inclusive na própria "
 "casa. O que <strong>não</strong> depende da classificação é o limite de lançamento: 1,0 mg de cobre "
 "por litro. A instrução e a vida real se separam aí.")}

{SEP}

<h3>Resumo do capítulo</h3>
<p><strong>Estabelecido:</strong> 100 L a 1% contêm 254 g de cobre; 8,8 L estragam uma piscina olímpica até o
limite de rio; uma banheira precisaria de 23 piscinas para diluir; pH 1,28 na solução de cobre e boro e 0,22
no CCB; germinação zero até diluição 1/10; índice pior que o do Roundup; as duas instruções mandam reusar;
a PNRS inclui resíduo líquido sob condição, e o banho está 2.545 vezes acima do padrão de cobre.</p>
<p><strong>Interpretação:</strong> como decantar não remove metal dissolvido, o reuso é a saída que
as duas instruções dão — e ele tem um fim, que nenhuma delas resolve. Se existe outra saída prática,
estas fontes não a discutem.</p>
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
controle da Polícia Federal</strong> (Portaria 240/2019 e Lei 10.357/2001){cit("tonini2024")}.</p>

{okbox("A instrução oficial não é irresponsável", "Ela dá EPI, proíbe descarte, manda reusar e avisa sobre "
 "controle federal de dois dos três sais. <strong>O problema deste artigo não é a instrução oficial.</strong>")}

<h4>O circuito informal: a receita completa, sem uma palavra de aviso</h4>

<p>Uma página da <strong>Universidade Federal de Minas Gerais</strong> publica a receita:</p>

<blockquote>&quot;Estas substâncias devem ser misturadas na proporção <strong>1kg:1kg:100litros</strong> […]
A imersão dos colmos deve durar de <strong>8 a 10 dias</strong>.&quot;{cit("ufmg_mom")}</blockquote>

<p>E, com honestidade que merece registro, acrescenta: <em>&quot;Este tipo de tratamento não foi comprovado
em pesquisas científicas, apesar de amplamente utilizado.&quot;</em></p>

<p>Um <strong>blog de construção sustentável</strong> vai além e ensina a fórmula completa, inclusive com
<strong>dicromato de sódio</strong>:</p>

<blockquote>&quot;<strong>Fórmula (2):</strong> ácido bórico / bórax / dicromato de sódio — proporção de
<strong>2: 2: 0,5</strong>&quot; — e ensina que &quot;se você quiser aumentar, pode chegar até uma concentração
de <strong>9%</strong>, é só dobrar a mistura&quot;.{cit("blogtcs2016")}</blockquote>

<p>Um <strong>site que vende construção em bambu</strong> resume, sem alarme: o produto mais utilizado é o
octoborato como inseticida, <em>&quot;e sulfato de cobre como fungicida&quot;</em>.{cit("espaconaturalmente")}</p>

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
pagina("p-limbo", "08 · O limbo legal", "08", "O limbo: duas políticas, nenhuma norma",
       "O LIMBO LEGAL · GAVETA COBRE · 2026-11-24", f"""
<p>Esta é a parte mais desconfortável do artigo, e a única em que a conclusão não vem de uma fonte
científica — vem da <strong>ausência de fonte normativa</strong>. Trate como pergunta aberta, não
como acusação provada.</p>

<h3>Primeiro, o fato que precisa ser dito sem rodeio</h3>

<p>No Brasil, <strong>o tratamento de bambu é artesanal</strong>. Não há, nas fontes examinadas,
registro de cadeia industrial com tratamento de efluente. Quando este artigo comparou o Acre ao
Sudeste e ao Sul, fez uma concessão que não se sustenta: <strong>não há prova de que exista, aqui,
a escala industrial que se imagina</strong>.</p>

<p>E isso muda o argumento. Se tudo é artesanal, o estudo do Acre{cit("araujo2025")} não é um caso
periférico — é, nas fontes que existem, <strong>a única coisa documentada</strong>. A ressalva é dura e
não é retórica: uma unidade, um município, um ano. Não faço dele a regra; faço dele o que ele é.</p>

<p>O que esse estudo mediu, em linguagem direta: numa oficina de Rio Branco que trata colmo com
bórax e ácido bórico, a categoria de impacto que mais pesou foi a de <strong>toxicidade
carcinogênica humana — 93% do total normalizado</strong> — e <strong>91% dessa carga veio dos
resíduos</strong>: a apara, o corte, o colmo descartado e o efluente. Não é a operação que pesa.
É o que sobra dela.</p>

{note("Por que isso entra num artigo sobre cobre", "Porque, nas receitas informais que esta frente "
      "leu, nenhuma é só sulfato de cobre. A ternária — ácido bórico, "
      "bórax e dicromato de sódio — e a receita de bórax usada em universidade pública é bórax e "
      "ácido bórico puros. Ou seja: <strong>na apara que sobra do tratamento com cobre, o bórax "
      "está junto</strong> — mas <strong>não em toda</strong>: o manual indiano e a instrução da Embrapa "
      "propõem banhos <em>separados</em>, e o estudo do Acre mediu um banho só de bórax com ácido bórico. "
      "O que sustenta a ligação é o <strong>local do dano</strong>, não a mistura: nos estudos desta "
      "gaveta que eu li, onde discordam do tratamento, concordam em apontar <strong>o resíduo e a água "
      "que sobra</strong> como o problema — sem que eu tenha contado quantos são.")}

<h3>Duas leis, duas datas, e o mesmo vazio</h3>

<p><strong>Lei 12.305/2010 — Política Nacional de Resíduos Sólidos.</strong>{cit("pnrs2010")} É a
lei-quadro, e a definição dela é ampla de propósito:</p>

{bq("resíduos sólidos: material, substância, objeto ou bem descartado resultante de atividades "
   "humanas em sociedade, nos estados sólido ou semissólido, bem como gases contidos em "
   "recipientes e <strong>líquidos cujas particularidades tornem inviável o seu lançamento na rede "
   "pública de esgotos ou em corpos d'água</strong>")}

<p><strong>O banho, como sai do tonel, não pode ser descartado direto.</strong> Uma solução a 1% —
1 kg de sulfato em 100 L de água — carrega cerca de <strong>2.545 mg de cobre por litro</strong>; o padrão de lançamento de efluente com cobre é
<strong>1,0 mg/L</strong>, pela CONAMA 430/2011.{cit("conama430")} São <strong>2.545 vezes</strong>
acima do padrão.</p>

<p>Isso <strong>não decide o nome jurídico</strong> do banho. Se ele é "resíduo sólido" pela definição
do art. 3º, XVI depende de a lei considerar inviável o lançamento, e essa é uma questão que este artigo
<strong>não resolve</strong>: exigiria caracterizar o banho e avaliar se existe tratamento viável, e
nada disso foi medido aqui.</p>

<p>O que o número estabelece é estreito, e é o bastante para o quintal: o lançamento
<strong>direto em corpo receptor</strong> só é admitido em conformidade com as condições e padrões da
CONAMA 430, e o padrão de cobre dissolvido ali é 1,0 mg/L.{cit("conama430")} O banho como sai do
tonel está 2.545 vezes acima — logo, direto no rio e como está, ele não passa nesse padrão. Isso
<strong>não</strong> decide a regra da rede pública de esgoto, que segue normas próprias e a diretriz
da operadora, nem se existe tratamento viável para este banho. Duas coisas que eu não medi. E não
atribuo à resolução uma exigência geral de "tratamento prévio": ela exige conformidade, e o modo de
chegar lá não é dela.</p>

<p><strong>Mas procure &quot;bambu&quot; na PNRS: zero ocorrências. &quot;Madeira&quot;: zero.</strong>
A lei que rege resíduo no Brasil <strong>não nomeia o material</strong>.</p>

<p><strong>Lei 12.484/2011 — Política Nacional de Incentivo ao Manejo Sustentado e ao Cultivo do
Bambu.</strong>{cit("pnmcb2011")} Ela dá <strong>crédito rural</strong>, <strong>assistência
técnica</strong>, <strong>certificação de origem</strong>, e estimula expressamente o <strong>uso
comunitário e cooperativo</strong>.</p>

<p><strong>Procure &quot;tratamento&quot;: zero. &quot;Químico&quot;: zero. &quot;Resíduo&quot;:
zero. &quot;Licença&quot;: zero. &quot;Fiscalização&quot;: zero.</strong> A política do bambu
<strong>incentiva a produção e não disciplina o que acontece com o que sobra</strong>.</p>

<h3>Quem fiscaliza? A pergunta sem dono</h3>

<p>A PNRS distribui competência por <strong>sistemas</strong>, não por material: <strong>Sisnama</strong>
(meio ambiente), <strong>SNVS</strong> (vigilância sanitária), <strong>Suasa</strong> (sanidade
agropecuária) e <strong>Sinmetro</strong> (metrologia).{cit("pnrs2010")} Nenhum dos que consegui
ler trata de bambu tratado.</p>

<p><strong>Na prática:</strong> quem trata bambu com sulfato de cobre na própria casa, no quintal ou
na cooperativa <strong>não está descumprindo uma norma específica</strong> — eu não localizei nenhuma
que trate do assunto. E também <strong>não está cumprindo</strong>: não há licença, não há plano de
gerenciamento, não há destinação prescrita em nada que eu tenha encontrado. "Não localizei" é
declaração sobre a minha busca, não sobre a existência.</p>

<p><strong>E há um problema de fronteira que ninguém resolveu:</strong></p>

<ul>
<li>o <strong>MAPA</strong> responde por insumo agrícola — e o sulfato de cobre é registrado como
fungicida agrícola, não como preservativo de bambu;</li>
<li>a <strong>ANVISA</strong> responde pelo produto saneante e pela água de consumo — não pelo
resíduo do processo;</li>
<li>o <strong>ICMBio</strong> responde por unidade de conservação — é o órgão a quem a competência
foi atribuída. Se isso é onde está o risco real, eu não medi: não tenho dado de exposição nem de
probabilidade dentro dessas áreas;</li>
<li>o <strong>município</strong> responde pelo resíduo domiciliar,{cit("pnrs2010")} mas não tem
como caracterizar apara de bambu tratado como perigosa sem a classificação da ABNT.</li>
</ul>

{danger("O que este artigo NÃO conseguiu verificar", "A classificação do resíduo de bambu tratado "
        "depende da <strong>ABNT NBR 10004</strong>, que é paga e <strong>não foi consultada por "
        "esta frente</strong>. Não se afirma aqui que a apara seja Classe I nem Classe II. Afirmar "
        "qualquer das duas sem o texto da norma seria inventar. É limite declarado, não omissão.")}

<h3>O que essa combinação produz</h3>

<p>Sem norma que nomeie o material e sem classificação consultada, <strong>a apara de bambu tratado
não tem rota escrita</strong>. O que acontece na prática eu não medi. As fontes descrevem três
desfechos — o quintal, a queima, o córrego — e não quantificam nenhum deles: a contagem não existe.
Registro os desfechos como relato, não como medição.</p>

<p><strong>E &quot;não listado&quot; não é &quot;inofensivo&quot;. É não avaliado.</strong> A
diferença é a mesma que separa absolvição de arquivamento.</p>

<h3>A rota que ninguém mediu: o subsolo e a cisterna</h3>

<p>Este é o ponto em que o artigo precisa ser mais cuidadoso, porque é o de maior consequência
social.</p>

<p><strong>O que se sabe do comportamento do cobre no solo:</strong> ele se liga fortemente à matéria
orgânica e aos óxidos, e por isso é <em>menos</em> móvel que o boro — o que é uma boa notícia para
o lençol e uma má notícia para o solo, porque o metal fica onde foi posto.{cit("rusch2023")} No
único ensaio de campo brasileiro com bambu tratado, cinco anos depois, o <strong>cobre no solo sob o
bambu subiu 12% — sem significância estatística</strong> — e o que subiu de forma expressiva foi o
<strong>cromo, 86%</strong>.{cit("rusch2023")}</p>

<p><strong>Traduzindo com honestidade:</strong> o dado disponível <em>contraria</em> a expectativa de
que o cobre do tratamento migre rapidamente para o subsolo. Mas ele mede <strong>um ensaio, uma
espécie, um solo</strong> — e solo arenoso, ácido e pobre em óxidos retém muito menos que solo
argiloso.</p>

<p><strong>O que isso significa para quem bebe água de cisterna:</strong> a cisterna capta chuva, não
lençol — então <strong>a exposição direta não é óbvia</strong>. O risco plausível é outro: apara em
decomposição no quintal, água da chuva lavando essa apara, e <strong>infiltração no solo sob a área
de descarte</strong>.</p>

<p><strong>E aqui o artigo precisa admitir:</strong> <strong>não há medição</strong>. Não localizei
nenhum estudo brasileiro de lixiviação de cobre sob área de descarte de bambu tratado, nem de cobre
em água de cisterna em comunidade produtora. A rota é <strong>plausível pelo mecanismo</strong> e
<strong>não demonstrada em campo</strong>. Quem afirmar que contamina está extrapolando; quem afirmar
que é seguro está extrapolando igual, e com mais consequência.</p>

<h3>A banalização do risco</h3>

<p>O sulfato de cobre tem uma propriedade perigosa para a percepção pública: <strong>é azul, brilha,
é vendido em loja de agropecuária sem receita, e é usado há gerações na piscina e na horta</strong>.
Não arde na pele na hora, não fede, não pega fogo.</p>

<p>Se fosse cromo ou arsênio, ninguém espalharia apara no quintal. Como é &quot;o azulzinho que mata
fungo&quot;, a hipótese — e aqui é hipótese, não medição — é que a apara siga para a composteira, para a
cama do animal, para a cobertura da horta ou para o fogo. <strong>Eu não medi nenhum desses
destinos.</strong> O que está documentado é a proibição, escrita pela própria cadeia, de que o resíduo
tratado vá para cama de animal, contato com alimento ou água potável, e de que seja queimado em fogão
ou a céu aberto.{cit("abpm2015")}</p>

<p><strong>O que a evidência sustenta, com precisão:</strong></p>

<ul>
<li>o resíduo contaminado é o <strong>maior contribuinte de impacto potencial</strong> na única
cadeia brasileira medida — 91% da carga de resíduo, 93% da categoria de toxicidade
carcinogênica;{cit("araujo2025")}</li>
<li>o cobre tem <strong>efeito crítico documentado</strong> — náusea aguda a partir de 4 mg/L e
acúmulo <strong>hepático</strong> na exposição prolongada;{cit("oms2004")}</li>
<li>as receitas informais que esta frente leu <strong>não trazem uma linha de EPI, ventilação ou
descarte</strong> — nas que eu li, nenhuma traz;{cit("blogtcs2016")}{cit("espaconaturalmente")}</li>
<li>as duas instruções oficiais — a brasileira e a indiana — mandam <strong>reusar</strong> a
solução, o que reduz o volume mas <strong>não elimina o resíduo final</strong>.{cit("tonini2024")}{cit("nmba2006")}</li>
</ul>

<p><strong>O que a evidência não sustenta:</strong> que a apara no quintal produza doença em quem
mora ali. Não há esse dado, em nenhum lugar que esta frente tenha encontrado.</p>

<h3>A pergunta que fica para quem regula</h3>

<p>Este artigo não tem autoridade para dizer quem deveria fiscalizar. Tem autoridade para registrar
o que a ausência produz:</p>

<ol>
<li><strong>É uma cadeia em crescimento</strong> — e a política do bambu existe justamente para
estimulá-la;{cit("pnmcb2011")}</li>
<li><strong>o estímulo não vem acompanhado de disciplina de resíduo</strong>, porque a norma do
bambu não trata do assunto e a norma de resíduo não nomeia o bambu;{cit("pnmcb2011")}{cit("pnrs2010")}</li>
<li><strong>o uso é comunitário e cooperativo</strong> — é o que a própria política incentiva — e é
justamente o formato em que <strong>não localizei nenhum controle de efluente</strong> nas fontes
consultadas;</li>
<li><strong>e as áreas de maior atrativo estão em território sensível.</strong></li>
</ol>

<p><strong>Onde isso deixa de ser artigo e passa a ser política pública:</strong> quando cooperativas
em comunidades remotas — inclusive em áreas de proteção — adotam o tratamento com sulfato de cobre
sem saber o que fazer com a apara. <strong>O boro e o cobre chegam ao território; a norma não.</strong></p>
""")

pagina("p-norma", "09 · A norma e o quintal", "09",
       "A norma existe — e o descarte mora no rótulo",
       "09 · A NORMA E O QUINTAL · GAVETA COBRE · 2026-11-24", f"""
<p>Ao longo deste artigo eu afirmei várias vezes que <strong>ninguém diz o que fazer com a
sobra</strong>. Isso estava errado — e a correção é o achado mais importante desta gaveta. Existe norma
federal, de 1989, que registra o preservativo e nomeia quem fiscaliza; existe uma instrução de 1992 com
<strong>seção própria sobre destinação final de resíduos</strong>; e existe, escrita na Portaria, uma
<strong>exceção para uso doméstico</strong>. Nada disso estava no artigo antes, e a última peça —
a instrução de 1992 — estava declarada como "pendente de custódia" enquanto o texto afirmava o
contrário do que ela diz.</p>

<p>O que está escrito, e o que eu deduzi — preciso separar as duas coisas, porque já confundi nesta
gaveta.</p>

<p><strong>Está escrito:</strong></p>
<ul>
<li>a norma <strong>manda</strong> o resíduo ter destinação final — item VIII da IN 5/92;</li>
<li>manda também que o descarte <strong>siga as recomendações da bula</strong>, e exige que a bula traga
o destino final;</li>
<li>a cadeia é definida por empresa — indústria, usina, importador, comércio (inclusive varejo) e
<strong>usuário, que é &quot;toda e qualquer empresa&quot;</strong>;</li>
<li>o art. 4º da Portaria <strong>dispensa de registro</strong> o preservativo destinado a experimentação
e uso domissanitário.</li>
</ul>

<p><strong>É dedução minha, e vai marcada como tal:</strong> que o produto dispensado de registro não
venha a ter bula; e que, sem bula, não haja onde a instrução de descarte pouse. Nenhum dos documentos
que custodiei diz isso. Pode perfeitamente haver bula, rótulo ou instrução para produto não registrado —
eu não verifiquei, e não afirmo.</p>

<p>O que a norma faz, com todas as letras, é <strong>apontar para o rótulo</strong>. Se o rótulo existe
fora do registro, é pergunta aberta. Se não existe, é o buraco. Eu não fechei essa pergunta.</p>

{SEP}

<h3>A regra, lida no original</h3>

<p>Três ministérios — Fazenda, Saúde e Interior — assinaram em 1989 a
<strong>Portaria Interministerial 292</strong>. Ela não ensina a tratar madeira: ela decide quem
pode tratar, e quem vigia. Em quatro páginas, três artigos sustentam tudo: {cit("pi292")}</p>

<ul>
<li><strong>art. 1º</strong> — a empresa que vive de preservar madeira tem de estar registrada no Ibama;</li>
<li><strong>art. 3º</strong> — o preservativo <em>não pode ser fabricado, consumido ou posto à venda</em>
antes do registro. O "consumido" aqui é o <strong>preservativo gasto no processo</strong>, na usina — não
o consumo doméstico da madeira tratada;</li>
<li><strong>art. 4º</strong> — e este artigo, que eu não tinha citado até a auditoria me obrigar a
relê-la: <em>"Não estão sujeitos ao registro no IBAMA os preservativos que forem destinados à
experimentação e ao uso domissanitário."</em> <strong>A norma prevê uma exceção escrita para uso
doméstico.</strong></li>
<li><strong>art. 20</strong> — e aqui está o que quase ninguém cita:
<strong>"O IBAMA fiscalizará as atividades relacionadas com a preservação e comércio dos
preservativos para madeira e de madeira preservada."</strong></li>
</ul>

{bq("<strong>A competência não está indefinida. Está escrita, com nome, desde 1989.</strong>")}

<p>Há mais: pelo <strong>art. 21</strong>, o Ibama não tem apenas o poder de autuar — tem o de
<em>implementar medidas para assegurar a correta utilização</em> do preservativo. E pelo
<strong>art. 22</strong>, a infração responde civil e penalmente. Uma norma posterior, de 1997,
completa o desenho: para registrar o produto, a empresa precisa provar o
<strong>risco ambiental</strong> dele.{cit("pn151")}</p>

{SEP}

<h3>A instrução que diz o resto — e o lugar onde ela põe a regra</h3>

<p>A Portaria de 1989 não é a última palavra. Ela foi <strong>disciplinada</strong> três anos depois
pela <strong>Instrução Normativa Ibama nº 5, de 20 de outubro de 1992</strong>{cit("in592")} — que tem,
literalmente, um item com este título:</p>

{bq("<strong>VIII - DA DESTINAÇÃO FINAL DE RESÍDUOS E EMBALAGENS</strong>")}

<p>E dentro dele, a alínea que resolve a pergunta deste artigo:</p>

<blockquote>&quot;o descarte da embalagem e resíduos de preservativos de madeira e ingredientes ativos
<strong>deverá atender às recomendações técnicas apresentadas na bula</strong>, relativas aos processos
de destinação final, observadas as exigências dos setores de saúde e meio ambiente&quot;</blockquote>

<p>Leia de novo, devagar, porque é aqui que o problema mora. A instrução <strong>não diz qual é o
descarte</strong>. Ela diz que o descarte tem de seguir <strong>o que o rótulo mandar</strong>. E o item
VI da mesma instrução exige que a bula traga &quot;informações sobre o destino final das embalagens e
dos resíduos&quot;.</p>

<p>Ou seja: a obrigação é da lei; <strong>o conteúdo da obrigação é do fabricante</strong>, que escreve
a bula, e do Ibama, que a aprova. Isso não é fraude nem brecha — é desenho declarado, e é comum em
regulação por produto. Mas tem uma consequência que a peça precisa dizer sem exagerar: <strong>a norma não diz qual é o
descarte — manda perguntar ao rótulo.</strong> A obrigação está na norma; o conteúdo técnico dela é
que mora na bula.</p>

<p>E agora a pergunta que a peça tem de deixar aberta, em vez de responder por conta própria. O art.
4º da Portaria dispensa de registro o preservativo destinado a <strong>experimentação e uso
domissanitário</strong>. A bula, tal como a IN 5/92 a descreve, é peça do regime de produto e empresa
registrados. <strong>Se o produto dispensado de registro tem bula, eu não verifiquei.</strong> Se tiver,
a instrução de descarte pode estar lá. Se não tiver, ela não tem onde estar. Eu não fecho essa
pergunta com documento — e não vou fechá-la por dedução.</p>

<h3>Quem a instrução enxerga — e quem ela não enxerga</h3>

<p>A IN 5/92 define a cadeia inteira. Vale ler a definição de <strong>usuário</strong>, que é o elo mais
próximo de quem trata bambu:</p>

<blockquote>&quot;usuário de preservativos de madeira - <strong>toda e qualquer empresa</strong> que faça uso
de preservativos de madeira em qualquer das etapas de seu processo produtivo, bem como as
<strong>empresas</strong> prestadoras de serviços&quot;</blockquote>

<p>O usuário é empresa. O comércio é &quot;estabelecimento comercial&quot;, inclusive de varejo. A
indústria é estabelecimento. A usina é unidade industrial. <strong>Não existe, em nenhuma alínea, uma
categoria para a pessoa que compra o produto na loja de agropecuária e trata a peça no quintal</strong>
— ele não é indústria, não é usina, não é comércio e não é usuário, pela definição da própria
instrução.</p>

<p>O cadastro do Ibama confirma o mesmo recorte por outro caminho: as categorias do Cadastro Técnico
Federal para o setor — inclusive &quot;depósito de resíduos perigosos&quot; e &quot;tratamento de
efluentes industriais&quot; — são descritas sempre <strong>&quot;no próprio estabelecimento
industrial&quot;</strong>. O controle é por estabelecimento. O quintal não é estabelecimento.</p>

{SEP}

<h3>A palavra que não aparece</h3>

<p>Varri as quatro páginas da Portaria à procura de uma palavra. Ela não está lá:
<strong>"resíduo"</strong>.</p>

<p>Não é descuido. É o desenho da norma: ela controla <strong>a entrada</strong> (registro do produto)
e <strong>o processo</strong> (relatório semestral de produção). Da <strong>saída</strong> — a peça
tratada que um dia vira o que descartar — ela não trata. Digo "não trata", que é o que está medido na
letra; dizer que ela "não alcança" seria juízo sobre alcance jurídico, e isso o texto da Portaria
sozinho não me dá.</p>

{note("O que isso significa na prática",
 "A norma acompanha o moirão até o portão da usina. Depois do portão, ele é propriedade de quem "
 "comprou — e a partir daí nenhuma das três páginas fala com ele. Não porque a norma seja omissa "
 "por acidente: porque ela nunca foi escrita para acompanhar a peça até a sua casa.")}

{SEP}

<h3>O próprio órgão ambiental escrevendo o que não sabe</h3>

<p>Aqui o material deixa de depender de interpretação. O Instituto Estadual de Meio Ambiente do
Espírito Santo publicou em 2023 uma nota técnica sobre licenciamento da preservação de madeira —
36 páginas escritas por quem licencia, não por quem critica.{cit("iema2023")}</p>

<p>Três frases dela, na ordem em que aparecem:</p>

<ol>
<li><strong>O CCA domina o setor</strong> — 80% do volume; o CCB, junto com lindane e
tribromofenato, 15%; creosoto, 5%.</li>
<li><strong>Não há proibição no Brasil</strong> — e o mesmo documento registra, duas páginas depois,
que a EPA americana anunciou em 2003 o fim do uso residencial do CCA: nada de playground, deck ou
cerca de casa.</li>
<li><strong>E sobre o CCB</strong> — que é justamente o preservativo que a Embrapa ensina ao
produtor rural: <em>"Não existem muitas informações sobre o CCB em relação aos aspectos ambientais
e à disposição de resíduos na madeira tratada."</em></li>
</ol>

{bq("O órgão que licencia diz, por escrito, que <strong>não há proibição</strong>, que o resto do mundo "
    "saiu do uso residencial, e que <strong>não tem informação sobre o destino do resíduo</strong>. "
    "As três coisas na mesma nota técnica.")}

<p>E o que a nota exige de quem opera dentro da lei? Que <strong>100% do efluente contaminado volte
para o processo</strong>, que a madeira fique 15 dias curando antes de ser tocada, e que o resíduo
sólido — <strong>Classe I</strong> — vá para aterro industrial licenciado. Essa é a régua. Guarde
ela, porque o capítulo seguinte compara.</p>

{SEP}

<h3>A própria cadeia diz que não se queima</h3>

<p>Não é preciso apelar a ambientalista. A associação brasileira do setor de madeira apresentou num
simpósio, em 2015, a lista do que o resíduo tratado <strong>não pode</strong>:{cit("abpm2015")}</p>

{bq("Contato com alimentos ou água potável · Cama para animais · "
    "<strong>Queima a céu aberto ou em fogões/churrasqueiras/fornos/caldeiras de baixa "
    "temperatura</strong>")}

<p>O detalhe que impede o exagero: a mesma lista <strong>admite</strong> recuperação energética — ou
seja, queimar em <strong>instalação licenciada</strong> é destino aceito. O que a lista proíbe é
queimar <strong>no fogão de casa</strong>. A diferença não está no fogo: está na instalação, no
filtro e no que sobra depois.</p>

{SEP}

<h3>O que a madeira perde e o solo ganha</h3>

<p>Se o preservativo ficasse dentro da peça, nada disso importaria. Ele não fica. Um ensaio de campo
publicado em 2025 acompanhou <strong>cinco moirões de eucalipto tratados com CCA</strong> durante
<strong>880 dias</strong>, medindo a madeira e o solo em volta, em duas profundidades.{cit("ufsm2025")}</p>

{kpis([("−55,0%", "queda de arsênio na madeira"),
       ("+129,2%", "aumento de arsênio no solo"),
       ("32,3%", "acima do limite de investigação agrícola"),
       ("880", "dias de campo, seis amostragens")])}

<p>O terceiro número é o que interessa juridicamente: o solo passou do <strong>valor máximo de
investigação</strong> que a Resolução CONAMA 420/2009 fixa para área agrícola — o ponto a partir do
qual a norma manda investigar se há risco.</p>

<p>E repare no que esse experimento é: <strong>um moirão de cerca, em campo, no uso para o qual foi
feito</strong>. Não é indústria, não é acidente, não é despejo: é o produto em uso, <strong>naquele
sítio, com aquelas cinco peças</strong>. Não é demonstração geral de que todo moirão tratado vaze —
é o que aquele ensaio mediu.</p>

<p>O que os números provam e o que eles não provam, separado: <strong>provam</strong> que a
concentração de arsênio caiu na madeira e subiu no solo em volta, no mesmo sítio e no mesmo
período, com cobre e cromo no sentido oposto. <strong>Não provam sozinhos</strong> o caminho do
material — a lixiviação é a explicação que os autores do estudo dão, não o que uma diferença de
concentração demonstra por si. Chamar aquilo de "a sobra que já estava saindo" é minha leitura da
conclusão deles, e vai marcada como leitura.</p>

{note("O limite do estudo, que o estudo declara",
 "Cinco peças, um sítio. Mediu solo até 40 cm — <strong>não mediu água subterrânea</strong>. Mediu "
 "lixiviação — <strong>não mediu queima</strong>. E é CCA, que tem arsênio; o CCB tem boro, e "
 "transportar a conclusão de um para o outro é inferência, não medição.")}

{SEP}

<h3>Onde a madeira e o bambu se separam — e é aqui que este artigo pesa</h3>

<p>Para a <strong>madeira</strong>, a estrutura existe: norma federal, registro obrigatório,
fiscalizador nomeado, órgão estadual licenciando, item próprio sobre destinação final de resíduo, e
uma <strong>bula</strong> onde essa destinação é escrita. Tudo isso pode não ser cumprido — mas está
escrito, e tem <em>onde</em> estar escrito.</p>

<p>Para o <strong>bambu</strong>, essa estrutura não existe: não há registro de preservativo para
bambu, não há usina licenciada de tratamento, e não localizei <em>classificação publicada</em> para o
resíduo do banho. O tratamento é feito em tonel, no quintal, por quem aprendeu numa apostila. E, sem
produto registrado, <strong>não localizei bula</strong> — não encontrei o documento em que a instrução
de descarte estaria escrita. Se existe bula para produto dispensado de registro, eu não fechei essa
pergunta, e nenhum dos sete documentos a responde. É ausência de busca minha, declarada, não
inexistência provada.</p>

<p>É por isso que a diferença entre a madeira e o bambu, aqui, não é de rigor de quem trata: é de
<strong>onde a regra consegue pousar</strong>. Na madeira, ela pousa num rótulo que existe, mesmo
que ninguém o leia. No bambu, ela não tem — nos documentos que eu li — onde pousar.</p>

<p>E aqui é preciso evitar o salto que eu mesmo já dei: <strong>não</strong> quer dizer que o resíduo
do bambu esteja fora da lei. A Política Nacional de Resíduos Sólidos vale para qualquer resíduo
sólido — e alcança o resíduo líquido quando o lançamento em rede ou corpo d'água é inviável, pelo
art. 3º, XVI,{cit("pnrs2010")} que é o caso do banho (seção 8). Para dar destinação, o
resíduo precisa ser classificado, e a norma técnica que faz isso é a NBR 10.004, citada aqui pelo
número, não pela leitura: a edição de 2024 é paga e eu não a li. O que
não existe é norma <em>da cadeia do bambu</em>, classificação publicada para esse resíduo específico,
e órgão que tenha olhado para ele.</p>

{bq("<strong>A madeira tem norma específica que não se cumpre. O bambu não tem norma específica: "
    "o resíduo dele cai na obrigação geral, escrita para todo resíduo.</strong> As duas coisas "
    "terminam no mesmo lugar — um resíduo cujo destino está escrito no rótulo de um produto "
    "que ele não tem.")}

<p>É por isso que este capítulo não substitui o capítulo do limbo: ele explica por que o limbo é
pior no bambu. A política de 2011 incentiva a cadeia do bambu; a de 2010 disciplina resíduo sólido
sem nomear bambu; e a norma que disciplina preservativo de madeira, de 1989, tem como sujeito a
<strong>empresa registrada</strong> e a usina licenciada — lida assim, ela não alcança uma peça
tratada no quintal, e o quintal não é empresa. Essa última frase é interpretação de escopo, não
medição: o que está medido é que a Portaria não trata da destinação final.</p>

{SEP}

<h3>O que não se mediu — e por que isso é resultado</h3>

<p>Procurei, para este artigo, um caso brasileiro documentado de intoxicação por queimar madeira
tratada em fogão a lenha. <strong>Não encontrei.</strong></p>

<p>Não é o mesmo que dizer que não acontece. É dizer que <strong>não está medido</strong> — e essa
distinção é o método deste artigo inteiro. O que existe é: a proibição, escrita pela própria
cadeia;{cit("abpm2015")} a constatação de que a fumaça de fogão a lenha é um problema de saúde
pública reconhecido no Brasil; e o registro de que a lenha catada em área rural
<strong>"engloba restos de caixas e madeiras tratadas"</strong>.</p>

<p>Há um detalhe que muda o lugar da busca: o próprio rótulo do preservativo registrado no Ibama
manda notificar casos ao <strong>Sinan</strong> e ao <strong>Notivisa</strong>, e traz o telefone do
Disque-Intoxicação — ou seja, <strong>existe um canal previsto</strong> para esse registro, e ele não
é um artigo científico. Não medi se a notificação é feita, nem se o registro é consultável. O que
posso dizer é que, se um caso existe e foi notificado, ele estaria num sistema de vigilância, não
necessariamente na literatura.</p>

{note("A frase honesta, que eu prefiro ao número inventado",
 "Não há, no material reunido, caso brasileiro documentado de intoxicação por combustão de madeira "
 "tratada em fogão doméstico. Há proibição declarada, há prática relatada e há canal de notificação. "
 "Transformar isso em \"há muitos casos\" seria fazer exatamente o que este artigo critica.")}

{SEP}

<h3>O que fica</h3>

<p>A norma brasileira de preservação de madeira existe, é de 1989, e nomeia quem fiscaliza. A
instrução que a disciplina existe, é de 1992, e tem seção própria sobre destinação final de resíduos.
<strong>As duas coisas são verdade, e nenhuma das duas é o problema.</strong></p>

<p>O problema é o encadeamento: a norma manda o resíduo ter destino, e manda o descarte seguir a bula.
Ora, quem trata bambu no quintal não é indústria, não é usina, não é comércio e não é usuário — pela
definição da própria instrução, que reserva o termo &quot;usuário&quot; às empresas. <strong>Não
localizei, na IN 5/92, uma única obrigação dirigida ao comprador pessoa física.</strong> Isso é o que
os documentos sustentam. Dizer que ele está fora da estrutura seria mais do que isso, e eu não
digo.</p>

<p>O que eu <em>não</em> afirmo, e faço questão de separar: que o tratamento de bambu no quintal seja
"uso domissanitário" no sentido do art. 4º. O termo vem da regulação de saneantes, e decidir se ele
abrange tratar material no quintal é interpretação que este artigo não faz. O que está documentado é
mais estreito e mais incômodo: <strong>a regra de descarte que existe foi escrita para caber num
rótulo, e não localizei rótulo nem bula para quem trata em casa</strong>. E não encontrei documento
de que as obrigações gerais tenham sido aplicadas a este resíduo.</p>
""")

pagina("p-9", "10 · Como ler · Resumo", "10", "Como ler qualquer texto sobre cobre — e o resumo do artigo",
       "10 · COMO LER · RESUMO · GAVETA COBRE · 2026-11-24", f"""
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
<li><strong>A lacuna:</strong> as instruções de <em>tratamento</em> não dizem o que fazer quando o reuso
acaba. A norma do <em>preservativo</em> diz — manda a bula dizer (IN 5/92, item VIII) —, e quem trata
em casa não tem bula que eu tenha localizado.</li>
<li>A lei brasileira inclui líquidos na definição de resíduo sólido <strong>sob condição</strong> (PNRS,
art. 3º, XVI); se esta água cumpre a condição é questão jurídica que o artigo não decide. O que não
depende dela: <strong>1,0 mg de cobre por litro</strong> é o limite de lançamento.</li>
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
  "seja inviável. Se o banho de tratamento cumpre essa condição é questão jurídica; o artigo não a decide."),
 ("Solubilidade", "capacidade de uma substância se dissolver em água. É a propriedade que permite o cobre "
  "entrar no bambu — e sair dele."),
 ("Toxicidade crônica", "efeito que aparece por exposição repetida ao longo do tempo, não de uma vez."),
 ("Toxicidade hepática", "dano ao fígado. É o efeito crônico do excesso de cobre."),
]

_itens = "".join(f"<p><strong>{t}</strong> — {d}</p>" for t, d in _GLOSS)

pagina("p-10", "Glossário", "11", "Glossário — para voltar quando esquecer um termo",
       f"GLOSSÁRIO · {len(_GLOSS)} TERMOS · GAVETA COBRE · 2026-11-24", f"""
<p>Termos em ordem alfabética. Todos aparecem explicados no corpo do texto; este é o lugar de consulta.</p>

{_itens}

{SEP}
""")


# ============================== 10 · PROVENIÊNCIA ==============================
pagina("p-11", "Proveniência", "12", "Para saber mais, e como este texto foi feito",
       "PROVENIÊNCIA · GAVETA COBRE · 2026-11-24", f"""
<p>Este artigo não inventa dados. Ele reorganiza, em linguagem simples, o conteúdo de uma frente de pesquisa
do <strong>Acervo Soberania Tecnológica</strong> dedicada ao cobre, que custodia as fontes com
<strong>hash SHA-256 registrado em manifesto</strong> — o hash prova que o arquivo não mudou desde o
registro; não é assinatura digital, não tem chave e não tem signatário.</p>

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

{okbox("O que as auditorias mediram — e o que não mediram",
 "Elas julgaram <strong>conteúdo</strong>, rodada a rodada: se cada afirmação tinha esteio no documento "
 "custodiado. <strong>Não</strong> fizeram um diff palavra por palavra das citações deste artigo. "
 "A medição de literalidade que existe é limitada, está registrada ao lado do texto e vai com o "
 "denominador contado antes: dos <strong>49</strong> blocos de citação do manuscrito, <strong>5</strong> "
 "retornam palavra por palavra no extrato custodiado e <strong>2</strong> são traduções — nelas, "
 "literalidade não é o instrumento aplicável. Os outros <strong>42</strong> não foram conferidos por "
 "esse método e ficam declarados como <strong>não medidos</strong>. À parte disso, nas 6 fichas das "
 "custódias normativas, os <strong>38</strong> blocos citados retornam verbatim no extrato "
 "(portão de fidelidade, saída 0). Integridade dos arquivos: <strong>hash SHA-256 em manifesto</strong>. "
 "E as declarações de &quot;não sei&quot; foram mantidas como declarações, sem virar afirmação no meio "
 "do texto. <strong>Limite da custódia, declarado:</strong> os PDFs das fontes saíram do repositório "
 "por regra do CI e vivem em custódia privada, com caminho e sha256 registrados em manifesto. Quem "
 "recebe o arquivo confere o byte; quem não recebe só confere a identidade. Isso é <strong>custódia "
 "parcial</strong> — a fonte não é reproduzível por quem não tem o PDF, e este texto não finge o "
 "contrário.")}

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
