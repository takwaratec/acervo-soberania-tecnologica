#!/Users/fabiotakwara/miniconda3/envs/whisper_env/bin/python3
"""Adicionar citacao ABNT em todas as 590 fichas + how_to_cite no YAML"""
import os, re, json
from datetime import datetime

ACERVO_DIR = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica/docs/analises"
LOG_PATH = "/Users/fabiotakwara/Documents/Premio Zayed 2025/fichas/_log_citacoes.json"

def extrair_doi(texto):
    match = re.search(r'(10\.\d{4,}/[a-zA-Z0-9._/-]+)', texto)
    return match.group(1) if match else None

def extrair_ano(texto):
    match = re.search(r'\b(19[0-9]{2}|20[0-9]{2})\b', texto[:1000])
    return match.group(1) if match else None

def extrair_titulo(texto, fname):
    # Try to get title from first heading
    match = re.search(r'^#\s+(.+)$', texto, re.MULTILINE)
    if match:
        title = match.group(1).strip()
        # Clean up title
        title = re.sub(r'^[A-Z]+_', '', title)  # remove prefix
        title = title.replace('_', ' ').replace('-', ' ')
        title = re.sub(r'\s+', ' ', title).strip()
        if len(title) > 10:
            return title
    return fname.replace('.md', '').replace('_', ' ').strip()

def extrair_autor(texto, yaml_text):
    # Check YAML first
    if 'autor:' in yaml_text:
        autor = re.search(r'autor:\s*(.+)', yaml_text)
        if autor:
            return autor.group(1).strip()
    if 'autores:' in yaml_text:
        autores = re.search(r'autores:\s*(.+)', yaml_text)
        if autores:
            return autores.group(1).strip()
    
    # Try to find author patterns in resumo
    # Look for "SOBRENOME, N." patterns
    match = re.search(r'([A-ZÇÃÂÁÀÉÊÍÓÔÚÕ]+[\s,]+[A-Z][a-záéíóúãõç]+,\s*[A-Z]\.)', texto[:1000])
    if match:
        return match.group(1).strip()
    
    return None

def detectar_tipo_ficha(texto, fname):
    """Detecta se é resenha de artigo, ficha tecnica, perfil, etc."""
    if 'resenha-' in fname or fname.startswith('SCI_'):
        tipo = 'resenha'
    elif 'perfil-' in fname or fname.startswith('PER_'):
        tipo = 'perfil'
    elif fname.startswith('FIC_') or fname.startswith('CER_'):
        tipo = 'ficha_tecnica'
    elif 'FICHA_' in fname or fname.startswith('LAB_'):
        tipo = 'documento_tecnico'
    elif fname.startswith('TEC-'):
        tipo = 'documento_tecnico'
    else:
        tipo = 'resenha'
    
    # Override based on content
    if 'Dissertação' in texto[:500] or 'dissertação' in texto[:500]:
        tipo = 'dissertacao'
    elif 'Tese' in texto[:500] or 'tese' in texto[:500]:
        tipo = 'tese'
    elif 'Perfil' in texto[:500] and 'Pesquisador' in texto[:500]:
        tipo = 'perfil'
    
    return tipo

def gerar_citacao_abnt(tipo, titulo, autor, ano, doi, texto, fname, area):
    """Gera citacao ABNT a partir dos metadados disponiveis"""
    
    if tipo == 'perfil':
        if autor:
            return f"{autor}. **{titulo}**. Acervo Soberania Tecnológica, {ano or '2026'}. Disponível em: https://github.com/takwaratec/acervo-soberania-tecnologica/blob/main/docs/analises/{area}/{fname}"
        else:
            return f"**{titulo}**. Acervo Soberania Tecnológica, {ano or '2026'}. Disponível em: https://github.com/takwaratec/acervo-soberania-tecnologica/blob/main/docs/analises/{area}/{fname}"
    
    # Try to extract periodical name
    periodico = ""
    match = re.search(r'(?:In:?\s*)?([A-Z][a-záéíóúãõç]+(?:\s+[A-Z][a-záéíóúãõç]+)+)\.?\s*(?:v\.|vol\.)', texto[:2000])
    if match:
        periodico = match.group(1)
    
    if doi:
        if autor and ano:
            return f"{autor}. **{titulo}**. {periodico}, {ano}. DOI: {doi}"
        elif ano:
            return f"**{titulo}**. {periodico}, {ano}. DOI: {doi}"
        else:
            return f"**{titulo}**. DOI: {doi}"
    
    if tipo == 'dissertacao':
        if autor:
            return f"{autor}. **{titulo}**. {ano or 's.d.'}. Dissertação (Mestrado) — Instituição. DOI: {doi or 'N/A'}"
        else:
            return f"**{titulo}**. {ano or 's.d.'}. Dissertação (Mestrado)."
    
    if tipo == 'documento_tecnico':
        return f"**{titulo}**. Acervo Soberania Tecnológica, {ano or '2026'}. Documento técnico. Disponível em: https://github.com/takwaratec/acervo-soberania-tecnologica/blob/main/docs/analises/{area}/{fname}"
    
    # Default: internal document
    if autor:
        return f"{autor}. **{titulo}**. Acervo Soberania Tecnológica, {ano or '2026'}. Disponível em: https://github.com/takwaratec/acervo-soberania-tecnologica/blob/main/docs/analises/{area}/{fname}"
    else:
        return f"**{titulo}**. Acervo Soberania Tecnológica, {ano or '2026'}. Disponível em: https://github.com/takwaratec/acervo-soberania-tecnologica/blob/main/docs/analises/{area}/{fname}"

