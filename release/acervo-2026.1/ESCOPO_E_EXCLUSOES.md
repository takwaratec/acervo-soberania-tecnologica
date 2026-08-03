# Escopo e exclusões — Edição 2026.1 do Acervo Soberania Tecnológica

> Rascunho de diagnóstico para decisão H2 (aprovação do corpus e das exclusões).
> Autorizado por Fabio Takwara em 2026-08-03 (H1 aprovado — edição curada de referência).
> Nenhum arquivo do Acervo foi editado; nenhum commit foi feito.

## 1. Identidade da edição

- **Edição:** Acervo Soberania Tecnológica 2026.1
- **Repositório:** takwaratec/acervo-soberania-tecnologica
- **Responsável pela decisão final:** Fabio Takwara
- **Estado desta versão do escopo:** rascunho para H2 (não aprovado)
- **Arquivos relacionados:** MATRIZ_CORPUS_EDICAO_2026_1.csv, FOTOGRAFIA_CORRENTE_REPOSITORIO_2026_08_03.md,
  RELATORIO_DIAGNOSTICO_ORQUESTRADOR_2026_08_03.md, REGISTRO_DECISOES_EDICAO_2026_1.csv

## 2. Modalidade

Edição **curada de referência** (H1 aprovado em 03/08/2026): coleção seletiva de objetos
que completaram os portões da edição; não é um instantâneo integral do repositório em
desenvolvimento. Os demais arquivos podem permanecer no repositório público, mas não
entram automaticamente no ZIP congelado.

## 3. Período coberto

- Conteúdo curado até **01/08/2026** (data do depósito Zenodo v1.1 dos Cadernos 1, 3 e 4).
- Data de corte proposta: **a definir em H2** (proposta preliminar: após integração dos
  PRs aprovados e correção da divergência de main).

## 4. Corpus nuclear proposto

Objetos com papel `nucleo` na MATRIZ_CORPUS (sujeitos a H2 e às condições indicadas):

