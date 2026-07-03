#!/Users/fabiotakwara/miniconda3/envs/whisper_env/bin/python3
"""
ESTEIRA DE TRIAGEM — /Users/fabiotakwara/Documents/Documentos
Processa PDFs e DOCXs científicos, cria fichas Cavichiolli, indexa no ChromaDB.
Gera relatório em _RELATORIO_TRIAGEM.md
"""
import os, re, subprocess, hashlib, json, shutil, fitz
from datetime import datetime

DOCS_DIR = "/Users/fabiotakwara/Documents/Documentos"
ACERVO_DIR = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica/docs/analises"
PROCESSED_DIR = os.path.join(ACERVO_DIR, "_pdfs_processados_para_revisao")
TEMP_DIR = os.path.join(ACERVO_DIR, "_temp_extracao")

os.makedirs(PROCESSED_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)

# Log
log = {"iniciado": datetime.now().isoformat(), "etapas": [], "erros": [], "criadas": [], "puladas": []}

def log_etapa(msg):
    log["etapas"].append(msg)
    print(f"  🌀 {msg}")

def log_erro(msg):
    log["erros"].append(msg)
    print(f"  ❌ {msg}")

# === ETAPA 1: INVENTARIAR ===
print("\n" + "="*70)
print("📋 ETAPA 1: INVENTARIAR PDFs CIENTIFICOS")
print("="*70)

# Scientific keywords to filter
SCIENTIFIC_KWS = ['bambu', 'pu vegetal', 'poliuretano', 'pirolenhoso', 'biochar', 'carvão',
                   'biocompósito', 'habitação', 'his', 'cdhu', 'mcmv', 'finep', 'carbono',
                   'sustentável', 'geodésica', 'briquetes', 'fitorremediação', 'inbar',
                   'guadua', 'tratamento', 'preservação', 'ácido', 'fibras', 'compósito',
                   'indústria ecológica', 'bambu ecologico', 'acv', 'ciclo de vida',
                   'dissertação', 'tese', 'mercado bambu', 'faO', 'sal graham',
                   'activated carbon', 'preservation', 'warka', 'bamboo']

scientific_files = []

for f in sorted(os.listdir(DOCS_DIR)):
    fpath = os.path.join(DOCS_DIR, f)
    if not os.path.isfile(fpath) or f.startswith('.'):
        continue
    
    ext = os.path.splitext(f)[1].lower()
    if ext not in ['.pdf', '.docx', '.doc']:
        continue
    
    fname_lower = f.lower()
    # Check if filename suggests scientific content
    if any(kw in fname_lower for kw in SCIENTIFIC_KWS):
        scientific_files.append((f, fpath, ext))
        continue
    
    # Check first page content for PDFs
    try:
        if ext == '.pdf':
            doc = fitz.open(fpath)
            first_page = doc[0].get_text()[:500].lower()
            doc.close()
            if any(kw in first_page for kw in SCIENTIFIC_KWS):
                scientific_files.append((f, fpath, ext))
    except:
        pass

log_etapa(f"Identificados {len(scientific_files)} arquivos científicos de {sum(1 for f in os.listdir(DOCS_DIR) if os.path.isfile(os.path.join(DOCS_DIR, f)) and not f.startswith('.'))} totais")

for f, fpath, ext in scientific_files:
    size = os.path.getsize(fpath)
    print(f"  📄 [{ext}] {f[:65]} ({size//1024}KB)")

# === ETAPA 2: VERIFICAR SE JA EXISTEM NO ACERVO ===
print(f"\n{'='*70}")
print("🔍 ETAPA 2: VERIFICAR DUPLICATAS NO ACERVO")
print("="*70)

existing_titles = set()
for area in sorted(os.listdir(ACERVO_DIR)):
    ap = os.path.join(ACERVO_DIR, area)
    if not os.path.isdir(ap) or area.startswith('_'):
        continue
    for fname in os.listdir(ap):
        existing_titles.add(fname.lower().replace('-', ' ').replace('_', ' '))

