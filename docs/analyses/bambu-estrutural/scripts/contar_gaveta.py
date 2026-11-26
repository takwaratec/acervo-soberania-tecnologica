#!/usr/bin/env python3
"""Contagem reproduzivel da gaveta bambu-estrutural por tipo_documental.

Uso:  python3 contar_gaveta.py [<repo>] [<gaveta>]
Saida: total de arquivos .md, contagem por tipo, e a lista arquivo -> tipo.

Existe porque um auditor cobrou, com razao, que o numero publicado nao era
reproduzivel a partir do comando que o acompanhava.
"""
import pathlib
import re
import sys
from collections import Counter

repo = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
gaveta = sys.argv[2] if len(sys.argv) > 2 else "docs/analyses/bambu-estrutural"
p = repo / gaveta

linhas = []
for m in sorted(p.glob("*.md")):
    texto = m.read_text(encoding="utf-8", errors="replace")
    fm = re.match(r"^---\n(.*?)\n---\n", texto, re.S)
    tipo = None
    if fm:
        achado = re.search(r"^tipo_documental:\s*[\"']?([^\"'\n]+)", fm.group(1), re.M)
        tipo = achado.group(1).strip() if achado else None
    linhas.append((m.name, tipo or "(sem front matter)"))

contagem = Counter(t for _, t in linhas)
fichas = sum(v for k, v in contagem.items() if k.startswith("ficha-"))

saida = [f"gaveta={gaveta} arquivos_md={len(linhas)} fichas={fichas} outros={len(linhas) - fichas}"]
for tipo, n in sorted(contagem.items(), key=lambda x: -x[1]):
    saida.append(f"  {n:3}  {tipo}")
saida.append("")
for nome, tipo in linhas:
    saida.append(f"  {tipo:38} {nome}")


# ---- particao por objeto (regra explicita, aplicada ao NOME do arquivo) ----
INSTRUMENTOS = {"ROTEIRO_GAVETAS_BAMBU_20261126.md",
                "INVENTARIO_CUSTODIA_BAMBU_20261126.md",
                "PLANO_FRENTES_GAVETAS_BAMBU_20261126.md"}

def familia(nome):
    s = nome.lower()
    if nome in INSTRUMENTOS:
        return "instrumento-da-frente (fora da particao)"
    if nome == "index.md" or s.startswith("00") or s.startswith(("estado-da-arte", "mapa-de-",
        "agenda-de-pesquisa", "maturidade")):
        return "sintese-e-registro"
    if "fitorremedi" in s:
        return "fitorremediacao"
    if re.search(r"flora|fenolog|regenera|clonal|minijardim|landsat", s):
        return "biologia"
    if re.search(r"coleobroca|antimicrobiano|dinoderus|patologias", s):
        return "fitossanidade"
    if re.search(r"pirolenhos|licor", s):
        return "pirolenhoso"
    if re.search(r"nativos-cadeia|materia-prima-mercado", s):
        return "cadeia"
    return "estrutural"

part = Counter(familia(n) for n, _ in linhas)
saida.append("")
saida.append("particao por objeto (regra: familia() neste script):")
for fam, n in sorted(part.items(), key=lambda x: -x[1]):
    saida.append(f"  {n:3}  {fam}")

sys.stdout.write("\n".join(saida) + "\n")
