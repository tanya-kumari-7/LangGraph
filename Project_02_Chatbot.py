'''
Project: “Simple Chat Workflow”

You’ll build a tiny chatbot workflow using LangGraph.
It will:

Take a user’s question as input
Use a model to generate a response
Optionally check if the response is polite before replying
'''

# Imports 

from langgraph.graph import StateGraph , START , END
from langchain_openai import ChatOpenAI
from typing import TypedDict
from dotenv import load_dotenv
import os


