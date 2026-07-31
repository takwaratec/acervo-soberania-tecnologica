# PLANO DE EXECUÇÃO — AUDITORIA E CORREÇÃO AGROECOLOGIA

> **Base:** FLUXO_COMPLEMENTAR_AUDITORIA_AGROECOLOGIA.md (diagnóstico de 14 falhas do plano anterior)
> **Repositório:** Acervo Soberania Tecnológica
> **Data:** 2026-07-31
> **Estado:** em-revisao-documental — aguarda aprovação de Fabio antes de executar correções
> **Natureza:** plano derivado; operação em paralelo ao plano de decupagem (P2/P3/P4 agendado no cron)

---

## 1. Mapa de falhas do plano anterior → correção

| # | Falha diagnosticada | Correção (fluxo complementar) | Fase |
|---|---|---|---|
| 2.1 | Sem trilha de evidências por endpoint | Registro de proveniência (data, HTTP, URL final, MIME, hash, título, instituição) | A, C |
| 2.2 | Metadados página ≠ documento | Tabela de confronto de metadados; bloqueio em divergência | D |
| 2.3 | "Endpoint confirmado" sem escala | Escala de proveniência A–E (E não processa; D exige busca A/B/C) | C |
| 2.4 | "Nascimento et al." sem protocolo | Fluxo de desambiguação com condições de encerramento | B |
| 2.5 | Edições/versões não verificadas | obra_conceitual_id + manifestacao_documental_id | E |
| 2.6 | Decupagem sem nomenclatura | Convenção de IDs (DOC-XXXX-CAP-01, TAB-001...) | F |
| 2.7 | Transcrição sem métrica | Amostragem 10%/25%, marcadores [ilegivel] etc. | G |
| 2.8 | Mineração sem preservar original | referencia_original + normalizada + correções curatoriais | H |
| 2.9 | Duplicatas mal controladas | Obra conceitual vs manifestação; histórico de fusão | E, H |
| 2.10 | Conexões bambu/resíduos abertas | Classes RD/AM/CT/HP/PP/VA | J |
| 2.11 | Sem teste de suficiência antes da ficha | Matriz de suficiência 8 seções | I |
| 2.12 | Sem conferência cruzada | Revisão independente por segundo agente | K |
| 2.13 | Sem política de encerramento de busca | Classificação final: não-localizado/restrito/etc. | B, C |
| 2.14 | Endpoints podem mudar | Revalidação obrigatória antes do uso | C |

## 2. Arquivos de controle (criar em `_privado/auditoria-agroecologia-2026/`)

```text
_privado/auditoria-agroecologia-2026/
├── auditoria_endpoints.csv
├── confronto_metadados.csv
├── referencias_ambiguas.csv
├── manifestacoes_documentais.csv
├── controle_ocr.csv
├── auditoria_transcricoes.csv
├── matriz_suficiencia_fichas.csv
├── relacoes_tecnologias_regenerativas.csv
├── fila_mineracao_bibliografica.csv
└── log_correcoes.md
```

> Instrumentos internos — NUNCA em `docs/` (regra do fluxo §6).

## 3. Etapas de execução

### ETAPA A — Auditoria de entrada (retroativa às 5 fichas P1 + 24 registros SAF)

- [ ] A1. Criar a estrutura `_privado/auditoria-agroecologia-2026/` com os 10 arquivos de controle
- [ ] A2. Registrar, para cada fonte já fichada (Petersen, Lopes, Raízes, Miccolis, Pessoa + 24 SAF):
  - título/autoria/ano/tipo/instituição confirmados (sim/não);
  - DOI/ISBN/ISSN quando existente;
  - endpoint + hash SHA-256;
  - licença/restrição;
  - grau de confiança de proveniência (A–E);
  - estado documental e pendências.
- [ ] A3. Critério de saída: somente fontes com título+autoria confirmados avançam; ambíguas → Etapa B

### ETAPA B — Desambiguação bibliográfica

- [ ] B1. "Nascimento et al." (construção participativa, ES da Bahia) — protocolo: preservar redação original; extrair entidades (sobrenome, território, projeto, instituição, tema); pesquisar variantes; conferir bibliografias de "Agrofloresta e a Prática", anais ABA, RBA, ESALQ/USP, Escola Egídio Brunetto; exigir 2 evidências independentes OU fonte primária inequívoca
- [ ] B2. "Nascimento et al." (produção agroecológica e soberania alimentar) — mesmo protocolo
- [ ] B3. Registrar resultado em `referencias_ambiguas.csv` com condição de encerramento:
  `identificado-com-seguranca | candidato-provavel | nao-identificado | referencia-tematica-sem-obra-unica`
- [ ] B4. NÃO criar ficha científica enquanto não houver identificação segura

### ETAPA C — Revalidação técnica de endpoints (retroativa + preventiva)

- [ ] C1. Revalidar TODOS os endpoints registrados (P1 + 24 SAF + plano anterior), no momento da execução:
  URL original → URL final, data, status HTTP, tipo MIME, tamanho, sha256, instituição hospedeira, título da página, título do documento, licença, grau A–E
- [ ] C2. Fontes E (sem proveniência): NÃO processar
- [ ] C3. Fontes D (agregador): buscar versão A/B/C antes
- [ ] C4. Casos pendentes prioritários:
  - Miccolis et al. 2016 → buscar ISPN/ICRAF/Embrapa (hoje: ResearchGate bloqueado, ISPN 404) — grau atual D/E;
  - Pessoa 1997 → baixar PDF do repositório Unicamp via sessão validada — grau A (endpoint institucional);
  - Machín Sosa et al. 2011 → validar arquivo no download do MST e conferir ISBN/edição

