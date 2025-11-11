'''
Project: “Simple Chat Workflow”

You’ll build a tiny chatbot workflow using LangGraph.
It will:

Take a user’s question as input
Use a model to generate a response
Optionally check if the response is polite before replying
'''

# Imports 

from langgraph.graph import StateGraph , START , END  #[for langgraph edge and state]
from langchain_openai import ChatOpenAI #[for AI model]
from typing import TypedDict #[to pass dict in format inside STATE]
from dotenv import load_dotenv #[call api key from .env file]
import os #[get key]

# load API Key
load_dotenv()
api_key_ = os.getenv("OPENAI_API_KEY")
model_url = os.getenv("base_url")

# define memory of your workflow [STATE]

class chatstate(TypedDict):
    question = str
    response = str

# Craeteing model 
llm_model = ChatOpenAI(
    model= "gpt-3.5-turbo",
    api_key=api_key_,
    base_url= model_url
)

def ask_question_node(state:chatstate):
    question = state["question"]
    response = llm_model.invoke(question)
    state['response'] = response.content
    return state



