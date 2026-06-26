# AGENTS.md — Análises e Escrita Científica

## Identidade

Repositório central de **fichas técnicas, estados da arte, resenhas científicas e materiais didáticos** que embasam todos os projetos do ecossistema Takwara.

**Site:** https://takwaratec.github.io/Analises-e-escrita-cientifica/

---

## Objetivo do Agente

Ao ser acionado neste repositório, seu papel é:

1. **Manter fichas técnicas atualizadas** — cada ficha baseada em material bruto original (PDF, tese, artigo)
2. **Organizar por eixos temáticos** — ECOSALA, Tecnologia Takwara, Bioeconomia, HIS, APO, Política Habitacional, Grandes Obras
3. **Referenciar projetos irmãos** — Vaga Lúmen (FINEP), MST Mário Lago (Juventude Solidária), Mulheres_Bioeconomia_Amazonia (Zenodo)
4. **Aplicar a triagem dos 200+ Prompts** — metodologia padronizada de análise: extração → mapeamento → referencial → metodologia → achados → crítica → estado da arte
5. **Garantir integridade científica** — DOIs verificados, ABNT, sem fabricação de citações

---

## Estrutura do Repositório

```
📂 docs/
├── index.md                    → Página inicial com cards de navegação
├── sobre.md                    → Propósito do repositório
├── metodologia.md              → Protocolo 200+ Prompts
├── assets/                     → CSS customizado
├── prompts/                    → Metodologia de escrita
└── analyses/
    ├── index.md                → Portal das análises
    ├── artigo-bambu-potencial-bioeconomia.md
    ├── ecosala/                → Fichas do grupo ECOSALA (11 membros + tecnologias)
    ├── tecnologia-takwara/     → Bambu, PU vegetal, compósitos, patentes (65 fichas)
    ├── bioeconomia-amazonica/  → Cadeias sociobiodiversidade, MQTF (23 fichas)
    ├── percecao-social/        → HIS, satisfação habitacional (7 fichas)
    ├── avaliacao-pos-ocupacao/ → APO, conforto ambiental (5 fichas)
    ├── politica-habitacional/  → PMCMV, ATHIS, direito à moradia (5 fichas)
    └── grandes-obras-amazonia/ → Reassentamentos, hidrelétricas (5 fichas)
```

---

## Repositórios Irmãos

| Repositório | Conteúdo | Público |
|---|---|---|
| `github.com/takwaratec/ECOSALA` | Coletivo de 11 membros — atas, projetos | Grupo de pesquisa |
| `github.com/takwaratec/fundo-vaga-lumen-2026` | Proposta FINEP Mais Inovação | FINEP/avaliadores |
| `github.com/takwaratec/plataforma-juventude-solidaria-2026` | Viveiro-Educador Terra Viva (MST) | MST Mário Lago |
| `github.com/takwaratec/projetos` → `Mulheres_Bioeconomia_Amazonia` | Zenodo DOI: 10.5281/zenodo.18827106 | Acadêmico |

---

## Ferramentas Disponíveis

| Ferramenta | Função | Status |
|---|---|---|
| **Pandoc** | DOCX/ODT → MD | ✅ |
| **PyMuPDF** (fitz) | Extração de texto de PDFs | ✅ |
| **python-docx** | Leitura/escrita DOCX | ✅ |
| **ffmpeg** (conda) | Conversão de áudio (opus → wav) | ✅ |
| **faster-whisper** | Transcrição de áudio | ⏳ Pendente (rede) |
| **pdfplumber** | PDF tabular | ⏳ Pendente (rede) |

**Workaround áudio:** Gateway Telegram já transcreve automaticamente.

---

## Convenções para o Agente

### Fichas técnicas
- Cada ficha deve ter **fonte verificada** (DOI, PDF original, link)
- NUNCA fabricar citações — atribuir sempre com honestidade
- Formato: tabela de dados → análise → referências ABNT
- Incluir data de elaboração e fonte

### Fluxo de trabalho
1. `git pull` — sincronizar
2. Fazer alterações
3. `git add + git commit -m "tipo: descrição"` + `git push`
4. `mkdocs gh-deploy --clean` (se alterou docs/)

### Triagem (200+ Prompts)
Ao analisar um novo artigo/PDF:
1. Extrair texto bruto (PyMuPDF)
2. Mapear estrutura do documento
3. Analisar referencial teórico
4. Avaliar metodologia
5. Extrair achados principais
6. Avaliação crítica
7. Inserir no estado da arte

---

## Acervo em Números

| Indicador | Total |
|---|---|
| Fichas técnicas | ~80 |
| Catálogo IFB | 84 referências |
| Eixos temáticos | 7 (ECOSALA + 6 originais) |
| MAMONEX RD70, UG 132A, RQI | 3 fichas Imperveg |
| Período coberto | 1998–2025 |

---

*AGENTS.md mantido pelo Hermes Agent · Tecnologia Takwara · 2026*
