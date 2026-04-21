import os
from pypdf import PdfReader

DATA_DIR = "data/tech_reports"  # start with one folder

def load_pdfs(folder):
    documents = []

    for filename in os.listdir(folder):
        if filename.endswith(".pdf"):
            path = os.path.join(folder, filename)
            reader = PdfReader(path)

            text = ""
            for page in reader.pages:
                if page.extract_text():
                    text += page.extract_text()

            documents.append({
                "source": filename,
                "content": text
            })

    return documents


def chunk_text(text, chunk_size=500, overlap=50):
    # If text is short (like FAQ), keep it as one chunk
    if len(text) < 800:
        return [text]

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks


def process_documents():
    docs = load_pdfs(DATA_DIR)

    all_chunks = []

    for doc in docs:
        chunks = chunk_text(doc["content"])
        for chunk in chunks:
            all_chunks.append({
                "text": chunk,
                "source": doc["source"]
            })

    return all_chunks


if __name__ == "__main__":
    chunks = process_documents()
    print(f"Loaded {len(chunks)} chunks")