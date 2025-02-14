from fastapi import FastAPI
from pydantic import BaseModel
from blog.schemas import Blog

app = FastAPI()


@app.post('/blog')
def create(request: Blog):
    return request
    return {'title':title, 'body':body}