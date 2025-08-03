from fastapi import APIRouter

from src.api.boards.router import api_boards_router

api_router = APIRouter(prefix="/api")

api_router.include_router(api_boards_router)
