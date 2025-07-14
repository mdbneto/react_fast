from contextlib import asynccontextmanager
from fastapi import FastAPI

from .db.init_db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup Logic
    init_db()
    print('Database initialized')

    yield

    # Shutdown logic
    print('Shutting down...')
    

app = FastAPI(
    title="Backend test",
    lifespan=lifespan,
) 


@app.get("/")
def read_root():
    return {"Hello": "World"}

