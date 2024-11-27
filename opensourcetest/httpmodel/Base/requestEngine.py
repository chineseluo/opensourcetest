#!/user/bin/env python
# -*- coding: utf-8 -*-
import os
import jmespath
from typing import Text, Union
from opensourcetest.common.yamlOperation import YamlFileOption
from opensourcetest.builtin.ostHttp import ost_http_runner

# Read the conf.yml Global profile
conf_yaml_path = os.path.join(os.path.dirname(__file__).split("Base")[0], "Conf/conf.yml")
# According to the read conf.yml To obtain the testing website service and other information
conf_server_info = YamlFileOption.read_yaml(conf_yaml_path)["server_info"]

BASE_URL = conf_server_info["protocol"] + '://' + conf_server_info["base_url"]
VERIFY = conf_server_info["verify"]


def start_run_case(params_object: object, params_mark: Union[Text, int], checker=None, session_connection=None, params=None,
                   data=None, json=None, files=None, url_converter=None, base_url=None, jmespath_rule=None, **kwargs):
    """

    @param params_object: yaml对象
    @param params_mark: 用于标记yaml对象中的接口请求元数据，通过yaml文件索引 or yaml文件对象中的desc进行锚定接口
    @param checker: 用于断言检查，支持多层断言
    @param session_connection: 用于在header添加信息，常用于token
    @param params: 用于params数据传递，同requests库
    @param data: 用于data数据传递，同requests库
    @param json: 用于json数据传递，同requests库
    @param files: 用于文件/图片上传，同requests库
    @param url_converter: 用于对yaml文件中，url里面的$进行动态转换，例如/admin/v1/$/detail/
    @param base_url: 请求地址
    @param jmespath_rule: 通过使用jmespath库的规则对于接口响应的数据进行提取
    @param kwargs:
    @return: 响应对象字典 or jmespath提取后的响应值
    """
    ost_req_resp = ost_http_runner(params_object, params_mark, base_url=BASE_URL if not base_url else base_url,
                                   verify=VERIFY, checker=checker,
                                   session_connection=session_connection, params=params,
                                   data=data, json=json, files=files, url_converter=url_converter, **kwargs)
    resp_dict = ost_req_resp.response.dict()
    return jmespath.search(jmespath_rule, resp_dict) if jmespath_rule is not None else resp_dict


if __name__ == "__main__":
    ...
