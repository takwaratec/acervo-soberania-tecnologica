import os
import re

D = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica/_privado/fontes-documentais/ago_28_Madeira_Tratada_S11c"

ALVOS = {
    "1989_pi292_preservativos_registro.md": [
        r"[Ff]iscalizar", r"Art\. 3", r"Art\. 20", r"Art\. 21", r"registro junto ao Instituto",
        r"relat[óo]rios semestrais",
    ],
    "1997_pn151_ibama_registro_risco_ambiental.md": [
        r"Risco .{0,3}mbiental", r"Art\. 1", r"Art\. 4",
    ],
    "2023_iema_es_nt01_preservacao_madeira.md": [
        r"80\s*%", r"sete registros", r"[Nn]ão existem muitas informa",
        r"Classe I", r"100\s*%", r"madeira tratada n[ãa]o podem",
        r"fiscaliza", r"aterro industrial",
    ],
    "2016_abpm_fg4mad_destinacao_residuos_madeira_tratada.md": [
        r"n[ãa]o Podem", r"[Qq]ueima a c[ée]u aberto", r"fog[õo]es",
        r"aterro", r"CONAMA 307",
    ],
    "2025_ufsm_ciencia_florestal_cca_moiroes_solo.md": [
        r"55[,.]0", r"129[,.]2", r"32[,.]3", r"420", r"[Aa]bsor",
    ],
}


def paginas(texto):
    """Devolve [(pagina, trecho_da_pagina)] a partir dos marcadores."""
    out = []
    for bloco in texto.split("<!-- PAGE: ")[1:]:
        n, resto = bloco.split(" -->", 1)
        out.append((int(n), resto))
    return out


for arq, pats in ALVOS.items():
    caminho = os.path.join(D, arq)
    texto = open(caminho, encoding="utf-8").read()
    print(f"\n{'=' * 78}\n{arq}\n{'=' * 78}")
    for pat in pats:
        achou = False
        for n, pag in paginas(texto):
            for m in re.finditer(pat, pag):
                ini = max(0, m.start() - 190)
                fim = min(len(pag), m.end() + 260)
                trecho = " ".join(pag[ini:fim].split())
                print(f"\n  [p.{n}] /{pat}/")
                print(f"    …{trecho}…")
                achou = True
                break
            if achou:
                break
        if not achou:
            print(f"\n  [NAO ENCONTRADO] /{pat}/")
