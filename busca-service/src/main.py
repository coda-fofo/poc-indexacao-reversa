from fastapi import FastAPI
from src.router import buscador_router

app = FastAPI()

app.include_router(buscador_router)