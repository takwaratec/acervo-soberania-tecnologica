#!/usr/bin/env python3
"""Compara, para cada CONFERE, o que o artigo afirma e o que a pagina diz."""
import importlib.util
import json
import os
import re

D = os.path.dirname(os.path.abspath(__file__))
G = os.path.join(D, "ops/command-center/metodo")
spec = importlib.util.spec_from_file_location("g", os.path.join(G, "gate_fidelidade_fonte.py"))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
spec2 = importlib.util.spec_from_file_location("rodar", os.path.join(D, "rodar.py"))
rodar = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(rodar)

reg = [json.loads(l) for l in open(os.path.join(D, "registro.jsonl"))]
cache = {}


def fonte_de(c):
    for rel in rodar.arquivos_de(c):
        p = os.path.join(rodar.BORO, rel)
        if os.path.exists(p):
            if p not in cache:
                cache[p] = rodar.texto_com_paginas(p)
            return cache[p]
    return None


def norm(v):
    return re.sub(r"[^\d.,]", "", v).replace(",", ".")


saida = []
for x in [y for y in reg if y["veredito"] == "CONFERE"]:
    txt, trecho = None, ""
    for c in x["citacoes"]:
        t = fonte_de(c)
        if t:
            txt = t
            break
    if txt and x["pagina"]:
        pg = mod.dividir_paginas(txt).get(x["pagina"], "")
        for m in rodar.RE_NUM.finditer(pg):
            if norm(m.group(0)) == norm(x["valor"]):
                trecho = re.sub(r"\s+", " ", pg[max(0, m.start() - 200):m.start() + 200])
                break
    saida.append(dict(id=x["id"], valor=x["valor"], unidade=x["unidade"],
                      cit=x["citacoes"], pagina=x["pagina"],
                      afirma=x["contexto"][:150], fonte=trecho[:330]))
json.dump(saida, open(os.path.join(D, "conf53.json"), "w"), ensure_ascii=False, indent=1)
print(len(saida))
