import chromadb
from sentence_transformers import SentenceTransformer
import ollama

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load persistent DB
client = chromadb.PersistentClient(path="index/chroma")
collection = client.get_collection("docs")


def query_docs(query, n_results=5):
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results


def build_context(results):
    context = ""
    sources = []

    for i, doc in enumerate(results["documents"][0]):
        source = results["metadatas"][0][i]["source"]
        context += f"\nSource: {source}\n{doc}\n"
        sources.append(source)

    return context, list(set(sources))


def ask_llm(question, context):
    prompt = f"""
You are an internal technical consultant.

Answer the user's question using the provided INTERNAL EVIDENCE first.

Rules:
- Use INTERNAL EVIDENCE as the primary source.
- Do not present assumptions as facts.
- If a step or detail is not clearly supported by the INTERNAL EVIDENCE, say:
  "Not clearly specified in retrieved internal evidence."
- Only add a separate section called "General knowledge (model-based)" if internal evidence is weak or incomplete.
- Never mix internal evidence and general knowledge in the same paragraph.
- Be concise, structured, and factual.
- When possible, mention the source document name alongside key points.

QUESTION:
{question}

INTERNAL EVIDENCE:
{context}

Required output format:

Internal Evidence:
- ...

General knowledge (model-based):
- ...   (only if needed)

ANSWER:
"""

    response = ollama.chat(
        model="qwen3:8b",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]


if __name__ == "__main__":
    user_query = input("Ask a question: ")

    results = query_docs(user_query)
    context, sources = build_context(results)

    answer = ask_llm(user_query, context)

    print("\n=== ANSWER ===\n")
    print(answer)

    print("\n=== SOURCES ===\n")
    for s in sources:
        print("-", s)