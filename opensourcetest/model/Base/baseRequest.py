#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : opensourcetest
@Time    : 2020/8/26 10:00
@Auth    : chineseluo
@Email   : 848257135@qq.com
@File    : baseRequest.py
@IDE     : PyCharm
------------------------------------
"""
import os
import requests
import logging
from opensourcetest.model.Common.FileOption.yamlOption import YamlFileOption

# 读取Conf下的conf.yml全局配置文件
conf_yaml_path = os.path.join(os.path.dirname(__file__).split("Base")[0], "Conf/conf.yml")
# 根据读取的conf.yml中的配置信息获取测试的网址服务等信息
conf_server_info = YamlFileOption.read_yaml(conf_yaml_path)["server_info"]


class BaseRequest:
    """
    封装requests库中常用的四种请求方式，通过提供一个公共方法，根据yaml中的get/post/delete/put进行判断，调用不同的私有方法
    """

    def __init__(self):
        # 获取base_url
        self.__base_url = conf_server_info["protocol"] + '://' + conf_server_info["base_url"]
        # 是否开启SSL验证
        self.__verify = conf_server_info["verify"]

    @staticmethod
    def __get(url, get_params=None, **kwargs):
        get_result = requests.get(url=url, params=get_params, **kwargs)
        return get_result

    @staticmethod
    def __delete(url, **kwargs):
        delete_result = requests.delete(url=url, **kwargs)
        return delete_result

    @staticmethod
    def __put(url, data=None, **kwargs):
        put_result = requests.put(url=url, data=data, **kwargs)
        return put_result

    @staticmethod
    def __post(url=None, data=None, json=None, **kwargs):
        post_result = requests.post(url=url, data=data, json=json, **kwargs)
        return post_result

    def send_request(self, part_url, method, send_params=None, send_data=None, send_json=None, **kwargs):
        """
        根据传递的方法选择不同的处理逻辑
        :param part_url:
        :param method:
        :param send_params:
        :param send_data:
        :param send_json:
        :param kwargs:
        :return:
        """
        result = None
        if method == "GET":
            result = self.__get(params=send_params, url=self.__base_url + part_url, verify=self.__verify, **kwargs)
        elif method == "POST":
            result = self.__post(data=send_data, json=send_json, url=self.__base_url + part_url, verify=self.__verify,
                                 **kwargs)
        elif method == "DELETE":
            result = self.__delete(url=self.__base_url + part_url, verify=self.__verify, **kwargs)
        elif method == "PUT":
            result = self.__put(data=send_data, url=self.__base_url + part_url, verify=self.__verify, **kwargs)
        else:
            logging.error("请传递正确的请求方法参数！当前错误参数为：{}".format(method))
        return result


if __name__ == '__main__':
    ...
