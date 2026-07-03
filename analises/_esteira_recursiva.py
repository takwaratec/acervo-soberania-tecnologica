#!/Users/fabiotakwara/miniconda3/envs/whisper_env/bin/python3
"""
ESTEIRA RECURSIVA — varre todos os subdiretórios de Documentos/
Pula diretórios administrativos explícitos. Cria fichas Cavichiolli para conteúdo científico.
"""
import os, re, subprocess, hashlib, fitz, shutil
from datetime import datetime

DOCS_DIR = "/Users/fabiotakwara/Documents/Documentos"
ACERVO_DIR = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica/docs/analises"
PROCESSED_DIR = os.path.join(ACERVO_DIR, "_pdfs_processados_para_revisao")
TEMP_DIR = os.path.join(ACERVO_DIR, "_temp_extracao")
os.makedirs(PROCESSED_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)

# Diretórios a pular integralmente (administrativo/fiscal/pessoal)
SKIP_DIRS = {'Contabilidade', 'NF Emitidas', 'NF Pagas', 'NF-e', 'Guias', 'Extratos',
             'SERPRO', 'BINANCE', 'Gerencianet', 'Mercado Pago', 'certificado digital',
             'CNPJ A1', 'Certificados de raiz', 'Neoid', 'KOMBI', 'Docs Pessoais',
             'Contas pagas', 'Fotos', 'Banners', 'XML', 'Fotos Satel', 'Cadastro CURITIBA',
             'Clientes/Coca-cola', 'Docs Ravi', 'Docs empresa', 'Estrada Real',
             'Transfêrencia PDF livro Pelos caminhos da tambatajá',
             'Copos japoneses_files', 'Inst Localiza', 'Stats Medium',
             'Tablaturas- Fingerstyle', 'Cliches', 'Erros sistema', 'BancoSocial',
             'Hotmart Cursos', 'MALELI', 'Rafael Schardosim', 'Serpro',
             'Movimento Ravi', 'Flavio', '++++Docs Defesa Qualificação Técnica',
             'edital BB', 'CRV - ALuguel', '+CRV - ALuguel', '+Zayed Prize'}

SCIENTIFIC_KWS = ['bambu', 'pu vegetal', 'poliuretano', 'pirolenhoso', 'biochar', 'carvão',
                   'biocompósito', 'habitação', 'his', 'cdhu', 'finep', 'carbono', 'geodésica',
                   'briquetes', 'fitorremediação', 'inbar', 'guadua', 'tratamento', 'preservação',
                   'ácido', 'fibras', 'compósito', 'dissertação', 'tese', 'mercado bambu',
                   'activated carbon', 'preservation', 'bamboo', 'fispq', 'ensaio',
                   'norma', 'nbr', 'iso', 'acv', 'ciclo de vida', 'imperveg',
                   'phyllostachys', 'dendrocalamus', 'bambusa', 'guadua',
                   'sustentável', 'ecological', 'charcoal', 'biochar',
                   'pinus', 'eucalipto', 'madeira', 'floresta', 'reflorestamento',
                   'ifb', 'instituto federal', 'relatório final', 'bibliografia',
                   'morin', 'freire', 'darcy ribeiro', 'permacultura', 'mollison',
                   'holmgren', 'van lengen', 'milton santos', 'krenak', 'bueno',
                   'carlos nobre', 'pedagogia', 'complexidade', 'soberania',
                   'territorio usado', 'geografia critica', 'outra globalizacao',
                   'cemaden', 'undrr', 'desastres', 'vulnerabilidade', 'risco climatico',
                   'nasa impact', 'hot osm', 'climate change ai', 'abrigo emergencial']

log = {"iniciado": datetime.now().isoformat(), "etapas": [], "erros": [], "criadas": [], "puladas": []}

def log_etapa(msg):
    log["etapas"].append(msg)
    print(f"  🌀 {msg}")

def log_erro(msg):
    log["erros"].append(msg)
    print(f"  ❌ {msg}")

def should_skip_dir(dirpath):
    parts = dirpath.replace(DOCS_DIR, '').split(os.sep)
    for p in parts:
        if p in SKIP_DIRS:
            return True
    return False

