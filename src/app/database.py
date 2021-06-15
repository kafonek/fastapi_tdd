import os

import sqlalchemy as sa
import sqlalchemy.orm

from app.config import settings

engine = sa.create_engine(
    settings.DATABASE_URL, connect_args={"check_same_thread": False}, echo=settings.DB_ECHO
)

SessionLocal = sa.orm.sessionmaker(bind=engine)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
