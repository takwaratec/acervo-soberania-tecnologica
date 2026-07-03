#!/Users/fabiotakwara/miniconda3/envs/whisper_env/bin/python3
"""Corrigir 320 titulos truncados + regenerar citacoes ABNT"""
import os, re

ACERVO_DIR = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica/docs/analises"

total_fix = 0
total_checked = 0

print("🔧 CORRIGINDO TITULOS TRUNCADOS...\n")

for area in sorted(os.listdir(ACERVO_DIR)):
    ap = os.path.join(ACERVO_DIR, area)
    if not os.path.isdir(ap) or area.startswith('_'):
        continue
    
    area_fix = 0
    
    for fname in sorted(os.listdir(ap)):
        if not fname.endswith('.md') or fname in ('index.md',):
            continue
        if fname.startswith('_'):
            continue
        
        total_checked += 1
        fpath = os.path.join(ap, fname)
        
        with open(fpath) as f:
            content = f.read()
        
        # Extract heading title
        heading_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if not heading_match:
            continue
        
        old_title = heading_match.group(1).strip()
        
        # Skip if title is clean (starts with uppercase letter, not HTML)
        if old_title and old_title[0].isupper() and not old_title.startswith('<') and not old_title.startswith('src='):
            continue
        
        # Try to extract REAL title from content body
        new_title = None
        
        # Strategy 1: Look for the actual content title in section 1 (IDENTIFICACAO)
        id_match = re.search(r'\*\*Título\*\*\s*\|\s*(.+)', content)
        if id_match:
            candidate = id_match.group(1).strip()
            if len(candidate) > 5 and not candidate.startswith('<'):
                new_title = candidate
        
        # Strategy 2: Look for title in YAML (nome field)
        if not new_title:
            yaml_part = content.split('---')[1] if content.startswith('---') else ""
            nome_match = re.search(r'^nome:\s*(.+)$', yaml_part, re.MULTILINE)
            if nome_match:
                candidate = nome_match.group(1).strip()
                if len(candidate) > 5:
                    new_title = candidate
        
        # Strategy 3: Use filename (without prefix)
        if not new_title:
            name_part = fname.replace('.md', '').split('_', 1)[-1] if '_' in fname else fname.replace('.md', '')
            new_title = name_part.replace('_', ' ').replace('-', ' ').strip()
            new_title = re.sub(r'\s+', ' ', new_title)
            # Capitalize
            new_title = new_title[0].upper() + new_title[1:] if new_title else "Documento"
        
        if not new_title or len(new_title) < 3:
            continue
        
        # Replace heading
        content = content.replace(f'# {old_title}', f'# {new_title}', 1)
        
        # Also update how_to_cite in YAML if it contains the bad title
        if 'how_to_cite:' in content:
            # Replace the cited title within how_to_cite
            yaml_part = content.split('---')[1] if content.startswith('---') else ""
            if old_title[:20] in yaml_part:  # Check if bad title is in citation
                # Regenerate: the how_to_cite will be fixed when _adicionar_citacoes runs again
                # For now, just clean the visible title
                pass
        
        with open(fpath, 'w') as f:
            f.write(content)
        
        area_fix += 1
        total_fix += 1
        
        if area_fix <= 3:
            print(f"  ✅ {area}/{fname}")
            print(f"     '{old_title[:60]}' → '{new_title[:60]}'")
    
    if area_fix > 3:
        print(f"  ... +{area_fix-3} em {area}")

print(f"\n📊 CORRECAO:")
print(f"  Total verificadas: {total_checked}")
print(f"  Titulos corrigidos: {total_fix}")

# Now regenerate citations
print(f"\n🔄 REGENERANDO CITACOES ABNT...")

total_cit = 0
for area in sorted(os.listdir(ACERVO_DIR)):
    ap = os.path.join(ACERVO_DIR, area)
    if not os.path.isdir(ap) or area.startswith('_'):
        continue
    for fname in sorted(os.listdir(ap)):
        if not fname.endswith('.md') or fname in ('index.md',):
            continue
        if fname.startswith('_'):
            continue
        
        fpath = os.path.join(ap, fname)
        with open(fpath) as f:
            content = f.read()
        
        # Get new title
        heading_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        new_title = heading_match.group(1).strip() if heading_match else fname
        
        # Get DOI if present
        doi_match = re.search(r'(10\.\d{4,}/[a-zA-Z0-9._/-]+)', content)
        doi = doi_match.group(1) if doi_match else None
        
        # Get year
        year_match = re.search(r'\b(19[0-9]{2}|20[0-9]{2})\b', content[:1000])
        year = year_match.group(1) if year_match else '2026'
        
        # Generate ABNT citation (clean, no links)
        if doi:
            citacao = f"{new_title}. {year}. DOI: {doi}"
        else:
            citacao = f"{new_title}. Acervo Soberania Tecnológica, {year}."
        
        # Update how_to_cite in YAML
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                yaml_text = parts[1]
                # Replace how_to_cite
                new_yaml = re.sub(
                    r'how_to_cite:.*?(?=\n\S|\Z)',
                    f'how_to_cite: "{citacao}"',
                    yaml_text,
                    count=1,
                    flags=re.DOTALL
                )
                content = f"---{new_yaml}---{parts[2]}"
                with open(fpath, 'w') as f:
                    f.write(content)
                total_cit += 1

print(f"  Citacoes regeneradas: {total_cit}")
print(f"\n✅ CONCLUIDO!")
