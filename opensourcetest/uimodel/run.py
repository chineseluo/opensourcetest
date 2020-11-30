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

root_dir = os.path.dirname(__file__)


# 运行命令参数配置
def run_all_case(browser, browser_opt, type_driver):
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
    cmd = 'allure generate ./Report/{}/allure-result -o ./Report/{}/allure-report --clean'.format(
        browser.replace(" ", "_"),
        browser.replace(" ", "_"))
    logger.info("命令行执行cmd:{}".format(cmd))
    try:
        os.system(cmd)
    except Exception as e:
        logging.error('命令【{}】执行失败！'.format(cmd))
        sys.exit()
    # 打印url，方便直接访问
    url = '本地报告链接：http://127.0.0.1:63342/{}/Report/{}/allure-report/index.html'.format(root_dir.split('/')[-1],
                                                                                       browser.replace(" ", "_"))
    logger.info(url)


# 命令行参数运行
def receive_cmd_arg(root_dir):
    # global root_dir
    input_browser = sys.argv
    if len(input_browser) > 1:
        root_dir = root_dir.replace("\\", "/")
        if input_browser[1] == "chrome":
            run_all_case(input_browser[1], input_browser[2], input_browser[3])
        elif input_browser[1] == "firefox":
            run_all_case(input_browser[1], input_browser[2], input_browser[3])
        elif input_browser[1] == "ie":
            run_all_case("ie", input_browser[2], input_browser[3])
        else:
            logging.error("参数错误，请重新输入！！！")
    else:
        run_all_case("chrome", "close", "local")


if __name__ == "__main__":
    receive_cmd_arg(root_dir)

