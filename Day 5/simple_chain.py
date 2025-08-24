# topic --> 5 facts

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate(
    template="Generate 5 intresting fact about {topic}?",
    input_variables=["topic"],
)

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite")

parser = StrOutputParser()

chain = prompt | model | parser  #LCEL

result = chain.invoke({"topic": "Python programming language"})

print(result)

# Visulalize the chain (simple way)
chain.get_graph().print_ascii()
