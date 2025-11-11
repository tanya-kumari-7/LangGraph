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
api_key = os.getenv("OPENAI_API_KEY")

# define memory of your workflow [STATE]

class chatstate(TypedDict):
    question = str
    response = str

# Craeteing model 



