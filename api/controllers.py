from sanic.views import HTTPMethodView
from sanic.response import json
from datetime import datetime
from .models import Application
from .helpers import app_to_dict, apps_to_dict
from .validators import ApplicationValidator

class Applications(HTTPMethodView):
    async def get(self, request):
        apps = await Application.query.gino.all()

        return json(apps_to_dict(apps), status=200)


    async def post(self, request):
        app_attributes = request.json
        now = datetime.utcnow()
        payload = {}
        status = 200

        validator = ApplicationValidator(app_attributes)

        if validator.is_valid():
            attrs = validator.attributes
            app = await Application.create(
                name = attrs["name"],
                env_name = attrs["env_name"],
                env_file = attrs["env_file"],
                deployment_script = attrs["deployment_script"],
                created_at = now,
                updated_at = now
            )

            payload = app_to_dict(app)
            status = 201

        else:
            status = 422
            payload = { 'errors': validator.errors }


        return json(payload, status = status)
