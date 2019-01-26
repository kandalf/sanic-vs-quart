from sanic import Blueprint
from api.controllers import Applications

apps_routes = Blueprint('apps')

apps_routes.add_route(Applications.as_view(), "/apps")
