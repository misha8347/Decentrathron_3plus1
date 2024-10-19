import google.generativeai as genai
import os
from dotenv import load_dotenv

def generate_response(prompt: str):
    load_dotenv()
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text