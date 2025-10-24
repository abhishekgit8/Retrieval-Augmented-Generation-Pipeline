# 5. Call LLM with context and prompt to get answer
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise RuntimeError("OPENAI_API_KEY not set in environment")

def ask_gemini(context, query):
    print("🔍 Querying LLM (OpenAI) ...")
    prompt = f"""You are a helpful assistant.
Use the following context to answer the user's question accurately.

Context:
{context}

Question:
{query}

Answer:"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
        max_tokens=512,
    )

    answer = response.choices[0].message.get("content", "").strip()
    print("✅ Received response from LLM.")
    return answer


