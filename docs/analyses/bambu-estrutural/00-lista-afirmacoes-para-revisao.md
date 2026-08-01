---
titulo: "Lista de afirmações para revisão editorial — corpus autoral do eixo Bambu"
tipo_documental: instrumento-de-pesquisa
estado_documental: em-revisao-documental
responsavel_curadoria: Fabio Takwara
data_revisao: 2026-08-01
---

# Lista de afirmações para revisão editorial

*Subconjunto da auditoria epistêmica que justifica um PR editorial separado (`v1.1/revisao-epistemica-cadernos`). Itens com prioridade ALTA são correções materiais; itens MÉDIA podem ser registrados como pendências na matriz.*

## Correções materiais (prioridade ALTA — PR editorial separado)

| ID | Documento | Seção | Afirmação | Motivo | Ação sugerida |
|---|---|---|---|---|---|
| R-01 | Caderno 1 | Front matter + subtítulo Zenodo + seção TRL | "Prova de conceito (TRL-3)" com base em "revisão de escopo documental de 17 fontes" | TRL-3 (prova de conceito experimental) não é sustentado por revisão documental sem ensaio primário próprio; a maturidade descrita é da agenda de pesquisa, não da tecnologia | Reformular para "prova de conceito analítica/documental (maturidade da agenda de pesquisa; maturidade da tecnologia não determinada)"; ajustar `nivel_maturidade_trl` para declarar a distinção; manter TRL-4 como alvo |
| R-02 | Caderno 3 | Seção de arquitetura | "desde a prova de conceito analítica (TRL-3) até a demonstração operacional (TRL-7)" | Mesma questão do R-01: sem ensaio próprio, a etapa atual é analítica; o trecho já usa o qualificador "analítica", mas a associação direta a "TRL-3" pode induzir leitura de maturidade experimental | Manter "prova de conceito analítica", acrescentando "sem validação experimental própria até a presente data" |
| R-03 | Caderno 3 | Resumo + seção de OPEX | "reduz a massa transportada de cada lote de bambu em até 50%"; "vantagem econômica estrutural"; "reduzindo drasticamente o OPEX" | Afirmação quantitativa ("até 50%") e superlativa ("estrutural", "drasticamente") sem modelagem de custo, balanço de massa real ou análise de sensibilidade; o próprio caderno rebaixa a afirmação na seção de limitações | Reformular para hipótese: "a redução da massa transportada (colmo verde 40-60% água) é hipótese a ser comprovada por balanço de massa real e análise de custo comparada (ver H-BAM-012 e Anexo 1)" |
| R-04 | Caderno 3 | Seção de pirólise/circuito | "fechando o circuito térmico sem combustíveis exógenos" | Nenhuma medição de balanço térmico existe; a autossuficiência térmica é hipótese de projeto | Reformular para "hipótese a ser verificada por balanço térmico em bancada ou escala reduzida (ver H-BAM-013)" |
| R-09 | Caderno 3 | Estado editorial | O corpo afirma "versão candidata 1.0... Ainda não possui DOI", mas o front matter registra DOI (10.5281/zenodo.21514991) e estado publicado-no-zenodo | Divergência entre estado editorial declarado e metadados publicados | Harmonizar o estado editorial com os metadados: ou remover "ainda não possui DOI" ou declarar a versão efetivamente depositada |
| R-10 | Caderno 4 | Versão e DOI | Front matter declara versão 1.0, mas o selo da versão em inglês indica v1.1; Cadernos 6 e 7 citam "versão 1.1"; Caderno 5 cita o Caderno 4 com DOI 10.5281/zenodo.21515210, divergente do DOI declarado pelo próprio Caderno 4 (10.5281/zenodo.21515361) | Divergência de versão e de DOI entre documentos autorais | Definir a versão vigente (1.0 ou 1.1), unificar o DOI citado pelos Cadernos 5, 6 e 7 e atualizar o front matter; conferir no Zenodo a versão realmente depositada |

## Pendências recomendadas (prioridade MÉDIA — podem permanecer na matriz)

| ID | Documento | Afirmação | Motivo |
|---|---|---|---|
| R-05 | Cadernos 6, 7 | Receita/valor por coprodutos (biochar, energia) | Potencial documentado por fontes externas, mas rendimentos e demanda do sistema autoral não medidos; manter como hipótese na matriz (H-BAM-021, H-BAM-025) |
| R-06 | Cadernos 6, 7 | Remoção líquida / emissão negativa | Sem balanço de massa/energia e cenário de referência próprios; alegação bloqueada até validação (H-BAM-021) |
| R-07 | Cadernos 1, 2, 7 | "Não tóxico" / "biodegradável" / "ativo" aplicado a híbridos | Sem ensaios de decomposição e emissões dos híbridos bambu-PU-espuma; rótulos não demonstrados (H-BAM-022) |
| R-08 | Caderno 7 | "Ciclo que não termina no descarte" / circularidade | Formulação autoral legítima como programa de pesquisa; não apresentar como resultado demonstrado |

## Itens verificados e aprovados (sem ação)

| ID | Documento | Item | Motivo da aprovação |
|---|---|---|---|
| R-11 | Caderno 6 | Sequestro 25-50% | O caderno declara explicitamente "não é fator pronto para o bambu Takwara" — limite correto |
| R-12 | Caderno 1, 3, 4, 7 | TRL-7 como alvo | Declarado como estratégia futura, não estado atual |
| R-13 | Anexo 1 | Viabilidade econômica | Front matter declara método por cenários; é instrumento, não confirmação |
| R-14 | Cadernos 1-7 | Perfis pessoais | Nenhum perfil usado como evidência de resultado |
| R-15 | Cadernos 1-7 | Certificado UL 94 | Matriz registra bloqueio de alegação (H-BAM-018) — uso correto |

## Nota

Esta lista não altera nenhum caderno. Se aprovada, abre-se o PR `v1.1/revisao-epistemica-cadernos` com as correções materiais **R-01 a R-04, R-09 e R-10** (seis correções: TRL-3, prova de conceito, OPEX, circuito térmico, estado editorial do Caderno 3 e versão/DOI do Caderno 4); as demais permanecem registradas na matriz como pendências.
