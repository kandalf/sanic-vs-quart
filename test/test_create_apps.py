from test_helper import *
import json

async def test_create_application_record(test_cli):
    reset_db()

    params = {
        "name": "testapp.com",
        "env_name": "staging",
        "env_file": ".env",
        "deployment_script": "#!/bin/bash\necho Deployed"
    }

    resp = await test_cli.post("/apps", headers={'Content-type': 'application/json'}, data=json.dumps(params))

    body = await resp.json()

    assert 201 == resp.status
    assert 'application/json' == resp.content_type

    assert body["id"] is not None
    assert body["name"] == params["name"]
    assert body["env_name"] == params["env_name"]

async def test_validate_required_attributes(test_cli):
    params = {
        "env_file": ".env",
        "deployment_script": "#!/bin/bash\necho Deployed"
    }

    resp = await test_cli.post("/apps", headers={'Content-type': 'application/json'}, data=json.dumps(params))

    body = await resp.json()

    assert 422 == resp.status
    assert 'application/json' == resp.content_type

    assert ['not_present'] == body['errors']['name']
    assert ['not_present'] == body['errors']['env_name']

async def test_validate_name_length(test_cli):
    params = {
        "name": "test", #less than 5 chars
        "env_name": "staging",
        "env_file": ".env",
        "deployment_script": "#!/bin/bash\necho Deployed"
    }

    resp = await test_cli.post("/apps", headers={'Content-type': 'application/json'}, data=json.dumps(params))

    body = await resp.json()

    assert 422 == resp.status
    assert 'application/json' == resp.content_type

    assert ['not_valid'] == body['errors']['name']
