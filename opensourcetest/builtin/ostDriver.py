#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : opensourcetest
@Time    : 2020/11/30 15:40
@Auth    : chineseluo
@Email   : 848257135@qq.com
@File    : ostDriver.py
@IDE     : PyCharm
------------------------------------
"""
import os
import pytest
import logging
from loguru import logger
from selenium import webdriver
from selenium.webdriver import Remote
from opensourcetest.common.fileOperation import FileOption
from selenium.webdriver.chrome.options import Options as CO
from selenium.webdriver.firefox.options import Options as FO
from selenium.webdriver.ie.options import Options as IEO
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile as FP


def ost_collection_modifyitems(items):
    """
    定义钩子函数hook进行测试用例name和_nodeid输出
    @param items:
    @return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        logging.info(item.name)
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode_escape")
        logging.info(item._nodeid)


def ost_option(parser):
    """
        定义钩子函数hook进行命令行定义浏览器传参，默认chrome,定义浏览器启动方式传参，默认启动
        @param parser:
        @return:
    """
    # Browser options
    parser.addoption("--browser", action="store", default="chrome", help="browser option: firefox or chrome or ie")
    # Do you want to turn on browser interface options
    parser.addoption("--browser_opt", action="store", default="open", help="browser GUI open or close")
    # driver options,Local or remote mode
    parser.addoption("--type_driver", action="store", default="local", help="type of driver: local or remote")


def ost_driver(request):
    """
    driver注入
    @param request:
    @return:
    """
    browser = request.config.getoption("--browser")
    # It is used to set whether or not to open the browser for local startup,browser_opt judge，default:open
    browser_opt = request.config.getoption("--browser_opt")
    logging.info(f'Get command line parameters:{request.config.getoption("--browser")}')
    type_driver = request.config.getoption("--type_driver")
    # Determine whether it is distributed locally or remotely
    if type_driver == "local":
        if browser_opt == "open":
            if browser == "chrome":
                # Skip non secure HTTPS security verification
                chrome_options = CO()
                chrome_options.add_argument("--ignore-certificate-errors")
                driver = webdriver.Chrome(chrome_options=chrome_options)
            elif browser == "firefox":
                # Skip non secure HTTPS security verification
                profile = FP()
                profile.accept_untrusted_certs = True
                driver = webdriver.Firefox(firefox_profile=profile)
            elif browser == "ie":
                # Skip non secure HTTPS security verification
                driver = webdriver.Ie()
            else:
                logging.info(f"Bad browser parameters:{browser}")
        else:
            if browser == "chrome":
                # Do not open the browser window, run the test code in the background
                chrome_options = CO()
                chrome_options.add_argument('--headless')
                # Skip non secure HTTPS security verification
                chrome_options.add_argument('--ignore-certificate-errors')
                driver = webdriver.Chrome(chrome_options=chrome_options)
            elif browser == "firefox":
                # Do not open the browser window, run the test code in the background
                firefox_options = FO()
                firefox_options.add_argument('--headless')
                # Skip non secure HTTPS security verification
                profile = FP()
                profile.accept_untrusted_certs = True
                driver = webdriver.Firefox(firefox_options=firefox_options, firefox_profile=profile)
            elif browser == "ie":
                # Do not open the browser window, run the test code in the background
                ie_options = IEO()
                ie_options.add_argument('--headless')
                # Skip non secure HTTPS security verification
                driver = webdriver.Ie(ie_options=ie_options)
            else:
                logging.info(f"Received incorrect browser parameters:{browser}")
        return driver
    elif type_driver == "remote":
        # Read selenium distributed configuration file
        selenium_config_path = os.path.join(os.getcwd(), "Conf", "config.yaml")
        selenium_config = FileOption.read_yaml(selenium_config_path)
        driver = Remote(command_executor=selenium_config["selenium_config"]["selenium_hub_url"],
                        desired_capabilities={'platform': 'ANY', 'browserName': browser, 'version': '',
                                              'javascriptEnabled': True})
        return driver
    else:
        logging.error(f"driver parameter transfer error, please check the parameter:{type_driver}")


if __name__ == "__main__":
    selenium_config_path = os.path.join(os.path.dirname(__file__), "Conf", "selenium_config.yaml")
    logger.info(selenium_config_path)
