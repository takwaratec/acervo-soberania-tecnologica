#!/usr/bin/env python3
"""Gate A7 (AGENTS_LOCAL.md § Conferência de afirmação).

Mede o diff de uma branch de frente contra uma base e recusa quando há arquivo fora da gaveta
declarada — em especial DELECAO (branch atrasada apaga trabalho alheio) e MODIFICACAO fora da
gaveta (regressao de conteudo de outra frente).

Não abre PR, não decide conteudo: mede escopo.

Uso:
    python3 scripts/check_escopo_do_diff.py --base origin/main --permitir docs/analises/x --permitir scripts/
    python3 scripts/check_escopo_do_diff.py --base origin/main --permitir docs/analyses/cobre --json
"""
import argparse
import json
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


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="origin/main")
    ap.add_argument("--ref", default="HEAD")
    ap.add_argument("--permitir", action="append", default=[],
                    help="caminho ou prefixo permitido (repetível)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)

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
        "total_no_diff": total, "fora_do_escopo": len(fora),
        "dentro_do_escopo": total - len(fora),
        "delecoes": deles,
        "fora": fora,
        "veredito": "PASS" if not fora else "FAIL",
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
