# For Visulaizing Results , Code them in Jupyter notebook or Colab
from pinecone import Pinecone
from langchain import schema
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings

import os
from dotenv import load_dotenv

load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENVIRONMENT")

pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "test_index"

if index_name not in [i.name for i in pc.list_indexes()]:
    pc.create_index(
        name=index_name,
        dimension=1536,
        metric="cosine"
    )

# Embeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

# Vector store
vectorstore = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

# Add texts
docs = ["Pinecone is a vector DB.", "LangChain makes AI easier."]
vectorstore.add_texts(docs)

# Query
results = vectorstore.similarity_search("What is Pinecone?", k=2)
for r in results:
    print(r.page_content)