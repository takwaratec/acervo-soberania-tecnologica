import os

D = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica/_privado/fontes-documentais/ago_28_Madeira_Tratada_S11c"
texto = open(os.path.join(D, "2023_iema_es_nt01_preservacao_madeira.md"), encoding="utf-8").read()
pags = {}
for bloco in texto.split("<!-- PAGE: ")[1:]:
    n, resto = bloco.split(" -->", 1)
    pags[int(n)] = resto

for n in (13, 14):
    print(f"\n{'=' * 70}\nPÁGINA {n}\n{'=' * 70}")
    print(" ".join(pags[n].split())[:2600])
