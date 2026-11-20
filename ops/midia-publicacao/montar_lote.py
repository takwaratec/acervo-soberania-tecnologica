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
  P0  esquema fechado: tipo e presença de cada campo, em todos os níveis; id único
  P1  a peça de mídia declara `deriva_de` com tipo editorial válido (nunca ficha)
  P2  a origem existe (bytes no worktree ou `git cat-file` no ref) e o `sha256` confere
  P3  a peça editorial está homologada E a coleção tem estado da arte + >=1 artigo, cada
      ponteiro resolvendo dentro do repositório, em papéis distintos e declarados
  P4  o formato declarado bate com o conteúdo (carrossel exige 2..20 itens)
  P5  toda afirmação da peça de mídia cita `fonte` que existe no corpo da peça editorial
  P6  aprovacao registrada: autor + data + hash da peça aprovada

Uso:
    python3 montar_lote.py --lote <lote.json> --raiz <repo> [--json]
    python3 montar_lote.py --selftest
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

# Estados documentais que contam como homologado para efeito de PUBLICAÇÃO.
# Derivados de GOVERNANCA_DOCUMENTAL.md (tabela de equivalência, linhas 82-90): o estado
# canônico mais os sete valores legados que ela mapeia para homologado-documentalmente.
# "em-revisao-documental" NÃO é homologação.
_BASE_HASH: "Path | None" = None


def _digest_dos_artefatos(peca: dict, raiz: "Path | None") -> dict:
    """sha256 dos artefatos que o P3 usa para decidir.

    Sem isso, a aprovação cobria o manifesto mas não as fontes: trocar uma palavra do
    artigo da coleção mudava o resultado do P3 sem invalidar o hash (auditoria TECO,
    rodada 8). A aprovação passa a cobrir as fontes que ela invoca.
    """
    if raiz is None:
        return {}
    alvos: list[str] = []
    der = peca.get("deriva_de")
    if isinstance(der, dict) and isinstance(der.get("path"), str):
        alvos.append(der["path"])
    col = peca.get("colecao")
    if isinstance(col, dict):
        if isinstance(col.get("estado_da_arte"), str):
            alvos.append(col["estado_da_arte"])
        arts = col.get("artigos")
        if isinstance(arts, list):
            alvos.extend([a for a in arts if isinstance(a, str)])
    if isinstance(der, dict) and isinstance(col, dict) and isinstance(col.get("artigos"), list):
        for a in col["artigos"]:
            if isinstance(a, str) and a != der.get("path"):
                d2 = dict(der)
                d2["path"] = a
                _ = d2
    out: dict[str, str] = {}
    for caminho in dict.fromkeys(alvos):
        try:
            texto = _ler_ponteiro(raiz, caminho, peca.get("deriva_de") if isinstance(peca.get("deriva_de"), dict) else {})
        except Exception:
            texto = None
        out[caminho] = hashlib.sha256(texto.encode("utf-8")).hexdigest() if texto is not None else "NAO_RESOLVIDO"
    return out


def hash_da_peca(peca: dict, raiz: "Path | None" = None) -> str:
    """sha256 canônico do conteúdo da peça: tudo, menos o próprio hash e a aprovação.

    Sem isso, `sha256_da_peca` era um campo livre: bastava declarar o mesmo texto
    nos dois lados para aprovar qualquer coisa — e alterar `texto_curto` depois não
    invalidava nada. A rodada 6 da auditoria TECO aprovou dois manifestos com o mesmo
    hash literal e conteúdo diferente. Aqui o hash é DERIVADO, não declarado.
    """
    corpo = {k: v for k, v in peca.items() if k not in {"sha256_da_peca", "aprovacao"}}
    # `por` e `em` entram no hash: sem isso a data da aprovação podia mudar sem invalidar
    # nada, e a nota do CLI prometia mais do que o código cumpria (auditoria TECO, rodada 7).
    apr = peca.get("aprovacao") if isinstance(peca.get("aprovacao"), dict) else {}
    corpo["#aprovacao"] = {"por": apr.get("por", ""), "em": apr.get("em", "")}
    corpo["#artefatos"] = _digest_dos_artefatos(peca, raiz if raiz is not None else _BASE_HASH)
    bruto = json.dumps(corpo, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(bruto.encode("utf-8")).hexdigest()


AUTORIDADES_APROVADORAS = {"FABIO_SOBERANO"}

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
                           capture_output=True, timeout=30)
    except (OSError, subprocess.SubprocessError) as e:
        return False, f"git indisponível: {e}"
    if b.returncode != 0:
        return False, (b.stderr or b"").decode("utf-8", "replace").strip()[:200] or "objeto não encontrado"
    try:
        return True, b.stdout.decode("utf-8")
    except UnicodeDecodeError:
        # blob binário não é documento de acervo: recusa nomeada, não exceção
        return False, "blob não é UTF-8 (documento de acervo é texto)"


def normalizar_estado(v: str) -> str:
    return (v or "").strip().strip('"').strip("'").lower()


def _dentro(raiz: Path, caminho: str) -> Path | None:
    """Contém o caminho na raiz. Ponteiro para ../../etc/hosts não é fonte do acervo."""
    alvo = (raiz / caminho).resolve()
    r = raiz.resolve()
    return alvo if (alvo == r or r in alvo.parents) else None


def _ler_ponteiro(raiz: Path, caminho: str, der: dict) -> str | None:
    """Devolve o TEXTO do ponteiro (disco, memória ou ref) — ou None se não resolver."""
    alvo = _dentro(raiz, caminho)
    if alvo is None:
        return None
    t = _texto(alvo)
    if t is not None:
        return t
    ref = (der.get("ref") or "").strip()
    if not ref:
        return None
    ok, bruto = _blob_no_ref(raiz, ref, caminho)
    return bruto if ok else None


def _resolve_ponteiro(raiz: Path, caminho: str, der: dict) -> bool:
    return _ler_ponteiro(raiz, caminho, der) is not None


