from app.ai.adapters.base import AIAdapter
from app.ai.models import AIRequest, AIResponse

class MockAIAdapter(AIAdapter):
    async def generate(self, request: AIRequest) -> AIResponse:
        return AIResponse(
            text=f"RMI-AI received: {request.message}",
            model="mock-v1",
            provider="internal"
        )
