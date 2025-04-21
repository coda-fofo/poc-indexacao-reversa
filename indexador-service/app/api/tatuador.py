import requests

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from app.core.database import SessionDep
from app.schemas.tatuador import TatuadorCreate
from app.repositories.tatuador_repo import create_tatuador
from app.repositories import tatuador_indice_repo
from app.config.env import SettingsDep

router = APIRouter()

@router.post(
        "/index",
        summary="Criação e indexação de tatuadores.", 
        tags=["Indexação Reversa"], 
        status_code=status.HTTP_201_CREATED
)
def criar_tatuador(
    tatuador: TatuadorCreate,
    db: SessionDep,
    settings: SettingsDep
):
    #Cria o tatuador 
    novo_tatuador = create_tatuador(db, tatuador)
    
    #Junta os dados em uma frase só
    frase = " ".join ([
        tatuador.nome_de_usuario,
        tatuador.nome_completo,
        tatuador.descricao,
        " ".join(tatuador.hashtags)
    ]) 

    tokenizer_url = settings.tokenizador_core_url.rstrip("/") + "/pipeline/tokenizar?versao=tokenizador-v1"

    #Envia ao serviço tokenizador
    try:
        response = requests.post(tokenizer_url, json={"frase": frase})
        response.raise_for_status()
        tokens = response.json().get("tokens")
    except requests.RequestException as e:
        print("Erro ao se comunicar com o serviço de tokenização:", e)
        tokens = []

    #Salva os dodos no banco
    for token in set(tokens):
        tatuador_indice_repo.adicionar_token(db, token, novo_tatuador.id)    
    
    return novo_tatuador
