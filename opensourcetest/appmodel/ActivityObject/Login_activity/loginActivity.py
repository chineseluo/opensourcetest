# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 21:11
# @Author  : chineseluo
# @Email   : 848257135@qq.com
# @File    : run.py
# @Software: PyCharm
from Base.base import Base
from selenium import webdriver
from ActivityObject.elemParams import LoginActivityElem


# 封装车联网app登录页面操作对象操作方法
class LoginActivity(Base):
    def __init__(self, driver):
        # 初始化页面元素对象，即yaml文件对象
        self.elem_locator = LoginActivityElem()
        # 初始化driver
        super().__init__(driver)

    def input_phone(self, value):
        elem = self.elem_locator.get_locator("phone_number")
        super().send_key(elem, value)

    def input_code(self, value):
        elem = self.elem_locator.get_locator("code")
        super().send_key(elem, value)

    def click_login_btn(self):
        elem = self.elem_locator.get_locator("login_btn")
        super().click_btn(elem)

    def get_message_value(self):
        elem = self.elem_locator.get_locator("message_id")
        return super().get_text(elem)


if __name__ == "__main__":
    home_activity = LoginActivity(webdriver.Chrome())
