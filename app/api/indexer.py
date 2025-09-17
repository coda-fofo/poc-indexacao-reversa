from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from services.indexer import index_words
from pydantic import BaseModel

router = APIRouter()

class IndexRequest(BaseModel):
    user_id: int
    tokens: list[str]

@router.post("/index")
def index_user_words(payload: IndexRequest, db: Session = Depends(get_db)):
    index_words(db, payload.user_id, payload.tokens)
    return {"message": "Palavras indexadas com sucesso!"}