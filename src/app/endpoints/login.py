from app import database, models, schemas, security
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/get-token", include_in_schema=False)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(database.get_session),
):
    user = (
        session.query(models.User)
        .filter(models.User.username == form_data.username)
        .first()
    )
    if not user:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not security.pwd_context.verify(form_data.password, user.password):
        raise HTTPException(
            status.HTTP_403_FORBIDDEN,
            detail="Invalid password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = security.create_access_token(user.username)
    return {"access_token": token, "token_type": "bearer"}


@router.get("/me", response_model=schemas.UserOut)
async def get_user(user: models.User = Depends(security.get_user)):
    return user
