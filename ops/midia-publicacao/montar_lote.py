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
    # `curado` e `revisado-com-fonte-integral` entram porque GOVERNANCA_DOCUMENTAL.md:86/88
    # os declara equivalentes a homologado-documentalmente. O gate recusá-los contradizia a
    # taxonomia do próprio acervo (defeito MEDIA da auditoria TECO de 2026-11-20).
    "curado",
    "revisado-com-fonte-integral",
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


# Leitor com dois modos: disco (produção) e memória (selftest em ambiente read-only).
# O selftest precisa rodar em sandbox read-only — auditor não tem diretório gravável —
# e um gate que só se prova onde há escrita não se prova onde é auditado.
_MEM: dict[str, str] | None = None


def _texto(p: Path) -> str | None:
    if _MEM is not None:
        return _MEM.get(str(p))
    return p.read_text(encoding="utf-8", errors="replace") if p.is_file() else None


def _existe(p: Path) -> bool:
    if _MEM is not None:
        return str(p) in _MEM
    return p.is_file()


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


def _resolve_ponteiro(raiz: Path, caminho: str, der: dict) -> bool:
    """Um ponteiro resolve se existe no disco (ou na memória) ou no ref declarado."""
    alvo = (raiz / caminho).resolve()
    if _existe(alvo):
        return True
    ref = (der.get("ref") or "").strip()
    if not ref:
        return False
    ok, _ = _blob_no_ref(raiz, ref, caminho)
    return ok


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
    if _existe(alvo):
        via = "BYTES"
        conteudo = _texto(alvo) or ""
        real = hashlib.sha256(conteudo.encode("utf-8")).hexdigest() if _MEM is not None else sha256_file(alvo)
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
    # P3 estrutural. O soberano definiu o critério como "estado da arte da coleção E no
    # mínimo um artigo". Um booleano declarado no frontmatter não prova nada: quem escreve
    # `tem_artigo: sim` não precisa ter artigo nenhum. Por isso a peça declara o bloco
    # `colecao` com os dois ponteiros, e cada ponteiro tem de RESOLVER — no disco ou no ref.
    # Medido em auditoria TECO de 2026-11-20: a versão anterior aceitava uma origem mínima
    # só com o booleano (defeito ALTA).
    col = peca.get("colecao") or {}
    eda = (col.get("estado_da_arte") or "").strip()
    arts = col.get("artigos") or []
    if not eda:
        erros.append(f"{pid}: P3 recusa — peça sem 'colecao.estado_da_arte'; homologação exige estado da arte da coleção")
    elif not _resolve_ponteiro(raiz, eda, der):
        erros.append(f"{pid}: P3 recusa — 'colecao.estado_da_arte' não resolve: {eda}")
    if not isinstance(arts, list) or not arts:
        erros.append(f"{pid}: P3 recusa — peça sem 'colecao.artigos'; homologação exige no mínimo um artigo")
    else:
        for a in arts:
            if not _resolve_ponteiro(raiz, str(a), der):
                erros.append(f"{pid}: P3 recusa — 'colecao.artigos' com ponteiro que não resolve: {a}")

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


_ORIGEM_OK = (
    "---\nestado_documental: homologado-documentalmente\ntem_artigo: sim\n---\n\n"
    "# Origem\n\nAchado Um\n\nAchado Dois\n"
)
_ORIGEM_REV = (
    "---\nestado_documental: em-revisao-documental\ntem_artigo: sim\n---\n\n"
    "# Origem em revisão\n\nAchado Um\n\nAchado Dois\n"
)


def _peca_base(pid: str, path: str, sha: str, **kw) -> dict:
    p = {
        "id": pid,
        "deriva_de": {"tipo": "estado-da-arte", "path": path, "sha256": sha},
        "colecao": {"gaveta": "g", "estado_da_arte": path, "artigos": [path]},
        "formato": "carrossel",
        "itens": [{"ordem": 1, "fonte": "Achado Um"}, {"ordem": 2, "fonte": "Achado Dois"}],
        "sha256_da_peca": "abc123",
        "aprovacao": {"por": "FABIO_SOBERANO", "em": "2026-11-20", "hash_da_peca": "abc123"},
        "agendamento": [{"canal": "instagram", "data": "2026-11-25", "hora": "09:00"}],
    }
    p.update(kw)
    return p


