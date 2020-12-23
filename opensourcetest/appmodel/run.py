# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 21:11
# @Author  : chineseluo
# @Email   : 848257135@qq.com
# @File    : run.py
# @Software: PyCharm
import os
import sys
import json
import logging
import pytest
from Common.publicMethod import PubMethod

root_dir = os.path.dirname(__file__)
config_yaml = PubMethod.read_yaml("./Conf/config.yaml")


def modify_report_environment_file(report_widgets_dir):
    """
    向environment.json文件添加测试环境配置，展现在allure测试报告中
    @return:
    """
    environment_info = [
        {"name": '测试地址', "values": [config_yaml['allure_environment']['URL']]},
        {"name": '测试版本号', "values": [config_yaml['allure_environment']["version"]]},
        {"name": '测试账户', "values": [config_yaml['allure_environment']['username']]},
        {"name": '测试说明', "values": [config_yaml['allure_environment']['description']]}
    ]
    # 确保目录存在
    PubMethod.create_dirs(os.path.join(report_widgets_dir, 'widgets'))
    with open('./Report/allure-results/widgets/environment.json', 'w', encoding='utf-8') as f:
        json.dump(environment_info, f, ensure_ascii=False, indent=4)


def run_all_case(mobile_system):
    report_widgets_dir = os.path.abspath("./Report/allure-results")
    # 使用pytest.main
    pytest.main()
    # 生成allure报告，需要系统执行命令--clean会清楚以前写入environment.json的配置
    cmd = 'allure generate ./Report/{} -o ./Report/{}/allure-results --clean'.format(mobile_system.replace(" ", "_"),
                                                                                     mobile_system.replace(" ", "_"))
    logging.info("命令行执行cmd:{}".format(cmd))
    try:
        os.system(cmd)
    except Exception as e:
        logging.error('命令【{}】执行失败，错误信息：{}！'.format(cmd, e))
        sys.exit()
    # 定义allure报告环境信息
    modify_report_environment_file(report_widgets_dir)
    # 打印url，方便直接访问
    url = '报告链接：http://127.0.0.1:63342/{}/Report/{}/allure-results/index.html'.format(root_dir.split('/')[-1],
                                                                                      mobile_system.replace(" ", "_"))
    print(url)


# 命令行参数调用
def receive_cmd_arg():
    global root_dir
    input_mobile_system = sys.argv
    if len(input_mobile_system) > 1:
        root_dir = root_dir.replace("\\", "/")
        if input_mobile_system[1] == "android":
            run_all_case("android")
        elif input_mobile_system[1] == "ios":
            run_all_case("ios")
        else:
            logging.error("参数错误，请重新输入！！！")
    else:
        run_all_case("android")


if __name__ == "__main__":
    receive_cmd_arg()
