# Parecer de auditoria — Gaveta BORO

**Task:** BORO-AUDITORIA-INTRODUTORIA-20261124-R1  
**Auditor declarado:** CODEX_LUNA_MEDIUM / TECO  
**Veredito global:** **REPLANEJAR**

## Base e limite da auditoria

O contrato fixa a gaveta em `383b0be` e o handoff em `2899553`; o pedido identifica `2899553` como HEAD. Auditei os quatro artefatos pelos blobs de `2899553` e li também `BOOTSTRAP_COBRE_20261124.md`. No checkout observado, a branch está em `c56ad64`, com alterações locais posteriores nos arquivos BORO e outros arquivos. Por isso, este parecer separa os artefatos do snapshot auditado de material que só aparece no estado local posterior.

Não alterei os artefatos auditados. O veredito decorre de defeitos de interpretação e de proveniência: a seção central de lixiviação omite evidência direta já custodiada; os números de retenção são comparados em bases diferentes e tratados como prática de campo; e as lacunas de exposição, suplemento e importação precisam ser delimitadas por data e por objeto.

## Achados

### A1 — MATERIAL — a lacuna ocupacional precisa ser delimitada; ausência de dado sobre bambu não prova prática sem EPI

**Onde:** `00-estado-da-questao-boro.md`, §9, especialmente “Interpretação curatorial”; `HANDOFF_BORO_20261124.md`, §§8.2 e 12.

**O que o executor diz:** “é o vácuo em que a prática sem EPI se instala.”

**Por que está fraco:** Há fonte toxicológica oficial com medições ocupacionais de poeira de boratos em trabalhadores de produção/manuseio de borax e sintomas respiratórios. A extração local de ATSDR resume estudos com concentrações de poeira e boro no ar e maior frequência de irritação nasal, ocular e de garganta nos grupos expostos. Isso derruba a formulação ampla de que não há material ocupacional sobre boro no acervo e dá contexto de perigo por inalação. Não mede, porém, operadores de preservação de bambu no Brasil ou na China, nem uso de EPI nesse ofício. Portanto, a lacuna específica permanece; a afirmação sobre prática “sem EPI” não decorre dela.

