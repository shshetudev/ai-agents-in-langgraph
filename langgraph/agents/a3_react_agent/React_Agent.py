from dotenv import load_dotenv
from typing import TypedDict, Annotated, Sequence

from langchain_core.messages import BaseMessage, SystemMessage, \
    HumanMessage  # foundational class for all message types in LangGraph
from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

load_dotenv()

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]


@tool
def add(num1: int, num2: int):
    """Add two numbers together."""
    return num1 + num2


@tool
def subtract(num1: int, num2: int):
    """Subtract the second number from the first."""
    return num1 - num2


@tool
def multiply(num1: int, num2: int):
    """Multiply two numbers together."""
    return num1 * num2


tools = [add, subtract, multiply]

# model_name = "llama2"
# model = ChatOllama(model=model_name, temperature=0).bind_tools(tools)

model = ChatOpenAI(model = "gpt-4o").bind_tools(tools)

def model_call(state: AgentState) -> AgentState:
    prompt = "You are my AI assistant, please answer my query to the best of your ability."
    system_prompt = SystemMessage(content=prompt)
    response = model.invoke([system_prompt] + state["messages"])
    return {"messages": [response]}


def should_continue(state: AgentState) -> str:
    messages = state["messages"]
    last_message = messages[-1]
    if not last_message.tool_calls:
        return "end"
    return "continue"


graph = StateGraph(AgentState)
graph.add_node("our_agent", model_call)

tool_node = ToolNode(tools=tools)
graph.add_node("tools", tool_node)

graph.set_entry_point("our_agent")
graph.add_conditional_edges(
    "our_agent",
    should_continue,
    {
        "continue": "tools",
        "end": END
    }
)

graph.add_edge("tools", "our_agent")
app = graph.compile()


def print_stream(stream):
    for chunk in stream:
        message = chunk["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()


# inputs = {
#     "messages": [
#         {
#             "role": "user",
#             "content": "Add 40 + 12 and then multiply the result by 6. Also tell me a joke please."
#         }
#     ]
# }

# inputs = {
#     "messages": [
#         HumanMessage(content="Add 40 + 12 and then multiply the result by 6. Also tell me a joke please.")
#     ]
# }


inputs = {"messages": [("user", "Add 40 + 12 and then multiply the result by 6. Also tell me a joke please.")]}

# todo-SH: Know the meaning of below line
print_stream(app.stream(inputs, stream_mode="values"))
