import json
import numpy as np
from sentence_transformers import SentenceTransformer
import os
from query import cosine

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Resolve rag directory
RAG_DIR = os.path.dirname(os.path.abspath(__file__))

# Load texts and embeddings
with open(os.path.join(RAG_DIR, "texts.json")) as f:
    texts = json.load(f)

embeddings = np.load(os.path.join(RAG_DIR, "embeddings.npy"))

# Load evaluation questions
with open(os.path.join(RAG_DIR, "evaluation.json")) as f:
    tests = json.load(f)

def retrieve(question):
    query_embedding = model.encode([question])[0]
    scores = [cosine(query_embedding, emb) for emb in embeddings]
    best_idx = int(np.argmax(scores))
    return texts[best_idx]

correct = 0
total = len(tests)

print("\n🧪 Running RAG Accuracy Evaluation...\n")

for test in tests:
    result = retrieve(test["question"])
    print(f"Question: {test['question']}")
    print("Retrieved:", result)

    if test["expected_keyword"].lower() in result.lower():
        correct += 1
        print("✅ Correct\n")
    else:
        print("❌ Wrong\n")

accuracy = (correct / total) * 100
print(f"🎯 Final Accuracy: {accuracy:.2f}%")

