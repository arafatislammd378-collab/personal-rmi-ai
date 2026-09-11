import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

try:
    print("Testing gemini-3.6-flash...")
    response = client.models.generate_content(
        model='gemini-3.6-flash',
        contents='Say Hello in Bengali!',
    )
    print("\n--- GEMINI RESPONSE ---")
    print(response.text)
except Exception as e:
    print(f"\nError Details: {e}")
