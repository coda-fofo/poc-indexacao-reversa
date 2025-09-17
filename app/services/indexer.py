from sqlalchemy.orm import Session
from models.word import Word
from models.word_user_link import WordUserLink

def index_words(db: Session, user_id: int, words: list[str]):
    for token in words:
        token = token.lower().strip()

        #Verifica se a palavra já existe
        word = db.query(Word).filter_by(token=token).first()
        if not word:
            word = Word(token=token)
            db.add(word)
            db.commit()
            db.refresh(word)

        #Verifica se o relacionamento já existe
        link_exists = db.query(WordUserLink).filter_by(word_id=word.id, user_id=user_id).first()
        if not link_exists:
            link = WordUserLink(word_id=word.id, user_id=user_id)
            db.add(link)
            db.commit()