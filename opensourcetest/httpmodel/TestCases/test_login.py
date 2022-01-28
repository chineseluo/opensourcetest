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
    @pytest.mark.parametrize("username,password", [("zouzou", "zouzou"), ("zouzou1", "zouzou1")])
    def test_login(self, username, password):
        params = {"username": username, "password": password}
        result = start_run_case(Login, 0, ("status_code", 200, "GTE"), json=params)
        auth = {
            "Authorization": f'JWT {result["body"]["data"]["token"]}'
        }
        logging.info(auth)

    @allure.severity("blocker")
    @allure.story("Test get")
    @allure.title("test get")
    def test_get(self, token):
        params = {
            "page": 1,
            "size": 20
        }
        start_run_case(Login, "查询", session_connection=token, params=params)

    @allure.severity("blocker")
    @allure.story("Test delete")
    @allure.title("test delete")
    def test_delete(self, token):
        start_run_case(Login, "删除", session_connection=token, url_converter="58")
