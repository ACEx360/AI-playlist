from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnablePassthrough,RunnableLambda,RunnableBranch
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-lite",
    max_tokens=256
    )

# 250 word / 50 words were added for testing the branch condition
prompt_1 = PromptTemplate(
    template="write 250 word detailed report on {topic}",
    input_variables=["topic"]
    )

prompt_2 = PromptTemplate(
    template="write 50 word a summary on {text}",
    input_variables=["text"]
    )

parser = StrOutputParser()

Report_gen_chain = RunnableSequence(prompt_1 , model , parser) 

condition_chain = RunnableBranch(
    (lambda x: len(x.split())>100, RunnableSequence(prompt_2 , model , parser)),
    RunnablePassthrough()
) 

chain = RunnableSequence(Report_gen_chain , condition_chain)

result=chain.invoke({"topic": "cricket"})
print(result)