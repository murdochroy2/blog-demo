from fastapi import Depends, FastAPI, HTTPException, status, Response
from pydantic import BaseModel
from blog import  models
from blog.database import SessionLocal, engine
from sqlalchemy.orm import Session
from blog.router import blog, user, auth

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(auth.router)