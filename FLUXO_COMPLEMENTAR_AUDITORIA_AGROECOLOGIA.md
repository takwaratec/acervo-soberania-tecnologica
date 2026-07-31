# Fluxo Complementar de Auditoria e Correção
## Agroecologia, Reforma Agrária, Soberania Alimentar e Tecnologias Regenerativas

**Repositório:** Acervo Soberania Tecnológica  
**Responsável pela curadoria:** Fabio Takwara  
**Data:** 31/07/2026  
**Estado documental:** em-revisao-documental  
**Natureza:** complemento ao plano `PLANO_DECOUPAGEM_FICHAMENTO_AGROECOLOGIA.md`

---

# 1. Finalidade

Este documento não substitui nem interrompe o plano de decupagem, transcrição e fichamento já em execução. Sua função é criar uma camada complementar de:

- auditoria bibliográfica;
- verificação de endpoints;
- controle de qualidade da transcrição;
- revisão da classificação documental;
- detecção de lacunas;
- correção de inconsistências;
- priorização das fontes ainda não resolvidas;
- prevenção de homologações indevidas.

O fluxo deve ser executado em paralelo ao plano anterior, preferencialmente por agente distinto daquele responsável pela extração principal.

---

# 2. Diagnóstico das falhas e limitações do plano anterior

## 2.1 Ausência de trilha formal de evidências para cada endpoint

O plano anterior registra páginas e PDFs, mas não exige que o agente guarde, para cada endpoint:

- data e hora da validação;
- código HTTP;
- URL final após redirecionamentos;
- tipo MIME;
- tamanho do arquivo;
- hash SHA-256;
- título exibido na página;
- instituição responsável;
- evidência de que o arquivo corresponde à referência citada.

### Risco

Um link pode permanecer ativo, mas passar a apontar para arquivo diferente, página genérica, versão incompleta ou edição distinta.

### Ajuste

Criar um registro de proveniência por fonte, antes de iniciar a decupagem.

---

## 2.2 Confirmação insuficiente entre metadados da página e metadados do documento

O plano orienta a confirmar autoria e identificadores, mas não determina uma comparação explícita entre:

- metadados da página institucional;
- folha de rosto;
- ficha catalográfica;
- cabeçalho do artigo;
- metadados embutidos no PDF;
- DOI, ISBN ou ISSN consultado externamente.

### Risco

O agente pode copiar metadados da página de divulgação que não correspondem exatamente à edição processada.

### Ajuste

Adotar uma tabela de confronto de metadados e bloquear a homologação quando houver divergência não resolvida.

---

## 2.3 Uso de “endpoint confirmado” sem escala de confiança

A classificação atual distingue endpoint confirmado, página confirmada e acesso restrito, mas não separa:

- fonte oficial primária;
- repositório institucional secundário;
- cópia disponibilizada por autor;
- agregador acadêmico;
- página comercial;
- referência indireta.

### Risco

Fontes com graus de confiabilidade distintos podem receber o mesmo tratamento operacional.

### Ajuste

Aplicar uma escala de confiança de proveniência de A a E.

---

## 2.4 Ambiguidade na referência “Nascimento et al.”

O plano reconhece a identificação pendente, mas ainda não define um protocolo de desambiguação com critérios de encerramento.

### Risco

O agente pode manter buscas indefinidas, associar obra semelhante ou duplicar referências relacionadas.

### Ajuste

Criar um fluxo específico de desambiguação, com termos, fontes, evidências mínimas e condição de encerramento como “não identificado”.

---

## 2.5 Falta de verificação sistemática das datas, edições e versões

Algumas obras podem possuir:

- primeira edição;
- edição revisada;
- tradução;
- reimpressão;
- versão preliminar;
- capítulo derivado;
- edição comercial diferente da versão institucional.

### Risco

Mistura de paginação, ISBN, data e conteúdo de edições distintas.

### Ajuste

Criar um identificador de manifestação documental para cada versão efetivamente processada.

---

## 2.6 Decupagem sem padrão de nomenclatura de unidades

O plano indica separar capa, sumário, capítulos, tabelas e anexos, mas não define nomes de arquivos, IDs ou relação hierárquica.

### Risco

Agentes diferentes podem gerar estruturas incompatíveis e dificultar auditoria ou recomposição do documento.

### Ajuste

Adotar convenção única de IDs para páginas, capítulos, tabelas, figuras e anexos.

---

## 2.7 Transcrição sem métrica objetiva de qualidade

O plano prevê revisão humana, porém não determina:

