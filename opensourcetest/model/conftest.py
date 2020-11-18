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
import pytest


@pytest.fixture(scope="session")
def function_fixture():
    print("Run before function")
    yield
    print("Run after function")


