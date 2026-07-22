#!/usr/bin/env python3
"""Auditoria estrutural e documental dos candidatos a análise do Acervo."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path


DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.I)
ISBN_RE = re.compile(r"\bISBN(?:-1[03])?\s*[:#]?\s*[0-9Xx -]{10,20}\b", re.I)
ISSN_RE = re.compile(r"\bISSN\s*[:#]?\s*\d{4}-\d{3}[\dXx]\b", re.I)
HANDLE_RE = re.compile(r"https?://hdl\.handle\.net/[^\s)>]+", re.I)
SECTION_RE = re.compile(r"^##\s+([1-8])(?:\.|\s|—|-)[^\n]*\n(.*?)(?=^##\s+[1-8](?:\.|\s|—|-)|\Z)", re.M | re.S)
STATUS_RE = re.compile(r"^(?:status|estado_documental):\s*[\"']?([^\n\"']+)", re.M | re.I)
IDENTIFIER_FIELD_RE = re.compile(r"^identificador:\s*[\"']?([^\n\"']+)", re.M | re.I)
TECH_IDENTIFIER_RE = re.compile(r"^identificador_tecnico:\s*[\"']?([^\n\"']+)", re.M | re.I)
PROVENANCE_RE = re.compile(r"^proveniencia:\s*[\"']?([^\n\"']+)", re.M | re.I)
AUTHOR_PATTERNS = [
    re.compile(r"^(?:autor(?:a|es)?|autoria|author|authors|entidade_responsavel):\s*.+$", re.M | re.I),
    re.compile(r"\|\s*\*\*(?:Autores?|Autoria)\*\*\s*\|\s*(?!—|não identificado|não confirmado).+\|", re.I),
    re.compile(r"^\*\*(?:Autores?|Autoria):\*\*\s*(?!—|não identificado|não confirmado).+", re.M | re.I),
    re.compile(r"\|\s*(?:\*\*)?(?:Autores?|Autoria|Autor(?:a)?|Emissor|Entidade responsável|Fabricante(?: declarado)?)(?:\*\*)?\s*\|\s*(?!—|não identificado|não confirmado)[^|\n]+\|", re.I),
    re.compile(r"^\*\*Referência(?: completa| ABNT| documental)?:\*\*\s*[A-ZÀ-Ý][A-ZÀ-Ý ,.'-]{2,},", re.M),
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def inspect(path: Path, repository: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    section_matches = list(SECTION_RE.finditer(text))
    section_lengths = {match.group(1): len(re.sub(r"\s+", " ", match.group(2)).strip()) for match in section_matches}
    sections = sorted(section_lengths)
    complete = sections == list("12345678")
    substantive = complete and all(section_lengths[str(number)] >= 80 for number in range(1, 9))
    dois = sorted(set(match.rstrip(".,;)") for match in DOI_RE.findall(text)))
    identifiers = dois[:]
    if ISBN_RE.search(text):
        identifiers.append("ISBN")
    if ISSN_RE.search(text):
        identifiers.append("ISSN")
    handles = sorted(set(HANDLE_RE.findall(text)))
    identifiers.extend(handles)
    identifier_field = IDENTIFIER_FIELD_RE.search(text[:2500])
    technical_identifier = TECH_IDENTIFIER_RE.search(text[:2500])
    provenance = PROVENANCE_RE.search(text[:2500])
    absence_declared = bool(
        identifier_field
        and re.search(r"ausente|não se aplica|nao se aplica", identifier_field.group(1), re.I)
        and provenance
    )
    if technical_identifier:
        identifiers.append("identificador técnico")
    if absence_declared:
        identifiers.append("ausente na fonte; proveniência declarada")
    has_document_identity = bool(identifiers)
    has_author = any(pattern.search(text[:5000]) for pattern in AUTHOR_PATTERNS)
    status_match = STATUS_RE.search(text[:2500])
    declared_status = status_match.group(1).strip() if status_match else "não declarado"

    if path.name.casefold() == "index.md":
        document_class = "indice"
        recommendation = "manter-como-indice; não contar como ficha"
    elif substantive and has_document_identity and has_author:
        document_class = "ficha-estruturalmente-completa"
        recommendation = "revisao-humana-da-fonte-antes-de-homologar"
    elif complete:
        document_class = "ficha-1-a-8-com-pendencias"
        missing = []
        if not has_document_identity:
            missing.append("identidade-documental")
        if not has_author:
            missing.append("autoria")
        if not substantive:
            missing.append("secoes-substantivas")
        recommendation = "revisar-" + "-e-".join(missing or ["conteudo"])
    elif sections:
        document_class = "ficha-incompleta"
        recommendation = "completar-secoes-" + "-".join(str(number) for number in range(1, 9) if str(number) not in sections)
    elif identifiers and has_author:
        document_class = "analise-fora-do-template"
        recommendation = "classificar-tipo-e-adaptar-sem-fabricar-conteudo"
    else:
        document_class = "triagem-manual"
        recommendation = "confirmar-tipo-autoria-identificador-e-fonte"

    return {
        "path": str(path.relative_to(repository)),
        "sha256": sha256(path),
        "bytes": path.stat().st_size,
        "sections": sections,
        "section_lengths": section_lengths,
        "has_sections_1_to_8": complete,
        "has_substantive_sections_1_to_8": substantive,
        "has_author_marker": has_author,
        "identifiers": identifiers,
        "declared_status": declared_status,
        "document_class": document_class,
        "recommendation": recommendation,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("repository", type=Path)
    parser.add_argument("--roots", nargs="+", default=["docs/analyses", "docs/analises"])
    parser.add_argument("--markdown", type=Path, required=True)
    parser.add_argument("--json", type=Path, required=True)
    args = parser.parse_args()
    repository = args.repository.resolve()

    files = []
    for root_name in args.roots:
        root = repository / root_name
        if root.exists():
            files.extend(sorted(root.rglob("*.md")))
    records = [inspect(path, repository) for path in files]
    by_hash = defaultdict(list)
    for record in records:
        by_hash[record["sha256"]].append(record["path"])
    duplicate_groups = [paths for paths in by_hash.values() if len(paths) > 1]
    unique_records = []
    seen = set()
    for record in records:
        if record["sha256"] in seen:
            continue
        seen.add(record["sha256"])
        unique_records.append(record)

    class_counts = Counter(record["document_class"] for record in unique_records)
    status_counts = Counter(record["declared_status"] for record in unique_records)
    payload = {
        "generated_on": str(date.today()),
        "input_files": len(records),
        "unique_documents": len(unique_records),
        "duplicate_groups": duplicate_groups,
        "class_counts": dict(sorted(class_counts.items())),
        "status_counts": dict(sorted(status_counts.items())),
        "records": unique_records,
    }
    args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        f"# Auditoria dos candidatos a análise — {date.today().strftime('%d/%m/%Y')}",
        "",
        "> Auditoria estrutural e documental automatizada. Nenhum arquivo recebe homologação científica automática.",
        "",
        "## Universo auditado",
        "",
        f"- Arquivos de entrada: **{len(records)}**",
        f"- Documentos únicos por SHA-256: **{len(unique_records)}**",
        f"- Grupos de duplicatas binárias: **{len(duplicate_groups)}**",
        "",
        "## Resultado por classe",
        "",
        "| Classe | Documentos únicos | Próxima decisão |",
        "|---|---:|---|",
    ]
    decisions = {
        "ficha-estruturalmente-completa": "Conferir PDF, metadados, fidelidade e direitos antes de homologar",
        "ficha-1-a-8-com-pendencias": "Corrigir metadados ou conteúdo faltante a partir da fonte",
        "ficha-incompleta": "Não publicar como ficha completa; localizar fonte e completar seções",
        "analise-fora-do-template": "Classificar o tipo documental antes de adaptar",
        "indice": "Manter como navegação; excluir da contagem de fichas",
        "triagem-manual": "Confirmar tipo, autoria, identificador e fonte",
    }
    for document_class, count in sorted(class_counts.items()):
        lines.append(f"| `{document_class}` | {count} | {decisions[document_class]} |")
    lines.extend(["", "## Duplicatas binárias", ""])
    if duplicate_groups:
        for group in duplicate_groups:
            lines.append("- " + " = ".join(f"`{path}`" for path in group))
    else:
        lines.append("Nenhuma.")
    lines.extend(
        [
            "",
            "## Lista auditável",
            "",
            "| Arquivo | Classe | Seções | Identificador | Autoria detectada | Estado declarado |",
            "|---|---|---:|---|---:|---|",
        ]
    )
    for record in unique_records:
        identifiers = ", ".join(record["identifiers"]) or "—"
        lines.append(
            f"| `{record['path']}` | `{record['document_class']}` | {len(record['sections'])}/8 | "
            f"{identifiers} | {'sim' if record['has_author_marker'] else 'não'} | `{record['declared_status']}` |"
        )
    lines.extend(
        [
            "",
            "## Limites",
            "",
            "- A auditoria verifica estrutura e sinais de metadados; não substitui leitura humana do PDF original.",
            "- Documento sem fonte integral acessível não pode ser completado por inferência.",
            "- A classe `ficha-estruturalmente-completa` significa apenas que os requisitos automáticos foram encontrados.",
            "- Homologação exige conferência individual conforme `GOVERNANCA_DOCUMENTAL.md`.",
            "",
        ]
    )
    args.markdown.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
