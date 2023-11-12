from datetime import time

import psycopg2
from psycopg2.extras import RealDictCursor
from fastapi import FastAPI

from . import models
from .database import engine
from .routers import post, user, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()





while True:
    try:
        conn = psycopg2.connect(host="localhost", database="fastapi", user="postgres", password="12345678",
                                cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("database connection was successfully!")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)
        time.sleep(2)

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "favorite foods", "content": "i like pizza", "id": 2}
            ]


# def find_post(id):
#     for post in my_posts:
#         if post['id'] == id:
#             return post
#     return None
#
#
# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "Hello World"}




