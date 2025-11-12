
"""
Description of the project :
Medical AI assistant

1. GET data from user : 
     a. Name of the user
     b. Age of the user
     c. Location of the user
     d. Mobile_no of the user
     e. Medical Issue description
"""

# Imports

from langgraph.graph import StateGraph , START , END
from langchain_openai import ChatOpenAI
from typing import  TypedDict
from dotenv import load_dotenv
import os

