from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get("/blog")
def index(limit = None, published: bool = True):
    # return published
    if published:
        return {"data": f'{limit} blogs from the published blog list'}
    else:
        return {"data": 'all blogs'}

@app.get("/about")
def abc():
    return {"data":"string"}


@app.get('/blog/unpublished')
def get_unpublished():
    return {'data':'unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    return {'data':id}


@app.get('/blog/{id}/comments')
def show_comments(id, limit):
    return limit
    return {'data':{'1', '2'}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = True
 
@app.post('/blog')
def create_blog(blog: Blog):
    return {"data":f"blog with title {blog.title} created"}

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)