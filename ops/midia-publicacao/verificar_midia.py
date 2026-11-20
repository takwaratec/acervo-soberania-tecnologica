"""Verificador de mídia servível (portão P7) — sem dependência externa.

Confere, para cada slide de um lote, o que a Graph API exige e o que o corte do
carrossel exige. Roda com a biblioteca padrão; lê dimensões do header JPEG/PNG/SOF
em vez de usar Pillow, porque dependência externa em gate é superfície de falha.

Uso:
    python3 verificar_midia.py --manifesto <manifesto.json> --raiz-public <dir> [--json]
    python3 verificar_midia.py --selftest
"""
from __future__ import annotations

import argparse
import hashlib
import json
import struct
import sys
from fractions import Fraction
from pathlib import Path

LIMITE_BYTES = 8 * 1024 * 1024          # Graph API: foto até 8 MB
PROP_MIN = Fraction(4, 5)               # 0.8  — vertical máximo
PROP_MAX = Fraction(191, 100)           # 1.91 — horizontal máximo
LARGURA_MIN, LARGURA_MAX = 320, 1440
JPEG_MAGIC = b"\xff\xd8\xff"


def dimensoes_jpeg(dados: bytes) -> tuple[int, int] | None:
    """Lê largura/altura de um JPEG percorrendo marcadores SOF.

    Percorre segmentos a partir de 0xFFD8. Um SOFn (0xC0..0xC3, 0xC5..0xC7,
    0xC9..0xCB, 0xCD..0xCF) carrega altura e largura em big-endian.
    Retorna None se não achar — e isso é recusa, não "assume quadrado".
    """
    if not dados.startswith(JPEG_MAGIC):
        return None
    i = 2
    n = len(dados)
    while i < n - 9:
        if dados[i] != 0xFF:
            i += 1
            continue
        marcador = dados[i + 1]
        # marcadores sem payload
        if marcador in (0xD8, 0xD9) or 0xD0 <= marcador <= 0xD7 or marcador == 0x01:
            i += 2
            continue
        if i + 4 > n:
            return None
        tam = struct.unpack(">H", dados[i + 2:i + 4])[0]
        if 0xC0 <= marcador <= 0xCF and marcador not in (0xC4, 0xC8, 0xCC):
            if i + 9 > n:
                return None
            altura, largura = struct.unpack(">HH", dados[i + 5:i + 9])
            return (largura, altura)
        i += 2 + tam
    return None


def dimensoes_png(dados: bytes) -> tuple[int, int] | None:
    """Lê IHDR. PNG não é aceito pela Graph API; serve para recusar com motivo nomeado."""
    if not dados.startswith(b"\x89PNG\r\n\x1a\n") or len(dados) < 24:
        return None
    largura, altura = struct.unpack(">II", dados[16:24])
    return (largura, altura)


