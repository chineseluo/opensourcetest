# !/user/bin/env python
# -*- coding: utf-8 -*-
import pytest
import logging
from opensourcetest.common.pictureOperation import screen_picture
from opensourcetest.builtin.exceptions import *


class AssertScreenShot:

    @staticmethod
    def assert_equal_screen_shot(driver, expector):
        if not isinstance(expector, tuple):
            logging.error('Expector parameter type error, must pass ancestor type:expector=("xx","xx")')
        else:
            try:
                logging.info(f"Element assertion in progress:Is {expector[0]} equal to {expector[1]}?")
                assert expector[0] == expector[1]
            except Exception as e:
                logging.error(f"Assertion execution failed with error message:{e}")
                picture_url = screen_picture(driver)
                raise AssertEqError

    @staticmethod
    def assert_gt_screen_shot(driver, expector):
        if not isinstance(expector, tuple):
            logging.error('Expector parameter type error, must pass ancestor type:expector=("xx","xx")')
        else:
            try:
                logging.info(f"Element assertion in progress:Is {expector[0]} greater than {expector[1]}?")
                assert int(expector[0]) > int(expector[1])
            except Exception as e:
                logging.error(f"Assertion execution failed with error message:{e}")
                picture_url = screen_picture(driver)
                raise AssertGtError

    @staticmethod
    def assert_gte_screen_shot(driver, expector):
        if not isinstance(expector, tuple):
            logging.error('Expector parameter type error, must pass ancestor type:expector=("xx","xx")')
        else:
            try:
                logging.info(f"Element assertion in progress:Is {expector[0]} greater than or equal to {expector[1]}?")
                assert int(expector[0]) >= int(expector[1])
            except Exception as e:
                logging.error(f"Assertion execution failed with error message:{e}")
                picture_url = screen_picture(driver)
                raise AssertGteError

    @staticmethod
    def assert_lt_screen_shot(driver, expector):
        if not isinstance(expector, tuple):
            logging.error('Expector parameter type error, must pass ancestor type:expector=("xx","xx")')
        else:
            try:
                logging.info(f"Element assertion in progress:Is {expector[0]} less than {expector[1]}?")
                assert int(expector[0]) < int(expector[1])
            except Exception as e:
                logging.error(f"Assertion execution failed with error message:{e}")
                picture_url = screen_picture(driver)
                raise AssertLtError

    @staticmethod
    def assert_lte_screen_shot(driver, expector):
        if not isinstance(expector, tuple):
            logging.error('Expector parameter type error, must pass ancestor type:expector=("xx","xx")')
        else:
            try:
                logging.info(f"Element assertion in progress:Is {expector[0]} less than or equal to {expector[1]}?")
                assert int(expector[0]) <= int(expector[1])
            except Exception as e:
                logging.error(f"Assertion execution failed with error message:{e}")
                picture_url = screen_picture(driver)
                raise AssertLteError

    @staticmethod
    def assert_contain_screen_shot(driver, expector):
        if not isinstance(expector, tuple):
            logging.error('Expector parameter type error, must pass ancestor type:expector=("xx","xx")')
        else:
            try:
                logging.info(f"Element assertion in progress:Is {expector[0]} contain to {expector[1]}?")
                assert expector[0] in expector[1]
            except Exception as e:
                logging.error(f"Assertion execution failed with error message:{e}")
                picture_url = screen_picture(driver)
                raise AssertContainError

    @staticmethod
    def assert_true_screen_shot(driver, bool_value):
        if not isinstance(bool_value, bool):
            logging.error('bool_value parameter type error, must pass bool type:bool_value=Ture/False')
        else:
            try:
                logging.info(f"Element assertion in progress:Is {bool_value} equal to True")
                assert bool_value
            except Exception as e:
                logging.error(f"Assertion execution failed with error message:{e}")
                picture_url = screen_picture(driver)
                raise AssertTrueError

    @staticmethod
    def assert_false_screen_shot(driver, bool_value):
        if not isinstance(bool_value, bool):
            logging.error('bool_value parameter type error, must pass bool type:bool_value=Ture/False')
        else:
            try:
                logging.info(f"Element assertion in progress:Is {bool_value} equal to False")
                assert not bool_value
            except Exception as e:
                logging.error(f"Assertion execution failed with error message:{e}")
                picture_url = screen_picture(driver)
                raise AssertFalseError
