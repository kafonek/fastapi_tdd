import os

import sqlalchemy as sa
import sqlalchemy.orm

from app.config import get_settings

settings = get_settings()

engine = sa.create_engine(
    settings.database_url, connect_args={"check_same_thread": False}, echo=True
)

SessionLocal = sa.orm.sessionmaker(bind=engine)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
