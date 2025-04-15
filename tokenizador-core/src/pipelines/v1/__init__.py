import re

from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

from src.pipelines import TokensPipeline, DescricaoPipeline

STOP_WORDS = set(stopwords.words('portuguese'))
STEMMER = SnowballStemmer("portuguese")

class PipelineV1(TokensPipeline):
    def __init__(self):
        self._stopWords = set(stopwords.words('portuguese'))
        self._stemmer = SnowballStemmer("portuguese")
        
    def rodar_pipeline(self, texto):
        texto_sanitizado = self._sanitizar_texto(texto)
        texto_tokenizado = self._tokenizar_texto(texto_sanitizado)
        tokens_relevantes = self._remover_stopwords(texto_tokenizado)
        tokens_radicalizados = self._aplicar_stemming(tokens_relevantes)
        
        return tokens_radicalizados
    
    def descricao_pipeline(self):
        return DescricaoPipeline(
            id="tokenizador-v1",
            descricao="Primeira versão do Tokenizador. Remove caractéres especiais, stop-words e radicaliza os tokens."
        )
    
    def _sanitizar_texto(self, texto: str) -> str:        
        texto = texto.strip()
        texto = re.sub(r'[^\w\s]', '', texto)
        texto = texto.lower()
        
        return texto


    def _tokenizar_texto(self, texto: str) -> list[str]:
        return word_tokenize(texto)


    def _remover_stopwords(self, tokens: list[str]) -> list[str]:
        return [word for word in tokens if word not in self._stopWords]


    def _aplicar_stemming(self, tokens: list[str]) -> list[str]:
        return [self._stemmer.stem(word) for word in tokens]