def format_sources(documents):

    sources = set()

    for doc in documents:
        if "source" in doc.metadata:
            sources.add(doc.metadata["source"])

    return list(sources)
