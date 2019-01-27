from quart import Blueprint
from api.controllers import Applications

apps_routes = Blueprint('apps', __name__)

apps_routes.add_url_rule("/apps", view_func=Applications.as_view('home'))
