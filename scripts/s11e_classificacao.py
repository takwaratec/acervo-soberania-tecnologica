#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Classificação da leitura integral, parágrafo por parágrafo.

Cada entrada cobre um intervalo contínuo de parágrafos e diz: o que o trecho faz (classe),
qual é o tema, e se ele toca a tese da gaveta. O portão `s11e_gate_leitura.py` exige que
todo parágrafo do índice esteja coberto e que nenhum id classificado seja inventado.

Classes:
  cabecalho      epígrafe, preâmbulo, assinatura, data de publicação
  definicao      define termo da norma
  dispõe         cria obrigação, proibição, prazo ou procedimento
  formulario     modelo de requerimento/relatório (anexo)
  tecnico        lista de teste, tabela de parâmetro
  rodape         ruído de extração (marca d'água, cabeçalho de página, navegação)
  dado           resultado medido, tabela de resultado (documento científico)
  discussao      argumento, interpretação do próprio autor do documento
"""

CLASSIFICACAO = {}

# --------------------------- Página oficial do Ibama — categorias do CTF (2026)
# Documento extraído de HTML: cada linha é um parágrafo, então a classificação é por
# intervalo de índice, convertido para id na hora.
_CTF_FAIXAS = [
    (0, 61, "rodape", "cabeçalho do portal, menus institucionais e ferramentas de acessibilidade", False),
    (62, 342, "rodape", "navegação de assuntos do portal — inclui o item «Cadastro Técnico Federal (CTF)»", False),
    (343, 407, "rodape", "menu do CTF/AIDA, CTF/APP e tabelas de correspondência", False),
    (408, 486, "rodape", "menu de categorias, data de atualização e cópia do índice de seções", False),
    (487, 493, "discussao", "índice da página: procedimentos de registro, categorias, alterações, lista de produtos, relatórios, mais informações", False),
    (494, 501, "dispoe", "a página declara que os procedimentos de registro estão previstos na PI 292/1989, na IN Ibama 05/1992 e na PN Ibama 151/1997", True),
    (502, 506, "dispoe", "«as empresas que pretendem registrar, produzir, importar ou usar produtos preservativos ... devem estar cadastradas no CTF em uma ou mais das categorias»", True),
    (507, 513, "dispoe", "categoria USUÁRIO, 7.2 Preservação de madeira: estocagem na usina, depósito de produto perigoso e de resíduos perigosos «no mesmo estabelecimento», tratamento de efluentes «no próprio estabelecimento industrial gerador»", True),
    (514, 526, "dispoe", "categoria FABRICANTE, 15.17 Produção de substâncias e fabricação de produtos químicos: produção de preservativo, creosoto, ingrediente ativo", True),
    (527, 535, "dispoe", "categoria TITULAR DE REGISTRO / COMERCIANTE / IMPORTADOR / EXPORTADOR, 18-17: importação, comércio atacadista, comércio direto entre fabricante e utilizador e — explicitamente — «comércio varejista de produtos preservativos de madeira»", True),
    (536, 537, "rodape", "alteração de dados de produto registrado pelo SEI", False),
    (538, 538, "discussao", "acesso à lista de produtos preservativos registrados no Ibama", False),
    (539, 544, "dispoe", "relatórios semestrais: fabricantes pelo anexo 4 e usinas pelo anexo 5 da IN 05/1992", True),
    (545, 557, "tecnico", "envio dos relatórios pelo SEI: planilha, manual de preenchimento, PDF com OCR e .zip com XLSX/ODS", False),
    (558, 559, "rodape", "guia para registro de produtos preservativos", False),
    (560, 578, "tecnico", "legislação correlata listada pela própria página: Lei 10.165/2000, PI 812/2015, Lei 6.938/81, IN 6/2014 (RAPP), IN 10/2013 e 6/2013 (CTF), IN 132/2006 (restrição a lindano e pentaclorofenol), IN 151/97 e IN 5/92", True),
    (579, 581, "rodape", "contato da Diretoria de Qualidade Ambiental (Diqua)", False),
    (582, 594, "rodape", "rodapé do portal: cookies, acesso à informação, licença, pesquisa de satisfação", False),
]

# ------------------------------- Iema-ES, Nota Técnica Orientativa GGE-COED 01/2023
CLASSIFICACAO["iema-es-nt01-preservacao-madeira"] = [
    ("p1.¶1", "cabecalho", "título: principais aspectos dos estudos de licenciamento da preservação de madeira por tratamento químico e/ou orgânico", False),
    ("p1.¶2", "discussao", "introdução: código 9.04 da IN Iema 15/2020; a atividade «possui elevado potencial de causar danos à saúde dos trabalhadores e ao meio ambiente»", True),
    ("p1.¶3", "rodape", "marca de captura eletrônica E-DOCS", False),
    ("p2.¶1", "discussao", "justificativa: o órgão registra «precariedade no conteúdo nos controles ambientais da operação», armazenamento incorreto do preservante e da madeira tratada, e deficiência dos estudos", True),
    ("p2.¶2", "discussao", "objetivos da nota", False),
    ("p2.¶3", "dispoe", "licenciamento: atividade potencialmente poluidora, CONAMA 237; no ES todas as empresas se licenciam no Iema", True),
    ("p3.¶1", "discussao", "rito do licenciamento e o custo da remediação de área contaminada", True),
    ("p3.¶2", "discussao", "abertura da descrição dos processos produtivos", False),
    ("p4.¶1", "tecnico", "fluxograma: armazenamento, preparação, tratamento em autoclave, cura, armazenamento, venda", False),
    ("p4.¶2", "tecnico", "fluxograma de impactos e controles: efluente contaminado vai à bacia de contenção e recircula; resíduo contaminado vai a aterro classe I", True),
    ("p4.¶3", "tecnico", "fluxograma: EPI conforme normas de saúde do trabalhador", False),
    ("p5.¶1", "dado", "matérias-primas; CTF e DOF; CCA = 80% do volume, CCB+lindane+TBP = 15%, creosoto = 5%; autoclave = 84%; «não existem muitas informações sobre o CCB em relação aos aspectos ambientais e à disposição de resíduos»", True),
    ("p6.¶1", "tecnico", "preparação: madeira sem casca para não gerar resíduo contaminado classe I; casca doada para agricultura ou olaria", True),
    ("p6.¶2", "tecnico", "a UPM e o ciclo de vácuo-pressão da autoclave", False),
    ("p7.¶1", "tecnico", "o papel de cada elemento do CCA — arsênico contra insetos, cobre contra fungos, cromo como fixador; madeira sai esverdeada e encharcada, escoando na bacia", True),
    ("p7.¶2", "dispoe", "cura: 15 dias em galpão coberto e impermeabilizado; condicionante de quantificação mensal de madeira tratada, comercializada, em cura e armazenada", True),
    ("p8.¶1", "discussao", "a cura como medida de proteção do solo e da água", False),
    ("p8.¶2", "tecnico", "armazenamento da madeira curada em pátio, sem mistura com madeira in natura", True),
    ("p8.¶3", "tecnico", "emissões atmosféricas por ressuspensão de particulado", False),
    ("p9.¶1", "tecnico", "FISPQ do preservante quanto à saúde do trabalhador", False),
    ("p9.¶2", "tecnico", "ruídos — NBR 10.152", False),
    ("p9.¶3", "dispoe", "«efluentes contaminados»: respingos da madeira pós-tratamento; todo efluente vai à bacia da autoclave e retorna ao tanque de solução", True),
    ("p10.¶1", "dispoe", "«todo efluente contaminado ... deverá ser, em sua totalidade (100 %), utilizado no processo de preservação de madeira»", True),
    ("p10.¶2", "dispoe", "resíduos de madeira NÃO tratada e sua destinação; «resíduos de madeira tratada não podem ser destinados juntamente com os resíduos de madeira não tratada»", True),
    ("p10.¶3", "dispoe", "resíduos contaminados: aparas da madeira tratada são Classe I; coleta e destinação por empresa licenciada classe I; embalagens vazias com logística reversa (Lei 12.305/2010 e Lei estadual 9.264/2009)", True),
    ("p11.¶1", "discussao", "o órgão sustenta que os preservativos se enquadram como agrotóxicos pela Lei 7.802/1989", True),
    ("p11.¶2", "dispoe", "citação do art. 2º da Lei 7.802/89 — definição de agrotóxicos", False),
    ("p11.¶3", "dispoe", "citação do inciso I, alínea a, da Lei 7.802/89", False),
    ("p11.¶4", "dispoe", "citação das alíneas b e do inciso II da Lei 7.802/89", False),
    ("p11.¶5", "discussao", "enquadramento «por similaridade»; rotulagem igual à de agrotóxico pelo Guia 12/2018 da Anvisa; devolução de embalagens vazias (art. 6º §2º); a IN Ibama 05/92 como norma de termos e obrigações", True),
    ("p12.¶1", "dispoe", "o órgão transcreve os itens VI-a e VIII a-c da IN 05/92 como as obrigações centrais", True),
    ("p12.¶2", "dispoe", "transcrição do item VI, alínea a — não reaproveitamento das embalagens em destaque", True),
    ("p12.¶3", "dispoe", "transcrição do item VIII, alíneas a a c — inclusive «o descarte da embalagem e resíduo de preservativos ... deverá atender às recomendações técnicas apresentadas na bula»", True),
    ("p12.¶4", "discussao", "«as instruções apresentadas nas bulas dos produtos preservativos de madeira ... têm poder normativo» e descumpri-las «constituem infração»; exigências de depósito segregado", True),
    ("p13.¶1", "tecnico", "tanques de contenção e sinalização das áreas de armazenamento", False),
    ("p13.¶2", "discussao", "manipulação após o tratamento; tempos de fixação primária por temperatura; padrão de 15 dias; «não há proibição de uso no Brasil»", True),
    ("p14.¶1", "rodape", "endereços das FISPQ e das fichas de registro no Ibama", False),
    ("p14.¶2", "dado", "CCA: classe I; restrições em Japão, Indonésia, Suécia, Dinamarca e Alemanha; EPA 2003 — indústria cessa uso residencial (playground, deck, cerca) mas mantém rural e industrial; UE restringe uso doméstico desde 2004; «no Brasil ... sete registros válidos para o composto CCA»", True),
    ("p14.¶3", "rodape", "nota de rodapé com o endereço da lista de produtos registrados", False),
    ("p14.¶4", "rodape", "marca de captura eletrônica", False),
    ("p15.¶1", "discussao", "FISPQ integra o registro; obrigações de registro e de relatórios ao Ibama; «o licenciamento ambiental ... na massiva maioria das vezes ocorre no ente licenciador estadual»; tendência de substituição do CCA (ACQ, boratos, azóis)", True),
    ("p16.¶1", "discussao", "tendência mundial de restrição progressiva aos preservantes mais danosos", False),
    ("p16.¶2", "dispoe", "prevenção e monitoramento: CCA como alto risco ambiental classe I, «altamente persistente», «altamente móvel», «altamente bioconcentrável» e «altamente tóxico»", True),
    ("p16.¶3", "tecnico", "conteúdo mínimo do estudo hidrogeológico e do plano de monitoramento", False),
    ("p17.¶1", "tecnico", "normas do plano de monitoramento de solo e água subterrânea", False),
    ("p17.¶2", "tecnico", "atividades de apoio: abastecimento veicular e oficina", False),
    ("p17.¶3", "tecnico", "abastecimento veicular: tanques e bacia de contenção", False),
    ("p17.¶4", "tecnico", "área de abastecimento: canaletas, tanque estanque, destinação classe I", False),
    ("p17.¶5", "rodape", "marca de captura eletrônica", False),
    ("p18.¶1", "tecnico", "oficina de manutenção: contenção e piso impermeável", False),
    ("p18.¶2", "tecnico", "aspectos construtivos da UPM: escritório e refeitório fora da área; componentes da UPM", True),
    ("p19.¶1", "tecnico", "impermeabilização do piso e cobertura contra água de chuva", False),
    ("p19.¶2", "dispoe", "localização: verificar captações de água e distância de segurança; indeferimento em risco iminente", True),
    ("p20.¶1", "dispoe", "captação e reuso de águas pluviométricas (Lei estadual 6.295/2000)", False),
    ("p20.¶2", "dispoe", "citação do art. 4º da Lei 6.295/2000", False),
    ("p20.¶3", "dispoe", "citação do art. 7º da Resolução AGERH 058/2017", False),
    ("p20.¶4", "dispoe", "citação do art. 8º da Resolução AGERH — reuso, reaproveitamento e reciclagem de água", False),
    ("p20.¶5", "tecnico", "área total da empresa: cercamento, cortina vegetal, drenagem pluvial", False),
    ("p21.¶1", "rodape", "abertura da seção 9, legislações pertinentes", False),
    ("p21.¶2", "tecnico", "leis e decretos aplicáveis — PNMA, PNRS, leis estaduais", True),
    ("p21.¶3", "tecnico", "resoluções CONAMA 237, 23, 307 e 313", True),
    ("p22.¶1", "tecnico", "resoluções CONAMA 382, 001, 428, 420, 430 e 357", True),
    ("p22.¶2", "tecnico", "resoluções AGERH", False),
    ("p22.¶3", "tecnico", "normas ABNT aplicáveis (início)", False),
    ("p23.¶1", "tecnico", "normas ABNT aplicáveis (continuação), incluindo NBR 10004, 12235 e 11174", False),
    ("p23.¶2", "rodape", "marca de captura eletrônica", False),
    ("p24.¶1", "tecnico", "instruções normativas, entre elas a IN Ibama 5/1992, a IN 6/2014 (RAPP) e a IN 12/2018 (CTF)", True),
    ("p24.¶2", "tecnico", "Portaria Interministerial 292/1989", True),
    ("p24.¶3", "rodape", "abertura da seção 10, documentos técnicos", False),
    ("p25.¶1", "tecnico", "documentos técnicos exigidos: plano de controle ambiental, laudos, certificados", False),
    ("p25.¶2", "discussao", "seção 11: as condicionantes padrão do Iema, exemplificativas e não exaustivas", True),
    ("p26.¶1", "formulario", "modelo de condicionante: identificação do empreendimento e escopo da licença", False),
    ("p26.¶2", "formulario", "quadro de quantidades: madeira comercializada m³/mês", False),
    ("p26.¶3", "rodape", "marca de captura eletrônica", False),
    ("p27.¶1", "formulario", "quadro de quantidades: madeira em galpão", False),
    ("p27.¶2", "formulario", "quadro de quantidades: madeira em área externa", False),
    ("p27.¶3", "formulario", "quadro de quantidades: dias de funcionamento", False),
    ("p27.¶4", "dispoe", "condicionantes 6 a 11: 15 dias de fixação em área impermeabilizada e coberta; proibição de comercializar antes da cura; proibição de misturar com madeira não tratada; laudo de impermeabilização; neutralizante para derrame", True),
    ("p28.¶1", "dispoe", "condicionantes 12 a 18: armazenamento de químicos com contenção e FISPQ; proibição de manipular sem piso impermeável; bombeamento da bacia ao tanque de solução; efluente 100% reutilizado", True),
    ("p29.¶1", "dispoe", "condicionantes 18 (fim) a 22: «em caso de necessidade de descarte, somente poderá ser realizado em empresas devidamente licenciadas para o recebimento de resíduos Classe I», com comprovantes ao Iema; vedação de lançamento em rio, esgoto ou rede pluvial sem autorização; poços e plano de monitoramento", True),
    ("p30.¶1", "dispoe", "condicionantes 23 a 27: relatório conclusivo de solo (CONAMA 420); MTR e CDF (Portaria MMA 280/2020); inventário SINIR, que «considera-se resíduo sólido também ... líquido (efluentes industriais)»; armazenamento de resíduos contaminados", True),
    ("p31.¶1", "dispoe", "condicionantes 28 a 33: devolução de bombonas, venda de resíduo só de madeira não preservada, destinação do resíduo da neutralização, NBR 11174 e 12235", True),
    ("p32.¶1", "dispoe", "condicionantes 37 a 43: RAPP ao Ibama, cadastro como usina conforme IN Ibama 5/1992, inspeção de vaso de pressão, treinamento de funcionários, emissões", True),
    ("p33.¶1", "dispoe", "condicionantes 44 e 45: cercamento e cortina vegetal; título do Quadro 01", False),
    ("p34.¶1", "discussao", "considerações finais: preservantes «altamente tóxicos, com rígido controle de comercialização e uso no Brasil»; e, no modelo licenciado, o efluente é recirculado e não há lançamento — «aspecto ambiental muito relevante em outras atividades»", True),
    ("p35.¶1-p35.¶8", "cabecalho", "equipe técnica do GGE/COED", False),
    ("p36.¶1-p36.¶2", "cabecalho", "assinaturas eletrônicas e informações de captura do documento", False),
]

# ------------------------------------------- ABPM / FG4mad 2016 (apresentação setorial)
CLASSIFICACAO["abpm-fg4mad-destinacao-residuos-madeira-tratada"] = [
    ("p1.¶1", "cabecalho", "título da apresentação: «Destinação de Resíduos de Madeira Tratada»", False),
    ("p2.¶1", "discussao", "o que é madeira tratada; NBR 16.143 (categorias de uso); tratamento por vácuo-pressão em autoclave, «sistema fechado», controle de processo e CQ pós-tratamento", True),
    ("p3.¶1", "discussao", "regulamentação citada pela própria cadeia: «Portaria Interministerial – PI 292 – 1989» e «Instrução Normativa – IN 05 – 1992», mais o conjunto de NBRs", True),
    ("p4.¶1", "tecnico", "NBR 16.143: categorias de uso, do interior de construções à exposição a água salgada", False),
    ("p5.¶1", "discussao", "resíduo de madeira tratada vem de sobras e substituições, e está sujeito às regras de resíduo sólido perigoso", True),
    ("p6.¶1", "discussao", "programa de autorregulamentação QUALITRAT: qualidade, legalidade, mercado", False),
    ("p7.¶1", "discussao", "QUALITRAT: concebido pelo Instituto Totum, auditoria do IPT, gestão da ABPM", False),
    ("p8.¶1", "discussao", "QUALITRAT é adesão VOLUNTÁRIA; itens auditáveis: habilitação, qualidade, gestão ambiental, regularidade trabalhista, saúde e segurança", True),
    ("p9.¶1", "discussao", "orientações de aquisição e uso: procedência, tipos de madeira e de tratamento, referenciais de qualidade e legalidade", False),
    ("p9.¶2", "discussao", "seção II — minimizando a produção de resíduos na obra", False),
    ("p10.¶1", "discussao", "recomendações de obra: partículas inaladas ou acumuladas em roupas; óculos, touca e máscara contra pó; lavar roupa separadamente", True),
    ("p10.¶2", "discussao", "seção III — durante as obras, recomendações além da disposição de resíduos", False),
    ("p11.¶1", "discussao", "responsabilidades do gerador, transportador, triagem, tratamento e destinação; CONAMA 307/2002 e legislações locais; base técnica em normas ABNT", True),
    ("p11.¶2", "discussao", "seção IV — destinação", False),
    ("p12.¶1", "dispoe", "a lista do «não podem»: contato com alimentos/água potável, cama para animais, queima a céu aberto ou em fogões, churrasqueiras, fornos e caldeiras de baixa temperatura; formas de destinação — ATT, ecopontos de 1 m³, reutilização, reciclagem, recuperação energética, aterros Classe IIA ou I", True),
    ("p12.¶2", "discussao", "seção IV — destinação", False),
    ("p13.¶1", "tecnico", "as regras do jogo: estimar volume, amostrar, caracterizar, e as normas aplicáveis — CONAMA 307/2002, NBR 10004/10005/10006/10007, NBR 13896, NBR 10157", True),
    ("p13.¶2", "discussao", "seção IV — destinação", False),
    ("p14.¶1", "tecnico", "NBR 10004:2004, Classe I: inflamabilidade, corrosividade, reatividade e patogenicidade N.A.; a classificação vem da TOXICIDADE dos extratos, Anexo F", True),
    ("p14.¶2", "discussao", "seção IV — destinação", False),
    ("p15.¶1", "tecnico", "NBR 10004:2004, Classe II A (não inerte) e II B (inerte), com o critério de solubilização", False),
    ("p15.¶2", "discussao", "seção IV — destinação", False),
    ("p16.¶1", "tecnico", "destino por classe: aterro Classe I para perigoso; IIA e IIB para não perigosos", True),
    ("p16.¶2", "discussao", "seção IV — destinação", False),
    ("p17.¶1", "dado", "volume anual de madeira tratada no Brasil: 2,0 milhões de m³ (estimativa), 85% eucalipto roliço; EUA 25,0 milhões; e o contraste — nos EUA há legislação estadual, rotulagem que identifica o tratamento «útil no manuseio e descarte nas obras» e regras claras de disposição", True),
    ("p18.¶1", "discussao", "identificação da madeira tratada nos EUA: rótulo na origem, reagentes químicos, raio-X portátil", True),
    ("p19.¶1", "discussao", "forma de destinação: reuso", False),
    ("p20.¶1", "discussao", "o que é a ABPM: fórum setorial, convênio com o IPT, participação na elaboração de normas, divulgação ao mercado", False),
    ("p21.¶1", "cabecalho", "contato e agradecimento", False),
]

# ---------------------------------------------- Portaria Normativa Ibama 151/97 (DOU)
CLASSIFICACAO["pn151-ibama-registro-risco-ambiental"] = [
    ("p1.¶1", "rodape", "OCR da página do DOU: cabeçalho do MMA, formulário de auto de infração e abertura da Portaria 151/97 — considerandos sobre determinação do risco ambiental", False),
    ("p1.¶2", "dispoe", "art. 1º: o registro do preservativo exige a documentação do art. 5º da Portaria 292/89 E do inciso II, alíneas b, d e da IN 05/92 — prova de que a IN é o instrumento operante", True),
    ("p1.¶3-p1.¶9", "dispoe", "art. 2º e §§: o dossiê vai em volumes separados por sessão (C, D, E, F, G), na ordem do anexo 3, item 11, da IN 05/92; justificativa técnica para teste não apresentado", True),
    ("p1.¶10-p1.¶11", "dispoe", "arts. 3º e 4º: 30 dias para complementar documentação, sob pena de arquivamento e cancelamento do registro", False),
    ("p1.¶12-p1.¶15", "rodape", "ruído de digitalização: boleto bancário, UFIR, multas, ficha de compensação", False),
    ("p1.¶16", "rodape", "fim da 151/97 (art. 5º, vigência, assinatura de Eduardo de Souza Martins) e início da Portaria 152/97, sobre formulários de infração", False),
    ("p1.¶17-p1.¶20", "rodape", "Portaria 152/97: aprovação dos formulários de auto de infração, termo de apreensão e embargo — não é norma de preservativo", False),
]

# ------------------------------------------- UFSM / Ciência Florestal 2025 (CCA-C)
CLASSIFICACAO["ufsm-ciencia-florestal-cca-moiroes-solo"] = [
    ("p1.¶1", "cabecalho", "título, autoria, licença CC BY e resumo em inglês: As na madeira −55,0%, no solo +129,2%, 32,3% acima do valor de investigação agrícola da CONAMA 420/2009", True),
    ("p2.¶1", "discussao", "resumo em português e introdução: lixiviação do CCA, contaminação de solo e água, tratamento por vácuo-pressão em autoclave industrial", True),
    ("p3.¶1", "discussao", "introdução: 1,4 milhão de m³ de madeira tratada em 2018 (IBÁ); «no Brasil, não há restrições ao uso de CCA» (Vidal et al., 2015); Cu limita crescimento de plantas", True),
    ("p4.¶1", "tecnico", "métodos: área em Frederico Westphalen/RS, janeiro de 2018 a junho de 2020, delineamento 6 × 2, cinco repetições", False),
    ("p5.¶1", "tecnico", "métodos: cinco moirões de Eucalyptus spp. de 1,5 m, 40 cm enterrados, tratados em autoclave industrial com CCA-C a 6,5 kg m⁻³", True),
    ("p6.¶1", "tecnico", "métodos: secção transversal antes e depois; solo a 5 cm do moirão, em 0–20 e 20–40 cm, seis amostragens", False),
    ("p7.¶1", "tecnico", "métodos analíticos (NBR 16137, fluorescência de raios X) e primeiro resultado: na madeira, As 3.698→1.662 (−55,0%), Cr 2.407→1.330 (−44,7%), Cu 1.068→512 (−52,0%)", True),
    ("p8.¶1", "dado", "resultado no solo: Cr 175,3→122,7 (−30%) e Cu 171,2→142,7 (−17%) CAÍRAM; só o As subiu, 20,2→46,3 (+129,2%)", True),
    ("p9.¶1", "dado", "resultado por período e profundidade: As aumenta entre 1 e 94 dias, cai até 460 e volta a subir até 880", False),
    ("p10.¶1", "discussao", "discussão: As lixivia no sentido longitudinal e é mais móvel que Cr e Cu; Jankowsky e Takeshita (2011) em ensaio de 30 anos", True),
    ("p11.¶1", "discussao", "discussão: contaminação maior junto do poste; metais retidos na superfície do solo argiloso; As acumula e pode ser absorvido por plantas", True),
    ("p12.¶1", "dado", "Tabela 1: valores de investigação da CONAMA 420/2009 — agrícola As 35, Cu 200, Cr 150 mg/kg — e os valores aos 880 dias", True),
    ("p12.¶2", "dado", "valores medidos aos 880 dias: As 46,3, Cu 147,0, Cr 122,7 mg/kg", True),
    ("p13.¶1", "dado", "comparação: As 32,3% ACIMA do agrícola; Cr 18,2% e Cu 28,6% ABAIXO; abaixo também de residencial e industrial", True),
    ("p14.¶1", "discussao", "conclusão e início das referências", True),
    ("p15.¶1", "rodape", "referências bibliográficas", False),
    ("p16.¶1", "rodape", "contribuição de autoria, ORCID e como citar", False),
]

# --------------------------------------------------- Portaria Interministerial 292/89
CLASSIFICACAO["pi292-preservativos-registro"] = [
    ("p1.¶1-p1.¶2", "cabecalho", "título e preâmbulo: Fazenda, Saúde e Interior criam «sistemática integrada» de disciplina da preservação de madeiras", False),
    ("p1.¶3", "dispoe", "art. 1º: empresas que se dediquem «à indústria e comércio» de preservativos são obrigadas ao registro no Ibama", True),
    ("p1.¶4-p1.¶12", "dispoe", "art. 1º, parágrafo único, alíneas a a i: dados do pedido — constituição, planta, combate a incêndio, capacidade, responsável técnico, licença de operação do órgão ambiental", True),
    ("p1.¶13", "dispoe", "art. 2º: relatórios semestrais de produção mensal de cada produto", True),
    ("p1.¶14", "dispoe", "art. 3º: preservativo e ingredientes ativos só podem ser «fabricados, consumidos ou postos à venda» depois de registrados, inclusive importados", True),
    ("p1.¶15-p1.¶16", "dispoe", "art. 3º §§: informação periódica à CACEX sobre importação permitida; definição de ingrediente ativo", False),
    ("p1.¶17", "dispoe", "art. 4º — a exceção: «Não estão sujeitos ao registro no IBAMA os preservativos que forem destinados à experimentação e ao uso domissanitário»", True),
    ("p1.¶18-p1.¶24", "dispoe", "art. 5º, alíneas a a f: memorial descritivo do produto — requerimento, prova de registro da empresa, fabricante, marca, nome químico, fórmula bruta", True),
    ("p2.¶1-p2.¶8", "dispoe", "art. 5º, alíneas g a o: composição, características, «instruções para uso, incluindo precauções na manipulação», modelo de rótulo, certidões toxicológica e de risco ambiental, análise química e comprovação de eficiência", True),
    ("p2.¶9-p2.¶10", "dispoe", "arts. 6º e 7º: o Ibama examina o memorial e pode fazer ensaios; marca registrada no INPI", False),
    ("p2.¶11-p2.¶14", "dispoe", "art. 8º: classificação das usinas — sob pressão, sem pressão, piloto", False),
    ("p2.¶15-p2.¶27", "dispoe", "art. 9º: dados do registro da usina — capacidade técnica, classificação, equipamento, preservativos usados, responsável técnico, licença de operação", True),
    ("p3.¶1-p3.¶8", "dispoe", "art. 10: dados do registro da usina piloto", False),
    ("p3.¶9-p3.¶14", "dispoe", "art. 11: relatório semestral da usina — gêneros/espécies, tipo e dimensões, «volume de madeira tratada mensalmente», concentração e consumo mensal de preservativo", True),
    ("p3.¶15-p3.¶17", "dispoe", "arts. 12 a 14: normas Conmetro para equipamentos; alteração de dados; cadastro obrigatório de usuárias e do comércio, inclusive importadoras", True),
    ("p3.¶18-p3.¶27", "dispoe", "art. 15: dados obrigatórios de rótulo E bula — marca, nº de registro, composição, características, instruções de uso, classificação de risco, precauções e primeiros socorros. O destino do resíduo NÃO está aqui", True),
    ("p3.¶28-p3.¶30", "dispoe", "arts. 16 a 18: uso da expressão «recomendado», vedação de propaganda enganosa, validade de 5 anos do registro", False),
    ("p4.¶1-p4.¶4", "dispoe", "arts. 19 a 22: fiscalização «por ocasião da instalação»; art. 20 — «O IBAMA fiscalizará as atividades relacionadas com a preservação e comércio»; art. 21 medidas de correção; art. 22 sanções", True),
    ("p4.¶5-p4.¶7", "dispoe", "arts. 23 a 25: prazos de regularização, atos complementares, vigência e revogação das Portarias 2.748-DN/72 e 5-P/82", False),
    ("p4.¶8-p4.¶10", "cabecalho", "assinaturas dos três ministros, «(DOU de 02.05.1989)» e nota sobre a criação da SECEX", False),
]

# ----------------------------------------------------------------- IN Ibama 5/92
CLASSIFICACAO["in05-ibama-destinacao-final-residuos"] = [
    ("p1.¶1-p1.¶4", "cabecalho", "título, preâmbulo de atribuições e o RESOLVE: disciplinar a Portaria 292/89", False),
    ("p1.¶5-p1.¶13", "definicao", "item I, «Das definições»: indústria, usina (sob pressão / sem pressão / piloto), produto, importador, comércio (varejo E atacado), usuário", True),
    ("p2.¶1-p2.¶2", "definicao", "fim das definições (nome químico, fabricação de equipamentos) + notas de rodapé dos decretos revogados", False),
    ("p2.¶3-p2.¶11", "dispoe", "item II, «Do registro»: quem é obrigado; documentação; «modelo de bula» exigido junto ao registro do produto; vedação de registro por similaridade", True),
    ("p3.¶1-p3.¶5", "dispoe", "item III, «Do cadastro»: importador, comércio e usuário cadastram-se (art. 14 da Portaria); formulário pede consumo médio mensal do usuário; fracionamento/reembalagem equipara-se a indústria", True),
    ("p3.¶6-p3.¶8", "dispoe", "item IV, «Da renovação»: cadastro anual, registro com 6 meses de antecedência", False),
    ("p3.¶9-p3.¶10", "dispoe", "item V, «Do prazo»: 60 dias para anexar documentação aos processos em tramitação", False),
    ("p3.¶11-p3.¶16", "dispoe", "item VI, «Da embalagem e rotulagem»: não-reaproveitamento em destaque, anuência para venda a granel, três colunas", True),
    ("p4.¶1-p4.¶8", "dispoe", "item VI, colunas do rótulo: dados obrigatórios, classificação toxicológica do Ministério da Saúde, «é obrigatório o uso de equipamentos de segurança», faixa colorida e caveira «CUIDADO - VENENO»", True),
    ("p5.¶1-p5.¶4", "dispoe", "item VI: legibilidade, impressão direta, rótulo de importado em português", False),
    ("p5.¶5-p5.¶15", "dispoe", "item VI, «h», a BULA: concentração, modo de aplicação, limitações, equipamentos de aplicação, EPI, e o item 6 — «informações sobre o destino final das embalagens e dos resíduos»; dados de saúde humana e de meio ambiente", True),
    ("p5.¶16-p5.¶19", "dispoe", "item VII, «Da comercialização»: organoclorados só em venda direta entre produtor/importador e consumidor (usina/usuário); prazo de 90 dias para o varejo escoar estoque; recolhimento posterior", True),
    ("p5.¶20-p5.¶21", "dispoe", "item VIII, «Da destinação final de resíduos e embalagens»: proibição de reutilizar embalagem para outra finalidade", True),
    ("p6.¶1-p6.¶3", "dispoe", "item VIII: autorização de reaproveitamento pela produtora; «c» — o descarte da embalagem e dos resíduos «deverá atender às recomendações técnicas apresentadas na bula»; tambores amassados e perfurados", True),
    ("p6.¶4-p6.¶19", "dispoe", "item IX, «Das disposições gerais»: taxas DUA por categoria, relatórios semestrais (art. 2º e 11 da Portaria), importação, ensaios adicionais", False),
    ("p7.¶1-p7.¶4", "dispoe", "fim do item IX: normas estrangeiras por 2 anos, pedidos separados, documentação de testes em português, 180 dias para avaliar", False),
    ("p7.¶5-p7.¶6", "cabecalho", "assinatura do presidente Humberto Cavalcante Lacerda e «(DOU de 21.10.92)»", False),
    ("p8.¶1-p8.¶5", "formulario", "Anexo 1 — modelo de requerimento de registro de empresa", False),
    ("p9.¶1-p9.¶5", "formulario", "Anexo 2 — modelo de requerimento de registro de produto, com a Certidão de Risco Ambiental", False),
    ("p10.¶1-p10.¶6", "tecnico", "Anexo 3 — documentação da certidão de risco ambiental: marca, nome químico, fórmula, classe e grupo químico do ingrediente ativo", False),
    ("p10.¶7-p10.¶10", "dispoe", "Anexo 3, itens 6 a 8: registro em outros países, métodos de aplicação e — item 8 — «indicações de uso para madeira tratada»", True),
    ("p10.¶11-p10.¶12", "dispoe", "Anexo 3, itens 9 e 10: «métodos para desativação do ingrediente ativo» e medidas de emergência em acidente ambiental", True),
    ("p10.¶13-p13.¶1", "tecnico", "Anexo 3, item 11: testes de ecotoxicidade exigidos — físico-químicos (C), organismos aquáticos e do solo (D), degradação e transporte (E: biodegradabilidade, mobilidade, adsorção/dessorção), mamíferos (F), mutagenicidade e carcinogenicidade (G)", True),
    ("p13.¶2", "dispoe", "Anexo 3: prazo de 5 anos para os testes lentos; justificativa por escrito na impossibilidade; carta compromisso empresa/Ibama", False),
    ("p14.¶1-p14.¶8", "formulario", "Anexo 4 — relatório semestral de produção e comércio da indústria (produto, cliente, quantidade vendida)", True),
    ("p15.¶1-p15.¶8", "formulario", "Anexo 5 — relatório semestral de consumo e produção da usina: preservativo, concentração, consumo, e da madeira tratada — gênero/espécie, tipo, dimensão, volume", True),
]


# ------------------------------------------- CTF/Ibama — conversão de índice para id
# Página de uma só página: o parágrafo ¶N corresponde ao índice N-1 da extração.
_CTF_DOC = "ctf-ibama-categorias-preservativos"
CLASSIFICACAO[_CTF_DOC] = [
    (f"p1.¶{a + 1}" if a == b else f"p1.¶{a + 1}-p1.¶{b + 1}", c, t, r)
    for a, b, c, t, r in _CTF_FAIXAS
]
