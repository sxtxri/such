from fastapi import APIRouter

from src.api.boards.endpoints.get_boards import api_boards_get_boards_router

api_boards_router = APIRouter(prefix="/boards")

api_boards_router.include_router(api_boards_get_boards_router)
