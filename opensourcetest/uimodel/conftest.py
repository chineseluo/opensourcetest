# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 9:15
# @Author  : chineseluo
# @Email   : 848257135@qq.com
# @File    : conftest.py
# @Software: PyCharm
import pytest
from opensourcetest.builtin.ostDriver import ost_driver, ost_option, ost_collection_modifyitems


def pytest_addoption(parser):
    ost_option(parser)


def pytest_collection_modifyitems(items):
    """
    定义钩子函数hook进行测试用例name和_nodeid输出
    @param items:
    @return:
    """
    ost_collection_modifyitems(items)


@pytest.fixture(scope="function")
def function_driver(request):
    driver = ost_driver(request)
    yield driver
    driver.quit()


if __name__ == '__main__':
    ...
