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
from loguru import logger
from typing import Text, List, Tuple, Dict, Union
from opensourcetest.builtin.exceptions import JsonSplicingError


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
            replace_url = re.sub("[$]", Text(item), replace_url, count=1)
    elif isinstance(Text(url_converter), Text):
        replace_url = url.replace("$", Text(url_converter))
    else:
        logging.error(f"Please enter the correct checker parameters, only supported list or tuple,The error parameter "
                      f"is:{url_converter}")
    return replace_url


def ost_http_argv_update(param_custom: Union[List, Dict], ost_yaml_param_type: Text, params_dict: List):
    """
    ost http yaml data splicing
    :param ost_yaml_param_type:
    :param params_dict:
    :param param_custom:
    :return:
    """

    logging.debug("Start to splice JSON parameters.")
    if isinstance(param_custom[0], (Tuple, Dict)):
        logging.debug("Start multi-layer JSON parameter splicing.")
        for item in param_custom:
            if isinstance(item, Tuple):
                interface_yaml_locator = f'params_dict["{ost_yaml_param_type}"]' + Text(item[0])
                if isinstance(eval(interface_yaml_locator), Dict):
                    eval(interface_yaml_locator).update(item[1])
                elif isinstance(eval(interface_yaml_locator), List):
                    eval(interface_yaml_locator).append(item[1])
                else:
                    logging.error("Interface request JSON parameter internal assembly failed, please check!!!")
                    raise JsonSplicingError
            elif isinstance(item, Dict):
                interface_yaml_locator = f'params_dict["{ost_yaml_param_type}"]'
                eval(interface_yaml_locator).update(item)
    elif isinstance(param_custom[0], Text) and isinstance(param_custom[1], (Dict, List)):
        logging.debug("Start single layer JSON parameter splicing.")
        interface_yaml_locator = f'params_dict["{ost_yaml_param_type}"]' + Text(param_custom[0])
        if isinstance(eval(interface_yaml_locator), Dict):
            eval(interface_yaml_locator).update(param_custom[1])
        elif isinstance(eval(interface_yaml_locator), List):
            eval(interface_yaml_locator).append(param_custom[1])
        else:
            logging.error("Interface request JSON parameter internal assembly failed, please check!!!")
            raise JsonSplicingError
