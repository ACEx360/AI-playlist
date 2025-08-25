from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnableParallel 
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite")

prompt_1 = PromptTemplate(
    template="write pros on topic {topic}",
    input_variables=["topic"]
    )

prompt_2 = PromptTemplate(
    template="write cons on topic {topic}",
    input_variables=["topic"]
    )   

parser = StrOutputParser() 

parallel_chain = RunnableParallel({
    "pros": prompt_1 | model | parser,
    "cons": prompt_2 | model | parser
})

result=parallel_chain.invoke({"topic": "cricket"})
print(result)