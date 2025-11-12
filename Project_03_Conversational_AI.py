
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
    
    name = str(input("Please enter your name:"))
    age = int(input("Please enter your name:"))
    location = str(input("Please enter your name:"))
    mobile = int(input("Please enter your name:"))
    issue = str(input("Please enter your name:"))

    return {
        "name":name,
        "age":age,
        "location":location,
        "mobile":mobile,
        "issue":issue
    }

def find_doctor(state:ChatState):
    prompt = f"""
        A patient named {state['name']}, age {state["age"]} from {state["location"]}
        has the following medical issue : {state["issue"]}.
        Please suggest the nearest doctor or medical department or hospital location
        """
    response = llm_model.invoke(prompt).content
    state['response'] = response
    return state

# ---------------------------------------
# Build the Graph
# ---------------------------------------

graph = StateGraph(ChatState)
graph.add_node('Get_user_data',get_data_from_user)
graph.add_node("get_doctor_info",find_doctor)

# -------------------------------------------
#  Add Edge
# -------------------------------------------

graph.add_edge(START,'Get_user_data')
graph.add_edge('Get_user_data','find_doctor')
graph.add_edge('find_doctor',END)

# ------------------------------------------------
#  Complie graph 
# ------------------------------------------------