from sanic import Sanic
from gino.ext.sanic import Gino

db = Gino()

def create_app(app_env):
    from api.apps import apps_routes

    app = Sanic('platappform')
    app.config.from_pyfile('./config_{}.py'.format(app_env))

    db.init_app(app)

    app.blueprint(apps_routes)

    return app
