import os
import streamlit as st

from dotenv import load_dotenv

#from langchain_openai import ChatOpenAI
from langchain_openai import AzureChatOpenAI

from rag.loaders import load_document
from rag.chunker import split_documents
from rag.vectorstore import create_vector_store
from rag.retriever import get_retriever

from classifier.query_classifier import classify_query

from router.response_router import get_prompt

from memory.memory_manager import (
    initialize_memory,
    add_message,
    get_chat_history
)

from utils.formatter import format_sources


load_dotenv()

st.set_page_config(page_title="Smart Support Copilot")

st.title("Smart Support Copilot")

initialize_memory()


# Sidebar
st.sidebar.header("Upload Support Documents")

uploaded_files = st.sidebar.file_uploader(
    "Upload Files",
    type=["pdf", "txt", "md", "csv"],   # Accept all file types
    accept_multiple_files=True
)

# Process Files
if uploaded_files:

    all_docs = []

    for file in uploaded_files:

        temp_path = f"temp_{file.name}"

        with open(temp_path, "wb") as f:
            f.write(file.read())

        # Detect file type
        docs = load_document(temp_path)

        try:

            docs = load_document(temp_path)

            for doc in docs:
                doc.metadata["source"] = file.name

            all_docs.extend(docs)

        except Exception as e:

            st.sidebar.error(
                f"Error processing {file.name}: {str(e)}"
            )

    chunks = split_documents(all_docs)

    vectorstore = create_vector_store(chunks)

    retriever = get_retriever(vectorstore)

    st.sidebar.success("Documents Processed Successfully")

# Display Chat History
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# User Input
query = st.chat_input("Ask your support question...")

if query:

    add_message("user", query)

    with st.chat_message("user"):
        st.markdown(query)


    if uploaded_files:

        # Query Classification
        query_type = classify_query(query)


        # Retrieve Documents
        retrieved_docs = retriever.invoke(query)

        context = "\n".join([
            doc.page_content for doc in retrieved_docs
        ])


        # Get Chat History
        history = get_chat_history()


        # Dynamic Prompt Routing
        prompt_template = get_prompt(query_type)
        final_prompt = prompt_template.format(
            context=context,
            history=history,
            query=query
        )


        # LLM
        llm = AzureChatOpenAI(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT")
        )


        response = llm.invoke(final_prompt)


        # Format Sources
        sources = format_sources(retrieved_docs)


        final_response = f"""
{response.content}


Query Type: {query_type}

Sources:
{', '.join(sources)}

Confidence:
Based on uploaded support documents.
"""


        add_message("assistant", final_response)


        with st.chat_message("assistant"):
            st.markdown(final_response)


    else:

        st.warning("Please upload at least one document.")
