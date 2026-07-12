import streamlit as st
from main import generate_response

st.set_page_config(
    page_title="StadiumAssist AI",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 StadiumAssist AI")


my_question = st.text_input(
    label="Enter your stadium or event query below:",
    placeholder="e.g., Where is the nearest parking lot or food court?",
    help="Type your question and press Enter to receive an automated AI response"
)

if my_question:
    with st.spinner("StadiumAssist AI is processing your request..."):
        answer = generate_response(my_question)
        st.write(answer)
    
