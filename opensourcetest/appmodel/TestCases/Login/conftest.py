# -*- coding: utf-8 -*-
import pytest
from ActivityObject.Login_activity.loginActivity import LoginActivity


@pytest.fixture(scope="function")
def login_activity_class_load(function_driver):
    login_activity = LoginActivity(function_driver)
    yield login_activity


