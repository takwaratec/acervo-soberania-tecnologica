#!/Users/fabiotakwara/miniconda3/envs/whisper_env/bin/python3
"""
MIGRADOR + CORRETOR + INDEXADOR DO ACERVO
Etapa 1: Cria subgrupos e move fichas
Etapa 2: Corrige citacoes genericas
Etapa 3: Gera indice catalografico cruzado
"""
import os, re, shutil, subprocess, json
from datetime import datetime

ACERVO = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica/docs/analises"
NOW = datetime.now().strftime('%Y-%m-%d %H:%M')

# === SUBGROUP DEFINITIONS ===
SUBGROUPS = {
    '01_polimeros-vegetais-e-biocompositos': [
        ('01_PU_Vegetal', ['imperveg', 'mamona', 'mamonex', 'espuma de pu', 'poliuretano vegetal', 'pu vegetal', 'selante', 'impermeabilizante', 'rqi', 'ug132', 'fl133']),
        ('02_Biocompositos', ['biocompósito', 'compósito', 'fibra+pu', 'bambu+pu', 'reforço interno', 'painel de bambu', 'osb', 'purcom']),
        ('03_Biochar_Pirolenhoso', ['biochar', 'carvão vegetal', 'carvão ativado', 'pirolenhoso', 'briquetes', 'pirólise', 'charcoal', 'biocarvão', 'carvao']),
        ('04_Fibras_Naturais', ['fibra vegetal', 'fibra natural', 'celulose', 'absorção de água', 'sisal', 'juta', 'malva', 'rami', 'agave', 'coco']),
        ('05_Bioeconomia', ['bioeconomia', 'mercado bambu', 'cadeia produtiva', 'bndes setorial', 'custo', 'viabilidade econômica', 'negócio', 'ACV', 'life cycle']),
        ('06_MQTF', ['wtf', 'mqft', 'mulheres que tecem', 'regência científica', 'dossiê bndes']),
    ],
    '02_bambu-estrutural-e-tratamentos': [
        ('01_Especies_Botanica', ['guadua angustifolia', 'guadua weberbaueri', 'phyllostachys', 'bambusa vulgaris', 'dendrocalamus', 'espécie nativa', 'botânica', 'taxonomia']),
        ('02_Propriedades_Fisicas_Mecanicas', ['propriedade física', 'propriedade mecânica', 'ensaio de tração', 'resistência', 'compressão', 'flexão', 'caracterização', 'física e térmica']),
        ('03_Tratamento_Preservacao', ['tratamento preservativo', 'ácido pirolenhoso', 'tratamento químico', 'tratamento térmico', 'boro', 'vapor saturado', 'preservação', 'fungo', 'deteriora']),
        ('04_Manejo_Silvicultura', ['manejo sustentado', 'silvicultura', 'cultivo', 'colheita', 'plantio', 'manejo florestal']),
        ('05_Amazonia_Invasoras', ['amazônia', 'nativo da amazônia', 'invasora', 'exótica', 'guadua tuberculata', 'acre', 'rondônia']),
        ('06_Construcao_Engenharia', ['domo geodésico', 'conexão estrutural', 'bambu laminado', 'blc', 'engenharia', 'estrutura', 'geodésica']),
    ],
    '03_habitacao-social-e-athis': [
        ('01_HIS_CDHU_MCMV', ['cdhu', 'mcmv', 'minha casa', 'déficit habitacional', 'fhp', 'joão pinheiro', 'habitacional']),
        ('02_ATHIS_Extensao', ['athis', 'assistência técnica', 'extensão', 'lei 11.888']),
        ('03_ECOSALA', ['ecosala', 'coletivo']),
        ('04_Tecnologias_Construtivas', ['domo geodésico', 'painel estrutural', 'saneamento ecológico', 'banheiro seco', 'cúpula', 'domo']),
    ],
    '04_certificacoes-e-normas': [
        ('01_Normas_NBR', ['nbr 15575', 'nbr 16828', 'abnt']),
        ('02_ISO', ['iso 14001', 'iso 14025', 'iso 14040', 'epd', 'sga']),
        ('03_FISPQ', ['fispq', 'kehl', 'aglomerante', 'segurança química']),
        ('04_Ensaios_Certificacao', ['ipt', 'ensaio de desempenho', 'verra', 'vm0044', 'certificação']),
    ],
    '05_perfis-e-referencias': [
        ('01_Pesquisadores', ['perfil de pesquisador', 'professor', 'dr.', 'pesquisador']),
        ('02_ICTs_Instituicoes', ['ifb', 'if goiano', 'ufscar', 'unicamp', 'usp', 'ufpr', 'ufac', 'unb', 'embrapa', 'instituto federal', 'universidade']),
        ('03_Empresas', ['imperveg', 'techsus', 'faleiros', 'kehl', 'purcom']),
        ('04_Bibliografias', ['bibliografia', 'catálogo', 'referências', 'literatura']),
    ],
}

