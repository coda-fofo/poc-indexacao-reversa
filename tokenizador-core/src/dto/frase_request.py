from pydantic import BaseModel

class FraseRequest(BaseModel):
    frase: str