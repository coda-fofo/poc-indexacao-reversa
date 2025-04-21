from fastapi import APIRouter
from fastapi import Query

from src.service.buscador_service import BuscadorServiceDeps, BuscaTatuadorResultado

router = APIRouter(prefix="/buscador")

@router.get("/buscar", summary="Busca por tatuadores disponíveis no Rabisko.", tags=["Motor de Busca"])
def buscar_por_tatuadores(service: BuscadorServiceDeps, pesquisa: str = Query(), page: int = Query(1, ge=1), size: int = Query(10, ge=1, le=20)) -> list[BuscaTatuadorResultado]:
    return service.buscar_tatuadores(pesquisa, page, size)
