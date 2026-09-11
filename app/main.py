from fastapi import FastAPI, HTTPException
from app.ai.models import AIRequest, AIResponse
from app.ai.router import router

app = FastAPI(title="Personal RMI AI Service")

@app.get("/")
def read_root():
    return {"message": "AI Backend System is Running"}

@app.post("/api/v1/generate", response_model=AIResponse)
async def generate_response(provider: str, request: AIRequest):
    try:
        return await router.route(provider, request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