new_files = []
for f, fpath, ext in scientific_files:
    # Check by filename similarity
    f_clean = f.lower().replace('-', ' ').replace('_', ' ').replace('.pdf', '').replace('.docx', '').replace('.doc', '')
    is_dup = False
    for et in existing_titles:
        # Check if significant word overlap
        f_words = set(f_clean.split()[:5])
        et_words = set(et.split()[:5])
        common = f_words & et_words
        if len(common) >= 2 and len(common) >= len(f_words) * 0.3:
            is_dup = True
            break
    if not is_dup:
        new_files.append((f, fpath, ext))
    else:
        log["puladas"].append((f, "ja existe no Acervo"))

log_etapa(f"{len(new_files)} novos / {len(scientific_files) - len(new_files)} duplicatas puladas")
for f, _, _ in scientific_files[:len(scientific_files) - len(new_files)]:
    print(f"  ⏭️  {f[:65]} — já existe no Acervo")
for f, _, _ in new_files:
    print(f"  🆕 {f[:65]} — novo")

# === ETAPA 3: EXTRAIR TEXTO E GERAR FICHAS ===
print(f"\n{'='*70}")
print("📝 ETAPA 3: EXTRAIR TEXTO E GERAR FICHAS")
print("="*70)

fichas_criadas = 0
for f, fpath, ext in new_files:
    fname_stem = os.path.splitext(f)[0]
    # Create safe filename
    safe_name = re.sub(r'[^a-zA-Z0-9]', '-', fname_stem)[:60].strip('-').lower()
    if not safe_name:
        safe_name = hashlib.md5(f.encode()).hexdigest()[:12]
    
    # Determine target area based on content keywords
    f_lower = f.lower()
    if any(kw in f_lower for kw in ['bambu', 'guadua', 'phyllostachys', 'tratamento', 'preservação', 'biochar', 'carvão', 'pirolenhoso']):
        prefix = 'BAM'
        area = '02_bambu-estrutural-e-tratamentos'
    elif any(kw in f_lower for kw in ['pu vegetal', 'poliuretano', 'biocompósito', 'fibras', 'compósito', 'acv']):
        prefix = 'POL'
        area = '01_polimeros-vegetais-e-biocompositos'
    elif any(kw in f_lower for kw in ['habitação', 'his', 'cdhu', 'mcmv', 'domo', 'geodésica']):
        prefix = 'SOC'
        area = '03_habitacao-social-e-athis'
    elif any(kw in f_lower for kw in ['certificação', 'iso', 'norma', 'carbono']):
        prefix = 'CER'
        area = '04_certificacoes-e-normas'
    else:
        prefix = 'BAM'
        area = '02_bambu-estrutural-e-tratamentos'
    
    target_dir = os.path.join(ACERVO_DIR, area)
    ficha_name = f"{prefix}_{safe_name}.md"
    ficha_path = os.path.join(target_dir, ficha_name)
    
    # Extract text
    texto = ""
    try:
        if ext == '.pdf':
            doc = fitz.open(fpath)
            for page in doc:
                texto += page.get_text()
            doc.close()
        elif ext in ['.docx', '.doc']:
            # Try Pandoc
            txt_path = os.path.join(TEMP_DIR, f"{safe_name}.txt")
            subprocess.run(['pandoc', fpath, '-t', 'plain', '-o', txt_path], capture_output=True, timeout=30)
            if os.path.exists(txt_path):
                with open(txt_path) as fh:
                    texto = fh.read()
                os.remove(txt_path)
    except Exception as e:
        log_erro(f"Erro extraindo {f}: {e}")
        continue
    
    if not texto or len(texto) < 100:
        log_erro(f"{f}: texto extraído insuficiente ({len(texto)} chars)")
        continue
    
    # Extract metadata
    lines = texto.split('\n')
    title = fname_stem[:80]
    year = ''
    year_m = re.search(r'\b(19[0-9]{2}|20[0-9]{2})\b', texto[:500])
    if year_m: year = year_m.group(1)
    
    # Generate a simple citation
    if year:
        citacao = f"{title}. {year}."
    else:
        citacao = f"{title}."
    
    # Check if ficha already exists
    if os.path.exists(ficha_path):
        log_erro(f"{f}: ficha ja existe em {area}/{ficha_name}")
        continue
    
    # Create Cavichiolli 8-section ficha
    resume = texto[:500].strip().replace('\n', ' ')
    resume = re.sub(r'\s+', ' ', resume)[:500]
    
    ficha_content = f"""---
conversao_cavichiolli: {datetime.now().strftime('%Y-%m-%d')}
how_to_cite: "{citacao}"
origem: "{f} ({ext})"
status_pdf: "✅ Triado em {datetime.now().strftime('%Y-%m-%d')}"
---

# {title}

> Ficha gerada automaticamente pela esteira de triagem em {datetime.now().strftime('%d/%m/%Y')}.
> Fonte: `{f}` — extraído via PyMuPDF/Pandoc.

---

## 1. IDENTIFICAÇÃO

| Campo | Dado |
|-------|------|
| **Título** | {title} |
| **Ano** | {year} |
| **Fonte** | {f} |
| **Tamanho** | {os.path.getsize(fpath)//1024} KB |
| **Extraído em** | {datetime.now().strftime('%Y-%m-%d')} |
| **Status PDF** | ✅ Processado — movido para revisão |

---

## 2. CLASSIFICAÇÃO TEMÁTICA

- **Eixo:** {area}
- **Área:** {area.split('_', 1)[-1] if '_' in area else area}
- **Palavras-chave:** {', '.join([kw for kw in ['bambu', 'tratamento', 'PU', 'HIS', 'carbono'] if kw.lower() in texto.lower()])}

---

## 3. RESUMO / SÍNTESE

> {resume}

---

## 4. ANÁLISE CRÍTICA

| Aspecto | Avaliação |
|---------|-----------|
| **Relevância** | ⏳ Pendente de revisão manual |
| **Qualidade** | ✅ Texto extraído |
| **Completude** | ⏳ Pendente de revisão |

> Ficha gerada automaticamente. Recomenda-se revisão manual para preenchimento das seções 4-8.

---

## 5. DADOS EXTRAÍDOS / EVIDÊNCIAS

*Dados extraídos disponíveis no PDF original, movido para `_pdfs_processados_para_revisao/`.*

---

## 6. CONEXÕES COM OUTRAS FICHAS DO ACERVO

| Ficha | Tipo de Relação |
|-------|-----------------|
| [Índice do Acervo](../index.md) | Hierárquica |

---

## 7. APLICAÇÕES PRÁTICAS

- Pendente de análise manual

---

## 8. REFERÊNCIAS

- Documento original: `{f}`
- Extraído em {datetime.now().strftime('%Y-%m-%d')}

---

⚠️ *Nota de Compliance:* A engenharia de contexto e a lógica de estruturação deste documento foram inspiradas nas diretrizes metodológicas desenvolvidas pela **Dra. Nathalia Cavichiolli**. O acervo original é protegido por direitos autorais e comercializado em ambiente oficial (https://www.doutoranathalia.com.br/). Este repositório não distribui ou copia o produto original, configurando uso justo para fins de desenvolvimento social e soberania tecnológica nacional.

*Ficha catalográfica conforme método Cavichiolli (2025) · 8 seções · Documento gerado por esteira automática em {datetime.now().strftime('%d/%m/%Y')}*
"""
    
    with open(ficha_path, 'w') as fh:
        fh.write(ficha_content)
    
    fichas_criadas += 1
    log["criadas"].append((f, ficha_name, area))
    print(f"  ✅ Ficha criada: {area}/{ficha_name}")
    
    # Move processed PDF to review dir
    review_path = os.path.join(PROCESSED_DIR, f)
    shutil.copy2(fpath, review_path)
    print(f"     📦 Copiado para revisão: {review_path}")