# === STEP 1: CLASSIFY, MOVE, FIX ===
print("="*70)
print("📦 ETAPA 1: CRIAR SUBGRUPOS E MOVER FICHAS")
print("="*70)

moved = 0
fixes = 0

for area, subgroups in SUBGROUPS.items():
    area_path = os.path.join(ACERVO, area)
    if not os.path.exists(area_path):
        continue
    
    # Create subgroup dirs
    for sub_name, _ in subgroups:
        sub_path = os.path.join(area_path, sub_name)
        os.makedirs(sub_path, exist_ok=True)
    
    # Add "00_Outros" for unclassified
    outros_path = os.path.join(area_path, '00_Outros')
    os.makedirs(outros_path, exist_ok=True)
    
    # Classify and move each ficha
    for fname in sorted(os.listdir(area_path)):
        if not fname.endswith('.md') or fname.startswith('_') or fname == 'index.md':
            continue
        if any(fname.startswith(s.split('_')[0] + '_') for s, _ in subgroups):
            # Already in a subgroup subdir
            continue
        
        fpath = os.path.join(area_path, fname)
        if os.path.isdir(fpath):
            continue
        
        with open(fpath) as f:
            content = f.read()
        content_lower = content.lower()
        
        # Find best subgroup
        target_sub = '00_Outros'
        for sub_name, keywords in subgroups:
            if any(kw in content_lower for kw in keywords):
                target_sub = sub_name
                break
        
        # Move file
        target_path = os.path.join(area_path, target_sub, fname)
        if not os.path.exists(target_path):
            shutil.move(fpath, target_path)
            moved += 1
        
        # Fix generic citations in YAML
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                yaml = parts[1]
                cite_m = re.search(r'how_to_cite:\s*"([^"]+)"', yaml)
                if cite_m:
                    cite_text = cite_m.group(1)
                    # Check if generic
                    if cite_text.startswith('Ficha ') and cite_text.endswith('. 2026.'):
                        # Extract real title from body
                        title_m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
                        real_title = title_m.group(1).strip() if title_m else fname.replace('.md','')
                        real_title = re.sub(r'\s*\|\s*$', '', real_title).strip()
                        
                        # Preserve DOI if exists
                        doi_m = re.search(r'(10\.\d{4,}/[a-zA-Z0-9._/-]+)', content)
                        doi_str = f' DOI: {doi_m.group(1)}.' if doi_m else ''
                        
                        # Find year
                        year_m = re.search(r'\*\*Ano\*\*\s*\|\s*(\d{4})', content)
                        year = year_m.group(1) if year_m else '2026'
                        
                        new_cite = f"{real_title}. {year}.{doi_str}"
                        new_yaml = yaml.replace(f'how_to_cite: "{cite_text}"', f'how_to_cite: "{new_cite}"')
                        content = content.replace(yaml, new_yaml)
                        
                        with open(target_path, 'w') as f:
                            f.write(content)
                        fixes += 1
                        if fixes <= 10:
                            print(f"  ✅ Fix: {area}/{target_sub}/{fname[:50]}")
                            print(f"     '{cite_text[:60]}' → '{new_cite[:60]}'")

