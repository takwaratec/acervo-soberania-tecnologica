---
titulo: "Relatório de auditoria epistêmica — corpus autoral do eixo Bambu"
tipo_documental: instrumento-de-pesquisa
estado_documental: em-revisao-documental
responsavel_curadoria: Fabio Takwara
data_revisao: 2026-08-01
---

# Relatório de auditoria epistêmica — corpus autoral do eixo Bambu

*Fase 3 do fluxo definido em ORIENTACOES_PRE_PR_INTEGRACAO_AUTORAL_ESTADO_DA_ARTE.md (seção 13). Auditados os oito documentos autorais: Cadernos 1 a 7 e Anexo 1, todos em `docs/analyses/visao-do-autor/`. A auditoria verifica TRL e maturidade, afirmações econômicas, alegações ambientais, uso de perfis, passagens culturais e riscos de propriedade intelectual.*

## 1. TRL e maturidade

| Item | Documento | Trecho verificado | Veredicto | Recomendação |
|---|---|---|---|---|
| TRL-3 | Caderno 1 | Subtítulo: "Prova de conceito (TRL-3)"; front matter `nivel_maturidade_trl: 3`, `trl_alvo: 4`; texto: "consolida a prova de conceito (TRL-3)... com base em revisão de escopo documental de 17 fontes" | ⚠️ **ATENÇÃO** | TRL-3 exige prova de conceito validada por experimentação; a base declarada é revisão documental sem ensaio primário próprio. O TRL-3 aqui descreve maturidade da *agenda de pesquisa* (hipótese formulada a partir do acervo), não da tecnologia. Recomenda-se rebaixar para "maturidade_da_tecnologia: nao-determinada" e usar "prova de conceito analítica" com qualificador explícito. Ver item R-01 da lista de revisão. |
| TRL-7 alvo | Cadernos 1, 3 | "tem como alvo o TRL-7 (demonstração em ambiente operacional)" | ✅ OK | Alvo declarado como estratégia futura, não como estado atual. Sem correção. |
| Prova de conceito | Caderno 3 | "desde a prova de conceito analítica (TRL-3) até a demonstração operacional" | ⚠️ ATENÇÃO | Mesmo qualificador: sem ensaio próprio, "prova de conceito" deve ser lida como analítica/documental. Ver R-02. |

## 2. Afirmações econômicas

| Item | Documento | Trecho verificado | Veredicto | Recomendação |
|---|---|---|---|---|
| OPEX logístico | Caderno 3 | "o modelo descentralizado... reduzindo drasticamente o OPEX"; "reduz a massa transportada de cada lote de bambu em até 50%"; "vantagem econômica estrutural" | ⚠️ **REQUER CORREÇÃO** | Sem modelagem de custo (frete, CAPEX/OPEX por cenário, sensibilidade), "até 50%" e "vantagem estrutural" são hipóteses analíticas apresentadas com força de fato. Recomenda-se reformular para: "hipótese a ser comprovada por balanço de massa real e análise de custo comparada (ver H-BAM-012)". O Anexo 1 é o portão de evidência econômica. Ver R-03 (alta prioridade). |
| Circuito térmico | Caderno 3 | "fechando o circuito térmico sem combustíveis exógenos" | ⚠️ ATENÇÃO | Nenhuma medição de balanço térmico existe; a afirmação de fechamento do circuito é hipótese. Ver R-04. Ver H-BAM-013. |
| Receita por coprodutos | Cadernos 6, 7 | Discussão de biochar, energia e coprodutos | ⚠️ ATENÇÃO | Potencial documentado, mas rendimentos, qualidade e demanda não medidos no sistema autoral. Manter como hipótese. Ver R-05. |
| Viabilidade territorial | Anexo 1 | Instrumento preenchível de modelagem econômico-financeira por cenários | ✅ OK | O próprio front matter declara método "modelagem-economico-financeira-por-cenarios"; é instrumento, não confirmação. Sem correção. |

## 3. Alegações ambientais

