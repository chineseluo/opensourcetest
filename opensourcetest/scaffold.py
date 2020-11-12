#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : opensourcetest
@Time    : 2020/10/13 14:19
@Auth    : 848257135
@Email   : 848257135@qq.com
@File    : scaffold.py
@IDE     : PyCharm
------------------------------------
"""
import os
import shutil
import loguru as logger


def create_scaffold(project_name):
    """create scaffold with specified project name.
    """
    if os.path.isdir(project_name):
        logger.warning(f"Project folder {project_name} exists, please specify a new project name.")
        return 1
    elif os.path.isfile(project_name):
        logger.warning(f"Project name {project_name} conflicts with existed file, please specify a new one.")
        return 1

    logger.info(f"OpenSourceTest start creating new project: {project_name}")
    logger.info(f"Project Root Dir: {os.path.join(os.getcwd(), project_name)}\n")

    def create_folder(path):
        os.makedirs(path)
        logger.info(msg=f"created folder:{path}")

    def copy_allfiles(target_path):
        source_path = "../model"
        if not os.path.exists(target_path):  # If the destination directory does not exist, the directory is created
            os.makedirs(target_path)
        files = os.listdir(source_path)  # Get the list of files and directories in the folder
        for f in files:
            if os.path.isdir(source_path + '/' + f):  # Determine whether it is a folder
                copy_allfiles(source_path + '/' + f, target_path + '/' + f)  # Call this function recursively
            else:
                shutil.copy(source_path + '/' + f, target_path + '/' + f)  # copy file

    create_folder(project_name)
    copy_allfiles(project_name)


if __name__ == "__main__":
    ...
