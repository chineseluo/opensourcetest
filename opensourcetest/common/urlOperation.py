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
from typing import Text, List, Tuple


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
