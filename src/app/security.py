from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.config import get_settings
from app.database import get_session
from app.models import User

settings = get_settings()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/security/login")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter(prefix="/security")


@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
):
    print("Query for all Users: %s" % session.query(User).all())
    user = session.query(User).filter(User.username == form_data.username).first()
    if not user:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not pwd_context.verify(form_data.password, user.password):
        raise HTTPException(
            status.HTTP_403_FORBIDDEN,
            detail="Invalid password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    data = {"username": user.username}
    token = jwt.encode(data, settings.secret_key, algorithm="HS256")
    return {"access_token": token, "token_type": "bearer"}


def get_user(
    token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=["HS256"])
        username = payload.get("username")
        if not username:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = session.query(User).filter(User.username == username).first()
    if not user:
        raise credentials_exception
    return user
