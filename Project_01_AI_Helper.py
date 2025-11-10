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
print(llm_model_chatGPT.invoke("Hello LangGraph!").content)

# Create a graph which will track all what's happing 

class GraphState(TypedDict):
    questions: str
    answer: str
graph = StateGraph(GraphState)

# Creating a node : which will decide what to do which input received from users

def decide_node(state):
    q=state["question"]
    if any(ch.isdigit() for ch in q) or any(op in q for op in ["+","-","*","/"]):
        return "math"
    else:
        return "gpt"