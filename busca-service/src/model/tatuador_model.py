from sqlmodel import SQLModel, Field

class TatuadorModel(SQLModel, table=True):
    __tablename__ = 'Tatuador'

    id: int = Field(default=None, primary_key=True, title='id')
    nome_de_usuario: str = Field(max_length=32, nullable=False, title='nome_de_usuario')
    nome_de_exibicao: str = Field(max_length=64, nullable=False, title='nome_de_exibicao')
    descricao: str = Field(max_length=255, nullable=False, title='descricao')
