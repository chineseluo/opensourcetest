#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : opensourcetest
@Time    : 2020/11/23 15:30
@Auth    : chineseluo
@Email   : 848257135
@File    : exceptions.py
@IDE     : PyCharm
------------------------------------
"""
from loguru import logger


class CheckerTypeError(Exception):
     ...


class CheckerArgvError(Exception):
    ...


class AssertEqError(Exception):
    ...


class AssertGtError(Exception):
    ...


class AssertGteError(Exception):
    ...


class AssertLtError(Exception):
    ...


class AssertLteError(Exception):
    ...


class AssertNeError(Exception):
    ...


class AssertContainError(Exception):
    ...


class AssertTrueError(Exception):
    ...


class AssertFalseError(Exception):
    ...


class JsonSplicingError(Exception):
    ...
