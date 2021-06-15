from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app import models, schemas
from app.config import settings
from app.database import get_session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/get-token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"


def create_access_token(username: str, expires_delta: timedelta = None):
    if expires_delta:
        expires = datetime.utcnow() + expires_delta
    else:
        expires = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRES_MINUTES
        )
    to_encode = {"exp": expires, "username": str(username)}
    token = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return token


def get_user(
    token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        # note: jwet.decode when there is an 'exp' key in payload automatically
        #       checks for expiration / raises jwt.ExpiredSignatureError
    except JWTError:
        raise credentials_exception

    username = payload.get("username")
    expires = payload.get("exp")

    if not username:
        raise credentials_exception

    user = session.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise credentials_exception
    return user
