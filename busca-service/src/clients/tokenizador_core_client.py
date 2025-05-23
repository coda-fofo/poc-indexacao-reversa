from typing import Annotated
from requests import post
from urllib.parse import urljoin
from fastapi import Depends
from src.config.env import SettingsDep

TokenizadorResponse = list[str]

class TokenizadorCoreClient:
    def __init__(self, settings: SettingsDep):
        self._base_uri = settings.tokenizador_core_url
        self._pipeline_version = settings.tokenizador_versao_pipeline
    
    def tokenizar(self, pesquisa: str) -> TokenizadorResponse:
        url = urljoin(self._base_uri, '/pipeline/tokenizar')
        response = post(url, params={'versao': self._pipeline_version}, json={'frase': pesquisa})

        if response.status_code != 200:
            raise ValueError(f"Erro ao tokenizar: {response.status_code} - {response.text}")

        return response.json().get('tokens', [])
    
def get_client(settings: SettingsDep):
    return TokenizadorCoreClient(settings)

TokenizadorCoreClientDep = Annotated[TokenizadorCoreClient, Depends(get_client)]