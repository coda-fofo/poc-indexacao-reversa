from typing import Annotated
from fastapi import Depends
from src.clients.tokenizador_core_client import TokenizadorCoreClientDep
from src.model.database import SessionDep
from sqlmodel import select
from sqlalchemy.orm import selectinload
from src.model.models import TatuadorIndiceModel, TatuadorModel, TatuadorHashtagModel
from itertools import chain
from pydantic import BaseModel

class BuscaTatuadorResultado(BaseModel):
    id: int
    nome_de_usuario: str
    nome_de_exibicao: str
    descricao: str
    hashtags: list[str]

class BuscadorService:
    def __init__(self, client: TokenizadorCoreClientDep, session: SessionDep):
        self._client = client
        self._session = session

    def buscar_tatuadores(self, pesquisa: str, page: int, size: int) -> list[BuscaTatuadorResultado]:
        tokens = self._client.tokenizar(pesquisa)
        
        documentos = self._session.exec(
            select(TatuadorIndiceModel).where(TatuadorIndiceModel.token.in_(tokens))
        ).all()

        documentos_ids = tuple(chain.from_iterable(documento.tatuadores_ids for documento in documentos))
        
        # Esse procedimento é CARO. Pós POC: cuidar com muitos selects.
        stmt = (
            select(TatuadorModel)
            .where(TatuadorModel.id.in_(documentos_ids))
            .order_by(TatuadorModel.id)
            .limit(size)
            .offset((page - 1) * size)
            .options(
                selectinload(TatuadorModel.hashtags).selectinload(TatuadorHashtagModel.hashtag)
            )
        )

        tatuadores = self._session.exec(stmt).unique().all()

        return [
            BuscaTatuadorResultado(
                id=t.id,
                nome_de_usuario=t.nome_de_usuario,
                nome_de_exibicao=t.nome_de_exibicao,
                descricao=t.descricao,
                hashtags=[th.hashtag.hashtag for th in t.hashtags]
            )
            for t in tatuadores
        ]

def get_service(client: TokenizadorCoreClientDep, session: SessionDep):
    return BuscadorService(client, session)

BuscadorServiceDeps = Annotated[BuscadorService, Depends(get_service)]