def is_scientific(name, content_preview=""):
    name_lower = name.lower()
    if any(kw in name_lower for kw in SCIENTIFIC_KWS):
        return True
    if content_preview and any(kw in content_preview.lower() for kw in SCIENTIFIC_KWS):
        return True
    return False

# === ETAPA 1: INVENTARIAR RECURSIVO ===
print("="*70)
print("📋 ETAPA 1: VARREDURA RECURSIVA")
print("="*70)

found_files = []
total_scanned = 0

for root, dirs, files in os.walk(DOCS_DIR):
    if should_skip_dir(root):
        continue
    for f in sorted(files):
        if f.startswith('.') or f == '.DS_Store':
            continue
        ext = os.path.splitext(f)[1].lower()
        if ext not in ['.pdf', '.docx', '.doc']:
            continue
        
        fpath = os.path.join(root, f)
        total_scanned += 1
        
        # Quick check by filename
        if is_scientific(f):
            found_files.append((f, fpath, ext, root))
            continue
        
        # Quick check by first page for PDFs
        try:
            if ext == '.pdf' and os.path.getsize(fpath) < 50*1024*1024:  # < 50MB
                doc = fitz.open(fpath)
                first_page = doc[0].get_text()[:300].lower()
                doc.close()
                if is_scientific(f, first_page):
                    found_files.append((f, fpath, ext, root))
                    continue
        except:
            pass

log_etapa(f"Escaneados {total_scanned} arquivos em {sum(1 for _,d,_ in os.walk(DOCS_DIR) for _ in d)} diretórios")
log_etapa(f"Identificados {len(found_files)} arquivos com potencial científico")

for f, fpath, ext, root in found_files:
    rel = os.path.relpath(root, DOCS_DIR)
    size = os.path.getsize(fpath)
    print(f"  📄 {rel[:35]:35s} | [{ext}] {f[:55]} ({size//1024}KB)")

# === ETAPA 2: VERIFICAR DUPLICATAS E CRIAR FICHAS ===
print(f"\n{'='*70}")
print("📝 ETAPA 2: EXTRAIR E CRIAR FICHAS")
print("="*70)

existing_fichas = set()
for area in sorted(os.listdir(ACERVO_DIR)):
    ap = os.path.join(ACERVO_DIR, area)
    if not os.path.isdir(ap) or area.startswith('_'):
        continue
    for fn in os.listdir(ap):
        existing_fichas.add(fn.lower().replace('-', ' ').replace('_', ' '))

fichas_criadas = 0
fichas_puladas = 0

