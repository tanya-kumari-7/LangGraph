
"""
Description of the project :
Medical AI assistant

1. GET data from user : 
     a. Name of the user
     b. Age of the user
     c. Location of the user
     d. Mobile_no of the user
     e. Medical Issue description
     
2. Check and nearest Doctor
"""
# ---------------------------
# Imports
# ---------------------------

from langgraph.graph import StateGraph , START , END
from langchain_openai import ChatOpenAI
from typing import  TypedDict
from dotenv import load_dotenv
import os

# ----------------------------------
# Load API
# ----------------------------------

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("base_url")

# --------------------------------------
#  Define state
# ------------------------------------

class ChatState(TypedDict):
    name : str
    age : int
    location : str
    mobile : int
    issue : str
    response : str
# --------------------------------------
#  Createing LLM Model 
# -------------------------------------

llm_model = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=api_key,
    base_url=base_url
)

# -------------------------------------
# Define Nodes 
# -------------------------------------

def get_data_from_user(state:ChatState):

    print('''
                Hi there !!!
                    I'm your medical AI Assistant.
                    To help you further I need few information from you
          ''')