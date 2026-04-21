import chromadb
from sentence_transformers import SentenceTransformer
from ingest import process_documents
from tqdm import tqdm

# Initialize embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize ChromaDB
client = chromadb.PersistentClient(path="index/chroma")
collection = client.get_or_create_collection("docs")


def main():
    chunks = process_documents()

    for i, chunk in enumerate(tqdm(chunks)):
        embedding = model.encode(chunk["text"]).tolist()

        collection.add(
            documents=[chunk["text"]],
            embeddings=[embedding],
            metadatas=[{"source": chunk["source"]}],
            ids=[str(i)]
        )

    print("✅ Stored embeddings in ChromaDB")


if __name__ == "__main__":
    main()