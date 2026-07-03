#!/Users/fabiotakwara/miniconda3/envs/whisper_env/bin/python3
"""Teste: buscar 'tratamento alcalino' e mostrar citacoes ABNT (sem links)"""
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

for i, (meta, dist) in enumerate(zip(results['metadatas'][0], results['distances'][0])):
    relevancia = f"{(1-dist)*100:.0f}%"
    arquivo = meta['arquivo']
    
    # Locate the file and extract ABNT citation
    fpath = None
    for area in sorted(os.listdir(ACERVO_DIR)):
        ap = os.path.join(ACERVO_DIR, area)
        if os.path.isdir(ap):
            tp = os.path.join(ap, arquivo)
            if os.path.exists(tp):
                fpath = tp
                break
    
    citacao_abnt = "[citacao nao encontrada]"
    autor_ano = ""
    
    if fpath:
        with open(fpath) as f:
            content = f.read()
        
        yaml_part = content.split('---')[1] if content.startswith('---') else ""
        cite_match = re.search(r'how_to_cite:\s*>\s*\n\s{2}(.+?)(?=\n\S|\Z)', yaml_part, re.DOTALL)
        if cite_match:
            citacao_abnt = cite_match.group(1).strip()
            citacao_abnt = re.sub(r'https?://[^\s]+', '', citacao_abnt).strip()
            citacao_abnt = re.sub(r'Dispon[íi]vel em:?\s*', '', citacao_abnt).strip()
            citacao_abnt = re.sub(r'\s+', ' ', citacao_abnt).strip()
            citacao_abnt = citacao_abnt.rstrip(',.;')
        
        # Extract author-year from citation
        autor_ano_match = re.match(r'^([A-ZÇÃÂÁÀÉÊÍÓÔÚÕ][a-zçãâáàéêíóôúõ]+(?:[\s,]+[A-Z][\.]?)?(?:[\s,]+[A-ZÇÃÂÁÀÉÊÍÓÔÚÕ][a-zçãâáàéêíóôúõ]+)*)\.?\s*\(?(\d{4})\)?', citacao_abnt)
        if autor_ano_match:
            autor_ano = f"({autor_ano_match.group(1).strip()}, {autor_ano_match.group(2)})"
        else:
            # Try simpler: just get first 30 chars + year
            ano_match = re.search(r'(\d{4})', citacao_abnt)
            autor_ano = f"(Documento interno, {ano_match.group(1) if ano_match else '2026'})"
    
    print(f"\n{'─'*80}")
    print(f"  [{i+1}] Relevância: {relevancia}")
    print(f"  {'─'*80}")
    print(f"  Citação completa (ABNT):")
    print(f"  {citacao_abnt}")
    print(f"  {'─'*80}")
    print(f"  No texto do formulário FINEP use:")
    print(f"  ... conforme estudos de tratamento alcalino {autor_ano} ...")
    print(f"  {'─'*80}")

print(f"\n{'='*80}")
print("BIBLIOGRAFIA (final do formulario FINEP):")
print(f"{'='*80}\n")
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
    citacao_abnt = "[nao encontrada]"
    if fpath:
        with open(fpath) as f:
            content = f.read()
        yaml_part = content.split('---')[1] if content.startswith('---') else ""
        cite_match = re.search(r'how_to_cite:\s*>\s*\n\s{2}(.+?)(?=\n\S|\Z)', yaml_part, re.DOTALL)
        if cite_match:
            citacao_abnt = cite_match.group(1).strip()
    
    print(f"  [{relevancia}] {citacao_abnt}")
