from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    CSVLoader
)


def load_pdf(file_path):

    loader = PyPDFLoader(file_path)

    documents = loader.load()

    return documents


def load_text_file(file_path):

    loader = TextLoader(file_path)

    documents = loader.load()

    return documents


def load_document(file_path):

    if file_path.endswith(".pdf"):

        loader = PyPDFLoader(file_path)

    elif file_path.endswith(".txt"):

        loader = TextLoader(file_path)

    elif file_path.endswith(".md"):

        loader = TextLoader(file_path)

    elif file_path.endswith(".csv"):

        loader = CSVLoader(file_path)

    else:

        raise ValueError(
            f"Unsupported file type: {file_path}"
        )

    documents = loader.load()

    return documents
