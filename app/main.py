from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes import router
from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    if settings.otel_enabled:
        from agno.db.sqlite import SqliteDb
        from agno.tracing import setup_tracing

        db = SqliteDb(db_file="tmp/traces.db")
        setup_tracing(db=db)

    yield


app = FastAPI(title="Northstack", lifespan=lifespan)

app.include_router(router)
