#!/Users/fabiotakwara/miniconda3/envs/whisper_env/bin/python3
"""Buscar fontes sobre: tratamento alcalino bambu, extrato pirolenhoso, PU vegetal adesao"""
import chromadb, os, re
from sentence_transformers import SentenceTransformer

CHROMA_DIR = "/Users/fabiotakwara/.chromadb"
ACERVO_DIR = "/Users/fabiotakwara/Documents/GitHub/acervo-soberania-tecnologica/docs/analises"

client = chromadb.PersistentClient(path=CHROMA_DIR)
model = SentenceTransformer('all-MiniLM-L6-v2')
collection = client.get_collection("acervo_cientifico")

queries = [
    "tratamento alcalino de bambu fibras adesao poliuretano vegetal",
    "extrato pirolenhoso acido ph neutralizacao tratamento alcalino bambu",
    "deterioracao fibras alcalinidade excessiva tratamento NaOH bambu",
    "adesao PU vegetal fibras bambu tratamento superficial",
]

for qi, query in enumerate(queries, 1):
    print(f"\n{'='*80}")
    print(f"📌 BUSCA {qi}: {query}")
    print(f"{'='*80}")
    
    results = collection.query(
        query_embeddings=model.encode(query).tolist(),
        n_results=3
    )
    
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
        content_summary = ""
        if fpath:
            with open(fpath) as f:
                content = f.read()
            yaml_part = content.split('---')[1] if content.startswith('---') else ""
            m = re.search(r'how_to_cite:\s*"([^"]+)"', yaml_part)
            if m:
                citacao = m.group(1).strip()
            # Get summary (section 3)
            sec3 = re.search(r'## 3\. RESUMO / SÍNTESE\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
            if sec3:
                summary = sec3.group(1).strip()
                content_summary = summary[:300]
        
        print(f"\n  [{i+1}] Relevância: {relevancia} | Arquivo: {arquivo}")
        print(f"  Citação: {citacao}")
        if content_summary:
            print(f"  Resumo: {content_summary}...")
