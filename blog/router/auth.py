from typing import Annotated
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from blog import schemas, models, database, repository
from sqlalchemy.orm import Session
from blog.repository import blog
from blog.hashing import Hash
from blog.token import create_access_token

router = APIRouter(tags=['Authentication'])

get_db = database.get_db

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid credentials. Please try again")
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect password')
    
    access_token = create_access_token(
        data={"sub": request.username}, 
    )
    return schemas.Token(access_token=access_token, token_type="bearer")

    return user

