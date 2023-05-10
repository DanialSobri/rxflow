from fastapi import FastAPI,APIRouter
from config import settings

import booking

router = APIRouter(prefix="/api/v1")

@router.get("/")
async def root():
    return {"message": "Hello Rxflow"}

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(router)
app.include_router(booking.router)
