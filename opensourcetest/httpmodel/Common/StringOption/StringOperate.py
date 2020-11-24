#!/user/bin/env python
# -*- coding: utf-8 -*-
import hashlib


class String:

    @staticmethod
    def transfer_md5(msg: str):
        """
        MD5 encryption of string
        :param msg:
        :return:
        """
        hl = hashlib.md5(msg.encode('utf-8'))
        return hl.hexdigest().upper()

