#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : interface_auto_frame
@Time    : 2020/8/25 16:10
@Auth    : chineseluo
@Email   : 848257135@qq.com
@File    : run.py
@IDE     : PyCharm
------------------------------------
"""
import os
import pytest

if __name__ == '__main__':
    pytest.main()
    # Generate assure Report
    cmd = 'allure generate Report/allure-results -o Report/allure-report -c'
    os.system(cmd)
