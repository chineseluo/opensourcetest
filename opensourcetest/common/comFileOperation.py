#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : opensourcetest
@Time    : 2020/8/25 16:38
@Auth    : chineseluo
@Email   : 848257135@qq.com
@File    : comFileOperation.py
@IDE     : PyCharm
------------------------------------
"""
import os


def get_roots_dirs_files_list(dir_path):
    """
    Get the root path, folder and file under the current folder
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
