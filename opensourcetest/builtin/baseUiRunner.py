# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 21:11
# @Author  : chineseluo
# @Email   : 848257135@qq.com
# @File    : run.py
# @Software: PyCharm
import os
import sys
import logging
import pytest
from loguru import logger

ROOT_DIR = os.path.dirname(__file__)


# 运行命令参数配置
def ost_ui_runner(browser, browser_opt, type_driver):
    """
    @param browser:传入浏览器，chrome/firefox/ie
    @param browser_opt: 浏览器操作，是否开启浏览器操作窗口，关闭操作窗口效率更高，open or close
    @param type_driver:驱动类型，是本地driver还是远程driver，local or remote
    @return:
    """
    # 测试结果文件存放目录
    result_dir = os.path.abspath("./Report/{}/allure-result".format(browser))
    # 测试报告文件存放目录
    report_dir = os.path.abspath("./Report/{}/allure-report".format(browser))
    allure_path_args = ['--alluredir', result_dir, '--clean-alluredir']
    test_args = ['-s', '-q', '--browser={}'.format(browser), '--browser_opt={}'.format(browser_opt),
                 '--type_driver={}'.format(type_driver)]
    # 拼接运行参数
    run_args = test_args + allure_path_args
    # 使用pytest.main
    pytest.main(run_args)
    # 生成allure报告，需要系统执行命令--clean会清楚以前写入environment.json的配置
    cmd = f'allure generate ./Report/{browser.replace(" ", "_")}/allure-result -o ./Report/{browser.replace(" ", "_")}/allure-report --clean'
    logger.info("命令行执行cmd:{}".format(cmd))
    try:
        os.system(cmd)
    except Exception as e:
        logging.error('命令【{}】执行失败！'.format(cmd))
        sys.exit()
    # 打印url，方便直接访问
    return browser


# 命令行参数运行
def ost_ui_cmd_runner():
    global ROOT_DIR
    input_browser = sys.argv
    if len(input_browser) > 1:
        ROOT_DIR = ROOT_DIR.replace("\\", "/")
        if input_browser[1] == "chrome":
            ost_ui_runner(input_browser[1], input_browser[2], input_browser[3])
            return input_browser[1]
        elif input_browser[1] == "firefox":
            ost_ui_runner(input_browser[1], input_browser[2], input_browser[3])
            return input_browser[1]
        elif input_browser[1] == "ie":
            ost_ui_runner("ie", input_browser[2], input_browser[3])
            return input_browser[1]
        else:
            logging.error("Parameter error, please re-enter！！！")
            sys.exit(0)
    else:
        ost_ui_runner("chrome", "close", "local")
        return "chrome"


if __name__ == "__main__":
    print(os.getcwd())