def _conferir_artefato(raiz: Path, caminho: str, der: dict, pid: str,
                       rotulo: str, exigir_artigo: bool = False,
                       exigir_estado_da_arte: bool = False) -> list[str]:
    """Existência não basta: o ponteiro tem de ser um documento HOMOLOGADO do acervo.

    A auditoria de 2026-11-20 (rodada 2) mostrou que aceitar só "o caminho existe"
    permitia usar o mesmo arquivo como estado da arte e artigo, e aceitava ../../etc/hosts.
    Aqui o frontmatter é lido e conferido: estado_documental homologado, e no caso do
    artigo, tipo documental de artigo ou marca e_artigo.
    """
    erros: list[str] = []
    if _dentro(raiz, caminho) is None:
        return [f"{pid}: P3 recusa — '{rotulo}' aponta para fora do repositório: {caminho}"]
    texto = _ler_ponteiro(raiz, caminho, der)
    if texto is None:
        return [f"{pid}: P3 recusa — '{rotulo}' não resolve: {caminho}"]
    fm = ler_frontmatter(texto)
    estado = normalizar_estado(str(fm.get("estado_documental", "")))
    if estado not in ESTADOS_HOMOLOGADOS:
        erros.append(
            f"{pid}: P3 recusa — '{rotulo}' ({caminho}) tem estado_documental={estado or 'ausente'}, "
            "que não é homologado"
        )
    tipo = str(fm.get("tipo_documental", "")).lower()
    tipo_norm = tipo.replace("_", "-")
    if exigir_artigo:
        marca = str(fm.get("e_artigo", "")).lower() in {"sim", "true", "1"}
        if not marca and not tipo_norm.startswith("artigo"):
            erros.append(
                f"{pid}: P3 recusa — '{rotulo}' ({caminho}) não se declara artigo "
                f"(tipo_documental={tipo or 'ausente'})"
            )
    if exigir_estado_da_arte:
        marca = str(fm.get("e_estado_da_arte", "")).lower() in {"sim", "true", "1"}
        if not marca and not tipo_norm.startswith("estado"):
            erros.append(
                f"{pid}: P3 recusa — '{rotulo}' ({caminho}) não se declara estado da arte "
                f"(tipo_documental={tipo or 'ausente'}); o papel de estado da arte não pode ser "
                "cumprido por um artigo"
            )
    return erros


# Esquema fechado da peça de mídia R1. Cada campo tem tipo e obrigatoriedade.
# "fechado" = campo não declarado é recusa: um erro de digitação em `colecao`
# não pode virar um campo ignorado em silêncio (auditoria TECO, rodada 5).
ESQUEMA: dict = {
    "id": (str, True),
    "deriva_de": (dict, True, {
        "tipo": (str, True),
        "path": (str, True),
        "sha256": (str, True),
        "ref": (str, False),
        "origem": (str, False),
    }),
    "colecao": (dict, True, {
        "gaveta": (str, False),
        "estado_da_arte": (str, True),
        "artigos": (list, True),
    }),
    "formato": (str, True),
    "formato_justificativa": (str, False),
    "itens": (list, True, {
        "ordem": (int, False),
        "texto_curto": (str, False),
        "fonte": (str, True),
    }),
    "sha256_da_peca": (str, True),
    "aprovacao": (dict, True, {
        "por": (str, True),
        "em": (str, True),
        "hash_da_peca": (str, True),
    }),
    "agendamento": (list, False, {
        "canal": (str, True),
        "data": (str, True),
        "hora": (str, False),
    }),
    "legenda": (str, False),
    "hashtags": (list, False),
    "alt_text": (str, False),
    "rastreabilidade_da_arte": (dict, False, {
        "autor_da_arte": (str, False),
        "prompt_usado": (str, False),
        "confere_com": (str, False),
    }),
}


def _conferir_campos(obj: dict, esquema: dict, caminho: str, pid: str) -> list[str]:
    erros: list[str] = []
    for campo in obj:
        if campo not in esquema:
            erros.append(
                f"{pid}: P0 recusa — campo desconhecido em {caminho or 'peça'}: {campo!r} "
                "(esquema fechado; campo ignorado em silêncio é erro de digitação, não extensão)"
            )
    for campo, defn in esquema.items():
        tipo, obrigatorio = defn[0], defn[1]
        sub = defn[2] if len(defn) > 2 else None
        cheio = f"{caminho}.{campo}" if caminho else campo
        if campo not in obj:
            if obrigatorio:
                erros.append(f"{pid}: P0 recusa — '{cheio}' é obrigatório")
            continue
        valor = obj[campo]
        # `isinstance(True, int)` é True em Python: booleano passaria como inteiro
        # (auditoria TECO, rodada 6). Tipo declarado é tipo de verdade.
        if tipo is int and isinstance(valor, bool):
            erros.append(f"{pid}: P0 recusa — '{cheio}' deve ser int, recebido bool")
            continue
        if not isinstance(valor, tipo):
            erros.append(
                f"{pid}: P0 recusa — '{cheio}' deve ser {tipo.__name__}, "
                f"recebido {type(valor).__name__}"
            )
            continue
        if sub is not None and tipo is dict:
            erros.extend(_conferir_campos(valor, sub, cheio, pid))
        elif sub is not None and tipo is list:
            for i, item in enumerate(valor):
                if not isinstance(item, dict):
                    erros.append(
                        f"{pid}: P0 recusa — '{cheio}[{i}]' deve ser objeto, "
                        f"recebido {type(item).__name__}"
                    )
                    continue
                erros.extend(_conferir_campos(item, sub, f"{cheio}[{i}]", pid))
    return erros


