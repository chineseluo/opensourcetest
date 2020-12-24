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
from opensourcetest.builtin.models import UiLocateMethodEnum, OSTUiBaseBy, AppUiLocateMethodEnum, OSTAppBaseBy


def get_ui_locator(page_elem_dict):
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


def get_locator(page_elem_dict):
    method = page_elem_dict["data"]["method"]
    value = page_elem_dict["data"]["value"]
    logging.info(f"The element positioning mode is：{method},The element object value is:{value}")
    if method == AppUiLocateMethodEnum.ID and value is not None:
        elem_locator = (OSTAppBaseBy.ID, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.XPATH and value is not None:
        elem_locator = (OSTAppBaseBy.XPATH, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.LINK_TEXT and value is not None:
        elem_locator = (OSTAppBaseBy.LINK_TEXT, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.PARTIAL_LINK_TEXT and value is not None:
        elem_locator = (OSTAppBaseBy.PARTIAL_LINK_TEXT, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.NAME and value is not None:
        elem_locator = (OSTAppBaseBy.NAME, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.TAG_NAME and value is not None:
        elem_locator = (OSTAppBaseBy.TAG_NAME, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.CLASS_NAME and value is not None:
        elem_locator = (OSTAppBaseBy.CLASS_NAME, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.CSS_SELECTOR and value is not None:
        elem_locator = (OSTAppBaseBy.CSS_SELECTOR, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.IOS_UIAUTOMATION and value is not None:
        elem_locator = (OSTAppBaseBy.IOS_UIAUTOMATION, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.IOS_PREDICATE and value is not None:
        elem_locator = (OSTAppBaseBy.IOS_PREDICATE, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.IOS_CLASS_CHAIN and value is not None:
        elem_locator = (OSTAppBaseBy.IOS_CLASS_CHAIN, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.ANDROID_UIAUTOMATOR and value is not None:
        elem_locator = (OSTAppBaseBy.ANDROID_UIAUTOMATOR, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.ANDROID_VIEWTAG and value is not None:
        elem_locator = (OSTAppBaseBy.ANDROID_VIEWTAG, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.WINDOWS_UI_AUTOMATION and value is not None:
        elem_locator = (OSTAppBaseBy.WINDOWS_UI_AUTOMATION, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.ACCESSIBILITY_ID and value is not None:
        elem_locator = (OSTAppBaseBy.ACCESSIBILITY_ID, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.IMAGE and value is not None:
        elem_locator = (OSTAppBaseBy.IMAGE, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.CUSTOM and value is not None:
        elem_locator = (OSTAppBaseBy.CUSTOM, value)
        return elem_locator
    else:
        logging.error("This element positioning method is abnormal, positioning element value is abnormal, "
                          "please check!!!")