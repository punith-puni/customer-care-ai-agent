import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def ask_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text


@app.get("/debug-env")
def debug_env():
    key = os.getenv("GOOGLE_API_KEY")
    return {
        "exists": key is not None,
        "length": len(key) if key else 0
    }