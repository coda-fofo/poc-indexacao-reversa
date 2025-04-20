from fastapi import FastAPI
from app.api import tatuador
from app.core.database import get_engine, Base
from app.config.env import get_env

app = FastAPI(
    title="API-Indexadora",
    description="Serviço para criação e indexação de tatuadores no banco de dados",
    version="1.0.0",
    contact={"nome_de_usuario": "Joao_Pedro123",
             "nome_completo": "João Pedro",
             "descricao": "O ser humano mais humano de todos",
             "hashtags": [
                 "top", "curibs", "tatuagem", "top"
             ]
    },
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

Base.metadata.create_all(bind=get_engine(get_env()))

app.include_router(tatuador.router)