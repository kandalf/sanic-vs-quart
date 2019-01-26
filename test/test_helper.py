import os, pytest

os.environ['APP_ENV'] = 'test'

from api import create_app, db
from sqlalchemy import create_engine

@pytest.yield_fixture
def app():
    app = create_app('test')
    yield app

@pytest.fixture
def test_cli(loop, app, test_client):
    return loop.run_until_complete(test_client(app))


def reset_db():
    app = create_app("test")

    db_url = "postgresql://{}:{}@{}/{}".format(app.config["DB_USER"], app.config["DB_PASSWORD"], app.config["DB_HOST"], app.config["DB_DATABASE"])

    engine = create_engine(db_url)

    db.drop_all(engine)
    db.create_all(engine)
