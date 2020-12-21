#!/user/bin/env python
# -*- coding: utf-8 -*-
import pytest
from Parameter.yamlChoice import Login
from Base.requestEngine import start_run_case


@pytest.fixture(scope="session")
def token():
    params = {"username": "zouzou", "password": "zouzou"}
    result = start_run_case(Login, 0, ("status_code", 200, "GTE"), json=params)
    auth = {
        "Authorization": f'JWT {result["body"]["data"]["token"]}'
    }
    yield auth


