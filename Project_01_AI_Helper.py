# Import
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv  # api file
from typing import TypedDict # to read state dict
import os

# Call APi Saved in .env file 
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Create Model 
llm_model_chatGPT = ChatOpenAI(model="gpt-4o-mini", api_key=api_key, base_url="https://openrouter.ai/api/v1" )
# print(llm_model_chatGPT.invoke("Hello LangGraph!").content)

# Create a graph which will track all what's happing 

class GraphState(TypedDict):
    question: str
    answer: str
graph = StateGraph(GraphState)

# Creating a node : which will decide what to do which input received from users
def decide_node(state):
    return{}

def decide_node_logic(state):
    q=state["question"]
    if any(ch.isdigit() for ch in q) or any(op in q for op in ["+","-","*","/"]):
        return "math"
    else:
        return "gpt"
    
def math_node(state):
    q=state["question"]
    try:
        result = str(eval(q))
    except Exception:
        result = "Sorry, I couldn't calculate"
    return {"answer":result}

def gpt_node(state):
    q=state["question"]
    response = llm_model_chatGPT.invoke(q)
    return {"answer":response.content}

# Add Nodes

graph.add_node("decide",decide_node)
graph.add_node("math",math_node)
graph.add_node("gpt",gpt_node)

# Add Edge
graph.add_edge(START,"decide")
graph.add_conditional_edges(
    "decide",
    decide_node_logic,
    {"math":"math","gpt":"gpt"}
)
graph.add_edge("math",END)
graph.add_edge("gpt",END)

# compile
app = graph.compile()

print(app.invoke({"question": "2+3"}))
print(app.invoke({"question": "Who are you?"}))