log_etapa(f"Fichas criadas: {fichas_criadas}")

# === ETAPA 4: REINDEXAR CHROMADB ===
print(f"\n{'='*70}")
print("🔄 ETAPA 4: REINDEXAR CHROMADB")
print("="*70)

log_etapa("Reindexando ChromaDB (pode levar ~10 min)...")
try:
    result = subprocess.run(
        ['/Users/fabiotakwara/miniconda3/envs/whisper_env/bin/python3',
         os.path.join(ACERVO_DIR, '_reindexar_acervo.py')],
        capture_output=True, text=True, timeout=600
    )
    log_etapa(f"ChromaDB reindexado: {result.stdout.strip()[-100:]}")
except Exception as e:
    log_erro(f"Erro no ChromaDB: {e}")

# === ETAPA 5: GERAR RELATORIO ===
print(f"\n{'='*70}")
print("📊 ETAPA 5: GERAR RELATORIO")
print("="*70)

report_path = os.path.join(ACERVO_DIR, "_RELATORIO_TRIAGEM.md")

# Count total fichas
total_fichas = 0
per_area = {}
for area in sorted(os.listdir(ACERVO_DIR)):
    ap = os.path.join(ACERVO_DIR, area)
    if not os.path.isdir(ap) or area.startswith('_'):
        continue
    n = sum(1 for f in os.listdir(ap) if f.endswith('.md') and not f.startswith('_') and f != 'index.md')
    total_fichas += n
    per_area[area] = n

