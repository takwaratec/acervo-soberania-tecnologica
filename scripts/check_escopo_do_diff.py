#!/usr/bin/env python3
"""Gate A7 (AGENTS_LOCAL.md § Conferência de afirmação).

Mede o diff de uma branch de frente contra uma base e recusa quando há arquivo fora da gaveta
declarada — em especial DELECAO (branch atrasada apaga trabalho alheio) e MODIFICACAO fora da
gaveta (regressao de conteudo de outra frente).

Não abre PR, não decide conteudo: mede escopo.

Uso:
    python3 scripts/check_escopo_do_diff.py --base origin/main --permitir docs/analises/x --permitir scripts/
    python3 scripts/check_escopo_do_diff.py --base origin/main --permitir docs/analyses/cobre --json
    python3 scripts/check_escopo_do_diff.py --base origin/main --frente BAMBU-SCIENCE --registro ../r4-claims/frentes_abertas
"""
import argparse
import glob
import hashlib
import json
import os
import subprocess
import sys


class MedicaoFalhou(RuntimeError):
    """O instrumento não conseguiu medir. É diferente de 'medido e reprovado'."""


def git(*args):
    r = subprocess.run(["git", *args], capture_output=True, text=True)
    if r.returncode != 0:
        raise MedicaoFalhou(f"git {' '.join(args)} -> exit {r.returncode}: {r.stderr.strip()[:200]}")
    return r.stdout


def diff_status(base, ref="HEAD"):
    saida = git("diff", "--name-status", f"{base}...{ref}", "--")
    itens = []
    for linha in saida.splitlines():
        if not linha.strip():
            continue
        partes = linha.split("\t")
        itens.append({"status": partes[0], "paths": [p for p in partes[1:] if p]})
    return itens


def dentro(caminho, prefixos):
    return any(caminho == p.rstrip("/") or caminho.startswith(p.rstrip("/") + "/") for p in prefixos)


def _prefixo(escopo):
    """`docs/analyses/bambu-estrutural/**` -> `docs/analyses/bambu-estrutural`."""
    return escopo.rstrip("/").removesuffix("/**").rstrip("/")


def escopo_do_registro(registro_dir, frente):
    """Lê `write_scope` da frente no registro vivo (A9.1/A9.2).

    Devolve (escopos, aberta_das_outras). Levanta MedicaoFalhou quando não consegue ler — registro que
    não abre é NÃO MEDIDO, nunca PASS.

    Se o diretório traz `MANIFESTO.json` (cópia derivada do ref `r4-claims`, usada quando o repositório de
    governança é privado e o CI não o alcança), o manifesto é conferido ANTES de usar: hash por arquivo e
    o `origem_commit` declarado. Divergência é NÃO MEDIDO — cópia que não confere com o manifesto não é
    registro, é boato.
    """
    man_path = os.path.join(registro_dir, "MANIFESTO.json")
    if os.path.isfile(man_path):
        try:
            with open(man_path, encoding="utf-8") as fh:
                man = json.load(fh)
        except Exception as e:
            raise MedicaoFalhou(f"MANIFESTO.json do registro ilegível: {e}")
        for nome, meta in (man.get("arquivos") or {}).items():
            p = os.path.join(registro_dir, nome)
            if not os.path.isfile(p):
                raise MedicaoFalhou(f"registro derivado não tem '{nome}', que o manifesto declara")
            h = hashlib.sha256(open(p, "rb").read()).hexdigest()
            if h != meta.get("sha256"):
                raise MedicaoFalhou(
                    f"'{nome}' divergiu do manifesto ({h[:12]} != {str(meta.get('sha256'))[:12]}) — "
                    f"cópia derivada de r4-claims@{str(man.get('origem_commit'))[:8]} está suja; "
                    f"resincronize antes de medir")
    alvo = os.path.join(registro_dir, f"{frente}.json")
    if not os.path.isfile(alvo):
        raise MedicaoFalhou(f"registro da frente '{frente}' não encontrado em {alvo}")
    try:
        with open(alvo, encoding="utf-8") as fh:
            reg = json.load(fh)
    except Exception as e:
        raise MedicaoFalhou(f"registro de '{frente}' ilegível: {e}")
    escopos = [_prefixo(e) for e in (reg.get("write_scope") or []) if isinstance(e, str) and e.strip()]
    if not escopos:
        raise MedicaoFalhou(f"frente '{frente}' não declara write_scope: sem gaveta não há escopo")
    outros = {}
    for p in glob.glob(os.path.join(registro_dir, "*.json")):
        nome = os.path.splitext(os.path.basename(p))[0]
        if nome == frente:
            continue
        try:
            with open(p, encoding="utf-8") as fh:
                r = json.load(fh)
        except Exception:
            continue
        if str(r.get("estado", "")).upper() == "CANCELADA":
            continue
        outros[nome] = [_prefixo(e) for e in (r.get("write_scope") or []) if isinstance(e, str) and e.strip()]
    return escopos, outros


