from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-lite",
    max_tokens=256
)

print(f"--------------MULTIPLY-TOOL-USE---------------------")

# Tool creation
@tool
def multiply(a: int, b: int) -> int:
    """Given 2 numbers a and b this tool returns their product"""
    return a * b

print(f"Multiply.invoke = {multiply.invoke({'a':3, 'b':4})}")
print(f"Tool name = {multiply.name}")
print(f"Tool Description = {multiply.description}")
print(f"Tool Arguments = {multiply.args}")

print(f"-------------------TOOL_BINDING-------------------------")

# Bind tool with model
model_with_tools = model.bind(tools=[multiply])

# Step 1: Human asks query
query = HumanMessage('can you multiply 3 with 1000')
messages = [query]

# Step 2: Model decides which tool to call
result = model_with_tools.invoke(messages)
messages.append(result)
print(f"Message = {messages}")

# Step 3: Actually run the tool with model’s arguments
tool_result = multiply.invoke(result.tool_calls[0])
tool_message = ToolMessage(
    content=str(tool_result), 
    tool_call_id=result.tool_calls[0]["id"]
)
messages.append(tool_message)
print(f"Tool Message = {tool_message}")

print(f"-------------------TOOL_EXECUTION-------------------------")

# Step 4: Send tool result back to model for final response
final_result = model_with_tools.invoke(messages)
print(f"Final Output = {final_result}")
print(f"\n====Final Answer = {final_result.content}====")
