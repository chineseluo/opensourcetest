# !/user/bin/env python
# -*- coding: utf-8 -*-
import pytest
import allure
import inspect
import logging
import time
from Base.assertMethod import AssertMethod


@allure.feature("Login_page_case")
class TestLoginPageCase:

    @allure.story("Login")
    @allure.severity("normal")
    @allure.description("测试登录")
    @allure.link("https://www.baidu.com", name="连接跳转百度")
    @allure.testcase("https://www.sina.com", name="测试用例位置")
    @allure.title("执行测试用例用于登录模块")
    def test_DLZC1(self, login_page_class_load, function_driver):
        logging.info("Case number code:{}".format(inspect.stack()[0][3]))
        login_page_class_load.login_by_config_url()
        username_input_attribute_value = login_page_class_load.get_username_attribute_value()
        AssertMethod.assert_equal_screen_shot(function_driver, (username_input_attribute_value, "手机号码"))


if __name__ == "__main__":
    pytest.main(["TestLoginPageCase.py"])
