import os
import sys
from pathlib import Path
from groq import Groq
# Add parent directory to path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from agents.evidence import extract_evidence
from agents.validator import validate_evidence


# Load environment variables if dotenv is available
try:
    from dotenv import load_dotenv
    load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
except ImportError:
    pass
client = Groq(api_key=os.getenv("GROQ_API_KEY"))



SYSTEM_PROMPT = """
You are an enterprise AI assistant.
Answer ONLY using the provided context.
If insufficient information exists, say:
"Insufficient information in the provided document."

End with:
Sources: Page X, Page Y
"""

def generate_answer(query, docs):
    pages, context = extract_evidence(docs)

    if not validate_evidence(pages):
        return "Insufficient information in the provided document."

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion:\n{query}"}
        ], 
        temperature=0.2
    )

    citation = ", ".join(f"Page {p}" for p in sorted(pages))
    return f"{response.choices[0].message.content.strip()}\n\nSources: {citation}"