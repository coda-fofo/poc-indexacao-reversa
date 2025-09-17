from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from core.database import Base

class WordUserLink(Base):
    __tablename__ = "word_user_link"
    __table_args__ = (UniqueConstraint('word_id', 'user_id', name='uix_word_user'),)

    word_id = Column(Integer, ForeignKey("words.id"), primary_key=True)
    user_id = Column(Integer, primary_key=True)

    word = relationship("Word", back_populates="users")