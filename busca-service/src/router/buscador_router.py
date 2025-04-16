from fastapi import APIRouter
from fastapi import Query

from src.service.buscador_service import BuscadorServiceDeps

router = APIRouter(prefix="/buscador")

@router.get("/buscar")
def buscar_por_tatuadores(service: BuscadorServiceDeps, pesquisa: str = Query()):
    return service.buscar_tatuadores(pesquisa)
