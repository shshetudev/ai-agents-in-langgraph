import datetime

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_tavily import TavilySearch

load_dotenv()

model_name = 'gemini-2.5-flash-lite'
llm = ChatGoogleGenerativeAI(model=model_name)

search_tool = TavilySearch(max_results=2)

@tool
def get_system_time(format: str = '%Y-%m-%d %H:%M:%S'):
    """Returns the current date and time in the specified format.
    Use this to calculate time differences."""
    return datetime.datetime.now().strftime(format)

tools = [search_tool, get_system_time]

agent = create_agent(model=llm, tools=tools)

inputs = {"messages": [("user", "When was SpaceX's last launch and how many days ago was that from this instant?")]}
response = agent.invoke(inputs)

print(response["messages"][-1].content)