1. **Estados da arte + mapas + agendas** dos eixos v1.1:
   - Bambu Estrutural (PR #7 integrado; PR #11 — integração autoral pendente de H2)
   - PU Vegetal (PR #12), Bioeconomia Amazônica (PR #13), Habitação Social (PR #14)
   - Reforma Agrária/Agrofloresta (PR #8 integrado; conteúdo de agroecologia/SAF condicionado
     à resolução da divergência de main)
2. **Cadernos 1–7** (visão do autor): Caderno 3 apto (publicado, sem divergência); Cadernos 1 e 4
   **bloqueados** (rodapé "candidata" na versão depositada); Cadernos 2, 5, 6 e 7 — avaliar estado
   e DOI correspondente (Caderno 5 citado como v1.0 no depósito do Caderno 4).
3. **Artigos metodológicos** (PR #15): maturidade tecnológica/cobertura normativa e arquitetura
   curatorial — PT + traduções EN/ES (head 749a1ac), condicionados à leitura textual de Fabio,
   decisão sobre traduções/PDFs/índices, revisão de PI e novo portão humano.
4. **Artefatos autorais curados** de tecnologia-takwara (edicao-revisada-para-acervo): ensaios
   (bambu sem manejo; neocolonialismo), manual tijolos ecológicos/biochar, memorial equipamentos
   de pirólise, plataforma Amazônia Regenerativa — PT + EN.

## 5. Corpus de sustentação

- **Fichas** (ficha-academica 78 + ficha-cientifica 76): identificar o **conjunto mínimo** que
  sustenta as conclusões de cada estado da arte candidato (Frente C — sem campanha de
  homologação indiscriminada).
- Instrumentos de pesquisa do eixo bambu (00-*: matriz de rastreabilidade, inventário de corpus
  autoral, lista de afirmações, relatório de auditoria epistêmica, linha do tempo).
- Metodologia (`docs/metodologia.md`) e fundamentos (arquitetura curatorial — PR #15).

## 6. Documentos incluídos

(Somente após H2 — lista definitiva = MATRIZ_CORPUS com `inclusao_proposta = sim` e
`decisao_humana` preenchida.) Nesta rodada, **nada foi incluído formalmente**.

## 7. Documentos condicionados

| Objeto | Condição |
|---|---|
| Cadernos 1 e 4 (PDFs/MDs) | Nova versão Zenodo com rodapé corrigido + decisão H2; enquanto isso, **bloqueados** |
| Artigos PR #15 (6 arquivos) | Leitura textual de Fabio; decisão traduções/PDFs/índices; revisão PI; novo portão humano |
| Estados da arte PU Vegetal, Bioeconomia, Habitação | Integração dos PRs #12/#13/#14 (H2 + Frente B) |
| Integração autoral do bambu | Integração do PR #11 + resolução de sobreposição com f858208 em index.md |
| Conteúdo de agroecologia/SAF | Resolução da divergência de main (integração do main local ao remoto via PR) |
| Índices e mkdocs.yml | Reconciliar navegação após integrações |

## 8. Documentos excluídos

- PDFs e fontes integrais protegidas (removidos do tracking no rewrite; não reincorporar).
- Documentos de patente (moreira-silva-2022, pandoli-ghavami-sa-2023) e fichas técnicas de
  produto (Imperveg UG132A, Mamonex RD70): papel `relacionado-mas-nao-incluido` — matéria
  potencialmente protegível passa por portão próprio.
- Documentos em `quarentena` ou com direitos pendentes (a identificar na Frente D).
- Todo conteúdo P3.

## 9. Materiais privados

- `_privado/` (governança operacional, tarefas, planos, auditorias, fontes, manuscritos,
  documentos sensíveis) — **fora do pacote**; não versionado (gitignore linha 28).
- Repositório Mentoria (master interno) e documentos associados — nunca referenciados em
  documentos públicos.

## 10. Materiais de quarentena

- Itens com identificação pendente, proveniência insuficiente ou direitos não resolvidos.
- Lista definitiva a ser produzida na Frente C/D (homologação + direitos).

## 11. Propriedade intelectual

- Classificação P0–P3 a aplicar por arquivo (Frente D — acervo-rights-ip-gatekeeper).
- Somente P0 e P1 expressamente aprovados entram no pacote.
- Matéria patenteável (forno, conexões, ancoragem — Núcleo Takwara) **não é divulgada** sem
  decisão humana; não integra o ZIP.
- Licenças: curadoria CC BY 4.0 (padrão dos depósitos Zenodo existentes); não presumir que a
  licença da curadoria cobre imagens/obras de terceiros (73 PNGs a auditar).
- Normas e livros protegidos não são redistribuídos integralmente.

## 12. Tarefas paralelas

| Tarefa | Relação | Bloqueia congelamento |
|---|---|---|
| Integração semiótica-relacional | paralela | não |
| Renderização 3D Atlas Geodésico | paralela | não |

Nenhum produto dessas tarefas entra na edição 2026.1 sem nova decisão de escopo. Atlas 3D,
assets, modelos e conteúdos protegíveis permanecem fora do pacote.

## 13. Depósitos Zenodo relacionados

| Objeto | DOI específico | DOI conceitual | Versão | Relação com a edição |
|---|---|---|---|---|
| Caderno 1 — Preservação | 10.5281/zenodo.21738428 | 10.5281/zenodo.21514735 | 1.1 | condicionado (rodapé) |
| Caderno 3 — Capacidade produtiva | 10.5281/zenodo.21738550 | 10.5281/zenodo.21514990 | 1.1 | incluir |
| Caderno 4 — Conformidade | 10.5281/zenodo.21738559 | 10.5281/zenodo.21515209 | 1.2 | condicionado (rodapé) |

Ver MAPA_DOIS_ZENODO.csv. Cadernos 2, 5, 6, 7: verificar DOIs/versões e relações
(v1.0 citada pelo Caderno 4 = 10.5281/zenodo.21515210). Nenhuma nova versão será publicada
nesta rodada.

## 14. Critérios de entrada

1. Objeto expressamente selecionado no escopo (H2).
2. Revisão documental exigida pela edição concluída (Frente C).
3. Autoria, proveniência e direitos resolvidos (Frente D).
4. Sem material P2/P3.
5. Metadados, versão e relações documentais conferidos (Frente E).
6. Aprovado por portão humano aplicável (H2–H5).

## 15. Critérios de retirada

- Divergência material entre versão local e versão depositada (ex.: rodapé "candidata").
- Direitos pendentes, sensibilidade ou risco de PI.
- Defeito editorial detectado após inclusão → condicionado/excluído até correção.
- Mudança de método, corpus ou interpretação → nova versão, não correção silenciosa.

## 16. Regra de alteração pós-corte

- Correção apenas de metadado no Zenodo: registrar a mudança.
- Erro material em arquivo: preparar nova versão (New version), preservando relação.
- Inclusão de nova ficha ou novo eixo: edição posterior.
- Nenhuma substituição silenciosa de arquivo congelado.
- Mudança após o corte exige nova versão, nunca alteração silenciosa (princípio 8 da tarefa 00).

---

**Status:** RASCUNHO para H2 — aguardando decisão de Fabio Takwara.
