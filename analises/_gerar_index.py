#!/Users/fabiotakwara/miniconda3/envs/whisper_env/bin/python3
"""Regenera INDEX.md com a estrutura final de subdiretorios"""
import os, re
from datetime import datetime

ACERVO = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica/docs/analises"
BASE_URL = "https://github.com/takwaratec/acervo-soberania-tecnologica/blob/main/docs/analises"
NOW = datetime.now().strftime('%d/%m/%Y %H:%M')

# Collect all fichas with full path relative to ACERVO
all_fichas = []
for root, dirs, files in os.walk(ACERVO):
    if any(x in root for x in ['_00_ADMIN', '_VISAO', '_pdfs_', '_temp_', '.git', '__pycache__']):
        continue
    for fname in sorted(files):
        if not fname.endswith('.md') or fname.startswith('_') or fname in ('index.md', 'INDEX.md'):
            continue
        fpath = os.path.join(root, fname)
        rel = os.path.relpath(fpath, ACERVO)
        
        with open(fpath) as f:
            content = f.read()
        
        # Extract metadata
        yaml_part = content.split('---')[1] if content.startswith('---') else ""
        cite_m = re.search(r'how_to_cite:\s*"([^"]+)"', yaml_part)
        citation = cite_m.group(1)[:120] if cite_m else ''
        doi_m = re.search(r'(10\.\d{4,}/[a-zA-Z0-9._/-]+)', content)
        doi = doi_m.group(1) if doi_m else ''
        title_m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        title = title_m.group(1).strip()[:80] if title_m else fname.replace('.md','')
        
        auth_m = re.search(r'\*\*Autor\*\*\s*(?:\|\s*)?(.+?)(?:\n|$)', content)
        author = auth_m.group(1).strip()[:50] if auth_m else ''
        year_m = re.search(r'\b(19[0-9]{2}|20[0-9]{2})\b', content[:500])
        year = year_m.group(1) if year_m else ''
        
        all_fichas.append({
            'path': rel, 'title': title, 'citation': citation,
            'author': author, 'year': year, 'doi': doi,
            'area': rel.split('/')[0] if '/' in rel else '',
            'subgroup': rel.split('/')[1] if rel.count('/') >= 1 else '',
        })

# Build INDEX
lines = []
lines.append(f"# 📚 Índice do Acervo Soberania Tecnológica\n")
lines.append(f"> Catálogo cruzado de **{len(all_fichas)} fichas** científicas organizadas em 5 áreas e 24 subgrupos")
lines.append(f"> Gerado em {NOW}\n")
lines.append("---\n")

# 1. BY STRUCTURE
lines.append("## 1. ESTRUTURA COMPLETA\n")
area_map = {}
for f in all_fichas:
    area_map.setdefault(f['area'], {}).setdefault(f['subgroup'], []).append(f)

for area in sorted(area_map.keys()):
    area_name = area.split('_', 1)[-1] if '_' in area else area
    subgroups = area_map[area]
    area_total = sum(len(v) for v in subgroups.values())
    lines.append(f"### 📁 {area_name} ({area_total} fichas)\n")
    for sub in sorted(subgroups.keys()):
        fichas = subgroups[sub]
        if sub:
            lines.append(f"**{sub}/** ({len(fichas)} fichas)\n")
            for f in fichas[:3]:
                lines.append(f"- [{f['title']}]({BASE_URL}/{f['path']}) | {f['author'][:40]}")
            if len(fichas) > 3:
                lines.append(f"  *+{len(fichas)-3} fichas*")
            lines.append("")
        else:
            for f in fichas:
                lines.append(f"- [{f['title']}]({BASE_URL}/{f['path']})")

# 2. BY KEY AUTHOR
lines.append("---\n## 2. AUTORES DE REFERÊNCIA\n")
key_authors = {
    'Beraldo': [], 'Ghavami': [], 'Claro Neto': [], 'Nobre': [], 'Santos, M': [],
    'Liese': [], 'INBAR': [], 'IPCC': [], 'ONU': [], 'PNUD': [], 'EMBRAPA': [],
    'Takwara': [], 'Matsuoka': [], 'Fiore': [], 'Kamaruddin': [],
}
for f in all_fichas:
    for auth in key_authors:
        if auth.lower() in f['author'].lower() or auth.lower() in f['title'].lower() or auth.lower() in f['path'].lower():
            key_authors[auth].append(f)

