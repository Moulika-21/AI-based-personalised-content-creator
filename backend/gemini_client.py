import os
import google.genai as genai
from google.genai import errors
from dotenv import load_dotenv
import traceback

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_content(prompt):
    try:
        response = client.models.generate_content(model="gemini-3-flash-preview", contents=prompt)
        return response.text
    except Exception as e:
        print(str(e))
        traceback.print_exc()
        return None
