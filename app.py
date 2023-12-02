import streamlit as st
from langchain import HuggingFaceHub
from dotenv import load_dotenv
import os

load_dotenv('.env')
HF_API_KEY = os.getenv('HF_API_KEY')
os.environ['HUGGINGFACEHUB_API_TOKEN'] = HF_API_KEY


def load_answer(question):
    llm = HuggingFaceHub(repo_id="google/flan-t5-large")
    answer = llm(question)
    return answer

st.set_page_config(page_title="LangChain", page_icon="🔗", layout="wide")
st.header("LangChain")

def get_text():
    st.subheader("Enter your question below")
    question = st.text_input("YOU:")
    return question

user_input = get_text()
submit = st.button("Submit")

if submit:
    response = load_answer(user_input)
    st.subheader("QnA GPT:")
    st.write(response, unsafe_allow_html=True)