print(f"\n📊 Movidos: {moved} | Citações corrigidas: {fixes}")

# === STEP 2: BUILD CROSS-REFERENCE INDEX ===
print(f"\n{'='*70}")
print("📇 ETAPA 2: GERAR ÍNDICE CATALOGRÁFICO CRUZADO")
print("="*70)

# Collect all fichas with metadata
all_fichas = []
projects_temas = {
    'fabrica-modelo': ['techsus', 'faleiros', 'painel estrutural', 'his', 'cdhu', 'habitação social', 'industrializado', 'nbr 15575', 'ipt', 'mcmv'],
    'vaga-lumen': ['ecosala', 'coletivo', 'vaga lumen'],
    'acervo-soberania': ['soberania tecnológica', 'acervo', 'cavichiolli', 'curadoria'],
    'mulheres-tecem-amazonia': ['mqft', 'mulheres que tecem', 'regência científica', 'bndes'],
    'personagens-bambu': ['personagem', 'bambu', 'biotipo'],
}

for area, subgroups in SUBGROUPS.items():
    area_path = os.path.join(ACERVO, area)
    area_name = area.split('_', 1)[-1]
    
    for root, dirs, files in os.walk(area_path):
        if root == area_path:
            continue  # skip root
        sub_name = os.path.basename(root)
        
        for fname in sorted(files):
            if not fname.endswith('.md') or fname.startswith('_') or fname == 'index.md':
                continue
            fpath = os.path.join(root, fname)
            
            with open(fpath) as f:
                content = f.read()
            
            # Extract metadata
            yaml_part = content.split('---')[1] if content.startswith('---') else ""
            cite_m = re.search(r'how_to_cite:\s*"([^"]+)"', yaml_part)
            citation = cite_m.group(1) if cite_m else ''
            doi_m = re.search(r'(10\.\d{4,}/[a-zA-Z0-9._/-]+)', content)
            doi = doi_m.group(1) if doi_m else ''
            title_m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            title = title_m.group(1).strip() if title_m else fname
            year_m = re.search(r'\b(19[0-9]{2}|20[0-9]{2})\b', content[:500])
            year = year_m.group(1) if year_m else ''
            
            # Extract author from various formats
            author = ''
            auth_m = re.search(r'\*\*Autor\*\*\s*(?:\|\s*)?(.+?)(?:\n|$)', content)
            if auth_m: author = auth_m.group(1).strip()
            auth_m2 = re.search(r'^autor:\s*(.+)$', yaml_part, re.MULTILINE)
            if auth_m2 and not author: author = auth_m2.group(1).strip()
            
            # Extract company/ICT from YAML
            empresa = ''
            inst_m = re.search(r'^instituicao:\s*(.+)$', yaml_part, re.MULTILINE)
            if inst_m: empresa = inst_m.group(1).strip()
            
            # Determine which projects this ficha relates to
            projetos = []
            for proj, kws in projects_temas.items():
                if any(kw in content.lower() for kw in kws):
                    projetos.append(proj)
            if not projetos:
                projetos.append('geral')
            
            rel_path = os.path.relpath(fpath, ACERVO)
            
            all_fichas.append({
                'path': rel_path,
                'area': area_name,
                'subgroup': sub_name,
                'title': title[:80],
                'citation': citation[:120],
                'author': author[:60],
                'year': year,
                'doi': doi[:60],
                'empresa': empresa[:60],
                'projetos': projetos,
                'has_doi': bool(doi),
                'has_author': bool(author),
            })

