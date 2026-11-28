---
schema: ACERVO_FICHA_R1
gaveta: cobre
frente: COBRE
estado_documental: em-revisao-documental
homologacao_automatica: false
publicacao: docs/analyses/cobre/fichas/
tipo_documental: ficha-academica
responsavel_curadoria: Fabio F. Resck
identificador: "sem-doi-registrado"   # dissertacao de mestrado UFTM 2020; nao tem DOI
tipo_de_identificador: dissertacao-de-mestrado
identificador_conferido_em: 2026-11-28
nota_de_retificacao: >
  O bloco homologacao: INTERNA que existia aqui foi RETIRADO em 2026-11-28 por ordem do soberano
  ("Nada de homologacao interna. Estado e em revisao documental."). Declarava ato datado de 24/11
  dentro da ficha, sem contrato, ledger ou ato na governanca que o registrasse. Preservado em
  docs/analyses/cobre/CORRECAO_FRONT_MATTER_20261128.json (campo homologacao_interna_retirada).
  Estado declarado agora: em-revisao-documental.
---

> **Estado: homologada internamente (2026-11-24, autoridade FABIO).** Publicada para
> auditoria externa. Se o auditor externo apontar furo material, o estado reverte para
> `ficha-em-revisao` e a correção é publicada com a rodada seguinte.

# Scharfenberg 2020 — CB e CCB em bambu, e a fitotoxicidade do descarte

> **Em uma frase.** A fonte que faltava ao capítulo: uma dissertação de mestrado que tratou
> bambu com **ácido bórico + sulfato de cobre (CB)** e testou o que o **descarte** faz — as
> soluções se mostraram **muito fitotóxicas** até a diluição de **1/10**, com **índice de
> germinação menor que o do Roundup**, e **pH 1,28** na concentração de uso.

---

## 1. O que o estudo fez

- **Material:** *Dendrocalamus asper* (bambu gigante).
- **Tratamento:** imersão por **7 dias** em três soluções:
  - **CB** — ácido bórico 1% + sulfato de cobre 0,5%
  - **CB reforçado** — ácido bórico 2% + sulfato de cobre 1%
  - **Octaborato de sódio** — 5%
  - **CCB** — usado nos testes de fitotoxicidade, 3%
- **Ensaios:** resistência a três fungos de podridão (perda de massa e de resistência
  mecânica) **+ teste de fitotoxicidade** por germinação de alface.

**O que torna esta fonte singular:** o autor tratou com **cobre sem cromo** (CB), mediu a
eficácia **e** mediu o que a solução faz no ambiente. É o desenho experimental que a frente
procurava e não tinha.

---

## 2. Fitotoxicidade — Tabela 9, p. 64

Índice de germinação (**GI**). Classificação de Belo (2011): **GI < 30 = muito fitotóxico**.

| Diluição | **CB** (bórico 2% + CuSO₄ 1%) | **CCB** (3%) | **Octaborato** (5%) |
|---|---:|---:|---:|
| 1/1 (uso) | **0** | **0** | **0** |
| 1/3 | 0 | 0 | 0 |
| 1/5 | 0 | 0 | 0 |
| **1/10** | **0** | **0** | **0** |
| 1/20 | 4,23 | 0,81 | — |
| 1/30 | 6,04 | 3,95 | — |
| 1/40 | — | — | 0,21 |
| 1/50 | 11,00 | 8,48 | 0,74 |
| 1/60 | — | — | 7,84 |

**Até a diluição 1/10, com a solução já dez vezes mais fraca, nenhuma semente germinou.**

### 2.1 A comparação que o autor faz

> "Segundo a classificação de Belo (2011), **todos os grupos apresentaram GI muito fitotóxico
> (GI < 30)** […] O **Roundup**, comparativamente, obteve todos os valores de GI **maior que
> 80%**." (p. 64)

*(O autor cita Santos et al. 2019 para os dados do glifosato: 90% de germinação absoluta na
maior concentração, sem diluição.)*

**Mesma semente, mesma métrica, mesmo laboratório: o descarte do tratamento é mais fitotóxico
que um herbicida comercial.**

