import streamlit as st
from main import generate_response

st.set_page_config(
    page_title="StadiumAssist AI",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 StadiumAssist AI")

st.markdown("""
Welcome to **StadiumAssist AI**.

Get help with:
- 🗺️ Stadium Navigation
- 🎫 Ticket Support
- 🎒 Lost & Found
- ♿ Accessibility Services
- 🍔 Vendor Recommendations
- 🚪 Entry & Exit Guidance
""")

my_question = st.text_input(
    label="Enter your stadium or event query below:",
    placeholder="e.g., Where is the nearest parking lot or food court?",
    help="Type your question and press Enter to receive an automated AI response"
)

if st.button("Get Assistance"):

    if not my_question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating response..."):
            answer = generate_response(my_question)

        st.subheader("Response")
        st.success(answer)

st.caption(
    "StadiumAssist AI provides general stadium assistance and may not reflect live match-day updates."
)
    
