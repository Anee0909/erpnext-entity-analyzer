import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

query = input("Ask a question: ")

with open("texts.json") as f:
    texts = json.load(f)

embeddings = np.load("embeddings.npy")

query_embedding = model.encode([query])
scores = cosine_similarity(query_embedding, embeddings)[0]

best_idx = scores.argmax()

print("\n🔍 Most relevant retrieved context:")
print(texts[best_idx])
