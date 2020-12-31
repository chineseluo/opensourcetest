# !/user/bin/env python
# -*- coding: utf-8 -*-
from opensourcetest.builtin.autoParamInjection import AutoInjection


# 注册yaml文件对象
class LoginActivityElem(AutoInjection):
    def __init__(self):
        super(LoginActivityElem, self).__init__('Login_activity', 'Login_activity')


if __name__ == '__main__':
    login_activity = LoginActivityElem()
    print(login_activity.get_elem_locator("phone_number"))
