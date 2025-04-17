from fastapi import FastAPI
from core.database import engine, Base
from api import indexer

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(indexer.router)