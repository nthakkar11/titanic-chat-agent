# 🚢 Titanic Dataset Chat Agent

An AI-powered chatbot that analyzes the Titanic dataset using natural language queries.

Users can ask questions in plain English and receive:

- 📊 Accurate statistical answers
- 📈 Automatically generated visualizations
- 💬 Clean and readable explanations

---

## 🔧 Tech Stack

- **Backend:** FastAPI
- **LLM Framework:** LangChain (Pandas Agent)
- **LLM Provider:** Groq (Llama 3.3)
- **Frontend:** Streamlit
- **Data Handling:** Pandas
- **Visualization:** Matplotlib, Seaborn

---

## 🧠 How It Works

1. User submits a natural language question via Streamlit.
2. The request is sent to the FastAPI backend.
3. A LangChain Pandas DataFrame Agent:
   - Interprets the question
   - Generates Python code
   - Executes analysis on the Titanic dataset
4. The backend returns:
   - A text response
   - A visualization (if applicable)
5. Streamlit displays the results in a clean interface.

---

## 📊 Example Questions

- What percentage of passengers were male?
- What was the average ticket fare?
- Show a histogram of passenger ages.
- How many passengers embarked from each port?
- What was the survival rate?

---

## 🚀 Live Demo

Streamlit App:

https://your-streamlit-url.streamlit.app


Backend API:

https://your-render-url.onrender.com/docs


---

## 🗂 Project Structure


titanic-dataset-agent/
│
├── backend/
│ ├── main.py
│ ├── agent.py
│ ├── titanic.csv
│
├── frontend/
│ ├── app.py
│
├── requirements.txt
└── README.md


---

## ⚙️ Environment Variables

The following environment variables are required:


OPENAI_API_KEY=your_groq_api_key
OPENAI_BASE_URL=https://api.groq.com/openai/v1


---

## 📌 Key Features

- Natural language dataset querying
- Automated statistical computation
- Dynamic visualization generation
- Modular backend + frontend architecture
- Cloud deployment ready

---

## 🎯 Assignment Goal

This project demonstrates:

- Practical LLM integration
- Agent-based reasoning with tools
- API-based architecture
- Clean UI presentation
- Production-style deployment

---