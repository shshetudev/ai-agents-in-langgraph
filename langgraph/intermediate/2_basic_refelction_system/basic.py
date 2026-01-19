from dotenv import load_dotenv

load_dotenv()

from typing import List, TypedDict
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages
from chains import generation_chain, reflection_chain


REFLECT = "reflect"
GENERATE = "generate"

class State(TypedDict):
    messages: List[BaseMessage] = []

def generate_node(state: State) -> State:
    response = generation_chain.invoke({"messages": state["messages"]})
    return {"messages": add_messages(state["messages"], response)}

def reflect_node(state: State) -> State:
    response = reflection_chain.invoke({"messages": state["messages"]})
    return {"messages": add_messages(state["messages"], HumanMessage(content=response.content))}

def should_continue(state: State):
    if len(state["messages"]) > 6:
        return END
    return REFLECT

graph = StateGraph(State)
graph.add_node(GENERATE, generate_node)
graph.add_node(REFLECT, reflect_node)
graph.set_entry_point(GENERATE)

graph.add_conditional_edges(GENERATE, should_continue)
graph.add_edge(REFLECT, GENERATE)

app = graph.compile()
print(app.get_graph().draw_mermaid())
app.get_graph().print_ascii()

result = app.invoke({"messages": [HumanMessage(content="AI Agents taking over content creation")]})
print(result)
