from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routers.brand import router as brand_router
from src.api.routers.model import router as model_router
from src.api.routers.car import router as car_router
from src.api.routers.auth import router as auth_router
from src.api.routers.user import router as user_router

from src.models.base import Base
from src.db.session import engine

from src.core.logging import setup_logging

@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    setup_logging()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=auth_router)
app.include_router(router=user_router)
app.include_router(router=brand_router)
app.include_router(router=model_router)
app.include_router(router=car_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=("*"),
    allow_methods=("*")
)
