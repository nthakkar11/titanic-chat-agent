import os
import pandas as pd
from dotenv import load_dotenv
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI

load_dotenv()

# Load Titanic dataset
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE_DIR, "titanic.csv"))

# Create LLM using Grok (OpenAI-compatible)
llm = ChatOpenAI(
    temperature=0,
    model="llama-3.3-70b-versatile", 
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base=os.getenv("OPENAI_BASE_URL"),
)

agent = create_pandas_dataframe_agent(
    llm,
    df,
    verbose=False,
    allow_dangerous_code=True,
    prefix="""
You are a data analyst working with the Titanic dataset.
Always round numerical answers to 2 decimal places unless explicitly asked for more precision.
Provide clear and concise explanations.
"""
)

def ask_agent(question: str):
    return agent.run(question)