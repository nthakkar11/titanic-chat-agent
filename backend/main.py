import io
import os
import base64
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from fastapi import FastAPI
from pydantic import BaseModel

from backend.agent import ask_agent
from fastapi.middleware.cors import CORSMiddleware

# Load dataset for plotting
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE_DIR, "titanic.csv"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for assignment, allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

def generate_plot(question):
    plt.figure()
    q = question.lower()

    if "histogram" in q and "age" in q:
        sns.histplot(df["Age"].dropna(), bins=20)
        plt.title("Age Distribution")

    elif "embarked" in q:
        df["Embarked"].value_counts().plot(kind="bar")
        plt.title("Passengers by Embarkation Port")

    else:
        return None

    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)

    image_base64 = base64.b64encode(buffer.read()).decode()
    plt.close()

    return image_base64

@app.post("/ask")
def ask(query: Query):
    try:
        answer = ask_agent(query.question)
        image = generate_plot(query.question)

        return {
            "answer": answer,
            "image": image
        }

    except Exception as e:
        return {"answer": str(e), "image": None}