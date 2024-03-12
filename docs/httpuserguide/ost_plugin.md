# OpenSourceTest 内置插件

OpenSourceTest内置插件用于处理OST中的请求，断言检查，yaml文件定位等操作。



## start_run_case

### requestEngine的start_run_case参数说明：

- params_object：必填，yaml接口文件对象
- params_mark：必填，yaml文件的定位方式，支持str和int两种定位方式，str定位根据yaml中的desc来进行，int根据yaml中的相同数据结构的索引进行（PS：索引从0开始）
- checker：断言器，支持列表和元组，或者元组列表嵌套的方式
- session_connection：用于保持客户端与服务端的连接，传递token/cookie，或者其他header，以字典的形式传入
- url_converter：url转换器，用于替换接口中的$符号，可以通过在yaml的具体某个接口中使用$代替url中的某些需要通过动态获取的参数，然后使用url_converter在脚本中进行替换，支持str/tuple/list（PS：替换的参数必须和yaml中该接口的$个数一一对应）
- json：支持与yaml中的该json数据进行深层拼接，支持嵌套
- 其他参数的传递通原始requests中的参数要求。

#### checker补充说明：
- 内置断言器，直接对http的response进行断言，支持元组/列表中嵌套元组的方式，如下所示，`checker = [("status_code", 200, "GTE"), ("body.code", 200, "EQ")]`，列表中是两个元组，会进行两次断言操作，元组中是三个参数，第一个是从响应数据中所需要取得值，第二个值是预期值，第三个是断言方式，先断言接口返回状态码status_code,然后断言接口返回数据body.code,使用的是jmespath进行取值
- 内置断言器支持元组中只有两个参数的情况，第一个是从响应数据中所需要取得值，第二个值是预期值，默认采用EQ断言
- 内置断言器支持的断言方式见表格

| 断言方式    | 说明                | 备注                            |
|---------|-------------------|-------------------------------|
| EQ      | 断言两个值相等           | checker中的断言方式不区分大小写，默认都会转换为大写 |
| GT      | 大于，第一个值大于第二个值     | checker中的断言方式不区分大小写，默认都会转换为大写                        |
| GTE     | 大于等于，第一个值大于等于第二个值 | checker中的断言方式不区分大小写，默认都会转换为大写                         |
| LT      | 小于，第一个值小于第二个值     | checker中的断言方式不区分大小写，默认都会转换为大写                         |
| LTE     | 小于等于，第一个值小于等于第二个值 | checker中的断言方式不区分大小写，默认都会转换为大写                         |
| NE      | 不等于               | checker中的断言方式不区分大小写，默认都会转换为大写                         |
| CONTAIN | 包含，第二个值包含于第一个值    | checker中的断言方式不区分大小写，默认都会转换为大写                         |

~~~python

class TestFinancialManagement:

    @allure.title("财务管理，汇款账户，测试分销商汇款账户新增")
    @pytest.mark.parametrize("reseller_id,remittance,remittance_name",
                             [(23075, "分销商汇款账户测试名字", "测试汇款账号")])
    def test_remittance_account_add(self, reseller_id, remittance, remittance_name, token):
        checker = [("status_code", 200, "GTE"), ("body.code", 200, "EQ")]
        remittance_account_add(reseller_id, remittance, remittance_name, token, checker)


~~~
~~~python
2024-03-12 09:29:26 | INFO      | consolelog:log_output:30 - 
================== response details ==================
status_code : 200
headers  : {
    "Content-Type": "application/json; charset=utf-8",
    "Transfer-Encoding": "chunked",
    "Connection": "keep-alive",
    "Server": "nginx",
    "X-Powered-By": "PHP/7.2.34",
    "Access-Control-Allow-Methods": "OPTIONS,POST,GET,PUT,DELETE",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Version,authorization,Authorization,Origin, X-Requested-With, Content-Type, Accept, authKey, sessionId,X-HTTP-Method-Override,reseller-authKey,reseller-sessionId",
    "Date": "Tue, 12 Mar 2024 01:29:26 GMT",
    "Access-Control-Allow-Credentials": "true",
    "X-Kong-Upstream-Latency": "189",
    "X-Kong-Proxy-Latency": "16",
    "Via": "kong/3.2.2"
}
cookies  : {}
encoding : utf-8
content_type : application/json; charset=utf-8
body     : {
    "code": 200,
    "data": {
        "reseller_id": 23075,
        "remittance": "分销商汇款账户测试名字",
        "remittance_name": "测试汇款账号",
        "create_time": "2024-03-12 09:29:26",
        "update_time": "2024-03-12 09:29:26",
        "id": "124"
    },
    "error": ""
}
~~~

