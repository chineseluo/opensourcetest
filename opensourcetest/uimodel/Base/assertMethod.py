# -*- coding: utf-8 -*-
# !/user/bin/env python
import pytest
import logging
from Common.publicMethod import PubMethod


class AssertMethod:

    @staticmethod
    def assert_equal_screen_shot(driver, exceptor):
        if not isinstance(exceptor, tuple):
            logging.error('exceptor参数类型错误，必须传元祖类型：exceptor=("xx","xx")')
        else:
            try:
                logging.info("正在进行元素断言：断言方式->%s：是否等于->%s" % (exceptor[0], exceptor[1]))
                assert exceptor[0] == exceptor[1]
            except Exception as e:
                logging.error(f"断言执行失败，错误信息为：{e}")
                picture_url = PubMethod.screen_picture(driver)
                raise AssertionError

    @staticmethod
    def assert_gt_screen_shot(driver, exceptor):
        if not isinstance(exceptor, tuple):
            logging.error('exceptor参数类型错误，必须传元祖类型：exceptor=("xx","xx")')
        else:
            try:
                logging.info("正在进行元素断言：断言方式->%s：是否大于->%s" % (exceptor[0], exceptor[1]))
                assert int(exceptor[0]) > int(exceptor[1])
            except Exception as e:
                logging.error(f"断言执行失败，错误信息为：{e}")
                picture_url = PubMethod.screen_picture(driver)
                raise AssertionError

    @staticmethod
    def assert_gte_screen_shot(driver, exceptor):
        if not isinstance(exceptor, tuple):
            logging.error('exceptor参数类型错误，必须传元祖类型：exceptor=("xx","xx")')
        else:
            try:
                logging.info("正在进行元素断言：断言方式->%s：是否大于等于->%s" % (exceptor[0], exceptor[1]))
                assert int(exceptor[0]) >= int(exceptor[1])
            except Exception as e:
                logging.error(f"断言执行失败，错误信息为：{e}")
                picture_url = PubMethod.screen_picture(driver)
                raise AssertionError

    @staticmethod
    def assert_lt_screen_shot(driver, exceptor):
        if not isinstance(exceptor, tuple):
            logging.error('exceptor参数类型错误，必须传元祖类型：exceptor=("xx","xx")')
        else:
            try:
                logging.info("正在进行元素断言：断言方式->%s：是否小于->%s" % (exceptor[0], exceptor[1]))
                assert int(exceptor[0]) < int(exceptor[1])
            except Exception as e:
                logging.error(f"断言执行失败，错误信息为：{e}")
                picture_url = PubMethod.screen_picture(driver)
                raise AssertionError

    @staticmethod
    def assert_lte_screen_shot(driver, exceptor):
        if not isinstance(exceptor, tuple):
            logging.error('exceptor参数类型错误，必须传元祖类型：exceptor=("xx","xx")')
        else:
            try:
                logging.info("正在进行元素断言：断言方式->%s：是否小于等于->%s" % (exceptor[0], exceptor[1]))
                assert int(exceptor[0]) <= int(exceptor[1])
            except Exception as e:
                logging.error(f"断言执行失败，错误信息为：{e}")
                picture_url = PubMethod.screen_picture(driver)
                raise AssertionError

    @staticmethod
    def assert_contain_screen_shot(driver, exceptor):
        if not isinstance(exceptor, tuple):
            logging.error('exceptor参数类型错误，必须传元祖类型：exceptor=("xx","xx")')
        else:
            try:
                logging.info("正在进行元素断言：断言方式->%s：是否包含->%s" % (exceptor[0], exceptor[1]))
                assert exceptor[0] in exceptor[1]
            except Exception as e:
                logging.error(f"断言执行失败，错误信息为：{e}")
                picture_url = PubMethod.screen_picture(driver)
                raise AssertionError

    @staticmethod
    def assert_true_screen_shot(driver, bool_value):
        if not isinstance(bool_value, bool):
            logging.error('bool_value参数类型错误，必须传bool类型：exceptor=Ture/False')
        else:
            try:
                logging.info("正在进行元素断言：断言方式->%s：是否等于True->%s" % bool_value)
                assert True == bool_value
            except Exception as e:
                logging.error(f"断言执行失败，错误信息为：{e}")
                picture_url = PubMethod.screen_picture(driver)
                raise AssertionError

    @staticmethod
    def assert_false_screen_shot(driver, bool_value):
        if not isinstance(bool_value, bool):
            logging.error('bool_value参数类型错误，必须传bool类型：exceptor=Ture/False')
        else:
            try:
                logging.info("正在进行元素断言：断言方式->{}：是否等于False->{}".format(False, bool_value))
                assert False == bool_value
            except Exception as e:
                logging.error(f"断言执行失败，错误信息为：{e}")
                picture_url = PubMethod.screen_picture(driver)
                raise AssertionError
