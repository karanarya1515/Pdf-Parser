from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.IndexFlatL2(384)
chunk_list = []

def build_index(chunks):
    global chunk_list
    chunk_list = chunks
    embeddings = model.encode(chunks)
    index.add(np.array(embeddings).astype("float32"))

def search(query, k=3):
    q_embed = model.encode([query]).astype("float32")
    D, I = index.search(q_embed, k)
    return [chunk_list[i] for i in I[0]]
