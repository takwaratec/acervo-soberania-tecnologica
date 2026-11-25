#!/usr/bin/env python3
"""Saneamento de custódia das fontes do cobre (C-02).

O que o repositório público precisa guardar de uma obra de terceiro é o que a peça
usa: metadados, os trechos citados e as tabelas que são nossas. O resto do extrato
é obra alheia inteira dentro de um repositório público — o PDF saiu do rastreio, o
conteúdo ficou, e a fronteira de custódia protege o conteúdo, não a extensão.

Regra, mecânica e reproduzível:
  - arquivo pequeno (< LIMITE bytes) fica como está: metadado ou extrato curto;
  - arquivo grande é reduzido aos parágrafos que contêm algum trecho efetivamente
    citado nas fichas e nos documentos da gaveta; o resto sai da árvore;
  - o que sai continua no histórico do git e nos PDFs em custódia privada.

Uso:
  python3 scripts/sanear_fontes_cobre.py            # mede, não escreve
  python3 scripts/sanear_fontes_cobre.py --aplicar  # reescreve os extratos
"""
import glob
import json
import os
import re
import sys

REPO = os.environ.get("COBRE_REPO", ".")
BASE = os.path.join(REPO, "docs/analyses/cobre")
MD = os.path.join(BASE, "fontes/md")
LIMITE = 20_000
MIN_CITACAO = 40
RELATORIO = os.path.join(BASE, "fontes/SANEAMENTO_CUSTODIA_FONTES.json")


def normaliza(t: str) -> str:
    t = t.replace("**", "").replace("*", "").replace("`", "")
    return re.sub(r"\s+", " ", t).strip().lower()


# só valor com unidade analítica: "%"/inteiro solto aparece em toda página e não seleciona nada
UNIDADE = re.compile(r"\d+[,.]\d+\s*(?:mg/L|mg/kg|mg/dm3|µg/L|ug/L|µg/kg|mg/m3|g/L|g/kg|mm|°C|m³)")
MAX_POR_FONTE = 40_000


def valores_da_gaveta():
    """Números com unidade que a gaveta usa — o que a peça afirma e precisa poder conferir."""
    vals = set()
    fontes = (glob.glob(os.path.join(BASE, "*.md"))
              + glob.glob(os.path.join(BASE, "fichas/*.md")))
    for caminho in fontes:
        texto = open(caminho, encoding="utf-8", errors="ignore").read()
        for m in UNIDADE.finditer(texto):
            vals.add(re.sub(r"\s+", " ", m.group(0)).strip().lower())
    return vals


def citacoes_da_gaveta():
    """Todo trecho entre aspas de bloco (> ...) ou entre "..." nos documentos do cobre."""
    trechos = []
    fontes = (glob.glob(os.path.join(BASE, "*.md"))
              + glob.glob(os.path.join(BASE, "fichas/*.md")))
    for caminho in fontes:
        texto = open(caminho, encoding="utf-8", errors="ignore").read()
        for linha in texto.splitlines():
            if linha.startswith(">"):
                t = linha.lstrip("> ").strip()
                if len(t) >= MIN_CITACAO:
                    trechos.append((os.path.basename(caminho), t))
        for m in re.finditer(r'"([^"\n]{%d,})"' % MIN_CITACAO, texto):
            trechos.append((os.path.basename(caminho), m.group(1)))
    vistos, saida = set(), []
    for origem, t in trechos:
        n = normaliza(t)
        if n not in vistos:
            vistos.add(n)
            saida.append((origem, t))
    return saida


def shingles(texto: str) -> set:
    palavras = re.findall(r"[a-zà-ú0-9,./%-]+", texto.lower())
    return {" ".join(palavras[i:i + 6]) for i in range(max(0, len(palavras) - 5))}


def paragrafos(texto: str):
    """Blocos separados por linha em branco, preservando a ordem."""
    return [p for p in re.split(r"\n\s*\n", texto)]


