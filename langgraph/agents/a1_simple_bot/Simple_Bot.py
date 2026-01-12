from typing import TypedDict, List
from langchain_core.messages import HumanMessage
from langchain_ollama import OllamaLLM
from langgraph.graph import StateGraph, START, END

class AgentState(TypedDict):
    messages: List[HumanMessage]

model_name = "gemma3:1b"
llm = OllamaLLM(model=model_name)

def process(state: AgentState) -> AgentState:
    response = llm.invoke(state["messages"])
    print(f"\nAI: {response}")
    return state

graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)
agent = graph.compile()

user_input = input("Enter: ")
while user_input != "exit":
    agent.invoke({"messages": [HumanMessage(content=user_input)]})
    user_input = input("Enter: ")