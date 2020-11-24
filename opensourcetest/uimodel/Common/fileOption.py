# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 21:11
# @Author  : chineseluo
# @Email   : 848257135@qq.com
# @File    : run.py
# @Software: PyCharm
import os


class FileOption:
    @staticmethod
    def file_mkdir(file_path):
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        else:
            print("{}目录已存在，不需要再次创建".format(file_path))

