from src.pipelines.v1 import PipelineV1
from src.pipelines import DescricaoPipeline
from src.http.frase_request import FraseRequest
from src.http.tokens_response import TokensResponse
from fastapi import FastAPI, Query

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

pipeline_v1 = PipelineV1()

@app.post("/pipeline/tokenizar", response_model=TokensResponse, summary="Transforma uma frase em linguagem natural para uma lista de tokens indexáveis.", tags=["Tokenização"])
def tokenizar(frase_request: FraseRequest, versao: str = Query(description="Versão da pipeline para utilizar na tokenização.")):
    if (versao == pipeline_v1.descricao_pipeline().id):
        tokens = pipeline_v1.rodar_pipeline(frase_request.frase)
        return { "tokens": tokens }
    
    raise RuntimeError("Pipeline não encontrada.")

@app.get("/pipeline/versoes", response_model=list[DescricaoPipeline], summary="Lista as versões disponíveis de tokenização.", tags=["Tokenização"])
def buscar_versoes_pipeline():
    return [
        pipeline_v1.descricao_pipeline()
    ]
