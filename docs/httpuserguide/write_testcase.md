# 编写测试用例

OpenSourceTest v0.1.0通过yaml接口对象注入的方式，整个框架分为三层，Base层、Parameter层、TestCase层，采用传统的互联网的垂直架构模式。



## yaml编写

在Parameter下Login模块新建一个页面元素yaml文件，Login.yaml，yaml内容如下：

~~~yaml
description: 获取blog权限接口信息
parameters:
  - url: /chineseluo/ajax/blogSubscription
    desc: 用户权限
    method: get
    headers: {
      "Content-Type": "application/json; charset=utf-8"
    }
    params: {}
    data: {}
    json: {}
~~~

yaml格式说明：

   - description：yaml文件说明
   - parameters：参数说明
       - url：接口地址（不含host,host在conf.yml单独配置）
       - desc：接口描述
       - method：请求方法
       - headers：请求头
       - params：请求拼接参数
       - data：data数据
       - json：json数据



## yaml对象注入



在Parameter模块下的yamlChoice.py文件中进行Login.yaml注册，继承AutoInjection，生成一个yaml文件对象，初始化传递参数规则举例：

- 当文件夹名和模块名一致时（不包括文件的yaml后缀），可以只传递一个参数。传递两个参数时候，第一个参数为文件夹名，第二个为文件名（不包括文件的yaml后缀）

  ![1](..\images\testcase\1.png)

  可以采用如下写法：

  ~~~python
  from opensourcetest.builtin.autoParamInjection import AutoInjection
  
  
  class Login(AutoInjection):
      def __init__(self):
          super(Login, self).__init__("Login")
  ~~~

- 当你定义的类名和文件夹名和模块名一致时（不包括文件的yaml后缀），可以只传递一个参数。传递两个参数时候，第一个参数为文件夹名，第二个为文件名（不包括文件的yaml后缀）

  例如在yamlChoice.py中新添加一个类，Login，可以使用如下写法：

  ~~~python
  from opensourcetest_test_test.builtin.autoParamInjection import AutoInjection
  
  
  class Login(AutoInjection):
      def __init__(self):
          super(Login, self).__init__(self.__class__.__name__)
  ~~~

- 当你在Parameter文件夹下，新建的文件夹名和其中的文件名（不包括文件的yaml后缀）不一致时，需要传递两个参数，第一个参数为文件夹名，第二个为文件名（不包括文件的yaml后缀）

  ![2](../images/testcase/2.png)

  ~~~python
  from opensourcetest_test_test.builtin.autoParamInjection import AutoInjection
  
  
  class Register(AutoInjection):
      def __init__(self):
          super(Register, self).__init__("Register", "Login")
  ~~~

  

## 编写测试用例

在TestCases下面创建一个test_login.py，导入Base.requestEngine.start_run_case方法，用于用例执行。获取接口对象方式，通过导入Parameter.yamlChoice中的接口yaml对象，可以通过desc定位到具体的接口，示例如下：

~~~python
# coding:utf-8
import pytest
import allure
from Base.requestEngine import start_run_case
from Common.StringOption.StringOperate import String
from Parameter.yamlChoice import Login


@allure.feature("Login")
class TestLoginPageCase:

 @allure.story("Login")
    @allure.severity("normal")
    @allure.description("测试登录")
    @allure.link("https://www.baidu.com", name="连接跳转百度")
    @allure.testcase("https://www.sina.com", name="测试用例位置")
    @allure.title("执行测试用例用于登录模块")
    def test_login(self, login_page_class_load, function_driver):
        result = start_run_case(Register, 0, [("encoding", "utf-8"), ("status_code", "200")])
        logging.info(result)
~~~



## 执行用例



执行用例可以通过两种常用的方法进行

1. pycharm中配置`test runner`为`pytest`，配置路径为`settings->Tools->Python Integrated Tools->Testing`；配置完成后就能够在打开测试用例文件后看到可执行的按钮了

2. 运行在根目录下的`run.py`文件

