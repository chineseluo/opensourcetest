#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : interface_auto_frame
@Time    : 2020/8/25 16:17
@Auth    : chineseluo
@Email   : 848257135@qq.com
@File    : autoParamInjection.py
@IDE     : PyCharm
------------------------------------
"""
import yaml
import os

import logging
from opensourcetest.Common.comFileOption import get_roots_dirs_files_list
from opensourcetest.Common.yamlOption import YamlFileOption


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

    def get_param_by_yaml(self, params_mark) -> dict:
        param_dict = {}
        if isinstance(params_mark, str):
            for item in self.interface_info:
                if item["desc"] == params_mark:
                    param_dict = item
                    return param_dict
                else:
                    logging.error(f"Failed to get interface parameters from yaml file. Please check the corresponding "
                                  f"relationship of yaml file. The error parameter is：{params_mark}")
        elif isinstance(params_mark, int):
            param_dict = self.interface_info[params_mark]
        else:
            logging.error(f"Parameter passing error. Only integer and string types are supported. The error parameter "
                          f"is：{params_mark}")
        return param_dict


if __name__ == '__main__':
    if os.path.dirname(__file__).find("opensourcetest") != -1:
        logging.info(os.path.dirname(__file__).find("opensourcetest"))