- taxa mínima de amostragem;
- limite aceitável de erros;
- campos de confiança;
- como registrar trechos ilegíveis;
- quando repetir OCR;
- quem aprova a transcrição.

### Risco

Transcrições aparentemente completas podem conter erros em nomes, números, referências e tabelas.

### Ajuste

Adotar amostragem mínima e critérios de reprovação.

---

## 2.8 Mineração bibliográfica sem preservação da forma original

O plano orienta normalizar referências, mas não obriga a manter lado a lado:

- referência exatamente como publicada;
- referência normalizada;
- erro ou lacuna presente na fonte;
- correspondência com identificador externo.

### Risco

A normalização pode apagar evidências importantes e introduzir correções não rastreáveis.

### Ajuste

Preservar sempre a referência original e registrar toda normalização como camada curatorial.

---

## 2.9 Falta de controle de duplicatas por obra e por manifestação

O plano menciona eliminar duplicatas, mas não distingue:

- mesma obra em edições diferentes;
- mesmo artigo em repositórios diferentes;
- preprint e versão publicada;
- capítulo e livro completo;
- tradução e original;
- registro repetido com variação de autoria.

### Risco

Excluir manifestações legítimas ou contar uma mesma obra várias vezes.

### Ajuste

Separar `obra_conceitual_id` de `manifestacao_documental_id`.

---

## 2.10 Relações com bambu, resíduos e tecnologias regenerativas ainda muito abertas

O plano anterior alerta contra extrapolações, mas não define classes formais de relação.

### Risco

O agente pode interpretar uma conexão temática como evidência técnica ou aplicação validada.

### Ajuste

Classificar cada vínculo como:

- evidência direta;
- analogia metodológica;
- contexto territorial;
- hipótese de pesquisa;
- oportunidade de política pública;
- visão autoral.

---

## 2.11 Ausência de teste de aderência às oito seções antes da redação integral

O plano manda produzir a ficha em oito seções, mas não prevê uma análise prévia de suficiência documental.

### Risco

O agente pode preencher seções com conteúdo fraco, repetitivo ou inferido apenas para completar a estrutura.

### Ajuste

Criar uma matriz de suficiência antes da redação da ficha.

---

## 2.12 Ausência de conferência cruzada por segundo agente

O fluxo anterior concentra aquisição, extração, classificação e fichamento no mesmo percurso.

### Risco

Erros do primeiro agente podem ser reproduzidos em todas as etapas seguintes.

### Ajuste

Exigir revisão independente para metadados, referências, números, conclusões e classificação documental.

---

## 2.13 Falta de política de encerramento para fontes inacessíveis

Não está definido quando uma busca por PDF, DOI ou edição deve ser encerrada.

### Risco

Consumo indefinido de tempo ou uso de fontes de baixa confiabilidade para “completar” a tarefa.

### Ajuste

Após ciclos documentados de busca, classificar como:

- não localizado;
- acesso restrito;
- metadados insuficientes;
- referência possivelmente incorreta;
- obra sem versão digital conhecida.

---

## 2.14 Endpoints precisam ser revalidados antes do uso

Os links registrados no plano anterior podem mudar, expirar ou redirecionar.

### Risco

O agente iniciar processamento sobre página indisponível ou arquivo incorreto.

### Ajuste

Nenhum endpoint antigo deve ser assumido como válido sem nova checagem no momento da execução.

---

# 3. Novo fluxo complementar

## Fase A — Auditoria de entrada

Antes de qualquer download ou transcrição, criar um registro para cada referência com:

| Campo | Obrigatório |
|---|---|
| ID provisório | sim |
| Referência recebida | sim |
| Descrição temática recebida | sim |
| Título confirmado | sim/não |
| Autoria confirmada | sim/não |
| Ano confirmado | sim/não |
| Tipo documental | sim/não |
| Instituição ou periódico | sim/não |
| DOI/ISBN/ISSN | quando existente |
| Página oficial | sim/não |
| Arquivo integral | sim/não |
| Licença ou restrição | sim/não |
| Estado documental | sim |
| Grau de confiança | sim |
| Pendências | sim |

### Critério de saída

Somente referências com título e autoria confirmados podem avançar para aquisição. Referências ambíguas seguem para a Fase B.

---

## Fase B — Desambiguação bibliográfica

Aplicar especialmente a “Nascimento et al.” e a qualquer referência temática sem título inequívoco.

### Procedimento

1. Preservar a redação original da referência recebida.
2. Extrair entidades conhecidas:
   - sobrenome;
   - território;
   - projeto;
   - instituição;
   - tema;
   - período provável.
