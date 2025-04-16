from sqlmodel import SQLModel, Field

class HashtagModel(SQLModel, table=True):
    __tablename__ = 'Hashtag'
    
    id: int = Field(default=None, primary_key=True, title="id")
    hashtag: str = Field(title='hashtag')
    