from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.core.database import Base
from sqlalchemy.dialects.postgresql import ARRAY

class Tatuador(Base):
    __tablename__ = "Tatuador"

    id: int = Column(Integer, primary_key=True, index=True)
    nome_de_usuario: str = Column(String(32), nullable=False)
    nome_de_exibicao: str = Column(String(64), nullable=False)
    descricao: str = Column(String(256), nullable=False)

    hashtags = relationship("Hashtag", secondary="Tatuador_Hashtag", back_populates="tatuadores")

class Hashtag(Base):
    __tablename__ = "Hashtag"

    id: int = Column(Integer, primary_key=True, index=True)
    hashtag: str = Column(String(128), nullable=False, unique=True)

    tatuadores = relationship("Tatuador", secondary="Tatuador_Hashtag", back_populates="hashtags")

class TatuadorHashtag(Base):
    __tablename__ = "Tatuador_Hashtag"
    
    id: int = Column(Integer, primary_key=True, index=True)
    tatuador_id: int  = Column(Integer, ForeignKey("Tatuador.id"), nullable=False)
    hashtag_id: int = Column(Integer, ForeignKey("Hashtag.id"), nullable=False)

class TatuadorIndice(Base):
    __tablename__ = "tatuador_indice"

    token: str = Column(String(255), primary_key=True, index=True)
    tatuadores_ids: list[int] = Column(ARRAY(Integer), nullable=False)  
