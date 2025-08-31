# I will Kill any one who tries to use this code 
# only 4 dollars are left in my account
# This code snippet demonstrates how to use the OpenAI API with LangChain.

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10)

result = model.invoke("Write a 5 line poem on cricket")

print(result.content)