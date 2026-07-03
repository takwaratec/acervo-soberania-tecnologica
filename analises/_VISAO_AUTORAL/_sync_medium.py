#!/usr/bin/env python3
"""
_sync_medium.py — Sincroniza artigos do Medium de Fabio Takwara com o acervo local.

Uso:
  conda run -n whisper_env python _VISAO_AUTORAL/_sync_medium.py

Requisitos: feedparser, pypandoc-binary
  pip install feedparser pypandoc-binary
"""

import feedparser
import pypandoc
import os
import re
import sys
from datetime import datetime

# ── Config ──────────────────────────────────────────────────────────────
RSS_URL = "https://medium.com/feed/@fabiotakwara"
DEST_DIR = os.path.join(os.path.dirname(__file__), "artigos-medium")
os.makedirs(DEST_DIR, exist_ok=True)

# ── Helpers ─────────────────────────────────────────────────────────────

def slugify(title: str) -> str:
    """Converte título em slug seguro para nome de arquivo."""
    s = title.lower().strip()
    s = re.sub(r'[^a-z0-9áéíóúâêîôûãõçàèìòùäëïöüñ\s-]', '', s)
    s = re.sub(r'[\s-]+', '-', s)
    s = s.strip('-')
    return s[:80]


def clean_html(html: str) -> str:
    """Remove divs do Medium que quebram a conversão, figcaption etc."""
    import re
    html = re.sub(r'<figcaption>.*?</figcaption>', '', html, flags=re.DOTALL)
    html = re.sub(r'<figure[^>]*>', '', html)
    html = re.sub(r'</figure>', '', html)
    return html


def iso_date(published: str) -> str:
    """Converte 'Tue, 18 Nov 2025 14:30:00 GMT' → '2025-11-18'"""
    from email.utils import parsedate_to_datetime
    try:
        dt = parsedate_to_datetime(published)
        return dt.strftime("%Y-%m-%d")
    except Exception:
        return published[:10]


def extract_tags(entry) -> list:
    """Extrai tags/categorias do entry."""
    tags = []
    if hasattr(entry, 'tags'):
        for t in entry.tags:
            if hasattr(t, 'term'):
                tags.append(t.term)
    return tags


def count_words(md: str) -> int:
    """Contagem simples de palavras no markdown."""
    text = re.sub(r'<[^>]+>', '', md)
    text = re.sub(r'[#*_`\[\]()>|~-]', ' ', text)
    return len(text.split())


# ── Main ────────────────────────────────────────────────────────────────

def sync():
    print(f"🌐 Conectando ao feed RSS: {RSS_URL}")
    feed = feedparser.parse(RSS_URL)

    if not feed.entries:
        print("❌ Nenhum artigo encontrado no feed.")
        print("   Possíveis causas: feed vazio, URL errada, ou bloqueio de rede.")
        return False

    print(f"📡 Feed encontrado: {len(feed.entries)} artigos\n")

    # Lista arquivos já sincronizados para evitar duplicatas
    existing = {f.replace('.md', '') for f in os.listdir(DEST_DIR) if f.endswith('.md')}

    imported = 0
    skipped = 0
    errors = 0

    for i, entry in enumerate(feed.entries, 1):
        title = entry.title.strip()
        slug = slugify(title)
        filename = f"AUT_MED_{slug}.md"
        filepath = os.path.join(DEST_DIR, filename)

        # Pular se já existe
        if filename.replace('.md', '') in existing:
            print(f"  ⏭️  [{i}] Já sincronizado: {title}")
            skipped += 1
            continue

        # Extrair conteúdo HTML
        if hasattr(entry, 'content') and entry.content:
            html_content = entry.content[0].value
        elif hasattr(entry, 'summary'):
            html_content = entry.summary
        else:
            print(f"  ⚠️  [{i}] Sem conteúdo: {title}")
            errors += 1
            continue

        # Limpar HTML
        html_content = clean_html(html_content)

        # Converter para Markdown com pypandoc
        try:
            md_body = pypandoc.convert_text(html_content, 'md', format='html',
                                            extra_args=['--wrap=none'])
        except Exception as e:
            print(f"  ❌ [{i}] Erro na conversão: {title} — {e}")
            errors += 1
            continue

        # Metadados
        pub_date = iso_date(entry.published)
        tags = extract_tags(entry)
        word_count = count_words(md_body)
        link = entry.link.split('?')[0]  # Remove query params do RSS

        # YAML frontmatter estilo Cavichiolli
        frontmatter = (
            "---\n"
            f"tipo: Artigo Autoral\n"
            f"autor: Fabio Takwara\n"
            f"titulo: \"{title}\"\n"
            f"data_publicacao: {pub_date}\n"
            f"link_original: {link}\n"
            f"palavras_chave: [autoral, {' ,'.join(tags[:5])}]\n"
            f"palavras: {word_count}\n"
            f"fonte: Medium (fabiotakwara)\n"
            f"idioma: pt-BR\n"
            f"licenca: CC BY-NC-ND 4.0\n"
            "---\n\n"
        )

        # Escrever arquivo
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(frontmatter)
            f.write(f"# {title}\n\n")
            f.write(md_body)

        print(f"  ✅ [{i}] {filename} ({word_count} palavras, {pub_date})")
        imported += 1

    # ── Resumo ──
    print(f"\n{'='*50}")
    print(f"📊 Resumo da Sincronização")
    print(f"{'='*50}")
    print(f"  Total no feed:     {len(feed.entries)}")
    print(f"  Importados:        {imported}")
    print(f"  Já existentes:     {skipped}")
    print(f"  Erros:             {errors}")
    print(f"  Destino:           {DEST_DIR}")
    print(f"\n  🔗 Todos os artigos preservam link original para o Medium.")

    if imported > 0:
        print(f"\n  ⚡ Execute _gerar_index.py para atualizar o INDEX.md")
        print(f"  ⚡ Execute _reindexar_acervo.py para atualizar o ChromaDB")

    return imported > 0


if __name__ == "__main__":
    print("╔══════════════════════════════════════════════╗")
    print("║  🖨️  Sincronizador Medium → Acervo Local     ║")
    print("║  fabiotakwara.medium.com → _VISAO_AUTORAL/   ║")
    print("╚══════════════════════════════════════════════╝\n")
    sync()
