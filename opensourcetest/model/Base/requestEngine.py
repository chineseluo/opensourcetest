#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : opensourcetest
@Time    : 2020/10/12 11:28
@Auth    : chineseluo
@Email   : 848257135@qq.com
@File    : requestEngine.py
@IDE     : PyCharm
------------------------------------
"""
import logging
import re
from baseRequest import BaseRequest


def check_assertion(res, checker) -> bool:
    check_result = None
    if isinstance(checker, (list, tuple)):
        ...
    elif isinstance(checker, str):
        try:
            assert res == checker
            return True
        except AssertionError:
            logging.error("断言失败，期望值：{}，响应数据：{}".format(checker, res))
            raise AssertionError
    else:
        logging.error("请输入正确的检查器参数，仅支持list or tuple，错误参数为：{}".format(checker))


def url_replace(url, url_converter) -> str:
    replace_url = url
    if isinstance(url_converter, (list, tuple)):
        for item in url_converter:
            replace_url = re.sub("[$]", item, replace_url, count=1)
    elif isinstance(url_converter, str):
        replace_url = url.replace("$", url_converter)
    else:
        logging.error("请输入正确的参数器参数，仅支持list or tuple，错误参数为：{}".format(url_converter))
    return replace_url


def start_run_case(params_object, params_mark, session_connection=None, checker=None, params=None, data=None,
                   json=None, url_converter=None, **kwargs):
    params_obj = params_object()
    params_dict = params_obj.get_param_by_yaml(params_mark)
    req = BaseRequest()
    logging.info(params_dict)
    if session_connection:
        params_dict['header'].update(session_connection)
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
    interface_response = req.send_request(part_url=part_url, method=params_dict['method'].upper(),
                                          send_params=params_dict['params'], send_data=params_dict['data'],
                                          send_json=params_dict['json'], headers=params_dict['headers'], **kwargs)
    if checker:
        check_assertion(interface_response, checker)
    return interface_response


if __name__ == "__main__":
    ...
