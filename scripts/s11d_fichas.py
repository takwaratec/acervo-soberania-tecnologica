#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera a ficha da custódia S11-d — a IN Ibama 5/92, que diz o que fazer com o resíduo."""
import hashlib
import json
import os

RAIZ = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica"
FONTES = f"{RAIZ}/_privado/fontes-documentais/ago_28_Madeira_Tratada_S11d"
DEST = f"{RAIZ}/_privado/fichas/ago_28_Madeira_Tratada_S11d"

MAN = {e["chave"]: e for e in json.load(open(f"{FONTES}/MANIFEST_S11D.json", encoding="utf-8"))["entradas"]}

CABECALHO = """---
schema: ACERVO_FICHA_R1
gaveta: cobre
frente: COBRE
estado_documental: homologado-internamente
homologacao:
  tipo: INTERNA
  autoridade: FABIO
  data: 2026-11-24
  instrumento: "instrução direta do soberano no tópico da frente COBRE"
  transcricao: >
    "Sim, você vai colocar como homologação interna. Internamente nós estamos homologando.
    Se o auditor externo disser que não, nós alteramos o status."
  alcance: >
    Homologação INTERNA: vale dentro do acervo e autoriza a publicação. NÃO é homologação
    científica por par, NÃO é homologação regulatória e NÃO substitui a auditoria externa.
    O estado reverte para ficha-em-revisao se o auditor externo apontar furo material.
  auditoria_externa: PENDENTE
homologacao_automatica: false
fonte:
  arquivo: {arquivo}
  sha256: {sha}
  paginas: {paginas}
  fonte_url: {url}
  custodia: _privado/fontes-documentais/ago_28_Madeira_Tratada_S11d/
publicacao: docs/analyses/cobre/fichas/
---

> **Estado: homologada internamente (2026-11-24, autoridade FABIO).** Publicada para
> auditoria externa. Se o auditor externo apontar furo material, o estado reverte para
> `ficha-em-revisao` e a correção é publicada com a rodada seguinte.

"""

DECL_IA = """
---

## Declaração de uso de IA

**Apoio de IA.** Esta ficha foi produzida com apoio de IA (Hermes Agent), que localizou o
documento, preservou os bytes do original, extraiu o texto com marcador de página, conferiu
cada citação contra o extrato por busca literal, executou os cálculos e estruturou a
redação. A seleção interpretativa, a perspectiva e a responsabilidade pela versão publicada
permanecem com o autor.
"""

