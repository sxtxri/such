from fastapi import FastAPI

from src.api.router import api_router

app = FastAPI()

app.include_router(api_router)
