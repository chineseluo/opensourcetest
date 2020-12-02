#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : opensourcetest_release_test
@Time    : 2020/11/25 16:10
@Auth    : chineseluo
@Email   : 848257135@qq.com
@File    : stringOperation.py
@IDE     : PyCharm
------------------------------------
"""
import string
import random


def random_string(strings=string.ascii_letters, length=15):
    """
    Get random string
    @param strings:
    @param length:
    @return:
    """
    values = ''.join(random.choices(strings, k=length))
    return values
