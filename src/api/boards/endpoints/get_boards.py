from fastapi import APIRouter

api_boards_get_boards_router = APIRouter()


@api_boards_get_boards_router.get(
    "/such:getBoards",
)
async def get_boards():
    return {"12": "213"}
