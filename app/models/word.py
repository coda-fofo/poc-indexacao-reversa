from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.database import Base

class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, unique=True, index=True)

    users = relationship("WordUserLink", back_populates="word")
    