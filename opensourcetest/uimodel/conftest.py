# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 9:15
# @Author  : chineseluo
# @Email   : 848257135@qq.com
# @File    : conftest.py
# @Software: PyCharm
import os
import pytest
import logging
from selenium import webdriver
from selenium.webdriver import Remote
from Common.publicMethod import PubMethod
from selenium.webdriver.chrome.options import Options as CO
from selenium.webdriver.firefox.options import Options as FO
from selenium.webdriver.ie.options import Options as IEO
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile as FP




def pytest_addoption(parser):
    """
    定义钩子函数hook进行命令行定义浏览器传参，默认chrome,定义浏览器启动方式传参，默认启动
    @param parser:
    @return:
    """
    # 浏览器选项
    parser.addoption("--browser", action="store", default="chrome", help="browser option: firefox or chrome or ie")
    # 是否开启浏览器界面选项
    parser.addoption("--browser_opt", action="store", default="open", help="browser GUI open or close")
    # driver选项，本地还是远程模式
    parser.addoption("--type_driver", action="store", default="local", help="type of driver: local or remote")


def pytest_collection_modifyitems(items):
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


@pytest.fixture(scope="function")
def function_driver(request):
    """
    driver注入
    @param request:
    @return:
    """
    browser = request.config.getoption("--browser")
    # 用于本地启动是否开启浏览器设置，根据命令行传参，browser_opt判断，默认open
    browser_opt = request.config.getoption("--browser_opt")
    print("获取命令行传参：{}".format(request.config.getoption("--browser")))
    type_driver = request.config.getoption("--type_driver")
    # 判断是本地还是远程
    if type_driver == "local":
        if browser_opt == "open":
            if browser == "chrome":
                # 跳过非安全的https安全校验
                chrome_options = CO()
                chrome_options.add_argument("--ignore-certificate-errors")
                driver = webdriver.Chrome(chrome_options=chrome_options)
            elif browser == "firefox":
                # 跳过非安全的https安全校验
                profile = FP()
                profile.accept_untrusted_certs = True
                driver = webdriver.Firefox(firefox_profile=profile)
            elif browser == "ie":
                # 跳过非安全的https安全校验，通过base里面封装的skip_ie_https_check方法跳过
                driver = webdriver.Ie()
            else:
                logging.info("发送错误浏览器参数：{}".format(browser))
        else:
            if browser == "chrome":
                # 不开启浏览器窗口，后台运行测试代码
                chrome_options = CO()
                chrome_options.add_argument('--headless')
                # 跳过非安全的https安全校验
                chrome_options.add_argument('--ignore-certificate-errors')
                driver = webdriver.Chrome(chrome_options=chrome_options)
            elif browser == "firefox":
                # 不开启浏览器窗口，后台运行测试代码
                firefox_options = FO()
                firefox_options.add_argument('--headless')
                # 跳过非安全的https安全校验
                profile = FP()
                profile.accept_untrusted_certs = True
                driver = webdriver.Firefox(firefox_options=firefox_options, firefox_profile=profile)
            elif browser == "ie":
                # 不开启浏览器窗口，后台运行测试代码
                ie_options = IEO()
                ie_options.add_argument('--headless')
                # 跳过非安全的https安全校验
                driver = webdriver.Ie(ie_options=ie_options)
            else:
                logging.info("发送错误浏览器参数：{}".format(browser))
        yield driver
        # driver.close()
        driver.quit()
    elif type_driver == "remote":
        # 读取selenium分布式配置文件
        selenium_config_path = os.path.join(os.path.dirname(__file__), "Conf", "selenium_config.yaml")
        selenium_config = PubMethod.read_yaml(selenium_config_path)
        driver = Remote(command_executor=selenium_config["selenium_config"]["selenium_hub_url"],
                        desired_capabilities={'platform': 'ANY', 'browserName': browser, 'version': '',
                                              'javascriptEnabled': True})
        yield driver
        # driver.close()
        driver.quit()
    else:
        logging.error("driver参数传递错误，请检查参数：{}".format(type_driver))


if __name__ == '__main__':
    ...
