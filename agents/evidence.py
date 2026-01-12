def extract_evidence(docs):
    pages = set()
    context = []

    for d in docs:
        page = d.metadata.get("page")
        pages.add(page)
        context.append(f"(Page {page}) {d.page_content[:400]}")

    return pages, "\n\n".join(context)