def verificar_slide(raiz: Path, slide: dict, primeiro: tuple[int, int] | None) -> list[str]:
    erros: list[str] = []
    nome = slide.get("arquivo") or "<sem-arquivo>"
    p = (raiz / nome).resolve()
    if raiz.resolve() not in p.parents:
        return [f"{nome}: caminho fora da pasta pública"]
    if not p.is_file():
        return [f"{nome}: arquivo não existe em {raiz}"]

    dados = p.read_bytes()

    # formato: a Graph API aceita JPEG para imagem
    dim = dimensoes_jpeg(dados)
    if dim is None:
        alt = dimensoes_png(dados)
        if alt:
            return [f"{nome}: PNG não é aceito pela Graph API para imagem ({alt[0]}x{alt[1]}); converta para JPEG"]
        return [f"{nome}: não é JPEG válido (magic bytes ou header SOF ausente)"]

    largura, altura = dim

    if len(dados) > LIMITE_BYTES:
        erros.append(f"{nome}: {len(dados)} bytes excede o limite de 8 MB ({LIMITE_BYTES})")
    if not (LARGURA_MIN <= largura <= LARGURA_MAX):
        erros.append(f"{nome}: largura {largura}px fora de {LARGURA_MIN}..{LARGURA_MAX}")

    prop = Fraction(largura, altura) if altura else Fraction(0)
    if not (PROP_MIN <= prop <= PROP_MAX):
        erros.append(
            f"{nome}: proporção {float(prop):.3f} ({largura}x{altura}) fora de 0.800 (4:5) .. 1.910 (1.91:1)"
        )

    # o corte do carrossel: todos herdam a proporção do primeiro
    if primeiro and (largura, altura) != primeiro:
        prop1 = Fraction(primeiro[0], primeiro[1])
        erros.append(
            f"{nome}: {largura}x{altura} difere do slide 1 ({primeiro[0]}x{primeiro[1]}). "
            f"O carrossel é cortado pela proporção do primeiro slide — este perderia conteúdo. "
            f"Proporção seria {float(prop):.3f} vs {float(prop1):.3f}."
        )

    sha = slide.get("sha256") or ""
    real = hashlib.sha256(dados).hexdigest()
    if not sha:
        erros.append(f"{nome}: slide sem sha256 no manifesto")
    elif sha.strip().lower() != real:
        erros.append(f"{nome}: sha256 não confere (declarado {sha[:16]}… != real {real[:16]}…)")

    url = slide.get("url") or ""
    if not url.startswith("https://"):
        erros.append(f"{nome}: url pública ausente ou não https")
    elif not url.endswith(nome):
        erros.append(f"{nome}: url não termina no nome do arquivo — ponteiro aponta para outro objeto")

    return erros


def verificar(manifesto: dict, raiz: Path) -> dict:
    slides = manifesto.get("slides") or []
    erros: list[str] = []
    primeiro = None
    if slides:
        p0 = (raiz / (slides[0].get("arquivo") or "")).resolve()
        if p0.is_file():
            primeiro = dimensoes_jpeg(p0.read_bytes())
            if primeiro is None:
                erros.append(f"{slides[0].get('arquivo')}: slide 1 ilegível — sem referência de proporção, o lote inteiro não é verificável")
    for s in slides:
        erros.extend(verificar_slide(raiz, s, primeiro))
    return {
        "lote": manifesto.get("lote"),
        "slides": len(slides),
        "padrao_do_carrossel": f"{primeiro[0]}x{primeiro[1]}" if primeiro else None,
        "ok": not erros,
        "erros": erros,
    }


def _jpeg(largura: int, altura: int) -> bytes:
    """JPEG mínimo válido com SOF0 — bytes suficientes para o parser, sem imagem real."""
    sof = b"\xff\xc0" + struct.pack(">H", 17) + bytes([8]) + struct.pack(">HH", altura, largura) + bytes([3]) + b"\x01\x11\x00" + b"\x02\x11\x01" + b"\x03\x11\x01"
    return b"\xff\xd8" + b"\xff\xe0" + struct.pack(">H", 16) + b"JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00" + sof + b"\xff\xd9"


