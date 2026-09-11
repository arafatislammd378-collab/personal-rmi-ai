from fastapi import APIRouter
from app.ai.models import AIRequest, AIResponse
from app.ai.router import ai_router

router = APIRouter(
    prefix="/api/chat",
    tags=["Chat"]
)

@router.post("", response_model=AIResponse)
async def chat(request: AIRequest):
    return await ai_router.route(request)
