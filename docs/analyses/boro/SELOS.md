---
schema: ACERVO_INDICE_R1
gaveta: boro
frente: BORO
titulo: "Selos da frente do boro"
tipo_documental: indice
estado_documental: em-revisao-documental
homologacao_automatica: false
responsavel_curadoria: Fabio Takwara
assistencia_documental: agente de IA, sujeito a revisao humana
---

# Indice de selos — BORO

Um selo e um **par**: manifesto de auditoria + resposta de hashes, no mesmo commit. O indice conta por
caminho no historico, nunca por mensagem de commit — contagem por mensagem ja fez um indice desta casa
dizer 19 quando havia 28.

| alvo (commit de conteudo) | sha256 do manifesto | sha256 da resposta | data | commit onde o par vive |
|---|---|---|---|---|
| `560815d2` | `ee3e0e129b523f88…` | `7fffdadb43da9b1d…` | 2026-11-25T20:20:00Z | `(este commit)` |

O ultimo selo entra marcado `(este commit)`: o commit nao pode nomear a si mesmo. A regeneracao seguinte
substitui a marca pelo hash real.

Total de selos indexados: **1**. Orfaos: **0**.
