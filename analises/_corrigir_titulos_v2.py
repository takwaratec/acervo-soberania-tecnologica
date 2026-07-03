#!/Users/fabiotakwara/miniconda3/envs/whisper_env/bin/python3
"""Corrigir titulos, YAML quebrado e citacoes com dados reais do corpo da ficha"""
import os, re

ACERVO_DIR = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica/docs/analises"

def extrair_titulo_real(content):
    """Extrai o titulo REAL do corpo da ficha, nao do filename"""
    # Strategy 1: Look for "Título original:" in section 3
    m = re.search(r'\*\*T[íi]tulo original:\*\*\s*(.+)', content)
    if m: return m.group(1).strip()
    
    # Strategy 2: Look for "Título:" in identificaçao
    m = re.search(r'\*\*T[íi]tulo\*\*\s*\|\s*(.+)', content[:1500])
    if m: 
        t = m.group(1).strip()
        if len(t) > 10: return t
    
    # Strategy 3: Use first meaningful heading
    m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if m:
        t = m.group(1).strip()
        if not t.startswith('<') and not t.startswith('src=') and len(t) > 5:
            return t
    
    return None

def extrair_autor_real(content):
    """Extrai autor do corpo da ficha"""
    m = re.search(r'\*\*Autor:\*\*\s*(.+?)(?:\n|$)', content)
    if m: return m.group(1).strip()
    m = re.search(r'\*\*Autor \(Fabio Takwara\)\*\*\s*\|\s*(.+?)(?:\n|$)', content)
    if m: return m.group(1).strip()
    return None

def extrair_doi_real(content):
    m = re.search(r'(10\.\d{4,}/[a-zA-Z0-9._/-]+)', content)
    return m.group(1) if m else None

def extrair_ano_real(content):
    m = re.search(r'\b(19[0-9]{2}|20[0-9]{2})\b', content[:1000])
    return m.group(1) if m else None

fixed = 0
yaml_fixed = 0

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
        
        # Fix broken YAML (how_to_cite without newline before ---)
        content = re.sub(r'(how_to_cite: "[^"]+)"---', r'\1"\n---', content)
        
        # Get real title
        real_title = extrair_titulo_real(content)
        if not real_title:
            continue
        
        # Update heading
        heading_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if heading_match:
            old_heading = heading_match.group(1).strip()
            if old_heading != real_title and len(real_title) > 10:
                content = content.replace(f'# {old_heading}', f'# {real_title}', 1)
                fixed += 1
                if fixed <= 5:
                    print(f"  ✅ Titulo: '{old_heading[:50]}' → '{real_title[:50]}'")
        
        # Get citation data
        autor = extrair_autor_real(content)
        ano = extrair_ano_real(content) or '2026'
        doi = extrair_doi_real(content)
        
        # Generate proper citation
        if autor and doi:
            citacao = f"{autor}. {real_title}. {ano}. DOI: {doi}"
        elif autor:
            citacao = f"{autor}. {real_title}. {ano}."
        elif doi:
            citacao = f"{real_title}. {ano}. DOI: {doi}"
        else:
            citacao = f"{real_title}. {ano}."
        
        # Update how_to_cite in YAML
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                yaml_text = parts[1]
                new_yaml = re.sub(
                    r'how_to_cite:\s*"[^"]*"',
                    f'how_to_cite: "{citacao}"',
                    yaml_text
                )
                if new_yaml != yaml_text:
                    content = f"---{new_yaml}---{parts[2]}"
                    yaml_fixed += 1
        
        with open(fpath, 'w') as f:
            f.write(content)

print(f"\n📊 CORRECAO:")
print(f"  Titulos corrigidos: {fixed}")
print(f"  YAML/citacoes corrigidos: {yaml_fixed}")