# Build INDEX.md
BASE_URL = "https://github.com/takwaratec/acervo-soberania-tecnologica/blob/main/docs/analises"

# Count by area+subgroup
sub_counts = {}
for f in all_fichas:
    key = (f['area'], f['subgroup'])
    sub_counts[key] = sub_counts.get(key, 0) + 1

index_lines = []
index_lines.append(f"# 📚 Índice do Acervo Soberania Tecnológica\n")
index_lines.append(f"> Catálogo cruzado de {len(all_fichas)} fichas científicas")
index_lines.append(f"> Gerado em {NOW}\n")
index_lines.append(f"---\n")

# === SECTION 1: BY AREA + SUBGROUP ===
index_lines.append("## 1. POR ÁREA E SUBGRUPO\n")
for area, subgroups in SUBGROUPS.items():
    area_name = area.split('_', 1)[-1]
    index_lines.append(f"### {area_name}\n")
    for sub_name, _ in subgroups:
        count = sub_counts.get((area_name, sub_name), 0)
        outros = sub_counts.get((area_name, '00_Outros'), 0)
        if count > 0:
            index_lines.append(f"- **{sub_name.replace('_', ' ')}** ({count} fichas)")
    outros_count = sub_counts.get((area_name, '00_Outros'), 0)
    if outros_count > 0:
        index_lines.append(f"- **Outros** ({outros_count} fichas)")
    index_lines.append("")

# === SECTION 2: BY PROJECT ===
index_lines.append("---\n## 2. POR PROJETO/REPOSITÓRIO\n")
for proj, kws in projects_temas.items():
    fichas_proj = [f for f in all_fichas if proj in f['projetos']]
    index_lines.append(f"### 📁 {proj} ({len(fichas_proj)} fichas)")
    for f in fichas_proj[:10]:
        index_lines.append(f"  - [{f['title']}]({BASE_URL}/{f['path']}) | {f['author'][:40]}")
    if len(fichas_proj) > 10:
        index_lines.append(f"  - ... +{len(fichas_proj)-10} fichas")
    index_lines.append("")

# === SECTION 3: BY AUTHOR ===
index_lines.append("---\n## 3. POR AUTOR\n")
authors = {}
for f in all_fichas:
    if f['author']:
        key = f['author'].split(',')[0].strip().upper()[:20] if ',' in f['author'] else f['author'].split()[0].upper()[:20] if f['author'] else '?'
        authors.setdefault(key, []).append(f)
for auth in sorted(authors.keys())[:30]:
    fichas_auth = authors[auth]
    if len(fichas_auth) <= 5:
        for f in fichas_auth:
            index_lines.append(f"- **{auth}**: [{f['title'][:60]}]({BASE_URL}/{f['path']})")
    else:
        index_lines.append(f"- **{auth}** ({len(fichas_auth)} fichas): [{fichas_auth[0]['title'][:50]}]({BASE_URL}/{fichas_auth[0]['path']}) ...")
if len(authors) > 30:
    index_lines.append(f"\n*+{len(authors)-30} autores no total*")

# === SECTION 4: BY ICT/INSTITUTION ===
index_lines.append("\n---\n## 4. POR ICT / INSTITUIÇÃO\n")
icts = ['EMBRAPA', 'IFB', 'USP', 'UNICAMP', 'UFPR', 'UFAC', 'UFSCar', 'UFRJ', 'UnB', 'IPT', 'IF Goiano']
for ict in icts:
    fichas_ict = [f for f in all_fichas if ict.lower() in f['empresa'].lower() or ict.lower() in f['path'].lower()]
    if fichas_ict:
        index_lines.append(f"- **{ict}**: {len(fichas_ict)} fichas")

# === SECTION 5: BY COMPANY ===
index_lines.append("\n---\n## 5. POR EMPRESA\n")
empresas = ['Imperveg', 'Techsus', 'Faleiros', 'Kehl', 'Purcom']
for emp in empresas:
    fichas_emp = [f for f in all_fichas if emp.lower() in f['empresa'].lower() or emp.lower() in f['path'].lower()]
    if fichas_emp:
        index_lines.append(f"- **{emp}**: {len(fichas_emp)} fichas")

