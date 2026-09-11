from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.ai.adapters.gemini import GeminiAdapter

router = APIRouter()
gemini_adapter = GeminiAdapter()

class AIRequest(BaseModel):
    prompt: str
    model: str = 'gemini-3.6-flash'

class AIResponse(BaseModel):
    text: str
    provider: str

@router.post('/generate', response_model=AIResponse)
def generate_response(request: AIRequest, provider: str = 'gemini'):
    if provider.lower() == 'gemini':
        response_text = gemini_adapter.generate(prompt=request.prompt, model=request.model)
        return AIResponse(text=response_text, provider='gemini')
    else:
        raise HTTPException(status_code=400, detail='Unsupported provider')
