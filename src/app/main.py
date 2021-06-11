import logging

from fastapi import Depends, FastAPI

from app import models, schemas, security

app = FastAPI()
app.include_router(security.router)


@app.get("/ping")
async def ping():
    return {"ping": "pong"}


@app.get("/user", response_model=schemas.User)
async def get_user(user: models.User = Depends(security.get_user)):
    return user
