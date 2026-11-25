# -*- coding: utf-8 -*-
"""Resumos das 14 fontes do cobre — o que cada uma sustenta, com os números medidos.

É o que a bibliografia da peça corrida imprime em itálico depois da referência ABNT,
no mesmo padrão da peça do boro: referência completa + travessão + síntese do conteúdo
que o artigo usa dela.

Cada resumo declara: o que o documento é, os números que ele mede e o limite que ele tem.
"""
import re

RESUMOS = {
"tonini2024":
 "Instrução oficial brasileira de tratamento de moirão na pequena propriedade, pelo método de "
 "substituição de seiva com CCB. <strong>EPI por peça</strong> (óculos, máscara, luvas de borracha, "
 "bota, avental); <strong>tonel de 200 L</strong>; proporção de CCB; proibição explícita de descarte "
 "no ambiente, repetida duas vezes; <strong>reuso da solução excedente em recipiente plástico</strong> "
 "(L207–214); alerta de que dicromato e ácido bórico estão sob controle da Polícia Federal "
 "(Portaria 240/2019, Lei 10.357/2001). <span class='limite'>Limite: trata de madeira (moirões), não de bambu, e não "
 "diz o que fazer quando o reuso termina.</span>",

"nmba2006":
 "Manual do governo indiano sobre preservação de bambu, 60 páginas. Prescreve que "
 "<strong>soluções preservativas não devem ser descartadas em ralos, rios ou córregos</strong>; que a "
 "solução usada <strong>pode ser decantada e reutilizada</strong> (p. 46–47); que o lodo gerado deve "
 "ser recuperado por reagente; e que <strong>resíduos podem ser misturados com serragem e enterrados</strong>. "
 "Prescreve ainda recomposição do lodo com <strong>ácido crômico a pH 2,5</strong>. <span class='limite'>Limite: o "
 "enterro com serragem não é admitido pela lei brasileira para resíduo com metal, e a recuperação com "
 "ácido crômico é operação industrial, não doméstica.</span>",

"scharfenberg2020":
 "Dissertação de mestrado (UFTM, 101 p.) que mediu o efeito das soluções de tratamento de bambu sobre "
 "sementes de alface. <strong>Índice de germinação zero até diluição 1/10</strong>, nas três soluções "
 "testadas (cobre+boro, CCB e boro isolado); <strong>pH 1,28</strong> na solução de cobre e boro e "
 "<strong>0,22</strong> no CCB; índice de germinação <strong>abaixo de 11</strong> contra "
 "<strong>acima de 80</strong> do glifosato; melhor radícula de <strong>0,33 mm</strong> contra "
 "<strong>2,78 mm</strong> em água. <span class='limite'>Limite: é ensaio de laboratório com uma espécie indicadora; não "
 "mede campo, nem solo, nem água corrente, e testou concentrações menores que a receita informal.</span>",

"rusch2023":
 "Ensaio de campo de cinco anos com bambu tratado, publicado na Pesquisa Florestal Brasileira. "
 "<strong>Cobre no solo sob bambu CCB 3%: 27,9 ppm contra 24,9 ppm do controle — +12%, sem "
 "significância estatística</strong>; <strong>cromo: 33,2 → 61,7, alta de 86%</strong>. Descreve a "
 "composição do CCB conforme NBR 6232: <strong>26% sulfato de cobre, 63,5% dicromato, 10,5% ácido "
 "bórico</strong>. <span class='limite'>Limite: é o dado que CONTRARIA a hipótese de que o cobre do CCB migra para o "
 "solo — o que migrou foi o cromo. Um ensaio, uma espécie, um solo.</span>",

"ufmg_mom":
 "Página institucional da Faculdade de Arquitetura da UFMG que publica a receita de tratamento com "
 "bórax: <strong>1 kg : 1 kg : 100 litros</strong>, imersão de <strong>8 a 10 dias</strong>. Declara "
 "expressamente que <em>“este tipo de tratamento não foi comprovado em pesquisas científicas, apesar de "
 "amplamente utilizado”</em>. <span class='limite'>Limite: é receita, não protocolo; não dá EPI, ventilação nem "
 "destinação da solução exaurida.</span>",

"blogtcs2016":
 "Post de blog de construção sustentável (2016) que ensina a fórmula completa com "
 "<strong>dicromato de sódio</strong>: ácido bórico / bórax / dicromato na proporção "
 "<strong>2 : 2 : 0,5</strong>; concentração de <strong>4,5%</strong>, com instrução de "
 "<strong>dobrar para 9%</strong>. Varredura do texto integral (19.305 caracteres): "
 "<strong>zero</strong> ocorrências de “luvas”, “máscara”, “EPI”, “descarte” e “resíduo”; a única "
 "palavra “CUIDADO!!” do texto é sobre mancha na casca do bambu. <span class='limite'>Limite: é fonte informal, "
 "citada aqui como evidência do que circula, não como orientação técnica.</span>",

"espaconaturalmente":
 "Site comercial-educativo sobre construção em bambu. Registra que o preservativo mais utilizado é o "
 "octoborato como inseticida, <em>“e sulfato de cobre como fungicida”</em>. Varredura do texto: "
 "<strong>zero</strong> ocorrências de EPI, descarte, resíduo e “tóxico”. <span class='limite'>Limite: é material de "
 "venda; descreve o padrão de mercado, não avalia risco.</span>",

"gauss2020":
 "Levantamento comparativo de preservantes e métodos de preservação de bambu. Na tabela de "
 "preservantes, a combinação de cloreto de zinco com sulfato de cobre é descrita como "
 "<em>“good fungicide”</em> e, no mesmo campo, <em>“ineffective for termites and insects”</em>. "
 "<span class='limite'>Limite: é a base da afirmação de que o cobre é fungicida e NÃO é inseticida — a distinção que "
 "explica por que a receita mistura três sais.</span>",

"conama430":
 "Resolução que fixa condições e padrões de lançamento de efluentes. <strong>Cobre: 1,0 mg/L</strong> "
 "como limite de lançamento. <span class='limite'>Limite: vale para efluente de fonte geradora regularizada; não é "
 "limite de água de consumo nem de solo.</span>",

"conama357":
 "Resolução que classifica os corpos de água e fixa padrões por classe. <strong>Cobre dissolvido em "
 "água doce Classe 1: 0,009 mg/L (9 µg/L)</strong>. <span class='limite'>Limite: é o padrão de qualidade do corpo "
 "receptor, e é 111 vezes mais restritivo que o limite de lançamento — a razão pela qual diluir não "
 "resolve.</span>",

"oms2004":
 "Documento de base da OMS para o valor de referência do cobre na água de consumo. "
 "<strong>2 mg/L, declarado PROVISÓRIO</strong> por incertezas na curva dose–resposta; "
 "<strong>LOAEL 4 mg/L</strong> para náusea, em estudo com 61 voluntários; acúmulo "
 "<strong>hepático</strong> (“copper accumulates in the liver, brain and eyes”); dose diária "
 "tolerável de <strong>0,17 mg/kg/dia</strong>; LOAEL <strong>10 mg Cu/kg/dia</strong> por água "
 "(machos, efeito renal) e sem efeito a <strong>23 mg/kg/dia</strong> por dieta. <span class='limite'>Limite: o valor "
 "é provisório e o efeito crítico é hepático — citar 2 mg/L como linha dura promove um número "
 "provisório a definitivo.</span>",

"pnrs2010":
 "Política Nacional de Resíduos Sólidos. Art. 3º, XVI define resíduo sólido incluindo "
 "<strong>“líquidos cujas particularidades tornem inviável o seu lançamento na rede pública de esgotos "
 "ou em corpos d'água”</strong>. <span class='limite'>Limite: a lei define e atribui a obrigação ao gerador; não diz "
 "onde o gerador doméstico deve entregar a solução exaurida.</span>",

"comexstat":
 "Base oficial de comércio exterior do MDIC. Série completa da NCM 2833.25 (sulfato de cobre), "
 "1997–2026: <strong>2025 com 177.854 t e US$ 370.053</strong>; <strong>China com 80,4% da massa e "
 "48,3% do valor</strong>; dispersão de preço de <strong>119×</strong> entre a origem mais barata "
 "(China, US$ 1,25/kg) e a mais cara (Reino Unido, US$ 148,43/kg); queda de <strong>86%</strong> "
 "entre 1997 (1.279 t) e 2020 (9,3 t). <span class='limite'>Limite: o preço disperso reflete a mistura de graus "
 "reagente e formulado na mesma NCM — hipótese declarada, não confirmada nos metadados da base.</span>",

"araujo2025":
 "Avaliação de ciclo de vida, com revisão por pares, da produção artesanal de colmo de "
 "<em>Guadua angustifolia</em> em <strong>Rio Branco, Acre</strong> — a única medição "
 "brasileira de uma cadeia artesanal de bambu tratado. Método declarado: SimaPro 9.1, "
 "Ecoinvent 3, <strong>ReCiPe 2016 Midpoint (h)</strong>, ISO 14040/14044, resultados "
 "normalizados em milipontos. <strong>Toxicidade carcinogênica humana = 93% do impacto "
 "potencial normalizado</strong>, e <strong>91% dele nos resíduos</strong> de apara, corte "
 "e colmo descartado — atribuído ao ácido bórico e ao bórax no resíduo e no efluente. "
 "Banho de 100 L de água + 5 kg de bórax + 5 kg de ácido bórico; por quilo de colmo: "
 "0,20 kg de resíduo, 0,13 kg de colmo descartado, 0,07 L de efluente, 25% de perda. "
 "<span class='limite'>Limite: uma unidade, um município, um ano. Os próprios autores "
 "declaram sazonalidade, variabilidade de mão de obra e escassez de dados de inventário no "
 "Brasil. '93%' é categoria do método, não probabilidade de câncer — e a regra que o "
 "artigo descreve é o bórax, não o sulfato de cobre.</span>",

"pnmcb2011":
 "Política Nacional de Incentivo ao Manejo Sustentado e ao Cultivo do Bambu. Seis artigos: "
 "crédito rural, assistência técnica, certificação de origem e incentivo ao intercâmbio "
 "institucional; o art. 5º, III, estimula expressamente o <strong>uso comunitário e "
 "cooperativo</strong>. <span class='limite'>Limite: procure tratamento, químico, resíduo, "
 "licença ou fiscalização no texto — não há. A política incentiva a produção e não "
 "disciplina o que acontece com o que sobra.</span>",

"nbr6232":
 "Norma técnica sobre penetração e retenção de preservativos em madeira tratada sob pressão. "
 "Fornece a <strong>retenção de 6,5 kg/m³</strong> e a <strong>composição percentual do CCB</strong> "
 "usadas no cálculo de cobre por banho. <span class='limite'>Limite: a norma é paga e foi lida apenas na descrição que "
 "Rusch et al. (2023) dela fazem — não foi consultada no original.</span>",
"ufsm2025":
 "Ensaio de campo de 880 dias com <strong>cinco moirões de eucalipto</strong> tratados com CCA-C em "
 "autoclave industrial, seis amostragens em duas profundidades (0–20 e 20–40 cm). O arsênio da "
 "madeira caiu <strong>55,0%</strong> e o do solo subiu <strong>129,2%</strong>, ficando "
 "<strong>32,3% acima do valor máximo de investigação para o setor agrícola</strong> da Resolução "
 "CONAMA 420/2009. <span class='limite'>Limite: cinco peças num sítio; mediu solo até 40 cm, não água "
 "subterrânea; mediu lixiviação, não queima; é CCA, não CCB.</span>",

"pi292":
 "A norma-mãe do setor no Brasil, de 1989, assinada por três ministérios. Torna o registro no Ibama "
 "obrigatório para a empresa (art. 1º) e para o produto — que <strong>não pode ser fabricado, "
 "consumido ou vendido antes do registro</strong> (art. 3º); exige relatório semestral de produção "
 "(art. 2º); e nomeia a competência: <strong>«O IBAMA fiscalizará as atividades relacionadas com a "
 "preservação e comércio dos preservativos para madeira e de madeira preservada»</strong> (art. 20), "
 "podendo «implementar medidas visando assegurar a correta utilização» (art. 21). "
 "<span class='limite'>Limite: a palavra «resíduo» não aparece no texto; a norma controla a entrada e o "
 "processo, não o destino da peça depois que ela sai da usina.</span>",

"in592":
 "A instrução que <strong>disciplina</strong> a Portaria 292/89, de 1992. Tem item com título próprio — "
 "<strong>VIII, «Da destinação final de resíduos e embalagens»</strong> — e manda que «o descarte da "
 "embalagem e resíduos de preservativos de madeira e ingredientes ativos <strong>deverá atender às "
 "recomendações técnicas apresentadas na bula</strong>»; o item VI exige que a bula traga «informações "
 "sobre o destino final das embalagens e dos resíduos». Define a cadeia por empresa, inclusive o "
 "«usuário». <span class='limite'>Limite: a instrução não fixa a destinação — delega à bula; e o "
 "resíduo líquido do banho só entra, no máximo, como «resíduos de preservativos e ingredientes ativos».</span>",

"pn151":
 "Portaria do Ibama que condiciona o registro do preservativo à <strong>determinação do risco "
 "ambiental</strong> do produto e fixa o dossiê exigido. <span class='limite'>Limite: o risco avaliado "
 "é o do produto em uso, não o do resíduo ao fim da vida útil; e o OCR da Imprensa Nacional grafa os "
 "ordinais como «10» e «50» onde a leitura é «1º» e «5º».</span>",

"iema2023":
 "Nota técnica do órgão ambiental do Espírito Santo sobre o licenciamento da preservação de madeira — "
 "o regulador por dentro. <strong>CCA em 80% do volume</strong> do setor, CCB com 15% junto de lindane "
 "e tribromofenato, creosoto 5%; autoclave em 84%; <strong>sete registros válidos de CCA</strong> no "
 "Brasil. Registra que a EPA americana anunciou em 2003 o fim do uso residencial do CCA e que "
 "<strong>«não há proibição de uso no Brasil»</strong>; que o efluente da usina deve ser "
 "<strong>100% reutilizado no processo</strong>; que resíduo tratado é <strong>Classe I</strong> e vai a "
 "aterro industrial; e, sobre o CCB, que <strong>«não existem muitas informações ... em relação aos "
 "aspectos ambientais e à disposição de resíduos na madeira tratada»</strong>. "
 "<span class='limite'>Limite: é orientação de um estado, não norma federal; e os percentuais de "
 "mercado são citados de terceiro, não medidos pelo próprio órgão.</span>",

"abpm2015":
 "Apresentação da associação brasileira do setor de madeira, para o 3º Simpósio Madeira e Construção. "
 "Lista o que o resíduo tratado <strong>não pode</strong>: contato com alimentos ou água potável, cama "
 "para animais, e <strong>«queima a céu aberto ou em fogões/churrasqueiras/fornos/caldeiras de baixa "
 "temperatura»</strong>; admite recuperação energética apenas em instalação licenciada. "
 "<span class='limite'>Limite: é material setorial, não norma; declara a proibição, mas não mede quanto "
 "resíduo é queimado em fogão doméstico no Brasil.</span>",
}


def resumo(chave):
    """Resumo em itálico, pronto para a bibliografia."""
    return RESUMOS.get(chave, "")


def conferir_contagem():
    """Confere que toda afirmação citada tem resumo, e vice-versa."""
    import referencias_cobre as R
    faltando = [r[0] for r in R.REFERENCIAS if r[0] not in RESUMOS]
    sobrando = [k for k in RESUMOS if k not in {r[0] for r in R.REFERENCIAS}]
    return faltando, sobrando


if __name__ == "__main__":
    f, s = conferir_contagem()
    print(f"resumos: {len(RESUMOS)}")
    print(f"sem resumo: {f or 'nenhum'}")
    print(f"órfãos: {s or 'nenhum'}")
    for k, v in RESUMOS.items():
        print(f"  {k:20s} {len(re.sub(chr(60)+'[^>]+'+chr(62), '', v))} chars")
