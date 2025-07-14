from sqlmodel import create_engine, Session, SQLModel

from ..core.config import get_settings


settings = get_settings()

DB_STR_CONNECTION = settings.DB_STR_CONNECTION
DB_ECHO = settings.DB_ECHO 

engine = create_engine(DB_STR_CONNECTION, echo=DB_ECHO)


def get_session():
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

