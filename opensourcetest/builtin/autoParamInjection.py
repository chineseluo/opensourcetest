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
from opensourcetest.builtin.locate import get_ui_locator, get_locator


class AutoInjection:
    """Automatic yaml object injection.
    Assign the basic attribute to the subclass by inheriting autoinjection.
    """

    def __init__(self, *args):
        # self.interface_info = []
        self.__read_yaml(*args)
        logging.info(f"{self.__class__.__name__} Yaml object injection in progress")

    @property
    def interface_info(self):
        return self._interface_info

    def __read_yaml(self, *args):
        """
        The interface or ui yaml object is read, and the parent class autoinjection is inherited by the subclass. When the
        subclass is initialized, it is transformed upward to read the yaml file in the corresponding subclass yaml
        module
        :param args:
        :return:
        """
        if len(args) == 1:
            if os.path.dirname(inspect.getfile(self.__class__)).find("opensourcetest") == -1:
                yaml_path = os.path.join(os.path.dirname(inspect.getfile(self.__class__).split("yamlChoice.py")[0]),
                                         args[0], args[0] + ".yaml")
            else:
                if os.path.dirname(inspect.getfile(self.__class__)).find("Parameter") != -1:
                    yaml_path = os.path.join(os.path.dirname(__file__).split("builtin")[0], "httpmodel/Parameter",
                                             args[0], args[0] + ".yaml")

                elif os.path.dirname(inspect.getfile(self.__class__)).find("ActivityObject") != -1:
                    yaml_path = os.path.join(os.path.dirname(__file__).split("builtin")[0], "appmodel/Parameter",
                                             args[0], args[0] + ".yaml")
                else:
                    yaml_path = os.path.join(os.path.dirname(__file__).split("builtin")[0], "uimodel/PageObject",
                                             args[0], args[0] + ".yaml")
                logging.warning(f"output class file path：{inspect.getfile(self.__class__)}")
                logging.warning(f"Use the yaml path configured by mode in OST framework to retrieve")
                logging.warning(f"Output {args[0]} yaml file address: {yaml_path}")
            self._interface_info = YamlFileOption().read_yaml(yaml_path)['parameters']
        elif len(args) == 2:
            if os.path.dirname(inspect.getfile(self.__class__)).find("opensourcetest") == -1:
                yaml_path = os.path.join(os.path.dirname(inspect.getfile(self.__class__).split("yamlChoice.py")[0]),
                                         args[0], args[1] + ".yaml")
            else:
                if os.path.dirname(inspect.getfile(self.__class__)).find("Parameter") != -1:
                    yaml_path = os.path.join(os.path.dirname(__file__).split("builtin")[0], "httpmodel/Parameter",
                                             args[0], args[1] + ".yaml")
                elif os.path.dirname(inspect.getfile(self.__class__)).find("ActivityObject") != -1:
                    yaml_path = os.path.join(os.path.dirname(__file__).split("builtin")[0], "appmodel/ActivityObject",
                                             args[0], args[0] + ".yaml")
                else:
                    yaml_path = os.path.join(os.path.dirname(__file__).split("builtin")[0], "uimodel/PageObject",
                                             args[0], args[1] + ".yaml")
                logging.warning(f"output class file path：{inspect.getfile(self.__class__)}")
                logging.warning(f"Use the yaml path configured by mode in OST framework to retrieve")
                logging.warning(f"Output {args[1]} yaml file address: {yaml_path}")
            self._interface_info = YamlFileOption().read_yaml(yaml_path)['parameters']
        else:
            logging.error("Parameter transfer error. Only two parameters can be received")

    def get_param_by_yaml(self, params_mark) -> Dict:
        param_dict = {}
        if isinstance(params_mark, Text):
            for item in self.interface_info:
                if Text(item["desc"]) == params_mark:
                    param_dict = item
                    return param_dict
                if os.path.dirname(inspect.getfile(self.__class__)).find("PageObject") != -1:
                    if Text(item["elem_name"]) == params_mark:
                        param_dict = item
                        return param_dict
                if os.path.dirname(inspect.getfile(self.__class__)).find("ActivityObject") != -1:
                    if Text(item["elem_name"]) == params_mark:
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

    def get_elem_locator(self, params_mark):
        param_dict = self.get_param_by_yaml(params_mark)
        locator = get_locator(param_dict)
        return locator


if __name__ == '__main__':
    if os.path.dirname(__file__).find("opensourcetest") != -1:
        logging.info(os.path.dirname(__file__).find("opensourcetest"))
