from pypdf import PdfReader
from langchain_core.documents import Document

def load_pdf(path):
    reader = PdfReader(path)
    documents = []

    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if text and text.strip():
            documents.append(
                Document(
                    page_content=text,
                    metadata={"page": page_num}
                )
            )

    return documents
