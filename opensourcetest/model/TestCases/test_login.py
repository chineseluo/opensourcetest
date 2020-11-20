#!/user/bin/env python
# -*- coding: utf-8 -*-
import allure
import logging
from Base.requestEngine import start_run_case
from Parameter.yamlChoice import Login


@allure.feature("Login")
class TestLogin:

    @allure.severity("blocker")
    @allure.story("Test Login")
    @allure.title("test login")
    def test_login(self):
        headers = {
            "Transfer-Encoding": "chunked"
        }
        result = start_run_case(Login, 0, [("encoding", "utf-8"), ("status_code", "200")])
        logging.info(result)
