# 4. Compute and Store embeddings into Vector DB
from langchain_community.vectorstores import Chroma

# def store_embeddings(chunks, embedding_model, persist_directory="vector_db"):
#     print("💾 Creating and storing embeddings in Chroma...")
#     vectordb = Chroma.from_documents(
#         documents=chunks,
#         embedding=embedding_model,
#         persist_directory=persist_directory
#     )
#     vectordb.persist()
#     print("✅ Vector database persisted locally.")
#     return vectordb

import os

def store_embeddings(chunks, embedding_model, persist_directory="vector_db"):
    print("💾 Creating and storing embeddings in Chroma...")
    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persist_directory
    )
    vectordb.persist()
    print("✅ Vector database persisted locally.")
    return vectordb

def load_existing_vectordb(embedding_model, persist_directory="vector_db"):
    if not os.path.exists(persist_directory):
        print(f"⚠️ No vector DB found at {persist_directory}")
        return None
    print("📂 Loading existing Chroma vector DB...")
    vectordb = Chroma(
        persist_directory=persist_directory,
        embedding_function=embedding_model
    )
    print("✅ Vector DB loaded successfully.")
    return vectordb



