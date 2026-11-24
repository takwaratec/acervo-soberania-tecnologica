# HANDOFF — Frente BORO

**Gerado em:** 2026-11-24
**Para:** abrir tópico novo sem repetir contexto
**Regente atual:** Hermes
**Estado da frente:** ABERTA, gaveta criada, capítulo introdutório commitado, **não homologado**

---

## 1. O que o soberano pediu (mandato original, verbatim resumido)

Investigar o **boro** sob domínio R4/MTCC:

1. Quanto de boro o Brasil importa — agricultura e usos industriais (tinta, papel, fibra de vidro).
2. Quantos medicamentos têm boro na composição e **qual a dosagem**.
3. O quanto se usa numa cápsula de consumo humano vs. na agricultura vs. na preservação de bambu.
4. Alertar para o **risco da dosagem**.
5. O boro **não é tratamento estável**: lixivia, não suporta umidade, dissolve. (intuição do soberano, confirmada)

**Recorte declarado pelo soberano:** esta gaveta é o **capítulo introdutório** da série
"tratamentos convencionais do bambu". Depois virão: **sulfato de cobre** (capítulo próprio),
CCA, CCB, vernizes voláteis, acabamentos acrílicos, concreto.

**Decisão de recorte já tomada:** sulfato de cobre, CCA e CCB **não entram** nesta gaveta.
CCA/CCB aparecem só como contraste normativo.

---

## 2. Estado real do repositório (verificado, não presumido)

```
Repo canônico acervo:  /Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica
Branch:                hermes/mtcc-peca-decisao-20261121
HEAD:                  383b0be  docs(boro): abre a gaveta boro com estado da questao do preservante
Ledger R4 (frentes):   worktree /Users/fabiotakwara/Takwara/worktrees/gaveta-gw-r4-r1
Ref do ledger:         r4-claims  (HEAD ecaa7153 "R4 abre frente BORO por FABIO_SOBERANO")
```

**Atenção — armadilha:** o ledger **não** está no working tree nem no HEAD do worktree.
Ele vive na ref `r4-claims`. `git log` normal não mostra `frentes_abertas/BORO.json`.
Para conferir: `git show r4-claims:frentes_abertas/BORO.json`.

**Arquivo alheio modificado no repo (NÃO é desta frente, não tocar):**
`docs/analyses/bambu-estrutural/ficha-heat-treatment-pdms-bamboo.md` — já estava `M` antes
desta sessão.

---

## 3. Frente BORO no ledger

```json
{
 "front": "BORO",
 "repo": "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica",
 "write_scope": ["docs/analyses/boro",
                 "_privado/governanca-operacional/extracoes/boro"],
 "aberta_por": "FABIO_SOBERANO",
 "aberta_em": "2026-11-24T11:47:11Z",
 "origem": "TOPICO_ABERTO_PELO_SOBERANO"
}
```

Aberto pelo executor real: `python3 ops/command-center/transicao-r4/runner/r4_runner.py --repo . abrir-frente ...`

---

## 4. Artefatos produzidos

### 4.1 Públicos (versionados, commitado em `383b0be`)

| Caminho | Bytes | SHA-256 (16) |
|---|---|---|
| `docs/analyses/boro/00-estado-da-questao-boro.md` | 24.530 | `304ccf98e5ab2260` |
| `docs/analyses/boro/index.md` | 2.949 | `cb84903c11c0d201` |
| `docs/analyses/boro/INVENTARIO_GAVETA.json` | 659 | `c4dfeedcb0e75541` |

### 4.2 Privados (fora do git por `.gitignore:28 _privado/`)

Raiz: `_privado/governanca-operacional/extracoes/boro/`

| Arquivo | Bytes | SHA-256 (16) |
|---|---|---|
| `HERANCA_MANIFEST.json` | 9.804 | `3e199c200a694833` |
| `FONTES_NOVAS_MANIFEST.json` | 1.224 | `b2139e4d9a248803` |
| `INVENTARIO_FONTES.json` | 1.691 | `b9e6ab97bd052a5e` |

**Herdado:** 42 arquivos, 16 PDFs, **zero divergências de hash** (reverificado por leitura própria).
Originado de dois pacotes existentes:

- `_privado/fontes-documentais/ago_28_Boratos_Cobre` — 10 PDFs / 301 páginas, gate C02 fechado,
  10 fichas em `em-revisao-documental`. **Mistura boro e cobre.**
