from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import os

# chat template
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []

# load chat history using script folder
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "chat_history.txt")

with open(file_path) as f:
    chat_history.extend(f.readlines())

print(chat_history)

# create prompt
prompt = chat_template.invoke({
    'chat_history':chat_history, 
    'query':'Where is my refund?'
    })
print(prompt)
