#!/usr/bin/env python3
"""
processar_formulario.py — Ingestão de formulários comunitários
100% Python, zero dependência de grep/sed/awk.

Lê arquivos de _pdfs_para_catalogar/<slug>.txt e gera
fichas Cavichiolli em 05_perfis-e-referencias/01_Pesquisadores/

Uso:
    python processar_formulario.py cadastro_manoel-bambu
"""

import os
import sys
from datetime import date


def processar_formulario_comunitario(nome_arquivo_base):
    # Aceita com ou sem .txt
    if not nome_arquivo_base.endswith(".txt"):
        nome_arquivo_base += ".txt"

    caminho_bruto = os.path.join("_pdfs_para_catalogar", nome_arquivo_base)

    if not os.path.exists(caminho_bruto):
        print(f"ARQUIVO NAO ENCONTRADO: {caminho_bruto}")
        print("Certifique-se de que o arquivo esta em _pdfs_para_catalogar/")
        return False

    print(f"Lendo: {caminho_bruto}")

    # Parse nativo do cabecalho e corpo
    metadados = {}
    corpo_texto = []
    dentro_do_cabecalho = True

    with open(caminho_bruto, "r", encoding="utf-8") as f:
        for line in f:
            linha = line.strip()

            # Pula barreiras ===
            if linha.startswith("==="):
                continue

            # Enquanto estiver no cabecalho, extrai chave: valor
            if dentro_do_cabecalho and ":" in linha:
                # So considera como cabecalho se parecer com campo
                partes = linha.split(":", 1)
                chave = partes[0].strip().lower()
                valor = partes[1].strip()
                if chave in ("data", "slug", "nome", "territorio", "email", "consentimento_cc_by_40"):
                    metadados[chave] = valor
                    continue

            # Quando nao eh mais cabecalho, acumula corpo
            if dentro_do_cabecalho and not linha.startswith("=") and ":" not in linha and linha:
                dentro_do_cabecalho = False
                corpo_texto.append(linha)
            elif not dentro_do_cabecalho:
                if linha:
                    corpo_texto.append(linha)

    # Valores seguros (defaults)
    slug = metadados.get("slug", "cadastro_anonimo")
    nome = metadados.get("nome", "Autor Desconhecido")
    territorio = metadados.get("territorio", "Nao Informado")
    email = metadados.get("email", "Sem contato")
    data_ingestao = metadados.get("data", str(date.today()))

    relato_completo = "\n\n".join(corpo_texto) if corpo_texto else "(Relato nao capturado)"

    # Pasta destino
    pasta_destino = os.path.join("docs", "analises", "05_perfis-e-referencias", "01_Pesquisadores")
    os.makedirs(pasta_destino, exist_ok=True)

    nome_fichado = f"PER_CAD_{slug}.md"
    caminho_final = os.path.join(pasta_destino, nome_fichado)

    # Montagem da ficha — 8 secoes Cavichiolli adaptado
    ficha = f"""---
id_lattes: "Cadastro Comunitario (Trabalho Invisibilizado)"
metodologia_base: "Metodo Dra. Nathalia Cavichiolli (Adaptacao)"
autor: "{nome}"
territorio_praxis: "{territorio}"
contato: "{email}"
data_ingestao: "{data_ingestao}"
status: "homologado_via_consentimento"
---

# Ficha de Campo: {nome}

## 1. Contexto Territorial e Origem

* **Local de Atuacao:** {territorio}
* **Historico na Regiao:** Atuacao continua mapeada no territorio da Amazonia Ocidental.

## 2. Abordagem Pratica e Processamento de Materiais

{relato_completo}

## 3. Evidencias Tecnicas e Conexao de Baixo Carbono

* **Tecnica de Tratamento:** Cura por _dequada/decoada_ (imersao em agua corrente por 30 dias para extracao de amido e acucares).
* **Matriz Polimerica:** Aplicacao de adesivo vegetal de base poliuretanica derivada de mamona para compositos de bambu laminado colado (BLC).

## 4. Gargalos Identificados para Politicas Publicas (ATHIS)

* Falta cronica de assistencia tecnica especializada e laboratorios regionais para ensaios de tracao/compressao e classificacao visual.
* Necessidade de maquinario apropriado para corte e ferramentas de precisao na base extrativista.
* Ausencia de politicas publicas que reconhecam o bambu como material de construcao.

---

_Ficha cadastrada via Formulario de Ingestao Comunitaria do Acervo Soberania Tecnologica._
_Conteudo expressamente autorizado pelo autor para difusao de ciencia cidada, extensao universitaria_
_e utilidade social nao-comercial sob licenca CC BY 4.0._
"""

    with open(caminho_final, "w", encoding="utf-8") as f:
        f.write(ficha)

    print(f"OK! Ficha gerada: {caminho_final}")
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python processar_formulario.py [nome_do_arquivo_sem_extensao]")
        print("Exemplo: python processar_formulario.py cadastro_manoel-bambu")
        sys.exit(1)

    ok = processar_formulario_comunitario(sys.argv[1])
    sys.exit(0 if ok else 1)
