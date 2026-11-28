#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consolida a gaveta HIS/ATHIS: nome de protocolo, custódia adotada e mapa de renomeação.

Três correções que este script existe para fazer:
  1. NOME. `<sobrenome>-<ano>-<tema>` derivado do front matter, nunca de "sem-autor" — e, em
     colisão real, o discriminante vem do título, não um número no fim.
  2. CUSTÓDIA PREEXISTENTE. As obras do release 1 já têm `original.pdf` em
     `_privado/fontes-academicas`; adotar o binário com o nome do protocolo, com sha256, é o
     estágio 3 feito — não "fonte ausente".
  3. MAPA. Toda troca de nome entra em `RENOMEACAO.json` com sha256 antes/depois, como manda o
     protocolo de renomeação em lote.
"""
from __future__ import annotations
import hashlib, json, re, shutil, unicodedata
from pathlib import Path

BASE = Path(__file__).parent
ACERVO_FONTES = Path("/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica/_privado/fontes-academicas")
PDF_DIR = BASE / "custodia" / "pdf"

TEMA = [("melhoria","melhoria-habitacional"),("belo monte","reassentamento-belo-monte"),
        ("altamira","reassentamento-belo-monte"),("assessoria","assessoria-tecnica"),
        ("assistência técnica","assistencia-tecnica"),("assistência tecnica","assistencia-tecnica"),
        ("athis","athis"),("regulariza","regularizacao-fundiaria"),("quilombola","quilombos"),
        ("kalunga","quilombos"),("rural","habitat-rural"),("autogest","autogestao"),
        ("inadequa","inadequacao-habitacional"),("formação","formacao-profissional"),
        ("residência","residencia-multiprofissional"),("sol nascente","sol-nascente"),
        ("distrito federal","distrito-federal"),("déficit","deficit-habitacional"),
        ("reassentamento","reassentamento"),("seguridade","seguridade-habitacional")]


def slug(s):
    s = unicodedata.normalize("NFD", str(s)).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def tema(titulo):
    t = (titulo or "").lower()
    for k, v in TEMA:
        if k in t:
            return v
    return "habitacao-interesse-social"


def sobrenome(autores):
    """`autores[0]` sem partícula: 'Sombrio, Catarina M.' → sombrio; 'Catarina M. Sombrio' → sombrio."""
    a = (autores or "").split(";")[0].strip()
    if not a:
        return ""
    if "," in a:
        s = a.split(",")[0].strip()
    else:
        partes = [p for p in a.split() if p.lower() not in ("de", "da", "do", "das", "dos", "e")]
        s = partes[-1] if partes else a
    return slug(s)


def main():
    resumos = json.loads((BASE / "obras_resumos.json").read_text(encoding="utf-8"))
    meta = json.loads((BASE / "acervo_r1_meta.json").read_text(encoding="utf-8"))
    cust = json.loads((BASE / "CUSTODIA_CONSOLIDADA.json").read_text(encoding="utf-8"))
    cust_por_arquivo = {c["arquivo_alvo"]: c for c in cust}

    fontes = {p.name: p for p in ACERVO_FONTES.iterdir() if p.is_dir() and (p / "original.pdf").exists()}

    itens, renomeacao, usados = [], [], {}
    for chave, v in resumos.items():
        arq_acervo = v.get("arq_acervo") or ""
        m = meta.get(arq_acervo, {}) if arq_acervo else {}
        autores = m.get("autores") or v.get("autor_principal") or "; ".join(v.get("autores") or [])
        titulo = (m.get("titulo") or v.get("titulo") or "").strip().strip('"')
        ano = str(m.get("ano") or v.get("ano") or "").strip()
        if not re.match(r"^(19|20)\d{2}$", ano):
            achado = re.search(r"\b(19|20)\d{2}\b", titulo)
            ano = achado.group(0) if achado else "s-d"
        sb = sobrenome(autores) or "sem-autor"
        base_nome = f"{sb}-{ano}-{tema(titulo)}"
        nome = base_nome
        if base_nome in usados:  # colisão real: discriminante vem do título
            extra = "-".join([w for w in slug(titulo).split("-") if w not in base_nome][:3])
            nome = f"{base_nome}-{extra}" if extra else f"{base_nome}-2"
            while nome in usados:
                nome += "-b"
        usados[nome] = True
        arquivo = nome + ".md"
        antigo = next((c for c in cust if c.get("titulo","").strip()[:40] == titulo[:40]), None)
        itens.append({"chave": chave, "arquivo_alvo": arquivo, "nome_antigo": (antigo or {}).get("arquivo_alvo", ""),
                      "titulo": titulo, "autores": autores, "ano": ano,
                      "tema": tema(titulo), "arq_acervo": arq_acervo,
                      "url": next((u for u in re.split(r"\s+", v.get("link_acesso") or "") if u.startswith("http")), ""),
                      "url_bdtd": v.get("url_bdtd", "")})

    # custódia adotada do acervo privado
    adotados = 0
    for it in itens:
        pasta = None
        if it["arq_acervo"]:
            # a pasta de fonte é `AAAA-<sobrenome>-...`, a ficha é `<sobrenome>-AAAA-...`;
            # comparar por (sobrenome, ano) evita o falso negativo da ordem invertida
            partes = slug(it["arq_acervo"].split("/")[-1]).split("-")
            ano_a = next((x for x in partes if re.match(r"^(19|20)\d{2}$", x)), "")
            sob_a = next((x for x in partes if not re.match(r"^(19|20)\d{2}$", x)), "")
            for nome_dir, p in fontes.items():
                if ano_a and sob_a and ano_a in nome_dir and sob_a in nome_dir:
                    pasta = p
                    break
        if not pasta:
            continue
        destino = PDF_DIR / (it["arquivo_alvo"].replace(".md", ".pdf"))
        if not destino.exists():
            shutil.copy2(pasta / "original.pdf", destino)
        dados = destino.read_bytes()
        it["custodia"] = {"estado": "CUSTODIADO", "rota": "acervo_privado_preexistente",
                          "origem": str((pasta / "original.pdf").relative_to(ACERVO_FONTES)),
                          "sha256": hashlib.sha256(dados).hexdigest(), "bytes": len(dados)}
        adotados += 1
        if it["nome_antigo"] and it["nome_antigo"] != it["arquivo_alvo"]:
            renomeacao.append({"nome_antigo": it["nome_antigo"], "nome_novo": it["arquivo_alvo"],
                               "motivo": "nome derivado de autores[0] do front matter; 'sem-autor' era defeito de leitura",
                               "sha256_binario": it["custodia"]["sha256"]})

    # custódia já baixada nas rodadas 1 e 2
    for it in itens:
        if it.get("custodia"):
            continue
        c = cust_por_arquivo.get(it["nome_antigo"]) or cust_por_arquivo.get(it["arquivo_alvo"])
        if c and c["estado"] == "CUSTODIADO":
            it["custodia"] = {"estado": "CUSTODIADO", "rota": c.get("rota"), "origem": c.get("origem_url"),
                              "sha256": c.get("sha256"), "bytes": c.get("bytes"), "paginas": c.get("paginas")}
        elif c:
            it["custodia"] = {"estado": "NAO_ALCANCADO", "motivo": c.get("motivo"),
                              "tentativas": [t.get("http") for t in c.get("tentativas", [])][-3:]}
        else:
            it["custodia"] = {"estado": "SEM_TENTATIVA"}

    # reconciliação: PDF baixado cujo nome não casou com o nome do protocolo não é órfão —
    # é a mesma obra; adota pelo par (sobrenome, ano) e registra o nome do arquivo.
    import subprocess as _sp
    def _paginas(path):
        r = _sp.run(["/Users/fabiotakwara/.venvs/pdf/bin/python", "-c",
                     "import fitz,sys;print(fitz.open(sys.argv[1]).page_count)", str(path)],
                    capture_output=True, text=True)
        return int(r.stdout.strip()) if r.returncode == 0 and r.stdout.strip().isdigit() else None

    for it in itens:
        if it["custodia"]["estado"] == "CUSTODIADO":
            continue
        alvo = it["arquivo_alvo"].replace(".md", ".pdf")
        partes = alvo.split("-")
        sb, ano = partes[0], partes[1]
        achado = PDF_DIR / alvo
        if not achado.exists():
            cand = [p for p in PDF_DIR.glob(f"{sb}-{ano}-*.pdf")]
            achado = cand[0] if cand else None
        if achado and achado.exists() and achado.read_bytes()[:5] == b"%PDF-":
            dados = achado.read_bytes()
            it["custodia"] = {"estado": "CUSTODIADO", "rota": "reconciliacao_por_par_sobrenome_ano",
                              "origem": achado.name, "sha256": hashlib.sha256(dados).hexdigest(),
                              "bytes": len(dados), "paginas": _paginas(achado)}

    (BASE / "INVENTARIO_GAVETA_V2.json").write_text(json.dumps(itens, ensure_ascii=False, indent=1), encoding="utf-8")
    (BASE / "RENOMEACAO.json").write_text(json.dumps(renomeacao, ensure_ascii=False, indent=1), encoding="utf-8")

    ok = [i for i in itens if i["custodia"]["estado"] == "CUSTODIADO"]
    print(f"itens={len(itens)} custodiados={len(ok)} adotados_do_acervo={adotados} renomeacoes={len(renomeacao)}")
    print(f"paginas_custodiadas={sum((i['custodia'].get('paginas') or 0) for i in ok)}")
    sem_nome = [i['arquivo_alvo'] for i in itens if 'sem-autor' in i['arquivo_alvo']]
    print(f"nomes 'sem-autor' restantes: {len(sem_nome)}")


if __name__ == "__main__":
    main()
