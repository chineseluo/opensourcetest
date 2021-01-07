#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : opensourcetest
@Time    : 2020/12/23 15:05
@Auth    : chineseluo
@Email   : 848257135@qq.com
@File    : baseAppRunner.py
@IDE     : PyCharm
------------------------------------
"""
import os
import sys
import logging
import pytest

ROOT_DIR = os.path.dirname(__file__)


def ost_app_runner(mobile_system):
    result_dir = os.path.abspath(f"./Report/{mobile_system}/allure-result")
    # 使用pytest.main
    allure_path_args = ['--alluredir', result_dir, '--clean-alluredir']
    test_args = ['-s', '-q', f'--mobile_system={mobile_system}']
    run_args = test_args + allure_path_args
    pytest.main(run_args)
    # 生成allure报告，需要系统执行命令--clean会清楚以前写入environment.json的配置
    cmd = f'allure generate ./Report/{mobile_system}/allure-result -o ./Report/{mobile_system}/allure-report --clean'
    logging.info("命令行执行cmd:{}".format(cmd))
    try:
        os.system(cmd)
    except Exception as e:
        logging.error('命令【{}】执行失败，错误信息：{}！'.format(cmd, e))
        sys.exit()
    return mobile_system


# 命令行参数调用
def ost_app_cmd_runner():
    global ROOT_DIR
    input_mobile_system = sys.argv
    if len(input_mobile_system) > 1:
        ROOT_DIR = ROOT_DIR.replace("\\", "/")
        if input_mobile_system[1] == "android":
            ost_app_runner("android")
        elif input_mobile_system[1] == "ios":
            ost_app_runner("ios")
        else:
            logging.error("Parameter error, please re-enter！！！")
    else:
        ost_app_runner("android")
