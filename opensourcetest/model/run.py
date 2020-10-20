#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : opensourcetest
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
    # 生成allure报告
    cmd = 'allure generate {} -o {} -c'.format("Report/allure-results", "Report/allure-report")
    os.system(cmd)
