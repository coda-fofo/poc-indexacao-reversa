FROM python:3.13-slim

RUN apt-get update && apt-get install -y curl libpq-dev
RUN curl -sSL https://install.python-poetry.org | python3

ENV PATH="/root/.local/bin:/app/.venv/bin:$PATH"
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

WORKDIR /app

COPY . .

RUN poetry install --no-root
RUN poetry run setup_nltk

EXPOSE 8010

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8010", "--reload"]