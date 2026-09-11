import os
import google.generativeai as genai

# Set API key into environment
os.environ['GEMINI_API_KEY'] = 'AQ.Ab8RN6KyBidkU5d6MtiAqOkztWOFH7_cZONdmnSNQpEs4JBZCw'
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

class GeminiAdapter:
    def __init__(self):
        pass

    async def generate(self, prompt: str, model: str = 'gemini-1.5-flash') -> str:
        try:
            m = genai.GenerativeModel('gemini-1.5-flash')
            res = m.generate_content(prompt)
            return res.text
        except Exception as e:
            return f'Gemini Error: {str(e)}'
