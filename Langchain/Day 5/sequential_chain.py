# topic --> report --> 5 point summary

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite")

prompt_1 =PromptTemplate(
    template="Generate detailed report on {topic}",
    input_variables=["topic"]
    )

prompt_2 =PromptTemplate(
    template="Generate a 5 point summary of the following report {report}",
    input_variables=["report"]
    )

parser = StrOutputParser()

chain = prompt_1 | model | parser | prompt_2 | model | parser  #LCEL

result=chain.invoke({"topic": "Unemployment in India"})

print(result)

chain.get_graph().print_ascii()