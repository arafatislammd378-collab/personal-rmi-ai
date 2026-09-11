from google import genai
from app.core.config import settings

class GeminiAdapter:
    def __init__(self):
        self.api_key = settings.gemini_api_key

    def generate(self, prompt: str, model: str = 'gemini-3.6-flash') -> str:
        try:
            client = genai.Client(api_key=self.api_key)
            response = client.models.generate_content(
                model=model,
                contents=prompt,
            )
            return response.text
        except Exception as e:
            return f'Gemini Service Error: {str(e)}. Fallback engaged.'
