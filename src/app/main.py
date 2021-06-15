from fastapi import FastAPI

from app.endpoints import login, ping

app = FastAPI()
app.include_router(login.router, prefix="/login")
app.include_router(ping.router, prefix="/ping")
