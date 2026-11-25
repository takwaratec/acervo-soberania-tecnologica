#!/usr/bin/env python3
"""SELOS.md — índice dos selos da frente do cobre.

A árvore carrega UM par (manifesto + resposta de hashes) para o alvo vigente.
O payload dos selos anteriores vive no git, onde já estava; aqui fica o índice:
alvo, sha256 das duas peças, data e commit em que o par completo existe.

Fonte da verdade é o HISTÓRICO DE CAMINHOS, não a mensagem de commit: selo antigo
cujo commit não dizia "alvo <hash>" existia do mesmo jeito. Índice que conta por
mensagem declara menos do que o repositório guarda.

Se um lado do par não existir, ele não vira linha de tabela: vira rodapé de órfãos.
"""
import hashlib
import os
import re
import subprocess

REPO = os.environ.get("COBRE_REPO", ".")
DIR = "docs/analyses/cobre"
SAIDA = f"{DIR}/SELOS.md"
PAD = "docs/analyses/cobre/AUDITORIA_SOL_COBRE_"


def _git(*a) -> bytes:
    r = subprocess.run(["git", "-C", REPO, *a], capture_output=True)
    if r.returncode != 0:
        raise SystemExit(f"git {' '.join(a)} falhou: {r.stderr.decode()[:300]}")
    return r.stdout


def _git_txt(*a) -> str:
    return _git(*a).decode()


def _caminhos_do_historico() -> list:
    bruto = _git_txt("log", "--all", "--pretty=format:", "--name-only", "--", DIR)
    return sorted({l.strip() for l in bruto.splitlines() if l.strip().startswith(PAD)})


def _sha_e_data(caminho: str):
    """sha256 do byte no commit mais recente que REALMENTE o contém, e a data desse commit.

    `git log -1 -- <caminho>` pode devolver o commit que apagou o arquivo; aqui se anda
    a lista de commits que tocam o caminho até achar um cujo blob exista.
    """
    for commit in _git_txt("rev-list", "--all", "--", caminho).split():
        r = subprocess.run(["git", "-C", REPO, "cat-file", "-e", f"{commit}:{caminho}"],
                           capture_output=True)
        if r.returncode != 0:
            continue
        blob = _git("show", f"{commit}:{caminho}")
        data = _git_txt("show", "-s", "--format=%cI", commit).strip()
        return hashlib.sha256(blob).hexdigest(), data, commit
    return None


def main():
    caminhos = _caminhos_do_historico()
    mans, hrs, sem_sufixo = {}, {}, {}
    for c in caminhos:
        nome = c[len(PAD):]
        m = re.fullmatch(r"MANIFEST_R1_([0-9a-f]{8})\.json", nome)
        h = re.fullmatch(r"HASHES_RESPONSE_R1_([0-9a-f]{8})\.json", nome)
        if m:
            mans[m.group(1)] = c
        elif h:
            hrs[h.group(1)] = c
        elif nome in ("MANIFEST_R1.json", "HASHES_RESPONSE_R1.json"):
            sem_sufixo[nome] = c

    selos, orfaos = [], []
    for alvo in sorted(set(mans) | set(hrs)):
        if alvo in mans and alvo in hrs:
            pm = _sha_e_data(mans[alvo])
            ph = _sha_e_data(hrs[alvo])
            if pm and ph:
                selos.append({"alvo": alvo, "man": pm[0], "hr": ph[0],
                              "data": pm[1], "commit": pm[2]})
            else:
                faltando = [l for l, v in (("manifesto", pm), ("resposta", ph)) if not v]
                orfaos.append((alvo, "sem blob recuperável: " + ", ".join(faltando)))
        else:
            lado = "manifesto" if alvo in mans else "resposta de hashes"
            orfaos.append((alvo, lado))

    if "MANIFEST_R1.json" in sem_sufixo and "HASHES_RESPONSE_R1.json" in sem_sufixo:
        pm = _sha_e_data(sem_sufixo["MANIFEST_R1.json"])
        ph = _sha_e_data(sem_sufixo["HASHES_RESPONSE_R1.json"])
        if pm and ph:
            selos.append({"alvo": "(sem sufixo)", "man": pm[0], "hr": ph[0],
                          "data": pm[1], "commit": pm[2]})
        else:
            orfaos.append(("(sem sufixo)", "sem blob recuperável"))
    elif sem_sufixo:
        orfaos.append(("(sem sufixo)", ", ".join(sorted(sem_sufixo))))

    # selo vigente: está no mesmo commit deste índice, então ainda não está no histórico.
    # Vem por ambiente (alvo|sha_manifesto|sha_resposta) e entra com commit nomeado como este.
    atual = os.environ.get("COBRE_SELO_ATUAL", "").strip()
    if atual:
        partes = atual.split("|")
        if len(partes) == 3:
            import datetime as _dt
            selos.append({"alvo": partes[0], "man": partes[1], "hr": partes[2],
                          "data": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
                          "commit": "(este commit)"})

    selos.sort(key=lambda s: s["data"], reverse=True)

    linhas = [
        "---",
        "schema: ACERVO_INDICE_R1",
        "gaveta: cobre",
        "frente: COBRE",
        'titulo: "Selos da frente do cobre"',
        "tipo_documental: indice",
        "estado_documental: em-revisao-documental",
        "homologacao_automatica: false",
        "responsavel_curadoria: Fabio Takwara",
        "assistencia_documental: agente de IA, sujeito a revisao humana",
        "---",
        "",
        "# Selos da frente do cobre",
        "",
        "A árvore carrega **um** par: `AUDITORIA_SOL_COBRE_MANIFEST_R1_<alvo>.json` e",
        "`AUDITORIA_SOL_COBRE_HASHES_RESPONSE_R1_<alvo>.json`, para o alvo vigente.",
        "Os pares anteriores foram retirados da árvore e continuam no git — o commit de cada",
        "um está na tabela. `git show <commit>:<arquivo>` recupera o byte, e o sha256 abaixo",
        "confere se o que veio é o mesmo.",
        "",
        "| alvo_commit | sha256 do manifesto | sha256 da resposta | data | commit do par |",
        "|---|---|---|---|---|",
    ]
    for s in selos:
        linhas.append(f"| `{s['alvo']}` | `{s['man'][:16]}…` | `{s['hr'][:16]}…` | "
                      f"{s['data'][:19]}Z | `{s['commit'][:12]}` |")
    linhas.append("")
    linhas.append(f"Total de selos indexados: **{len(selos)}**.")
    if orfaos:
        linhas.append("")
        linhas.append(f"Manifestos ou respostas órfãos, sem par no histórico: **{len(orfaos)}**.")
        for alvo, lado in orfaos:
            linhas.append(f"- `{alvo}` — só {lado}.")
    linhas += [
        "",
        "Gerado por `scripts/gerar_selos_cobre.py` a partir do histórico de caminhos; "
        "não editar à mão.",
    ]
    open(os.path.join(REPO, SAIDA), "w", encoding="utf-8").write("\n".join(linhas) + "\n")
    print(f"SELOS: {SAIDA} — {len(selos)} selos, {len(orfaos)} órfãos")


if __name__ == "__main__":
    main()
