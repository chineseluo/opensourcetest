#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : interface_auto_frame
@Time    : 2020/10/23 18:06
@Auth    : chineseluo
@Email   : 848257135@qq.com
@File    : consolelog.py
@IDE     : PyCharm
------------------------------------
"""
import json
from loguru import logger


def log_output(ost_model, ost_type):
    """
    Only used in console for request response model log output beautification
    :param ost_model: OST request or response model
    :param ost_type:OST type(request or response)
    :return:
    """
    msg = f"\n================== {ost_type} details ==================\n"
    for key, value in ost_model.dict().items():
        if isinstance(value, dict):
            value = json.dumps(value, indent=4)

        msg += "{:<8} : {}\n".format(key, value)
    logger.debug(msg)


class OSTConsoleLog(object):
    pass