**Fonte:** `_privado/governanca-operacional/extracoes/boro/fontes_novas/atsdr_tp26/ATSDR_tp26_BORON.extracao.md`; [ATSDR, Toxicological Profile for Boron](https://www.atsdr.cdc.gov/ToxProfiles/tp26.pdf).

**O que deveria dizer:** “Há dados ocupacionais de trabalhadores de produção/manuseio de boratos, usados aqui somente como analogia toxicológica. Não foram localizadas medições de exposição nem dados de EPI em operadores de tratamento de bambu com boro no Brasil ou na China. Não se infere que trabalhem sem EPI.”

### A2 — MATERIAL — a lacuna do suplemento foi derrubada no estado local; “por cápsula” e a comparação de limites estão errados

**Onde:** `00-estado-da-questao-boro.md`, §6.3 e §12, item 2; `index.md`, tabela “cinco réguas”; `HANDOFF_BORO_20261124.md`, §§5 e 8.

**O que o executor diz:** “0,15 a 6 mg de boro elementar por cápsula” e “uma cápsula de 6 mg B consome 60% do PDE adulto e duas vezes o PDE de uma criança”.

**Por que está fraco:** A ficha profissional do NIH ODS registra que quantidades comuns em suplementos variam de 0,15 a 6 mg de boro elementar. A cópia integral está agora no estado local, apesar de a extração inicial ter falhado. Ela não sustenta “por cápsula” para todo produto, nem estabelece uma dose brasileira ou frequência de consumo. A divisão 6/10 e 6/3 está aritmeticamente correta, mas o PDE citado pelo EMA é uma exposição permitida para boro usado como excipiente em medicamentos; não deve ser chamado de limite geral de segurança de suplemento ou de criança. Comparar valores como razão pode ser informativo se a base e o contexto forem explicitados, sem converter a razão em conclusão de risco.

**Fonte:** `_privado/governanca-operacional/extracoes/boro/fontes_novas/nih_ods/NIH_ODS_Boron_HealthProfessional_20261116.extracao.md`, linha 194 da extração; [NIH ODS — Boron, Health Professional Fact Sheet](https://ods.od.nih.gov/factsheets/Boron-HealthProfessional/).

**O que deveria dizer:** “O NIH ODS relata 0,15–6 mg de boro elementar em suplementos. Isso não identifica a dose por cápsula nem um produto brasileiro específico. O valor de 6 mg equivale numericamente a 60% do PDE adulto do EMA, mas PDE medicinal não é UL alimentar nem recomendação de uso para crianças.” A lacuna de rótulos/produtos brasileiros continua aberta.

**Controle temporal:** o snapshot de extração atual não consta dos blobs auditados; portanto, derruba a lacuna para o estado local da auditoria, não prova que o executor já dispunha dessa cópia ao produzir R1.

### A3 — MATERIAL — importação brasileira deixou de ser “não iniciada” no estado local posterior

**Onde:** `HANDOFF_BORO_20261124.md`, §8.1 e §§12–13; `00-estado-da-questao-boro.md`, §12, item 1.

**O que o executor diz:** “Nenhum dado brasileiro foi extraído ainda” e “não iniciado”.

**Por que está fraco:** Essa descrição é compatível com o snapshot do handoff auditado, mas já não descreve o workspace observado: existe `docs/analyses/boro/01-importacao-brasileira-boro-comexstat.md`, com consulta à API oficial do ComexStat para os NCM 2528, 2810 e 2840, série 1997–2026. O arquivo informa que peso líquido é peso do produto comercial, não massa de boro elementar, e que 2026 é parcial. Seus resultados não devem ser tratados como se fossem parte do commit auditado nem como medição direta do consumo de boro elementar.

**Fonte:** `docs/analyses/boro/01-importacao-brasileira-boro-comexstat.md` e dados privados em `_privado/governanca-operacional/extracoes/boro/fontes_novas/comexstat/`.

**O que deveria dizer:** Atualizar o handoff no próximo estado da gaveta e marcar a extração como posterior ao snapshot auditado. Usar os dados com os limites NCM, nomenclatura e peso comercial declarados, sem afirmar equivalência de massa entre minério, ácido bórico e borax.

### A4 — BLOQUEANTE — a tese de lixiviação omite evidência direta de borato e usa Rusch 2023 para um elemento que o estudo não mediu

**Onde:** `00-estado-da-questao-boro.md`, §7 e §10, itens 2–3.

**O que o executor diz:** “A evidência direta de lixiviação medida é em CCB” e “ele mostra que o problema de mobilidade é de família”.

**Por que está errado:** Rusch et al. mediram cobre e cromo nos colmos; o artigo não apresenta medição de boro. Logo, essa pesquisa não é evidência direta de lixiviação de boro, nem sustenta por si só mobilidade de “família” do boro. Mais grave, a tese Gauss 2020 já custodiada inclui ensaio de lixiviação em material tratado somente com DOT: o tratamento B5 perdeu 82,4% do boro no ensaio severo. A própria tese registra que a lixiviação severa eliminou a atividade fungicida do tratamento OST. É evidência laboratorial direta, com limite experimental claro, que deveria formar o núcleo desta seção.

**Fonte:** `_privado/fontes-academicas/2020-gauss-tratamento-preservativo-modificacao-quimica/extracao.md`, pp. 10 e 192–193, Tabela 4.7; ficha em `docs/analyses/bambu-estrutural/gauss-2020-tratamento-preservativo-modificacao-quimica.md`; [tese Gauss, DOI 10.11606/T.74.2020.tde-12042021-165453](https://doi.org/10.11606/T.74.2020.tde-12042021-165453). Para o limite do estudo de campo CCB, ver `_privado/governanca-operacional/extracoes/boro/herdado/ago_28_CCA_CCB/md/Rusch_2023_CCB_Bambu.md`, pp. 100–101, que identifica as medições como cobre e cromo.

**O que deveria dizer:** “Em ensaio laboratorial severo, amostras de bambu tratadas apenas com DOT perderam 82,4% do boro; isso demonstra vulnerabilidade à lixiviação naquela formulação e protocolo, não uma taxa universal de perda em serviço. Rusch et al. mediram Cu e Cr em bambu tratado com CCB e entram apenas como contraste de campo; não demonstram lixiviação de B.”

### A5 — MATERIAL — “3–8 vezes” mistura massa de DOT com equivalentes de B₂O₃ e extrapola laboratório para campo

**Onde:** `00-estado-da-questao-boro.md`, §6.5 e §10, item 3; `index.md`, tabela das réguas.

**O que o executor diz:** “14,79 e 21,79 kg/m³ — de três a oito vezes a recomendação normativa” e “a prática documentada”.

**Por que está errado/fraco:** Os valores 14,79 e 21,79 kg/m³ são retenções teóricas de DOT seco calculadas a partir da absorção de solução em amostras de *Dendrocalamus asper*. A tese também fornece a base equivalente de B₂O₃: 9,98 e 14,71 kg/m³. Os valores AWPA 2,7 e IS 401 5 são expressos como retenção de B₂O₃ e referem-se a aplicações internas em madeira. A conta “3–8” divide as retenções brutas de DOT por dois limites de B₂O₃ e cruza extremos diferentes. Com a base B₂O₃, as razões seriam 3,7–5,4 contra 2,7 e 2,0–2,9 contra 5; são comparações indicativas com referências para madeira, não limites validados para bambu. O ensaio de laboratório não demonstra prática de campo nem que aplicadores desconheçam a retenção.

**Fonte:** Gauss, tese, p. 88–89 (retenção DOT e equivalentes de B₂O₃; padrões citados para madeira), e tabela 4.7; mesma ficha e DOI citados em A4.

**O que deveria dizer:** Separar massa de DOT, B₂O₃ equivalente e boro elementar. Apresentar os valores medidos como resultados de laboratório em *D. asper*, e as normas de madeira como comparadores externos, não como recomendação para bambu. Remover “prática de campo”, “excesso” e “dosado às cegas” até existir levantamento de campo.

### A6 — MATERIAL — a descrição de classificação reprodutiva está desatualizada para o CLP vigente

**Onde:** `00-estado-da-questao-boro.md`, §6.2; `HANDOFF_BORO_20261124.md`, §5.

**O que o executor diz:** “ácido bórico e boratos foram classificados como […] CMR Repr. cat. 2”.

**Por que está fraco:** Isso reproduz uma classificação mencionada no documento EMA de 2021, mas não descreve a classificação harmonizada atual no CLP europeu para ácido bórico: Repr. 1B, H360FD. Entradas harmonizadas também incluem determinados boratos. A diferença de categoria é material para um capítulo que usa classificação regulatória como argumento toxicológico. Deve-se distinguir o texto histórico/regulatório do EMA da classificação CLP vigente e especificar a substância, pois “boratos” não deve ser tratado como uma classe química uniforme sem identificar os compostos.

**Fonte:** [Regulamento Delegado (UE) 2023/1435, EUR-Lex](https://eur-lex.europa.eu/eli/reg_del/2023/1435/oj/eng); [ECHA, classificação harmonizada do ácido bórico](https://echa.europa.eu/documents/10162/17233/annex_5_tpp_odd_extract_from_annex_vi_of_clp_en.pdf/277bd887-b9e4-4d63-a097-2994b74a8870?t=1430229331560).

**O que deveria dizer:** “O documento EMA de 2021 cita Repr. categoria 2 no enquadramento então usado. No CLP harmonizado vigente, o ácido bórico está classificado como Repr. 1B, H360FD; a classificação de cada borato deve ser verificada por composto.” Não confundir toxicidade reprodutiva com carcinogenicidade.

### A7 — MATERIAL — a concentração geopolítica sustenta risco de suprimento dos EUA, não uma tese geral de insustentabilidade

**Onde:** `00-estado-da-questao-boro.md`, §4; `HANDOFF_BORO_20261124.md`, §§5 e 8.

**O que o executor diz:** “O que é insustentável […] é a concentração geopolítica” e “sob controle estatal de um fornecedor dominante”.

**Por que está fraco:** A USGS diz que os recursos mundiais são adequados ao consumo previsível e informa que 90% das importações norte-americanas vieram da Turquia em 2021–2024. Isso sustenta vulnerabilidade de suprimento para o mercado dos EUA, não que a cadeia global ou brasileira seja, sem métrica adicional, “insustentável”. A soma de reservas também não pode ser calculada de modo consistente segundo a própria USGS; o texto reconhece esse limite, mas a participação turca calculada sobre o subtotal listado não deve ser apresentada como parcela das reservas mundiais. A análise ComexStat posterior aponta perfil brasileiro diferente, com origem regional relevante.

**Fonte:** [USGS, Mineral Commodity Summaries 2026 — Boron](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-boron.pdf); `docs/analyses/boro/01-importacao-brasileira-boro-comexstat.md` (estado posterior, com limites metodológicos).

**O que deveria dizer:** Trocar “insustentabilidade” por hipótese delimitada de risco de concentração de suprimento, identificar o mercado analisado e medir concentração por país/forma do produto. Manter “recursos adequados ao futuro previsível” separado de risco logístico/geopolítico.

### A8 — MATERIAL — cinco categorias são úteis, mas “nenhuma converte” é falso e agricultura não tem dose

**Onde:** `00-estado-da-questao-boro.md`, §§2 e 6; `index.md`, tabela “as cinco réguas”.

**O que o executor diz:** “as três escalas […] nenhuma converte na outra”; no index, “Nenhuma converte na outra.”

**Por que está errado/fraco:** A ficha lista cinco tópicos, embora §6 anuncie três. Há conversões químicas explícitas no próprio texto: B ↔ H₃BO₃ e DOT ↔ B₂O₃ equivalente. O que não é intercambiável sem condições adicionais são os critérios de segurança/desempenho, vias, alvos e denominadores. Além disso, os 11–15% do consumo mundial atribuídos a fertilizantes são participação de mercado, não uma dose agronômica em kg B/ha; o index chama essa linha de “kg/ha” sem fornecer um valor. A separação entre normas de exposição humana e retenção de material é válida, mas a fórmula absoluta “não converte” oculta conversões de massa úteis e não resolve a comparabilidade toxicológica.

**Fonte:** a própria ficha §§2, 6.2, 6.4–6.5; [USGS MCS2026](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-boron.pdf).

**O que deveria dizer:** Organizar cinco bases declaradas — concentração da solução; dose oral diária de B; teor de B no rótulo por porção; dose agronômica por área; retenção do preservante por volume — e indicar quais conversões químicas são possíveis. Declarar que seus limites normativos não são substituíveis. Não chamar participação do consumo de “dose agrícola”.

### A9 — MATERIAL — “dose de campo desconhecida” é uma hipótese, não um achado de Gauss

**Onde:** `00-estado-da-questao-boro.md`, §§6.5 e 10; `index.md`, descrição da régua de bambu.

**O que o executor diz:** “quem aplica banho por percentagem de solução não sabe sua retenção real” e “dosado às cegas”.

**Por que está fraco:** Gauss mediu absorção/retensão em protocolos de laboratório para espécies e corpos de prova específicos. A tese não acompanhou operadores, práticas comerciais ou a conversa em campo. O salto de um resultado laboratorial para a descrição de como “quem aplica” trabalha não está apoiado por pesquisa observacional. A concentração do banho, isoladamente, também não determina uma retenção universal: depende de espécie, geometria, umidade, método, tempo e absorção.

**Fonte:** Gauss, tese, pp. 88–89; ficha local em `docs/analyses/bambu-estrutural/gauss-2020-tratamento-preservativo-modificacao-quimica.md`.

**O que deveria dizer:** “Os estudos localizados não estabelecem uma retenção-alvo universal nem descrevem a distribuição das retenções em operações de campo. Isso justifica medir retenção por lote e estudar prática real; não permite afirmar que aplicadores em geral dosam às cegas.”

### A10 — MATERIAL — o histórico da Green School não prova que Stamm criou ou padronizou o método

**Onde:** `00-estado-da-questao-boro.md`, §8, título e conclusão “transformou o banho de boro em padrão de facto”.

**O que o executor diz:** “A Green School é a vitrine mundial que transformou o banho de boro em padrão de facto.”

**Por que está fraco:** O próprio texto admite Linda Garland e Walter Liese como anteriores, então não sustenta paternidade de Stamm. A documentação da Environmental Bamboo Foundation e de Walter Liese situa pesquisa e prática de preservação por boratos antes da notoriedade da Green School. A ficha não demonstra adoção internacional, nem que o banho tenha se tornado padrão de facto; descreve uma vitrine arquitetônica e um método usado em algumas obras.

**Fonte:** [Environmental Bamboo Foundation, Treatment Manual](https://www.greenb.it/wp-content/uploads/2021/06/EBF_-_TreatmentManual.pdf); [Walter Liese, Protection of Bamboo in Service](https://www.greenb.it/wp-content/uploads/2021/06/W._Liese_-_Protection_of_Bamboo_in_Service.pdf); perfil de Stamm citado na própria ficha.

**O que deveria dizer:** Usar o caso Green School como difusão/visibilidade da construção em bambu tratada, sem atribuir origem ou padronização ao profissional. A história técnica exige cronologia independente de Garland, EBF, Liese e práticas anteriores.

### A11 — MATERIAL — texto autoral adjacente converte indicador de ACV em exposição e dano humano

**Onde:** `docs/analyses/tecnologia-takwara/ensaio-bambu-sem-manejo-riscos-regulacao.md`, §§ “93%…”, “Números da Vergonha” e conclusões; contraste com `00-estado-da-questao-boro.md`, §11.

**O que o texto afirma:** “trabalhadores expostos diariamente a substâncias que podem causar câncer” e “efluentes tóxicos sendo despejados diretamente no solo”; chama os resultados de “evidência irrefutável”.

**Por que está errado/fraco:** A ficha da ACV de Araújo et al. registra 93% como parcela de impacto potencial normalizado na categoria HCT, em uma unidade produtiva e uma unidade funcional. O estudo não mediu exposição ocupacional, dose absorvida, incidência de câncer, contaminação de nascentes ou prevalência de descarte direto no solo. A ficha local deixa esses limites explícitos. A classificação reprodutiva CLP não autoriza chamar o boro de carcinógeno humano. Este texto autoral não é evidência para a gaveta e contamina qualquer argumento que tente usar “93%” como dano real observado.

**Fonte:** `docs/analyses/bambu-estrutural/ficha-acv-bambu-unesp-araujo2025.md`; [artigo de Araújo et al. (2025)](https://periodicos.cerradopub.com.br/bjs/article/view/719); [ATSDR ToxFAQs — Boron](https://www.atsdr.cdc.gov/toxfaqs/tfacts26.pdf).

**O que deveria dizer:** Corrigir esse ensaio antes de citá-lo ou reutilizar sua narrativa: “93%” é resultado de uma categoria de impacto potencial modelada, não taxa de doença nem medição de exposição. Remover alegações de exposição diária, câncer e contaminação de corpos d’água sem fontes independentes. A ficha BORO deve manter distância explícita desse texto até a correção.

### A12 — MENOR — nicho aeroespacial é plausível; “massa desprezível” não está quantificada

**Onde:** `00-estado-da-questao-boro.md`, §5.

**O que o executor diz:** “O boro aeroespacial consome massa desprezível.”

**Por que está fraco:** A USGS confirma que mais de três quartos do consumo global se destinam a cerâmicas, detergentes, fertilizantes e vidro. Isso sustenta a refutação de que foguetes absorvam “grande parte” da oferta. Não quantifica a massa de usos aeroespaciais, nem permite converter “menos que os grandes grupos” em “desprezível”. Os percentuais de segmentos individuais já estão corretamente identificados como ordem de grandeza; mantenha essa ressalva e complete as referências do estudo europeu usado.

**Fonte:** [USGS MCS2026 — Boron](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-boron.pdf); as referências de aplicações aeroespaciais citadas no §5 documentam aplicações, não participação em massa.

**O que deveria dizer:** “Aeroespacial é uma aplicação especializada; a participação em massa não foi quantificada nas fontes consultadas.” A afirmação >3/4 é sustentada pela USGS. Também está correto atribuir à USGS as maiores jazidas economicamente viáveis em Mojave, Alpide e Andino. A afirmação astronômica sobre espalação por raios cósmicos também é compatível com Reeves, Fowler e Hoyle ([DOI 10.1038/226727a0](https://doi.org/10.1038/226727a0)).

## MATERIAL IGNORADO LOCALIZADO

- `_privado/governanca-operacional/extracoes/boro/fontes_novas/atsdr_tp26/ATSDR_tp26_BORON.extracao.md` — estudos ocupacionais de poeira de boratos e sintomas respiratórios. Muda a formulação geral de “vácuo” e fornece analogia; não fecha operadores de bambu no Brasil/China.
- `_privado/governanca-operacional/extracoes/boro/fontes_novas/nih_ods/NIH_ODS_Boron_HealthProfessional_20261116.extracao.md` — fonte primária que ancora a faixa 0,15–6 mg em suplementos; muda “não ancorado”. Não comprova dose por cápsula nem produto brasileiro.
- `docs/analyses/boro/01-importacao-brasileira-boro-comexstat.md` + `_privado/governanca-operacional/extracoes/boro/fontes_novas/comexstat/` — série oficial por NCM, adicionada após o snapshot auditado; muda “não iniciado” no estado local. O peso é produto comercial, não teor elementar de B.
- `_privado/fontes-academicas/2020-gauss-tratamento-preservativo-modificacao-quimica/extracao.md` e `docs/analyses/bambu-estrutural/gauss-2020-tratamento-preservativo-modificacao-quimica.md` — ensaio direto de lixiviação de DOT, 82,4% de perda no B5, e conversão DOT/B₂O₃ que corrige a comparação de retenção.
- `_privado/governanca-operacional/extracoes/advance-bamboo-science/fichas_cavichiolli_candidatas_v2/` — Mwanja et al. 2024 mede eficácia de formulações de borax/ácido bórico em espécies de bambu e discute uso protegido da lixiviação. Relevante à eficácia e ao limite de uso; não é fonte de exposição ocupacional.
- `docs/analyses/bambu-estrutural/ficha-acv-bambu-unesp-araujo2025.md` — leitura crítica da ACV, que delimita os 93% como impacto potencial modelado; contrapõe as alegações excessivas do ensaio autoral.
- `_privado/fontes-documentais/ago_28_Boratos_Cobre/` — pacote herdado misto com fontes de boratos e cobre; Liu 2023 já é citado, mas não reprocessar as dez fichas não transforma as demais em evidência automaticamente.
- `_privado/fichas/ago_28_CCA_CCB/ferrarini-2012-cca-boro-fluor-classificacao-residuos.md` e `_privado/governanca-operacional/extracoes/boro/herdado/ago_28_CCA_CCB/md/Rusch_2023_CCB_Bambu.md` — materiais úteis para contraste e destinação de resíduos CCA/CCB; não provam lixiviação de borato isolado no estudo Rusch.
- `_quarentena/ifb/ifb-boron-greenfacts.md` e `_quarentena_old/_duplicatas/BAM_boron-greenfacts.md` — resumos secundários/duplicados em quarentena; não são evidência primária nem fecham exposição de trabalhadores de bambu.
- `_privado/acervo-autoral-fabio-takwara/`, `docs/analyses/visao-do-autor/caderno-01-preservacao-socioecologica-bambu.md`, `_quarentena/`, `_quarentena_old/` e `arquivo_historico/` foram percorridos por busca dirigida. A ficha do caderno socioecológico já separa ACV potencial, exposição e dano; o ensaio de riscos/regulação citado em A11 não mantém essa separação.

## LACUNAS DERRUBADAS

1. **Dose geral de suplemento:** derrubada para a faixa geral de 0,15–6 mg em suplementos pelo NIH ODS no estado local. Não derrubada para dose por cápsula ou rótulo de produto brasileiro.
2. **Importação brasileira:** derrubada no estado local pela extração ComexStat posterior. Não faz parte do snapshot de gaveta auditado; exige incorporar os dados e preservar limites metodológicos.
3. **Existência de qualquer dado ocupacional de borato:** derrubada — ATSDR resume estudos com trabalhadores expostos à poeira de boratos.
4. **Exposição de operador de tratamento de bambu no Brasil/China:** **não derrubada**; não localizei medição direta dessa atividade.
5. **Poeira respirável de bambu tratado, cortado ou serrado, com quantificação de boro/sílica e exposição humana:** **não derrubada**. ACV de resíduos e estudos de poeira de borato industrial não medem essa exposição.

## RECOMENDAÇÃO DE RUMO

1. **Parar a progressão para homologação/publicação desta versão** até reescrever §§6–10. O recorte boro como capítulo introdutório é viável; a inferência atual não.
2. Reconstruir §7 começando pela evidência direta DOT-only da tese Gauss; manter Rusch como estudo CCB com medições de Cu/Cr, sem atribuir-lhe medição de B.
3. Refazer a comparação de retenção em base química comum, declarar que AWPA/IS são referências de madeira e que os dados são laboratoriais. Apagar “3–8 vezes” e “dosado às cegas” como conclusões sobre campo.
4. Separar cinco tipos de valor e consertar o índice: adicionar dose agrícola real por cultura/área ou retirar agricultura da lista de réguas de dosagem.
5. Atualizar a classificação CLP e a fonte NIH; integrar ComexStat como artefato posterior com data, NCM, produto comercial e limites.
6. Reescrever a tese para: eficácia biológica demonstrada em condições experimentais; lixiviação de boratos demonstrada em ensaio laboratorial e sensível à formulação/protocolo; desempenho em serviço, retenção de campo, exposição de operadores e poeira de bambu tratado ainda sem medição direta identificada. A evidência sustenta uma agenda de mensuração e gestão; não prova dano ocupacional ou ao usuário de edifícios.
7. Corrigir o ensaio autoral antes de usar sua narrativa como contexto ou justificativa para norma. Nenhuma conclusão de ACV deve ser convertida em dose, exposição ou incidência clínica sem evidência própria.

## NÃO SEI

- Não encontrei estudo que meça diretamente a exposição de operadores de preservação de bambu com boratos no Brasil ou na China; ATSDR é analogia de trabalhadores de boratos industriais.
- Não encontrei estudo que quantifique aerossol respirável de serragem/aparas de bambu tratado com boratos e determine simultaneamente boro, sílica e dose ocupacional.
- Não validei por rótulos de produtos brasileiros qual fração das doses NIH é por cápsula, por porção ou por dia.
- Não auditei a API ComexStat linha por linha contra cada resposta bruta; considerei o artefato local posterior e suas próprias ressalvas apenas para corrigir o status “não iniciado”.
- Não estabeleci a participação em massa de usos aeroespaciais nem que a Green School tenha tornado o método padrão internacional; as fontes consultadas não demonstram esses quantificadores.

---

**Conclusão:** REPLANEJAR a tese e as bases de comparação; a versão auditada não deve avançar para homologação. O defeito decisivo não é a existência de uma lacuna ocupacional específica — ela permanece —, mas a mistura entre resultado experimental e prática de campo, a omissão da lixiviação direta de DOT já disponível e a extrapolação de indicadores e referências para afirmações que as fontes não sustentam.

