from typing import Annotated
from fastapi import Depends
from src.clients.tokenizador_core_client import TokenizadorCoreClientDeps

class BuscadorService:
    def __init__(self, client: TokenizadorCoreClientDeps):
        self._client = client

    def buscar_tatuadores(self, pesquisa: str):
        return self._client.tokenizar(pesquisa)
    
def get_service(client: TokenizadorCoreClientDeps):
    return BuscadorService(client)

BuscadorServiceDeps = Annotated[BuscadorService, Depends(get_service)]