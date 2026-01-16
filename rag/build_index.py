import json
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("../output.json") as f:
    data = json.load(f)

texts = []

texts.append(f"Entity: {data['entity']}")

for field in data.get("fields", []):
    texts.append(f"Field: {field}")

for method in data.get("methods", []):
    texts.append(f"Method: {method}")

embeddings = model.encode(texts)

np.save("embeddings.npy", embeddings)

with open("texts.json", "w") as f:
    json.dump(texts, f, indent=2)

print("✅ RAG index built successfully")
