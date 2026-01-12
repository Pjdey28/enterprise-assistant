from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

def retrieve(query, path, k=4):
    embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)

    db = FAISS.load_local(
        path,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return db.similarity_search(query, k=k)
