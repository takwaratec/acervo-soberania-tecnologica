#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deriva os números didáticos da aba 'Espécies' a partir dos valores de tabela.

Toda aritmética da aba passa por aqui: nada é digitado à mão no texto.
Uso: python3 derivar_numeros.py  → imprime JSON com os valores e as equivalências.
"""
import json

G = 9.80665          # aceleração da gravidade (m/s²)
KGF_CM2_POR_MPA = 10.197162  # 1 MPa = 1 N/mm² = 10,1972 kgf/cm²


def tf(kgf):
    return kgf / 1000.0


def cm2(mm2):
    return mm2 / 100.0


# Áreas de parede medidas nas tabelas dos próprios artigos
AREAS = {
    "Madake": 739.0,      # Drury, Tabela 2 (média dos 6 corpos)
    "Moso": 1605.0,
    "Guadua": 1728.0,
    "Tali": 1939.0,
    "BlackJava": 1511.0,
}

# Compressão paralela média — Drury et al. 2023, Tabela 2 (recalculado das 30 linhas)
DRURY = {"Madake": 88.90, "Moso": 69.88, "Guadua": 60.73, "Tali": 59.08, "BlackJava": 54.62}

# Panti et al. 2024, Tabela 6
PANTI = {
    "B. blumeana": {"n": 93, "cov": 0.19, "p5": 48.53, "k": 1.94, "fck": 46.63, "media": 70.67},
    "B. vulgaris": {"n": 36, "cov": 0.21, "p5": 43.43, "k": 2.01, "fck": 40.35, "media": 61.16},
    "D. asper":    {"n": 36, "cov": 0.20, "p5": 43.15, "k": 2.01, "fck": 40.21, "media": 59.49},
    "G. angustifolia": {"n": 30, "cov": 0.19, "p5": 39.82, "k": 2.01, "fck": 36.99, "media": 57.53},
}

# Lorenzo et al. 2020, Tabela 3
LORENZO = {
    "Moso":    {"dens": 684, "fc": 54, "E": 11930, "fv": 16, "fck": 40, "Ek": 7529},
    "Guadua":  {"dens": 730, "fc": 58, "E": 18480, "fv": 12, "fck": 38, "Ek": 12502},
    "Oldhamii": {"dens": 734, "fc": 68, "E": 20683, "fv": 13, "fck": 50, "Ek": 7604},
}

# Franck et al. 2026, Tabelas 4 e 8 (colmo inteiro, internó)
FRANCK = {
    "Moso":   {"fc": 66.72, "FkN": 143.39, "MOE": 10.45, "fm": 76.97, "Fm": 6.49, "dmax": 172.79},
    "Guadua": {"fc": 66.35, "FkN": 171.20, "MOE": 19.76, "fm": 56.23, "Fm": 5.05, "dmax": 57.83},
}

# Rodríguez-Sotelo et al. 2023, Tabelas 4, 5 e 6
RODRIGUEZ = {
    "G. lynnclarkiae": {"MoR": 21.01, "ELP": 15.76, "MoE": 773.31, "MoR_basal": 18.73, "MoR_cepa": 23.65},
    "G. weberbaueri":  {"MoR": 17.70, "ELP": 13.95, "MoE": 663.78, "MoR_basal": 13.51, "MoR_cepa": 25.57},
    "G. superba":      {"MoR": 71.20, "ELP": 56.22, "MoE": 5931.06, "MoR_basal": 84.49, "MoR_cepa": 55.15},
}
RODRIGUEZ_COMP = {"MoE": 11454.35, "MoR": 39.50}
RODRIGUEZ_CORTE = {"lynnclarkiae": (5.25, 5.18), "weberbaueri": (9.01, 9.85), "superba": (6.12, 5.69)}
RODRIGUEZ_CPERP = {"superba": (19.33, 13.71, 10.15), "lynnclarkiae_min": (7.79, 6.06)}


def carga_por_colmo(fc_mpa, area_mm2):
    """Carga axial de pico num colmo de seção conhecida."""
    N = fc_mpa * area_mm2
    return {"kN": round(N / 1000, 1), "tf": round(N / G / 1000, 2)}


def main():
    out = {"drury": {}, "panti": {}, "franck": {}, "controles": {}}

    for esp, fc in DRURY.items():
        c = carga_por_colmo(fc, AREAS[esp])
        out["drury"][esp] = {
            "fc_MPa": fc,
            "kgf_cm2": round(fc * KGF_CM2_POR_MPA),
            "area_mm2": AREAS[esp],
            "carga": c,
        }

    for esp, v in PANTI.items():
        c = carga_por_colmo(v["fck"], AREAS["Guadua"])
        out["panti"][esp] = {
            "fck_MPa": v["fck"],
            "kgf_cm2": round(v["fck"] * KGF_CM2_POR_MPA),
            "fator_media_para_fck": round(v["media"] / v["fck"], 2),
            "carga_em_colmo_80": c,
        }

    for esp, v in FRANCK.items():
        out["franck"][esp] = {
            "FkN": v["FkN"],
            "tf": round(v["FkN"] / G, 2),
            "fc_MPa": v["fc"],
            "MOE_GPa": v["MOE"],
            "fm_MPa": v["fm"],
            "fletor_tf": round(v["Fm"] / G, 2),
            "deflexao_mm": v["dmax"],
        }
    out["franck"]["razao_MOE"] = round(FRANCK["Guadua"]["MOE"] / FRANCK["Moso"]["MOE"], 2)
    out["franck"]["razao_fletor"] = round(FRANCK["Moso"]["fm"] / FRANCK["Guadua"]["fm"], 2)
    out["franck"]["razao_deflexao"] = round(FRANCK["Moso"]["dmax"] / FRANCK["Guadua"]["dmax"], 2)

    # Reduções sucessivas: média → característico → admissível
    m, ck, adm = 57.53, 36.99, 17.80
    out["controles"] = {
        "reducao_media_caracteristico": round(m / ck, 2),
        "reducao_caracteristico_admissivel": round(ck / adm, 2),
        "reducao_media_admissivel": round(m / adm, 2),
        "carga_admissivel_colmo_80": carga_por_colmo(adm, AREAS["Guadua"]),
        "carga_media_colmo_80": carga_por_colmo(m, AREAS["Guadua"]),
        "carga_caract_colmo_80": carga_por_colmo(ck, AREAS["Guadua"]),
        "kgf_cm2_por_mpa": KGF_CM2_POR_MPA,
        "mpa_200_em_kgf_cm2": round(200 * KGF_CM2_POR_MPA),
        "mpa_200_em_tf_cm2": round(200 * KGF_CM2_POR_MPA / 1000, 2),
    }

    # Controle: peso de 1,2 t sobre 2 cm²
    out["controles"]["carro_1200kg_2cm2_kgf_cm2"] = round(1200 / 2)

    print(json.dumps(out, indent=1, ensure_ascii=False))
    return out


if __name__ == "__main__":
    main()
