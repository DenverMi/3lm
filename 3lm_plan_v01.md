# 🧠 Internal LLM Consultant – Project Plan (V1)

## 🎯 Objective
Build a **local LLM-powered internal consultant** that:
- Uses company knowledge (testing, standards, reports)
- Provides reliable, citation-based answers
- Distinguishes between:
  - Internal company evidence
  - General model knowledge

---
## 🧭 Core Design Philosophy

This is NOT a chatbot.

This is a:
> **Retrieval-first technical authority system with AI augmentation**

---
## 🧠 Key Design Features
1. Program-aware system
- Supports multiple standards/frameworks
- Easy expansion without redesign

2. Document-type awareness
- FAQ → prioritized for definitions
- Specs → detailed technical reference
- Reports → historical evidence

3. Page-level traceability
- Every answer can be traced to:
    document
    page range
4. Separation of knowledge

Every answer must follow:
  Internal Evidence:
  ...
  General knowledge (model-based):
  ...

---
## 🧱 System Behavior Rules

Every response must follow this structure:
Documents → Pages → Chunks → Embeddings → Retrieval → LLM Answer

### 1. Internal Evidence (Primary)
- Retrieved from company documents
- Treated as authoritative
- Prefer multiple sources when possible

### 2. General Knowledge (Model-Based)
- Used only when internal data is weak or missing
- Clearly labeled as:
  > General knowledge (model-based)

### 3. Strict Separation
- Never mix internal and model knowledge in the same paragraph
- Always clearly distinguish the source

### 4. Missing Evidence Handling
If internal data is insufficient:
> "No strong internal evidence found. Providing general background below."

---
## 🧠 Model Strategy

### Selected Model Family
- **Qwen 3** (via Ollama)

### Initial Model
- `qwen3:14b`

### Why
- Strong reasoning + technical capability
- Good multilingual support
- Optimized for Ollama + Apple MLX
- Fits well within M1 Max (64GB RAM)

### Cost
- $0 (runs locally)
- No API usage
- Cost is only local compute and storage

---

## 🧩 System Architecture (V1)

Pipeline:

```
Documents → Chunking → Embeddings → Vector DB → LLM → Structured Answer
```

Components:
- **Ollama** → LLM execution
- **Qwen 3 (14B)** → reasoning + generation
- **Embedding model** → document search
- **ChromaDB** → vector storage
- **Python backend** → orchestration logic

---

## 📂 Data Scope (V1)

### Included (Phase 1)
- Lab procedures / SOPs
- Past certification reports
- Technical reports / standards summaries

### Deferred (Phase 2)
- Emails
- Raw Excel/test data
- Internal wiki / Notion

---

## 📁 Project Structure

3lm/
  app/
    config.py
    ingest.py
    chunk.py
    embed_store.py
    retrieve.py
    answer.py
    cli.py

  data/
    programs/
      aliro/
        specs/
        policies/
        manuals/
        faqs/
        reports/
      matter/
      wifi/

  storage/
    pages.jsonl
    chunks.jsonl

  index/
    chroma/

  prompts/
    answer_prompt.txt

  tests/

  requirements.txt
  README.md

---

## ⚙️ Development Phases

### V1a – CLI Prototype

Goals:
- Ask questions via terminal
- Retrieve relevant document chunks
- Generate structured responses
- Show citations

---
## Program-Based Structure
Program-Based Structure

Each program has its own folder:
- aliro
- matter
- wifi
- (future: usb, bluetooth, nfc, iso17025, etc.)

Document Types
Each program contains:
- specs
- policies
- manuals
- faqs
- reports
- emails

---
## Storage Layers
1. pages.jsonl (Raw extraction)
{
  "program": "aliro",
  "doc_type": "faqs",
  "doc_name": "Aliro_FAQ.pdf",
  "page": 1,
  "text": "Aliro is a standardized credential..."
}

2. chunks.jsonl (Processed knowledge)
Each chunk includes:
{
  "chunk_id": "aliro:Aliro_FAQ:c00001",
  "program": "aliro",
  "doc_type": "faqs",
  "doc_name": "Aliro_FAQ.pdf",
  "page_start": 1,
  "page_end": 2,
  "text": "Aliro is a standardized credential..."
}

3. Vector Index (index/chroma/)
- Stores embeddings
- Enables semantic search
- Persistent across runs

---
## Application Modules

### config.py
- Paths
- Model settings
- Chunk sizes

### ingest.py
- Extracts text from documents
- Outputs page-level records

### chunk.py
- Converts pages → chunks
- Preserves page ranges
- Applies document-type logic

### embed_store.py
- Converts chunks → embeddings
- Stores in ChromaDB

### retrieve.py
- Searches vector DB
- Applies ranking logic
- Handles document-type prioritization (e.g., FAQ boost)

### answer.py
- Sends context to LLM (Qwen)
- Enforces:
- Internal evidence first
- Strict separation from model knowledge

### cli.py
- Entry point for terminal usage
- Used for demo

---
### V1b – Demo Interface

Purpose: Demonstration for stakeholders

Features:
- Simple browser-based chat UI
- Display:
  - Internal Evidence
  - General Knowledge
  - Source references

---

## 🧪 Success Criteria (V1)

The system can answer:
- "What internal procedure applies to this test?"
- "Have we seen similar failures before?"
- "Which reports mention this issue?"

With:
- Relevant citations
- Clear separation of knowledge sources

---

## 🧱 Tech Stack (V1)

- Python
- Ollama
- Qwen3:14B
- ChromaDB
- Local embedding model

---
## 🚀 Development Phases

### Phase 1 (Current)
- CLI-based prototype
- Aliro-focused
- Core pipeline working

### Phase 2
- Multi-program support
- Improved ranking
- Better chunking strategies

### Phase 3
- Web UI (demo-ready)
- User interaction layer
- Document filtering

---
## 🔮 Future Phases

- Web UI (React / Next.js or similar)
- API layer (FastAPI)
- Multi-user support
- Document ingestion pipelines
- Integration with internal systems

---

## 🚀 Key Principle

Build the **engine first (CLI)** → then wrap it with UI.

Avoid building UI before validating the intelligence layer.

---

## 🧭 Success Criteria

The system can:
- Answer using internal documents
- Cite correct sources
- Prefer internal knowledge over model assumptions
- Handle multiple programs

---

## Useful commands

- How to start python virtual environment
     
     source .venv/bin/activate

- How to ask 3lm a question:
 
     python -m app.answer "What is a user device?" 


### When restarting a session, give this instruction:

 ## 
    To save time, space and resources, let's do the steps one at a time. I can't follow too many instructions/tasks all at once. So please limit your instructions on what we're doing at hand. Don't give too many instructions in one reply. One instructions first, I do it, and then next. If there are codes to be edited, you can give me multiple instructions, but if it's too many, I want you to edit the code file yourself or give me instructions to do edit it one at a time. Don't ask me to edit the code line by line when it can be done once in bulk. I want you to give suggestions, but not too many that I can't decide which one to do first. Don't assume. If you're not sure about our code base, you should ask me to paste it or attach it (which ever you prefer) before attempting to revise it. Do you understand? 
