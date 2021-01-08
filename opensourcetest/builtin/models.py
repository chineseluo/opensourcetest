#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : opensourcetest
@Time    : 2020/10/23 17:01
@Auth    : chineseluo
@Email   : 848257135@qq.com
@File    : models.py
@IDE     : PyCharm
------------------------------------
"""
from enum import Enum
from pydantic import BaseModel, HttpUrl, Field
from typing import Any, Dict, Text, Union, Callable, List, Tuple, Optional
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

Name = Text
Url = Text
BaseUrl = Union[HttpUrl, Text]
VariablesMapping = Dict[Text, Any]
FunctionsMapping = Dict[Text, Callable]
Headers = Dict[Text, Text]
Cookies = Dict[Text, Text]
Verify = Optional[bool]
checker_item = Union[List, Tuple, Text]


class MethodEnum(Text, Enum):
    """OST Method"""
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"
    PATCH = "PATCH"


class CheckerMethodEnum(Text, Enum):
    """OST Checker Method"""
    GT = "GT"
    GTE = "GTE"
    LT = "LT"
    LTE = "LTE"
    NE = "NE"
    EQ = "EQ"
    CONTAIN = "CONTAIN"


class UiLocateMethodEnum(Text, Enum):
    """OST UI Locate Method"""
    ID = "ID"
    XPATH = "XPATH"
    LINK_TEXT = "LINK_TEXT"
    PARTIAL_LINK_TEXT = "PARTIAL_LINK_TEXT"
    NAME = "NAME"
    TAG_NAME = "TAG_NAME"
    CLASS_NAME = "CLASS_NAME"
    CSS_SELECTOR = "CSS_SELECTOR"


class OSTUiBaseBy(Enum):
    """OST UI Base By"""
    ID = By.ID
    XPATH = By.XPATH
    LINK_TEXT = By.LINK_TEXT
    PARTIAL_LINK_TEXT = By.PARTIAL_LINK_TEXT
    NAME = By.NAME
    TAG_NAME = By.TAG_NAME
    CLASS_NAME = By.CLASS_NAME
    CSS_SELECTOR = By.CSS_SELECTOR


class AppUiLocateMethodEnum(Text, Enum):
    """OST APP Locate Method"""
    ID = "ID"
    XPATH = "XPATH"
    LINK_TEXT = "LINK_TEXT"
    PARTIAL_LINK_TEXT = "PARTIAL_LINK_TEXT"
    NAME = "NAME"
    TAG_NAME = "TAG_NAME"
    CLASS_NAME = "CLASS_NAME"
    CSS_SELECTOR = "CSS_SELECTOR"
    IOS_UIAUTOMATION = "IOS_UIAUTOMATION"
    IOS_PREDICATE = "IOS_PREDICATE"
    IOS_CLASS_CHAIN = "IOS_CLASS_CHAIN"
    ANDROID_UIAUTOMATOR = "ANDROID_UIAUTOMATOR"
    ANDROID_VIEWTAG = "ANDROID_VIEWTAG"
    WINDOWS_UI_AUTOMATION = "WINDOWS_UI_AUTOMATION"
    ACCESSIBILITY_ID = "ACCESSIBILITY_ID"
    IMAGE = "IMAGE"
    CUSTOM = "CUSTOM"


class OSTAppBaseBy(Enum):
    """OST App Base By"""
    ID = By.ID
    XPATH = By.XPATH
    LINK_TEXT = By.LINK_TEXT
    PARTIAL_LINK_TEXT = By.PARTIAL_LINK_TEXT
    NAME = By.NAME
    TAG_NAME = By.TAG_NAME
    CLASS_NAME = By.CLASS_NAME
    CSS_SELECTOR = By.CSS_SELECTOR
    IOS_UIAUTOMATION = MobileBy.IOS_UIAUTOMATION
    IOS_PREDICATE = MobileBy.IOS_PREDICATE
    IOS_CLASS_CHAIN = MobileBy.IOS_CLASS_CHAIN
    ANDROID_UIAUTOMATOR = MobileBy.ANDROID_UIAUTOMATOR
    ANDROID_VIEWTAG = MobileBy.ANDROID_VIEWTAG
    WINDOWS_UI_AUTOMATION = MobileBy.WINDOWS_UI_AUTOMATION
    ACCESSIBILITY_ID = MobileBy.ACCESSIBILITY_ID
    IMAGE = MobileBy.IMAGE
    CUSTOM = MobileBy.CUSTOM


class OSTReqArgv(BaseModel):
    """OST Request httpmodel"""
    method: MethodEnum = MethodEnum.GET
    part_url: Url
    params: Dict[Text, Text] = {}
    req_json: Union[Dict, List, Text] = Field(None, alias="json")
    req_data: Union[Text, Dict[Text, Any]] = Field(None, alias="data")
    headers: Headers = {}
    cookies: Cookies = {}
    upload: Dict = Field({}, alias="files")
    auth: Optional[Tuple[Text]]
    timeout: float = 1200
    allow_redirects: bool = True
    proxies: Dict = None
    verify: Verify = None
    stream: bool = True
    cert: Union[Text, Tuple[Text, Text], None]


# class OSTAddArgv(BaseModel):
#     """OST add custom argv"""
#     params_object: PyObject
#     params_mark: Union[Text, int]
#     checker: Union[List, tuple, Dict[Text, Any], Tuple[Text, Any]]


# class OSTHttpArgv(BaseModel):
#     """OST test case argv"""
#     addArgv: OSTAddArgv
#     originalArgv: OSTReqArgv


class OSTReqData(BaseModel):
    """OST Response.Request Model"""
    method: MethodEnum = MethodEnum.GET
    url: Url
    headers: Headers = {}
    cookies: Cookies = {}
    body: Union[Text, bytes, Dict, List, None] = {}


class OSTRespData(BaseModel):
    """OST Response.Response Model"""
    status_code: int
    headers: Dict
    cookies: Cookies = {}
    encoding: Union[Text, None] = None
    content_type: Text
    body: Union[Dict, Text, bytes]


class OSTReqRespData(BaseModel):
    """OST Response Model"""
    request: OSTReqData
    response: OSTRespData


class Checker(BaseModel):
    """OST Checker"""
    CheckerResource: OSTRespData
    CheckerCondition: Union[Text, int]
    CheckerMethod: CheckerMethodEnum = CheckerMethodEnum.EQ


class Locator(BaseModel):
    """OST locator"""
    method: OSTAppBaseBy
    value: Text
