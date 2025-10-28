# llm_call.py — using Google Gemini (Free)
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY not set in environment")

# Configure Gemini client
genai.configure(api_key=api_key)

def ask_gemini(context, query):
    print("🔍 Querying LLM (Gemini 1.5 Flash)...")

    prompt = f"""You are a helpful assistant.
Use the following context to answer the user's question accurately.

Context:
{context}

Question:
{query}

Answer:"""

    # Initialize Gemini model
    model = genai.GenerativeModel("gemini-2.5-flash")


    # Generate response
    response = model.generate_content(prompt)

    # Gemini returns `.text` directly (not .choices like OpenAI)
    answer = response.text.strip() if response.text else "No response from Gemini."

    print("✅ Received response from Gemini.")
    return answer