report = f"""# 📊 Relatório de Triagem — {datetime.now().strftime('%d/%m/%Y %H:%M')}

> Processamento de `/Users/fabiotakwara/Documents/Documentos`
> Executado por Hermes Agent · Esteira automática

---

## 1. Inventário

| Item | Valor |
|------|-------|
| Total de arquivos no diretório | {sum(1 for f in os.listdir(DOCS_DIR) if os.path.isfile(os.path.join(DOCS_DIR, f)) and not f.startswith('.'))} |
| Arquivos científicos identificados | {len(scientific_files)} |
| Já existentes no Acervo (pulados) | {len(scientific_files) - len(new_files)} |
| **Novos processados** | **{fichas_criadas}** |

## 2. Arquivos Científicos Encontrados

| Status | Arquivo | Tamanho |
|--------|---------|---------|
"""
for f, fpath, ext in scientific_files:
    size = os.path.getsize(fpath)
    if os.path.exists(os.path.join(PROCESSED_DIR, f)):
        report += f"| ✅ Processado | {f[:60]} | {size//1024}KB |\n"
    else:
        report += f"| ⏭️  Duplicata | {f[:60]} | {size//1024}KB |\n"

report += f"""
## 3. Fichas Criadas

| # | Ficha | Área | Origem |
|---|---|---|---|
"""
for i, (orig, fname, area) in enumerate(log["criadas"], 1):
    area_name = area.split('_', 1)[-1] if '_' in area else area
    report += f"| {i} | `{fname}` | {area_name} | `{orig}` |\n"

report += f"""
## 4. PDFs Processados

Os PDFs processados foram copiados para:
```
{PROCESSED_DIR}/
```
Lá você pode inspecionar, deletar ou manter conforme sua avaliação.

## 5. Estado do Acervo

| Área | Fichas |
|------|--------|
"""
for area, n in sorted(per_area.items()):
    area_name = area.split('_', 1)[-1] if '_' in area else area
    report += f"| {area_name} | {n} |\n"

report += f"""
| **Total** | **{total_fichas}** |

## 6. Erros e Observações

| Erro |
|------|
"""
if log["erros"]:
    for e in log["erros"]:
        report += f"| {e} |\n"
else:
    report += "| Nenhum erro registrado |\n"

report += f"""
## 7. Ações Pendentes

- [ ] Revisar fichas geradas (seções 4-8 estão vazias)
- [ ] Verificar PDFs em `_pdfs_processados_para_revisao/`
- [ ] Deletar PDFs confirmados ou manter como referência
- [ ] Preencher metadados (autor, DOI) nas novas fichas

---

*Relatório gerado em {datetime.now().strftime('%d/%m/%Y %H:%M')} · Hermes Agent*
"""

with open(report_path, 'w') as f:
    f.write(report)

log_etapa(f"Relatório salvo em {report_path}")
print(f"\n✅ ESTEIRA CONCLUÍDA — {fichas_criadas} fichas criadas")
