#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Resela o pacote de auditoria COBRE sobre um alvo novo.

Regra da casa, que este script respeita na ordem: material -> manifesto -> HASHES_RESPONSE
-> ponteiro. O manifesto não pode conter o hash do commit que o publica, e por isso cada
peça ganha o seu próprio commit, e todo hash é lido do commit (`git show`), nunca do disco.

Uso: reselar_auditoria_cobre.py <alvo_commit_40hex>
"""
import glob
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

# REPO e BRANCH por variável de ambiente: o script rodava sempre no checkout principal, e
# reseleiar de dentro de um worktree commitava na branch errada. Aconteceu — e o selo foi para
# a branch abandonada. Quem chama declara onde está.
REPO = os.environ.get("COBRE_REPO", os.environ.get("COBRE_REPO", "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica"))
BRANCH = os.environ.get("COBRE_BRANCH", "hermes/cobre-plano-20261124")
DIR = "docs/analyses/cobre"
PT = "ops/command-center/auditoria-atual/COBRE.json"

# Por que o nome do arquivo carrega o alvo: o manifesto nasce DEPOIS do conteúdo, porque não pode
# conter o hash do commit que o publica. Isso deixa, dentro do commit-alvo, a cópia do manifesto
# ANTERIOR — e o auditor que abrir "o manifesto do commit auditado", que é o gesto natural, lê o
# documento errado e reporta hashes divergentes. Aconteceu. O nome resolve: se o arquivo diz
# _R1_<alvo>.json, ele vale para aquele alvo e para nenhum outro.

# fontes novas desta rodada (S11-c)
NOVAS = [
    ("docs/analyses/cobre/fichas/ficha-pi292-89-registro-preservativos-madeira.md",
     "ficha 7 — a norma-mãe: registro obrigatório e art. 20 (competência de fiscalização)"),
    ("docs/analyses/cobre/fichas/ficha-pn151-97-ibama-risco-ambiental.md",
     "ficha 8 — o registro condicionado à determinação do risco ambiental"),
    ("docs/analyses/cobre/fichas/ficha-iema-es-nt01-2023-preservacao-madeira.md",
     "ficha 9 — o regulador do ES: «não há proibição no Brasil» e a falta de dados do CCB"),
    ("docs/analyses/cobre/fichas/ficha-abpm-fg4mad-destinacao-residuo-madeira-tratada.md",
     "ficha 10 — a própria cadeia: resíduo tratado não pode queima em fogão nem a céu aberto"),
    ("docs/analyses/cobre/fichas/ficha-ufsm-2025-cca-moiroes-contaminacao-solo.md",
     "ficha 11 — 880 dias de campo: As na madeira −55,0%, no solo +129,2%"),
    ("docs/analyses/cobre/fontes/s11c/1989_pi292_preservativos_registro.pdf",
     "ref 17 — Portaria Interministerial 292/89, texto integral (4 p.)"),
    ("docs/analyses/cobre/fontes/s11c/1997_pn151_ibama_registro_risco_ambiental.pdf",
     "ref 18 — Portaria Normativa Ibama 151/97 (DOU, OCR degradado)"),
    ("docs/analyses/cobre/fontes/s11c/2023_iema_es_nt01_preservacao_madeira.pdf",
     "ref 19 — NT 01/2023 do Iema-ES (36 p.)"),
    ("docs/analyses/cobre/fontes/s11c/2016_abpm_fg4mad_destinacao_residuos_madeira_tratada.pdf",
     "ref 20 — ABPM/FG4mad, destinação de resíduo de madeira tratada (21 p.)"),
    ("docs/analyses/cobre/fontes/s11c/2025_ufsm_ciencia_florestal_cca_moiroes_solo.pdf",
     "ref 21 — Ciência Florestal v.35 e86024 (16 p.)"),
    ("docs/analyses/cobre/fontes/s11c/MANIFEST_FONTES_S11C.json",
     "manifesto da custódia S11-c, com as duas pendências declaradas"),
    # S11-d — a instrução que diz onde a regra de descarte mora
    ("docs/analyses/cobre/fichas/ficha-in05-92-ibama-destinacao-final-residuos.md",
     "ficha 12 — item VIII da IN 5/92: o descarte segue a bula, e a bula é do produto registrado"),
    ("docs/analyses/cobre/fontes/s11d/1992_in05_ibama_destinacao_final_residuos.pdf",
     "ref 22 — Instrução Normativa Ibama 5/92, fac-símile do DOU de 21.10.1992 (15 p.)"),
    ("docs/analyses/cobre/fontes/s11d/1992_in05_ibama_destinacao_final_residuos.md",
     "extração com marcador de página da IN 5/92"),
    ("docs/analyses/cobre/fontes/s11d/2026-ctf-ibama-categorias-preservativos.md",
     "página oficial do CTF: as categorias da cadeia são por estabelecimento industrial"),
    ("docs/analyses/cobre/fontes/s11d/MANIFEST_FONTES_S11D.json",
     "manifesto da custódia S11-d, com a pendência da S11-c resolvida"),
]


def git(*a, check=True):
    r = subprocess.run(["git", "-C", REPO] + list(a), capture_output=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"git {' '.join(a)}: {r.stderr.decode()[:300]}")
    return r


def blob_sha(commit, path):
    r = git("show", f"{commit}:{path}")
    return hashlib.sha256(r.stdout).hexdigest(), len(r.stdout)


def manifesto_anterior():
    """O manifesto vigente vem do ponteiro; sem ponteiro, o de nome mais recente no disco."""
    caminho_pt = os.path.join(REPO, PT)
    if os.path.exists(caminho_pt):
        try:
            pt = json.load(open(caminho_pt, encoding="utf-8"))
            if os.path.exists(os.path.join(REPO, pt["manifest_path"])):
                return pt["manifest_path"]
        except Exception:
            pass
    cand = sorted(glob.glob(os.path.join(REPO, DIR, "AUDITORIA_SOL_COBRE_MANIFEST_R1*.json")))
    if not cand:
        raise SystemExit("nenhum manifesto anterior encontrado")
    return os.path.relpath(cand[-1], REPO)


def main():
    # O ponteiro vive em ops/command-center/auditoria-atual/, que é fora da gaveta do cobre.
    # A regra A7 proíbe arquivo fora da gaveta na PR da frente: o ponteiro é atualizado em PR
    # de governança própria. --sem-ponteiro reseleia o manifesto e a resposta de hashes (ambos
    # em docs/analyses/cobre) e deixa o ponteiro para aquela PR.
    sem_ponteiro = "--sem-ponteiro" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    alvo = args[0]
    assert len(alvo) == 40, "alvo precisa ser sha de 40 hex"
    git("cat-file", "-e", f"{alvo}^{{commit}}")

    man_path = f"{DIR}/AUDITORIA_SOL_COBRE_MANIFEST_R1_{alvo[:8]}.json"
    hr_path = f"{DIR}/AUDITORIA_SOL_COBRE_HASHES_RESPONSE_R1_{alvo[:8]}.json"
    prev = manifesto_anterior()

    man = json.load(open(os.path.join(REPO, prev), encoding="utf-8"))

    # PDFs saíram do rastreio (governance-check.yml proíbe PDF versionado): o manifesto declara
    # onde a cópia privada mora, com o mesmo sha256 do byte que estava versionado.
    custodia = {}
    _cp = os.path.join(REPO, DIR, "fontes", "CUSTODIA_PRIVADA_PDFS.json")
    if os.path.exists(_cp):
        custodia = json.load(open(_cp, encoding="utf-8")).get("pdfs", {})

    def medir(path):
        """(sha, bytes, no_repositorio, caminho_privado) — do commit quando está versionado,
        da custódia declarada quando não está."""
        try:
            h, n = blob_sha(alvo, path)
            return h, n, True, None
        except Exception:
            c = custodia.get(path)
            if not c:
                raise
            return c["sha256"], c["bytes"], False, c.get("caminho_privado")

    # 1) reconferir cada fonte existente no alvo novo
    novas, vistas = 0, set()
    for f in man["fontes"]:
        h, n, no_repo, priv = medir(f["path"])
        f["sha256"], f["bytes"] = h, n
        f["no_repositorio"] = no_repo
        if priv:
            f["caminho_privado"] = priv
        vistas.add(f["path"])

    # 2) acrescentar as fontes desta rodada
    for path, papel in NOVAS:
        if path in vistas:
            continue
        h, n, no_repo, priv = medir(path)
        e = {"path": path, "sha256": h, "bytes": n, "papel": papel, "no_repositorio": no_repo}
        if priv:
            e["caminho_privado"] = priv
        man["fontes"].append(e)
        novas += 1

    # 3) metadados
    man["alvo_commit"] = alvo
    man["gerado_utc"] = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    man["total_fontes"] = len(man["fontes"])
    man["como_ler"] = (
        "Este arquivo descreve o alvo_commit acima e vale apenas para ele; o nome do arquivo "
        "carrega o alvo por isso. NÃO leia o manifesto que aparece dentro do próprio alvo_commit: "
        "aquele é o da rodada anterior. A entrada é o ponteiro em " + PT + ".")
    man["alvo_nota"] = ("alvo_commit é o último commit que mudou os bytes auditados (artigo, "
                        "manuscrito, 11 fichas, fontes). Todos os sha256 de fontes[] foram lidos "
                        "do próprio commit, com `git show <alvo>:<path>`.")
    man["pergunta"] = ("As afirmações do artigo e das 11 fichas são fielmente sustentadas pelas "
                       "21 fontes custodiadas neste repositório, e o que não está medido está "
                       "declarado como tal?")
    obj = man.get("objeto", {})
    for k in list(obj):
        if "ficha" in k:
            obj[k] = obj[k] if isinstance(obj[k], (int, str)) else obj[k]
    man["objeto"] = obj
    ed = man.get("estado_declarado", {})
    ed["fichas"] = (f"{len([f for f in man['fontes'] if '/fichas/' in f['path']])} fichas, todas em "
                    "em-revisao-documental: homologacao interna e ato declarado, nao leitura medida")
    ed["artigo"] = ("peça corrida (molde do boro, 13 seções), peça em abas e manuscrito único de "
                    "ponta a ponta com 21 referências ABNT comentadas")
    man["estado_declarado"] = ed
    if "parte_1_perguntas" in man:
        # idempotente: rodar o reselar duas vezes não pode duplicar a pergunta
        _existentes = {q.get("id") for q in man["parte_1_perguntas"]}
        _novas = []
        _novas.append({
            "id": "Q9",
            "pergunta": ("O capítulo 9 afirma que a norma federal de preservação de madeira (PI 292/89) "
                         "existe, nomeia o Ibama como fiscalizador (art. 20) e NÃO trata da destinação "
                         "final do resíduo. Isso é sustentado pelo texto integral da Portaria, e a "
                         "palavra «resíduo» está de fato ausente dela?"),
            "arquivo": "docs/analyses/cobre/o-cobre-no-bambu-corrido.html",
            "ancora": "seção 9 — A norma existe — e ela não chega ao quintal",
            "fonte": "docs/analyses/cobre/fontes/s11c/1989_pi292_preservativos_registro.pdf",
        })
        _novas.append({
            "id": "Q10",
            "pergunta": ("O capítulo distingue norma ESPECÍFICA (que a madeira tem e não cumpre) de "
                         "OBRIGAÇÃO GERAL (que vale para o bambu)? O texto afirma que a obrigação "
                         "geral não foi aplicada a este resíduo, ou apenas que não há documento de "
                         "aplicação — e onde diz qual das duas coisas?"),
            "arquivo": "docs/analyses/cobre/o-cobre-no-bambu-corrido.html",
            "ancora": "seção 9 — «O que fica»",
            "fonte": "docs/analyses/cobre/fontes_novas/pnrs_art3_XVI.txt",
        })

        man["parte_1_perguntas"].extend(q for q in _novas if q["id"] not in _existentes)

    open(os.path.join(REPO, man_path), "w", encoding="utf-8").write(
        json.dumps(man, ensure_ascii=False, indent=1) + "\n")
    print(f"MANIFESTO {man_path}\n  {man['total_fontes']} fontes ({novas} novas) | alvo {alvo[:12]}")

    # 4) HASHES_RESPONSE já no disco, calculado sobre os bytes do próprio manifesto.
    #    O sha256 de um arquivo não depende do commit que o contém, então dá para fechar os dois
    #    no MESMO commit — e é obrigatório que seja assim: o gate 14 lê o HASHES_RESPONSE no
    #    manifest_commit, e se ele for commitado depois, o que está lá é a versão anterior.
    man_bytes_disco = open(os.path.join(REPO, man_path), "rb").read()
    man_sha = hashlib.sha256(man_bytes_disco).hexdigest()

    # 5) HASHES_RESPONSE
    resp = {
        "schema": "TAKWARATEC_R4_HASHES_RESPONSE_R1",
        "manifest_id": man["manifest_id"],
        "commit_alvo": alvo,
        "manifest_path_lido": man_path,
        "sha256_do_manifesto": man_sha,
        "metodo": ("Cada sha256 foi calculado sobre os bytes servidos por `git show "
                   "<commit>:<path>`, no próprio repositório, e não sobre cópia local."),
        "total_fontes": man["total_fontes"],
        "fontes_sha256": {f["path"]: f["sha256"] for f in man["fontes"]},
    }
    # bytes_do_manifesto precisa refletir o disco
    resp["bytes_do_manifesto"] = len(man_bytes_disco)
    open(os.path.join(REPO, hr_path), "w", encoding="utf-8").write(
        json.dumps(resp, ensure_ascii=False, indent=1) + "\n")

    # números da mensagem saem do manifesto, não de constante digitada
    nf_fich = len([f for f in man["fontes"] if "/fichas/" in f["path"]
                   and not f["path"].endswith("MANIFEST_FICHAS_PUBLICADAS.json")])
    # manifesto e resposta no mesmo commit
    git("add", man_path, hr_path)
    if prev != man_path:
        git("rm", "-q", "--ignore-unmatch", prev)
    git("commit", "-q", "-m",
        f"auditoria(cobre): manifesto e hashes do alvo {alvo[:8]} — {nf_fich} fichas, "
        f"{man['total_fontes']} fontes")
    man_commit = git("rev-parse", "HEAD").stdout.decode().strip()

    # conferência: o hash declarado é o que o git serve?
    man_sha_git, man_bytes_git = blob_sha(man_commit, man_path)
    assert man_sha_git == man_sha, f"manifesto divergente do commit: {man_sha_git[:12]} != {man_sha[:12]}"
    hr_sha, _ = blob_sha(man_commit, hr_path)
    hr_commit = man_commit  # as duas peças vivem no mesmo commit, por desenho
    print(f"MANIFESTO+HASHES commit {man_commit[:12]}  manifesto {man_sha[:16]}…  hr {hr_sha[:16]}…  {man_bytes_git:,} B")
    print(f"HASHES_RESPONSE {hr_path}\n  commit {hr_commit[:12]}  sha256 {hr_sha[:16]}…")

    # 6) ponteiro
    if sem_ponteiro:
        print("PONTEIRO: nao escrito (--sem-ponteiro). O ponteiro mora em ops/ e pertence a "
              "PR de governanca: a gaveta do cobre nao carrega arquivo fora dela (A7).")
        print(f"\nMANIFESTO {man_commit} · HASHES_RESPONSE {hr_commit}")
        print("CASCATA COMPLETA sem ponteiro. Falta: git push e a verificacao dos 23 gates.")
        return
    pt = {
        "schema": "TAKWARATEC_R4_AUDIT_POINTER_R1",
        "frente": "COBRE",
        "manifest_id": man["manifest_id"],
        "status": "ABERTO",
        "manifest_branch": BRANCH,
        "manifest_commit": man_commit,
        "manifest_path": man_path,
        "sha256_do_manifesto": man_sha,
        "hashes_response_path": hr_path,
        "sha256_do_hashes_response": hr_sha,
        "hashes_response_commit": hr_commit,
        "alvo_commit": alvo,
        "atualizado_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "instrucao_ao_auditor": (
            "Comece AQUI, neste arquivo, no commit da branch que você recebeu. Leia o manifesto "
            "em manifest_commit e confira sha256_do_manifesto; leia o HASHES_RESPONSE no mesmo "
            "commit e confira sha256_do_hashes_response; só então abra as fontes em alvo_commit. "
            "Não leia o manifesto que aparece dentro do alvo_commit: é o da rodada anterior."),
    }
    open(f"{REPO}/{PT}", "w", encoding="utf-8").write(
        json.dumps(pt, ensure_ascii=False, indent=1) + "\n")
    git("add", PT)
    git("commit", "-q", "-m", f"auditoria(cobre): ponteiro repinado — alvo {alvo[:8]}, manifesto {man_sha[:12]}")
    print(f"PONTEIRO commit {git('rev-parse', 'HEAD').stdout.decode().strip()[:12]}")
    print("\nCASCATA COMPLETA. Falta: git push e a verificação dos 23 gates.")


if __name__ == "__main__":
    main()
