from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnablePassthrough,RunnableParallel,RunnableLambda
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite")

prompt = PromptTemplate(
    template="write a one liner joke on {topic}",
    input_variables=["topic"]
    )

parser = StrOutputParser()

chain_1 = RunnableSequence(prompt, model , parser ) 

# def count_words(text: str) -> int:
#     return len(text.split())

# chain_2 = RunnableParallel({
#     "joke1": RunnablePassthrough(),
#     "length": RunnableLambda(count_words)
# }) 

chain_2 = RunnableParallel({
    "joke1": RunnablePassthrough(),
    "length": RunnableLambda(lambda x: len(x.split()))
}) 

chain = RunnableSequence(chain_1 , chain_2)

result=chain.invoke({"topic": "cricket"})
print(result)
