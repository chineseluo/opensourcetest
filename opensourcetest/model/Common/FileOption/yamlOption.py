#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : opensourcetest
@Time    : 2020/8/25 16:22
@Auth    : chineseluo
@Email   : 848257135@qq.com
@File    : yamlOption.py
@IDE     : PyCharm
------------------------------------
"""
import yaml
import os
import logging


class YamlFileOption:
    @staticmethod
    def read_yaml(file):
        """
        读取yml文件
        :param file:
        :return:
        """
        if os.path.isfile(file):
            fr = open(file, 'r', encoding='utf-8')
            yaml_info = yaml.safe_load(fr)
            fr.close()
            return yaml_info
        else:
            print(file, '文件不存在')
            logging.error('文件不存在！{}'.format(file))
            return None