# Processar todas as fichas
log = []
total = 0
com_citacao = 0
sem_citacao = 0

print("🔍 ADICIONANDO CITACOES ABNT...\n")

for area in sorted(os.listdir(ACERVO_DIR)):
    ap = os.path.join(ACERVO_DIR, area)
    if not os.path.isdir(ap) or area.startswith('_'):
        continue
    
    area_count = 0
    area_ok = 0
    
    for fname in sorted(os.listdir(ap)):
        if not fname.endswith('.md') or fname in ('index.md', '_converter_cavichiolli.py'):
            continue
        
        fpath = os.path.join(ap, fname)
        with open(fpath) as f:
            content = f.read()
        
        total += 1
        area_count += 1
        
        # Extract YAML and body
        yaml_text = ""
        body = content
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                yaml_text = parts[1]
                body = parts[2]
        
        # Skip if already has how_to_cite
        if 'how_to_cite:' in yaml_text:
            area_ok += 1
            com_citacao += 1
            continue
        
        # Extract data
        titulo = extrair_titulo(body, fname)
        autor = extrair_autor(body, yaml_text)
        ano = extrair_ano(body)
        doi = extrair_doi(body)
        tipo = detectar_tipo_ficha(body, fname)
        
        # Generate citation
        citacao = gerar_citacao_abnt(tipo, titulo, autor, ano, doi, body, fname, area)
        
        # Add how_to_cite to YAML
        if 'conversao_cavichiolli:' in yaml_text:
            yaml_updated = yaml_text.replace(
                'conversao_cavichiolli: 2026-07-02',
                f'conversao_cavichiolli: 2026-07-02\nhow_to_cite: >\n  {citacao}'
            )
        else:
            yaml_updated = yaml_text + f'\nhow_to_cite: >\n  {citacao}\n'
        
        # Add ABNT citation to section 8 (REFERENCIAS)
        # Find section 8 and add citation
        section8_match = re.search(r'(## 8\. REFERÊNCIAS\s*\n)(.*?)(?=\n⚠️|\Z)', content, re.DOTALL)
        if section8_match:
            section8_header = section8_match.group(1)
            section8_body = section8_match.group(2)
            
            # Add citation if not already there
            if citacao not in section8_body:
                nova_section8 = section8_header + citacao + '\n\n' + section8_body
                content = content.replace(section8_match.group(0), nova_section8)
        
        # Reconstruct file
        novo_conteudo = f"---{yaml_updated}---{body}"
        
        with open(fpath, 'w') as f:
            f.write(novo_conteudo)
        
        area_ok += 1
        com_citacao += 1
        log.append({'file': fname, 'area': area, 'citacao': citacao[:80]})
    
    print(f"  📁 {area:40s} {area_count:3d} fichas | citacoes: {area_ok:3d}")

print(f"\n{'='*60}")
print(f"📊 RESUMO")
print(f"{'='*60}")
print(f"  Total: {total}")
print(f"  ✅ Com citacao ABNT: {com_citacao}")
print(f"  ⚠️  Sem citacao: {sem_citacao}")

with open(LOG_PATH, 'w') as f:
    json.dump(log, f, indent=2, ensure_ascii=False)
print(f"\n📝 Log salvo em: {LOG_PATH}")
