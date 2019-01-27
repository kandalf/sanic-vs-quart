from test_helper import *
from api.models import Application
import asyncio

@pytest.mark.asyncio
@pytest.mark.skip(reason="Skipping due to loop errors")
async def test_list_applications(app):
    reset_db()
    test_cli = app.test_client()

    await asyncio.gather(Application.create(name="App1", env_name="staging"),
    Application.create(name="App1", env_name="production"),
    Application.create(name="App2", env_name="staging"),
    Application.create(name="App2", env_name="production"))

    resp = await test_cli.get("/apps", headers={"Content-type": "application/json"})

    body = await resp.json

    assert 200 == resp.status_code
    assert "application/json" == resp.content_type

    assert len(body) == 4

    for app in body:
        assert app["id"] is not None
        assert app["name"] in ["App1", "App2"]
        assert app["env_name"] in ["staging", "production"]
