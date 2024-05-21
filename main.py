from fastapi import FastAPI
from route import router as items_route
from contextlib import asynccontextmanager
from db import create_tables, delete_tables


@asynccontextmanager
async def lifespan(_app: FastAPI):
    await delete_tables()
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(items_route)