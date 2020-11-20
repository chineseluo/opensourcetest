#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : interface_auto_frame
@Time    : 2020/8/26 10:00
@Auth    : chineseluo
@Email   : 848257135@qq.com
@File    : baseRequest.py
@IDE     : PyCharm
------------------------------------
"""
import os
import jmespath
import requests
import logging
from opensourcetest.common.consolelog import log_output
from opensourcetest.builtin.models import OSTRespData, OSTReqData, OSTReqRespData, MethodEnum
from opensourcetest.common.yamlOperation import YamlFileOption

# 读取Conf下的conf.yml全局配置文件
conf_yaml_path = os.path.join(os.path.dirname(__file__).split("builtin")[0], "model/Conf/conf.yml")
# 根据读取的conf.yml中的配置信息获取测试的网址服务等信息
conf_server_info = YamlFileOption.read_yaml(conf_yaml_path)["server_info"]


class BaseRequest:
    """
    Encapsulate the four common request methods in requests library, and call different private methods according to
    get / post / delete / put in yaml by providing a public method
    """


    @staticmethod
    def __get(url, params=None, jmespath_rule=None, **kwargs):
        if jmespath_rule:
            get_result = jmespath.search(jmespath_rule, requests.get(url=url, params=params, **kwargs).json())
        else:
            get_result = requests.get(url=url, params=params, **kwargs)
        return get_result

    @staticmethod
    def __delete(url, jmespath_rule=None, **kwargs):
        if jmespath_rule:
            delete_result = jmespath.search(jmespath_rule, requests.delete(url=url, **kwargs).json())
        else:
            delete_result = requests.delete(url=url, **kwargs)
        return delete_result

    @staticmethod
    def __put(url, data=None, jmespath_rule=None, **kwargs):
        if jmespath_rule:
            put_result = jmespath.search(jmespath_rule, requests.put(url=url, data=data, **kwargs).json())
        else:
            put_result = requests.put(url=url, data=data, **kwargs)
        return put_result

    @staticmethod
    def __post(url=None, data=None, json=None, jmespath_rule=None, **kwargs):
        if jmespath_rule:
            post_result = jmespath.search(jmespath_rule, requests.post(url=url, data=data, json=json, **kwargs).json())
        else:
            post_result = requests.post(url=url, data=data, json=json, **kwargs)
        return post_result

    def send_request(self, url, method, send_params=None, send_data=None, send_json=None,
                     **kwargs) -> OSTReqRespData:
        """
        Choose different processing logic according to the method of transfer
        :param url:
        :param method:
        :param send_params:
        :param send_data:
        :param send_json:
        :param kwargs:
        :return:
        """
        result = None
        if method == MethodEnum.GET:
            result = self.__get(params=send_params, url=url, **kwargs)
        elif method == MethodEnum.POST:
            result = self.__post(data=send_data, json=send_json, url=url,
                                 **kwargs)
        elif method == MethodEnum.DELETE:
            result = self.__delete(url=url, **kwargs)
        elif method == MethodEnum.PUT:
            result = self.__put(data=send_data, url=url, **kwargs)
        else:
            logging.error(f"Please pass the correct request method parameters! The current error parameter is:{method}")
        ost_req = OSTReqData(
            method=result.request.method,
            url=result.request.url,
            headers=result.request.headers,
            cookies=result.request._cookies,
            body=result.request.body
        )
        log_output(ost_req, "request")
        if result.headers["Content-Type"].find("json") != -1:
            ost_rep_body = result.json()
        elif result.headers["Content-Type"].find("xml") != -1 \
                or result.headers["Content-Type"].find("html") != -1 \
                or result.headers["Content-Type"].find("text") != -1:
            ost_rep_body = result.text
        else:
            ost_rep_body = result.content
        ost_resp = OSTRespData(
            status_code=result.status_code,
            cookies=result.cookies,
            encoding=result.encoding,
            headers=result.headers,
            content_type=result.headers.get("content-type"),
            body=ost_rep_body
        )
        log_output(ost_resp, "response")
        ost_req_resp = OSTReqRespData(
            request=ost_req,
            response=ost_resp
        )
        logging.info(f"Output object:{ost_req_resp}")
        return ost_req_resp


if __name__ == '__main__':
    ...
