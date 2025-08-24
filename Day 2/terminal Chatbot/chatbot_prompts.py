from langchain_core.prompts import ChatPromptTemplate

# This does not work ar require with the ChatPromptTemplate
#from langchain_core.messages import HumanMessage ,AIMessage ,SystemMessage

# 1 latest way to create a chat template langchain 3
chat_template =ChatPromptTemplate([
    ('system', "You are a helpful and experienced {domain} expert."),
    ('human', "Explain in simple terms, what is {topic}?")
],input_variables=["doamin", "topic"]
)

# 2 same o/p
# chat_template =ChatPromptTemplate.from_messages([
#     ('system', "You are a helpful and experienced {domain} expert."),
#     ('human', "Explain in simple terms, what is {topic}?")
# ])

prompt = chat_template.invoke({
    "domain":"Cricket", "topic":"Batting Techniques"
})

print(prompt)