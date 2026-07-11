from google import genai
from dotenv import load_dotenv
from google.genai import types
from safety import emergency_saftey_list
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

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
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=my_question,
        config=types.GenerateContentConfig(
            system_instruction=assistant_role,
            safety_settings=emergency_saftey_list
        )
    )
    return response.text

