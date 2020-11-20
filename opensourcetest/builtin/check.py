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
from typing import List, Tuple, Text


def check_assertion(res, checker):
    """
    The data is extracted according to the objects passed in by the checker. The checker may be a nested list or tuple
    :param res:
    :param checker:
    :return:
    """

    if isinstance(checker[0], (List, Tuple)):
        for assert_item in checker:
            extract_resp = jmespath.search(assert_item[0], res.dict())
            if assert_item[1] is not None:
                try:
                    assert Text(extract_resp) == Text(assert_item[1])
                except AssertionError:
                    logging.error(f"Assert Fail,Expected Value：{assert_item[1]},Response Data：{extract_resp}")
                    raise AssertionError
            else:
                logging.error(f"Assert Fail,Get Assert Object Fail：{assert_item}")
                raise AssertionError
    elif isinstance(checker[0], Text):
        extract_resp = jmespath.search(checker[0], res.dict())
        try:
            assert extract_resp == checker[1]
        except AssertionError:
            logging.error(f"Assert Fail,Expected Value：{checker[1]}，response data：{extract_resp}")
            raise AssertionError
    else:
        logging.error(f"Please enter the correct checker parameters, only supported list or tuple，The error parameter "
                      f"is：{checker}")