# === SECTION 6: BY YEAR ===
index_lines.append("\n---\n## 6. POR ANO\n")
years = {}
for f in all_fichas:
    if f['year']:
        dec = f['year'][:3] + '0'
        years.setdefault(dec, []).append(f)
for dec in sorted(years.keys()):
    index_lines.append(f"- **{dec}s**: {len(years[dec])} fichas")

# === SECTION 7: BY DOCUMENT TYPE ===
index_lines.append("\n---\n## 7. POR TIPO DE DOCUMENTO\n")
com_doi = sum(1 for f in all_fichas if f['has_doi'])
com_autor = sum(1 for f in all_fichas if f['has_author'])
index_lines.append(f"- **Artigos com DOI**: {com_doi} fichas")
index_lines.append(f"- **Com autor identificado**: {com_autor} fichas")
index_lines.append(f"- **Fichas MQTF (Mulheres Que Tecem a Floresta)**: {sub_counts.get(('polimeros-vegetais-e-biocompositos', '06_MQTF'), 0)}")
index_lines.append(f"- **FISPQ (Fichas de Segurança)**: {sub_counts.get(('certificacoes-e-normas', '03_FISPQ'), 0)}")
index_lines.append(f"- **Normas Técnicas**: {sub_counts.get(('certificacoes-e-normas', '01_Normas_NBR'), 0)}")
index_lines.append(f"- **Perfis de Pesquisadores**: {sub_counts.get(('perfis-e-referencias', '01_Pesquisadores'), 0)}")

# === SECTION 8: NAVIGATION GUIDE FOR AGENTS ===
index_lines.append("\n---\n## 8. GUIA DE NAVEGAÇÃO PARA AGENTES\n")
index_lines.append("| Para escrever sobre... | Consulte... |")
index_lines.append("|---|---|")
index_lines.append("| PU Vegetal / Imperveg | `01_polimeros/01_PU_Vegetal/` |")
index_lines.append("| Tratamento de bambu | `02_bambu/03_Tratamento_Preservacao/` |")
index_lines.append("| Propriedades do bambu | `02_bambu/02_Propriedades_Fisicas_Mecanicas/` |")
index_lines.append("| HIS / CDHU / MCMV | `03_habitacao/01_HIS_CDHU_MCMV/` |")
index_lines.append("| Certificações ISO | `04_certificacoes/02_ISO/` |")
index_lines.append("| Biochar / Pirólise | `01_polimeros/03_Biochar_Pirolenhoso/` |")
index_lines.append("| Fitorremediação | `02_bambu/05_Amazonia_Invasoras/` |")
index_lines.append("| Perfil de pesquisador | `05_perfis/01_Pesquisadores/` |")
index_lines.append("| Economia circular | `01_polimeros/05_Bioeconomia/` |")
index_lines.append("| Espécies de bambu | `02_bambu/01_Especies_Botanica/` |")

index_lines.append(f"\n---\n*Índice gerado em {NOW} · {len(all_fichas)} fichas catalogadas*")

# Write index
index_path = os.path.join(ACERVO, 'INDEX.md')
with open(index_path, 'w') as f:
    f.write('\n'.join(index_lines))
print(f"\n📇 INDEX.md criado com {len(all_fichas)} fichas catalogadas")

# === SUMMARY ===
print(f"\n{'='*70}")
print("✅ RESUMO DA OPERAÇÃO")
print(f"{'='*70}")
print(f"  Fichas movidas para subgrupos: {moved}")
print(f"  Citações genéricas corrigidas: {fixes}")
print(f"  Fichas no índice: {len(all_fichas)}")
print(f"  INDEX.md: {index_path}")
