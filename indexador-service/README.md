# indexador-service

> Serviço para a criação e indexação de tatuadores no banco de dados

## configurando a aplicação

- Primeiro, instale o gerenciador [Poetry](https://python-poetry.org).
- Depois, instale as dependências do projeto:

```bash
poetry install
```

- Por fim, inicie o app

```bash
uvicorn app.main:app --port 8011 --reload
```

## docker

```bash
docker build -t indexador-service .
docker run -p 8011:8011 --network=rabisko_network --name=indexador-service indexador-service
```