
from typing import Union, TypedDict
from langchain_core.messages import AIMessage, HumanMessage
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START

class agentState(TypedDict):
    messages: list[Union[HumanMessage, AIMessage]]

llm = ChatOllama(model="llama3.2:latest", base_url="http://localhost:11434", api_key="1234567890")

def process(state: agentState) -> agentState:
    response = llm.invoke(state["messages"])
    print(response.content)
    return state

graph = StateGraph(agentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.set_finish_point("process")

agent = graph.compile()

convo_history = []

user_input = input("Enter your next command: ")
while user_input.lower() != "exit":
    convo_history.append(HumanMessage(content=user_input))
    result = agent.invoke({"messages": convo_history})
    # print(result)
    user_input = input("Enter your next command: ")


