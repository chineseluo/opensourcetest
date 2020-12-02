# !/user/bin/env python
# -*- coding: utf-8 -*-
import pytest
from PageObject.loginPage import LoginPage


@pytest.fixture(scope="function")
def login_page_class_load(function_driver):
    """
    注入登录页面对象
    @param function_driver:
    @return:
    """
    login_page = LoginPage(function_driver)
    yield login_page


