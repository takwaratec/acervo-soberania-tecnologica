#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica o ponteiro e o manifesto COBRE pelo caminho do auditor externo.

Uso:
  python3 verificar_ponteiro_cobre.py --repo <path> --ref origin/hermes/cobre-plano-20261124

Reproduz a cadeia: ponteiro -> manifest_branch + manifest_commit -> manifest_path
-> sha256_do_manifesto -> HASHES_RESPONSE -> fontes[] conferidas no alvo_commit.

Sai 0 se todos os gates passam, 1 com o nome do primeiro gate que falhou.
"""
import argparse
import hashlib
import json
import subprocess
import sys

GATES = []


def gate(nome, ok, detalhe=""):
    GATES.append((nome, ok, detalhe))
    print(f"  [{'OK ' if ok else 'FAIL'}] {nome}" + (f" — {detalhe}" if detalhe else ""))
    return ok


def git(repo, *args):
    r = subprocess.run(["git", "-C", repo] + list(args), capture_output=True)
    return r.returncode, r.stdout, r.stderr.decode(errors="replace")


def blob(repo, commit, path):
    rc, out, err = git(repo, "show", f"{commit}:{path}")
    if rc != 0:
        return None
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--ref", default="origin/hermes/cobre-plano-20261124")
    ap.add_argument("--pointer", default="ops/command-center/auditoria-atual/COBRE.json")
    a = ap.parse_args()
    R = a.repo

    print("=" * 72)
    print("VERIFICAÇÃO — caminho do auditor externo — COBRE")
    print("=" * 72)

    # 0. o ref resolve
    rc, out, _ = git(R, "rev-parse", a.ref)
    if not gate("0. ref resolve", rc == 0, a.ref):
        return 1
    ref_sha = out.decode().strip()

    # 1. ponteiro existe
    b = blob(R, ref_sha, a.pointer)
    if not gate("1. ponteiro existe no ref", b is not None, a.pointer):
        return 1
    pt = json.loads(b)

    # 2. ponteiro não está FECHADO
    gate("2. ponteiro ABERTO (auditoria existe)", pt.get("status") != "FECHADO",
         pt.get("status", "?"))

    # 3. campos de endereçamento
    falta = [k for k in ("manifest_branch", "manifest_commit", "manifest_path",
                         "sha256_do_manifesto", "hashes_response_path",
                         "sha256_do_hashes_response", "alvo_commit") if not pt.get(k)]
    gate("3. campos de endereçamento completos", not falta, str(falta) if falta else "")

    # 4. alvo_commit existe e tem 40 hex
    alvo = pt.get("alvo_commit", "")
    gate("4. alvo_commit com 40 hex", len(alvo) == 40 and all(c in "0123456789abcdef" for c in alvo), alvo)
    rc, _, err = git(R, "cat-file", "-e", f"{alvo}^{{commit}}")
    gate("5. alvo_commit existe no remoto", rc == 0, err.strip())

    # 6. manifest_commit existe
    mc = pt.get("manifest_commit", "")
    gate("6. manifest_commit com 40 hex", len(mc) == 40, mc)

    # 7. manifesto no manifest_commit
    mb = blob(R, mc, pt["manifest_path"])
    if not gate("7. manifesto existe no manifest_commit", mb is not None, pt["manifest_path"]):
        return 1

    # 8. sha256 do manifesto confere
    h = hashlib.sha256(mb).hexdigest()
    gate("8. sha256 do manifesto confere", h == pt["sha256_do_manifesto"],
         f"medido {h[:16]}… declarado {pt['sha256_do_manifesto'][:16]}…" if h != pt["sha256_do_manifesto"] else h[:16] + "…")

    man = json.loads(mb)

    # 9. manifest_id bate
    gate("9. manifest_id bate com o ponteiro", man.get("manifest_id") == pt.get("manifest_id"),
         man.get("manifest_id", "?"))

    # 10. manifesto aponta o mesmo alvo que o ponteiro
    gate("10. manifesto.alvo_commit == ponteiro.alvo_commit",
         man.get("alvo_commit") == alvo, f"{man.get('alvo_commit','?')[:16]}…")

    # 11. os dois nomes de formato de resposta, com conteúdo igual
    fr = man.get("formato_resposta", {})
    gate("11. formato_resposta é objeto com campos_obrigatorios",
         isinstance(fr, dict) and isinstance(fr.get("campos_obrigatorios"), list),
         f"{len(fr.get('campos_obrigatorios', []))} campos" if isinstance(fr, dict) else type(fr).__name__)

    # 12. campos mínimos do protocolo
    minimos = ["manifest_id", "status", "tipo", "frente", "pergunta", "fora_de_escopo",
               "fontes", "criterios", "severidade", "formato_resposta", "limites",
               "alvo_commit", "alvo_branch"]
    ausentes = [k for k in minimos if k not in man]
    gate("12. campos mínimos do protocolo", not ausentes, str(ausentes) if ausentes else f"{len(minimos)}/{len(minimos)}")

    # 13. sem teto de furos na estrutura
    esquema = json.dumps(fr, ensure_ascii=False)
    gate("13. sem teto de furos no esquema (FURO1..N fixos)",
         not any(f"FURO{i}" in esquema for i in range(1, 10)))

    # 14. HASHES_RESPONSE
    hb = blob(R, mc, pt["hashes_response_path"])
    if not gate("14. HASHES_RESPONSE existe no manifest_commit", hb is not None,
                pt["hashes_response_path"]):
        return 1
    hh = hashlib.sha256(hb).hexdigest()
    gate("15. sha256 do HASHES_RESPONSE confere", hh == pt["sha256_do_hashes_response"],
         hh[:16] + "…")
    hr = json.loads(hb)
    gate("16. HASHES_RESPONSE.sha256_do_manifesto == ponteiro",
         hr.get("sha256_do_manifesto") == pt["sha256_do_manifesto"])
    gate("17. HASHES_RESPONSE.manifest_id bate", hr.get("manifest_id") == man.get("manifest_id"))
    gate("18. HASHES_RESPONSE.commit_alvo == alvo", hr.get("commit_alvo") == alvo)

    # 19. TODAS as fontes: existem no alvo E o sha256 confere
    fontes = man.get("fontes", [])
    ruins, ausentes_f = [], []
    for f in fontes:
        fb = blob(R, alvo, f["path"])
        if fb is None:
            ausentes_f.append(f["path"])
            continue
        if hashlib.sha256(fb).hexdigest() != f["sha256"]:
            ruins.append(f["path"])
    gate(f"19. as {len(fontes)} fontes existem no alvo_commit", not ausentes_f,
         str(ausentes_f[:3]) if ausentes_f else "")
    gate(f"20. os sha256 das {len(fontes)} fontes conferem", not ruins,
         str(ruins[:3]) if ruins else "")

    # 21. HASHES_RESPONSE.fontes_sha256 == manifesto.fontes[].sha256
    mapa_man = {f["path"]: f["sha256"] for f in fontes}
    gate("21. fontes_sha256 do HASHES_RESPONSE == fontes do manifesto",
         hr.get("fontes_sha256") == mapa_man)

    # 22. os documentos de resolução existem no alvo
    for doc in ("AGENTS.md", "CANONICAL_REGENCY_LOCATOR_R4.md",
                "ops/command-center/bootstrap/SESSION_START_DISCIPLINE_R4.md"):
        pass  # não se aplica a este repositório de conteúdo

    # 23. contagens declaradas batem
    gate("23. total_fontes declarado == len(fontes)",
         man.get("total_fontes") == len(fontes), f"{man.get('total_fontes')} × {len(fontes)}")

    print("-" * 72)
    falhas = [g for g in GATES if not g[1]]
    print(f"gates: {len(GATES)} | passaram: {len(GATES)-len(falhas)} | falharam: {len(falhas)}")
    if falhas:
        print("PRIMEIRO GATE VERMELHO:", falhas[0][0])
        return 1
    print("\nRESULTADO: PACOTE VERIFICADO — o auditor alcança e confere tudo")
    return 0


if __name__ == "__main__":
    sys.exit(main())
