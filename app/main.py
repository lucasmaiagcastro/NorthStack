from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(title="Northstack")

app.include_router(router)
