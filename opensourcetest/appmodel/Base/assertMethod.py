# -*- coding: utf-8 -*-
# !/user/bin/env python
# @Time    : 2020/6/1 16:45
# @Author  : chineseluo
# @Email   : l848257135@qq.com
# @File    : assertMethod.py
# @Software: PyCharm
import logging
from Common.publicMethod import PubMethod


class AssertMethod:

    @staticmethod
    def assert_equal_screen_shot(driver, exceptor):
        if not isinstance(exceptor, tuple):
            logging.error('exceptor参数类型错误，必须传元祖类型：exceptor=("xx","xx")')
        else:
            logging.info("正在进行元素断言：断言方式:{}是否等于{}".format(exceptor[0], exceptor[1]))
            try:
                assert exceptor[0] == exceptor[1]
            except Exception as e:
                logging.error("断言执行失败，错误信息为：{}".format(e))
                picture_url = PubMethod.screen_picture(driver)
                raise e

    @staticmethod
    def assert_gt_screen_shot(driver, exceptor):
        if not isinstance(exceptor, tuple):
            logging.error('exceptor参数类型错误，必须传元祖类型：exceptor=("xx","xx")')
        else:
            logging.info("正在进行元素断言：断言方式->%s：是否大于->%s" % (exceptor[0], exceptor[1]))
            try:
                assert int(exceptor[0]) > int(exceptor[1])
            except Exception as e:
                logging.error("断言执行失败，错误信息为：{}".format(e))
                picture_url = PubMethod.screen_picture(driver)
                raise e

    @staticmethod
    def assert_gte_screen_shot(driver, exceptor):
        if not isinstance(exceptor, tuple):
            logging.error('exceptor参数类型错误，必须传元祖类型：exceptor=("xx","xx")')
        else:
            logging.info("正在进行元素断言：断言方式->%s：是否大于等于->%s" % (exceptor[0], exceptor[1]))
            try:
                assert int(exceptor[0]) >= int(exceptor[1])
            except Exception as e:
                logging.error("断言执行失败，错误信息为：{}".format(e))
                picture_url = PubMethod.screen_picture(driver)
                raise e

    @staticmethod
    def assert_lt_screen_shot(driver, exceptor):
        if not isinstance(exceptor, tuple):
            logging.error('exceptor参数类型错误，必须传元祖类型：exceptor=("xx","xx")')
        else:
            logging.info("正在进行元素断言：断言方式->%s：是否小于->%s" % (exceptor[0], exceptor[1]))
            try:
                assert int(exceptor[0]) < int(exceptor[1])
            except Exception as e:
                logging.error("断言执行失败，错误信息为：{}".format(e))
                picture_url = PubMethod.screen_picture(driver)
                raise e

    @staticmethod
    def assert_lte_screen_shot(driver, exceptor):
        if not isinstance(exceptor, tuple):
            logging.error('exceptor参数类型错误，必须传元祖类型：exceptor=("xx","xx")')
        else:
            logging.info("正在进行元素断言：断言方式->%s：是否小于等于->%s" % (exceptor[0], exceptor[1]))
            try:
                assert int(exceptor[0]) <= int(exceptor[1])
            except Exception as e:
                logging.error("断言执行失败，错误信息为：{}".format(e))
                picture_url = PubMethod.screen_picture(driver)
                raise e

    @staticmethod
    def assert_contain_screen_shot(driver, exceptor):
        if not isinstance(exceptor, tuple):
            logging.error('exceptor参数类型错误，必须传元祖类型：exceptor=("xx","xx")')
        else:
            logging.info("正在进行元素断言：断言方式->%s：是否包含->%s" % (exceptor[0], exceptor[1]))
            try:
                assert exceptor[0] in exceptor[1]
            except Exception as e:
                logging.error("断言执行失败，错误信息为：{}".format(e))
                picture_url = PubMethod.screen_picture(driver)
                raise e

    @staticmethod
    def assert_true_screen_shot(driver, bool_value):
        if not isinstance(bool_value, bool):
            logging.error('bool_value参数类型错误，必须传bool类型：exceptor=Ture/False')
        else:
            logging.info("正在进行元素断言：断言方式->%s：是否等于True" % bool_value)
            try:
                assert True == bool_value
            except Exception as e:
                logging.error("断言执行失败，错误信息为：{}".format(e))
                picture_url = PubMethod.screen_picture(driver)
                raise e

    @staticmethod
    def assert_false_screen_shot(driver, bool_value):
        if not isinstance(bool_value, bool):
            logging.error('bool_value参数类型错误，必须传bool类型：exceptor=Ture/False')
        else:
            logging.info("正在进行元素断言：断言方式->{}：是否等于False->{}".format(False, bool_value))
            try:
                assert False == bool_value
            except Exception as e:
                logging.error("断言执行失败，错误信息为：{}".format(e))
                picture_url = PubMethod.screen_picture(driver)
                raise e

    @staticmethod
    def assert_arg_in_list(driver, exceptor):
        if not isinstance(exceptor[1], list):
            logging.error("断言传递参数错误：{}".format(exceptor[1]))
        else:
            logging.info("正在进行元素断言：断言方式->{}：是否位于列表->{}中".format(exceptor[0], exceptor[1]))
            try:
                assert exceptor[0] in exceptor[1]
            except Exception as e:
                logging.error("断言执行失败，错误信息为：{}".format(e))
                picture_url = PubMethod.screen_picture(driver)
                raise e

