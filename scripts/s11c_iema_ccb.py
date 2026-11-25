import os
import re

D = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica/_privado/fontes-documentais/ago_28_Madeira_Tratada_S11c"
arq = os.path.join(D, "2023_iema_es_nt01_preservacao_madeira.md")
texto = open(arq, encoding="utf-8").read()


def paginas(t):
    out = []
    for bloco in t.split("<!-- PAGE: ")[1:]:
        n, resto = bloco.split(" -->", 1)
        out.append((int(n), resto))
    return out


print("=== ocorrencias de CCB no IEMA ===")
total = 0
for n, pag in paginas(texto):
    for m in re.finditer(r"CCB", pag):
        total += 1
        ini = max(0, m.start() - 240)
        fim = min(len(pag), m.end() + 300)
        print(f"\n[p.{n}] …{' '.join(pag[ini:fim].split())}…")
print(f"\nTOTAL de ocorrencias de CCB: {total}")

print("\n=== 'informa' + negativa ===")
for n, pag in paginas(texto):
    for m in re.finditer(r"[Nn]ão (existem|há|se tem)[^.]{0,120}", pag):
        print(f"[p.{n}] {' '.join(m.group(0).split())}")
