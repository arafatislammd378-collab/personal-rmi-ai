from pydantic import BaseModel
from typing import Optional

class AIRequest(BaseModel):
    message: str
    model: Optional[str] = None
    task: str = "chat"

class AIResponse(BaseModel):
    text: str
    model: str
    provider: str
