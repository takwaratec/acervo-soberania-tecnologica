#!/Users/fabiotakwara/miniconda3/envs/whisper_env/bin/python3
"""Teste de citacao para proposta FINEP"""
import chromadb, os, re, json
from sentence_transformers import SentenceTransformer

CHROMA_DIR = "/Users/fabiotakwara/.chromadb"
ACERVO_DIR = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica/docs/analises"

client = chromadb.PersistentClient(path=CHROMA_DIR)
model = SentenceTransformer('all-MiniLM-L6-v2')
collection = client.get_collection("acervo_cientifico")

temas = [
    "tratamento de bambu com pirolenhoso para construcao civil",
    "poliuretano vegetal de mamona impermeabilizante",
    "deficit habitacional habitacao social Brasil",
    "certificacao LEED construcao sustentavel",
]

print("🔍 TESTE DE CITACAO PARA PROPOSTA FINEP\n")

for tema in temas:
    results = collection.query(
        query_embeddings=model.encode(tema).tolist(),
        n_results=1
    )
    
    meta = results['metadatas'][0][0]
    dist = results['distances'][0][0]
    arquivo = meta['arquivo']
    
    # Find the actual file
    fpath = None
    for area in sorted(os.listdir(ACERVO_DIR)):
        ap = os.path.join(ACERVO_DIR, area)
        if os.path.isdir(ap):
            test_path = os.path.join(ap, arquivo)
            if os.path.exists(test_path):
                fpath = test_path
                break
    
    print(f"\n📌 '{tema}'")
    print(f"   Relevância: {1-dist:.1%}")
    print(f"   Arquivo: {arquivo}")
    
    if fpath:
        with open(fpath) as f:
            content = f.read()
        
        # Extract citation
        yaml_part = content.split('---')[1] if content.startswith('---') else ""
        cite_match = re.search(r'how_to_cite:\s*>\s*\n\s{2}(.+?)(?=\n\S|\Z)', yaml_part, re.DOTALL)
        citacao = cite_match.group(1).strip() if cite_match else "Nao encontrada"
        
        print(f"   📖 Citação ABNT:")
        print(f"      {citacao}")
        
        rel_path = fpath.replace(ACERVO_DIR, 'docs/analises')
        print(f"   🔗 https://github.com/takwaratec/acervo-soberania-tecnologica/blob/main/{rel_path}")

print("\n✅ Sistema validado!")
