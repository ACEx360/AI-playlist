# ---------------- PDF Loaders in LangChain ----------------
#link  = https://python.langchain.com/docs/concepts/document_loaders/
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("Langchain\Day 8\Example files\dl-curriculum.pdf")

doc = loader.load()

print(type(doc))
print(len(doc))

# print(doc[0]) #full content
print(doc[0].page_content)
print(doc[0].metadata)