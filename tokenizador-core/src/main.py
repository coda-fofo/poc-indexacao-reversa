from fastapi import FastAPI
from src.routers import pipeline_router

app = FastAPI(
    title="Tokenizador API",
    description="Serviço para a tokenização de linguagem natural no TattooGo.",
    version="1.0.0",
    contact={
        "name": "Coda Fofo",
        "email": "caiohporcel@gmail.com"
    },
    docs_url="/docs",           
    redoc_url="/redoc",         
    openapi_url="/openapi.json"
)

app.include_router(pipeline_router)