CORPO = """
## 1. O que o documento é

**Instrução Normativa nº 5, do Ibama, de 20 de outubro de 1992**, publicada no DOU de
21.10.1992. Ela **disciplina os procedimentos** exigidos pela Portaria Interministerial
292/89: como se registra a empresa, como se registra o produto, como se cadastra a usina,
como se rotula, e — o que interessa a esta gaveta — **como se destina o resíduo**.

Quinze páginas. Não é norma nova: é o **manual de execução** da Portaria de 1989.

**Como ela apareceu nesta rodada.** Na custódia S11-c, esta Instrução foi declarada
**pendente**, com o motivo "a página do DOU de 21/10/1992 separada não trazia o ato". Isso
estava errado: o ato está no DOU daquela data e é hospedado pela ABPM. A pendência foi
fechada — e ela continha exatamente o que a peça vinha afirmando que não existia.

---

## 2. O que ela estabelece — item por item

### 2.1 A cadeia inteira é definida por empresa — inclusive o "usuário"

> "usuário de preservativos de madeira - toda e qualquer empresa que faça uso de
> preservativos de madeira em qualquer das etapas de seu processo produtivo, bem como as
> empresas prestadoras de serviços" (p. 1)

> "comércio de preservativos de madeira - todo estabelecimento comercial que se dedique
> à compra e venda, no varejo ou atacado, de preservativos de madeira" (p. 1)

A definição de "usuário" do preservativo é **empresa**, e a de comércio é **estabelecimento
comercial**, inclusive de varejo. Não existe, em nenhuma alínea, uma categoria para a pessoa
física que compra o produto na loja de agropecuária e trata a peça no quintal. Ele não é
indústria, não é usina, não é importador, não é comércio e não é usuário — pela definição da
própria instrução.

### 2.2 O descarte do resíduo existe como obrigação — e mora na bula

O item VIII tem por título, literalmente, **"DA DESTINAÇÃO FINAL DE RESÍDUOS E
EMBALAGENS"**. É seção própria, não nota de rodapé:

> "o descarte da embalagem e resíduos de preservativos de madeira e ingredientes ativos
> deverá atender às recomendações técnicas apresentadas na bula, relativas aos processos de
> destinação final, observadas as exigências dos setores de saúde e meio ambiente" (p. 6)

E o item VI exige que a bula traga essa informação:

> "informações sobre o destino final das embalagens e dos resíduos" (p. 5)

**Este é o mecanismo, e é o achado central desta ficha.** A instrução **não fixa** qual é a
destinação final. Ela **cria a obrigação e delega o conteúdo à bula**, que o fabricante
redige e o Ibama aprova. A regra do descarte não está na norma: está no rótulo do produto
registrado.

### 2.3 As outras três alíneas do mesmo item

> "é proibida a reutilização de embalagens de preservativos de madeira para outras
> finalidades" (p. 6)

> "o IBAMA poderá autorizar o reaproveitamento de embalagens de preservativos de madeira
> pela empresa produtora" (p. 6)

> "os tambores metálicos vazios devem ser amassados, além de terem o seu fundo perfurado,
> de maneira a torná-los inadequados para qualquer outro acondicionamento de produtos" (p. 6)

O detalhamento é de embalagem: inutilizar tambor, não reutilizar frasco. Sobre o **líquido**
que sobra do banho, a instrução não tem alínea própria — ele entra, no máximo, como
"resíduos de preservativos de madeira e ingredientes ativos".

---

## 3. Por que isso muda a tese da peça

Até esta custódia, a peça afirmava, em várias passagens, que **ninguém diz o que fazer com a
sobra**. Isso era falso, e a ficha anterior não tinha como saber: a norma que diz estava
declarada pendente.

O que se pode afirmar agora, com documento:

1. **Existe obrigação de destinação final** de resíduos de preservativo — item VIII da IN
   5/92, vigente desde 1992;
2. **o conteúdo dessa obrigação é delegado à bula** — art. VIII "c" combinado com VI "h";
3. **quem é dispensado do registro não tem bula** — a Portaria 292/89, art. 4º, dispensa de
   registro o preservativo destinado a "experimentação e uso domissanitário", e a bula é
   exigência do produto registrado;
4. **a cadeia é definida por empresa** — inclusive o "usuário" (item I, "f"), o que deixa a
   pessoa física fora de todas as categorias da instrução.

Ou seja: o risco não é deixado em silêncio. Ele é **transferido duas vezes** — da norma para
o rótulo, e do rótulo para quem não tem rótulo.

---

## 4. O que esta ficha NÃO afirma

- **Não afirma que o banho caseiro de sulfato de cobre para bambu seja "domissanitário".**
  O termo é da família dos saneantes de uso domiciliar; decidir se abrange tratar material no
  quintal é interpretação, e não foi feita aqui.
- **Não afirma que o resíduo do banho esteja coberto pelo item VIII.** A alínea fala de
  "resíduos de preservativos de madeira e ingredientes ativos"; se o líquido exaurido entra
  nessa expressão é leitura, não literalidade.
- **Não afirma que a IN 5/92 esteja em vigor sem alteração.** Ela é de 1992 e não foi
  revogada por norma que eu tenha localizado; isso é limite da busca, não achado.
- **Não mediu** se as bulas dos produtos registrados hoje trazem, de fato, a instrução de
  destinação final que o item VI "h" exige. Ler as bulas dos sete produtos registrados é
  rodada própria.

---

## 5. Proveniência e limites da custódia

- **Via oficial bloqueada:** `ibama.gov.br/component/legislacao` responde **403** a
  requisição automatizada (verificado nesta rodada).
- **Fac-símile usado:** PDF de 15 páginas hospedado pela **ABPM** (associação setorial),
  com o texto do DOU de 21.10.1992. Bytes preservados, sha256 no cabeçalho e no
  `MANIFEST_S11D.json`.
- **Extração:** por página, com marcador `<!-- PAGE: n -->`, para que cada citação desta
  ficha seja conferível no extrato.
- **Conferência:** todas as citações desta ficha passaram pelo portão de fidelidade
  (busca literal no extrato). O número está no relatório da rodada.
"""


def main():
    e = MAN["in592_1992"]
    os.makedirs(DEST, exist_ok=True)
    cab = CABECALHO.format(arquivo=e["arquivo"], sha=e["sha256"], paginas=e["paginas"],
                           url=e["fonte_url"])
    texto = cab + CORPO + DECL_IA
    nome = "ficha-in05-92-ibama-destinacao-final-residuos.md"
    p = os.path.join(DEST, nome)
    open(p, "w", encoding="utf-8").write(texto)
    print(f"{nome}  {len(texto.splitlines())} linhas  "
          f"sha256 {hashlib.sha256(texto.encode()).hexdigest()[:12]}")
    print(f"DESTINO: {DEST}")


if __name__ == "__main__":
    main()