for f, fpath, ext, root in sorted(found_files, key=lambda x: os.path.getsize(x[1])):
    fname_stem = os.path.splitext(f)[0]
    safe_name = re.sub(r'[^a-zA-Z0-9]', '-', fname_stem)[:60].strip('-').lower()
    if not safe_name:
        safe_name = hashlib.md5(f.encode()).hexdigest()[:12]
    
    # Target area
    f_lower = f.lower()
    if any(kw in f_lower for kw in ['bambu', 'guadua', 'phyllostachys', 'tratamento', 'pirolenhoso', 'preservação', 'charcoal', 'carvão']):
        prefix, area = 'BAM', '02_bambu-estrutural-e-tratamentos'
    elif any(kw in f_lower for kw in ['pu vegetal', 'poliuretano', 'biocompósito', 'fibras', 'compósito', 'acv', 'imperveg']):
        prefix, area = 'POL', '01_polimeros-vegetais-e-biocompositos'
    elif any(kw in f_lower for kw in ['habitação', 'his', 'domo', 'geodésica']):
        prefix, area = 'SOC', '03_habitacao-social-e-athis'
    elif any(kw in f_lower for kw in ['norma', 'nbr', 'iso', 'fispq', 'ensaio']):
        prefix, area = 'CER', '04_certificacoes-e-normas'
    elif any(kw in f_lower for kw in ['ifb', 'relatório final', 'bibliografia']):
        prefix, area = 'PER', '05_perfis-e-referencias'
    else:
        prefix, area = 'BAM', '02_bambu-estrutural-e-tratamentos'
    
    target_dir = os.path.join(ACERVO_DIR, area)
    ficha_name = f"{prefix}_{safe_name}.md"
    ficha_path = os.path.join(target_dir, ficha_name)
    
    # Check duplicate
    f_clean = f.lower().replace('-', ' ').replace('_', ' ').replace('.pdf', '').replace('.docx', '').replace('.doc', '')
    is_dup = False
    for ef in existing_fichas:
        fw = set(f_clean.split()[:5])
        ew = set(ef.split()[:5])
        if len(fw & ew) >= 2 and len(fw & ew) >= len(fw) * 0.3:
            is_dup = True
            break
    
    if is_dup or os.path.exists(ficha_path):
        fichas_puladas += 1
        log["puladas"].append((f, "duplicata"))
        continue
    
    # Extract text
    texto = ""
    try:
        if ext == '.pdf':
            doc = fitz.open(fpath)
            for page in doc:
                texto += page.get_text()
            doc.close()
        elif ext in ['.docx', '.doc']:
            txt_path = os.path.join(TEMP_DIR, f"{safe_name}.txt")
            subprocess.run(['pandoc', fpath, '-t', 'plain', '-o', txt_path], capture_output=True, timeout=30)
            if os.path.exists(txt_path):
                with open(txt_path) as fh:
                    texto = fh.read()
                os.remove(txt_path)
    except Exception as e:
        log_erro(f"{f}: erro extração - {e}")
        continue
    
    if not texto or len(texto) < 100:
        log_erro(f"{f}: texto insuficiente ({len(texto)} chars) — provavelmente escaneado")
        continue
    
    # Build ficha
    lines = texto.split('\n')
    title = fname_stem[:80]
    year = ''
    year_m = re.search(r'\b(19[0-9]{2}|20[0-9]{2})\b', texto[:500])
    if year_m: year = year_m.group(1)
    
    citacao = f"{title}. {year}." if year else f"{title}."
    resume = re.sub(r'\s+', ' ', texto[:500].strip())
    rel_dir = os.path.relpath(root, DOCS_DIR)
    
    # Extract keywords found
    found_kws = [kw for kw in ['bambu', 'tratamento', 'PU', 'HIS', 'carbono', 'ensaio', 'norma', 'fibras', 'biochar', 'pirolenhoso', 'imperveg', 'ifb', 'biocompósito'] if kw.lower() in texto.lower()]
    
    ficha_content = f"""---
conversao_cavichiolli: {datetime.now().strftime('%Y-%m-%d')}
how_to_cite: "{citacao}"
origem: "{rel_dir}/{f}"
status_pdf: "✅ Triado em {datetime.now().strftime('%Y-%m-%d')}"
---

# {title}

> Ficha gerada automaticamente pela esteira recursiva em {datetime.now().strftime('%d/%m/%Y')}.
> Fonte: `{rel_dir}/{f}` — extraído via PyMuPDF/Pandoc.

---

## 1. IDENTIFICAÇÃO

| Campo | Dado |
|-------|------|
| **Título** | {title} |
| **Ano** | {year} |
| **Fonte** | {f} |
| **Diretório** | {rel_dir} |
| **Tamanho** | {os.path.getsize(fpath)//1024} KB |
| **Extraído em** | {datetime.now().strftime('%Y-%m-%d')} |

---

## 2. CLASSIFICAÇÃO TEMÁTICA

- **Eixo:** {area}
- **Palavras-chave:** {', '.join(found_kws) if found_kws else 'geral'}

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

> Ficha gerada automaticamente. Revisão manual necessária para seções 4-8.

---

## 5. DADOS EXTRAÍDOS / EVIDÊNCIAS

*Dados disponíveis no PDF original, copiado para `_pdfs_processados_para_revisao/`.*

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

- Documento original: `{rel_dir}/{f}`
- Extraído em {datetime.now().strftime('%Y-%m-%d')}

---

⚠️ *Nota de Compliance:* [...] conforme método Cavichiolli (2025) · 8 seções · Documento gerado em {datetime.now().strftime('%d/%m/%Y')}*
"""
    
    with open(ficha_path, 'w') as fh:
        fh.write(ficha_content)
    
    fichas_criadas += 1
    log["criadas"].append((f, ficha_name, area, rel_dir))
    print(f"  ✅ Ficha: {area}/{ficha_name}")
    
    # Copy to review dir
    review_path = os.path.join(PROCESSED_DIR, f"{rel_dir.replace('/','_')}_{f}")
    shutil.copy2(fpath, review_path)

