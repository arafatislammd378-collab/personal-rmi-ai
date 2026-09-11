from abc import ABC, abstractmethod
from app.ai.models import AIRequest, AIResponse

class AIAdapter(ABC):
    @abstractmethod
    async def generate(self, request: AIRequest) -> AIResponse:
        pass
