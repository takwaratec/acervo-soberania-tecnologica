#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Custódia S11-c — a norma da madeira tratada e o descarte.

Cinco documentos custodiados, dois declarados como pendência com motivo.
Extração com marcador de página (é o que torna a citação conferível depois),
manifesto com URL de origem por entrada.
"""
import hashlib
import json
import os
import shutil
import unicodedata

import fitz

SCRATCH = "/Users/fabiotakwara/.hermes/cache/scratch/s11c"
RAIZ = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica"
DEST = f"{RAIZ}/_privado/fontes-documentais/ago_28_Madeira_Tratada_S11c"

# chave: (arquivo de origem, nome canônico, url, título, tipo, observação)
DOCS = {
    "pi292_1989": (
        "pi292_pdf.pdf",
        "1989_pi292_preservativos_registro.pdf",
        "https://www.gov.br/ibama/pt-br/assuntos/quimicos-e-biologicos/preservativos-de-madeiras/arquivos/2017-registados/areas%20tematicas_produtos%20preservativo%20de%20madeiras_2.pdf",
        "Portaria Interministerial nº 292, de 28 de abril de 1989",
        "norma",
        "Norma-mãe do setor: registro obrigatório no Ibama e competência de fiscalização (art. 20).",
    ),
    "pn151_1997": (
        "dou/pn151_p72.pdf",
        "1997_pn151_ibama_registro_risco_ambiental.pdf",
        "http://pesquisa.in.gov.br/imprensa/servlet/INPDFViewer?jornal=1&pagina=72&data=25/11/1997&captchafield=firstAccess",
        "Portaria Normativa Ibama nº 151, de 24 de novembro de 1997",
        "norma",
        "DOU Seção 1, p. 27.552, 25/11/1997. OCR da Imprensa Nacional degradado: os artigos 1º a 4º são legíveis, o número no cabeçalho não.",
    ),
    "iema2023": (
        "iema.pdf",
        "2023_iema_es_nt01_preservacao_madeira.pdf",
        "https://iema.es.gov.br/Media/iema/LICENCIAMENTO/NTO_01-2023_Preserva%C3%A7ao_de_Madeira_14122023.pdf",
        "Nota Técnica Orientativa GGE-COED nº 01/2023 — licenciamento da preservação de madeira (Iema-ES)",
        "norma-orientativa",
        "Regulador estadual descrevendo o processo, os resíduos e o que falta de informação sobre o CCB.",
    ),
    "fg4mad2016": (
        "fg4mad.pdf",
        "2016_abpm_fg4mad_destinacao_residuos_madeira_tratada.pdf",
        "https://fg4mad.com.br/wp-content/uploads/2016/10/DestinacaoResiduosMadeiraTratada.pdf",
        "Destinação de Resíduos de Madeira Tratada (ABPM / FG4mad)",
        "material-setorial",
        "Apresentação da associação setorial. Hospedagem com certificado expirado: baixado com verificação TLS desativada; bytes preservados.",
    ),
    "ufsm2025": (
        "ufsm.pdf",
        "2025_ufsm_ciencia_florestal_cca_moiroes_solo.pdf",
        "https://periodicos.ufsm.br/cienciaflorestal/article/download/86024/66278",
        "Contaminação do solo pelo uso de moirões tratados com arseniato de cobre cromatado — Ciência Florestal v.35 e86024 (2025)",
        "artigo",
        "Ensaio de campo de 880 dias: cinco moirões, duas profundidades, seis amostragens.",
    ),
}

PENDENTES = [
    {
        "chave": "in_ibama_05_1992",
        "titulo": "Instrução Normativa Ibama nº 05, de 20 de outubro de 1992",
        "fonte_url": "http://pesquisa.in.gov.br/imprensa/jsp/visualiza/index.jsp?jornal=1&pagina=60&data=21/10/1992",
        "estado": "PENDENTE",
        "motivo": "A página do DOU indicada nos índices do Ibama não contém a Instrução: as páginas 57 a 62 do DOU de 21/10/1992 foram baixadas e conferidas, e trazem outros atos. A Instrução não foi localizada no intervalo varrido.",
        "destrava": "Localizar a página correta do DOU de 21/10/1992, ou obter cópia no processo administrativo do registro (o certificado do Tanalith cita a IN 5/92 como base legal).",
    },
    {
        "chave": "unipar2022",
        "titulo": "Madeira preservada com CCA: proficuidade, potencial deletério, toxicidade dos resíduos e tecnologias de recuperação — Revista em Agronegócio e Meio Ambiente (2022)",
        "fonte_url": "https://doi.org/10.17765/2176-9168.2022v15n1e8871",
        "estado": "PENDENTE",
        "motivo": "O periódico responde 403 a requisição automatizada e, no navegador, devolve a página 'Site em manutenção' da Vitru Educação. Não é bloqueio antibot: o serviço está indisponível.",
        "destrava": "Nova tentativa quando o periódico voltar, ou cópia via biblioteca/Periódicos Capes.",
    },
]


def nfc(s):
    return unicodedata.normalize("NFC", s)


def extrair(pdf, md):
    d = fitz.open(pdf)
    partes = []
    for i, p in enumerate(d, 1):
        partes.append(f"<!-- PAGE: {i} -->\n{p.get_text()}")
    d.close()
    texto = nfc("\n".join(partes))
    open(md, "w", encoding="utf-8").write(texto)
    return texto, texto.count("<!-- PAGE:")


def main():
    os.makedirs(DEST, exist_ok=True)
    man = {
        "lote": "S11-c — a norma da madeira tratada e o descarte",
        "frente": "COBRE",
        "data": "2026-11-24",
        "regra": "bytes preservados; extração com marcador de página; URL de origem por entrada",
        "entradas": [],
        "pendentes": PENDENTES,
    }
    for chave, (origem, canonico, url, titulo, tipo, obs) in DOCS.items():
        src = os.path.join(SCRATCH, origem)
        dst = os.path.join(DEST, canonico)
        shutil.copy2(src, dst)
        md = dst.replace(".pdf", ".md")
        texto, pags = extrair(dst, md)
        man["entradas"].append({
            "chave": chave,
            "titulo": titulo,
            "tipo": tipo,
            "arquivo": canonico,
            "pdf_bytes": os.path.getsize(dst),
            "pdf_sha256": hashlib.sha256(open(dst, "rb").read()).hexdigest(),
            "paginas": pags,
            "texto_chars": len(texto),
            "md_sha256": hashlib.sha256(open(md, "rb").read()).hexdigest(),
            "fonte_url": url,
            "observacao": obs,
        })
        print(f"  {chave:14s} {pags:>3}p {len(texto):>7} chars  {canonico}")
    json.dump(man, open(f"{DEST}/MANIFEST_S11C.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(f"\nCUSTODIADOS: {len(man['entradas'])}  PENDENTES: {len(PENDENTES)}")
    print(f"DESTINO: {DEST}")


if __name__ == "__main__":
    main()
