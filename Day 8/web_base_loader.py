from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-lite",
    max_tokens=256
    )

prompt = PromptTemplate(
    template=" Answer the following question\n {question} ? \n  from the following text \n {text}",
    input_variables=["question","text"]
    )

parser = StrOutputParser()

url = 'https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421'

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/114.0.0.0 Safari/537.36"
    )
}

loader = WebBaseLoader(
    url,
    header_template=headers
)

doc = loader.load()

chain = prompt | model | parser

result=chain.invoke({
    "question": "What is the price of macbook air m2 256 gb inr",
    "text": doc[0].page_content
    })

print(result)