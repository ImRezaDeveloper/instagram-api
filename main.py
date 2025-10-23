from fastapi import FastAPI
from db import models
from db.database import engine
from routers import user, posts, comment
from fastapi.staticfiles import StaticFiles
from auth import authentication

app = FastAPI()

@app.get('/')
def root():
    return {'message': 'Hello World'}

models.Base.metadata.create_all(engine)

app.include_router(user.router)
app.include_router(posts.router)
app.include_router(authentication.router)
app.include_router(comment.router)


app.mount('/images', StaticFiles(directory='images'), name='images')