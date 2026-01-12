import os
from dotenv import load_dotenv
from pathlib import Path
import sys

# Load environment variables
load_dotenv()

# Validate API key
if not os.getenv("GROQ_API_KEY"):
    print("ERROR: GROQ_API_KEY not found in environment.")
    sys.exit(1)

# Validate FAISS index
FAISS_PATH = Path("embeddings/faiss_index")
if not FAISS_PATH.exists():
    print("ERROR: FAISS index not found.")
    print("Run: python app/ingestion/build_index.py")
    sys.exit(1)

# Entry point (Streamlit or CLI)
def main():
    print("Agentic Enterprise Assistant initialized.")
    print("Run UI using:")
    print("streamlit run app/ui/streamlit_app.py")

if __name__ == "__main__":
    main()
