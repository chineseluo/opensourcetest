# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 21:11
# @Author  : chineseluo
# @Email   : 848257135@qq.com
# @File    : run.py
# @Software: PyCharm

from opensourcetest.builtin.autoParamInjection import AutoInjection


# 注册yaml文件对象
class LoginPageElem(AutoInjection):
    def __init__(self):
        super(LoginPageElem, self).__init__('Login_page', 'Login_page')


class BuyPageElem(AutoInjection):
    def __init__(self):
        super(BuyPageElem, self).__init__('Buy_page', 'Buy_page')


class RegisterPageElem(AutoInjection):
    def __init__(self):
        super(RegisterPageElem, self).__init__('Register_page', 'Register_page')


if __name__ == '__main__':
    login_page = LoginPageElem()