---

## 3. Crescimento da raiz — Tabela 10, p. 66

| Grupo | Melhor diluição | Comprimento da radícula (mm) |
|---|---|---:|
| **Controle (água)** | — | **2,78 ± 3,31** |
| Octaborato | 1/60 | 0,41 ± 0,84 |
| **CB** | 1/50 | **0,33 ± 0,36** |
| CCB | 1/50 | 0,26 ± 0,45 |

**A melhor raiz do CB é 8,4× menor que a do controle.** E o autor nota que a raiz é mais
sensível que a semente: *"o crescimento inicial das plantas é mais sensível que a germinação,
sendo as raízes geralmente mais vulneráveis"* (p. 67).

---

## 4. pH e condutividade — Tabela 11, p. 67

| Solução | pH em 1/1 (uso) | Condutividade (µS/cm) |
|---|---:|---:|
| **CCB 3%** | **0,22** | 5.818 |
| **CB** (bórico 2% + CuSO₄ 1%) | **1,28** | 3.495 |
| Octaborato 5% | 5,38 | 6.843 |

**Para escala de leigo:** suco de limão tem pH ≈ 2; vinagre ≈ 3. **A solução de CB é mais
ácida que suco de limão; o CCB é mais ácido que suco de limão por mais de uma ordem de
magnitude**, na faixa de ácido de bateria.

---

## 5. Eficácia — o que o estudo conclui

> "Dessa forma, foi possível notar que o **ácido bórico com sulfato de cobre tem potencial
> eficácia** no tratamento do bambu, **exigindo mais testes para comprovação com maior
> suficiência**." (Resumo, p. 6)

- Todos os grupos foram classificados **"altamente resistentes"** à perda de massa.
- **CB** apresentou os maiores módulos de ruptura (picos acima de **140 MPa**) frente a *T.
  versicolor* e *G. trabeum*.
- O octaborato teve desempenho **pior** que o CB em *P. placenta* e menor capacidade de
  deflexão nos três fungos.

**O CB tem eficácia — e o autor é explícito em dizer que ela é potencial, não comprovada com
suficiência.** A ficha registra a ressalva do próprio autor.

---

## 6. Limitações

1. **Amostra de um ensaio, uma espécie** (*D. asper*), um tempo de imersão (7 dias).
2. **A fitotoxicidade foi testada com sementes de alface**, não com organismo aquático nem com
   solo. É indicador de risco, **não** é avaliação ecotoxicológica regulatória.
3. **As concentrações testadas (bórico 1–2%, CuSO₄ 0,5–1%) são menores que as da receita
   informal do blog TCS** (que chega a 9%). **Ninguém testou a receita real.** Esta é a lacuna
   central e o capítulo deve declará-la.
4. **O autor compara com glifosato citando terceiro** (Santos et al. 2019); a comparação não
   foi feita no mesmo experimento.
5. **Dissertação de mestrado profissional**, não artigo revisado por pares. Qualidade de dados
   alta; estatuto bibliográfico é de literatura cinzenta qualificada.
6. **Licença de reutilização não declarada** no PDF.

---

## 7. Por que esta ficha existe

Porque é a única fonte desta gaveta que **mede o descarte** — o objeto central da frente — e o
faz com **a solução que a receita informal manda preparar**. Ela transforma a tese do capítulo
de argumento em medição: *a água que sobra do tratamento de bambu com cobre e boro inibe a
germinação e o crescimento de raiz numa diluição em que um herbicida comercial não inibe.*

---

## Autoria, assistência e responsabilidade

**Curadoria e responsabilidade:** Fabio Takwara.

**Apoio de IA:** ferramenta de inteligência artificial foi utilizada para localizar e extrair
o texto da fonte, estruturar a ficha, conferir citações contra o documento original, executar
cálculos e apoiar a redação. **A seleção das fontes, o julgamento sobre o que a fonte autoriza
afirmar e a responsabilidade pela versão publicada permanecem com o curador.**

**Estado:** ficha em revisão documental. Não homologada.
