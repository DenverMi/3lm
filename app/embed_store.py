import json
import shutil
from sentence_transformers import SentenceTransformer
import chromadb
from tqdm import tqdm

from app.config import (
    CHUNKS_PATH,
    CHROMA_PATH,
    COLLECTION_NAME,
    EMBED_MODEL,
    ensure_directories,
)


def load_chunks():
    chunks = []

    with CHUNKS_PATH.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                chunks.append(json.loads(line))

    return chunks


def reset_chroma():
    if CHROMA_PATH.exists():
        shutil.rmtree(CHROMA_PATH)
    CHROMA_PATH.mkdir(parents=True, exist_ok=True)


def main():
    if not CHUNKS_PATH.exists():
        raise FileNotFoundError(f"Missing {CHUNKS_PATH}. Run chunk.py first.")

    ensure_directories()
    reset_chroma()

    print(f"Loading embedding model: {EMBED_MODEL}")
    model = SentenceTransformer(EMBED_MODEL)

    print(f"Loading chunks from: {CHUNKS_PATH}")
    chunks = load_chunks()
    print(f"Loaded {len(chunks)} chunks")

    client = chromadb.PersistentClient(path=str(CHROMA_PATH))
    collection = client.get_or_create_collection(COLLECTION_NAME)

    for chunk in tqdm(chunks, desc="Embedding chunks"):
        embedding = model.encode(chunk["text"]).tolist()

        collection.add(
            ids=[chunk["chunk_id"]],
            documents=[chunk["text"]],
            embeddings=[embedding],
            metadatas=[{
                "program": chunk["program"],
                "doc_type": chunk["doc_type"],
                "doc_name": chunk["doc_name"],
                "chunk_kind": chunk.get("chunk_kind"),
                "priority": chunk.get("priority", 0),
                "page_start": chunk["page_start"],
                "page_end": chunk["page_end"],
            }]
        )

    print(f"✅ Stored {len(chunks)} chunks in ChromaDB at {CHROMA_PATH}")


if __name__ == "__main__":
    main()