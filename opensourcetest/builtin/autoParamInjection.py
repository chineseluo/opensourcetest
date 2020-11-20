#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : opensourcetest
@Time    : 2020/8/25 16:17
@Auth    : chineseluo
@Email   : 848257135@qq.com
@File    : autoParamInjection.py
@IDE     : PyCharm
------------------------------------
"""
import os
import inspect
import logging
from typing import Text, Dict
from opensourcetest.common.yamlOperation import YamlFileOption


class AutoInjection:
    """Automatic yaml object injection.
    Assign the basic attribute to the subclass by inheriting autoinjection.
    """

    def __init__(self, *args):
        self.interface_info = []
        self.__read_yaml(*args)
        logging.info(f"{self.__class__.__name__} Yaml object injection in progress")

    def __read_yaml(self, *args):
        """
        The interface yaml object is read, and the parent class autoinjection is inherited by the subclass. When the
        subclass is initialized, it is transformed upward to read the yaml file in the corresponding subclass yaml
        module
        :param args:
        :return:
        """
        # 待优化项：支持读取Parameter下新建模块和文件，以及直接创建文件
        logging.warning(f"output class file path：{inspect.getfile(self.__class__)}")
        logging.warning(os.path.dirname(__file__))
        if len(args) == 1:
            if os.path.dirname(__file__).find("opensourcetest") == -1:
                yaml_path = os.path.join(os.path.dirname(__file__), args[0], args[0] + ".yml")
            else:
                logging.warning(f"Use the yaml path configured by mode in OST framework to retrieve")
                yaml_path = os.path.join(os.path.dirname(__file__).split("builtin")[0], "model/Parameter", args[0],
                                         args[0] + ".yml")
            self.interface_info = YamlFileOption().read_yaml(yaml_path)['parameters']
        elif len(args) == 2:
            if os.path.dirname(__file__).find("opensourcetest") == -1:
                yaml_path = os.path.join(os.path.dirname(__file__), args[0], args[1] + ".yml")
            else:
                logging.warning(f"Use the yaml path configured by mode in OST framework to retrieve")
                yaml_path = os.path.join(os.path.dirname(__file__).split("builtin")[0], "model/Parameter", args[0],
                                         args[1] + ".yml")
            self.interface_info = YamlFileOption().read_yaml(yaml_path)['parameters']
        else:
            logging.error("Parameter transfer error. Only two parameters can be received")

    def get_param_by_yaml(self, params_mark) -> Dict:
        param_dict = {}
        if isinstance(params_mark, Text):
            for item in self.interface_info:
                if Text(item["desc"]) == params_mark:
                    param_dict = item
                    return param_dict
            if not param_dict:
                logging.error(f"Failed to get interface parameters from yaml file by desc. Please check the "
                              f"corresponding relationship of yaml file. The error parameter is：{params_mark}")
        elif isinstance(params_mark, int):
            param_dict = self.interface_info[params_mark]
            if not param_dict:
                logging.error(f"Failed to get interface parameters from yaml file by index. Please check the "
                              f"corresponding relationship of yaml file. The error parameter is：{params_mark}")
        else:
            logging.error(f"Parameter passing error. Only integer and string types are supported. The error parameter "
                          f"is：{params_mark}")
        return param_dict


if __name__ == '__main__':
    if os.path.dirname(__file__).find("opensourcetest") != -1:
        logging.info(os.path.dirname(__file__).find("opensourcetest"))
