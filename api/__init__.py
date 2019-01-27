from quart import Quart
from gino.ext.quart import Gino

db = Gino()

def create_app(app_env):
    from api.apps import apps_routes

    app = Quart('platappform')
    app.config.from_pyfile('./config_{}.py'.format(app_env))

    db.init_app(app)

    app.register_blueprint(apps_routes)

    @app.after_request
    def enforce_json(response):
        response.headers["Content-type"] = "application/json"
        return response

    return app