def main():
    aplicar = "--aplicar" in sys.argv
    citacoes = citacoes_da_gaveta()
    norm_cit = [normaliza(c[1]) for c in citacoes]
    vals = valores_da_gaveta()
    print(f"valores com unidade usados pela gaveta: {len(vals)}")
    print(f"citações colhidas nas fichas e documentos: {len(citacoes)}")

    linhas = []
    total_antes = total_depois = 0
    for caminho in sorted(glob.glob(os.path.join(MD, "*"))):
        nome = os.path.basename(caminho)
        if nome.endswith(".json"):
            continue
        bruto = open(caminho, encoding="utf-8", errors="ignore").read()
        antes = len(bruto.encode("utf-8"))
        total_antes += antes
        if antes < LIMITE:
            total_depois += antes
            linhas.append({"arquivo": nome, "bytes_antes": antes, "bytes_depois": antes,
                           "paragrafos_antes": len(paragrafos(bruto)),
                           "paragrafos_mantidos": len(paragrafos(bruto)),
                           "acao": "mantido (abaixo de 20 KB: metadado ou extrato curto)"})
            continue

        ps = paragrafos(bruto)
        mantidos, usados = [], set()
        for p in ps:
            np_ = normaliza(p)
            bateu = False
            for i, c in enumerate(norm_cit):
                if c in np_:
                    bateu = True
                    usados.add(i)
                    continue
                # a citação da ficha vem reflowada e com elipses: casa por shingle de 6 palavras
                if shingles(c) & shingles(np_):
                    bateu = True
                    usados.add(i)
            if not bateu:
                # parágrafo que carrega número com unidade usada pela peça: fica, é o que se confere
                for m in UNIDADE.finditer(p):
                    if re.sub(r"\s+", " ", m.group(0)).strip().lower() in vals:
                        bateu = True
                        break
            if bateu:
                if sum(len(x.encode()) for x in mantidos) + len(p.encode()) > MAX_POR_FONTE:
                    continue
                mantidos.append(p)

        if not mantidos:
            # nenhuma citação direta: guarda só o cabeçalho (título, fonte, URL, hash)
            mantidos = ps[:1]

        # front matter do extrato original NUNCA sai: é o metadado da fonte
        fm = ""
        if bruto.startswith("---"):
            fim_fm = bruto.find("\n---", 3)
            if fim_fm != -1:
                fm = bruto[:bruto.find("\n", fim_fm + 1) + 1].rstrip() + "\n"
                mantidos = [p for p in mantidos if not p.startswith("---")]
                if not mantidos:
                    mantidos = [ps[1]] if len(ps) > 1 else ps[:1]
                txt_fm = fm
                fm = txt_fm
        cabecalho = ("<!-- extrato curado: este arquivo guarda apenas o que a peça cita e o que é "
                     "nosso. O texto integral está no PDF em custódia privada (ver "
                     "fontes/CUSTODIA_PRIVADA_PDFS.json) e no histórico do git. "
                     "Saneamento C-02, 2026-11-25. -->\n\n")
        novo = fm + cabecalho + "\n\n".join(mantidos).rstrip() + "\n"
        depois = len(novo.encode("utf-8"))
        total_depois += depois
        linhas.append({"arquivo": nome, "bytes_antes": antes, "bytes_depois": depois,
                       "paragrafos_antes": len(ps), "paragrafos_mantidos": len(mantidos),
                       "citacoes_atendidas": len(usados),
                       "acao": "reduzido aos parágrafos citados"})
        if aplicar:
            open(caminho, "w", encoding="utf-8").write(novo)

    rel = {
        "schema": "SANEAMENTO_CUSTODIA_FONTES_R1",
        "mede": ("quanto de obra de terceiro o repositório público guarda em fontes/md/. "
                 "Não mede se o trecho mantido é suficiente para a tese — isso é leitura humana."),
        "regra": ("arquivo < 20 KB fica inteiro; acima disso sobram só os parágrafos que contêm "
                  "trecho citado nas fichas ou nos documentos, mais o primeiro bloco (cabeçalho). "
                  "O restante permanece no histórico do git e nos PDFs de custódia privada."),
        "denominador_fixado": len([l for l in linhas]),
        "limite_bytes": LIMITE,
        "total_bytes_antes": total_antes,
        "total_bytes_depois": total_depois,
        "reducao_bytes": total_antes - total_depois,
        "arquivos": linhas,
        "aplicado": bool(aplicar),
    }
    print(f"arquivos medidos: {len(linhas)}  antes {total_antes:,} B  depois {total_depois:,} B  "
          f"redução {total_antes - total_depois:,} B")
    if aplicar:
        open(RELATORIO, "w", encoding="utf-8").write(json.dumps(rel, ensure_ascii=False, indent=1) + "\n")
        print(f"relatório: {RELATORIO}")
    else:
        for l in linhas:
            if l["bytes_antes"] != l["bytes_depois"]:
                print(f"  {l['arquivo']}: {l['bytes_antes']:,} → {l['bytes_depois']:,} B "
                      f"({l['paragrafos_mantidos']}/{l['paragrafos_antes']} parágrafos)")


if __name__ == "__main__":
    main()