- `_privado/fontes-documentais/ago_28_CCA_CCB` — 6 PDFs. É a fonte do CCA/CCB, **não** é desta gaveta.

**Fontes novas custodiadas nesta rodada (3):**

| ID | PDF | SHA-256 (16) | Serve para |
|---|---|---|---|
| `USGS-MCS2026-BORON` | 115.584 B | `a7606ad4a3c2b0b2` | reservas, produção, importação EUA, usos, mineral crítico |
| `BVS-ANVISA-RDC199-2006` | 157.537 B | `91f19e4458c324a4` | água boricada 3%, dose tópica, restrição adultos/crianças |
| `EMA-BORIC-BORATES-EXCIPIENTS-2021` | 1.376.513 B | `0bdd9aaa3fb35df2` | PDE por faixa etária, BMDL₀₅, efeito crítico |

Todos com `.extracao.md` ao lado, extraídos com `~/.venvs/pdf/bin/python` (PyMuPDF).

---

## 5. Resultado científico — as quatro afirmações submetidas à verificação

Este é o núcleo que **não deve ser refeito**.

| Afirmação do soberano | Veredito | Evidência |
|---|---|---|
| Boro veio de explosões estelares | **CONFIRMADO no mecanismo, CORRIGIDO no autor** | Não é nucleossíntese estelar — estrelas **destroem** boro. Origem: espalação por raios cósmicos sobre CNO no meio interestelar. Supernova = aceleradora. |
| Maiores jazidas: Yellowstone e Paquistão | **NÃO CONFIRMADO** | USGS aponta Mojave (EUA), cinturão Alpide, cinturão Andino. Não lista nenhum dos dois. |
| Grande parte do boro vai para foguetes | **INVERTIDO em volume, CORRETO em prioridade** | >3/4 do consumo: cerâmica, detergente, fertilizante, vidro. Aeroespacial é nicho real mas massa desprezível. |
| Arquiteta alemã do Green School | **CONFIRMADO, corrigido gênero/especialidade** | **Jörg Stamm**, homem, construtor-arquiteto de bambu, Olpe-Alemanha. Contratado por John Hardy em 2004. Ressalva: Linda Garland + Walter Liese já tratavam com borax em Bali nos anos 90. |

**Achado que fortalece o argumento do soberano por outro caminho:** a USGS declara recursos
**adequados ao futuro previsível** — logo a insustentabilidade **não** é escassez física, é
**concentração geopolítica** (90% das importações dos EUA vêm da Turquia; Turquia detém 87,5%
das reservas listadas; boro entrou na lista crítica dos EUA em 2025).

---

## 6. As cinco réguas de dosagem (todas ancoradas, exceto uma)

| Régua | Unidade | Valor | Fonte | Status |
|---|---|---|---|---|
| Tópica medicinal BR | % do sal | água boricada 3% (2,900–3,200% H₃BO₃), 2–3×/dia, só adultos | ANVISA RDC 199/2006 | **ancorado** |
| Sistêmica medicinal UE | mg B/dia | PDE 1 (0–2a) · 3 (2–12a) · 7 (12–18a) · **10 (adulto)** | EMA/CHMP/765436/2012 | **ancorado** |
| Suplemento humano | mg B/cápsula | 0,15–6 (típico), UL 20 mg/dia | NIH ODS | **NÃO ANCORADO** (HTTP 403) |
| Agricultura | % do consumo | 11–15% do boro mundial | USGS / estudo UE CRM | **ordem de grandeza** |
| Preservação de bambu | kg/m³ | AWPA 2,7 · IS 401 5 · **medido 14,79 (5%) e 21,79 (8%)** | Gauss 2020, p. 89 | **ancorado** |

**Cadeia toxicológica:** efeito crítico = **toxicidade do desenvolvimento** (rato).
BMDL₀₅ **10,3 mg B/kg/dia** → MRL ATSDR **0,2 mg B/kg/dia** → PDE adulto **10 mg B/dia**
(fator de incerteza 66). Classificação CMR **Repr. cat. 2**.

**Conversão que a ficha trava:** B é 17,5% da massa de H₃BO₃ → 10 mg B = 57,2 mg de ácido bórico.
Converter ao contrário subestima risco por fator de ~6.

