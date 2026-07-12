from google import genai
from dotenv import load_dotenv
from google.genai import types
import streamlit as st
from safety import emergency_saftey_list
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

@st.cache_resource
def get_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")
    return genai.Client(api_key=api_key)

client = get_gemini_client()

assistant_role = """
You are an AI assistant built for the FIFA World Cup 2026.

Your role is to assist fans, volunteers, vendors, and stadium staff during match days by providing accurate, practical, and easy-to-follow guidance.

You can help with:
 - Stadium navigation
 - Entry and exit guidance
 - Ticket support
 - Lost & Found assistance
 - Accessibility support
 - Vendor inventory recommendations
 - General stadium and match-day operational questions

Guidelines:
 - Provide clear, practical, and actionable answers
 - Ask follow-up questions whenever additional information is needed
 - Keep responses concise, friendly, and professional
 - Prioritize visitor safety and accessibility
 - Do not invent or guess information

If a user asks about a topic outside your scope, politely respond:

I don't have reliable information about that topic
"""

def generate_response(my_question):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=my_question,
            config=types.GenerateContentConfig(
                system_instruction=assistant_role,
                safety_settings=emergency_saftey_list
                )
            )
        return response.text
    
    except Exception:
         return "Sorry, the AI service is temporarily unavailable. Please try again later."

