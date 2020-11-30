# !/user/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import yaml
import logging


class FileOption:
    @staticmethod
    def file_mkdir(file_path):
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        else:
            logging.warning(f"{file_path} The directory already exists and does not need to be created again.")

    @staticmethod
    def create_file(file_path):
        """
        创建文件，当目录不存在时自动创建
        :param file_path:
        :return:
        """
        dir_path = os.path.split(file_path)[0]
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        if not os.path.isfile(file_path):
            f = open(file_path, mode='w', encoding='utf-8')
            f.close()

    @staticmethod
    def create_dirs(file_dir):
        """
        创建文件路径,先判断目录是否存在
        :param file_dir:
        :return:
        """
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

    @staticmethod
    def read_yaml(file):
        """
            读取yaml文件，返回文件对象
        @param file:
        @return:
        """
        if os.path.isfile(file):
            fr = open(file, 'r', encoding='utf-8')
            yaml_info = yaml.safe_load(fr)
            fr.close()
            return yaml_info
        else:
            logging.error(file, '文件不存在')
            sys.exit()
