import streamlit as st
from main import generate_response

st.title("🤖 StadiumAssist AI")

my_question = st.text_input("Enter your query")

if my_question:
    answer = generate_response(my_question)
    st.write(answer)
