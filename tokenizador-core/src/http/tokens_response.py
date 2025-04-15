from pydantic import BaseModel

class TokensResponse(BaseModel):
    tokens: list[str]