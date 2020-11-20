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
from pydantic import BaseModel, HttpUrl, Field, PyObject
from opensourcetest.builtin.autoParamInjection import AutoInjection
from typing import Any, Dict, Text, Union, Callable, List, Tuple, Optional

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


class OSTReqArgv(BaseModel):
    """OST Request model"""
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
