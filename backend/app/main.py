from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.ai.router import router as ai_router

app = FastAPI(
    title='Personal RMI AI API',
    docs_url='/docs',
    openapi_url='/openapi.json'
)

@app.get('/')
async def root():
    return {'message': 'Server is running! Go to /docs for API documentation.'}

app.include_router(ai_router, prefix='/api/v1', tags=['AI'])