**O argumento de dosagem:** recomendação normativa 2,7 kg/m³ vs. prática medida 14,79–21,79 kg/m³
= **3 a 8× a norma**, e quem aplica banho por percentagem de solução não sabe sua retenção real.

---

## 7. Validação já executada (não repetir)

- **19/19 números** da ficha conferidos por busca literal contra a fonte custodiada. Zero falhas.
- **Aritmética revalidada:** Turquia/soma = 87,5% ✓ · 10 mg B = 57,2 mg H₃BO₃ ✓ · 6 mg B = 60% do PDE adulto e 2× o PDE de criança ✓.
- **42 arquivos herdados:** sha256 recalculado, **0 divergências**.

---

## 8. Lacunas — o que o soberano pediu na ÚLTIMA mensagem

O soberano respondeu "vamos fazer as duas coisas" e listou, textualmente:

> fechar as lacunas sobre **importação** e a **exposição ocupacional** e a **legislação no mundo**,
> como é tratado o boro, a sua **classificação**, quais são as **restrições**, quais os **estudos
> apontam toxicidade humana**, **áreas de risco**, **pequenas jazidas na América do Sul** — talvez
> no Chile, Argentina — e as **implicações do descarte inadequado** e do **contato com a pele e a
> respiração**, sobretudo a **respiração de poeira de bambu tratado, cortado, serrado**, sem o
> cuidado adequado.

E decidiu também **abrir a gaveta do sulfato de cobre em paralelo**, com tópico próprio.

### 8.1 Trabalho já iniciado e interrompido

**ComexStat (MDIC) — API oficial respondeu 200.** Endpoint validado:

```
https://api-comexstat.mdic.gov.br/general?flow=import&year=2024&month=1&ncm=2810
```

Anos disponíveis: 1997–2026. **Nenhum dado brasileiro foi extraído ainda.** NCMs de interesse:

| NCM | Descrição |
|---|---|
| `2528` | boratos naturais e concentrados (exceto de salmouras) |
| `2810` | óxidos de boro; ácidos bóricos |
| `2840` | boratos (tetraborato de sódio, etc.) |

### 8.2 Lista de lacunas a fechar

| # | Lacuna | Fonte a buscar | Estado |
|---|---|---|---|
| 1 | Importação brasileira de boro por NCM, série histórica | API ComexStat (validada) | **não iniciado** |
| 2 | Dose de suplemento humano | NIH ODS (403 — tentar via curl com UA ou fonte espelho) | bloqueado |
| 3 | Legislação mundial: classificação e restrições (CLP/UE Repr. 1B, TSCA/EUA, outras jurisdições) | Eur-Lex CLP, EPA | não iniciado |
| 4 | Estudos de toxicidade humana e áreas de risco | ATSDR ToxProfile tp26 (já citado indiretamente) | não iniciado |
| 5 | Pequenas jazidas América do Sul (Chile, Argentina) | USGS MCS2026 já tem produção; falta detalhe de jazida | parcial (só produção/reserva) |
| 6 | Descarte inadequado: destino de efluente do banho | CONAMA 430 (já herdado: 5,0 mg B/L) + literatura | parcial |
| 7 | Contato dérmico e inalação de poeira | EMA (já cobre dérmico parcialmente) | parcial |
| 8 | **Poeira de bambu tratado cortado/serrado** — sílica + boro + particulado | **nenhuma fonte custodiada** | **zero** |
| 9 | EPI / exposição ocupacional de operadores BR e China | **nenhuma fonte custodiada** | **zero** |

**Itens 8 e 9 são as lacunas materiais.** Nenhuma das 10 fichas herdadas mede trabalhador —
todas são de água, efluente ou produto. Esta é a pendência de pesquisa mais importante da gaveta.

---

## 9. O que foi decidido sobre dividir o contexto

Recomendação registrada ao soberano: **sim, abrir tópico novo para o CÓBRE**, por higiene causal.

Motivo concreto: boro e cobre têm toxicologia **oposta** — cobre é micronutriente essencial e
ecotóxico aquático a 1–2 µg/L; boro é toxicidade do desenvolvimento na casa de mg B/kg/dia.
O pacote herdado **já mistura fichas dos dois** no mesmo diretório, e isso virou pendência
declarada (item 7 da ficha). Frentes separadas forçam a separação que o acervo precisa.

