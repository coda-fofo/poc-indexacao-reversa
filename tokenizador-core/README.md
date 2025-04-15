# tokenizador-core

> Serviço para a tokenização de linguagem natural no TattooGo.

## Configurando a Aplicação

- Primeiro, instale o gerenciador [Poetry](https://python-poetry.org).
- Depois, instale as dependências do projeto:

```bash
poetry install
poetry run setup_nltk
```

- Por fim, inicie o app:

```bash
uvicorn src.main:app --reload
```

- E acesse [`localhost:8000/docs`](http://localhost:8000/docs).