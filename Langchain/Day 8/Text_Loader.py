from langchain_community.document_loaders import TextLoader

loader = TextLoader("Day 8\Example files\cricket .txt", encoding="utf-8")
doc = loader.load()

print(type(doc))
print(len(doc))

# print(doc[0]) #full content
print(doc[0].page_content)
print(doc[0].metadata)
