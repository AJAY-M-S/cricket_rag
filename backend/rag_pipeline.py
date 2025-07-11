# rag_pipeline.py
import faiss
from sentence_transformers import SentenceTransformer
import numpy as np
from utils import normalize_query

model = SentenceTransformer("all-MiniLM-L6-v2")
def load_index():
    index = faiss.read_index("faiss_store/cricket.index")
    with open("faiss_store/texts.txt", "r", encoding="utf-8") as f:
        texts = f.read().splitlines()
    return index, texts

def search_query(query, top_k=1):
    query = normalize_query(query)
    emb = model.encode([query])
    index, texts = load_index()
    D, I = index.search(emb, top_k)

    # Take top-1 result only
    top_text = texts[I[0][0]]

    # Split and extract details
    match = {}
    for segment in top_text.split(" | "):
        if ':' in segment:
            key, value = segment.split(":", 1)
            match[key.strip()] = value.strip()
        
    

    
    return match
