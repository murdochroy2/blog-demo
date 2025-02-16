from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import HTTPException
from pydantic import BaseModel
import jwt
from jwt.exceptions import InvalidTokenError

from blog.schemas import TokenData

SECRET_KEY = "a09bc3035508b4f0af3239e09456acafda41e87eea7d48e99cf4fb9c994298f5"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30



def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy() 
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str, credentials_exception: HTTPException):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(username=email)
    except InvalidTokenError:
        raise credentials_exception