| Item | Documento | Trecho verificado | Veredicto | Recomendação |
|---|---|---|---|---|
| Sequestro de carbono 25–50% | Caderno 6 | "biochars estáveis apresentaram eficiência estimada de sequestro entre 25% e 50%... Esse intervalo não é fator pronto para o bambu Takwara" | ✅ OK | O caderno declara explicitamente o limite (fonte externa modelada em cem anos; não transferível). Auditoria passa. |
| Remoção líquida / emissão negativa | Cadernos 6, 7 | Discussão de carbono, biochar e cascata | ⚠️ ATENÇÃO | Sem balanço de massa/energia próprio e cenário de referência, qualquer alegação de remoção líquida é hipótese. Ver H-BAM-021 e R-06. |
| Atoxicidade / biodegradabilidade | Cadernos 1, 2, 7 | Menções a PU vegetal, pirolenhoso e ciclo | ⚠️ ATENÇÃO | Sem ensaios de decomposição/emissões dos híbridos (H-BAM-022), "não tóxico"/"biodegradável" são rótulos não demonstrados. Ver R-07. |
| Circularidade integral | Caderno 7 | "O ciclo que não termina no descarte" | ⚠️ ATENÇÃO | O título é formulação autoral; "circularidade integral" não é demonstrada. Manter como programa de pesquisa, não resultado. Ver R-08. |

## 4. Perfis e trajetórias profissionais

| Item | Documento | Veredicto |
|---|---|---|
| Perfis de pesquisadores | Cadernos 1-7 | ✅ OK — nenhum caderno usa perfil pessoal como evidência estatística de resultado; perfis do Acervo (respaldo-academico) são referenciados apenas como interlocução, não como confirmação. Sem correção. |

## 5. Passagens culturais, etimológicas e filosóficas

| Item | Documento | Veredicto |
|---|---|---|
| Referências culturais | Cadernos 1-7 | ✅ OK — onde há passagens culturais/filosóficas (ex.: soberania tecnológica, ciclo), são formulações autorais declaradas, não demonstração de propriedade física. Sem correção. |

## 6. Riscos de propriedade intelectual

| Item | Documento | Veredicto |
|---|---|---|
| Parâmetros habilitantes | Cadernos 2, 3, 4, 7 | ⚠️ **ATENÇÃO** — a matriz classifica como `restrito-pd` as hipóteses que envolvem geometrias, formulações, faixas de pH, tempos/temperaturas e configurações protegíveis (H-BAM-003, H-BAM-004, H-BAM-008, H-BAM-009, H-BAM-016, H-BAM-018, H-BAM-023). Publicação defensiva ≠ patente ≠ certificação ≠ liberdade de operação. Antes de qualquer divulgação técnica nova, confirmar o nível de divulgação por hipótese (seção 13.6 da orientação). |
| Certificado UL 94 | Caderno 2, 4 | ✅ OK — matriz registra que o certificado pertence à amostra isolada (H-BAM-018), bloqueando alegação sobre o componente. Auditoria passa. |

## 7. Síntese da auditoria

- **8 documentos auditados** (Cadernos 1-7 + Anexo 1), 30 hipóteses mapeadas na matriz (H-BAM-001 a 030).
- **3 pontos requerem correção material** (PR editorial separado): R-01 (TRL-3 do Caderno 1), R-03 (OPEX "até 50%" do Caderno 3), R-04 (circuito térmico sem combustíveis exógenos do Caderno 3).
- **5 pontos de atenção** (podem permanecer como pendências na matriz, sem PR): R-02, R-05, R-06, R-07, R-08.
- **Nenhum perfil pessoal usado como evidência.**
- **Nenhuma passagem cultural usada como demonstração física.**
- **Parâmetros protegíveis** classificados como `restrito-pd` na matriz; nenhum parâmetro habilitante divulgado nos artefatos 00.

## 8. Nota metodológica

Esta auditoria é uma **revisão editorial de consistência epistêmica** — não uma avaliação técnica da viabilidade das tecnologias. Ela verifica se as afirmações dos documentos autorais estão no nível de evidência adequado (hipótese vs. resultado), conforme a orientação pré-PR. A auditoria não produz, nem pode produzir, validação experimental própria.
