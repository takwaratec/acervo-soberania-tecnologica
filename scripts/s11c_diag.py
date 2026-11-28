import difflib
import os
import re

RAIZ = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica"
FICHAS = f"{RAIZ}/_privado/fichas/ago_28_Madeira_Tratada_S11c"
FONTES = f"{RAIZ}/_privado/fontes-documentais/ago_28_Madeira_Tratada_S11c"

ALVOS = [
    ("ficha-pi292-89-registro-preservativos-madeira.md", "1989_pi292_preservativos_registro.md",
     "Art. 20. O IBAMA fiscalizará as atividades relacionadas com"),
    ("ficha-pn151-97-ibama-risco-ambiental.md", "1997_pn151_ibama_registro_risco_ambiental.md",
     "Para efeito de registro de produtos Preservativos de Madeira"),
    ("ficha-iema-es-nt01-2023-preservacao-madeira.md", "2023_iema_es_nt01_preservacao_madeira.md",
     "Segundo a Revista da Madeira"),
    ("ficha-abpm-fg4mad-destinacao-residuo-madeira-tratada.md",
     "2016_abpm_fg4mad_destinacao_residuos_madeira_tratada.md", "Resíduos de Madeira Tratada não Podem"),
    ("ficha-ufsm-2025-cca-moiroes-contaminacao-solo.md",
     "2025_ufsm_ciencia_florestal_cca_moiroes_solo.md", "The wood preservative chemical constituents"),
]


def norm(s):
    s = s.replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2014", "-").replace("\u2013", "-").replace("\u00ad", "")
    return re.sub(r"\s+", " ", s).strip()


for ficha, fonte, agulha in ALVOS:
    txt = norm(open(os.path.join(FONTES, fonte), encoding="utf-8").read())
    i = txt.lower().find(agulha.lower()[:40])
    print(f"\n{'=' * 76}\n{ficha[:58]}")
    print(f"agulha: {agulha[:70]}")
    if i < 0:
        print("  AGULHA NAO ENCONTRADA — procurando a palavra-chave")
        kw = agulha.split()[-1].lower()
        j = txt.lower().find(kw)
        print(f"  '{kw}' em {j}: {txt[max(0, j - 120):j + 200] if j >= 0 else 'NADA'}")
        continue
    print(f"EXTRATO ({i}):")
    print("  " + txt[max(0, i - 60):i + 420])
