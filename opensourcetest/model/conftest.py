#!/user/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(scope="session")
def function_fixture():
    print("Run before function")
    yield
    print("Run after function")


