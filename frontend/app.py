import streamlit as st
import requests
import base64

st.set_page_config(page_title="Titanic Chat Agent")

st.title("🚢 Titanic Dataset Chat Agent")

st.write("Ask questions about the Titanic dataset in plain English.")

question = st.text_input("Enter your question")

if st.button("Ask"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Analyzing dataset..."):
            response = requests.post(
                "http://127.0.0.1:8000/ask",
                json={"question": question}
            )

            data = response.json()

            st.subheader("Answer")
            st.write(data["answer"])

            if data["image"]:
                st.subheader("Visualization")
                image_bytes = base64.b64decode(data["image"])
                st.image(image_bytes)