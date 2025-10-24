# 3. Loading the embedding model
from langchain_community.embeddings import HuggingFaceEmbeddings

def create_embedding_model():
    print("🧠 Loading MiniLM embedding model..")
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    print("✅ Embedding model loaded successfully.")
    return embedding_model