#### url_converter补充说明：
- 主要用于对yaml文件中的url直接拼接字符的情况进行补充，例如下列情况，需要通过id对用户进行删除，/admin/user/22，此时可以在yaml写成/admin/user/$的形式，在start_run_case的参数中指定url_converter="22",即可在发送请求前完成替换。
- url_converter也支持多重替换，支持参数为字符串/列表/元组，当为列表和元组时，会遍历url path中所有的$进行依次替换
~~~yaml
description: "人员管理"
parameters:
  - url: /admin/user/$
    desc: "删除账户"
    method: delete
    headers: {
      "Content-Type": "application/json",
      "accept": "application/json, text/plain, */*",
    }
    params: { }
    data: { }
    json: { }
    files: { }
~~~

#### base_url补充说明：
- 这是一个url的扩展，有时候，我们需要接口去访问不同的网址获取数据，如果不指定base_url，那么从conf目录的conf.yaml中进行获取server_info的base_url，如果指定了base_url，那么使用指定的base_url与yaml文件对象中对应的接口进行拼接，然后发送请求
- 在opensourcetest默认生成的项目框架目录中，位于Base中的requestEngine模块（代码如下）有一个BASE_URL参数，就是从conf.yaml中获取全局的base_url，非全局的base_url只需要在调用start_run_case中指定即可
~~~python
#!/user/bin/env python
# -*- coding: utf-8 -*-
import os
import logging
from typing import Text, Union
from opensourcetest.common.yamlOperation import YamlFileOption
from opensourcetest.builtin.ostHttp import ost_http_runner
# Read the conf.yml Global profile
conf_yaml_path = os.path.join(os.path.dirname(__file__).split("Base")[0], "Conf/conf.yml")
# According to the read conf.yml To obtain the testing website service and other information
conf_server_info = YamlFileOption.read_yaml(conf_yaml_path)["server_info"]

BASE_URL = conf_server_info["protocol"] + '://' + conf_server_info["base_url"]
VERIFY = conf_server_info["verify"]


def start_run_case(params_object, params_mark: Union[Text, int], checker=None, session_connection=None, params=None,
                   data=None, json=None, files=None, url_converter=None, base_url=None, **kwargs):
    ost_req_resp = ost_http_runner(params_object, params_mark,  base_url=BASE_URL if not base_url else base_url, verify=VERIFY, checker=checker,
                                   session_connection=session_connection, params=params,
                                   data=data, json=json, files=files, url_converter=url_converter, **kwargs)
    return ost_req_resp.response.dict()
~~~

#### session_connection补充说明：
- 这是一个特殊的参数主要用来向request请求中的header传递token/cookie参数，需要自己组装成字典，指定后，会自动拼接到header中去，通常用于将fixture的作用域设置为session，全局唯一初始化使用，示例如下。

~~~python
#定义全局session函数token
@pytest.fixture(scope="session")
def token():
    params = {"username": "zouzou", "password": "zouzou"}
    result = start_run_case(Login, 0, ("status_code", 200, "GTE"), json=params)
    auth = {
        "Authorization": f'JWT {result["body"]["data"]["token"]}'
    }
    yield auth
~~~

~~~python

# 在start_run_case对session_connection指定token进行header拼接
@allure.feature("登录模块")
class TestLogin:
    @allure.story("用户管理")
    @allure.title("查询用户")
    def test_get(self, token):
        params = {
            "page": 1,
            "size": 20
        }
        start_run_case(Login, "查询", session_connection=token, params=params)


~~~