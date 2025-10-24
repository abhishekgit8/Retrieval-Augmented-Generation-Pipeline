# main.py
from loader import load_all_docs
from splitter import split_text
from embedder import create_embedding_model
from store import store_embeddings
from llm_call import ask_gemini
import os

def main():
    folder_path = input("📂 Enter your documents folder path (e.g., ./my_docs/): ").strip()
    if not os.path.exists(folder_path):
        print("❌ Folder does not exist. Exiting.")
        return

    query = input("🧑‍💻 Ask a question: ").strip()

    # 1️⃣ Load all documents in the folder
    docs = load_all_docs(folder_path)
    if not docs:
        print("❌ No documents loaded. Exiting.")
        return

    # 2️⃣ Split documents into chunks
    chunks = split_text(docs)

    # 3️⃣ Load embedding model
    embedding_model = create_embedding_model()

    # 4️⃣ Store embeddings in Chroma
    vectordb = store_embeddings(chunks, embedding_model)

    # 5️⃣ Retrieve similar context
    print("🔎 Performing similarity search...")
    results = vectordb.similarity_search(query, k=3)  # retrieve top 3 chunks
    context_text = " ".join([doc.page_content for doc in results])
    print("✅ Retrieved context from vector DB.")

    # 6️⃣ Ask Gemini LLM
    answer = ask_gemini(context_text, query)
    print("\n💡 Answer:\n", answer)

if __name__ == "__main__":
    main()
