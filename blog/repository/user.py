from fastapi import APIRouter, HTTPException, status, Depends
from blog import schemas, models
from sqlalchemy.orm import Session
from blog.hashing import Hash
from passlib.context import CryptContext

def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"detail": f"User with id {id} not found"},
        )
    return user

def create(request: schemas.User, db: Session):
    # new_user = models.User(**request.model_dump())
    hashed_password = Hash.bcrypt(request.password)
    new_user = models.User(
        name=request.name, email=request.email, password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user