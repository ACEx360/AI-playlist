# Models are deleted after use

from langchain_huggingface import HuggingFaceEmbeddings
embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
documents = [
    "is Delhi is the capital of china?",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]
vector = embedding.embed_documents(documents)
print(str(vector))