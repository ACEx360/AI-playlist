from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='Day 8\Example files\Example Directory',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)


# if more documents i.e more no of pages
docs = loader.lazy_load()

# else if we have limites no of documents  (used for all the other loaders)
# docs = loader.load()

for document in docs:
    print(document.metadata)
  
    
# Glob Pattern | What It Loads
# "**/*.txt" → All .txt files in all subfolders
# "*.pdf" → All .pdf files in the root directory
# "data/*.csv" → All .csv files in the data/ folder
# "**/*" → All files (any type, all folders)