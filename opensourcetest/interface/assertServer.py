#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : opensourcetest
@Time    : 2021/1/8 16:53
@Auth    : chineseluo
@Email   : 848257135@qq.com
@File    : assertServer.py
@IDE     : PyCharm
------------------------------------
"""
from typing import Text
from abc import ABCMeta, abstractmethod


class AssertServer(metaclass=ABCMeta):
    @abstractmethod
    def assert_eq(self, response_value: Text, except_value: Text):
        ...

    @abstractmethod
    def assert_gt(self, response_value: int, except_value: int):
        ...

    @abstractmethod
    def assert_gte(self, response_value: int, except_value: int):
        ...

    @abstractmethod
    def assert_lt(self, response_value: int, except_value: int):
        ...

    @abstractmethod
    def assert_lte(self, response_value: int, except_value: int):
        ...

    @abstractmethod
    def assert_ne(self, response_value: Text, except_value: Text):
        ...

    @abstractmethod
    def assert_contain(self, response_value: Text, except_value: Text):
        ...
