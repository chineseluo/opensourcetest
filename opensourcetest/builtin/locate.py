#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : opensourcetest_release_test
@Time    : 2020/11/24 11:38
@Auth    : chineseluo
@Email   : 848257135@qq.com
@File    : locate.py
@IDE     : PyCharm
------------------------------------
"""
import logging
from loguru import logger
from opensourcetest.builtin.models import UiLocateMethodEnum, OSTUiBaseBy


def get_locator(page_elem_dict):
        method = page_elem_dict["data"]["method"]
        value = page_elem_dict["data"]["value"]
        logging.info(f"The element positioning mode is：{method},The element object value is:{value}")
        if method == UiLocateMethodEnum.ID and value is not None:
            elem_locator = (OSTUiBaseBy.ID, value)
            return elem_locator
        elif method == UiLocateMethodEnum.XPATH and value is not None:
            elem_locator = (OSTUiBaseBy.XPATH, value)
            return elem_locator
        elif method == UiLocateMethodEnum.LINK_TEXT and value is not None:
            elem_locator = (OSTUiBaseBy.LINK_TEXT, value)
            return elem_locator
        elif method == UiLocateMethodEnum.PARTIAL_LINK_TEXT and value is not None:
            elem_locator = (OSTUiBaseBy.PARTIAL_LINK_TEXT, value)
            return elem_locator
        elif method == UiLocateMethodEnum.NAME and value is not None:
            elem_locator = (OSTUiBaseBy.NAME, value)
            return elem_locator
        elif method == UiLocateMethodEnum.TAG_NAME and value is not None:
            elem_locator = (OSTUiBaseBy.TAG_NAME, value)
            return elem_locator
        elif method == UiLocateMethodEnum.CLASS_NAME and value is not None:
            elem_locator = (OSTUiBaseBy.CLASS_NAME, value)
            logger.error(elem_locator)
            return elem_locator
        elif method == UiLocateMethodEnum.CSS_SELECTOR and value is not None:
            elem_locator = (OSTUiBaseBy.CSS_SELECTOR, value)
            return elem_locator
        else:
            logging.error("This element positioning method is abnormal, positioning element value is abnormal, "
                          "please check!!!")
