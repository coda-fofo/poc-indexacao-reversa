from sqlalchemy.orm import Session
from sqlalchemy import text

def adicionar_token(db: Session, token: str, tatuador_id: int):
    # Verifica se o token já existe
    resultado = db.execute(
        text("SELECT tatuadores_ids FROM tatuador_indice WHERE token = :token"),
        {"token": token}
    ).fetchone()

    if resultado:
        ids = resultado[0]
        if tatuador_id not in ids:
            #Atualiza adicionando o novo ID ao array (usando a função array_append do PostgreSQL)
            db.execute(
                text("UPDATE tatuador_indice SET tatuadores_ids = array_append(tatuadores_ids, :id) WHERE token = :token"),
                {"id": tatuador_id, "token": token}
            )
    else:
        db.execute(
            text("INSERT INTO tatuador_indice (token, tatuadores_ids) VALUES (:token, :ids)"),
            {"token": token, "ids": [tatuador_id]}
        )
    db.commit()