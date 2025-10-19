from fastapi import FastAPI
from db import models
from db.database import engine
from routers import user

app = FastAPI()

@app.get('/')
def root():
    return {'message': 'Hello World'}

models.Base.metadata.create_all(engine)

app.include_router(user.router)