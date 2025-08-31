# This Code shows How TOOL BINDING, CALLING AND EXECUTION works
# This is not AI Agent as we are manually handling tool execution

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage , AIMessage ,ToolMessage
from langchain_core.tools import InjectedToolArg
from typing import Annotated
from dotenv import load_dotenv
import requests
import os

load_dotenv()

EXCHANGE_RATE_API= os.getenv("EXCHANGE_RATE_API_KEY")

if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY not found in environment variables.")

print(f"-------------------TOOL_CREATION-------------------------")
@tool
def conversion_factor_fetcher(base_currency:str,target_currency:str)-> float:
    """
    Fetches the currency conversion factor between base currency and target currency.
    """
    url = f'https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API}/pair/{base_currency}/{target_currency}'
    conversion_factor = requests.get(url).json()
    if "conversion_rate" not in conversion_factor:
        raise ValueError(f"API Error: {conversion_factor}")
    return conversion_factor["conversion_rate"]

@tool
def convert(amount:int,conversion_factor:Annotated[float, InjectedToolArg()])->float:
    """
    Converts a base currency amount into target currency using the conversion factor.
    """
    return amount * conversion_factor

factor = conversion_factor_fetcher.invoke({'base_currency': 'INR','target_currency':'USD'})
result = convert.invoke({'amount': 10, 'conversion_factor': factor})
print(f"10 INR = {result} USD")

print(f"-------------------TOOL_BINDING-&-CALLING-------------------------")
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-lite"
)
tools = [conversion_factor_fetcher, convert]
model_with_tools = model.bind_tools(tools=tools)


user_query = HumanMessage(content="Convert 10 USD to INR and What is the conversion factor between USD and INR ?")
messages = [user_query]
print(f"Initial Message: {messages}")

model_response = model_with_tools.invoke(messages)
print(f"\n Model's Response with Tool Calls: {model_response}")
messages.append(model_response)

tool_calls = model_response.tool_calls
print(f"\n Tool Calls = {tool_calls}")

print(f"-------------------TOOL_EXECUTION-------------------------")
tool_messages = []
factor = None # Variable to store the conversion factor for the second tool
for tool_call in tool_calls: 
    tool_name = tool_call["name"]
    tool_args = tool_call["args"]
    if tool_name== 'conversion_factor_fetcher':
        factor = conversion_factor_fetcher.invoke(tool_args)
        tool_output = factor
        tool_messages.append(ToolMessage(tool_call_id=tool_call['id'], content=str(tool_output)))
        print(f"Tool output: {tool_output}")

    elif tool_name == 'convert':
        convert_args = tool_args
        # We need to make sure we have the factor from the first call before this one
        if factor is not None:
             convert_args['conversion_factor'] = factor
        else:
             raise ValueError("Conversion factor not found")             
        tool_output = convert.invoke(convert_args)
        tool_messages.append(ToolMessage(tool_call_id=tool_call['id'], content=str(tool_output)))
        print(f"Tool output: {tool_output}")
        
    else:
        print(f"unknown tool requested: {tool_name}")

messages.extend(tool_messages)
print(f"\nMessages after tool results = {messages}")

print(f"\n------------------- FINAL RESPONSE -------------------------")
final_response = model_with_tools.invoke(messages)
print(f"Final Answer = {final_response.content}")