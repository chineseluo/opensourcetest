#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : interface_auto_frame
@Time    : 2020/10/12 11:28
@Auth    : chineseluo
@Email   : 848257135@qq.com
@File    : requestEngine.py
@IDE     : PyCharm
------------------------------------
"""
from loguru import logger
import logging
import re
from typing import Text, List, Dict, Tuple
import jmespath
from opensourcetest.models.models import OSTReqRespData, OSTReqArgv
from .baseRequest import BaseRequest


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
                    assert extract_resp == assert_item[1]
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


def url_replace(url: Text, url_converter) -> Text:
    """
    Used to convert the & parameter in the URL
    :param url:
    :param url_converter:
    :return:
    """
    replace_url = url
    if isinstance(url_converter, (List, Tuple)):
        for item in url_converter:
            replace_url = re.sub("[$]", item, replace_url, count=1)
    elif isinstance(url_converter, Text):
        replace_url = url.replace("$", url_converter)
    else:
        logging.error(f"Please enter the correct checker parameters, only supported list or tuple,The error parameter "
                      f"is:{url_converter}")
    return replace_url


def start_run_case(params_object, params_mark, checker=None, session_connection=None, params=None, data=None,
                   json=None, files=None, url_converter=None, **kwargs) -> OSTReqRespData:
    # 注入请求对象
    params_obj = params_object()
    params_dict = params_obj.get_param_by_yaml(params_mark)
    req = BaseRequest()
    logging.info(params_dict)
    # 注入请求数据
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
        **kwargs
    )
    logging.info(ost_req_argv)
    ost_req_resp = req.send_request(part_url=part_url, method=params_dict['method'].upper(),
                                    send_params=None, send_data=params_dict['data'],
                                    send_json=params_dict['json'], headers=params_dict['headers'], **kwargs)
    if checker:
        # According to jmespath_rule and contrast value are used to judge, which needs to support multiple judgments
        check_assertion(ost_req_resp.response, checker)
    return ost_req_resp


if __name__ == "__main__":
    ...
