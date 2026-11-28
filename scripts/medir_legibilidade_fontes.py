# -*- coding: utf-8 -*-
"""Mede legibilidade das fontes do manifesto: hash prova byte, não prova que há texto."""
import json
import os
import re

R = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica"
MAN = f"{R}/docs/analyses/cobre/AUDITORIA_SOL_COBRE_MANIFEST_R1_61ac1152.json"

BLOQUEIO = re.compile(
    r"just a moment|checking your browser|access denied|403 forbidden|captcha|"
    r"attention required|enable javascript|cloudflare|are you a robot|"
    r"p[áa]gina n[ãa]o encontrada|site em manuten[çc][ãa]o|not found", re.I)

man = json.load(open(MAN, encoding="utf-8"))
fontes = man.get("fontes") or man.get("arquivos") or []
print(f"manifesto: {os.path.basename(MAN)}")
print(f"fontes listadas: {len(fontes)}\n")

legiveis, bloqueadas, ausentes, ilegiveis = [], [], [], []
for f in fontes:
    caminho = f.get("path") or f.get("caminho") or f.get("arquivo") or ""
    p = os.path.join(R, caminho)
    if not os.path.exists(p):
        ausentes.append((caminho, "arquivo não existe na árvore"))
        continue
    tam = os.path.getsize(p)
    if tam == 0:
        ausentes.append((caminho, "arquivo vazio (0 byte)"))
        continue
    if p.endswith((".pdf",)):
        ok, motivo = (tam > 20_000), f"PDF de {tam:,} B"
    else:
        t = open(p, encoding="utf-8", errors="replace").read()
        util = len(re.sub(r"\s+", " ", t).strip())
        # JSON de manifesto descreve bloqueios nos próprios campos: detectar bloqueio ali é
        # falso positivo — o objeto é o metadado, não a página.
        if p.endswith(".json"):
            ok, motivo = (util > 500), f"manifesto JSON, {util:,} chars"
        elif BLOQUEIO.search(t[:4000]):
            ok, motivo = False, f"página de bloqueio/erro detectada ({tam:,} B, {util} chars úteis)"
        elif util < 500:
            ok, motivo = False, f"texto útil muito curto ({util} chars)"
        else:
            ok, motivo = True, f"{util:,} chars úteis"
    (legiveis if ok else ilegiveis).append((caminho, motivo))

print(f"LEGÍVEIS:  {len(legiveis)}")
for c, m in legiveis:
    print(f"   ok  {c[:78]:80s} {m}")
print(f"\nBLOQUEADAS/ILEGÍVEIS: {len(ilegiveis)}")
for c, m in ilegiveis:
    print(f"   !!  {c[:78]:80s} {m}")
if ausentes:
    print(f"\nAUSENTES: {len(ausentes)}")
    for c, m in ausentes:
        print(f"   --  {c[:78]:80s} {m}")

print(f"\nRESUMO: {len(legiveis)} legíveis · {len(ilegiveis)} bloqueadas · {len(ausentes)} ausentes "
      f"de {len(fontes)}")
