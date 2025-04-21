from fastapi import FastAPI
from src.router import buscador_router
from fastapi.middleware.cors import CORSMiddleware

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

origins = [ 
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(buscador_router)