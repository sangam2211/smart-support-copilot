from langchain_community.vectorstores import FAISS
#from langchain_openai import OpenAIEmbeddings
from langchain_openai import AzureOpenAIEmbeddings
import os

def create_vector_store(chunks):
    embeddings = AzureOpenAIEmbeddings(
                azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
                api_key=os.getenv("AZURE_OPENAI_API_KEY"),
                api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
                azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_EMBD")
    )


    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    return vectorstore