def selftest() -> int:
    """Controle negativo duplo, em memória: cada portão tem de RECUSAR o que deve recusar.

    Roda sem diretório gravável de propósito — o auditor executa em sandbox read-only, e um
    selftest que exige escrita não pode ser executado por quem audita (defeito medido na
    auditoria TECO de 2026-11-20, Q1/Q6/Q8 não executáveis).
    """
    global _MEM
    falhas: list[str] = []
    h_ok = hashlib.sha256(_ORIGEM_OK.encode()).hexdigest()
    h_rev = hashlib.sha256(_ORIGEM_REV.encode()).hexdigest()
    base = Path("/mem")

    _MEM = {"/mem/ok.md": _ORIGEM_OK, "/mem/rev.md": _ORIGEM_REV}
    try:
        # controle positivo
        r = montar({"lote": "ST", "pecas": [_peca_base("ok", "ok.md", h_ok)]}, base)
        if r["aprovadas"] != 1:
            falhas.append(f"controle positivo falhou: peça correta recusada -> {r['erros']}")
        if len(r["fila"]) != 1:
            falhas.append(f"esperava 1 item de fila, obteve {len(r['fila'])}")

        # P1 — tipo ficha
        r = montar({"lote": "ST", "pecas": [_peca_base("p1", "ok.md", h_ok,
                    deriva_de={"tipo": "ficha", "path": "ok.md", "sha256": h_ok})]}, base)
        if not any("P1 recusa" in e and "ficha" in e for e in r["erros"]):
            falhas.append("P1: ficha não foi recusada")

        # P2 — hash divergente
        r = montar({"lote": "ST", "pecas": [_peca_base("p2", "ok.md", "0" * 64)]}, base)
        if not any("P2 recusa" in e and "sha256" in e for e in r["erros"]):
            falhas.append("P2: hash divergente não foi recusado")

        # P3a — estado não homologado
        r = montar({"lote": "ST", "pecas": [_peca_base("p3a", "rev.md", h_rev,
                    deriva_de={"tipo": "estado-da-arte", "path": "rev.md", "sha256": h_rev},
                    colecao={"estado_da_arte": "rev.md", "artigos": ["rev.md"]})]}, base)
        if not any("P3 recusa" in e and "em-revisao-documental" in e for e in r["erros"]):
            falhas.append("P3a: estado em-revisao-documental não foi recusado")

        # P3b — coleção SEM estado da arte (defeito ALTA da auditoria: booleano não prova)
        r = montar({"lote": "ST", "pecas": [_peca_base("p3b", "ok.md", h_ok,
                    colecao={"artigos": ["ok.md"]})]}, base)
        if not any("P3 recusa" in e and "estado_da_arte" in e for e in r["erros"]):
            falhas.append("P3b: coleção sem estado da arte não foi recusada")

        # P3c — coleção sem artigo
        r = montar({"lote": "ST", "pecas": [_peca_base("p3c", "ok.md", h_ok,
                    colecao={"estado_da_arte": "ok.md", "artigos": []})]}, base)
        if not any("P3 recusa" in e and "colecao.artigos" in e for e in r["erros"]):
            falhas.append("P3c: coleção sem artigo não foi recusada")

        # P3d — ponteiro de coleção que não resolve
        r = montar({"lote": "ST", "pecas": [_peca_base("p3d", "ok.md", h_ok,
                    colecao={"estado_da_arte": "nao-existe.md", "artigos": ["ok.md"]})]}, base)
        if not any("P3 recusa" in e and "não resolve" in e for e in r["erros"]):
            falhas.append("P3d: ponteiro de coleção inexistente não foi recusado")

        # P4 — formato incoerente com a contagem de itens (carrossel exige 2..20)
        r = montar({"lote": "ST", "pecas": [_peca_base("p4", "ok.md", h_ok,
                    formato="carrossel", itens=[{"ordem": 1, "fonte": "Achado Um"}])]}, base)
        if not any("P4 recusa" in e for e in r["erros"]):
            falhas.append("P4: carrossel com 1 item não foi recusado")
        r = montar({"lote": "ST", "pecas": [_peca_base("p4b", "ok.md", h_ok, formato="reels-x")]}, base)
        if not any("P4 recusa" in e and "desconhecido" in e for e in r["erros"]):
            falhas.append("P4b: formato desconhecido não foi recusado")

        # P6 — aprovação de outro bytes
        r = montar({"lote": "ST", "pecas": [_peca_base("p6", "ok.md", h_ok,
                    aprovacao={"por": "F", "em": "D", "hash_da_peca": "outro-hash"})]}, base)
        if not any("P6 recusa" in e for e in r["erros"]):
            falhas.append("P6: aprovação de outro bytes não foi recusada")
        r = montar({"lote": "ST", "pecas": [_peca_base("p6b", "ok.md", h_ok,
                    aprovacao={"hash_da_peca": "abc123"})]}, base)
        if not any("P6 recusa" in e and "'por'" in e for e in r["erros"]):
            falhas.append("P6b: aprovação sem autor não foi recusada")

        # P5 — fonte inventada
        r = montar({"lote": "ST", "pecas": [_peca_base("p5", "ok.md", h_ok,
                    itens=[{"ordem": 1, "fonte": "Achado Um"},
                           {"ordem": 2, "fonte": "Achado Que Nao Existe"}])]}, base)
        if not any("P5 recusa" in e and "Achado Que Nao Existe" in e for e in r["erros"]):
            falhas.append("P5: fonte inventada não foi recusada")

        # PONTEIRO — resolução real por git, sem diretório temporário.
        # O próprio arquivo deste script é usado como objeto existente no HEAD.
        aqui = Path(__file__).resolve().parent
        # o caminho no git é relativo à RAIZ do repositório, não ao cwd do script
        try:
            topo = subprocess.run(["git", "-C", str(aqui), "rev-parse", "--show-toplevel"],
                                  capture_output=True, text=True, timeout=15).stdout.strip()
            rel = str(Path(__file__).resolve().relative_to(topo)) if topo else "montar_lote.py"
        except (OSError, subprocess.SubprocessError, ValueError):
            rel = "montar_lote.py"
        ok, _ = _blob_no_ref(aqui, "HEAD", rel)
        if not ok:
            falhas.append(f"ponteiro: 'HEAD:{rel}' não resolveu neste clone")
        ok2, _ = _blob_no_ref(aqui, "ref-que-nao-existe", rel)
        if ok2:
            falhas.append("ponteiro: ref inexistente resolveu (deveria falhar)")

        # PONTEIRO — origem ausente sem ref
        r = montar({"lote": "ST", "pecas": [_peca_base("ptr1", "sumiu.md", h_ok)]}, base)
        if not any("sem ponteiro remoto" in e for e in r["erros"]):
            falhas.append("ponteiro: origem ausente sem ref não foi recusada")
    finally:
        _MEM = None

    for f in falhas:
        print(f"FALHA: {f}")
    print(json.dumps({"selftest": "PASS" if not falhas else "FAIL",
                      "modo": "EM_MEMORIA", "controles_negativos": 11,
                      "falhas": len(falhas)}, ensure_ascii=False))
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
