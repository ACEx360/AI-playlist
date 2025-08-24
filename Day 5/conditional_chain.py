# Customer feedback system

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv

# important to this lecture
from langchain.schema.runnable import RunnableBranch
from langchain.schema.runnable import RunnableLambda

load_dotenv()

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="Sentiment of the feedback")
    
pydantic_parser = PydanticOutputParser(pydantic_object=Feedback)
parser = StrOutputParser()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite")

prompt_1_classify = PromptTemplate(
    template="Classify the sentiment of the following feedback into positive or negative.\n\nFeedback: {feedback}\n\n{format_instructions}",
    input_variables=["feedback"],
    partial_variables={'format_instructions': pydantic_parser.get_format_instructions()} 
)

# New Persona-driven prompt for negative feedback
prompt_2_negative = PromptTemplate(
    template="""You are an empathetic and professional customer support agent. A customer has sent the following negative feedback. Write a polite email acknowledging their problem and offering to help.

Customer Feedback: {feedback}

Your Email:""",
    input_variables=['feedback']
)

# New Persona-driven prompt for positive feedback
prompt_3_positive = PromptTemplate(
    template="""You are a friendly customer support agent. A customer has left the following positive feedback. Write a short, enthusiastic response to thank them.

Customer Feedback: {feedback}

Your Response:""",
    input_variables=['feedback']
)


classifier_chain = prompt_1_classify | model | pydantic_parser

# tuples -> (condition, chain)
branch_chain = RunnableBranch(
    (lambda x: x["classification"].sentiment == 'positive', prompt_3_positive | model | parser),  # if response is positive
    (lambda x: x["classification"].sentiment == 'negative', prompt_2_negative | model | parser),  # if response is negative
    RunnableLambda(lambda x: "Could not find the sentiment")
)
chain = {
    "classification": classifier_chain,
    "feedback": lambda x: x['feedback']
} | branch_chain

result = chain.invoke({'feedback': 'This is a beautiful phone'})

print(result)

chain.get_graph().print_ascii()