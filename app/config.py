from pathlib import Path

ANSWER_LANGUAGE = "auto"

# Project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data folders
DATA_DIR = PROJECT_ROOT / "data"
STORAGE_DIR = PROJECT_ROOT / "storage"
INDEX_DIR = PROJECT_ROOT / "index"
PROMPTS_DIR = PROJECT_ROOT / "prompts"

# Storage files
PAGES_PATH = STORAGE_DIR / "pages.jsonl"
CHUNKS_PATH = STORAGE_DIR / "chunks.jsonl"

# Vector DB
CHROMA_PATH = INDEX_DIR / "chroma"
COLLECTION_NAME = "docs"

# Models
RAG_LLM_MODEL = "gemma4:26b-mlx"
GENERAL_LLM_MODEL = "gemma4:26b-mlx"
EMBED_MODEL = "BAAI/bge-m3"

# Chunking
MAX_CHARS = 4000
OVERLAP_CHARS = 400
FIRST_N_PAGES = 5

# Retrieval
DEFAULT_TOP_K = 5
INITIAL_RETRIEVAL_K = 10

# Supported file types for v1
SUPPORTED_EXTENSIONS = {".pdf", ".md", ".txt", ".json" }

# Prompt files
ANSWER_PROMPT_PATH = PROMPTS_DIR / "answer_prompt.txt"


def ensure_directories() -> None:
    """Create required project directories if they do not exist."""
    for path in [STORAGE_DIR, INDEX_DIR, CHROMA_PATH, PROMPTS_DIR]:
        path.mkdir(parents=True, exist_ok=True)