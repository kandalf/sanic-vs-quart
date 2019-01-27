import os, pytest, asyncio

os.environ['APP_ENV'] = 'test'

from api import create_app, db
from sqlalchemy import create_engine

def aiotest(func):
    _app = create_app('test')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(func(_app))

@pytest.yield_fixture
def app():
    app = create_app('test')
    yield app

def reset_db():
    app = create_app("test")

    db_url = "postgresql://{}:{}@{}/{}".format(app.config["DB_USER"], app.config["DB_PASSWORD"], app.config["DB_HOST"], app.config["DB_DATABASE"])

    engine = create_engine(db_url)

    db.drop_all(engine)
    db.create_all(engine)
