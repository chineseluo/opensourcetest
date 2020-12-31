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
    if method == UiLocateMethodEnum.ID.value and value is not None:
        elem_locator = (OSTUiBaseBy.ID.value, value)
        return elem_locator
    elif method == UiLocateMethodEnum.XPATH.value and value is not None:
        elem_locator = (OSTUiBaseBy.XPATH.value, value)
        return elem_locator
    elif method == UiLocateMethodEnum.LINK_TEXT.value and value is not None:
        elem_locator = (OSTUiBaseBy.LINK_TEXT.value, value)
        return elem_locator
    elif method == UiLocateMethodEnum.PARTIAL_LINK_TEXT.value and value is not None:
        elem_locator = (OSTUiBaseBy.PARTIAL_LINK_TEXT.value, value)
        return elem_locator
    elif method == UiLocateMethodEnum.NAME.value and value is not None:
        elem_locator = (OSTUiBaseBy.NAME.value, value)
        return elem_locator
    elif method == UiLocateMethodEnum.TAG_NAME.value and value is not None:
        elem_locator = (OSTUiBaseBy.TAG_NAME.value, value)
        return elem_locator
    elif method == UiLocateMethodEnum.CLASS_NAME.value and value is not None:
        elem_locator = (OSTUiBaseBy.CLASS_NAME.value, value)
        return elem_locator
    elif method == UiLocateMethodEnum.CSS_SELECTOR.value and value is not None:
        elem_locator = (OSTUiBaseBy.CSS_SELECTOR.value, value)
        return elem_locator
    else:
        logging.error("This element positioning method is abnormal, positioning element value is abnormal, "
                      "please check!!!")


def get_locator(page_elem_dict):
    method = page_elem_dict["data"]["method"]
    value = page_elem_dict["data"]["value"]
    logging.info(f"The element positioning mode is：{method},The element object value is:{value}")
    if method == AppUiLocateMethodEnum.ID.value and value is not None:
        elem_locator = (OSTAppBaseBy.ID.value, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.XPATH.value and value is not None:
        elem_locator = (OSTAppBaseBy.XPATH.value, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.LINK_TEXT.value and value is not None:
        elem_locator = (OSTAppBaseBy.LINK_TEXT.value, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.PARTIAL_LINK_TEXT.value and value is not None:
        elem_locator = (OSTAppBaseBy.PARTIAL_LINK_TEXT.value, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.NAME.value and value is not None:
        elem_locator = (OSTAppBaseBy.NAME.value, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.TAG_NAME.value and value is not None:
        elem_locator = (OSTAppBaseBy.TAG_NAME.value, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.CLASS_NAME.value and value is not None:
        elem_locator = (OSTAppBaseBy.CLASS_NAME.value, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.CSS_SELECTOR.value and value is not None:
        elem_locator = (OSTAppBaseBy.CSS_SELECTOR.value, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.IOS_UIAUTOMATION.value and value is not None:
        elem_locator = (OSTAppBaseBy.IOS_UIAUTOMATION.value, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.IOS_PREDICATE.value and value is not None:
        elem_locator = (OSTAppBaseBy.IOS_PREDICATE.value, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.IOS_CLASS_CHAIN.value and value is not None:
        elem_locator = (OSTAppBaseBy.IOS_CLASS_CHAIN.value, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.ANDROID_UIAUTOMATOR.value and value is not None:
        elem_locator = (OSTAppBaseBy.ANDROID_UIAUTOMATOR.value, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.ANDROID_VIEWTAG.value and value is not None:
        elem_locator = (OSTAppBaseBy.ANDROID_VIEWTAG.value, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.WINDOWS_UI_AUTOMATION.value and value is not None:
        elem_locator = (OSTAppBaseBy.WINDOWS_UI_AUTOMATION.value, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.ACCESSIBILITY_ID.value and value is not None:
        elem_locator = (OSTAppBaseBy.ACCESSIBILITY_ID.value, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.IMAGE.value and value is not None:
        elem_locator = (OSTAppBaseBy.IMAGE.value, value)
        return elem_locator
    elif method == AppUiLocateMethodEnum.CUSTOM.value and value is not None:
        elem_locator = (OSTAppBaseBy.CUSTOM.value, value)
        return elem_locator
    else:
        logging.error("This element positioning method is abnormal, positioning element value is abnormal, "
                      "please check!!!")