def selftest() -> int:
    import tempfile

    falhas: list[str] = []
    with tempfile.TemporaryDirectory() as td:
        raiz = Path(td)
        # lote bom: 1080x1350 (4:5) nos três slides
        bom = []
        for i in (1, 2, 3):
            b = _jpeg(1080, 1350)
            (raiz / f"0{i}.jpg").write_bytes(b)
            bom.append({"arquivo": f"0{i}.jpg", "sha256": hashlib.sha256(b).hexdigest(),
                        "url": f"https://exemplo.workers.dev/midia/L/0{i}.jpg"})
        r = verificar({"lote": "BOM", "slides": bom}, raiz)
        if not r["ok"]:
            falhas.append(f"lote bom foi recusado: {r['erros']}")

        # controle negativo 1: slide com outra proporção (1080x1080)
        b = _jpeg(1080, 1080)
        (raiz / "quadrado.jpg").write_bytes(b)
        q = dict(bom[1]); q["arquivo"] = "quadrado.jpg"; q["sha256"] = hashlib.sha256(b).hexdigest()
        q["url"] = "https://exemplo.workers.dev/midia/L/quadrado.jpg"
        r2 = verificar({"lote": "Q", "slides": [bom[0], q, bom[2]]}, raiz)
        if not any("difere do slide 1" in e for e in r2["erros"]):
            falhas.append("controle negativo ausente: proporção divergente não foi pega")

        # controle negativo 2: sha errado
        bad = dict(bom[2]); bad["sha256"] = "0" * 64
        r3 = verificar({"lote": "S", "slides": [bom[0], bad]}, raiz)
        if not any("sha256 não confere" in e for e in r3["erros"]):
            falhas.append("controle negativo ausente: sha divergente não foi pego")

        # controle negativo 3: proporção fora da faixa, mas IGUAL ao slide 1.
        # Sem este caso, desligar PROP_MIN/PROP_MAX não quebra nada e o selftest
        # continua PASS com o gate de proporção aberto — medido em 2026-11-20.
        b = _jpeg(1080, 2400)   # 0.45 — vertical muito alongado
        (raiz / "alongado.jpg").write_bytes(b)
        a1 = dict(bom[1]); a1["arquivo"] = "alongado.jpg"; a1["sha256"] = hashlib.sha256(b).hexdigest()
        a1["url"] = "https://exemplo.workers.dev/midia/L/alongado.jpg"
        r_fora = verificar({"lote": "F", "slides": [a1]}, raiz)
        if not any("fora de 0.800" in e for e in r_fora["erros"]):
            falhas.append("controle negativo ausente: proporção fora da faixa (mas igual ao slide 1) não foi pega")

        # controle negativo 4: largura fora da faixa, slides todos iguais
        b = _jpeg(200, 250)     # proporção 0.8 válida, largura 200 < 320
        (raiz / "estreito.jpg").write_bytes(b)
        e1 = dict(bom[1]); e1["arquivo"] = "estreito.jpg"; e1["sha256"] = hashlib.sha256(b).hexdigest()
        e1["url"] = "https://exemplo.workers.dev/midia/L/estreito.jpg"
        r_larg = verificar({"lote": "E", "slides": [e1]}, raiz)
        if not any("largura 200px fora" in e for e in r_larg["erros"]):
            falhas.append("controle negativo ausente: largura fora da faixa não foi pega")

        # controle negativo 5: png
        png = b"\x89PNG\r\n\x1a\n" + b"\x00\x00\x00\x0dIHDR" + struct.pack(">II", 1080, 1350) + b"\x08\x06\x00\x00\x00"
        (raiz / "x.png").write_bytes(png)
        r4 = verificar({"lote": "P", "slides": [{"arquivo": "x.png", "sha256": hashlib.sha256(png).hexdigest(),
                                                 "url": "https://e/x.png"}]}, raiz)
        if not any("PNG não é aceito" in e for e in r4["erros"]):
            falhas.append("controle negativo ausente: PNG passou")

        # controle negativo 4: arquivo ausente
        r5 = verificar({"lote": "A", "slides": [{"arquivo": "nao-existe.jpg", "sha256": "x", "url": "https://e/nao-existe.jpg"}]}, raiz)
        if not any("não existe" in e for e in r5["erros"]):
            falhas.append("controle negativo ausente: ausente passou")

    for f in falhas:
        print(f"FALHA: {f}")
    print(json.dumps({"selftest": "PASS" if not falhas else "FAIL", "controles": 6}, ensure_ascii=False))
    return 0 if not falhas else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Portão P7 — mídia servível.")
    ap.add_argument("--manifesto")
    ap.add_argument("--raiz-public", default=".")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if not a.manifesto:
        ap.error("--manifesto e obrigatorio (ou use --selftest)")
    m = json.loads(Path(a.manifesto).read_text(encoding="utf-8"))
    r = verificar(m, Path(a.raiz_public))
    print(json.dumps(r, ensure_ascii=False, indent=1))
    return 0 if r["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