3. Pesquisar combinações exatas e variantes.
4. Conferir bibliografias das fontes que citaram a obra.
5. Comparar autores, título, resumo, território e metodologia.
6. Registrar candidatos sem substituí-los pela referência original.
7. Confirmar somente quando houver duas evidências independentes ou uma fonte primária inequívoca.

### Condições de encerramento

- `identificado-com-seguranca`;
- `candidato-provavel-nao-confirmado`;
- `nao-identificado`;
- `referencia-tematica-sem-obra-unica`.

---

## Fase C — Validação técnica do endpoint

Para cada URL, registrar:

```yaml
endpoint_original:
endpoint_final:
data_validacao:
status_http:
tipo_mime:
tamanho_bytes:
sha256:
instituicao_hospedeira:
titulo_pagina:
titulo_documento:
licenca:
grau_proveniencia:
```

### Escala de proveniência

- **A:** editora, periódico ou repositório institucional responsável;
- **B:** instituição parceira ou repositório acadêmico reconhecido;
- **C:** arquivo disponibilizado pelo autor;
- **D:** agregador acadêmico sem responsabilidade editorial;
- **E:** cópia sem proveniência suficiente.

Fontes E não devem ser processadas. Fontes D exigem busca adicional por versão A, B ou C.

---

## Fase D — Confronto de metadados

Comparar:

| Elemento | Página | Documento | Identificador externo | Resultado |
|---|---|---|---|---|
| Título | | | | |
| Autores | | | | |
| Ano | | | | |
| Edição | | | | |
| Editora/instituição | | | | |
| DOI | | | | |
| ISBN/ISSN | | | | |
| Número de páginas | | | | |

### Regra

Divergências devem ser documentadas. O agente não pode escolher silenciosamente um valor.

---

## Fase E — Controle de manifestações e versões

Criar dois identificadores:

```yaml
obra_conceitual_id: OBRA-XXXX
manifestacao_documental_id: DOC-XXXX-V01
```

Exemplos de manifestações distintas:

- edição original;
- tradução portuguesa;
- edição revisada;
- versão institucional;
- versão comercial;
- preprint;
- artigo final.

Cada ficha deve informar exatamente qual manifestação foi utilizada.

---

## Fase F — Decupagem padronizada

### Convenção de IDs

```text
DOC-XXXX-P0001        página
DOC-XXXX-CAP-01       capítulo
DOC-XXXX-SEC-01-02    seção
DOC-XXXX-TAB-001      tabela
DOC-XXXX-FIG-001      figura
DOC-XXXX-QUA-001      quadro
DOC-XXXX-ANX-01       anexo
DOC-XXXX-REF-0001     referência bibliográfica
```

### Arquivo de mapa estrutural

Criar `mapa_decupagem.yaml` contendo:

- ID da unidade;
- páginas inicial e final;
- título;
- tipo;
- nível hierárquico;
- unidade pai;
- relevância;
- necessidade de OCR;
- estado da revisão.

---

## Fase G — Auditoria da transcrição

### Requisitos mínimos

- revisar 100% da folha de rosto e ficha catalográfica;
- revisar 100% das referências bibliográficas;
- revisar 100% de tabelas, quadros e números usados na ficha;
- revisar amostra mínima de 10% das páginas de texto corrido;
- ampliar a amostra para 25% se forem encontrados erros relevantes;
- reprovar e repetir a extração se houver erro sistemático.

### Marcadores obrigatórios

```text
[ilegivel]
[texto_cortado]
[erro_no_original]
[transcricao_incerta]
[nota_do_curador]
```

Não corrigir silenciosamente o original.

---

## Fase H — Mineração bibliográfica auditável

Para cada referência citada, preservar:

```yaml
referencia_original:
referencia_normalizada:
localizacao_no_documento:
identificador_externo:
status_identificacao:
correcoes_curatoriais:
fonte_da_correcao:
```

### Regra de duplicidade

- agrupar referências equivalentes sob o mesmo `obra_conceitual_id`;
- manter manifestações diferentes separadas;
- nunca eliminar registro sem manter histórico de fusão.

---

## Fase I — Matriz de suficiência para a ficha

Antes de redigir, avaliar cada seção:

| Seção | Evidência suficiente? | Páginas-base | Lacunas |
|---|---|---|---|
| Dados gerais | | | |
| Estrutura e organização | | | |
| Problema e perguntas | | | |
| Referencial | | | |
| Metodologia | | | |
| Achados | | | |
| Avaliação crítica | | | |
| Inserção no estado da arte | | | |

### Regra

