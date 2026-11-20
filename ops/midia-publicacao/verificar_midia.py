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
import re
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


# Leitor com dois modos: disco (produção) e memória (selftest em sandbox read-only).
_MEM_B: dict[str, bytes] | None = None


def _bytes_de(p: Path) -> bytes | None:
    if _MEM_B is not None:
        return _MEM_B.get(str(p))
    return p.read_bytes() if p.is_file() else None


def verificar_slide(raiz: Path, slide: dict, primeiro: tuple[int, int] | None) -> list[str]:
    erros: list[str] = []
    nome = slide.get("arquivo") or "<sem-arquivo>"
    p = (raiz / nome).resolve()
    if raiz.resolve() not in p.parents:
        return [f"{nome}: caminho fora da pasta pública"]
    dados = _bytes_de(p)
    if dados is None:
        return [f"{nome}: arquivo não existe em {raiz}"]

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


def verificar_ponteiro(manifesto: dict) -> dict:
    """Modo --sem-bytes: o binário NÃO está no repositório (decisão do soberano:
    arte não entra no Git). Valida o que o manifesto pode provar sozinho —
    sha256 presente e com forma de sha256, URL https terminando no arquivo,
    e dimensão declarada que permita conferir o corte do carrossel.

    Limite declarado: sem os bytes, NÃO se prova que o arquivo remoto tem
    aquelas dimensões nem aquele hash. Prova-se apenas que o ponteiro é
    internamente coerente. Quem prova as dimensões é o verificador com bytes.
    """
    slides = manifesto.get("slides") or []
    erros: list[str] = []
    primeiro = None
    if slides:
        primeiro = slides[0].get("dimensao")
    for s in slides:
        nome = s.get("arquivo") or "<sem-arquivo>"
        sha = (s.get("sha256") or "").strip().lower()
        if not re.fullmatch(r"[0-9a-f]{64}", sha):
            erros.append(f"{nome}: sha256 ausente ou não é sha256 (64 hex)")
        url = s.get("url") or ""
        if not url.startswith("https://"):
            erros.append(f"{nome}: url pública ausente ou não https")
        elif not url.endswith(nome):
            erros.append(f"{nome}: url não termina no nome do arquivo — ponteiro aponta para outro objeto")
        dim = s.get("dimensao") or ""
        if not re.fullmatch(r"\d{2,5}x\d{2,5}", dim):
            erros.append(f"{nome}: 'dimensao' ausente ou mal formada (esperado LARGURAxALTURA)")
            continue
        largura, altura = (int(x) for x in dim.split("x"))
        if not (LARGURA_MIN <= largura <= LARGURA_MAX):
            erros.append(f"{nome}: largura {largura}px fora de {LARGURA_MIN}..{LARGURA_MAX}")
        prop = Fraction(largura, altura) if altura else Fraction(0)
        if not (PROP_MIN <= prop <= PROP_MAX):
            erros.append(f"{nome}: proporção {float(prop):.3f} fora de 0.800 .. 1.910")
        if primeiro and dim != primeiro:
            erros.append(f"{nome}: {dim} difere do slide 1 ({primeiro}) — o carrossel é cortado pela proporção do primeiro")
    return {"lote": manifesto.get("lote"), "slides": len(slides), "modo": "SEM_BYTES",
            "padrao_do_carrossel": primeiro, "ok": not erros, "erros": erros,
            "limite": "sem os bytes o manifesto prova coerência do ponteiro, NÃO que o objeto remoto tem essas dimensões"}


