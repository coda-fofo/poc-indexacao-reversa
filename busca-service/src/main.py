from fastapi import FastAPI
from src.router import buscador_router

app = FastAPI(
    title="Buscador API",
    description="Serviço para buscar por tatuadores no Rabisko.",
    version="1.0.0",
    contact={
        "name": "Coda Fofo",
        "email": "caiohporcel@gmail.com"
    },
    docs_url="/docs",           
    redoc_url="/redoc",         
    openapi_url="/openapi.json"
)

app.include_router(buscador_router)