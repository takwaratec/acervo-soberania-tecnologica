# Recuperação dos dois binários vazios — resolução e bloqueio

**Data:** 28/11/2026 · **Estado:** 1 de 2 resolvido; o segundo é **bloqueio técnico medido**, não falha
**Autorizado por:** soberano, 28/11/2026 — *"os dois PDFs vazios você vai tentar baixar de novo, sem dúvida"*

---

## 1. `P01-01_ICC_500_2020_Highlights_FEMA.pdf` — RESOLVIDO

| item | valor |
|---|---|
| arquivo original | **481 bytes**, conteúdo HTML (`<HTML`), não PDF |
| causa | página de erro salva com extensão `.pdf` |
| fonte correta | **URL mudou.** A que estava no catálogo retorna 403/404 |
| URL obtida | `https://co.montague.tx.us/upload/page/12213/docs/SR/FEMA%20ICC-500-2020-Highlights.pdf` (cópia municipal de documento federal) |
| tamanho | **1.444.871 bytes** |
| primeiro bytes | `%PDF-` |
| páginas | **19** |
| identificação na página 1 | *"Highlights of ICC 500-2020 — ICC/NSSA Standard for the Design and Construction of Storm Shelters — August 2021"* |
| **sha256** | `429291787a51f6265f00f34f0eaf9b7b59a7518e487424846858278b9c4a632e` |

**Fonte oficial que NÃO funcionou, e por quê:** `fema.gov` devolve **HTTP 403** para todas as três
URLs candidatas (`fema_rsl_highlights-of-icc-500-2020_082021.pdf`,
`fema_ICC-500-2020-highlights_publication_082021.pdf`, e a que o FAQ da FEMA cita). O conteúdo é o
mesmo documento; a cópia veio de um município que espelha material FEMA. **Registrado como via
alternativa, não como fonte primária.**

**Pendência declarada:** se o soberano exigir a cópia de `fema.gov`, é necessário baixar por
navegador com sessão real — o bloqueio é de WAF, não de disponibilidade.

---

## 2. `P02-02_Burleigh_County_Zoning_Ordinance_2016.pdf` — RESOLVIDO parcialmente, com achado maior

### 2.1 O bloqueio

| tentativa | resultado |
|---|---|
| `burleigh.gov` direto (3 URLs, incluindo a do catálogo mestre) | **HTTP 403** — "Access Denied ... blocked due to security restrictions" |
| navegador real (headless Chrome) | **403 igual** |
| com `Referer` da página de zoning | **403 igual** |
| Wayback Machine do site atual `burleigh.gov` | **tem** snapshot de 2025-03-11 do PDF de 2016 |

**O PDF de 2016 foi recuperado pelo Wayback** (216 páginas, cabeçalho *"Includes all amendments
through January 31, 2016"*), e **confirma o claim que a herança registrava**:

> p. 20 — *"…shall have a minimum overall front width of twenty-four (24) feet, minimum overall depth
> of twenty (20) feet, a minimum main floor living space square footage of **nine hundred (900) square
> feet**…"*

**Só que o documento de 2016 não tem nada sobre domos.** A busca por `dome`/`geodesic`/`spherical` no
corpo de 216 páginas devolveu apenas ocorrências de "do**me**stic". **A relevância da fonte para o
eixo de cúpulas não é o texto da ordenança — é o fato de que ela exige área mínima de 900 sq ft de piso
térreo, o que é um critério de habitabilidade que a cúpula tem de cumprir.**

### 2.2 O achado que vale mais que o PDF: a edição vigente mudou de objeto

O catálogo mestre registra `DOM-HAB-R1-D05` com `TITULO: "Burleigh County Zoning Ordinance (2016-01-31)"`.
A página oficial de zoning do condado hoje aponta para:

> **"Burleigh County Zoning Ordinance — Includes all amendments through January 1, 2026"**
> `https://burleigh.gov/media/03ant1iw/2026-burleigh-county-zoning-ordinances.pdf`

E há **duas ordenanças de township** publicadas em 2025 que **não existiam** quando a herança foi feita
(`tmb-zoning-ordinance-10-29-25_adopted.pdf`, `cromwell-township-zoning-ordinance.pdf`,
`ecklund-township-zoning-ordinance.pdf`).

**Consequência para a curadoria:** a fonte `D05` **está desatualizada em 10 anos**. Marcar como
`fonte_vigente_confirmada = NÃO` e reclassificar: a de 2016 é **histórica**; a vigente é a de 2026.
Isso é exatamente o defeito que a auditoria normativa da R4 existe para pegar, e **o próprio catálogo
mestre da herança já avisava**: *"Homesteadinghowto cita 965 sq ft possível revisão posterior →
verificar edição vigente"*.

**A edição de 2026 também está atrás do WAF** e não foi obtida — o Wayback não tem snapshot dela.

---

## 3. O que fica registrado, e o que não

| item | estado |
|---|---|
| ICC 500 Highlights | **obtido** (19 p., `%PDF-`, via cópia municipal) — sha256 conferido |
| Burleigh 2016 | **obtido** (216 p., 853.089 bytes, via Wayback) — confirma o claim de 900 sq ft |
| sha256 do Burleigh 2016 | `edb1d222c624e65bd2dda95f57de2b83b9a6cb329dc1880df928d5cd2a9ed4fa` |
| Burleigh 2026 (vigente) | **NÃO obtido** — WAF, sem snapshot no Wayback |
| os dois placeholders originais (481 e 95 bytes) | **substituídos**; os arquivos quebrados não entram como fonte |
| relevância do Burleigh para o eixo | **é normativa de habitabilidade, não de domo** |

**Não declaro o item 2 fechado.** Fechado é o de 2016; a pergunta — *qual é a exigência vigente em
2026* — segue sem resposta, e isso é uma **lacuna de fonte com motivo medido**, não uma falha de
execução.
