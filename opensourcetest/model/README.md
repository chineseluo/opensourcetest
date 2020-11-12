```markdown
# 简介

接口自动化测试框架：pytest+requests+allure

## 项目结构

整个框架主要分为三层：Base层、Parameter层、TestCase层，采用传统的互联网的垂直架构模式。

- Base层封装requests对象方法
- Parameter层负责解析yaml文件
- 测试case存放在TestCases层，主要做断言等操作

## 运行环境

运行此项目前需要进行如下操作：

1. 使用pycharm导入项目

2. 打开pycharm的terminal，切换到 requirements.txt 所在的目录下，使用如下命令 ，就能在当前的 python 环境中导入所有需要的包：

```
pip install -r requirements.txt
   ```

环境说明：

- 开发工具：pycharm
- python版本：python3.8
- 测试case总入口：run.py

---

**有任何使用问题请联系我：chineseluo**

---

# 模块设计

## Base模块

封装操作接口请求方法、断言等

## Common模块

封装的读取配置文件的公共方法，类似于util工具类

## Conf模块

存放全局配置文件

- config.yaml中存放全局配置文件

## Parameter模块

用于处理yaml文件对象

## Report模块

存放测试报告，以及测试报告的生成模板allure

- report模块使用allure进行测试报告生成

## TestCases模块

用于存放测试case

- 使用conftest.py进行页面对象注入，类似unintest的setup，teardown的操作，通过装饰器进行控制
- 测试case，页面的测试用例，根据模块来进行划分

## 其他文件说明

- `conftest.py`：封装了本地测试driver，分布式driver方法，定义了钩子函数，进行pytest功能拓展

- `pytest.ini`：配置了pytest的日志功能，以及测试用例扫描等

- `requirements.txt`：框架运行所需要的包

- `run.py`：本地调试入口，ci集成测试入口

---

# allure装饰器

- @allure.severity("critical")
  - 优先级，包含blocker, critical, normal, minor, trivial几个不同的等级
    - 测试用例优先级1：blocker，中断缺陷（客户端程序无响应，无法执行下一步操作）
    - 测试用例优先级2：critical，临界缺陷（ 功能点缺失）
    - 测试用例优先级3：normal，普通缺陷（数值计算错误）
    - 测试用例优先级4：minor，次要缺陷（界面错误与UI需求不符）
    - 测试用例优先级5：trivial级别，轻微缺陷（必输项无提示，或者提示不规范）'
- @allure.feature("测试模块_demo1")
  - 功能块，feature功能分块时比story大,即同时存在feature和story时,feature为父节点
- @allure.story("测试模块_demo2")
  - 功能块，具有相同feature或story的用例将规整到相同模块下,执行时可用于筛选
- @allure.issue("BUG号：123")
  - 问题标识，关联标识已有的问题，可为一个url链接地址
- @allure.testcase("用例名：测试字符串相等")
  - 用例标识，关联标识用例，可为一个url链接地址

# 环境搭建

## python安装

`version:3.8`

## java环境配置

`version 1.8`，win10系统中配置配置java环境，参考[win10java环境配置](https://www.runoob.com/w3cnote/windows10-java-setup.html)

## allure安装

- 不同平台安装allure的方法不同，这里仅介绍windows平台下allure的安装步骤。其它平台请阅读[allure官方文档](https://docs.qameta.io/allure/)进行操作
- 官方提供的安装方法可能会受网络环境影响而安装失败，可选择在[GitHub仓库](https://github.com/allure-framework/allure2 )下载文件并安装allure2
- Windows环境下可以用以下步骤进行安装
  - 安装scoop，使用**管理员权限**打开powershell窗口，输入命令`Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')`
  - 如果安装不成功则运行`Set-ExecutionPolicy RemoteSigned -scope CurrentUser`，运行成功后重新执行第一步
  - scoop安装成功后控制台会输出`Scoop was installed successfully!`
  - 执行`scoop install allure`进行allure的安装
  - allure安装成功后控制台会输出`'allure' (2.13.1) was installed successfully!`

# 如何编写测试用例

下面详细说明如何添加一条用例，以登录界面演示

1. 在Parameter下Login模块新建一个页面元素yaml文件，Login.yaml

   字段说明：

   - description：yaml文件说明
   - parameters：参数说明
       - url：接口地址（不含host,host在conf.yml单独配置）
       - desc：接口描述
       - method：请求方法
       - headers: 请求头
       - params: 请求拼接参数
       - data: data数据
       - json： json数据

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
   ```

   

2. 在Parameter模块下的yamlChoice.py文件中进行Login.yaml注册，生成一个yaml文件对象，初始化传递两个参数，一个是模块名，一个是yaml配置文件名

   ```yaml
   # 注册yaml文件对象
   class Login(AutoInjection):
       def __init__(self):
           super(Login, self).__init__(self.__class__.__name__)
   ```

5. 在TestCases下面创建一个test_login.py，导入Base.requestEngine.start_run_case方法，用于用例执行

   

   ```python
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
           result = start_run_case(Login, "用户权限")
           print(result)
   ```
   
6. 执行用例

   执行用例可以通过两种常用的方法进行

   1. pycharm中配置`test runner`为`pytest`，配置路径为`settings->Tools->Python Integrated Tools->Testing`；配置完成后就能够在打开测试用例文件后看到可执行的按钮了

   2. 运行在根目录下的`run.py`文件

      


```

# requests几种传递参数的区别：
params:字典或者字节序列，作为参数添加到URL中，即params是往URL后面添加参数，存在于requests.get中
body:传递的消息体，里面通常是data和json
data:消息体的一种格式，字典格式
json:消息体的一种格式，json格式


```