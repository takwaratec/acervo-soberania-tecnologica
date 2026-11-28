#!/usr/bin/env python3
"""Reproduz a soma de importação de boro do ComexStat a partir do bruto custodiado.

Existe para que o número do artigo possa ser refeito por quem lê, sem confiar no
relato de quem escreveu. Somar não é interpretar: mesma entrada, mesmo total.

Uso:
    python3 scripts/gate_boro/reproduzir_comexstat.py --ano 2024
    python3 scripts/gate_boro/reproduzir_comexstat.py --ano 2024 --sem 28499010 28500010 28045000
"""
import argparse
import json
import os
import sys

# Os doze códigos declarados na Seção 5 do artigo. Dois deles (2528.10.00 e 2528.90.00)
# não têm linha no bruto de 2024 — foram desmembrados de 2528.00.00 na NCM; por isso a
# soma efetiva é de dez códigos, e é isso que o artigo declara.
CODNCM = [
    "25280000",  # boratos naturais e concentrados
    "25281000",  # boratos de sódio naturais (ausente no bruto de 2024)
    "25289000",  # outros boratos naturais (ausente no bruto de 2024)
    "28045000",  # boro; telúrio
    "28100010",  # ácido ortobórico
    "28100090",  # óxidos de boro e outros ácidos bóricos
    "28401100",  # tetraborato dissódico anidro
    "28401900",  # outros tetraboratos dissódicos
    "28402000",  # outros boratos
    "28403000",  # peroxoboratos
    "28499010",  # carbonetos de boro
    "28500010",  # nitreto de boro
]

PADRAO = ("_privado/governanca-operacional/extracoes/boro/fontes_novas/"
          "comexstat/raw/ncm_{ano}.json")

# A gaveta vive fora do worktree, no acervo. Procurar só relativo à raiz do repo fazia o
# comando falhar para quem clona o repo e não tem a camada privada montada — e comando que
# falha no primeiro uso não reproduz nada. Ordem: --bruto, $ACERVO, caminho relativo.
RAIZES = [
    os.environ.get("ACERVO", ""),
    "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica",
]


def resolver(ano, bruto=None):
    if bruto:
        return bruto
    raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    for base in [raiz] + [r for r in RAIZES if r]:
        c = os.path.join(base, PADRAO.format(ano=ano))
        if os.path.exists(c):
            return c
    return os.path.join(raiz, PADRAO.format(ano=ano))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ano", default="2024")
    ap.add_argument("--bruto", default=None, help="caminho do ncm_<ano>.json")
    ap.add_argument("--sem", nargs="*", default=[], help="códigos a excluir")
    a = ap.parse_args()

    caminho = resolver(a.ano, a.bruto)
    if not os.path.exists(caminho):
        sys.exit(f"bruto ausente: {caminho}\n"
                 "o manifesto do ComexStat está em "
                 "_privado/governanca-operacional/extracoes/boro/fontes_novas/comexstat/\n"
                 "aponte a gaveta com --bruto ou com ACERVO=<raiz do acervo>")

    dados = json.load(open(caminho, encoding="utf-8"))["data"]["list"]
    por = {r["coNcm"]: r for r in dados}

    fob = kg = 0
    presentes = 0
    print(f"{'NCM':10s} {'descrição':52s} {'FOB (US$)':>15s} {'massa (kg)':>15s}")
    for c in CODNCM:
        if c in a.sem:
            print(f"{c:10s} {'— excluído por --sem':52s} {'':>15s} {'':>15s}")
            continue
        r = por.get(c)
        if r is None:
            print(f"{c:10s} {'— ausente no bruto do ano':52s} {'':>15s} {'':>15s}")
            continue
        f, k = int(r["metricFOB"]), int(r["metricKG"])
        fob += f
        kg += k
        presentes += 1
        print(f"{c:10s} {(r['ncm'] or '')[:52]:52s} {f:>15,} {k:>15,}")
    print("-" * 96)
    print(f"{'TOTAL':10s} {presentes} códigos presentes"
          f"{fob:>24,} {kg:>15,}")
    print(f"\nFOB  = US$ {fob:,}  ({fob / 1e6:.1f} milhões)")
    print(f"massa = {kg:,} kg  ({kg / 1000:,.0f} toneladas)")
    print(f"preço médio = US$ {fob / kg:.3f}/kg")


if __name__ == "__main__":
    main()
