#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : opensourcetest
@Time    : 2020/8/25 16:38
@Auth    : chineseluo
@Email   : 848257135@qq.com
@File    : comFileOption.py
@IDE     : PyCharm
------------------------------------
"""
import os


def get_roots_dirs_files_list(dir_path):
    """
    获取当前文件夹下的根路径，文件夹，文件
    :param dir_path:
    :return:
    """
    roots = []
    dirs = []
    files = []
    for r, d, f in os.walk(dir_path):
        roots.append(r)
        dirs.append(d)
        files.append(f)
    return roots, dirs, files
