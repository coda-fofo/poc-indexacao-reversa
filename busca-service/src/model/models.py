from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import ARRAY

class TatuadorHashtagModel(SQLModel, table=True):
    __tablename__ = "tatuador_hashtag"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    tatuador_id: int = Field(foreign_key="tatuador.id", nullable=False)
    hashtag_id: int = Field(foreign_key="hashtag.id", nullable=False)

    tatuador: Optional["TatuadorModel"] = Relationship(back_populates="hashtags")
    hashtag: Optional["HashtagModel"] = Relationship(back_populates="tatuadores")

class TatuadorModel(SQLModel, table=True):
    __tablename__ = "tatuador"

    id: Optional[int] = Field(default=None, primary_key=True)
    nome_de_usuario: str = Field(max_length=32, nullable=False)
    nome_de_exibicao: str = Field(max_length=64, nullable=False)
    descricao: str = Field(max_length=255, nullable=False)

    hashtags: List["TatuadorHashtagModel"] = Relationship(back_populates="tatuador")

class HashtagModel(SQLModel, table=True):
    __tablename__ = "hashtag"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    hashtag: str = Field(max_length=128, nullable=False)

    tatuadores: List["TatuadorHashtagModel"] = Relationship(back_populates="hashtag")

class TatuadorIndiceModel(SQLModel, table=True):
    __tablename__ = "tatuadorindice"

    token: str = Field(primary_key=True, max_length=255)
    tatuadores_ids: List[int] = Field(sa_column=Column(ARRAY(Integer)))
