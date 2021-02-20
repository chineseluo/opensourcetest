# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 22:53
# @Author  : chineseluo
# @Email   : 848257135@qq.com
# @File    : conftest.py
# @Software: PyCharm

import pytest
from PageObject.loginPage import LoginPage
from PageObject.registerPage import RegisterPage


@pytest.fixture(scope="function")
def login_page_class_load(function_driver):
    """
    注入等页面对象
    @param function_driver:
    @return:
    """
    login_page = LoginPage(function_driver)
    yield login_page


@pytest.fixture(scope="function")
def register_page_class_load(function_driver):
    """
    注入注册页面对象
    @param function_driver:
    @return:
    """
    register_page = RegisterPage(function_driver)
    yield register_page



