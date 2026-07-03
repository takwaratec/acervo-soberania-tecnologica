#!/Users/fabiotakwara/miniconda3/envs/whisper_env/bin/python3
"""Re-indexar ChromaDB com suporte a subdiretorios"""
import chromadb, os, re, hashlib
from sentence_transformers import SentenceTransformer

CHROMA_DIR = "/Users/fabiotakwara/.chromadb"
ACERVO_DIR = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica/docs/analises"

client = chromadb.PersistentClient(path=CHROMA_DIR)
model = SentenceTransformer('all-MiniLM-L6-v2')

try:
    client.delete_collection("acervo_cientifico")
    print("🗑️  Colecao antiga removida")
except:
    pass

collection = client.create_collection(name="acervo_cientifico")
print("📦 Nova colecao criada")

PREFIX_NOME = {
    'POL_': 'Polímeros Vegetais e Biocompósitos',
    'BAM_': 'Bambu Estrutural e Tratamentos',
    'SOC_': 'Habitação Social e ATHIS',
    'CER_': 'Certificações e Normas',
    'PER_': 'Perfis e Referências',
    'AUT_': 'Visão Autoral e Práxis',
}

total = 0
for area in sorted(os.listdir(ACERVO_DIR)):
    ap = os.path.join(ACERVO_DIR, area)
    if not os.path.isdir(ap) or (area.startswith('_') and area != '_VISAO_AUTORAL'):
        continue
    for root, dirs, files in os.walk(ap):
        for fname in sorted(files):
            if not fname.endswith('.md') or fname in ('index.md',):
                continue
            if fname.startswith('_'):
                continue
            
            fpath = os.path.join(root, fname)
            with open(fpath) as f:
                content = f.read()
            
            prefix = fname[:4]
            eixo_display = PREFIX_NOME.get(prefix, area)
            
            yaml_part = content.split('---')[1] if content.startswith('---') else ""
            m = re.search(r'how_to_cite:\s*"([^"]+)"', yaml_part)
            citacao = m.group(1).strip() if m else ""
            
            title = citacao.split('.')[0] if citacao else fname
            title = title.strip('"')
            
            body = content
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    body = parts[2]
            
            body_clean = re.sub(r'^#\s+.*$', '', body, flags=re.MULTILINE)
            body_clean = re.sub(r'[>|]', '', body_clean)
            body_clean = re.sub(r'\n{3,}', '\n\n', body_clean)
            
            doc_text = f"{citacao}\n\n{body_clean[:500]}"
            
            metadata = {
                'arquivo': fname,
                'eixo_original': eixo_display,
                'area': area,
                'citacao': citacao,
            }
            
            doc_id = hashlib.md5(fname.encode()).hexdigest()[:12]
            
            collection.add(
                documents=[doc_text],
                metadatas=[metadata],
                ids=[doc_id]
            )
            total += 1

print(f"✅ {total} fichas indexadas no ChromaDB")
print("Colecao: acervo_cientifico (re-indexada)")
