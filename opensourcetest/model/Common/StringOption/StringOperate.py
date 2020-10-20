#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : opensourcetest
@Time    : 2020/8/25 16:17
@Auth    : chineseluo
@Email   : 848257135@qq.com
@File    : StringOperate.py
@IDE     : PyCharm
------------------------------------
"""
import hashlib


class String:

    @staticmethod
    def transfer_md5(msg: str):
        """
        对字符串进行md5加密
        :param msg:
        :return:
        """
        hl = hashlib.md5(msg.encode('utf-8'))
        return hl.hexdigest().upper()