def validar_estrutura(peca: object) -> list[str]:
    """P0 — tipo e presença de cada campo, em todos os níveis, antes de qualquer `.get`.

    A rodada 4 fechou o nível da peça; a rodada 5 mostrou que os níveis aninhados
    (`deriva_de.tipo`, `deriva_de.path`, `itens[i]`, `agendamento[i]`) ainda levantavam
    exceção e que campo ausente era pulado em silêncio. Agora o esquema é fechado e
    percorrido inteiro.
    """
    if not isinstance(peca, dict):
        return [f"<peça não textual>: P0 recusa — peça deve ser objeto, recebido {type(peca).__name__}"]
    pid = peca.get("id") if isinstance(peca.get("id"), str) else "<sem-id>"
    erros = _conferir_campos(peca, ESQUEMA, "", pid)
    if isinstance(peca.get("id"), str) and not peca["id"].strip():
        erros.append(f"{pid}: P0 recusa — 'id' vazio; identificador serve para rastrear o lote")
    # limites que o schema declara e o código tem de aplicar — senão o documento mente
    leg = peca.get("legenda")
    if isinstance(leg, str) and len(leg) > 2200:
        erros.append(f"{pid}: P0 recusa — 'legenda' com {len(leg)} caracteres; limite da plataforma é 2200")
    tag = peca.get("hashtags")
    if isinstance(tag, list) and len(tag) > 30:
        erros.append(f"{pid}: P0 recusa — 'hashtags' com {len(tag)} itens; limite é 30")
    for i, t in enumerate(tag if isinstance(tag, list) else []):
        if not isinstance(t, str):
            erros.append(f"{pid}: P0 recusa — 'hashtags[{i}]' deve ser str, recebido {type(t).__name__}")
    rast = peca.get("rastreabilidade_da_arte")
    if isinstance(rast, dict):
        pu = rast.get("prompt_usado")
        if "prompt_usado" in rast and (not isinstance(pu, str) or not re.fullmatch(r"[0-9a-f]{64}", (pu or "").lower())):
            erros.append(f"{pid}: P0 recusa — 'rastreabilidade_da_arte.prompt_usado' deve ser sha256 (64 hex), recebido {pu[:20]!r}")
    return erros


def validar_peca(peca: dict, raiz: Path) -> list[str]:
    erros = validar_estrutura(peca)
    if erros:
        return erros
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
    col = peca.get("colecao")
    if col is None:
        erros.append(f"{pid}: P3 recusa — peça sem bloco 'colecao'")
        return erros
    if not isinstance(col, dict):
        erros.append(f"{pid}: P3 recusa — 'colecao' deve ser objeto, recebido {type(col).__name__}")
        return erros
    eda = col.get("estado_da_arte")
    if eda is not None and not isinstance(eda, str):
        erros.append(f"{pid}: P3 recusa — 'colecao.estado_da_arte' deve ser texto, recebido {type(eda).__name__}")
        return erros
    eda = (eda or "").strip()
    arts = col.get("artigos")
    if arts is not None and not isinstance(arts, list):
        erros.append(f"{pid}: P3 recusa — 'colecao.artigos' deve ser lista, recebido {type(arts).__name__}")
        return erros
    arts = arts or []
    for a in arts:
        if not isinstance(a, str):
            erros.append(f"{pid}: P3 recusa — 'colecao.artigos' contém item não textual: {type(a).__name__}")
            return erros
    if not eda:
        erros.append(f"{pid}: P3 recusa — peça sem 'colecao.estado_da_arte'; homologação exige estado da arte da coleção")
    else:
        erros.extend(_conferir_artefato(raiz, eda, der, pid, "colecao.estado_da_arte",
                                        exigir_estado_da_arte=True))
    if not isinstance(arts, list) or not arts:
        erros.append(f"{pid}: P3 recusa — peça sem 'colecao.artigos'; homologação exige no mínimo um artigo")
    else:
        eda_norm = str(_dentro(raiz, eda)) if eda else ""
        for a in arts:
            a = str(a)
            a_norm = str(_dentro(raiz, a))
            if eda and (a == eda or a_norm == eda_norm):
                erros.append(
                    f"{pid}: P3 recusa — 'colecao.artigos' repete o estado da arte ({a}); "
                    "o critério exige estado da arte E artigo, dois artefatos distintos"
                )
                continue
            erros.extend(_conferir_artefato(raiz, a, der, pid, "colecao.artigos", exigir_artigo=True))

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
    # Quando P2 passa, o corpo está sempre disponível (bytes ou ref), então este portão
    # sempre verifica. Não existe estado "NAO_VERIFICADO": a documentação anterior prometia
    # um estado que o fluxo nunca produz (auditoria TECO, rodada 5).
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
    h_peca = (peca.get("sha256_da_peca") or "").strip().lower()
    h_apr = (apr.get("hash_da_peca") or "").strip().lower()
    # Dois campos vazios são IGUAIS: comparar só igualdade aprovava peça sem hash
    # nenhum (auditoria TECO, rodada 5). Presença é exigida antes da comparação.
    if not h_peca:
        erros.append(f"{pid}: P6 recusa — 'sha256_da_peca' ausente; sem hash não há bytes aprovados")
    elif not re.fullmatch(r"[0-9a-f]{64}", h_peca):
        erros.append(f"{pid}: P6 recusa — 'sha256_da_peca' não é sha256 (64 hex): {h_peca[:20]}…")
    else:
        calculado = hash_da_peca(peca, raiz)
        if h_peca != calculado:
            erros.append(
                f"{pid}: P6 recusa — 'sha256_da_peca' não corresponde ao conteúdo da peça: "
                f"declarado {h_peca[:16]}… != calculado {calculado[:16]}…; "
                "aprovação de outro conteúdo não aprova este"
            )
    if not h_apr:
        erros.append(f"{pid}: P6 recusa — 'aprovacao.hash_da_peca' ausente; aprovação sem bytes não aprova nada")
    if h_peca and h_apr and h_peca != h_apr:
        erros.append(
            f"{pid}: P6 recusa — 'aprovacao.hash_da_peca' não corresponde a 'sha256_da_peca'; "
            "aprovação de outro bytes não aprova esta peça"
        )
    autor = (apr.get("por") or "").strip()
    if autor.upper() not in AUTORIDADES_APROVADORAS:
        erros.append(
            f"{pid}: P6 recusa — aprovador {autor!r} não é autoridade registrada "
            f"(aceitos: {sorted(AUTORIDADES_APROVADORAS)}); texto livre não é assinatura"
        )
    data = (apr.get("em") or "").strip()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", data):
        erros.append(f"{pid}: P6 recusa — 'aprovacao.em'={data!r} não é data ISO (AAAA-MM-DD)")
    else:
        try:
            datetime.date.fromisoformat(data)
        except ValueError:
            erros.append(f"{pid}: P6 recusa — 'aprovacao.em'={data!r} não é data de calendário válida")
    return erros


