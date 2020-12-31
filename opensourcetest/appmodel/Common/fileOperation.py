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
            logging.info(f"Start creating file:{file_path}")
            os.mkdir(file_path)

    @staticmethod
    def create_file(file_path):
        """
        Create a file, which is automatically created when the directory does not exist
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
        To create a file path, first determine whether the directory exists
        :param file_dir:
        :return:
        """
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

    @staticmethod
    def read_yaml(file):
        """
        Read yaml file and return file object
        @param file:
        @return:
        """
        if os.path.isfile(file):
            fr = open(file, 'r', encoding='utf-8')
            yaml_info = yaml.safe_load(fr)
            fr.close()
            return yaml_info
        else:
            logging.error(file, 'File does not exist!')
            sys.exit()
