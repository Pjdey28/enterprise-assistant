import os
from urllib import response
from dotenv import load_dotenv

from groq import Groq
# Load environment variables from parent directory
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


SYSTEM_PROMPT = """
Classify the user query into exactly one category:
- factual
- analytical
- action

Return only the category word.
"""

def classify_query(query:str) -> str:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": f"{SYSTEM_PROMPT}\n\nQuery:\n{query}"}],
        temperature=0
    )
    return response.choices[0].message.content.strip().lower()