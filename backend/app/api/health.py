from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["System"]
)


@router.get("")
def health():
    return {
        "status": "healthy",
        "service": "personal-rmi-ai"
    }
