# coding:utf-8
import pytest
import allure
from Base.assertMethod import AssertMethod


@allure.feature("Register_page_case")
class Test_RegisterPageCase:

    @allure.story("Register")
    @allure.severity("normal")
    @allure.description("测试登录")
    @allure.link("https://www.baidu.com", name="连接跳转百度")
    @allure.testcase("https://www.sina.com", name="测试用例位置")
    @allure.title("执行测试用例用于登录模块")
    def test_DLZC7(self, login_page_class_load, register_page_class_load, function_driver):
        login_page_class_load.login_by_config_url()
        login_page_class_load.click_register_btn()
        username_input_attribute_value = register_page_class_load.get_username_attribute_value()
        AssertMethod.assert_equal_screen_shot(function_driver, (username_input_attribute_value, "手机号码"))

    # @allure.story("Register")
    # @allure.severity("normal")
    # @allure.description("测试登录")
    # @allure.link("https://www.baidu.com", name="连接跳转百度")
    # @allure.testcase("https://www.sina.com", name="测试用例位置")
    # @allure.title("执行测试用例用于登录模块")
    # def test_DLZC8(self, login_page_class_load, register_page_class_load, function_driver):
    #     login_page_class_load.login_by_config_url()
    #     login_page_class_load.click_register_btn()
    #     register_page_class_load.click_other_register_btn()
    #     res = register_page_class_load.check_page_is_other_page()
    #     AssertMethod.assert_false_screen_shot(function_driver, res)
    #
    # @allure.story("Register")
    # @allure.severity("normal")
    # @allure.description("测试登录")
    # @allure.link("https://www.baidu.com", name="连接跳转百度")
    # @allure.testcase("https://www.sina.com", name="测试用例位置")
    # @allure.title("执行测试用例用于登录模块")
    # def test_DLZC9(self, login_page_class_load, register_page_class_load, function_driver):
    #     login_page_class_load.login_by_config_url()
    #     login_page_class_load.click_register_btn()
    #     register_page_class_load.click_login_btn()
    #     login_title = register_page_class_load.get_login_page_title()
    #     AssertMethod.assert_equal_screen_shot(function_driver, (login_title, "登录"))
    #
    # @allure.story("Register")
    # @allure.severity("normal")
    # @allure.description("测试登录")
    # @allure.link("https://www.baidu.com", name="连接跳转百度")
    # @allure.testcase("https://www.sina.com", name="测试用例位置")
    # @allure.title("执行测试用例用于登录模块")
    # def test_DLZC10(self, login_page_class_load, register_page_class_load, function_driver):
    #     login_page_class_load.login_by_config_url()
    #     login_page_class_load.click_register_btn()
    #     register_page_class_load.click_register_btn()
    #     error_text = register_page_class_load.get_error_text()
    #     AssertMethod.assert_equal_screen_shot(function_driver, (error_text, "登录"))
    #
    # @allure.story("Register")
    # @allure.severity("normal")
    # @allure.description("测试登录")
    # @allure.link("https://www.baidu.com", name="连接跳转百度")
    # @allure.testcase("https://www.sina.com", name="测试用例位置")
    # @allure.title("执行测试用例用于登录模块")
    # def test_DLZC11(self, login_page_class_load, register_page_class_load, function_driver):
    #     login_page_class_load.login_by_config_url()
    #     login_page_class_load.click_register_btn()
    #     register_page_class_load.click_code_btn()
    #     error_text = register_page_class_load.get_error_text()
    #     AssertMethod.assert_equal_screen_shot(function_driver, (error_text, "用户名不能为空"))
    #
    # @allure.story("Register")
    # @allure.severity("normal")
    # @allure.description("测试登录")
    # @allure.link("https://www.baidu.com", name="连接跳转百度")
    # @allure.testcase("https://www.sina.com", name="测试用例位置")
    # @allure.title("执行测试用例用于登录模块")
    # def test_DLZC12(self, login_page_class_load, register_page_class_load, function_driver):
    #     login_page_class_load.login_by_config_url()
    #     login_page_class_load.click_register_btn()
    #     register_page_class_load.username_send_keys(1)
    #     register_page_class_load.click_register_btn()
    #     error_text = register_page_class_load.get_error_text()
    #     AssertMethod.assert_equal_screen_shot(function_driver, (error_text, "手机号码格式不正确"))


if __name__ == '__main__':
    pytest.main(["Test_RegisterPageCase.py"])
