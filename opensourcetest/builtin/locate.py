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
from selenium.webdriver.common.by import By


def get_locator(page_elem_dict):
        method = page_elem_dict["data"]["method"]
        value = page_elem_dict["data"]["value"]
        logging.info("元素定位方式为：{}，元素对象值为：{}".format(method, value))
        if method == "ID" and value is not None:
            elem_locator = (By.ID, value)
            return elem_locator
        elif method == "XPATH" and value is not None:
            elem_locator = (By.XPATH, value)
            return elem_locator
        elif method == "LINK_TEXT" and value is not None:
            elem_locator = (By.LINK_TEXT, value)
            return elem_locator
        elif method == "PARTIAL_LINK_TEXT" and value is not None:
            elem_locator = (By.PARTIAL_LINK_TEXT, value)
            return elem_locator
        elif method == "NAME" and value is not None:
            elem_locator = (By.NAME, value)
            return elem_locator
        elif method == "TAG_NAME" and value is not None:
            elem_locator = (By.TAG_NAME, value)
            return elem_locator
        elif method == "CLASS_NAME" and value is not None:
            elem_locator = (By.CLASS_NAME, value)
            logger.error(elem_locator)
            return elem_locator
        elif method == "CSS_SELECTOR" and value is not None:
            elem_locator = (By.CSS_SELECTOR, value)
            return elem_locator
        else:
            logging.error("元素名称：{}，此元素定位方式异常，定位元素值异常，请检查！！！".format(elem_name))
