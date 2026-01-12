from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_docs(docs, size=1000, overlap=150):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=size,
        chunk_overlap=overlap
    )
    return splitter.split_documents(docs)
