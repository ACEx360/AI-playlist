from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-lite')

history = [
    SystemMessage(content="You are a helpful chatbot that can answer questions and assist with various tasks."),
]

while True:
    user_input = input("You: ")
    history.append(HumanMessage(user_input))
    if user_input.lower() == "byy":
        print("Exiting the chatbot. Goodbye!")
        break
    result = model.invoke(history)
    history.append(AIMessage(result.content))
    print(f"Bot: {result.content}")

print(history)
     