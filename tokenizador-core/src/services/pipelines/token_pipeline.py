from abc import ABC, abstractmethod
from pydantic import BaseModel

class DescricaoPipeline(BaseModel):
    """
    Informações complementares para a Pipeline.
    """
    id: str
    descricao: str

class TokensPipeline(ABC):
    """
    Define o processo de tranformação dos dados para _tokens_.
    """
    
    @abstractmethod
    def rodar_pipeline(self, texto: str) -> list[str]:
        """
        Transforma um texto em um conjunto de tokens.
        """
        pass

    @abstractmethod
    def descricao_pipeline(self) -> DescricaoPipeline:
        """
        Retorna a descrição da pipeline.
        """
        pass
