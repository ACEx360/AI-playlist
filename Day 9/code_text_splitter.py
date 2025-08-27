from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text = """from operator import itemgetter

from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough
from langchain.vectorstores import FAISS

vectorstore = FAISS.from_texts(
    ["harrison worked at kensho"], embedding=OpenAIEmbeddings()
)
retriever = vectorstore.as_retriever()

template = \"\"\"Answer the question based only on the following context:
{context}

Question: {question}
\"\"\"  # Correctly escape the triple quotes here
prompt = ChatPromptTemplate.from_template(template)

model = ChatOpenAI()

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)"""

# Initialize the RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,           # Here we can use laguages that are supported
    chunk_size=200,
    chunk_overlap=0
)

# Split the text into chunks
chunks = splitter.split_text(text)

# Output the number of chunks and the chunks themselves
print(len(chunks))
print(chunks[0])
for i in chunks:
    print(f"chunk = \n      {i}\n")
