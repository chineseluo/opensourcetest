#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : opensourcetest
@Time    : 2020/11/20 15:20
@Auth    : chineseluo
@Email   : 848257135@qq.com
@File    : check.py
@IDE     : PyCharm
------------------------------------
"""
import logging
import jmespath
from loguru import logger
from typing import List, Tuple, Text, Dict
from opensourcetest.builtin.exceptions import CheckerTypeError, CheckerArgvError
from opensourcetest.builtin.models import CheckerMethodEnum
from opensourcetest.builtin.assertChecker import AssertChecker


def ost_assertion(extract_resp, assert_item):
    if assert_item[2].upper() == CheckerMethodEnum.EQ:
        AssertChecker().assert_eq(extract_resp, assert_item[1])
    elif assert_item[2].upper() == CheckerMethodEnum.GT:
        AssertChecker().assert_gt(extract_resp, assert_item[1])
    elif assert_item[2].upper() == CheckerMethodEnum.GTE:
        AssertChecker().assert_gte(extract_resp, assert_item[1])
    elif assert_item[2].upper() == CheckerMethodEnum.LT:
        AssertChecker().assert_lt(extract_resp, assert_item[1])
    elif assert_item[2].upper() == CheckerMethodEnum.LTE:
        AssertChecker().assert_lte(extract_resp, assert_item[1])
    elif assert_item[2].upper() == CheckerMethodEnum.NE:
        AssertChecker().assert_ne(extract_resp, assert_item[1])
    elif assert_item[2].upper() == CheckerMethodEnum.CONTAIN:
        AssertChecker().assert_contain(extract_resp, assert_item[1])
    else:
        logging.error("The assertion judged that the condition parameter was passed in error!")
        raise CheckerArgvError


def check_assertion(res, checker):
    """
    The data is extracted according to the objects passed in by the checker. The checker may be a nested list or tuple, add gt gte lt lte ne eq in
    :param res:
    :param checker:
    :return:
    """
    if isinstance(checker, (int, Dict, Text)):
        logging.error("Inspector parameter type error")
        raise CheckerTypeError
    if isinstance(checker[0], (List, Tuple)):
        for assert_item in checker:
            extract_resp = jmespath.search(assert_item[0], res.dict())
            if assert_item[1] is not None:
                if len(assert_item) == 2:
                    AssertChecker().assert_eq(extract_resp, assert_item[1])
                elif len(assert_item) == 3:
                    ost_assertion(extract_resp, assert_item)
                else:
                    logging.warning("You passed too many unrecognized parameters!")
            else:
                logging.error(f"Assert Fail,Get Assert Object Fail：{assert_item}")
                raise AssertionError
    elif isinstance(checker[0], Text):
        extract_resp = jmespath.search(checker[0], res.dict())
        if len(checker) == 2:
            AssertChecker().assert_eq(extract_resp, checker[1])
        elif len(checker) == 3:
            ost_assertion(extract_resp, checker)
        else:
            logging.warning("You passed too many unrecognized parameters!")
            raise CheckerTypeError
    else:
        logging.error(f"Please enter the correct checker parameters, only supported list or tuple，The error parameter "
                      f"is：{checker}")