**BORO fica neste tópico. CÓBRE vai para tópico novo.**

---

## 10. Regras que valem neste trabalho (para não errar no tópico novo)

1. **Toda etapa na `main`**; frente isolada só se declarada.
2. **Nunca expor `_privado/`** — PDF, extração, tabela/ficha derivada de artigo ficam privados.
3. **Não presumir homologação.** Estado honesto é `em-revisao-documental`, `homologacao_automatica: false`.
4. **Hash não é homologação.**
5. **Não transportar valor entre meios** (água potável ≠ corpo receptor ≠ efluente ≠ solo ≠ lixiviado ≠ material).
6. **Preservar divergência**, não harmonizar. Ex.: Liu 9,15% vs 9,18±0,14%.
7. **Commit/push/PR/merge só com OK explícito do soberano.** Self-approve bloqueado.
8. **Auditor externo (Teco/Luna) é opcional**, não regra de aceite.
9. **Não inventar** e-mail, DOI, licença ou número. Pendência declarada > valor plausível.
10. Scripts Python: **`~/.venvs/pdf/bin/python`** (PyMuPDF 1.24.14). O Python 3.15 do host **não** instala pymupdf4llm.

---

## 11. Defeitos encontrados que o próximo executor deve saber

1. **`validar_gaveta()` e `GAVETAS_R4.json` NÃO EXISTEM no código.**
   A skill `acervo-gaveta-custodia` descreve ambos como se estivessem implementados.
   Grep em todo o repo não encontra nada. O executor real tem `abrir_frente()` e **não** valida
   gaveta contra registro nenhum. **Não confie na skill nesse ponto** — ela descreve intenção,
   não código. (Skill a corrigir.)

2. **`web_extract` está quebrado nesta instalação** — backend `openai-native` é *search-only*:
   `"cannot extract URL content. Set web.extract_backend to firecrawl, tavily, keenable, exa, or parallel."`
   **Workaround que funciona:** `curl -sL -o arquivo.pdf URL` + extração local com PyMuPDF.
   Melhor para custódia de qualquer forma.

3. **Ponteiro de runtime R4 diverge do registro.** `r4-active-regency.json` pinа
   `ledger_registry_sha256=ab0df624…`; o arquivo em disco dá `a62fb36b…`.
   Pela regra das três camadas, isso é **NÃO SEI**. Não foi tocado. **Não "consertar" sem ordem.**

4. **`_privado/RASTREABILIDADE_PRIVADO.md` e `RASTREABILIDADE.md` não existem.**
   Não há registro vivo de custódia do material de boro. Se a frente exigir rastreabilidade,
   ela precisa ser criada.

5. **O diretório correto do repo canônico** é `~/Documents/GitHub/acervo-soberania-tecnologica`.
   `~/Takwara/worktrees/acervo-soberania-tecnologica` existe mas **não é** repositório git —
   é cópia morta. Não trabalhar lá.

---

## 12. Próximo passo imediato (retomar daqui)

1. Extrair ComexStat para NCM 2528, 2810, 2840, série 2015–2026, fluxo importação.
   API já validada. Gravar em `_privado/governanca-operacional/extracoes/boro/fontes_novas/`.
2. Buscar ATSDR ToxProfile tp26 (toxicidade humana, áreas de risco) e CLP/Eur-Lex
   (classificação Repr. 1B, restrições).
3. Buscar literatura de **poeira de bambu** (sílica + boro + particulado respirável) e
   exposição ocupacional em indústria de bambu na China.
4. Atualizar `00-estado-da-questao-boro.md` com as seções 9 (ocupacional) e nova seção de
   importação brasileira — hoje ambas são lacuna declarada.
5. Só depois: reprocessar as 10 fichas herdadas pelo MTCC (estágios 3–8), separando boro de cobre.

---

## 13. Comando para retomar (colar no tópico novo)

```
Leia o handoff em /Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica/docs/analyses/boro/HANDOFF_BORO_20261124.md
e continue a frente BORO do ponto "Próximo passo imediato".
Frente já aberta no ledger (ref r4-claims, commit ecaa7153). Não reabrir.
Comece pelo ComexStat: NCM 2528, 2810, 2840, importação, série histórica.
```

---

**Este handoff não é homologação, certificação nem autorização de publicação.**