def verificar(manifesto: dict, raiz: Path) -> dict:
    slides = manifesto.get("slides") or []
    erros: list[str] = []
    primeiro = None
    if slides:
        p0 = (raiz / (slides[0].get("arquivo") or "")).resolve()
        b0 = _bytes_de(p0)
        if b0 is not None:
            primeiro = dimensoes_jpeg(b0)
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
    """Controle negativo duplo, em memória — roda em sandbox read-only.

    Um selftest que exige diretório gravável não pode ser executado por quem audita
    (defeito medido na auditoria TECO de 2026-11-20, Q6 não executável).
    """
    global _MEM_B
    falhas: list[str] = []
    raiz = Path("/mem")

    def _b(largura, altura):
        return _jpeg(largura, altura)

    bom = []
    memoria = {}
    for i in (1, 2, 3):
        b = _b(1080, 1350)
        memoria[f"/mem/0{i}.jpg"] = b
        bom.append({"arquivo": f"0{i}.jpg", "sha256": hashlib.sha256(b).hexdigest(),
                    "url": f"https://exemplo.workers.dev/midia/L/0{i}.jpg"})

    _MEM_B = memoria
    try:
        r = verificar({"lote": "BOM", "slides": bom}, raiz)
        if not r["ok"]:
            falhas.append(f"controle positivo falhou: {r['erros']}")

        # 1. proporção divergente do slide 1 (o corte do carrossel)
        b = _b(1080, 1080)
        memoria["/mem/quadrado.jpg"] = b
        q = dict(bom[1]); q.update(arquivo="quadrado.jpg", sha256=hashlib.sha256(b).hexdigest(),
                                   url="https://e/midia/L/quadrado.jpg")
        r = verificar({"lote": "Q", "slides": [bom[0], q, bom[2]]}, raiz)
        if not any("difere do slide 1" in e for e in r["erros"]):
            falhas.append("1: proporção divergente não foi pega")

        # 2. proporção fora da faixa, mas IGUAL ao slide 1 (pega limites desligados)
        b = _b(1080, 2400)
        memoria["/mem/alongado.jpg"] = b
        a1 = dict(bom[1]); a1.update(arquivo="alongado.jpg", sha256=hashlib.sha256(b).hexdigest(),
                                     url="https://e/midia/L/alongado.jpg")
        r = verificar({"lote": "F", "slides": [a1]}, raiz)
        if not any("fora de 0.800" in e for e in r["erros"]):
            falhas.append("2: proporção fora da faixa não foi pega")

        # 3. largura fora da faixa, slides iguais
        b = _b(200, 250)
        memoria["/mem/estreito.jpg"] = b
        e1 = dict(bom[1]); e1.update(arquivo="estreito.jpg", sha256=hashlib.sha256(b).hexdigest(),
                                     url="https://e/midia/L/estreito.jpg")
        r = verificar({"lote": "E", "slides": [e1]}, raiz)
        if not any("largura 200px fora" in e for e in r["erros"]):
            falhas.append("3: largura fora da faixa não foi pega")

        # 4. sha divergente
        bad = dict(bom[2]); bad["sha256"] = "0" * 64
        r = verificar({"lote": "S", "slides": [bom[0], bad]}, raiz)
        if not any("sha256 não confere" in e for e in r["erros"]):
            falhas.append("4: sha divergente não foi pego")

        # 5. PNG (a Graph API aceita JPEG para imagem)
        png = (b"\x89PNG\r\n\x1a\n" + b"\x00\x00\x00\x0dIHDR"
               + struct.pack(">II", 1080, 1350) + b"\x08\x06\x00\x00\x00")
        memoria["/mem/x.png"] = png
        r = verificar({"lote": "P", "slides": [{"arquivo": "x.png",
                      "sha256": hashlib.sha256(png).hexdigest(), "url": "https://e/x.png"}]}, raiz)
        if not any("PNG não é aceito" in e for e in r["erros"]):
            falhas.append("5: PNG não foi recusado")

        # 6. arquivo ausente
        r = verificar({"lote": "A", "slides": [{"arquivo": "nao-existe.jpg",
                      "sha256": "x", "url": "https://e/nao-existe.jpg"}]}, raiz)
        if not any("não existe" in e for e in r["erros"]):
            falhas.append("6: arquivo ausente não foi recusado")

        # 7. modo PONTEIRO bom
        ptr = [{"arquivo": "1.jpg", "sha256": "a" * 64, "url": "https://x/1.jpg", "dimensao": "1080x1350"},
               {"arquivo": "2.jpg", "sha256": "b" * 64, "url": "https://x/2.jpg", "dimensao": "1080x1350"}]
        if not verificar_ponteiro({"lote": "P", "slides": ptr})["ok"]:
            falhas.append("7: ponteiro correto recusado")

        # 8. ponteiro com dimensão divergente
        ruim = [ptr[0], {**ptr[1], "dimensao": "1080x1080"}]
        if not any("difere do slide 1" in e for e in verificar_ponteiro({"lote": "P", "slides": ruim})["erros"]):
            falhas.append("8: ponteiro com dimensão divergente não foi pego")

        # 9. ponteiro sem sha256
        if not any("sha256 ausente" in e for e in verificar_ponteiro(
                {"lote": "P", "slides": [{"arquivo": "1.jpg", "sha256": "", "url": "https://x/1.jpg",
                                          "dimensao": "1080x1350"}]})["erros"]):
            falhas.append("9: ponteiro sem sha256 não foi pego")

        # 10. URL apontando para outro objeto
        if not any("termina no nome" in e for e in verificar_ponteiro(
                {"lote": "P", "slides": [{"arquivo": "1.jpg", "sha256": "a" * 64,
                                          "url": "https://x/outro.jpg", "dimensao": "1080x1350"}]})["erros"]):
            falhas.append("10: URL apontando para outro objeto não foi pega")
    finally:
        _MEM_B = None

    for f in falhas:
        print(f"FALHA: {f}")
    print(json.dumps({"selftest": "PASS" if not falhas else "FAIL", "modo": "EM_MEMORIA",
                      "controles_negativos": 10, "falhas": len(falhas)}, ensure_ascii=False))
    return 0 if not falhas else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Portão P7 — mídia servível.")
    ap.add_argument("--manifesto")
    ap.add_argument("--raiz-public", default=".")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--sem-bytes", action="store_true", dest="sem_bytes",
                    help="valida so o ponteiro do manifesto (binario fora do repositorio)")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if not a.manifesto:
        ap.error("--manifesto e obrigatorio (ou use --selftest)")
    m = json.loads(Path(a.manifesto).read_text(encoding="utf-8"))
    r = verificar_ponteiro(m) if a.sem_bytes else verificar(m, Path(a.raiz_public))
    print(json.dumps(r, ensure_ascii=False, indent=1))
    return 0 if r["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
