import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain.schema import Document

load_dotenv()

# trying to learn about try and catch block 
try:
    os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
except Exception as e:
    raise ValueError(
        f"GOOGLE_API_KEY not found in environment variables. Please add it to your .env file."
    ) from e

doc1 = Document(
    page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.",
    metadata={"team": "Royal Challengers Bangalore"}
)
doc2 = Document(
    page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.",
    metadata={"team": "Mumbai Indians"}
)
doc3 = Document(
    page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
    metadata={"team": "Chennai Super Kings"}
)
doc4 = Document(
    page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.",
    metadata={"team": "Mumbai Indians"}
)
doc5 = Document(
    page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.",
    metadata={"team": "Chennai Super Kings"}
)

docs = [doc1, doc2, doc3, doc4, doc5]

print("Initializing Google Generative AI embedding model...")
gemini_embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

print("Initializing ChromaDB vector store...")
vector_store = Chroma(
    embedding_function=gemini_embeddings,
    persist_directory='my_chroma_db_gemini',
    collection_name='ipl_players'
)

print("Adding documents to the vector store...")
vector_store.add_documents(docs)

query = "Who among these are a bowler?"
print(f"\nSearching for documents most similar to: '{query}'")

results = vector_store.similarity_search(query, k=2)

print("\n--- Search Results ---")
for i, doc in enumerate(results, 1):
    print(f"Result {i}:")
    print(f"  Page Content: {doc.page_content}")
    print(f"  Metadata: {doc.metadata}")