Se metodologia ou achados não puderem ser sustentados diretamente, a ficha não deve ser homologada como análise científica completa.

---

## Fase J — Classificação das conexões com tecnologias regenerativas

Cada relação com bambu, poliuretano vegetal, biomassa, resíduos, biochar ou habitação deve receber uma classe:

| Código | Relação |
|---|---|
| RD | evidência direta na fonte |
| AM | analogia metodológica |
| CT | contexto territorial |
| HP | hipótese de pesquisa |
| PP | oportunidade de política pública |
| VA | visão autoral de Fabio Takwara |

### Regra

Somente `RD` pode ser descrita como achado da fonte. As demais devem ser apresentadas explicitamente como conexão curatorial ou autoral.

---

## Fase K — Revisão independente

Um segundo agente deve conferir:

- título e autoria;
- DOI/ISBN/ISSN;
- versão processada;
- citações e páginas;
- números e percentuais;
- nomes científicos;
- resumo dos achados;
- limitações;
- classe das conexões com tecnologias regenerativas;
- estado documental atribuído.

### Resultado possível

- `aprovado-para-revisao-humana`;
- `devolver-para-correcao`;
- `bloqueado-por-falta-de-fonte`;
- `bloqueado-por-divergencia-bibliografica`.

---

# 4. Perfis de busca complementares

Transformar os nove temas propostos em perfis permanentes de busca.

## Perfil 1 — Diagnóstico de agroecossistemas

Termos principais:

- análise econômico-ecológica;
- método Lume;
- metabolismo socioecológico;
- indicadores de sustentabilidade;
- linha de base agroecológica;
- monitoramento de agroecossistemas.

Referência obrigatória inicial:

- Petersen et al.

---

## Perfil 2 — Planejamento participativo de assentamentos

Termos principais:

- assentamentos agroecológicos;
- Extremo Sul da Bahia;
- pesquisa-ação;
- planejamento territorial participativo;
- Projeto Assentamentos Agroecológicos;
- Escola Popular Egídio Brunetto.

Pendência central:

- identificação conclusiva de Nascimento et al.

---

## Perfil 3 — SAFs, restauração e quintais

Termos principais:

- quintais produtivos;
- enriquecimento com espécies nativas;
- restauração produtiva;
- SAF sucessional;
- Cerrado;
- Caatinga;
- reforma agrária.

Referências obrigatórias iniciais:

- Lopes et al.;
- Miccolis et al.

---

## Perfil 4 — Camponês a Camponês

Termos principais:

- campesino a campesino;
- ANAP;
- intercâmbio horizontal;
- promotores camponeses;
- difusão agroecológica;
- formação territorial.

Referência obrigatória inicial:

- Machín Sosa et al.

---

## Perfil 5 — Gênero e economia feminista

Termos principais:

- mulheres e agroecologia;
- economia invisível;
- divisão sexual do trabalho;
- quintais;
- economia do cuidado;
- redes solidárias;
- comercialização territorial.

Referências obrigatórias iniciais:

- Emma Siliprandi;
- Liliam Telles;
- Raízes da Resistência.

---

## Perfil 6 — Economia política da terra

Termos principais:

- questão agrária;
- assentamentos;
- campesinato;
- capitalismo brasileiro;
- território camponês;
- cotidiano e história.

Referências obrigatórias iniciais:

- Francisco de Oliveira;
- Jadir de Morais Pessoa.

---

## Perfil 7 — Conhecimentos tradicionais e agrossociobiodiversidade

Termos principais:

- roça de coivara;
- quilombolas;
- conhecimentos tradicionais;
- Anna Primavesi;
- agrossociobiodiversidade;
- territórios de resistência;
- bioeconomia comunitária.

Referência obrigatória inicial:

- Raízes da Resistência.

---

## Perfil 8 — Mercados, certificação e políticas públicas

Termos principais:

- Rede Ecovida;
- certificação participativa;
- SPG;
- OCS;
- circuitos curtos;
- marco regulatório;
- mercados territoriais.

Referência obrigatória inicial:

- documentação institucional da Rede Ecovida.

---

## Perfil 9 — Tecnologias regenerativas e soberania tecnológica

Termos principais:

- bambu em assentamentos;
- biomassa agroflorestal;
- resíduos agrícolas;
- uso em cascata;
- biochar;
- poliuretano vegetal;
- biomateriais;
- habitação social;
- bioeconomia territorial.

### Regra

Este perfil deve sempre ser cruzado com os oito perfis anteriores, sem transformar conexão temática em evidência experimental.

---

# 5. Ordem de execução complementar

