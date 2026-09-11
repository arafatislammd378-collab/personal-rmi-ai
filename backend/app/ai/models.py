from typing import Optional
from pydantic import BaseModel

class AIRequest(BaseModel):
    prompt: str
    model: Optional[str] = "gemini-1.5-flash"

class AIResponse(BaseModel):
    text: str
    provider: str