def contem(outro, proprio):
    """`proprio` contém `outro`? (A9.2 — escopo de uma frente não pode englobar o de outra.)"""
    return outro == proprio or outro.startswith(proprio + "/")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="origin/main")
    ap.add_argument("--ref", default="HEAD")
    ap.add_argument("--permitir", action="append", default=[],
                    help="caminho ou prefixo permitido (repetível)")
    ap.add_argument("--frente", help="nome da frente no registro vivo; a gaveta vem do write_scope dela")
    ap.add_argument("--registro", help="diretório com frentes_abertas/<FRENTE>.json (ref r4-claims)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)

    outros = {}
    colisoes = []
    if a.frente:
        if not a.registro:
            print(f"NAO_MEDIDO frente '{a.frente}' declarada sem --registro: a gaveta tem de vir do "
                  f"registro vivo, não de lista digitada (A9).")
            return 2
        try:
            a.permitir, outros = escopo_do_registro(a.registro, a.frente)
        except MedicaoFalhou as e:
            print(f"NAO_MEDIDO {e}")
            return 2
        # A9.2: escopo que contém — ou repete — o de outra frente aberta é recusa, não alerta.
        for nome, escopos in sorted(outros.items()):
            for proprio in a.permitir:
                for escopo in escopos:
                    if contem(escopo, proprio):
                        tipo = "idêntico a" if escopo == proprio else "contém"
                        colisoes.append({"frente": nome, "tipo": tipo, "escopo": escopo})
        if colisoes:
            for c in colisoes:
                verbo = "é idêntico ao" if c["tipo"] == "idêntico a" else "contém o"
                print(f"FAIL A9.2 — o escopo '{c['escopo']}' de '{c['frente']}' {verbo} declarado por "
                      f"'{a.frente}'. Sobreposição é recusa: o caminho pertence a quem o abriu, e a "
                      f"outra frente pede emenda — não herda.")
            print("     a medição segue abaixo: o número existe junto do motivo, não no lugar dele.")
            print("     escopo declarado: " + str(a.permitir))

    if not a.permitir:
        print("FAIL sem --permitir: sem gaveta declarada não há escopo, e sem escopo não há medição")
        return 2
    if not a.base or a.base.rstrip("/") in ("origin", "origin/"):
        print(f"NAO_MEDIDO base declarada e vazia ('{a.base}'): sem base não há diff, e sem diff não há "
              f"escopo medido. Em push, passe --base <sha> ou --base origin/main.")
        return 2

    # Base não resolvível (shallow clone, ref não buscada) é o erro mais comum no CI: diga o que fazer.
    try:
        base_sha = git("rev-parse", "--verify", f"{a.base}^{{commit}}").strip()
    except MedicaoFalhou:
        print(f"NAO_MEDIDO base '{a.base}' não existe neste clone. No CI, o checkout precisa de "
              f"fetch-depth: 0 e da ref da base buscada (git fetch origin {a.base}).")
        return 2

    try:
        itens = diff_status(base_sha, a.ref)
    except MedicaoFalhou as e:
        print(f"NAO_MEDIDO o instrumento não conseguiu ler o diff: {e}")
        return 2
    fora, deles, total = [], [], 0
    for it in itens:
        for p in it["paths"]:
            total += 1
            if it["status"].startswith("D"):
                deles.append({"status": it["status"], "path": p, "origem": p})
            if not dentro(p, a.permitir):
                fora.append({"status": it["status"], "path": p})

    resultado = {
        "base": a.base, "base_sha": base_sha[:12], "ref": a.ref, "permitido": a.permitir,
        "frente": a.frente, "colisoes_de_escopo": colisoes,
        "total_no_diff": total, "fora_do_escopo": len(fora),
        "dentro_do_escopo": total - len(fora),
        "delecoes": deles,
        "fora": fora,
        "veredito": "PASS" if not fora and not colisoes else "FAIL",
    }
    if a.json:
        print(json.dumps(resultado, ensure_ascii=False, indent=2))
    else:
        print(f"BASE={a.base} BASE_SHA={base_sha[:12]} REF={a.ref}")
        print("Nota: o escopo medido vale para esta base. Se a base andar, remeça antes de mergear — "
              "PR medida contra uma main antiga acusa deleção de trabalho que já entrou.")
        print(f"TOTAL_NO_DIFF={total} DENTRO={resultado['dentro_do_escopo']} FORA={len(fora)}")
        for d in deles:
            print(f"  DELECAO {d['path']} — branch atrasada apaga trabalho alheio? confirme")
        for f in fora:
            print(f"  FORA {f['status']} {f['path']}")
        print(f"VEREDITO={resultado['veredito']}")
    return 0 if resultado["veredito"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
