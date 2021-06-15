from pydantic import BaseModel


class UserOut(BaseModel):
    username: str

    class Config:
        orm_mode = True
