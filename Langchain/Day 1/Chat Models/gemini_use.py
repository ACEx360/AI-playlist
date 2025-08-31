# Use in Moderation
# Billing is on for this Api Key
# Do not use this key for production or large scale applications

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

#model = ChatGoogleGenerativeAI(model='gemini-2.5-pro')
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-lite')

result = model.invoke('What is the capital of India')

print(result.content) 