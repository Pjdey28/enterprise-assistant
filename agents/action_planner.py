import os
import json
from groq import Groq
from dotenv import load_dotenv
from tools.actions import ACTION_SCHEMAS
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

SYSTEM_PROMPT = """
You are an enterprise action-planning agent.

Instructions:
1. Decide if the user request requires an ACTION.
2. If yes, select the MOST appropriate action.
3. Fill all required parameters.
4. Output ONLY valid JSON.
5. If no action is needed, output exactly:
{"action": "none"}
"""

def plan_action(user_query: str):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"""
Available Actions:
{json.dumps(ACTION_SCHEMAS, indent=2)}

User Query:
{user_query}
"""
            }
        ],
        temperature=0
    )

    text = response.choices[0].message.content.strip()

    try:
        return json.loads(text)
    except Exception:
        return {"action": "none"}