### ETAPA D — Confronto de metadados

- [ ] D1. Para cada ficha: tabela Página × Documento × Identificador externo (título, autores, ano, edição, editora, DOI, ISBN/ISSN, páginas)
- [ ] D2. Divergências documentadas em `confronto_metadados.csv` — NUNCA escolher valor silenciosamente
- [ ] D3. Aplicar às 5 fichas P1 (verificar se a ficha reflete a manifestação efetivamente processada)

### ETAPA E — Controle de manifestações

- [ ] E1. Atribuir `obra_conceitual_id` + `manifestacao_documental_id` às fichas P1 e registros SAF
- [ ] E2. Registrar exemplos de manifestação: original/tradução/revisada/institucional/comercial/preprint
- [ ] E3. Verificar duplicidade de manifestações nos 24 registros SAF (ex.: Cochrane 1998a/b, Kato 1998a/b)

### ETAPA F — Decupagem padronizada (para fichas que avançarem)

- [ ] F1. Aplicar convenção de IDs (DOC-XXXX-P0001, -CAP-01, -SEC, -TAB, -FIG, -QUA, -ANX, -REF)
- [ ] F2. Criar `mapa_decupagem.yaml` por documento processado integralmente

### ETAPA G — Auditoria de transcrição

- [ ] G1. Para transcrições já produzidas: revisar 100% folha de rosto/ficha catalográfica, 100% referências, 100% tabelas/números usados na ficha; amostra mínima 10% do texto corrido
- [ ] G2. Ampliar para 25% se houver erros relevantes; reprovar extração se erro sistemático
- [ ] G3. Usar marcadores: [ilegivel], [texto_cortado], [erro_no_original], [transcricao_incerta], [nota_do_curador]
- [ ] G4. Registrar em `controle_ocr.csv` e `auditoria_transcricoes.csv`

### ETAPA H — Mineração bibliográfica auditável

- [ ] H1. Para cada referência extraída: referencia_original + normalizada + localização + identificador externo + correções curatoriais com fonte
- [ ] H2. Agrupar equivalentes sob mesmo obra_conceitual_id; manter manifestações separadas; histórico de fusão
- [ ] H3. Alimentar `fila_mineracao_bibliografica.csv`

### ETAPA I — Matriz de suficiência (pré-ficha)

- [ ] I1. Para cada ficha em elaboração: 8 seções avaliadas (evidência suficiente? páginas-base? lacunas?)
- [ ] I2. Regra: metodologia/achados não sustentados → NÃO homologar como análise completa (fica registro)

### ETAPA J — Classificação de conexões com tecnologias regenerativas

- [ ] J1. Revisar as 5 fichas P1 e classificar cada relação com bambu/PU/biomassa/resíduos/biochar/habitação:
  RD (evidência direta) | AM (analogia metodológica) | CT (contexto territorial) | HP (hipótese) | PP (política pública) | VA (visão autoral)
- [ ] J2. Somente RD pode ser descrita como achado; demais → conexão curatorial/autoral explícita

### ETAPA K — Revisão independente

- [ ] K1. Segundo agente confere: título/autoria, DOI/ISBN/ISSN, versão, citações/páginas, números, nomes científicos, resumo de achados, limitações, classe de conexões, estado documental
- [ ] K2. Resultado: `aprovado-para-revisao-humana | devolver-para-correcao | bloqueado-por-falta-de-fonte | bloqueado-por-divergencia-bibliografica`
- [ ] K3. Registrar em `log_correcoes.md`

## 4. Perfis de busca permanentes (9)

1. Diagnóstico de agroecossistemas (Petersen, Lume, metabolismo socioecológico)
2. Planejamento participativo de assentamentos (ES Bahia, Egídio Brunetto, Nascimento)
3. SAFs, restauração e quintais (Lopes, Miccolis)
4. Camponês a Camponês (Machín Sosa, ANAP)
5. Gênero e economia feminista (Siliprandi, Telles, Raízes)
6. Economia política da terra (Oliveira, Pessoa)
7. Conhecimentos tradicionais e agrossociobiodiversidade (Raízes, Primavesi)
8. Mercados, certificação e políticas públicas (Rede Ecovida)
9. Tecnologias regenerativas e soberania tecnológica (sempre cruzado, nunca evidência experimental)

## 5. Ordem sugerida de execução (blocos do fluxo)

| Bloco | Conteúdo | Quando |
|---|---|---|
| 1 — Auditoria imediata | Revalidar endpoints, hashes, confronto, manifestações, sinalizar divergências | Agora (Etapas A, C, D, E sobre o que já existe) |
| 2 — Fontes críticas | Nascimento, Miccolis, Machín Sosa, Raízes, Pessoa | Próximo ciclo (Etapas B, C) |
| 3 — Controle da produção | Amostras de transcrição, suficiência, conexões, devoluções | Durante P2/P3/P4 (Etapas G, I, J) |
| 4 — Expansão | 9 perfis de busca, mineração, fila, estado da arte | Contínuo (Etapa H) |

## 6. Critérios de bloqueio (aplicar sempre)

Autoria/título não confirmado · arquivo incompleto · divergência de edição · endpoint sem proveniência · suspeita de violação de direitos · OCR sem revisão · metodologia/achados não sustentados · referência normalizada sem original · conexão apresentada como prova sem RD.

## 7. Critérios de prontidão para revisão humana

Identidade confirmada + manifestação identificada + endpoint/hash registrados + direitos classificados + decupagem completa + transcrição auditada + referências preservadas + matriz de suficiência preenchida + ficha sustentada + conexões classificadas + segundo agente conferiu.

---

*Plano criado por Hermes Agent em 2026-07-31. Não commitado — aguarda aprovação.*
