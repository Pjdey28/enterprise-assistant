import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv(Path(__file__).resolve().parents[1] / ".env")

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from load_pdf import load_pdf
from chunker import chunk_docs
from embed_store import build_faiss
from app.config import (
    PDF_PATH, FAISS_PATH, CHUNK_SIZE, CHUNK_OVERLAP
)

def main():
    # Resolve paths relative to project root
    project_root = Path(__file__).resolve().parents[1]
    pdf_path = project_root / PDF_PATH
    faiss_path = project_root / FAISS_PATH
    
    docs = load_pdf(str(pdf_path))
    chunks = chunk_docs(docs, CHUNK_SIZE, CHUNK_OVERLAP)
    build_faiss(chunks, str(faiss_path))
    print("FAISS index built successfully.")

if __name__ == "__main__":
    main()
