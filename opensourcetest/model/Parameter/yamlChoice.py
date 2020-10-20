#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : interface_auto_frame
@Time    : 2020/10/12 16:30
@Auth    : chineseluo
@Email   : 848257135@qq.com
@File    : yamlChoice.py
@IDE     : PyCharm
------------------------------------
"""
from opensourcetest.builtin.autoParamInjection import AutoInjection


class Login(AutoInjection):
    def __init__(self):
        super(Login, self).__init__(self.__class__.__name__)


if __name__ == '__main__':
    t = Login()
    print(t.interface_info)