for auth, fichas in sorted(key_authors.items()):
    if fichas:
        lines.append(f"**{auth}**: {len(fichas)} fichas\n")
        for f in fichas[:3]:
            lines.append(f"  - [{f['title'][:60]}]({BASE_URL}/{f['path']})")
        if len(fichas) > 3:
            lines.append(f"  *+{len(fichas)-3}*")
        lines.append("")

# 3. BY INSTITUTION
lines.append("---\n## 3. POR INSTITUIÇÃO / ICT\n")
icts = ['EMBRAPA', 'USP', 'UNICAMP', 'UFPR', 'UFAC', 'UnB', 'IFB', 'IPT', 'INBAR', 'FAO', 'IPCC', 'ONU']
for ict in icts:
    count = sum(1 for f in all_fichas if ict.lower() in f['path'].lower() or ict.lower() in f['author'].lower())
    if count > 0:
        lines.append(f"**{ict}**: {count} fichas\n")
        for f in all_fichas:
            if ict.lower() in f['path'].lower() or ict.lower() in f['author'].lower():
                lines.append(f"  - [{f['title'][:60]}]({BASE_URL}/{f['path']})")
                break

# 4. BY YEAR
lines.append("---\n## 4. POR DÉCADA\n")
decades = {}
for f in all_fichas:
    if f['year']:
        dec = f['year'][:3] + '0'
        decades.setdefault(dec, []).append(f)
for dec in sorted(decades.keys()):
    lines.append(f"**{dec}s**: {len(decades[dec])} fichas\n")

# 5. NAVIGATION GUIDE
lines.append("---\n## 5. GUIA DE NAVEGAÇÃO PARA AGENTES\n")
lines.append("| Para escrever sobre... | Consulte... |")
lines.append("|---|---|")
lines.append("| PU Vegetal / Imperveg | `01_polimeros/01_PU_Vegetal/` |")
lines.append("| Fibras vegetais e compósitos | `01_polimeros/02_Biocompositos/02A_Fibras_Reforco/` |")
lines.append("| Compósitos bambu+PU | `01_polimeros/02_Biocompositos/02B_BambuPU_Compósitos/` |")
lines.append("| Tratamento de bambu | `02_bambu/03_Tratamento_Preservacao/` |")
lines.append("| Propriedades do bambu | `02_bambu/02_Propriedades_Fisicas_Mecanicas/` |")
lines.append("| Construção / domos / BLC | `02_bambu/06_Construcao_Engenharia/` |")
lines.append("| HIS / CDHU / MCMV | `03_habitacao/01_HIS_CDHU_MCMV/` |")
lines.append("| ATHIS / Extensão | `03_habitacao/02_ATHIS_Extensao/02_ATHIS/` |")
lines.append("| Certificações ISO | `04_certificacoes/02_ISO/` |")
lines.append("| Normas NBR | `04_certificacoes/01_Normas_NBR/` |")
lines.append("| FISPQ | `04_certificacoes/03_FISPQ/` |")
lines.append("| Perfis de pesquisadores | `05_perfis/01_Pesquisadores/` |")
lines.append("| ICTs e instituições | `05_perfis/02_ICTs_Instituicoes/` |")
lines.append("| Empresas parceiras | `05_perfis/03_Empresas/` |")
lines.append("| Visão autoral do Fabio | `_VISAO_AUTORAL/` |")

lines.append(f"\n---\n*Catálogo gerado em {NOW} · {len(all_fichas)} fichas catalogadas*")

index_path = os.path.join(ACERVO, 'INDEX.md')
with open(index_path, 'w') as f:
    f.write('\n'.join(lines))
print(f"✅ INDEX.md regenerado com {len(all_fichas)} fichas")
