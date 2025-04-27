from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.core.database import Base
from sqlalchemy.dialects.postgresql import ARRAY
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import ARRAY

class Tatuador(SQLModel, table=True):
    __tablename__ = "tatuador"

    id: Optional[int] = Field(default=None, primary_key=True)
    nome_de_usuario: str = Field(max_length=32, nullable=False)
    nome_de_exibicao: str = Field(max_length=64, nullable=False)
    descricao: str = Field(max_length=255, nullable=False)

    hashtags: List["TatuadorHashtag"] = Relationship(back_populates="tatuador")

class Hashtag(SQLModel, table=True):
    __tablename__ = "hashtag"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    hashtag: str = Field(max_length=128, nullable=False)

    tatuadores: List["TatuadorHashtag"] = Relationship(back_populates="hashtag")

class TatuadorHashtag(SQLModel, table=True):
    __tablename__ = "tatuador_hashtag"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    tatuador_id: int = Field(foreign_key="tatuador.id", nullable=False)
    hashtag_id: int = Field(foreign_key="hashtag.id", nullable=False)

    tatuador: Optional["Tatuador"] = Relationship(back_populates="hashtags")
    hashtag: Optional["Hashtag"] = Relationship(back_populates="tatuadores")
    

class TatuadorIndice(SQLModel, table=True):
    __tablename__ = "tatuadorindice"

    token: str = Field(primary_key=True, max_length=255)
    tatuadores_ids: List[int] = Field(sa_column=Column(ARRAY(Integer))) 
