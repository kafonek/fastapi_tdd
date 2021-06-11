import pytest
from app import database, main, models
from passlib.hash import bcrypt
from starlette.testclient import TestClient


@pytest.fixture(scope="session", autouse=True)
def create_test_user():
    with database.SessionLocal() as session:
        test_user = models.User(username="test", password=bcrypt.hash("test"))
        session.add(test_user)
        session.commit()

        yield

        # clear out the User table
        session.query(models.User).delete()
        session.commit()
        session.close()


@pytest.fixture
def client():
    with TestClient(main.app) as test_client:
        yield test_client