## Bloco 1 — Auditoria imediata

1. Revalidar todos os endpoints do plano anterior.
2. Registrar hashes e proveniência.
3. Confrontar metadados das páginas com os documentos.
4. Separar obras conceituais de manifestações documentais.
5. Sinalizar divergências.

## Bloco 2 — Fontes críticas

1. Resolver ou encerrar a busca de Nascimento et al.
2. Localizar versão institucional preferencial de Miccolis et al.
3. Confirmar edição, tradução e ISBN de Machín Sosa et al.
4. Confirmar autores, organizadoras e manifestação de Raízes da Resistência.
5. Confirmar acesso integral da tese de Jadir de Morais Pessoa.

## Bloco 3 — Controle da produção em curso

1. Auditar amostras das transcrições já produzidas.
2. Conferir números, tabelas e referências.
3. Aplicar matriz de suficiência às fichas em elaboração.
4. Reclassificar conexões com tecnologias regenerativas.
5. Devolver ao agente executor os itens que exigem correção.

## Bloco 4 — Expansão do acervo

1. Executar os nove perfis de busca.
2. Minerar bibliografias das fontes prioritárias.
3. Criar fila de novas referências.
4. Eliminar duplicidades sem apagar manifestações.
5. Atualizar estado da arte e índice mestre.

---

# 6. Arquivos de controle recomendados

```text
controle/
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

Esses arquivos são instrumentos internos de trabalho e não devem ser publicados automaticamente em `docs/`.

---

# 7. Critérios de bloqueio

Bloquear o avanço da fonte quando houver:

- autoria não confirmada;
- título não confirmado;
- arquivo incompleto;
- divergência de edição;
- endpoint sem proveniência;
- suspeita de violação de direitos;
- OCR sem revisão suficiente;
- metodologia ou achados não sustentados;
- referência normalizada sem preservação do original;
- conexão com tecnologia regenerativa apresentada como prova sem evidência direta.

---

# 8. Critérios para conclusão da auditoria

Uma fonte será considerada pronta para revisão humana quando:

- identidade bibliográfica estiver confirmada;
- manifestação documental estiver identificada;
- endpoint e hash estiverem registrados;
- direitos e licença estiverem classificados;
- decupagem estiver completa;
- transcrição estiver auditada;
- referências tiverem sido extraídas e preservadas;
- matriz de suficiência estiver preenchida;
- ficha em oito seções estiver sustentada;
- conexões curatoriais estiverem classificadas;
- segundo agente tiver concluído a conferência.

---

# 9. Relação com o plano anterior

O plano anterior continua responsável por:

- aquisição;
- decupagem;
- transcrição;
- mineração bibliográfica;
- criação das fichas;
- integração ao eixo Reforma Agrária e Agrofloresta.

Este fluxo complementar passa a ser responsável por:

- auditoria;
- desambiguação;
- confronto de metadados;
- controle de versões;
- verificação de OCR;
- avaliação de suficiência;
- revisão independente;
- bloqueio ou liberação para revisão humana.

Os dois fluxos devem operar em paralelo, com registros separados e comunicação por meio do `log_correcoes.md`.

---

# 10. Checklist de conferência e ajustes

- [ ] Todos os endpoints antigos foram revalidados.
- [ ] URL final, status HTTP e tipo MIME foram registrados.
- [ ] Hash SHA-256 foi calculado.
- [ ] Metadados da página foram confrontados com o documento.
- [ ] Edição e manifestação utilizadas foram identificadas.
- [ ] “Nascimento et al.” recebeu protocolo de desambiguação.
- [ ] Decupagem segue convenção de IDs.
- [ ] OCR possui amostragem e registro de confiança.
- [ ] Referência original foi preservada antes da normalização.
- [ ] Duplicatas foram tratadas por obra e manifestação.
- [ ] Matriz de suficiência foi aplicada.
- [ ] Relações com bambu e resíduos foram classificadas.
- [ ] Segundo agente realizou revisão independente.
- [ ] Pendências foram registradas sem preenchimento por inferência.
- [ ] Revisão humana foi solicitada antes da homologação.

---

# 11. Resultado esperado

A aplicação deste fluxo complementar deve reduzir erros silenciosos, impedir a propagação de metadados incorretos, melhorar a qualidade das transcrições e tornar rastreável cada decisão tomada pelos agentes locais.

O objetivo não é aumentar artificialmente a quantidade de fichas, mas garantir que cada documento incorporado ao Acervo Soberania Tecnológica possua identidade, proveniência, conteúdo e relações curatoriais verificáveis.