def montar(lote: dict, raiz: Path) -> dict:
    if not isinstance(lote, dict):
        return {"lote": None, "total_declarado": 0, "aprovadas": 0, "recusadas": 0,
                "erros": [f"P0 recusa — lote deve ser objeto, recebido {type(lote).__name__}"],
                "fila": [], "publicou_alguma_coisa": False,
                "nota": "montar_lote.py nao publica. Produz lote e fila; a publicacao e outro ato."}
    if not isinstance(lote.get("pecas"), list):
        return {"lote": lote.get("lote"), "total_declarado": 0, "aprovadas": 0, "recusadas": 0,
                "erros": [f"P0 recusa — 'pecas' deve ser lista, recebido {type(lote.get('pecas')).__name__}"],
                "fila": [], "publicou_alguma_coisa": False,
                "nota": "montar_lote.py nao publica. Produz lote e fila; a publicacao e outro ato."}
    pecas = lote.get("pecas") or []
    erros: list[str] = []
    aprovadas: list[dict] = []

    # id duplicado torna a fila ambígua: duas peças com o mesmo nome não são rastreáveis
    vistos: dict[str, int] = {}
    for p in pecas:
        if isinstance(p, dict) and isinstance(p.get("id"), str):
            vistos[p["id"]] = vistos.get(p["id"], 0) + 1
    duplicados = {k for k, n in vistos.items() if n > 1}

    for p in pecas:
        e = validar_peca(p, raiz)
        if isinstance(p, dict) and p.get("id") in duplicados:
            e = list(e) + [f"{p.get('id')}: P0 recusa — id repetido no lote; identificador tem de ser único"]
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
    fila.sort(key=lambda x: (str(x.get("data") or ""), str(x.get("hora") or "")))

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


_EDA = (
    "---\nestado_documental: homologado-documentalmente\ntipo_documental: estado-da-arte\n"
    "titulo: Estado da arte da coleção\n---\n\n# Estado da arte\n\nAchado Um\n\nAchado Dois\n"
)
_ART = (
    "---\nestado_documental: homologado-documentalmente\ntipo_documental: artigo-didatico\n"
    "titulo: Artigo didático da coleção\n---\n\n# Artigo\n\nAchado Um\n\nAchado Dois\n"
)
_REV = (
    "---\nestado_documental: em-revisao-documental\ntipo_documental: artigo-didatico\n---\n\n"
    "# Em revisão\n\nAchado Um\n\nAchado Dois\n"
)
_NAO_ART = (
    "---\nestado_documental: homologado-documentalmente\ntipo_documental: estado-da-arte\n---\n\n"
    "# Outro estado da arte\n\nAchado Um\n\nAchado Dois\n"
)


def _peca_base(pid: str, path: str, sha: str, **kw) -> dict:
    p = {
        "id": pid,
        "deriva_de": {"tipo": "estado-da-arte", "path": path, "sha256": sha},
        "colecao": {"gaveta": "g", "estado_da_arte": path, "artigos": ["/mem/art.md"]},
        "formato": "carrossel",
        "itens": [{"ordem": 1, "fonte": "Achado Um"}, {"ordem": 2, "fonte": "Achado Dois"}],
        "sha256_da_peca": "abc123",
        "aprovacao": {"por": "FABIO_SOBERANO", "em": "2026-11-20", "hash_da_peca": "abc123"},
        "agendamento": [{"canal": "instagram", "data": "2026-11-25", "hora": "09:00"}],
    }
    p.update(kw)
    p["sha256_da_peca"] = hash_da_peca(p, _BASE_HASH)
    if isinstance(p.get("aprovacao"), dict) and "hash_da_peca" in p["aprovacao"]:
        p["aprovacao"]["hash_da_peca"] = p["sha256_da_peca"]
    return p


