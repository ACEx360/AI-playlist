import requests
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

# ---------------- ENV -----------------
load_dotenv()
WEATHER_API = os.getenv("WEATHER_API_KEY")
if not WEATHER_API:
    raise ValueError("WEATHER_API_KEY not found in environment variables.")

# ---------------- TOOL DEFINITIONS -----------------
@tool
def get_weather_data(city: str) -> str:
    """
    Fetches the current weather data for a given city using Weatherstack API.
    """
    url = f'https://api.weatherstack.com/current?access_key={WEATHER_API}&query={city}'
    response = requests.get(url).json()
    if "current" not in response:
        return f"Could not fetch weather data. Response: {response}"
    return f"The weather in {city} is {response['current']['temperature']}°C, {response['current']['weather_descriptions'][0]}."

# Search tool
search_tool = DuckDuckGoSearchRun()

# ---------------- MODEL -----------------
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-lite",
    max_tokens=256
)

# Pull ReAct prompt
prompt = hub.pull("hwchase17/react")

# ---------------- AGENT -----------------
tools = [get_weather_data, search_tool]

agent = create_react_agent(
    llm=model,
    tools=tools,
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

# ---------------- QUERY -----------------
response = agent_executor.invoke({
    "input": "Find the capital of Maharastra, then find its current weather condition."
})

print("\n------------------- FINAL RESPONSE -------------------")
print(response["output"])
