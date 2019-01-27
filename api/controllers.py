import json
from quart.views import MethodView
from quart import request
from datetime import datetime
from .models import Application
from .helpers import app_to_dict, apps_to_dict
from .validators import ApplicationValidator

class Applications(MethodView):
    async def get(self):
        apps = await Application.query.gino.all()

        return json.dumps(apps_to_dict(apps))

    async def post(self):
        app_attributes = await request.json
        now = datetime.utcnow()
        payload = {}
        status = 200

        validator = ApplicationValidator(app_attributes)

        if validator.is_valid():
            attrs = validator.attributes
            app = await Application.create(
                name = attrs["name"],
                env_name = attrs["env_name"],
                env_file = attrs.get("env_file"),
                deployment_script = attrs.get("deployment_script"),
                created_at = now,
                updated_at = now
            )

            payload = app_to_dict(app)
            status = 201

        else:
            status = 422
            payload = { 'errors': validator.errors }


        return json.dumps(payload), status