log_etapa(f"Fichas criadas: {fichas_criadas} | Puladas (duplicatas/erro): {fichas_puladas}")

# === ETAPA 3: REINDEXAR ===
print(f"\n{'='*70}")
print("🔄 ETAPA 3: REINDEXAR CHROMADB")
print("="*70)
log_etapa("Reindexando...")
try:
    result = subprocess.run(
        ['/Users/fabiotakwara/miniconda3/envs/whisper_env/bin/python3',
         os.path.join(ACERVO_DIR, '_reindexar_acervo.py')],
        capture_output=True, text=True, timeout=600
    )
    log_etapa(f"ChromaDB: {result.stdout.strip()[-80:]}")
except Exception as e:
    log_erro(f"Erro ChromaDB: {e}")

# === ETAPA 4: RELATORIO ===
print(f"\n{'='*70}")
print("📊 ETAPA 4: RELATORIO")
print("="*70)

total_fichas = sum(1 for _,_,fs in os.walk(ACERVO_DIR) for f in fs 
                   if f.endswith('.md') and not f.startswith('_') and f != 'index.md')

rel_path = os.path.join(ACERVO_DIR, "_RELATORIO_TRIAGEM_RECURSIVA.md")
report = f"""# 📊 Relatório de Triagem Recursiva — {datetime.now().strftime('%d/%m/%Y %H:%M')}

> Varredura completa de `/Users/fabiotakwara/Documents/Documentos` e subdiretórios
> Ignorados diretórios administrativos: Contabilidade, NFs, Certificados, etc.

---

## 1. Inventário

| Item | Valor |
|------|-------|
| Arquivos escaneados | {total_scanned} |
| Potencial científico | {len(found_files)} |
| Fichas criadas | **{fichas_criadas}** |
| Duplicatas/erros | {fichas_puladas} |
| **Total Acervo** | **{total_fichas}** |

## 2. Fichas Criadas

| # | Área | Ficha | Origem |
|---|---|---|---|
"""
for i, (orig, fname, area, rel_dir) in enumerate(log["criadas"], 1):
    area_name = area.split('_', 1)[-1] if '_' in area else area
    report += f"| {i} | {area_name} | `{fname}` | `{rel_dir}` |\n"

report += f"""
## 3. Diretórios Visitados

| Diretório | Status |
|-----------|--------|
"""
visited = set()
for _, _, _, rel_dir in log["criadas"]:
    if rel_dir not in visited:
        visited.add(rel_dir)
        report += f"| `{rel_dir}` | ✅ Processado |\n"

report += f"""
## 4. PDFs para Revisão

```
{PROCESSED_DIR}/
```

## 5. Erros

| Erro |
|------|
"""
for e in log["erros"]:
    report += f"| {e} |\n"
if not log["erros"]:
    report += "| Nenhum |\n"

report += f"""
## 6. Ações Pendentes

- [ ] Revisar fichas geradas (seções 4-8)
- [ ] Verificar PDFs em `_pdfs_processados_para_revisao/`
- [ ] Deletar ou manter PDFs
- [ ] Preencher metadados (autor, DOI)

---

*Relatório gerado em {datetime.now().strftime('%d/%m/%Y %H:%M')} · Hermes Agent*
"""

with open(rel_path, 'w') as f:
    f.write(report)

log_etapa(f"Relatório: {rel_path}")
print(f"\n✅ ESTEIRA RECURSIVA CONCLUÍDA — {fichas_criadas} fichas criadas | Total Acervo: {total_fichas}")
