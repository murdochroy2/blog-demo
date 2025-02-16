from fastapi import APIRouter, HTTPException, status, Depends
from blog import schemas, models, database
from sqlalchemy.orm import Session
from blog.hashing import Hash
from passlib.context import CryptContext
from blog.repository import user


router = APIRouter(prefix="/user", tags=["Users"])

get_db = database.get_db

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)
