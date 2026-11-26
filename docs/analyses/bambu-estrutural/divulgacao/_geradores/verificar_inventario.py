#!/usr/bin/env python3
"""Verifica o inventário do pacote Sol contra o próprio git — sem confiar no disco.

Regras que este verificador obedece:

1. O inventário é lido DO COMMIT (`git show`), nunca do disco. Um inventário que se verifica
   lendo a si mesmo não prova nada.
2. Cada caminho é resolvido por `git cat-file blob` no commit declarado no campo `commit` do
   inventário, com fallback para o HEAD quando o caminho não existe lá.
3. Os `removidos` são conferidos ao contrário: cada um tem de continuar INEXISTENTE no commit
   declarado, e o commit que o removeu tem de ser alcançável a partir daqui.
4. Falha em alcançar um repositório remoto produz NAO_VERIFICADO — nunca AUSENTE. "Não consegui
   olhar" e "não está lá" são fatos diferentes, e confundi-los é como se perde custódia.
5. O sha256 sai dos bytes crus do blob (`git cat-file blob`), sem strip, sem decodificação.

Uso:
  python3 verificar_inventario.py --conferir
  python3 verificar_inventario.py --conferir --commit <sha>
  python3 verificar_inventario.py --json

Saída: uma linha PASS: N quando tudo confere; DISCREPANCIA listando arquivo e motivo quando não.
Exit: 0 tudo confere · 1 há divergência ou ausente · 2 nada pôde ser verificado.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys

REL_INV = "docs/analyses/bambu-estrutural/divulgacao/_geradores/INVENTARIO_PACOTE_SOL.json"


def git(repo: str, *args: str, texto: bool = False):
    r = subprocess.run(["git", "-C", repo, *args], capture_output=True)
    if texto:
        return r.stdout.decode("utf-8", "replace") if r.returncode == 0 else None
    return r.stdout if r.returncode == 0 else None


def blob(repo: str, commit: str, path: str) -> bytes | None:
    dados = git(repo, "cat-file", "blob", f"{commit}:{path}")
    return dados if isinstance(dados, bytes) else None


def existe(repo: str, commit: str, path: str) -> bool:
    return subprocess.run(["git", "-C", repo, "cat-file", "-e", f"{commit}:{path}"],
                          capture_output=True).returncode == 0


def commit_existe(repo: str, sha: str) -> bool:
    return subprocess.run(["git", "-C", repo, "cat-file", "-e", f"{sha}^{{commit}}"],
                          capture_output=True).returncode == 0


def remoto_alcancavel(repo: str) -> bool:
    """Tenta falar com o remoto. Falha de rede vira NAO_VERIFICADO, não AUSENTE."""
    r = subprocess.run(["git", "-C", repo, "ls-remote", "--exit-code", "origin", "HEAD"],
                       capture_output=True, timeout=30)
    return r.returncode == 0


def ler_inventario(repo: str, commit: str) -> tuple[dict | None, str]:
    txt = git(repo, "show", f"{commit}:{REL_INV}", texto=True)
    if txt is None:
        return None, "inventario nao existe nesse commit"
    try:
        return json.loads(txt), ""
    except json.JSONDecodeError as e:
        return None, f"inventario ilegivel: {e}"


def verificar(repo: str, commit: str, disco: bool = False) -> dict:
    inv, erro = ler_inventario(repo, commit)
    if inv is None:
        return {"veredito": "AUSENTE", "motivo": erro, "itens": []}

    declarado = inv.get("commit") or commit
    itens, ok, divergentes, ausentes, nao_verif = [], 0, 0, 0, 0

    for a in inv.get("arquivos", []):
        caminho, esperado = a["caminho"], a["sha256"]
        dados = blob(repo, declarado, caminho)
        origem = declarado
        if dados is None:                      # fallback previsto na regra 2
            dados = blob(repo, commit, caminho)
            origem = commit
        if dados is None:
            if not remoto_alcancavel(repo):
                nao_verif += 1
                itens.append({"caminho": caminho, "veredito": "NAO_VERIFICADO",
                              "motivo": "objeto ausente local e remoto inalcancavel"})
            else:
                ausentes += 1
                itens.append({"caminho": caminho, "veredito": "AUSENTE",
                              "motivo": f"nao existe em {declarado[:8]} nem em {commit[:8]}"})
            continue
        obtido = hashlib.sha256(dados).hexdigest()
        if disco:
            no_disco = os.path.join(repo, caminho)
            if os.path.exists(no_disco):
                with open(no_disco, "rb") as fh:
                    cru = fh.read()
                if hashlib.sha256(cru).hexdigest() != esperado:
                    divergentes += 1
                    itens.append({"caminho": caminho, "veredito": "DIVERGE", "origem": "disco",
                                  "motivo": "o arquivo no disco nao tem os bytes do inventario",
                                  "esperado": esperado, "obtido": hashlib.sha256(cru).hexdigest()})
                    continue
        if obtido == esperado and len(dados) == a.get("bytes", len(dados)):
            ok += 1
            itens.append({"caminho": caminho, "veredito": "OK", "origem": origem[:8]})
        else:
            divergentes += 1
            itens.append({"caminho": caminho, "veredito": "DIVERGE", "origem": origem[:8],
                          "esperado": esperado, "obtido": obtido,
                          "bytes_esperado": a.get("bytes"), "bytes_obtido": len(dados)})

    # conferência ao contrário: o removido tem de continuar inexistente
    for r in inv.get("removidos", []):
        caminho = r["caminho"]
        if existe(repo, declarado, caminho):
            divergentes += 1
            itens.append({"caminho": caminho, "veredito": "DIVERGE",
                          "motivo": "declarado removido, mas existe no commit descrito"})
            continue
        if disco and os.path.exists(os.path.join(repo, caminho)):
            divergentes += 1
            itens.append({"caminho": caminho, "veredito": "DIVERGE",
                          "motivo": "declarado removido, mas reapareceu no disco"})
            continue
        sha_remocao = (r.get("motivo") or "").split(" ")[0]
        if sha_remocao and not commit_existe(repo, sha_remocao):
            nao_verif += 1
            itens.append({"caminho": caminho, "veredito": "NAO_VERIFICADO",
                          "motivo": f"commit da remocao {sha_remocao} nao alcancavel"})
            continue
        ok += 1
        itens.append({"caminho": caminho, "veredito": "OK",
                      "motivo": f"continua ausente; remocao em {sha_remocao}"})

    if divergentes or ausentes:
        veredito = "FALHA"
    elif nao_verif:
        veredito = "NAO_VERIFICADO"
    else:
        veredito = "PASS"
    removidos_ok = sum(1 for it in itens if it["veredito"] == "OK" and "continua ausente" in (it.get("motivo") or ""))
    return {"veredito": veredito, "commit": commit, "descreve": declarado,
            "arvore": inv.get("arvore"), "ok": ok, "removidos_ok": removidos_ok,
            "arquivos_ok": ok - removidos_ok, "divergentes": divergentes,
            "ausentes": ausentes, "nao_verificado": nao_verif, "itens": itens}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    ap.add_argument("--commit", default="HEAD")
    ap.add_argument("--conferir", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if not os.path.isdir(os.path.join(a.repo, ".git")) and git(a.repo, "rev-parse", "--git-dir") is None:
        print("NAO_VERIFICADO: nao e um repositorio git")
        return 2

    sha_ref = git(a.repo, "rev-parse", a.commit, texto=True)
    if not isinstance(sha_ref, str) or not sha_ref.strip():
        print(f"NAO_VERIFICADO: commit {a.commit} nao alcancavel")
        return 2
    sha = sha_ref.strip()

    head = (git(a.repo, "rev-parse", "HEAD", texto=True) or "").strip()
    r = verificar(a.repo, sha, disco=(sha == head))

    if a.json:
        print(json.dumps(r, ensure_ascii=False, indent=1))
    else:
        print(f"commit:   {sha[:8]}")
        print(f"descreve: {str(r.get('descreve'))[:8]}  arvore: {str(r.get('arvore'))[:8]}")
        if r["veredito"] == "AUSENTE":
            print(f"NAO_VERIFICADO: {r['motivo']}")
            return 2
        for it in r["itens"]:
            if it["veredito"] != "OK":
                extra = it.get("motivo") or f"esperado {it.get('esperado','')[:12]} obtido {it.get('obtido','')[:12]}"
                print(f"  {it['veredito']:<15} {it['caminho']} — {extra}")
        if r["veredito"] == "PASS":
            print(f"PASS: {r['ok']}  ({r['ok'] - r.get('removidos_ok', 0)} arquivos + "
                  f"{r.get('removidos_ok', 0)} removidos)")
        elif r["veredito"] == "NAO_VERIFICADO":
            print(f"NAO_VERIFICADO: {r['nao_verificado']} itens sem alcance; ok: {r['ok']}")
        else:
            print(f"DISCREPANCIA: {r['divergentes']} divergentes, {r['ausentes']} ausentes; ok: {r['ok']}")

    return {"PASS": 0, "NAO_VERIFICADO": 2}.get(r["veredito"], 1)


if __name__ == "__main__":
    sys.exit(main())