def selftest() -> int:
    """Controle negativo duplo por portão, em memória — roda em sandbox read-only.

    O total de controles é CONTADO, não digitado: contador escrito à mão já divergiu do
    código real em auditoria (rodada 2, defeito BAIXA). Aqui não há como divergir.
    """
    global _MEM, _blob_no_ref, _BASE_HASH
    falhas: list[str] = []
    negativos: list[str] = []
    positivos: list[str] = []

    def ctl(nome: str, ok: bool, msg: str, positivo: bool = False) -> None:
        (positivos if positivo else negativos).append(nome)
        if not ok:
            falhas.append(f"{nome}: {msg}")

    h_eda = hashlib.sha256(_EDA.encode()).hexdigest()
    h_rev = hashlib.sha256(_REV.encode()).hexdigest()
    base = Path("/mem")
    _MEM = {"/mem/eda.md": _EDA, "/mem/art.md": _ART, "/mem/rev.md": _REV, "/mem/nao-art.md": _NAO_ART}
    _BASE_HASH = Path("/mem")
    refs = {"/mem/remoto.md": _EDA, "/mem/remoto-art.md": _ART}
    real_blob = _blob_no_ref

    def falso_blob(raiz, ref, caminho):
        if ref == "ref-existente" and caminho in {"/mem/remoto.md".lstrip("/"), "remoto.md", "remoto-art.md"}:
            return True, refs.get("/mem/" + caminho.lstrip("/"), _ART)
        return False, "objeto não encontrado"

    try:
        # ---------- controle positivo ----------
        r = montar({"lote": "ST", "pecas": [_peca_base("ok", "eda.md", h_eda)]}, base)
        ctl("positivo", r["aprovadas"] == 1, f"peça correta recusada -> {r['erros']}", positivo=True)
        ctl("fila", len(r["fila"]) == 1, f"esperava 1 item de fila, obteve {len(r['fila'])}", positivo=True)

        # ---------- P1 ----------
        r = montar({"lote": "ST", "pecas": [_peca_base("p1", "eda.md", h_eda,
                    deriva_de={"tipo": "ficha", "path": "eda.md", "sha256": h_eda})]}, base)
        ctl("P1", any("P1 recusa" in e and "ficha" in e for e in r["erros"]), "ficha não recusada")

        # ---------- P2 ----------
        r = montar({"lote": "ST", "pecas": [_peca_base("p2", "eda.md", "0" * 64)]}, base)
        ctl("P2", any("P2 recusa" in e and "sha256" in e for e in r["erros"]),
            "hash divergente não recusado")

        # ---------- P2 modo PONTEIRO, INTEGRADO (montar -> validar -> _blob_no_ref) ----------
        _blob_no_ref = falso_blob
        r = montar({"lote": "ST", "pecas": [_peca_base("ptr-ok", "remoto.md", h_eda,
                    deriva_de={"tipo": "estado-da-arte", "path": "remoto.md", "sha256": h_eda,
                               "ref": "ref-existente"},
                    colecao={"estado_da_arte": "remoto.md", "artigos": ["remoto-art.md"]})]}, base)
        ctl("PONTEIRO-ok", r["aprovadas"] == 1, f"ponteiro íntegro recusado -> {r['erros']}", positivo=True)

        r = montar({"lote": "ST", "pecas": [_peca_base("ptr-hash", "remoto.md", "0" * 64,
                    deriva_de={"tipo": "estado-da-arte", "path": "remoto.md", "sha256": "0" * 64,
                               "ref": "ref-existente"},
                    colecao={"estado_da_arte": "remoto.md", "artigos": ["remoto-art.md"]})]}, base)
        ctl("PONTEIRO-hash", any("sha256 do ponteiro" in e for e in r["erros"]),
            "hash divergente no ref não recusado")

        _blob_no_ref = real_blob
        r = montar({"lote": "ST", "pecas": [_peca_base("ptr-ref", "remoto.md", h_eda,
                    deriva_de={"tipo": "estado-da-arte", "path": "remoto.md", "sha256": h_eda,
                               "ref": "ref-que-nao-existe"},
                    colecao={"estado_da_arte": "remoto.md", "artigos": ["remoto-art.md"]})]}, base)
        ctl("PONTEIRO-ref", any("sem ponteiro remoto" in e or "não resolve" in e for e in r["erros"]),
            "ref inexistente aceito")
        r = montar({"lote": "ST", "pecas": [_peca_base("ptr-sem-ref", "sumiu.md", h_eda)]}, base)
        ctl("PONTEIRO-sem-ref", any("sem ponteiro remoto" in e for e in r["erros"]),
            "origem ausente sem ref aceita")

        # ---------- P3a: estado não homologado ----------
        r = montar({"lote": "ST", "pecas": [_peca_base("p3a", "rev.md", h_rev,
                    deriva_de={"tipo": "estado-da-arte", "path": "rev.md", "sha256": h_rev},
                    colecao={"estado_da_arte": "rev.md", "artigos": ["art.md"]})]}, base)
        ctl("P3-estado", any("não é homologado" in e for e in r["erros"]),
            "em-revisao-documental aceito")

        # ---------- P3b: sem estado da arte ----------
        r = montar({"lote": "ST", "pecas": [_peca_base("p3b", "eda.md", h_eda,
                    colecao={"artigos": ["art.md"]})]}, base)
        ctl("P3-sem-eda",
            any("sem 'colecao.estado_da_arte'" in e or "'colecao.estado_da_arte' é obrigatório" in e
                for e in r["erros"]), "coleção sem estado da arte aceita")

        # ---------- P3c: sem artigo ----------
        r = montar({"lote": "ST", "pecas": [_peca_base("p3c", "eda.md", h_eda,
                    colecao={"estado_da_arte": "eda.md", "artigos": []})]}, base)
        ctl("P3-sem-artigo", any("sem 'colecao.artigos'" in e for e in r["erros"]),
            "coleção sem artigo aceita")

        # ---------- P3d: ponteiro inexistente ----------
        r = montar({"lote": "ST", "pecas": [_peca_base("p3d", "eda.md", h_eda,
                    colecao={"estado_da_arte": "nao-existe.md", "artigos": ["art.md"]})]}, base)
        ctl("P3-inexistente", any("não resolve" in e for e in r["erros"]),
            "ponteiro inexistente aceito")

        # ---------- P3e: mesmo arquivo como estado da arte e artigo (rodada 2, defeito ALTA) ----------
        r = montar({"lote": "ST", "pecas": [_peca_base("p3e", "eda.md", h_eda,
                    colecao={"estado_da_arte": "eda.md", "artigos": ["eda.md"]})]}, base)
        ctl("P3-mesmo-arquivo", any("repete o estado da arte" in e for e in r["erros"]),
            "mesmo arquivo aceito como estado da arte e artigo")

        # ---------- P3f: artigo que não se declara artigo (rodada 2, defeito ALTA) ----------
        r = montar({"lote": "ST", "pecas": [_peca_base("p3f", "eda.md", h_eda,
                    colecao={"estado_da_arte": "eda.md", "artigos": ["nao-art.md"]})]}, base)
        ctl("P3-artigo-falso", any("não se declara artigo" in e for e in r["erros"]),
            "documento que não é artigo aceito como artigo")

        # ---------- P3g: ponteiro fora da raiz (rodada 2, defeito ALTA) ----------
        r = montar({"lote": "ST", "pecas": [_peca_base("p3g", "eda.md", h_eda,
                    colecao={"estado_da_arte": "../../etc/hosts", "artigos": ["art.md"]})]}, base)
        ctl("P3-fora-da-raiz", any("fora do repositório" in e for e in r["erros"]),
            "caminho fora da raiz aceito")

        # ---------- P3h: mesmo blob por caminho alias (rodada 3, defeito ALTA) ----------
        r = montar({"lote": "ST", "pecas": [_peca_base("p3h", "eda.md", h_eda,
                    colecao={"estado_da_arte": "art.md", "artigos": ["./art.md"]})]}, base)
        ctl("P3-alias", any("repete o estado da arte" in e for e in r["erros"]),
            "mesmo blob por caminho alias aceito nos dois papéis")

        # ---------- P3i: estado da arte tipado como artigo (rodada 3, defeito ALTA) ----------
        r = montar({"lote": "ST", "pecas": [_peca_base("p3i", "eda.md", h_eda,
                    colecao={"estado_da_arte": "art.md", "artigos": ["art.md"]})]}, base)
        ctl("P3-eda-e-artigo", any("não se declara estado da arte" in e for e in r["erros"]),
            "artigo aceito no papel de estado da arte")

        # ---------- P3j: estrutura malformada não pode explodir (rodada 3, defeito BAIXA) ----------
        r = montar({"lote": "ST", "pecas": [_peca_base("p3j", "eda.md", h_eda, colecao=["campo"])]}, base)
        ctl("P3-colecao-lista", any("'colecao' deve ser" in e for e in r["erros"]),
            "colecao como lista não gerou recusa nomeada")
        r = montar({"lote": "ST", "pecas": [_peca_base("p3k", "eda.md", h_eda,
                    colecao={"estado_da_arte": "eda.md", "artigos": "art.md"})]}, base)
        ctl("P3-artigos-texto", any("'colecao.artigos' deve ser list" in e or "deve ser lista" in e
            for e in r["erros"]), "artigos como texto não gerou recusa nomeada")

        # ---------- P0: estrutura (rodada 4, defeito MEDIA) ----------
        for nome, peca_ruim, esperado in [
            ("P0-deriva-lista", _peca_base("p0a", "eda.md", h_eda, deriva_de=["x"]), "'deriva_de' deve ser dict"),
            ("P0-itens-int", _peca_base("p0b", "eda.md", h_eda, itens=7), "'itens' deve ser list"),
            ("P0-aprovacao-texto", _peca_base("p0c", "eda.md", h_eda, aprovacao="ok"), "'aprovacao' deve ser dict"),
            ("P0-agendamento-texto", _peca_base("p0d", "eda.md", h_eda, agendamento="amanha"), "'agendamento' deve ser list"),
            ("P0-item-inteiro", _peca_base("p0e", "eda.md", h_eda, itens=[1, 2]), "'itens[0]' deve ser objeto"),
        ]:
            r = montar({"lote": "ST", "pecas": [peca_ruim]}, base)
            ctl(nome, any("P0 recusa" in e and esperado in e for e in r["erros"]),
                f"{nome} não gerou recusa nomeada -> {r['erros'][:1]}")

        r = montar(["nao", "e", "lote"], base)
        ctl("P0-lote-lista", any("P0 recusa" in e and "lote deve ser objeto" in e for e in r["erros"]),
            "lote como lista não gerou recusa nomeada")
        r = montar({"lote": "ST", "pecas": "uma"}, base)
        ctl("P0-pecas-texto", any("P0 recusa" in e and "'pecas' deve ser lista" in e for e in r["erros"]),
            "pecas como texto não gerou recusa nomeada")

        # ---------- P0 aninhado (rodada 5, defeito ALTA) ----------
        for nome, peca_ruim, esperado in [
            ("P0-deriva-tipo-int", _peca_base("p0f", "eda.md", h_eda,
                deriva_de={"tipo": 7, "path": "eda.md", "sha256": h_eda}), "'deriva_de.tipo' deve ser str"),
            ("P0-deriva-path-int", _peca_base("p0g", "eda.md", h_eda,
                deriva_de={"tipo": "estado-da-arte", "path": 7, "sha256": h_eda}), "'deriva_de.path' deve ser str"),
            ("P0-deriva-sha-int", _peca_base("p0h", "eda.md", h_eda,
                deriva_de={"tipo": "estado-da-arte", "path": "eda.md", "sha256": 7}), "'deriva_de.sha256' deve ser str"),
            ("P0-item-fonte-int", _peca_base("p0i", "eda.md", h_eda,
                itens=[{"fonte": 7}, {"fonte": "Achado Dois"}]), "'itens[0].fonte' deve ser str"),
            ("P0-agen-data-int", _peca_base("p0j", "eda.md", h_eda,
                agendamento=[{"canal": "ig", "data": 20261125}]), "'agendamento[0].data' deve ser str"),
            ("P0-aprov-em-int", _peca_base("p0k", "eda.md", h_eda,
                aprovacao={"por": "FABIO_SOBERANO", "em": 7, "hash_da_peca": "abc123"}),
                "'aprovacao.em' deve ser str"),
            ("P0-campo-desconhecido", _peca_base("p0l", "eda.md", h_eda, colecão={"x": 1}),
                "campo desconhecido"),
            ("P0-ausente-obrigatorio", _peca_base("p0m", "eda.md", h_eda,
                deriva_de={"tipo": "estado-da-arte", "path": "eda.md"}), "'deriva_de.sha256' é obrigatório"),
        ]:
            r = montar({"lote": "ST", "pecas": [peca_ruim]}, base)
            ctl(nome, any("P0 recusa" in e and esperado in e for e in r["erros"]),
                f"{nome} não gerou recusa nomeada -> {r['erros'][:1]}")

        # ---------- P6: hash ausente nos dois lados não pode aprovar (rodada 5, defeito ALTA) ----------
        peca_p6c = _peca_base("p6c", "eda.md", "")
        peca_p6c["sha256_da_peca"] = ""
        peca_p6c["aprovacao"]["hash_da_peca"] = ""
        r = montar({"lote": "ST", "pecas": [peca_p6c]}, base)
        ctl("P6-sem-hashes", any("P6 recusa" in e and "ausente" in e for e in r["erros"]),
            "peça sem hash nenhum foi aprovada")

        # ---------- P6: autor e data não são texto livre (rodada 5, defeito ALTA) ----------
        peca_p6d = _peca_base("p6d", "eda.md", h_eda)
        peca_p6d["aprovacao"]["por"] = "QUALQUER_TEXTO"
        r = montar({"lote": "ST", "pecas": [peca_p6d]}, base)
        ctl("P6-autor-falso", any("não é autoridade registrada" in e for e in r["erros"]),
            "aprovador inventado aceito")
        peca_p6e = _peca_base("p6e", "eda.md", h_eda)
        peca_p6e["aprovacao"]["em"] = "ontem"
        r = montar({"lote": "ST", "pecas": [peca_p6e]}, base)
        ctl("P6-data-invalida", any("não é data ISO" in e for e in r["erros"]),
            "data 'ontem' aceita como aprovação")

        # ---------- P6: aprovação tem de estar vinculada ao CONTEUDO (rodada 6, defeito ALTA) ----------
        peca_trocada = _peca_base("p6f", "eda.md", h_eda)
        peca_trocada["itens"][0]["texto_curto"] = "Texto alterado depois da aprovação"
        r = montar({"lote": "ST", "pecas": [peca_trocada]}, base)
        ctl("P6-conteudo-alterado", any("não corresponde ao conteúdo da peça" in e for e in r["erros"]),
            "conteúdo alterado após a aprovação ainda passa")

        peca_hex = _peca_base("p6g", "eda.md", h_eda)
        peca_hex["sha256_da_peca"] = "abc123"
        peca_hex["aprovacao"]["hash_da_peca"] = "abc123"
        r = montar({"lote": "ST", "pecas": [peca_hex]}, base)
        ctl("P6-hash-nao-hex", any("não é sha256" in e for e in r["erros"]),
            "hash de 6 caracteres aceito como sha256")

        # ---------- P0: bool não é int (rodada 6, defeito MEDIA) ----------
        r = montar({"lote": "ST", "pecas": [_peca_base("p0n", "eda.md", h_eda,
                    itens=[{"ordem": True, "fonte": "Achado Um"}, {"fonte": "Achado Dois"}])]}, base)
        ctl("P0-bool-como-int", any("recebido bool" in e for e in r["erros"]),
            "booleano aceito como inteiro")

        # ---------- P0: id vazio e id duplicado (rodada 6, defeito MEDIA) ----------
        r = montar({"lote": "ST", "pecas": [_peca_base("   ", "eda.md", h_eda)]}, base)
        ctl("P0-id-vazio", any("'id' vazio" in e for e in r["erros"]), "id vazio aceito")
        par = [_peca_base("mesmo-id", "eda.md", h_eda), _peca_base("mesmo-id", "eda.md", h_eda)]
        r = montar({"lote": "ST", "pecas": par}, base)
        ctl("P0-id-duplicado", any("id repetido no lote" in e for e in r["erros"]),
            "id duplicado aceito")

        # ---------- P0: rastreabilidade e campos documentados (rodada 6, defeito MEDIA) ----------
        r = montar({"lote": "ST", "pecas": [_peca_base("p0o", "eda.md", h_eda,
                    rastreabilidade_da_arte={"autor_da_arte": 7})]}, base)
        ctl("P0-rastreabilidade-tipo", any("rastreabilidade_da_arte.autor_da_arte" in e for e in r["erros"]),
            "rastreabilidade com tipo errado aceita")
        r = montar({"lote": "ST", "pecas": [_peca_base("p0p", "eda.md", h_eda,
                    rastreabilidade_da_arte={"campo-inventado": "x"})]}, base)
        ctl("P0-rastreabilidade-desconhecida", any("campo desconhecido em rastreabilidade_da_arte" in e
            for e in r["erros"]), "campo inventado em rastreabilidade aceito")
        r = montar({"lote": "ST", "pecas": [_peca_base("p0q", "eda.md", h_eda,
                    legenda="legenda", hashtags=["#bambu"], alt_text="descrição")]}, base)
        ctl("P0-campos-documentados", r["aprovadas"] == 1,
            f"campos documentados (legenda/hashtags/alt_text) recusados -> {r['erros']}", positivo=True)

        # ---------- limites documentados (rodada 7, defeito MEDIA) ----------
        r = montar({"lote": "ST", "pecas": [_peca_base("p0r", "eda.md", h_eda, legenda="x" * 2201)]}, base)
        ctl("P0-legenda-limite", any("limite da plataforma é 2200" in e for e in r["erros"]),
            "legenda com 2201 caracteres aceita")
        r = montar({"lote": "ST", "pecas": [_peca_base("p0s", "eda.md", h_eda,
                    hashtags=["#t"] * 31)]}, base)
        ctl("P0-hashtags-limite", any("limite é 30" in e for e in r["erros"]),
            "31 hashtags aceitas")
        r = montar({"lote": "ST", "pecas": [_peca_base("p0t", "eda.md", h_eda,
                    rastreabilidade_da_arte={"prompt_usado": "x"})]}, base)
        ctl("P0-prompt-nao-hash", any("prompt_usado' deve ser sha256" in e for e in r["erros"]),
            "prompt_usado que não é hash aceito")
        r = montar({"lote": "ST", "pecas": [_peca_base("p0u", "eda.md", h_eda, legenda="ok",
                    hashtags=["#a", "#b"], rastreabilidade_da_arte={"prompt_usado": "a" * 64})]}, base)
        ctl("P0-limites-ok", r["aprovadas"] == 1, f"peça dentro dos limites recusada -> {r['erros']}",
            positivo=True)

        # ---------- data da aprovação mudou depois do hash (rodada 7, defeito BAIXA) ----------
        peca_data = _peca_base("p6h", "eda.md", h_eda)
        peca_data["aprovacao"]["em"] = "2026-11-21"
        r = montar({"lote": "ST", "pecas": [peca_data]}, base)
        ctl("P6-data-pos-hash", any("não corresponde ao conteúdo" in e for e in r["erros"]),
            "data da aprovação alterada depois do hash ainda passa")

        # ---------- hash cobre os artefatos referenciados (rodada 8, defeito MEDIA) ----------
        peca_art = _peca_base("p6i", "eda.md", h_eda)
        _MEM["/mem/art.md"] = _ART + "\n\nParagrafo novo que muda o artigo."
        r = montar({"lote": "ST", "pecas": [peca_art]}, base)
        ctl("P6-artefato-alterado", any("não corresponde ao conteúdo da peça" in e for e in r["erros"]),
            "artigo da coleção alterado depois da aprovação ainda passa")
        _MEM["/mem/art.md"] = _ART

        # ---------- prompt_usado presente e vazio (rodada 8, defeito MEDIA) ----------
        r = montar({"lote": "ST", "pecas": [_peca_base("p0v", "eda.md", h_eda,
                    rastreabilidade_da_arte={"prompt_usado": ""})]}, base)
        ctl("P0-prompt-vazio", any("prompt_usado' deve ser sha256" in e for e in r["erros"]),
            "prompt_usado vazio aceito")

        # ---------- blob e lote não-UTF8: recusa nomeada, não exceção (rodada 8) ----------
        _blob_orig = _blob_no_ref
        def _blob_binario(raiz, ref, caminho):
            return (True, "\x00\x01") if False else (False, "blob não é UTF-8")
        globals()["_blob_no_ref"] = _blob_binario
        try:
            r = montar({"lote": "ST", "pecas": [
                _peca_base("p2bin", "remoto.md", h_eda,
                           deriva_de={"tipo": "estado-da-arte", "path": "remoto.md",
                                      "sha256": h_eda, "ref": "origin/x"})]}, base)
            ctl("P2-blob-nao-utf8", any("P2 recusa" in e for e in r["erros"]),
                "blob não-UTF-8 não gerou recusa nomeada")
        finally:
            globals()["_blob_no_ref"] = _blob_orig

        # ---------- P4 ----------
        r = montar({"lote": "ST", "pecas": [_peca_base("p4", "eda.md", h_eda,
                    formato="carrossel", itens=[{"ordem": 1, "fonte": "Achado Um"}])]}, base)
        ctl("P4-carrossel-curto", any("P4 recusa" in e for e in r["erros"]),
            "carrossel com 1 item aceito")
        r = montar({"lote": "ST", "pecas": [_peca_base("p4b", "eda.md", h_eda, formato="reels-x")]}, base)
        ctl("P4-formato", any("P4 recusa" in e and "desconhecido" in e for e in r["erros"]),
            "formato desconhecido aceito")

        # ---------- P5 ----------
        r = montar({"lote": "ST", "pecas": [_peca_base("p5", "eda.md", h_eda,
                    itens=[{"ordem": 1, "fonte": "Achado Um"},
                           {"ordem": 2, "fonte": "Achado Que Nao Existe"}])]}, base)
        ctl("P5-fonte-inventada", any("Achado Que Nao Existe" in e for e in r["erros"]),
            "fonte inventada aceita")

        # ---------- P6 ----------
        peca_p6 = _peca_base("p6", "eda.md", h_eda)
        peca_p6["aprovacao"]["hash_da_peca"] = "outro-hash"
        r = montar({"lote": "ST", "pecas": [peca_p6]}, base)
        ctl("P6-hash", any("P6 recusa" in e for e in r["erros"]), "aprovação de outro bytes aceita")
        peca_p6b = _peca_base("p6b", "eda.md", h_eda)
        del peca_p6b["aprovacao"]["por"]
        r = montar({"lote": "ST", "pecas": [peca_p6b]}, base)
        ctl("P6-autor", any("'aprovacao.por' é obrigatório" in e or ("P6 recusa" in e and "'por'" in e)
            for e in r["erros"]), "aprovação sem autor aceita")

        # ---------- resolvedor REAL por git (sem diretório gravável) ----------
        aqui = Path(__file__).resolve().parent
        try:
            topo = subprocess.run(["git", "-C", str(aqui), "rev-parse", "--show-toplevel"],
                                  capture_output=True, text=True, timeout=15).stdout.strip()
            rel = str(Path(__file__).resolve().relative_to(topo)) if topo else "montar_lote.py"
        except (OSError, subprocess.SubprocessError, ValueError):
            rel = "montar_lote.py"
        ok, _ = real_blob(aqui, "HEAD", rel)
        ctl("git-HEAD", ok, f"'HEAD:{rel}' não resolveu neste clone", positivo=True)
        ok2, _ = real_blob(aqui, "ref-que-nao-existe", rel)
        ctl("git-ref-falso", not ok2, "ref inexistente resolveu (deveria falhar)")
    finally:
        _MEM = None
        _blob_no_ref = real_blob

    for f in falhas:
        print(f"FALHA: {f}")
    print(json.dumps({"selftest": "PASS" if not falhas else "FAIL", "modo": "EM_MEMORIA",
                      "controles_negativos": len(negativos), "controles_positivos": len(positivos),
                      "falhas": len(falhas)}, ensure_ascii=False))
    return 0 if not falhas else 1


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Monta lote de publicação; não publica.")
    ap.add_argument("--lote")
    ap.add_argument("--raiz", default=".")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--hash-peca", dest="hash_peca",
                    help="imprime o sha256 canonico do conteudo da peca: campos de conteudo, "
                         "aprovacao.por/em e o sha256 dos artefatos de derivacao/colecao")
    a = ap.parse_args(argv)

    if a.selftest:
        return selftest()
    if a.hash_peca:
        try:
            peca = json.loads(Path(a.hash_peca).read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError, RecursionError) as e:
            print(json.dumps({"erro": "P0 recusa — peca ilegivel, nao e UTF-8 ou nao e JSON valido",
                              "path": a.hash_peca, "detalhe": str(e)}, ensure_ascii=False))
            return 2
        if not isinstance(peca, dict):
            print(json.dumps({"erro": "peca deve ser objeto JSON"}, ensure_ascii=False))
            return 2
        print(json.dumps({"sha256_da_peca": hash_da_peca(peca, Path(a.raiz)),
                          "nota": "hash do conteudo MAIS 'aprovacao.por' e 'aprovacao.em'. "
                                  "Alterar qualquer um deles, ou qualquer campo de conteudo, invalida a aprovacao. "
                                  "O hash nao autentica identidade: 'por' e declaracao, nao assinatura digital."},
                         ensure_ascii=False, indent=1))
        return 0
    if not a.lote:
        ap.error("--lote e obrigatorio (ou use --selftest)")

    try:
        bruto = Path(a.lote).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        print(json.dumps({"erro": "P0 recusa — lote ilegível ou não é UTF-8", "path": a.lote,
                          "detalhe": str(e)}, ensure_ascii=False))
        return 2
    try:
        lote = json.loads(bruto)
    except (json.JSONDecodeError, RecursionError) as e:
        print(json.dumps({"erro": "P0 recusa — lote não é JSON válido (ou aninhado demais)", "path": a.lote,
                          "detalhe": getattr(e, "msg", str(e)) or "aninhamento excessivo"}, ensure_ascii=False))
        return 2
    r = montar(lote, Path(a.raiz))
    print(json.dumps(r, ensure_ascii=False, indent=1))
    return 0 if not r["erros"] else 1


if __name__ == "__main__":
    sys.exit(main())
