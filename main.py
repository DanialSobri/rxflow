from typing import Optional
from fastapi import FastAPI,APIRouter
from config import settings

import booking

router = APIRouter(prefix="/api/v1")

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)
app.include_router(router)
app.include_router(booking.router)
