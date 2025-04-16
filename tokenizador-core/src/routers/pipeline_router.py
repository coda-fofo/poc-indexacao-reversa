from fastapi import APIRouter, Query

from src.dto.tokens_response import TokensResponse
from src.dto.frase_request import FraseRequest
from src.services.pipelines import PipelineV1Dep
from src.services.pipelines.token_pipeline import DescricaoPipeline

router = APIRouter(prefix="/pipeline")

@router.post("/tokenizar", response_model=TokensResponse, summary="Transforma uma frase em linguagem natural para uma lista de tokens indexáveis.", tags=["Tokenização"])
def tokenizar(pipeline_v1: PipelineV1Dep, frase_request: FraseRequest, versao: str = Query(default="tokenizador-v1", description="Versão da pipeline para utilizar na tokenização.")):
    if (versao == pipeline_v1.descricao_pipeline().id):
        tokens = pipeline_v1.rodar_pipeline(frase_request.frase)
        return { "tokens": tokens }
    
    raise RuntimeError("Pipeline não encontrada.")

@router.get("/versoes", response_model=list[DescricaoPipeline], summary="Lista as versões disponíveis de tokenização.", tags=["Tokenização"])
def buscar_versoes_pipeline(pipeline_v1: PipelineV1Dep):
    return [
        pipeline_v1.descricao_pipeline()
    ]
