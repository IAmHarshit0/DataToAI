from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START

class Agent:
    messages: list[HumanMessage]

llm = ChatOllama(model="llama3.2:latest", base_url="http://localhost:11434", api_key="1234567890")

def process(state: Agent) -> Agent:
    response = llm.invoke(state["messages"])
    print(response.content)
    return state

graph = StateGraph(Agent)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.set_finish_point("process")

agent = graph.compile()

user_input = input("Enter your next command: ")
while user_input.lower() != "exit":
    agent.invoke({"messages": [HumanMessage(content=user_input)]})
    user_input = input("Enter your next command: ")
