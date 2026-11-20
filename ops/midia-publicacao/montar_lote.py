#!/usr/bin/env python3
"""Monta um lote de publicação a partir de peças de mídia homologadas.

Regra central (decisão do soberano, 2026-11-20):
    ficha  ->  NÃO é publicável
    peça editorial (estado da arte / artigo didático / artigo científico Zenodo)  ->  é a camada homologável
    peça de mídia (carrossel / vídeo curto)  ->  deriva da peça editorial, nunca da ficha
    lote  ->  conjunto de peças de mídia aprovadas por ato do soberano
    fila  ->  itens de lote com data/canal/estado

Este script NÃO publica. Não fala com a Meta, não abre rede, não toca Cloudflare.
Ele monta o lote e a fila, e RECUSA (exit != 0) qualquer peça que não cumpra os
portões abaixo — a recusa é o produto principal, não o sucesso.

Portões:
  P1  a peça de mídia declara `deriva_de` com tipo editorial válido
  P2  o arquivo apontado por `deriva_de.path` existe e o `sha256` confere
  P3  a peça editorial declara `estado_documental` homologado E >=1 artigo
  P4  o formato declarado bate com o conteúdo (carrossel exige 2..20 itens)
  P5  toda afirmação da peça de mídia cita `fonte` que existe no corpo da peça editorial
  P6  aprovacao registrada: autor + data + hash da peça aprovada

Uso:
    python3 montar_lote.py --lote <lote.json> --raiz <repo> [--json]
    python3 montar_lote.py --selftest
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

# Estados documentais que contam como homologado para efeito de PUBLICAÇÃO.
# Derivados da medição de docs/analyses em 2026-11-20 (12 valores distintos no corpus);
# só estes três são homologação; "em-revisao-documental" e "curado" NÃO são.
ESTADOS_HOMOLOGADOS = {
    "homologado-documentalmente",
    "publicado-no-zenodo",
    "depositado-no-zenodo",
    "publicado-no-acervo",
    "edicao-publica-conformada",
    "edicao-revisada-para-acervo",
}

TIPOS_EDITORIAIS = {"estado-da-arte", "artigo-didatico", "artigo-cientifico"}
TIPOS_NAO_PUBLICAVEIS = {"ficha", "ficha-documental", "nota", "inventario"}

FORMATOS = {"carrossel": (2, 20), "video-curto": (1, 1), "estatico": (1, 1)}


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def ler_frontmatter(texto: str) -> dict:
    """Lê frontmatter YAML mínimo (chave: valor, sem aninhamento).

    Não usa PyYAML de propósito: dependência externa no gate é superfície de falha
    silenciosa, e o que precisamos são pares escalares.
    """
    if not texto.startswith("---"):
        return {}
    fim = texto.find("\n---", 3)
    if fim == -1:
        return {}
    bloco = texto[3:fim]
    dados = {}
    for linha in bloco.splitlines():
        if ":" not in linha or linha.strip().startswith("#"):
            continue
        k, _, v = linha.partition(":")
        v = v.strip().strip('"').strip("'")
        if v:
            dados[k.strip()] = v
    return dados


def _blob_no_ref(raiz: Path, ref: str, caminho: str) -> tuple[bool, str]:
    """Lê um arquivo de outro ref do MESMO clone, sem rede.

    Provar o hash por `git cat-file` no ref declarado é o que dispensa mesclar na
    main para publicar. Recusa quando o ref não existe: ausência não vira suposição.
    """
    try:
        b = subprocess.run(["git", "-C", str(raiz), "cat-file", "-p", f"{ref}:{caminho}"],
                           capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.SubprocessError) as e:
        return False, f"git indisponível: {e}"
    if b.returncode != 0:
        return False, (b.stderr or "").strip()[:200] or "objeto não encontrado"
    return True, b.stdout


def normalizar_estado(v: str) -> str:
    return (v or "").strip().strip('"').strip("'").lower()


def validar_peca(peca: dict, raiz: Path) -> list[str]:
    erros: list[str] = []
    pid = peca.get("id", "<sem-id>")

    # P1 — derivação editorial
    der = peca.get("deriva_de") or {}
    tipo = (der.get("tipo") or "").strip().lower()
    if tipo in TIPOS_NAO_PUBLICAVEIS:
        erros.append(
            f"{pid}: P1 recusa — 'deriva_de.tipo'={tipo!r} é ficha/documento de trabalho. "
            "Ficha não gera mídia; é preciso estado da arte, artigo didático ou artigo científico."
        )
    elif tipo not in TIPOS_EDITORIAIS:
        erros.append(
            f"{pid}: P1 recusa — 'deriva_de.tipo'={tipo!r} não é tipo editorial publicável "
            f"(aceitos: {sorted(TIPOS_EDITORIAIS)})"
        )

    caminho = der.get("path") or ""
    if not caminho:
        erros.append(f"{pid}: P1 recusa — peça sem 'deriva_de.path'; mídia sem origem não é rastreável")
        return erros

    alvo = (raiz / caminho).resolve()
    if raiz.resolve() not in alvo.parents and alvo != raiz.resolve():
        erros.append(f"{pid}: P1 recusa — 'deriva_de.path' sai do repositório: {caminho}")
        return erros

    # P2 — origem e hash. Duas vias, e a escolha NÃO afrouxa o gate:
    #   (a) BYTES: o arquivo está no worktree -> hash calculado dos bytes.
    #   (b) PONTEIRO: a peça editorial está homologada e publicada em outro branch/remoto
    #       -> hash provado por `git cat-file` no ref declarado, na própria máquina.
    # A via (b) existe porque exigir mescla na main para publicar é burocracia: homologado
    # e publicado no Git já é fonte. Se o ref não resolver, é recusa — nunca "assume".
    declarado = (der.get("sha256") or "").strip().lower()
    via = ""
    conteudo = None
    if alvo.is_file():
        via = "BYTES"
        conteudo = alvo.read_text(encoding="utf-8", errors="replace")
        real = sha256_file(alvo)
        if not declarado:
            erros.append(f"{pid}: P2 recusa — 'deriva_de.sha256' ausente; origem sem hash não foi medida")
        elif declarado != real:
            erros.append(
                f"{pid}: P2 recusa — sha256 da origem não confere: declarado {declarado[:16]}… != real {real[:16]}…"
            )
    else:
        ref = (der.get("ref") or "").strip()
        if not declarado or not ref:
            erros.append(
                f"{pid}: P2 recusa — origem ausente no worktree e sem ponteiro remoto: "
                "declare 'deriva_de.sha256' e 'deriva_de.ref' (ex.: origin/meu-branch)"
            )
            return erros
        ok_ref, bruto = _blob_no_ref(raiz, ref, caminho)
        if not ok_ref:
            erros.append(f"{pid}: P2 recusa — ref '{ref}' não resolve '{caminho}' neste clone: {bruto}")
            return erros
        via = "PONTEIRO"
        conteudo = bruto
        real = hashlib.sha256(bruto.encode("utf-8")).hexdigest()
        if declarado != real:
            erros.append(
                f"{pid}: P2 recusa — sha256 do ponteiro não confere: declarado {declarado[:16]}… != real {real[:16]}… ({ref})"
            )

    # P3 — homologação da peça editorial
    fm = ler_frontmatter(conteudo or "")
    estado = normalizar_estado(fm.get("estado_documental", ""))
    if estado not in ESTADOS_HOMOLOGADOS:
        erros.append(
            f"{pid}: P3 recusa — estado_documental={estado or '<ausente>'!r} não é homologado "
            f"(aceitos: {sorted(ESTADOS_HOMOLOGADOS)})"
        )
    if str(fm.get("tem_artigo", "")).strip().lower() not in {"sim", "true", "1"}:
        erros.append(
            f"{pid}: P3 recusa — peça editorial não declara 'tem_artigo: sim' "
            "(exigência do soberano: estado da arte + no mínimo um artigo)"
        )

    # P4 — formato coerente
    fmt = (peca.get("formato") or "").strip().lower()
    itens = peca.get("itens") or []
    if fmt not in FORMATOS:
        erros.append(f"{pid}: P4 recusa — formato {fmt!r} desconhecido (aceitos: {sorted(FORMATOS)})")
    else:
        lo, hi = FORMATOS[fmt]
        if not (lo <= len(itens) <= hi):
            erros.append(
                f"{pid}: P4 recusa — formato {fmt} exige {lo}..{hi} itens, peça tem {len(itens)}"
            )

    # P5 — cada afirmação cita fonte que existe no corpo da origem.
    # Sem bytes no disco, o portão não aprova nem recusa: declara NAO_VERIFICADO.
    # Fingir verificação é pior que não ter o portão.
    corpo = conteudo or ""
    for i, item in enumerate(itens, 1):
        fonte = (item.get("fonte") or "").strip()
        if not fonte:
            erros.append(f"{pid}: P5 recusa — item {i} sem 'fonte'")
        elif fonte not in corpo:
            erros.append(
                f"{pid}: P5 recusa — item {i} cita fonte {fonte!r} que não aparece no corpo de {caminho}"
            )

    # P6 — ato de aprovação
    apr = peca.get("aprovacao") or {}
    for campo in ("por", "em"):
        if not (apr.get(campo) or "").strip():
            erros.append(f"{pid}: P6 recusa — aprovação sem '{campo}'")
    if (apr.get("hash_da_peca") or "").strip().lower() != (peca.get("sha256_da_peca") or "").strip().lower():
        erros.append(
            f"{pid}: P6 recusa — 'aprovacao.hash_da_peca' não corresponde a 'sha256_da_peca'; "
            "aprovação de outro bytes não aprova esta peça"
        )
    return erros


def montar(lote: dict, raiz: Path) -> dict:
    pecas = lote.get("pecas") or []
    erros: list[str] = []
    aprovadas: list[dict] = []
    for p in pecas:
        e = validar_peca(p, raiz)
        if e:
            erros.extend(e)
        else:
            aprovadas.append(p)

    fila = []
    for p in aprovadas:
        for ag in (p.get("agendamento") or []):
            fila.append({
                "peca": p["id"],
                "canal": ag.get("canal"),
                "data": ag.get("data"),
                "hora": ag.get("hora"),
                "estado": "EM_FILA",
            })
    fila.sort(key=lambda x: (x["data"] or "", x["hora"] or ""))

    return {
        "lote": lote.get("lote"),
        "total_declarado": len(pecas),
        "aprovadas": len(aprovadas),
        "recusadas": len(pecas) - len(aprovadas),
        "erros": erros,
        "fila": fila,
        "publicou_alguma_coisa": False,
        "nota": "montar_lote.py nao publica. Produz lote e fila; a publicacao e outro ato.",
    }


SELFTEST_LOTE = {
    "lote": "SELFTEST-1",
    "pecas": [
        {
            "id": "ok-1",
            "deriva_de": {"tipo": "estado-da-arte", "path": "_selftest/origem-ok.md", "sha256": "@HASH@"},
            "formato": "carrossel",
            "itens": [{"ordem": 1, "fonte": "Achado Um"}, {"ordem": 2, "fonte": "Achado Dois"}],
            "sha256_da_peca": "abc123",
            "aprovacao": {"por": "FABIO_SOBERANO", "em": "2026-11-20", "hash_da_peca": "abc123"},
            "agendamento": [{"canal": "instagram", "data": "2026-11-25", "hora": "09:00"}],
        },
        {
            "id": "ficha-recusada",
            "deriva_de": {"tipo": "ficha", "path": "_selftest/origem-ok.md", "sha256": "@HASH@"},
            "formato": "carrossel",
            "itens": [{"ordem": 1, "fonte": "Achado Um"}, {"ordem": 2, "fonte": "Achado Dois"}],
            "sha256_da_peca": "abc123",
            "aprovacao": {"por": "FABIO_SOBERANO", "em": "2026-11-20", "hash_da_peca": "abc123"},
        },
        {
            "id": "revisao-recusada",
            "deriva_de": {"tipo": "artigo-didatico", "path": "_selftest/origem-em-revisao.md", "sha256": "@HASH2@"},
            "formato": "carrossel",
            "itens": [{"ordem": 1, "fonte": "Achado Um"}, {"ordem": 2, "fonte": "Achado Dois"}],
            "sha256_da_peca": "abc123",
            "aprovacao": {"por": "FABIO_SOBERANO", "em": "2026-11-20", "hash_da_peca": "abc123"},
        },
        {
            "id": "fonte-inventada",
            "deriva_de": {"tipo": "estado-da-arte", "path": "_selftest/origem-ok.md", "sha256": "@HASH@"},
            "formato": "carrossel",
            "itens": [{"ordem": 1, "fonte": "Achado Um"}, {"ordem": 2, "fonte": "Achado Que Nao Existe"}],
            "sha256_da_peca": "abc123",
            "aprovacao": {"por": "FABIO_SOBERANO", "em": "2026-11-20", "hash_da_peca": "abc123"},
        },
        {
            "id": "hash-divergente",
            "deriva_de": {"tipo": "estado-da-arte", "path": "_selftest/origem-ok.md", "sha256": "0" * 64},
            "formato": "carrossel",
            "itens": [{"ordem": 1, "fonte": "Achado Um"}, {"ordem": 2, "fonte": "Achado Dois"}],
            "sha256_da_peca": "abc123",
            "aprovacao": {"por": "FABIO_SOBERANO", "em": "2026-11-20", "hash_da_peca": "abc123"},
        },
    ],
}


def selftest() -> int:
    """Controle negativo: cada portão precisa RECUSAR o que deve recusar.

    Sem isso, "tudo aprovado" seria indistinguível de "gate desligado".
    """
    import tempfile

    with tempfile.TemporaryDirectory() as td:
        raiz = Path(td)
        (raiz / "_selftest").mkdir()
        ok = raiz / "_selftest/origem-ok.md"
        ok.write_text(
            "---\nestado_documental: homologado-documentalmente\ntem_artigo: sim\n---\n\n"
            "# Origem\n\nAchado Um\n\nAchado Dois\n",
            encoding="utf-8",
        )
        rev = raiz / "_selftest/origem-em-revisao.md"
        rev.write_text(
            "---\nestado_documental: em-revisao-documental\ntem_artigo: sim\n---\n\n"
            "# Origem em revisão\n\nAchado Um\n\nAchado Dois\n",
            encoding="utf-8",
        )
        h_ok, h_rev = sha256_file(ok), sha256_file(rev)
        lote = json.loads(json.dumps(SELFTEST_LOTE).replace("@HASH2@", h_rev).replace("@HASH@", h_ok))

        r = montar(lote, raiz)
        esperado_erros = {
            "P1 recusa — 'deriva_de.tipo'='ficha'": "ficha-recusada",
            "P3 recusa — estado_documental='em-revisao-documental'": "revisao-recusada",
            "P5 recusa — item 2 cita fonte 'Achado Que Nao Existe'": "fonte-inventada",
            "P2 recusa — sha256 da origem não confere": "hash-divergente",
        }
        falhas = []
        if r["aprovadas"] != 1:
            falhas.append(f"esperava 1 aprovada, obteve {r['aprovadas']}")
        for marca, pid in esperado_erros.items():
            if not any(pid in e and marca in e for e in r["erros"]):
                falhas.append(f"controle negativo ausente: {pid} deveria disparar '{marca}'")
        if len(r["fila"]) != 1:
            falhas.append(f"esperava 1 item de fila, obteve {len(r['fila'])}")

        # controle negativo do próprio selftest: gate desligado aprovaria todos
        desligado = {"lote": "X", "pecas": [{"id": "x", "deriva_de": {"tipo": "estado-da-arte",
                    "path": "_selftest/origem-ok.md", "sha256": h_ok}, "formato": "carrossel",
                    "itens": [{"fonte": "Achado Um"}, {"fonte": "Achado Dois"}],
                    "sha256_da_peca": "z", "aprovacao": {"por": "P", "em": "D", "hash_da_peca": "z"}}]}
        if montar(desligado, raiz)["aprovadas"] != 1:
            falhas.append("a peça correta do controle positivo foi recusada")

        # controle negativo 7: modo PONTEIRO — ref inexistente tem de RECUSAR,
        # e ref existente do mesmo clone tem de passar pelo caminho do cat-file.
        import subprocess as _sp
        _sp.run(["git", "init", "-q"], cwd=raiz, check=True)
        (_sp.run(["git", "config", "user.email", "t@t"], cwd=raiz, check=False))
        (_sp.run(["git", "config", "user.name", "t"], cwd=raiz, check=False))
        (raiz / "_selftest/remota.md").write_text(
            "---\nestado_documental: homologado-documentalmente\ntem_artigo: sim\n---\n\n# R\n\nAchado Um\n\nAchado Dois\n",
            encoding="utf-8")
        _sp.run(["git", "add", "-A"], cwd=raiz, check=True)
        _sp.run(["git", "commit", "-qm", "base"], cwd=raiz, check=True)
        _sp.run(["git", "branch", "-f", "minha-fonte"], cwd=raiz, check=True)
        h_rem = hashlib.sha256((raiz / "_selftest/remota.md").read_bytes()).hexdigest()
        (raiz / "_selftest/remota.md").unlink()   # agora só existe no ref

        ponteiro_bom = {
            "id": "ponteiro-ok",
            "deriva_de": {"tipo": "artigo-didatico", "path": "_selftest/remota.md",
                          "sha256": h_rem, "ref": "minha-fonte"},
            "formato": "carrossel",
            "itens": [{"ordem": 1, "fonte": "Achado Um"}, {"ordem": 2, "fonte": "Achado Dois"}],
            "sha256_da_peca": "abc", "aprovacao": {"por": "P", "em": "D", "hash_da_peca": "abc"},
        }
        rp = montar({"lote": "PT", "pecas": [ponteiro_bom]}, raiz)
        if rp["aprovadas"] != 1:
            falhas.append(f"modo PONTEIRO recusou peca boa: {rp['erros']}")

        ruim = json.loads(json.dumps(ponteiro_bom)); ruim["id"] = "ref-falso"
        ruim["deriva_de"]["ref"] = "branch-que-nao-existe"
        rp2 = montar({"lote": "PT", "pecas": [ruim]}, raiz)
        if not any("ref 'branch-que-nao-existe'" in e for e in rp2["erros"]):
            falhas.append("controle negativo ausente: ref inexistente nao foi recusado")

        ruim2 = json.loads(json.dumps(ponteiro_bom)); ruim2["id"] = "sem-ref"
        del ruim2["deriva_de"]["ref"]
        rp3 = montar({"lote": "PT", "pecas": [ruim2]}, raiz)
        if not any("sem ponteiro remoto" in e for e in rp3["erros"]):
            falhas.append("controle negativo ausente: origem ausente sem ref nao foi recusada")

        ruim3 = json.loads(json.dumps(ponteiro_bom)); ruim3["id"] = "hash-do-ref-errado"
        ruim3["deriva_de"]["sha256"] = "0" * 64
        rp4 = montar({"lote": "PT", "pecas": [ruim3]}, raiz)
        if not any("sha256 do ponteiro nao confere" in e or "sha256 do ponteiro não confere" in e for e in rp4["erros"]):
            falhas.append("controle negativo ausente: hash divergente no modo PONTEIRO nao foi pego")

        for f in falhas:
            print(f"FALHA: {f}")
        print(json.dumps({"selftest": "PASS" if not falhas else "FAIL",
                          "aprovadas": r["aprovadas"], "recusadas": r["recusadas"],
                          "erros": len(r["erros"]), "fila": len(r["fila"])}, ensure_ascii=False))
        return 0 if not falhas else 1


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Monta lote de publicação; não publica.")
    ap.add_argument("--lote")
    ap.add_argument("--raiz", default=".")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)

    if a.selftest:
        return selftest()
    if not a.lote:
        ap.error("--lote e obrigatorio (ou use --selftest)")

    lote = json.loads(Path(a.lote).read_text(encoding="utf-8"))
    r = montar(lote, Path(a.raiz))
    print(json.dumps(r, ensure_ascii=False, indent=1))
    return 0 if not r["erros"] else 1


if __name__ == "__main__":
    sys.exit(main())
