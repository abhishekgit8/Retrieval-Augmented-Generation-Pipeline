# 1. Load raw data
# from langchain_community.document_loaders import TextLoader

# def load_data(file_path):
#     print(f"📄 Loading file: {file_path}")
#     loader = TextLoader(file_path)
#     docs = loader.load()
#     print(f"✅ Loaded {len(docs)} document(s).")
#     return docs

from langchain_community.document_loaders import TextLoader, PyPDFLoader
import os

def load_all_docs(folder_path):
    print(f"📂 Loading all documents from folder: {folder_path}")

    def loader_for_path(file_path):
        ext = os.path.splitext(file_path)[1].lower()
        if ext == ".txt":
            return TextLoader(file_path, encoding="utf-8")
        if ext == ".pdf":
            return PyPDFLoader(file_path)
        return None

    docs = []
    for root, _, files in os.walk(folder_path):
        for fname in files:
            path = os.path.join(root, fname)
            loader = loader_for_path(path)
            if loader:
                try:
                    loaded = loader.load()
                    docs.extend(loaded)
                except Exception as e:
                    print(f"⚠️ Failed to load {path}: {e}")
    print(f"✅ Loaded {len(docs)} document(s) from folder.")
    return docs


