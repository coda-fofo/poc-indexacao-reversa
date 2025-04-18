# busca-service

> Serviço para buscar por tatuadores no Rabisko.

## Configurando a Aplicação

- Primeiro, instale o gerenciador [Poetry](https://python-poetry.org).
- Depois, instale as dependências do projeto:

```bash
poetry install
```

- Por fim, inicie o app:

```bash
uvicorn src.main:app --reload 
```

- E acesse [`localhost:8000/docs`](http://localhost:8000/docs).