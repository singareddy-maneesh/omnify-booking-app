import pytest 
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, session_local, engine

Base.metadata.drop_all(bind = engine)
Base.metadata.create_all(bind = engine)

@pytest.fixture(scope = "module")
def test_client():
    """ 
    Test client
    """
    with TestClient(app) as tc:
        yield tc 

@pytest.fixture(scope="module")
def db_session():
    """ 
    Test DB
    """
    db = session_local()
    try:
        yield db
    finally:
        db.close()

