# -*- coding: utf-8 -*-
"""Consolida a leitura integral: o que as sete custodiadas dizem, parágrafo por parágrafo."""
import json
import os
import sys

RAIZ = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica"
DEST = f"{RAIZ}/docs/analyses/cobre/leitura-integral"
sys.path.insert(0, f"{RAIZ}/scripts")
from s11e_classificacao import CLASSIFICACAO  # noqa: E402

ORDEM = [
    "pi292-preservativos-registro",
    "in05-ibama-destinacao-final-residuos",
    "pn151-ibama-registro-risco-ambiental",
    "ctf-ibama-categorias-preservativos",
    "iema-es-nt01-preservacao-madeira",
    "abpm-fg4mad-destinacao-residuos-madeira-tratada",
    "ufsm-ciencia-florestal-cca-moiroes-solo",
]

linhas = [
    "# Leitura integral das sete custodiadas — o que a letra diz",
    "",
    "Gaveta cobre · 2026-11-24 · 1.008 parágrafos lidos, classificados um por um, com portão de "
    "cobertura total (`scripts/s11e_gate_leitura.py`).",
    "",
    "**Por que este arquivo existe.** A peça vinha afirmando, em várias passagens, que ninguém diz "
    "o que fazer com o resíduo. A IN Ibama 5/92 estava declarada *pendente* na custódia, e a "
    "Portaria 292/89 tinha sido lida por recorte. Documento custodiado e lido em pedaços é meia "
    "custódia: o que se afirma sobre ele herda o recorte.",
    "",
    "## O que mudou quando os documentos foram lidos inteiros",
    "",
    "| antes | depois da leitura integral |",
    "|---|---|",
    "| «ninguém diz o que fazer com a sobra» | a IN 5/92, item VIII, **manda** o descarte seguir as recomendações da bula; o item VI «h» exige que a bula traga o destino final |",
    "| «a norma não alcança o resíduo» | a norma alcança e delega: o conteúdo técnico é da bula, a obrigação é dela |",
    "| «não há controle de efluente» | no Espírito Santo a condicionante de licença exige **100% de reuso** do efluente industrial; o descarte, se necessário, só em empresa licenciada Classe I, com comprovante ao Iema |",
    "| «a bula é só recomendação» | o próprio regulador escreve que as instruções da bula «têm poder normativo» e descumpri-las «constituem infração» |",
    "| «ninguém mede a madeira tratada» | a Portaria 292/89, art. 11, exige relatório semestral de **volume de madeira tratada** por preservativo; a ABPM estima 2,0 milhões de m³/ano |",
    "| «o cobre do CCA lixivia para o solo» | na medição da UFSM, **Cu e Cr caíram** no solo (−17% e −30%); só o arsênio subiu (+129,2%) |",
    "| «o varejo vende sem controle» | o Ibama tem categoria de CTF para **comércio varejista** de preservativo (18-17) |",
    "",
    "## 1. Portaria Interministerial 292/89 — 4 páginas, 91 parágrafos",
    "",
    "- **art. 1º** — registro obrigatório para empresas que se dediquem «à indústria e comércio» de "
    "preservativos e preservação de madeiras.",
    "- **art. 3º** — o preservativo «só poderá ser fabricado, consumido ou posto à venda depois de "
    "registrado». O «consumido» é o produto gasto no processo, não o uso doméstico da madeira tratada.",
    "- **art. 4º** — **a exceção**: «Não estão sujeitos ao registro no IBAMA os preservativos que "
    "forem destinados à experimentação e ao uso domissanitário.»",
    "- **art. 5º** — o memorial de registro do produto exige, entre outros, «instruções para uso, "
    "incluindo precauções na manipulação» e «modelo de rótulo».",
    "- **art. 11** — a usina entrega relatório semestral com gêneros, dimensões, **volume de madeira "
    "tratada mensalmente**, concentração e consumo de preservativo.",
    "- **art. 14** — usuárias e comércio, inclusive importadoras, são obrigadas ao **cadastro**.",
    "- **art. 15** — o que rótulo e bula devem conter: marca, registro, composição, instruções de uso, "
    "classificação de risco, primeiros socorros. **O destino do resíduo não está neste artigo** — vem "
    "da instrução de 1992.",
    "- **art. 19** — fiscalização «por ocasião da instalação das empresas ... ou em época que julgar "
    "oportuna». **art. 20** — «O IBAMA fiscalizará as atividades relacionadas com a preservação e "
    "comércio dos preservativos para madeira e de madeira preservada.»",
    "",
    "## 2. Instrução Normativa Ibama 5/92 — 15 páginas, 161 parágrafos",
    "",
    "- **item I** — a cadeia inteira é definida por estabelecimento: indústria, usina (sob pressão, sem "
    "pressão, piloto), importador, comércio «no varejo ou atacado» e **usuário, que é «toda e qualquer "
    "empresa»**. Não existe alínea para pessoa física.",
    "- **item II** — registro de empresas (indústria, usina) e de produtos; o pedido de registro do "
    "produto vem acompanhado de **«modelo de bula»**.",
    "- **item III** — cadastro de importador, comércio e usuário, com «consumo médio / mensal / produto».",
    "- **item VI «h»** — a bula deve trazer «informações sobre o destino final das embalagens e dos "
    "resíduos», além de EPI, modo de aplicação e limitações de uso.",
    "- **item VII «a»** — organoclorados só em venda direta entre produtor/importador e consumidor; "
    "o varejo tem 90 dias para escoar estoque.",
    "- **item VIII** — «**DA DESTINAÇÃO FINAL DE RESÍDUOS E EMBALAGENS**»: embalagem não se reutiliza; "
    "«o descarte da embalagem e resíduos de preservativos de madeira e ingredientes ativos **deverá "
    "atender às recomendações técnicas apresentadas na bula**, relativas aos processos de destinação "
    "final, observadas as exigências dos setores de saúde e meio ambiente».",
    "- **anexo 3, item 8** — o dossiê de risco ambiental pede «indicações de uso para madeira tratada».",
    "- **anexo 3, item 9** — e pede «**métodos para desativação do ingrediente ativo**».",
    "- **anexo 3, item 11** — a bateria de ecotoxicidade inclui biodegradabilidade em solos (E.1.2), "
    "**mobilidade (E.2)**, **adsorção/dessorção (E.3)** e toxicidade a organismos do solo (D.5.1).",
    "- **anexos 4 e 5** — modelos de relatório semestral: produção e comércio da indústria; consumo e "
    "produção da usina, com volume de madeira tratada.",
    "",
    "## 3. Portaria Normativa Ibama 151/97 — 1 página, 20 parágrafos",
    "",
    "Condiciona o registro à determinação do risco ambiental e organiza o dossiê em volumes C, D, E, F "
    "e G. Confirma, no art. 1º, que a documentação exigida é a do art. 5º da Portaria 292/89 **e a do "
    "inciso II da IN 05/92** — a instrução é o instrumento operante do sistema.",
    "",
    "## 4. Página oficial do CTF/Ibama — 595 parágrafos",
    "",
    "As categorias do Cadastro Técnico Federal, transcritas:",
    "",
    "- **Usuário — 7.2 Preservação de madeira**: inclui «o depósito de resíduos perigosos, **no mesmo "
    "estabelecimento** em que ocorra a sua geração» e «o tratamento de efluentes industriais **no "
    "próprio estabelecimento industrial** gerador de efluentes».",
    "- **Fabricante — 15.17**: produção de preservativo, creosoto, ingrediente ativo.",
    "- **Titular de registro / Comerciante / Importador — 18-17**: importação, comércio atacadista, "
    "comércio direto entre fabricante e utilizador e «**comércio varejista de produtos preservativos "
    "de madeira**».",
    "",
    "O recorte é por estabelecimento em todas as alíneas. O quintal não é estabelecimento.",
    "",
    "## 5. Iema-ES, NT 01/2023 — 36 páginas, 95 parágrafos",
    "",
    "O regulador estadual, escrevendo para quem licencia e para quem é licenciado:",
    "",
    "- **p. 2** — registra «precariedade no conteúdo nos controles ambientais da operação», com "
    "armazenamento incorreto do preservante e da madeira tratada.",
    "- **p. 5** — CCA = 80% do volume; CCB + lindane + TBP = 15%; creosoto = 5%; e a admissão: «não "
    "existem muitas informações sobre o CCB em relação aos aspectos ambientais e à disposição de "
    "resíduos na madeira tratada».",
    "- **p. 9–10** — o efluente da autoclave volta ao tanque de solução; «todo efluente contaminado ... "
    "deverá ser, em sua totalidade (100 %), utilizado no processo de preservação de madeira».",
    "- **p. 11–12** — enquadra os preservativos como agrotóxicos por similaridade (Lei 7.802/89) e "
    "transcreve os itens VI-a e VIII a-c da IN 05/92 como as obrigações centrais. E então: «as "
    "instruções apresentadas nas bulas ... **têm poder normativo** e o não atendimento ... caracterizam "
    "mau uso dos produtos e, portanto, constituem infração».",
    "- **p. 14** — sete registros válidos de CCA no Brasil; EPA 2003 cessa uso residencial e mantém "
    "rural e industrial; UE restringe uso doméstico desde 2004.",
    "- **p. 29** — condicionante: «em caso de necessidade de descarte, somente poderá ser realizado em "
    "empresas devidamente licenciadas para o recebimento de resíduos Classe I», com comprovantes ao Iema.",
    "- **p. 30** — inventário SINIR considera resíduo sólido também o «líquido (efluentes industriais)».",
    "- **p. 34** — considerações finais: preservantes «altamente tóxicos, com **rígido controle de "
    "comercialização e uso no Brasil**»; e, no modelo licenciado, o efluente é recirculado e não há "
    "lançamento.",
    "",
    "## 6. ABPM / FG4mad (2016) — 21 páginas, 29 parágrafos",
    "",
    "- **p. 3** — a própria cadeia lista o marco: «PI 292 – 1989» e «IN 05 – 1992».",
    "- **p. 12** — o «não podem»: contato com alimentos e água potável, cama para animais, queima a céu "
    "aberto ou em fogão, churrasqueira, forno e caldeira de baixa temperatura.",
    "- **p. 17** — volume anual de madeira tratada no Brasil: 2,0 milhões de m³ (estimativa); EUA, 25,0 "
    "milhões. E o contraste que a própria cadeia faz: nos EUA há rotulagem que identifica o tratamento "
    "«útil no manuseio e descarte nas obras» e regras claras de disposição.",
    "",
    "## 7. UFSM / Ciência Florestal (2025) — 16 páginas, 17 parágrafos",
    "",
    "Ensaio de campo, 880 dias, cinco moirões de eucalipto tratados com CCA-C em autoclave industrial:",
    "",
    "- **na madeira**: As 3.698 → 1.662 mg/kg (−55,0%); Cr 2.407 → 1.330 (−44,7%); Cu 1.068 → 512 (−52,0%).",
    "- **no solo**: **Cr caiu** 175,3 → 122,7 (−30%) e **Cu caiu** 171,2 → 142,7 (−17%); só o **As subiu** "
    "20,2 → 46,3 mg/kg (+129,2%), ficando 32,3% acima do valor de investigação agrícola da CONAMA "
    "420/2009. Cu e Cr ficaram abaixo do agrícola (−28,6% e −18,2%).",
    "- A leitura correta, então, é mais estreita e mais forte: entre os três metais do CCA, **o que "
    "migra para o solo neste ensaio é o arsênio**; cobre e cromo ficam retidos na madeira e no solo.",
    "",
    "## O que a leitura integral **não** resolveu",
    "",
    "- Se o tratamento de bambu no quintal cai na exceção do art. 4º — o termo é «domissanitário», da "
    "família dos saneantes, e a decisão é interpretativa.",
    "- Se o produto dispensado de registro tem ou não bula. Nenhum dos sete documentos diz que não tem.",
    "- Se o resíduo líquido do banho é «resíduo de preservativo e ingrediente ativo» para o item VIII.",
    "- Se as bulas dos sete produtos registrados **de fato** trazem a instrução de destino final exigida "
    "pelo item VI «h». Lê-las é rodada própria.",
    "- Nenhuma norma dirigida ao comprador pessoa física foi localizada nas sete.",
]

p = os.path.join(DEST, "LEITURA_INTEGRAL_SINTESE.md")
open(p, "w", encoding="utf-8").write("\n".join(linhas) + "\n")
print(f"{p}\n{len(linhas)} linhas")
