from typing import Annotated, Sequence, TypedDict
from langchain_core.messages import BaseMessage, ToolMessage, SystemMessage
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode

class AgentConfig(TypedDict):
    messages : Annotated[Sequence[BaseMessage], add_messages]

@tool
def add(a: int, b: int) -> int:
    """This function adds two integers together."""
    return a + b

@tool
def multiply(a: int, b: int) -> int:
    """This function multiplies two integers."""
    return a * b

tools = [add, multiply]

llm = ChatOllama(model="deepseek-coder:6.7b", base_url="http://localhost:11434", api_key="Nothing").bind_tools(tools)

def model_call(state: AgentConfig) -> AgentConfig:
    system_prompt = SystemMessage(content="You are a helpful assistant that can perform basic arithmetic operations. You have access to the following tools: add and multiply. Use these tools to answer the user's questions.")
    response = llm.invoke([system_prompt] + state["messages"])
    return {"messages": [response]}

def should_continue(state: AgentConfig):
    messages = state["messages"]
    last_message = messages[-1]
    if not last_message.tool_calls:
        return "end"
    else:
        return "continue"
    
graph = StateGraph(AgentConfig)

tools_node = ToolNode(tools)

graph.add_node("model_call", model_call)
graph.add_node("tools", tools_node)

graph.set_entry_point("model_call")
graph.add_conditional_edges("model_call", should_continue, {
    "continue": "tools",
    "end": END
})

graph.add_edge("tools", "model_call")

app = graph.compile()

def print_stream(stream):
    for s in stream:
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()
        
input_messages = {"messages": [("user", "add 10 and 12 and multiply 5 by the result")]}
print_stream(app.stream(input_messages, stream_mode="values"))