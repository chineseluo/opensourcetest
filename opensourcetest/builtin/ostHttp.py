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
import urllib
import time
from loguru import logger
from typing import Text, Union, Dict, List
from opensourcetest.common.urlOperation import url_replace
from opensourcetest.builtin.check import check_assertion
from opensourcetest.builtin.models import OSTReqRespData, OSTReqArgv
from opensourcetest.builtin.baseRequest import BaseRequest
from opensourcetest.common.urlOperation import ost_http_argv_update


def ost_http_runner(params_object, params_mark: Union[Text, int], checker=None, session_connection=None, params=None,
                    data=None, json=None, files=None, url_converter=None, url_quote_save=None, base_url=None,
                    verify=None, ost_timeout=None, ost_poll_frequency=None, **kwargs) -> OSTReqRespData:
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
        if isinstance(data, Dict):
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
        data=data,
        json=params_dict['json'],
        headers=params_dict['headers'],
        files=params_dict['files'],
        **kwargs
    )
    logging.debug(ost_req_argv)
    if ost_timeout and ost_poll_frequency and checker:
        if not ost_timeout:
            logging.error("使用接口重试模式缺少ost_timeout超时时间配置...请检查！")
            raise Exception
        if not ost_poll_frequency:
            logging.error("使用接口重试模式缺少ost_poll_frequency时间间隔配置...请检查！")
            raise Exception
        if not checker:
            logging.error("使用接口重试模式缺少checker断言器配置...请检查！")
            raise Exception
        end_time = time.monotonic() + ost_timeout
        retry_index = 1
        while True:
            try:
                logging.info(f"开始第{retry_index}次重试去获取接口期望的断言")
                value = req.send_request(url=base_url + part_url, method=params_dict['method'].upper(),
                                        send_params=params_dict[
                                            "params"] if not url_quote_save else urllib.parse.urlencode(
                                            params_dict["params"], quote_via=urllib.parse.quote,
                                            safe=f"{url_quote_save}"),
                                        send_data=params_dict['data'] if isinstance(data, Dict) else data,
                                        send_json=params_dict['json'], headers=params_dict['headers'],
                                        files=params_dict['files'], verify=verify,
                                        **kwargs)
                try:
                    check_assertion(value.response, checker)
                    return value
                except Exception as e:
                    logging.warning(f"第{retry_index}次重试去获取接口期望的断言失败，error message:{e}")
            except Exception as e:
                logging.error(e)
            time.sleep(ost_poll_frequency)
            if time.monotonic() > end_time:
                break
            retry_index += 1
        raise Exception
    else:
        ost_req_resp = req.send_request(url=base_url + part_url, method=params_dict['method'].upper(),
                                        send_params=params_dict[
                                            "params"] if not url_quote_save else urllib.parse.urlencode(
                                            params_dict["params"], quote_via=urllib.parse.quote,
                                            safe=f"{url_quote_save}"),
                                        send_data=params_dict['data'] if isinstance(data, Dict) else data,
                                        send_json=params_dict['json'], headers=params_dict['headers'],
                                        files=params_dict['files'], verify=verify,
                                        **kwargs)
        if checker:
            # According to jmespath_rule and contrast value are used to judge, which needs to support multiple judgments
            check_assertion(ost_req_resp.response, checker)
    return ost_req_resp


def until(method, ost_timeout=None, ost_poll_frequency=None, checker=None):
    if not ost_timeout:
        logging.error("使用接口重试模式缺少ost_timeout超时时间配置...请检查！")
        raise Exception
    if not ost_poll_frequency:
        logging.error("使用接口重试模式缺少ost_poll_frequency时间间隔配置...请检查！")
        raise Exception
    if not checker:
        logging.error("使用接口重试模式缺少checker断言器配置...请检查！")
        raise Exception
    end_time = time.monotonic() + ost_timeout
    retry_index = 1
    while True:
        try:
            logging.info(f"开始第{retry_index}次重试去获取接口期望的断言")
            value = method(*argv)
            try:
                check_assertion(value.response, checker)
                return value
            except Exception as e:
                logging.warning(f"第{retry_index}次重试去获取接口期望的断言失败，error message:{e}")
        except Exception as e:
            logging.error(e)
        time.sleep(ost_poll_frequency)
        if time.monotonic() > end_time:
            break
        retry_index += 1
    raise Exception("获取期望断言响应超时！！！")
