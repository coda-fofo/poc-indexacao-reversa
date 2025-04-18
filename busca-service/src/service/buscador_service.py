from typing import Annotated
from fastapi import Depends
from src.clients.tokenizador_core_client import TokenizadorCoreClientDep
from src.model.database import SessionDep
from sqlmodel import select
from src.model.models import TatuadorIndiceModel, TatuadorModel
from itertools import chain

class BuscadorService:
    def __init__(self, client: TokenizadorCoreClientDep, session: SessionDep):
        self._client = client
        self._session = session

    def buscar_tatuadores(self, pesquisa: str):
        tokens = self._client.tokenizar(pesquisa)
        
        documentos = self._session.exec(
            select(TatuadorIndiceModel).where(TatuadorIndiceModel.token.in_(tokens))
        ).all()

        documentos_ids = chain.from_iterable(documento.tatuadores_ids for documento in documentos)

        return self._session.exec(
            select(TatuadorModel).where(TatuadorModel.id.in_(documentos_ids))
        ).all()

def get_service(client: TokenizadorCoreClientDep, session: SessionDep):
    return BuscadorService(client, session)

BuscadorServiceDeps = Annotated[BuscadorService, Depends(get_service)]