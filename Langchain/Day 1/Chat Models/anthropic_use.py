# The anthropic keys are Expensive, so we are not using them
# This code snippet demonstrates how to use the Anthropic API with LangChain.


from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='claude-3-5-sonnet-20241022')

result = model.invoke('What is the capital of India')

print(result.content)