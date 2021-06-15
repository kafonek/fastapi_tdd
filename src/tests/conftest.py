import pytest
from app import database, main, models
from passlib.hash import bcrypt
from starlette.testclient import TestClient


@pytest.fixture(scope="session")
def db():
    yield database.SessionLocal()


@pytest.fixture(scope="module")
def client():
    with TestClient(main.app) as test_client:
        yield test_client


@pytest.fixture(scope="session", autouse=True)
def create_test_data(db):
    test_user = models.User(username="test", password=bcrypt.hash("test"))
    db.add(test_user)
    db.commit()

    yield

    db.query(models.User).delete()
    db.commit()
    db.close()
