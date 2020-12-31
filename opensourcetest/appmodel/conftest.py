# !/user/bin/env python
# -*- coding: utf-8 -*-
import os
import pytest
import logging
from appium import webdriver
from Common.fileOperation import FileOption
from opensourcetest.builtin.ostDriver import ost_driver, ost_option, ost_collection_modifyitems

appium_config_path = os.path.join(os.path.dirname(__file__), "Conf", "config.yaml")
appium_config = FileOption.read_yaml(appium_config_path)["appium_config"]


def pytest_collection_modifyitems(items):
    """
    定义钩子函数hook进行测试用例name和_nodeid输出
    """
    ost_collection_modifyitems(items)


# 定义钩子函数hook实现ios和android系统测试切换
def pytest_addoption(parser):
    parser.addoption("--mobile_system", action="store", default="android", help="choose system version, android or ios")


@pytest.fixture(scope="function")
def function_driver(request):
    desired_caps = {
        'platformName': appium_config['platformName'],
        'deviceName': appium_config['deviceName'],
        'platformVersion': appium_config['platformVersion'],
        'appPackage': appium_config['appPackage'],
        'appActivity': appium_config['appActivity'],
        'unicodeKeyboard': appium_config['unicodeKeyboard'],
        'resetKeyboard': appium_config['resetKeyboard']
    }
    driver = webdriver.Remote(appium_config["remote_URL"], desired_caps)
    yield driver
    logging.info("driver.quit:Clean up driver process！！！")
    driver.quit()


if __name__ == '__main__':
    ...
