from test_helper import *
import json

@pytest.mark.asyncio
async def test_create_application_record(app):
    reset_db()
    test_cli = app.test_client()

    params = {
        "name": "testapp.com",
        "env_name": "staging",
        "env_file": ".env",
        "deployment_script": "#!/bin/bash\necho Deployed"
    }

    resp = await test_cli.post("/apps", headers={'Content-type': 'application/json'}, data=json.dumps(params))

    body = await resp.json

    assert 201 == resp.status_code
    assert 'application/json' == resp.content_type

    assert body["id"] is not None
    assert body["name"] == params["name"]
    assert body["env_name"] == params["env_name"]

@pytest.mark.asyncio
async def test_validate_required_attributes(app):
    test_cli = app.test_client()

    params = {
        "env_file": ".env",
        "deployment_script": "#!/bin/bash\necho Deployed"
    }

    resp = await test_cli.post("/apps", headers={'Content-type': 'application/json'}, data=json.dumps(params))

    body = await resp.json

    assert 422 == resp.status_code
    assert 'application/json' == resp.content_type

    assert ['not_present'] == body['errors']['name']
    assert ['not_present'] == body['errors']['env_name']

@pytest.mark.asyncio
async def test_validate_name_length(app):
    test_cli = app.test_client()

    params = {
        "name": "test", #less than 5 chars
        "env_name": "staging",
        "env_file": ".env",
        "deployment_script": "#!/bin/bash\necho Deployed"
    }

    resp = await test_cli.post("/apps", headers={'Content-type': 'application/json'}, data=json.dumps(params))

    body = await resp.json

    assert 422 == resp.status_code
    assert 'application/json' == resp.content_type

    assert ['not_valid'] == body['errors']['name']
