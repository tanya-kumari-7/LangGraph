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
    question : str
    response : str

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

def check_politeness_node(state:chatstate):
    response = state["response"]
    if "please" in response.lower() or "thank" in response.lower():
        print("Response is polite")
    else:
        print("Response is not polite")

def end_conversion_node(state:chatstate):
    print(f"Final response is :{state['response']}")
    return state

# Building Graph 

graph = StateGraph(chatstate)
graph.add_node("ask",ask_question_node)
graph.add_node('check',check_politeness_node)
graph.add_node('end',end_conversion_node)


# define Edge :

graph.add_edge(START,'ask')
graph.add_edge('ask','check')
graph.add_edge('check','end')
graph.add_edge('end',END)

# compliations

app =graph.compile()

# run graph:

if __name__ == "__main__":
    while True:
        user_question = input("Enter your question: ASK ME ANYTHING ------")
        initial_question = {"question":user_question,"response":""}
        final_state = app.invoke(initial_question)

        another = input("\nWould you like to ask me anything else : (Yes/No)").strip().lower()
        if another not in ["yes"]:
            print("Thanks for connecting : SEE YOU SOON !!!!!")
            break

        