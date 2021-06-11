import uuid

import sqlalchemy as sa
import sqlalchemy.orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import UUIDType

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String, unique=True)
    password = sa.Column(sa.String)  # only put hashed values in here
