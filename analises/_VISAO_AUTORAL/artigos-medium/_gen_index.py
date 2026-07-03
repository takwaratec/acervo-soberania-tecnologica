#!/usr/bin/env python3
"""Gera index.md para a pasta artigos-medium."""
import os, re, glob, yaml

base = os.path.dirname(os.path.abspath(__file__))
files = sorted(glob.glob(os.path.join(base, 'AUT_MED_*.md')))

rows = []
for f in files:
    with open(f, encoding='utf-8') as fp:
        content = fp.read()
    m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if m:
        meta = yaml.safe_load(m.group(1))
        slug = os.path.basename(f).replace('.md', '')
        title = meta.get('titulo', slug)
        date = meta.get('data_publicacao', '')
        words = meta.get('palavras', 0)
        if hasattr(date, 'isoformat'):
            date = date.isoformat()[:10]
        rows.append((str(date), title, slug, words))

rows.sort(key=lambda r: r[0], reverse=True)

md = '# Artigos no Medium\n\n'
md += 'Artigos de opiniao, analise e praxis territorial publicados por Fabio Takwara no [Medium (fabiotakwara)](https://fabiotakwara.medium.com/).\n\n'
md += '> Sincronizados automaticamente via RSS. Para atualizar, execute:\n'
md += '> `conda run -n whisper_env python _VISAO_AUTORAL/_sync_medium.py`\n\n'
md += '| # | Titulo | Data | Palavras |\n'
md += '|---|--------|------|----------|\n'

total_words = 0
for i, (date, title, slug, words) in enumerate(rows, 1):
    md += f'| {i} | [{title}]({slug}.md) | {date} | {words} |\n'
    total_words += words

md += f'\n*{len(rows)} artigos · ~{total_words} palavras · {rows[-1][0][:7]} — {rows[0][0][:7]} · CC BY-NC-ND 4.0*\n'

with open(os.path.join(base, 'index.md'), 'w', encoding='utf-8') as f:
    f.write(md)

print(f'index.md atualizado com {len(rows)} artigos, ~{total_words} palavras')
