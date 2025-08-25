from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite")

prompt_1 = PromptTemplate(
    template="write a one liner joke on {topic}",
    input_variables=["topic"]
    )

prompt_2 = PromptTemplate(
    template="write joke properly and explain the following joke {joke}",
    input_variables=["joke"]
    )

parser = StrOutputParser()

chain_1 = RunnableSequence(prompt_1 , model , parser)

parallel_chain = RunnableParallel({
    "Joke": RunnablePassthrough(),
    "Explanation": prompt_2 | model | parser
})

chain = RunnableSequence(chain_1 , parallel_chain)
result=chain.invoke({"topic": "cricket"})
print(result)