#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : opensourcetest
@Time    : 2020/12/21 17:07
@Auth    : chineseluo
@Email   : 848257135@qq.com
@File    : ostHttp.py
@IDE     : PyCharm
------------------------------------
"""
import os
import jmespath
import logging
from loguru import logger
from typing import Text, Union, Dict, List
from opensourcetest.common.urlOperation import url_replace
from opensourcetest.builtin.check import check_assertion
from opensourcetest.builtin.models import OSTReqRespData, OSTReqArgv
from opensourcetest.builtin.baseRequest import BaseRequest
from opensourcetest.common.urlOperation import ost_http_argv_update


def ost_http_runner(params_object, params_mark: Union[Text, int], checker=None, session_connection=None, params=None,
                   data=None, json=None, files=None, url_converter=None, base_url=None, verify=None, **kwargs) -> OSTReqRespData:
    # Inject yaml request object
    params_obj = params_object()
    params_dict = params_obj.get_param_by_yaml(params_mark)
    req = BaseRequest()
    logging.info(f'Corresponding to yaml interface: {params_dict}')
    # Injection request data
    if session_connection:
        params_dict['headers'].update(session_connection)
    if url_converter:
        part_url = url_replace(params_dict['url'], url_converter)
    else:
        part_url = params_dict['url']
    if params:
        params_dict['params'].update(params)
    if data:
        params_dict['data'].update(data)
    if json:
        if isinstance(json, tuple):
            ost_http_argv_update(json, "json", params_dict)
        elif isinstance(json, list):
            params_dict['json'] = json
        else:
            params_dict['json'].update(json)
    if files:
        params_dict['files'].update(files)
    # receive a request and response object
    ost_req_argv = OSTReqArgv(
        part_url=part_url,
        method=params_dict['method'].upper(),
        params=params_dict['params'],
        data=params_dict['data'],
        json=params_dict['json'],
        headers=params_dict['headers'],
        files=params_dict['files'],
        **kwargs
    )
    logging.debug(ost_req_argv)

    ost_req_resp = req.send_request(url=base_url + part_url, method=params_dict['method'].upper(),
                                    send_params=params_dict['params'], send_data=params_dict['data'],
                                    send_json=params_dict['json'], headers=params_dict['headers'], files=params_dict['files'], verify=verify,
                                    **kwargs)
    if checker:
        # According to jmespath_rule and contrast value are used to judge, which needs to support multiple judgments
        check_assertion(ost_req_resp.response, checker)
    return ost_req_resp
