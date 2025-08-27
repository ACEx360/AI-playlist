# This is annoying i can get this splitter to work properly
# reasons can be input is too small ,embedding model
# Potential solution could be using **RecursiveCharacterTextSplitter** and then applying the Semantic Chunker

from langchain_experimental.text_splitter import SemanticChunker
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

text_splitter = SemanticChunker(
    embeddings,
    breakpoint_threshold_type="percentile",
    breakpoint_threshold_amount=50
)

sample = """
Farmers were working hard in the fields, preparing the soil and planting seeds for the next season. 
The sun was bright, and the air smelled of earth and fresh grass. 
The Indian Premier League (IPL) is the biggest cricket league in the world. 
People all over the world watch the matches and cheer for their favourite teams.

Terrorism is a big danger to peace and safety. 
It causes harm to people and creates fear in cities and villages. 
When such attacks happen, they leave behind pain and sadness. 
To fight terrorism, we need strong laws, alert security forces, and support from people who care about peace and safety.
"""

docs = text_splitter.create_documents([sample])

print(f"Number of chunks: {len(docs)}\n")
for i, doc in enumerate(docs, 1):
    print(f"--- Chunk {i} ---\n{doc.page_content}\n")