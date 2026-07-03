#!/Users/fabiotakwara/miniconda3/envs/whisper_env/bin/python3
"""Teste final - buscar 'tratamento alcalino' e mostrar citacoes ABNT limpas"""
import chromadb, os, re
from sentence_transformers import SentenceTransformer

CHROMA_DIR = "/Users/fabiotakwara/.chromadb"
ACERVO_DIR = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica/docs/analises"

client = chromadb.PersistentClient(path=CHROMA_DIR)
model = SentenceTransformer('all-MiniLM-L6-v2')
collection = client.get_collection("acervo_cientifico")

query = "tratamento alcalino de fibras vegetais para biocompositos"
results = collection.query(
    query_embeddings=model.encode(query).tolist(),
    n_results=5
)

print("=" * 80)
print("📌 BUSCA: tratamento alcalino de fibras vegetais para biocompositos")
print("=" * 80)
print()
print("RESULTADOS DA BUSCA SEMÂNTICA (por relevância):")
print()

for i, (meta, dist) in enumerate(zip(results['metadatas'][0], results['distances'][0])):
    relevancia = f"{(1-dist)*100:.0f}%"
    arquivo = meta['arquivo']
    
    # Find file and extract citation
    fpath = None
    for area in sorted(os.listdir(ACERVO_DIR)):
        ap = os.path.join(ACERVO_DIR, area)
        if os.path.isdir(ap):
            tp = os.path.join(ap, arquivo)
            if os.path.exists(tp):
                fpath = tp
                break
    
    citacao = ""
    if fpath:
        with open(fpath) as f:
            content = f.read()
        yaml_part = content.split('---')[1] if content.startswith('---') else ""
        m = re.search(r'how_to_cite:\s*"([^"]+)"', yaml_part)
        if m:
            citacao = m.group(1).strip()
    
    print(f"  [{i+1}] Relevância: {relevancia}")
    print(f"      Citação ABNT: {citacao}")
    print(f"      No texto: ... ({citacao.split('.')[0] if '.' in citacao else citacao[:40]}, {meta.get('eixo_original', '?')}) ...")
    print()

print()
print("=" * 80)
print("BIBLIOGRAFIA (final do formulário FINEP):")
print("=" * 80)
print()
for i, (meta, dist) in enumerate(zip(results['metadatas'][0], results['distances'][0])):
    relevancia = f"{(1-dist)*100:.0f}%"
    arquivo = meta['arquivo']
    fpath = None
    for area in sorted(os.listdir(ACERVO_DIR)):
        ap = os.path.join(ACERVO_DIR, area)
        if os.path.isdir(ap):
            tp = os.path.join(ap, arquivo)
            if os.path.exists(tp):
                fpath = tp
                break
    citacao = ""
    if fpath:
        with open(fpath) as f:
            content = f.read()
        yaml_part = content.split('---')[1] if content.startswith('---') else ""
        m = re.search(r'how_to_cite:\s*"([^"]+)"', yaml_part)
        if m:
            citacao = m.group(1).strip()
    print(f"  [{relevancia}] {citacao}")
