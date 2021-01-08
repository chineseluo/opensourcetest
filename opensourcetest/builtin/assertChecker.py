#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : OST_HTTP
@Time    : 2020/12/21 14:33
@Auth    : chineseluo
@Email   : 848257135@qq.com
@File    : assertChecker.py
@IDE     : PyCharm
------------------------------------
"""
import logging
from typing import Text
from opensourcetest.interface.assertServer import AssertServer
from opensourcetest.builtin.exceptions import *


class AssertChecker(AssertServer):

    def assert_eq(self, response_value: Text, except_value: Text):
        logging.info(f"Assert EQ<equal>,Expected Value：{except_value},Response Data：{response_value}")
        try:
            assert Text(response_value) == Text(except_value)
        except AssertionError:
            logging.error(f"Assert EQ<equal> Fail,Expected Value：{except_value},Response Data：{response_value}")
            raise AssertEqError

    def assert_gt(self, response_value: int, except_value: int):
        logging.info(f"Assert GT<greater than>,Expected Value：{except_value},Response Data：{response_value}")
        try:
            assert int(response_value) > int(except_value)
        except AssertionError:
            logging.error(f"Assert GT<greater than> Fail,Expected Value：{except_value},Response Data：{response_value}")
            raise AssertGtError

    def assert_gte(self, response_value: int, except_value: int):
        logging.info(f"Assert GTE<gt equeal>,Expected Value：{except_value},Response Data：{response_value}")
        try:
            assert int(response_value) >= int(except_value)
        except AssertionError:
            logging.error(f"Assert GTE<gt equeal> Fail,Expected Value：{except_value},Response Data：{response_value}")
            raise AssertGteError

    def assert_lt(self, response_value: int, except_value: int):
        logging.info(f"Assert LT<less than>,Expected Value：{except_value},Response Data：{response_value}")
        try:
            assert int(response_value) < int(except_value)
        except AssertionError:
            logging.error(f"Assert LT<less than> Fail,Expected Value：{except_value},Response Data：{response_value}")
            raise AssertLtError

    def assert_lte(self, response_value: int, except_value: int):
        logging.info(f"Assert LTE<lt equal>,Expected Value：{except_value},Response Data：{response_value}")
        try:
            assert int(response_value) <= int(except_value)
        except AssertionError:
            logging.error(f"Assert LTE<lt equal> Fail,Expected Value：{except_value},Response Data：{response_value}")
            raise AssertLteError

    def assert_ne(self, response_value: Text, except_value: Text):
        logging.info(f"Assert NE<not equal>,Expected Value：{except_value},Response Data：{response_value}")
        try:
            assert Text(response_value) != Text(except_value)
        except AssertionError:
            logging.error(f"Assert NE<not equal> Fail,Expected Value：{except_value},Response Data：{response_value}")
            raise AssertNeError

    def assert_contain(self, response_value: Text, except_value: Text):
        logging.info(f"Assert CONTAIN<contain>,Expected Value：{except_value},Response Data：{response_value}")
        if except_value in response_value:
            assert True
        else:
            try:
                assert False
            except AssertionError:
                logging.error(
                    f"Assert CONTAIN<contain> Fail,Expected Value：{except_value},Response Data：{response_value}")
                raise AssertContainError
