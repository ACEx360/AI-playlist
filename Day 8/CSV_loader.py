from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="Day 8\Example files\Social_Network_Ads.csv")

data = loader.load()

print(len(data))

# First Row[0] data
print(f"\ncontent row 0 = \n{data[0].page_content} \n")
print(f"metadata row 0 = \n{data[0].metadata} \n")

# Second Row[1] data
print(f"full row 1 = \n{data[1]} \n")

data = loader.lazy_load()
for i in data:
    print(f"\ndoc = \n{i}")