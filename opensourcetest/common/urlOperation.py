#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : opensourcetest
@Time    : 2020/11/20 16:12
@Auth    : chineseluo
@Email   : 848257135@qq.com
@File    : urlOperation.py
@IDE     : PyCharm
------------------------------------
"""
import re
import logging
from typing import Text, List, Tuple, Dict, Union


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
    elif isinstance(Text(url_converter), Text):
        replace_url = url.replace("$", Text(url_converter))
    else:
        logging.error(f"Please enter the correct checker parameters, only supported list or tuple,The error parameter "
                      f"is:{url_converter}")
    return replace_url


def ost_http_argv_update(param_type_custom: Union[List, Dict], ost_exception: Exception):
    """
    ost http yaml data splicing
    :param param_type_custom:
    :param ost_exception: ost custom exception
    :return:
    """
    if isinstance(param_type_custom[0], tuple):
        for item in param_type_custom:
            interface_yaml_locator = 'params_dict' + Text(item[0])
            if isinstance(item[1], Dict):
                eval(interface_yaml_locator).update(item[1])
            elif isinstance(item[1], List):
                eval(interface_yaml_locator).append(item[1])
            else:
                raise ost_exception
    elif isinstance(param_type_custom[0], Text):
        interface_yaml_locator = 'params_dict' + Text(param_type_custom[0])
        if isinstance(param_type_custom[1], Dict):
            eval(interface_yaml_locator).update(param_type_custom[1])
        elif isinstance(param_type_custom[1], List):
            eval(interface_yaml_locator).append(param_type_custom[1])
        else:
            raise ost_exception
