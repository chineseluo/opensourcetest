#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : interface_auto_frame
@Time    : 2020/8/25 16:07
@Auth    : chineseluo
@Email   : 848257135@qq.com
@File    : conftest.py
@IDE     : PyCharm
------------------------------------
"""
import allure
import logging
import pytest
from loguru import logger
from .Parameter.yamlChoice import Login
from .Base.requestEngine import start_run_case


@pytest.fixture()
def function_fixture():
    print("Run before function")
    yield
    print("Run after function")

