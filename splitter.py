# 2. Split data into chunks
# from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter


def split_text(docs, chunk_size=500, chunk_overlap=50):
    print("✂️ Splitting text into chunks...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = splitter.split_documents(docs)
    print(f"✅ Split into {len(chunks)} chunks.")
    return chunks


