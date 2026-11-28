#!/usr/bin/env python3
"""Gerador de pacote de auditoria externa (Sol) — Acervo Soberania Tecnologica.

Nasceu do molde do COBRE, com as quatro falhas que a auditoria R19 encontrou embutidas
como falha fechada. Cada uma virou uma checagem que RECUSA gerar:

  R19-A  metodo impossivel   -> `git show` sobre item fora do rastreio. Cada fonte declara o
                                metodo REAL usado; o gerador le os bytes e falha se nao existir.
  R19-B  ponteiro fantasma   -> referencia a arquivo que nao existe no alvo. Toda referencia do
                                manifesto e resolvida contra o commit alvo antes de selar.
  R19-C  selo que nao e par  -> manifesto e resposta de hashes saem juntos, no mesmo commit.
  R19-D  caminho vazio       -> instrucao de leitura apontando para diretorio esvaziado. Toda
                                instrucao `como_reproduzir` que nomeia caminho e verificada.

Mais duas que esta casa aprendeu doendo:

  A2     declaracao de conferencia sem registro -> o manifesto declara NAO_MEDIDO o que nao
         foi medido, e nunca afirma cobertura que nao existe.
  BASE   escopo e selo valem para um commit; o alvo entra no nome do arquivo e na saida.

Uso:
    python3 scripts/pacote_auditoria/gerar.py --frente cobre --alvo HEAD --repo .
    python3 scripts/pacote_auditoria/gerar.py --frente boro  --alvo origin/main --repo . --check

`--check` nao escreve: valida o existente e sai 1 se algo nao resolve.
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys

SCHEMA_MANIFEST = "TAKWARATEC_R4_AUDIT_MANIFEST_R1"
SCHEMA_HASHES = "TAKWARATEC_R4_HASHES_RESPONSE_R1"
VERSAO = "2.0.0"

# Metodos que o gerador sabe EXECUTAR. Metodo declarado fora desta lista recusa o selo:
# declarar um metodo que o instrumento nao executa foi o defeito R19-A.
METODOS = {
    "git_show_no_commit": "bytes servidos por `git show <alvo>:<path>`, nunca copia local",
    "registro_custodia_privada": (
        "bytes do arquivo em disco no caminho privado declarado, hash conferido contra o "
        "registro de custodia; `git show` NAO se aplica"
    ),
}


class Recusa(RuntimeError):
    """O pacote nao pode ser selado. Nao e aviso: e parada."""


def git(repo, *args, binario=False):
    r = subprocess.run(["git", "-C", repo, *args], capture_output=True)
    if r.returncode != 0:
        raise Recusa(f"git {' '.join(args)} -> exit {r.returncode}: {r.stderr.decode()[:300]}")
    return r.stdout if binario else r.stdout.decode()


def resolve_alvo(repo, ref):
    return git(repo, "rev-parse", f"{ref}^{{commit}}").strip()


def existe_no_commit(repo, commit, path):
    r = subprocess.run(["git", "-C", repo, "cat-file", "-e", f"{commit}:{path}"], capture_output=True)
    return r.returncode == 0


def bytes_no_commit(repo, commit, path):
    return git(repo, "cat-file", "-p", f"{commit}:{path}", binario=True)


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def serializar(obj):
    """O UNICO lugar que produz o byte publicado.

    O defeito que o Sol achou (C-02/B-02 dos pareceres): o gerador selava o objeto em memoria sem o
    LF final e escrevia o arquivo com LF. Hash declarado nunca conferia com o arquivo publicado.
    Agora o mesmo byte e selado e escrito, e depois RELIDO do disco.
    """
    return (json.dumps(obj, ensure_ascii=False, indent=2) + "\n").encode()


def publicar(caminho, obj):
    b = serializar(obj)
    with open(caminho, "wb") as f:
        f.write(b)
    return b


def conferir_no_disco(caminho, esperado, rotulo):
    """Rele o arquivo publicado e compara. Selo que nao confere com o disco e selo quebrado."""
    with open(caminho, "rb") as f:
        b = f.read()
    obtido = sha256(b)
    if obtido != esperado:
        raise Recusa(
            f"selagem inconsistente em {rotulo}: disco={obtido[:16]}... declarado={esperado[:16]}... "
            f"({len(b)} bytes). O byte selado tem de ser o byte publicado."
        )
    return obtido, len(b)


def montar_fonte(repo, commit, item, raiz_privada=""):
    """Monta uma entrada de fonte e PROVA o metodo. Falha fechado."""
    path = item["path"]
    papel = item.get("papel", "")
    no_repo = bool(item.get("no_repositorio", True))

    if no_repo:
        if not existe_no_commit(repo, commit, path):
            raise Recusa(f"R19-B: fonte declarada no repositorio nao existe em {commit[:12]}: {path}")
        b = bytes_no_commit(repo, commit, path)
        return {
            "path": path,
            "sha256": sha256(b),
            "bytes": len(b),
            "papel": papel,
            "no_repositorio": True,
            "metodo": "git_show_no_commit",
        }

    # Fora do rastreio: o byte tem de existir em disco. Sem isso o metodo declarado e ficcao.
    caminho_privado = item.get("caminho_privado")
    if not caminho_privado:
        raise Recusa(
            f"R19-A: fonte fora do rastreio sem caminho_privado: {path}. "
            f"Sem o byte, 'git show' seria mentira e o registro de custodia nao pode ser afirmado."
        )
    # A custodia privada vive FORA de qualquer worktree (o _privado/ e gitignored): num worktree
    # ela nao existe. raiz_privada permite apontar para a raiz do checkout principal.
    if os.path.isabs(caminho_privado):
        abs_path = caminho_privado
    elif raiz_privada:
        abs_path = os.path.join(raiz_privada, caminho_privado)
    else:
        abs_path = os.path.join(repo, caminho_privado)
    if not os.path.exists(abs_path):
        raise Recusa(
            f"R19-A: caminho_privado declarado nao existe em disco: {caminho_privado} "
            f"(fonte {path}). Declarar custodia que nao se pode ler e metodo impossivel."
        )
    with open(abs_path, "rb") as f:
        b = f.read()
    esperado = item.get("sha256")
    if esperado and esperado != sha256(b):
        raise Recusa(
            f"R19-A: hash do arquivo privado nao confere com o declarado em {path}: "
            f"disco={sha256(b)[:16]}... declarado={esperado[:16]}..."
        )
    return {
        "path": path,
        "sha256": sha256(b),
        "bytes": len(b),
        "papel": papel,
        "no_repositorio": False,
        "caminho_privado": caminho_privado,
        "metodo": "registro_custodia_privada",
    }


def instrucoes_nomeiam_caminho(instrucoes, repo, commit, ignorar=()):
    """R19-D: toda instrucao que nomeia um caminho do repositorio tem de resolver no commit.

    Uma instrucao que manda abrir `fontes/pdf/` num pacote onde esse diretorio foi esvaziado e
    o mesmo defeito do ponteiro fantasma: o auditor segue e nao acha nada.
    """
    problemas = []
    padrao = re.compile(r"(docs/[\w\-./]+|scripts/[\w\-./]+|_privado/[\w\-./]+)")
    for linha in instrucoes:
        for caminho in padrao.findall(linha):
            c = caminho.rstrip(".,;:)]")
            if any(c == i or c.endswith(os.path.basename(i)) for i in ignorar):
                continue
            if not (existe_no_commit(repo, commit, c) or existe_no_commit(repo, commit, c + "/")
                    or _tem_prefixo(repo, commit, c)):
                problemas.append(f"R19-D: instrucao aponta para caminho inexistente no alvo: {c}")
    return problemas


def _tem_prefixo(repo, commit, prefixo):
    """Um diretorio so existe no git por ter arquivos dentro; confere se ha algum."""
    try:
        saida = git(repo, "ls-tree", "-r", "--name-only", commit, "--", prefixo + "/")
    except Recusa:
        return False
    return bool(saida.strip())


def pendura_em_algum_commit(repo, path):
    """R19-B: referencias em allowed_refs tem de existir em ALGUM lugar do historico."""
    r = subprocess.run(["git", "-C", repo, "log", "--all", "--name-only", "--pretty=format:", "--", path],
                       capture_output=True, text=True)
    return bool(r.stdout.strip())


def contar_selos(repo, pasta):
    """Conta por CAMINHO no historico, nao por mensagem de commit (o erro que fez 19 de 28)."""
    r = subprocess.run(["git", "-C", repo, "log", "--all", "--name-only", "--pretty=format:", "--", pasta],
                       capture_output=True, text=True)
    manifestos = sorted({l.strip() for l in r.stdout.splitlines()
                         if "MANIFEST_R1" in l and l.strip().endswith(".json")})
    respostas = sorted({l.strip() for l in r.stdout.splitlines()
                        if "HASHES_RESPONSE_R1" in l and l.strip().endswith(".json")})
    def sufixo(p):
        m = re.search(r"R1_([0-9a-f]{8})\.json$", p)
        return m.group(1) if m else "sem-sufixo"
    s_m = {sufixo(p) for p in manifestos}
    s_r = {sufixo(p) for p in respostas}
    return {
        "manifestos_no_historico": len(manifestos),
        "respostas_no_historico": len(respostas),
        "alvos": sorted(s_m | s_r),
        "so_manifesto": sorted(s_m - s_r),
        "so_resposta": sorted(s_r - s_m),
    }


CONTAGEM_EM_PROSA = re.compile(
    r"\b(\d+)\s+(arquivos?|fontes?|fichas?|PDFs?|afirmac\S*|afirma\S*|paragraf\S*|par\S*grafos?|"
    r"blocos?|registros?|citac\S*|cita\S*es?)\b", re.I)


def proibir_contagem_em_prosa(cfg):
    """C-04 do parecer: o objeto dizia 34, a lista tinha 33, o registro de custodia 16.

    Tres numeros para a mesma coisa porque cada um foi escrito a mao. Contagem e afirmacao sobre o
    pacote: quem conta e o gerador, num lugar so.
    """
    achados = []
    for campo in ("objeto", "estado_declarado", "aviso_de_leitura", "como_ler", "nao_medido_declarado"):
        texto = json.dumps(cfg.get(campo, ""), ensure_ascii=False)
        for m in CONTAGEM_EM_PROSA.finditer(texto):
            achados.append(f"{campo}: '{m.group(0)}'")
    if achados:
        raise Recusa(
            "C-04: contagem escrita a mao na prosa (" + "; ".join(achados) + "). "
            "O denominador e calculado pelo gerador no bloco 'denominador'. Descreva a composicao "
            "sem numero, para nao haver dois totais para o mesmo conjunto."
        )


def contar_registros(repo, commit, definicoes):
    """O placar do registro e LIDO do registro, nunca redigitado no manifesto.

    B-01 do parecer do Sol: o manifesto dizia 283/65/200 e o registro tinha 286/62/206. O manifesto
    repetia um numero copiado a mao de um relato. Quem conta e o registro; o manifesto cita o hash e
    o resultado da contagem.
    """
    saida = []
    for d in definicoes:
        path = d["path"]
        if not existe_no_commit(repo, commit, path):
            raise Recusa(f"registro declarado nao existe no alvo: {path}")
        bruto = bytes_no_commit(repo, commit, path)
        if path.endswith(".jsonl"):
            itens = [json.loads(l) for l in bruto.decode().splitlines() if l.strip()]
        else:
            doc = json.loads(bruto)
            itens = doc
            for chave in d.get("lista", "registros").split("."):
                itens = itens[chave]
        campo = d.get("campo", "veredito")
        contagem = {}
        for i in itens:
            k = str(i.get(campo))
            contagem[k] = contagem.get(k, 0) + 1
        saida.append({
            "path": path,
            "sha256": sha256(bruto),
            "bytes": len(bruto),
            "campo_de_veredito": campo,
            "total": len(itens),
            "por_veredito": dict(sorted(contagem.items(), key=lambda kv: -kv[1])),
            "nota": "contagem derivada do registro neste commit; nenhum numero deste bloco foi escrito a mao",
        })
    return saida


def gerar_manifesto(cfg, repo, commit, raiz_privada_arg=None):
    raiz_privada = raiz_privada_arg or cfg.get("raiz_privada", "")
    fontes = [montar_fonte(repo, commit, f, raiz_privada) for f in cfg["fontes"]]

    proibir_contagem_em_prosa(cfg)

    suf = commit[:8]
    nome_m = f"AUDITORIA_SOL_{cfg['frente'].upper()}_MANIFEST_R1_{suf}.json"
    path_m = os.path.join(cfg["pasta"], nome_m)

    # C-09/B-05 do parecer: o manifesto e publicado DEPOIS do commit de conteudo — instrucao que
    # manda ler o manifesto dentro do alvo nao funciona. O gerador separa os dois commits.
    passo_pacote = [
        f"1. Os objetos auditados estao no commit de CONTEUDO {commit}: faca `git checkout {commit}` "
        f"para ler o texto, as fichas e os registros.",
        f"2. Este manifesto NAO existe dentro do commit de conteudo — ele foi publicado depois, no "
        f"commit de EMPACOTAMENTO. Localize-o assim: `git log --all --format=%h -- {path_m}` e leia o "
        f"mais recente. Procurar o manifesto em {suf} encontra a rodada anterior, ou nada.",
    ]
    resto = [re.sub(r"^\s*\d+\.\s*", "", t) for t in cfg["como_reproduzir"]]
    como_reproduzir = passo_pacote + [f"{i + 3}. {t}" for i, t in enumerate(resto)]

    problemas = instrucoes_nomeiam_caminho(como_reproduzir, repo, commit,
                                          ignorar={path_m, path_m.replace("MANIFEST", "HASHES_RESPONSE")})
    if problemas:
        raise Recusa("; ".join(problemas))

    for ref in cfg.get("referencias_resolviveis", []):
        if not (existe_no_commit(repo, commit, ref) or pendura_em_algum_commit(repo, ref)):
            raise Recusa(f"R19-B: referencia do manifesto nao resolve no alvo nem no historico: {ref}")

    por_metodo = {}
    for f in fontes:
        por_metodo.setdefault(f["metodo"], []).append(f["path"])

    m = {
        "schema": SCHEMA_MANIFEST,
        "versao": VERSAO,
        "manifest_id": cfg["manifest_id"],
        "status": "ABERTO",
        "gerado_utc": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
        "tipo": "CONTEUDO",
        "frente": cfg["frente"],
        "autoridade": cfg["autoridade"],
        "alvo_branch": cfg["alvo_branch"],
        "alvo_commit": commit,
        "alvo_nota": (
            "alvo_commit e o ultimo commit que mudou os bytes auditados. O manifesto nao nomeia o "
            "proprio commit: um objeto nao pode conter o proprio hash. Quem audita compara alvo_commit "
            "ao ultimo commit de CONTEUDO, nunca ao HEAD."
        ),
        "aviso_de_leitura": cfg["aviso_de_leitura"],
        "o_que_esta_auditoria_e": cfg["o_que_esta_auditoria_e"],
        "pedido_do_soberano": cfg["pedido_do_soberano"],
        "objeto": cfg["objeto"],
        "estado_declarado": cfg["estado_declarado"],
        "pergunta": cfg["pergunta"],
        "parte_1_perguntas": cfg["parte_1_perguntas"],
        "fontes": fontes,
        "criterios": cfg["criterios"],
        "severidade": cfg["severidade"],
        "formato_resposta": cfg["formato_resposta"],
        "limites": cfg["limites"],
        "nao_homologa": cfg["nao_homologa"],
        "como_reproduzir": como_reproduzir,
        "erro_anterior_declarado": cfg.get("erro_anterior_declarado", {"nota": "", "itens": []}),
        "metodos_de_hash": METODOS,
        "registros_de_conferencia": contar_registros(repo, commit, cfg.get("registros", [])),
        "denominador": {
            "aviso": (
                "Estas sao as unicas contagens do pacote. Quantidade de ARQUIVO nao e quantidade de OBRA: "
                "uma obra pode ter PDF custodiado, extrato textual e ficha, e tres arquivos contam uma fonte."
            ),
            "fontes_no_manifesto": len(fontes),
            "no_repositorio": sum(1 for f in fontes if f["no_repositorio"]),
            "em_custodia_privada": sum(1 for f in fontes if not f["no_repositorio"]),
            "por_metodo": {k: len(v) for k, v in por_metodo.items()},
            "o_que_conta_como_fonte": cfg.get("o_que_conta_como_fonte",
                                              "obra cientifica ou normativa referenciada pelo texto"),
            "o_que_NAO_conta": cfg.get("o_que_nao_conta",
                                       ["extrato textual (derivado da obra)", "ficha (documento proprio)",
                                        "instrumento de medicao", "registro de conferencia"]),
        },
        "pacote": {
            "manifest_path": path_m,
            "commit_do_conteudo": commit,
            "commit_do_pacote": None,
            "nota": (
                "commit_do_pacote fica nulo porque o commit nao pode nomear a si mesmo. Quem audita "
                "localiza o pacote pelo caminho do manifesto no historico, nunca dentro do commit de conteudo."
            ),
        },
        "total_fontes": len(fontes),
        "fontes_por_metodo": {k: len(v) for k, v in por_metodo.items()},
        "nao_medido_declarado": cfg["nao_medido_declarado"],
        "como_ler": cfg["como_ler"],
    }
    return m, por_metodo


def gerar_resposta(cfg, repo, commit, m, por_metodo, path_manifesto):
    b = serializar(m)   # o byte publicado, nao o objeto em memoria
    return {
        "schema": SCHEMA_HASHES,
        "manifest_id": m["manifest_id"],
        "commit_alvo": commit,
        "manifest_path_lido": path_manifesto,
        "sha256_do_manifesto": sha256(b),
        "metodo": (
            f"Para os {m['fontes_por_metodo'].get('git_show_no_commit', 0)} itens presentes no "
            f"repositorio, o sha256 foi calculado sobre os bytes servidos por `git show <commit>:<path>`. "
            f"Para os {m['fontes_por_metodo'].get('registro_custodia_privada', 0)} itens fora do rastreio, "
            f"o sha256 vem do arquivo em disco no caminho privado declarado, conferido contra o registro "
            f"de custodia; `git show` NAO se aplica a eles."
        ),
        "sha256_por_metodo": por_metodo,
        "total_fontes": m["total_fontes"],
        "fontes_sha256": {f["path"]: f["sha256"] for f in m["fontes"]},
        "bytes_do_manifesto": len(b),
    }


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--frente", required=True, help="cobre | boro | nome da gaveta")
    ap.add_argument("--alvo", default="HEAD", help="commit/branch auditado (default: HEAD)")
    ap.add_argument("--repo", default=".", help="raiz do repositorio do acervo")
    ap.add_argument("--cfg", required=True, help="configuracao da frente (JSON)")
    ap.add_argument("--check", action="store_true", help="valida sem escrever; sai 1 se nao resolve")
    ap.add_argument("--privado", default=None,
                    help="raiz da custodia privada (default: <repo>). Necessario em worktree.")
    a = ap.parse_args(argv)

    with open(a.cfg, encoding="utf-8") as f:
        cfg = json.load(f)

    repo = os.path.abspath(a.repo)
    commit = resolve_alvo(repo, a.alvo)

    try:
        m, por_metodo = gerar_manifesto(cfg, repo, commit, a.privado)
    except Recusa as e:
        print(f"RECUSA: {e}")
        return 2

    pasta = cfg["pasta"]
    suf = commit[:8]
    nome_m = f"AUDITORIA_SOL_{cfg['frente'].upper()}_MANIFEST_R1_{suf}.json"
    nome_r = f"AUDITORIA_SOL_{cfg['frente'].upper()}_HASHES_RESPONSE_R1_{suf}.json"
    path_m = os.path.join(pasta, nome_m)

    r = gerar_resposta(cfg, repo, commit, m, por_metodo, path_m)
    r_selo = sha256(serializar(r))

    selos = contar_selos(repo, pasta)
    print(f"FRENTE={cfg['frente']} ALVO={suf} FONTES={m['total_fontes']}")
    print(f"  por metodo: {m['fontes_por_metodo']}")
    print(f"  manifesto:  {path_m}")
    print(f"  resposta:   {os.path.join(pasta, nome_r)}")
    print(f"  sha256 manifesto: {r['sha256_do_manifesto'][:16]}... bytes={r['bytes_do_manifesto']}")
    print(f"  selos no historico: {selos['manifestos_no_historico']} manifestos / "
          f"{selos['respostas_no_historico']} respostas")
    if selos["so_manifesto"] or selos["so_resposta"]:
        print(f"  ATENCAO orfaos: so_manifesto={selos['so_manifesto']} so_resposta={selos['so_resposta']}")
    print("  R19-A metodo por fonte: OK · R19-B referencias: OK · R19-D instrucoes: OK")

    if a.check:
        print("CHECK: nada foi escrito (--check).")
        return 0

    os.makedirs(os.path.join(repo, pasta), exist_ok=True) if not os.path.isabs(pasta) else os.makedirs(pasta, exist_ok=True)
    base = repo if not os.path.isabs(pasta) else ""
    alvo_m = os.path.join(base, path_m)
    alvo_r = os.path.join(base, pasta, nome_r)

    # Escreve o byte que foi selado, e depois RELÊ do disco: vale o que esta publicado, nao o que se
    # pretendia publicar. Sem esta releitura, o selo do COBRE saiu com o hash do objeto em memoria
    # (sem o LF final) e nao conferiu com o arquivo — achado do Sol, 25/11.
    try:
        bm = publicar(alvo_m, m)
        br = publicar(alvo_r, r)
        h, n = conferir_no_disco(alvo_m, r["sha256_do_manifesto"], "manifesto")
        hr, nr = conferir_no_disco(alvo_r, r_selo, "resposta")
    except Recusa as e:
        for alvo in (alvo_m, alvo_r):
            if os.path.exists(alvo):
                os.remove(alvo)
        print(f"RECUSA: {e}")
        return 2

    print(f"  escrito: {alvo_m} ({len(bm)} bytes)")
    print(f"  escrito: {alvo_r} ({len(br)} bytes)")
    print(f"  RELIDO DO DISCO: manifesto {h[:16]}... == declarado na resposta ({n} bytes)")
    print(f"  RELIDO DO DISCO: resposta {hr[:16]}... == selo da resposta ({nr} bytes)")

    print("  R19-C par selado junto: manifesto e resposta no mesmo commit (commite os dois).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
