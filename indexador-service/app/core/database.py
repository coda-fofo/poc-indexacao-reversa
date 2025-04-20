from typing import Annotated
from sqlmodel import create_engine, Session
from sqlalchemy import Engine
from sqlalchemy.orm import declarative_base
from fastapi import Depends

Base = declarative_base()

from app.config.env import SettingsDep

def get_engine(settings: SettingsDep):
    return create_engine(settings.database_uri)

def get_session(engine: Annotated[Engine, Depends(get_engine)]):
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]