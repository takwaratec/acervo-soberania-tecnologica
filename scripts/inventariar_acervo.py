#!/usr/bin/env python3
"""Gera inventário reproduzível do conteúdo Markdown público do Acervo."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path


DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.I)
ISBN_RE = re.compile(r"\bISBN(?:-1[03])?\s*[:#]?\s*[0-9Xx -]{10,20}\b", re.I)
ISSN_RE = re.compile(r"\bISSN\s*[:#]?\s*\d{4}-\d{3}[\dXx]\b", re.I)
HANDLE_RE = re.compile(r"https?://hdl\.handle\.net/[^\s)>]+", re.I)
SECTION_RE = re.compile(r"^##\s+([1-8])(?:\.|\s|—|-)", re.M)
STATUS_RE = re.compile(r"^(?:status|estado_documental):\s*[\"']?([^\n\"']+)", re.M | re.I)
TYPE_RE = re.compile(r"^tipo_documental:\s*[\"']?([^\n\"']+)", re.M | re.I)
EXCLUDED_PUBLIC_PREFIXES = (
    Path("cadernos-revisao-ecologica"),
    Path("analyses/tecnologia-takwara"),
)


def is_public_build_document(path: Path, docs: Path) -> bool:
    relative = path.relative_to(docs)
    return not any(
        relative == prefix or prefix in relative.parents
        for prefix in EXCLUDED_PUBLIC_PREFIXES
    )


def relative_group(path: Path, docs: Path) -> str:
    relative = path.relative_to(docs)
    return relative.parts[0] if len(relative.parts) > 1 else "raiz-docs"


def inspect_markdown(path: Path, docs: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    sections = sorted(set(SECTION_RE.findall(text)))
    identifiers = sorted(set(DOI_RE.findall(text)))
    has_identifier = bool(
        identifiers or ISBN_RE.search(text) or ISSN_RE.search(text) or HANDLE_RE.search(text)
    )
    status_match = STATUS_RE.search(text[:2500])
    type_match = TYPE_RE.search(text[:2500])
    return {
        "path": str(path.relative_to(docs.parent)),
        "group": relative_group(path, docs),
        "bytes": path.stat().st_size,
        "sections": sections,
        "has_sections_1_to_8": sections == list("12345678"),
        "has_public_identifier": has_identifier,
        "dois": identifiers,
        "declared_status": status_match.group(1).strip() if status_match else "não declarado",
        "declared_type": type_match.group(1).strip() if type_match else "não declarado",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("repository", type=Path)
    parser.add_argument("--markdown", type=Path, required=True)
    parser.add_argument("--json", type=Path, required=True)
    args = parser.parse_args()

    repository = args.repository.resolve()
    docs = repository / "docs"
    records = [
        inspect_markdown(path, docs)
        for path in sorted(docs.rglob("*.md"))
        if is_public_build_document(path, docs)
    ]
    group_counts = Counter(record["group"] for record in records)
    status_counts = Counter(record["declared_status"] for record in records)
    type_counts = Counter(record["declared_type"] for record in records)
    structured = [record for record in records if record["has_sections_1_to_8"]]
    identified = [record for record in records if record["has_public_identifier"]]
    analysis_records = [
        record for record in records if record["group"] == "analyses"
    ]
    analysis_structured = [record for record in analysis_records if record["has_sections_1_to_8"]]
    analysis_identified = [record for record in analysis_records if record["has_public_identifier"]]

    payload = {
        "generated_on": str(date.today()),
        "repository": str(repository),
        "definitions": {
            "public_markdown": "arquivo .md sob docs/ incluído no build público",
            "structured_1_to_8": "arquivo com os oito títulos numerados detectáveis",
            "identified": "arquivo contendo DOI, ISBN, ISSN ou Handle detectável",
            "analysis_document": "arquivo sob docs/analyses, sem presumir que seja ficha científica",
        },
        "counts": {
            "public_markdown": len(records),
            "analysis_documents": len(analysis_records),
            "structured_1_to_8_all_docs": len(structured),
            "structured_1_to_8_analysis": len(analysis_structured),
            "identified_all_docs": len(identified),
            "identified_analysis": len(analysis_identified),
        },
        "by_group": dict(sorted(group_counts.items())),
        "by_declared_status": dict(sorted(status_counts.items())),
        "by_declared_type": dict(sorted(type_counts.items())),
        "records": records,
    }
    args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        f"# Inventário reproduzível do Acervo — {date.today().strftime('%d/%m/%Y')}",
        "",
        "> Este documento conta arquivos; não confunde volume documental com validação científica.",
        "",
        "## Contagens principais",
        "",
        "| Medida | Total | Definição operacional |",
        "|---|---:|---|",
        f"| Markdown público | {len(records)} | Arquivos `.md` sob `docs/` incluídos no build |",
        f"| Documentos em `analyses` | {len(analysis_records)} | Arquivos sob `docs/analyses/`; incluem fichas, perfis e índices |",
        f"| Estrutura numerada 1–8 em `analyses` | {len(analysis_structured)} | Os oito títulos numerados foram detectados; o conteúdo ainda exige revisão humana |",
        f"| Identificador público em `analyses` | {len(analysis_identified)} | DOI, ISBN, ISSN ou Handle detectável no arquivo |",
        "",
        "## Distribuição do Markdown público",
        "",
        "| Diretório inicial | Arquivos |",
        "|---|---:|",
    ]
    lines.extend(f"| `{group}` | {count} |" for group, count in sorted(group_counts.items()))
    lines.extend(
        [
            "",
            "## Estados explicitamente declarados",
            "",
            "| Estado encontrado | Arquivos |",
            "|---|---:|",
        ]
    )
    lines.extend(f"| `{status}` | {count} |" for status, count in sorted(status_counts.items()))
    lines.extend(
        [
            "",
            "## Tipos documentais declarados",
            "",
            "| Tipo documental | Arquivos |",
            "|---|---:|",
        ]
    )
    lines.extend(f"| `{doc_type}` | {count} |" for doc_type, count in sorted(type_counts.items()))
    lines.extend(
        [
            "",
            "## Limites da contagem",
            "",
            "- Uma ficha só é considerada documentalmente homologada após conferência humana do PDF, da autoria, do identificador e das oito seções.",
            "- A presença automática das seções 1–8 não atesta qualidade, fidelidade ou validade científica.",
            "- Índices, perfis, textos institucionais e estados da arte são documentos do acervo, mas não devem ser anunciados como fichas científicas.",
            "- PDFs privados, quarentena, extrações integrais e materiais ignorados pelo Git não entram nesta contagem pública.",
            "- Cadernos aguardando DOI e a gaveta Tecnologia Takwara em revisão são excluídos da contagem enquanto permanecerem fora do build.",
            "",
            "## Reprodução",
            "",
            "```bash",
            "python3 scripts/inventariar_acervo.py . --markdown INVENTARIO_ACERVO.md --json INVENTARIO_ACERVO.json",
            "```",
            "",
        ]
    )
    args.markdown.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
