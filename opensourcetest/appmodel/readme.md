# 简介

app自动化测试框架：pytest+appium+allure

## 项目结构

整个框架主要分为三层：Base层、ActivityObject层、TestCase层，采用传统的互联网的垂直架构模式。

- 元素公共操作方法封装存放在Base层
- 页面元素操作存放在第二层ActivityObject层，后面如果页面元素变化，直接在第二层相应的Activity对象修改即可
- 测试case存放在TestCases层，主要做断言等操作

---

# 模块设计

## Base模块

封装操作元素的公共方法，以及断言方法

- assertMethod.py封装断言的方法，断言失败截图，按需自己可以进行封装
- base封装页面元素操作方法

## Common模块

封装的读取配置文件的公共方法，类似于util工具类

- publicMethod，封装公共方法，后面可能会讲一些方法分类创建不同的py模块进行管理，便于维护
- file_option.py，封装文件操作方法

## Conf模块

存放全局配置文件

- config.yaml中存放全局配置文件，当前包含两个
  - allure_environment：存放allure报告中环境描述初始化文件
- appium_config.yaml：存放selenium远程分布式调用配置文件

## Logs模块

用于生成日志文件

- 使用pyteset本身集成的日志插件，不在进行手动封装日志模块，存放pytest.ini中的日志文件输出

## ActivityObject模块

提取页面对象封装公共操作方法

- 使用yaml文件进行页面元素的管理
- 使用elem_params.py进行yaml文件注入，生成yaml文件对象
- 页面对象初始化页面元素对象，调用base层，封装元素操作方法

## Report模块

存放测试报告，以及测试报告的生成模板allure

- report模块使用allure进行测试报告生成
- 可以自定义启用不同的测试分析图表用于测试结果分析
- 内置测试图片存放路径，如果需要每次测试都清理以前的图片，可以添加allure命令进行清理

## TestCases模块

用于存放测试case

- 使用conftest.py进行页面对象注入，类似unintest的setup，teardown的操作，通过装饰器进行控制
- 测试case，页面的测试用例，根据模块来进行划分

## 其他文件说明

- `conftest.py`：封装了本地测试driver，分布式driver方法，定义了钩子函数，进行pytest功能拓展

- `pytest.ini`：配置了pytest的日志功能，以及测试用例扫描

- `requirements.txt`：框架运行所需要的jar包

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

`version:3.7`

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

## appium环境搭建

参考资料：`https://download.csdn.net/download/qq_39214101/12721006`

or进群下载：自动化测试-夜行者（816489363)

# 如何编写测试用例

下面详细说明如何添加一条用例，以登录界面演示

1. 在ActivityObject下Login_page模块新建一个页面元素yaml文件，Login_page.yaml

   字段说明：

   - desc：yaml文件说明
   - parameters：参数说明
   - elem_name：元素别名（你调用的时候需要使用）
   - desc：元素描述（例如用户输入框的名称）
   - data：里面是一个字典，元素定位方式，以及元素定位方式的取值

   ```yaml
   #封装需要操作的元素对象
   desc: "登录页面元素操作对象"
   parameters:
     - elem_name: "phone_number"
       desc: "请输入手机号"
       data: {
         method: "ANDROID_UIAUTOMATOR",
         value: 'new UiSelector().text("请输入手机号")'
       }
   
     - elem_name: "code"
       desc: "请输入验证码"
       data: {
         method: "ANDROID_UIAUTOMATOR",
         value: 'new UiSelector().text("请输入验证码")'
       }
   
     - elem_name: "login_btn"
       desc: "登录按钮"
       data: {
         method: "ANDROID_UIAUTOMATOR",
         value: 'new UiSelector().text("登录")'
       }
   
     - elem_name: "message_id"
       desc: "消息弹框信息"
       data: {
         method: "ID",
         value: "android:id/message"
       }
   ```

   

2. 在ActivityObject模块下的elem_params.py文件中进行Login_activity.yaml注册，生成一个yaml文件对象，初始化传递两个参数，一个是模块名，一个是yaml配置文件名

   ```yaml
   # 注册yaml文件对象
   class LoginActivityElem(ElemParams):
       def __init__(self):
           super(LoginActivityElem, self).__init__('Login_activity', 'Login_activity.yaml')
   ```

3. 在ActivityObject下Login_activity模块创建一个login_activity.py封装login页面操作元素，导入Login_activity.yaml文件对象，初始化，然后获取yaml文件中封装的元素，底层通过传入locator定位器（元组），进行页面元素操作

   ```python
   # !/user/bin/env python
   # -*- coding: utf-8 -*-
   from Base.base import Base
   from selenium import webdriver
   from ActivityObject.elemParams import LoginActivityElem
   
   
   # 封装车联网app登录页面操作对象操作方法
   class LoginActivity(Base):
       def __init__(self, driver):
           # 初始化页面元素对象，即yaml文件对象
           self.elem_locator = LoginActivityElem()
           # 初始化driver
           super().__init__(driver)
   
       def input_phone(self, value):
           elem = self.elem_locator.get_locator("phone_number")
           super().send_key(elem, value)
   
       def input_code(self, value):
           elem = self.elem_locator.get_locator("code")
           super().send_key(elem, value)
   
       def click_login_btn(self):
           elem = self.elem_locator.get_locator("login_btn")
           super().click_btn(elem)
   
       def get_message_value(self):
           elem = self.elem_locator.get_locator("message_id")
           return super().get_text(elem)
   
   
   if __name__ == "__main__":
       home_activity = LoginActivity(webdriver.Chrome())
   
   ```
   
4. 在TestCases下面新建一个包，例如Login模块，测试登录页面

5. 在Login下面创建一个conftest.py和test_loginActivityCase.py

   conftest.py中指定需要加载的测试页面对象，使用scope级别为function

   ```python
   # !/user/bin/env python
   # -*- coding: utf-8 -*-
   import pytest
   from ActivityObject.Login_activity.loginActivity import LoginActivity
   
   
   @pytest.fixture(scope="function")
   def login_activity_class_load(function_driver):
       login_activity = LoginActivity(function_driver)
       yield login_activity
   ```
   
   test_loginActivityCase.py中每个测试case需要调用页面模块conftest.py中的页面对象，以及全局配置conftest.py中function_driver，断言使用Base模块中的assert_method的AssertMethod，里面封装了断言方法，包含了allure断言失败截图等操作，根据不同的断言场景取用，或者自己再进行封装
   
   ```python
# !/user/bin/env python
   # -*- coding: utf-8 -*-
import pytest
   import allure
   import inspect
   import logging
   from Base.assertMethod import AssertMethod
   
   
   @allure.feature("TestLoginPageCase")
   class TestLoginPageCase:
   
       @allure.story("Login")
       @allure.severity("normal")
       @allure.description("测试登录")
       @allure.link("https://www.baidu.com", name="连接跳转百度")
       @allure.testcase("https://www.sina.com", name="测试用例位置")
       @allure.title("执行测试用例用于登录模块")
       def test_d1(self, login_activity_class_load, function_driver):
           logging.info("用例编号编码：{}".format(inspect.stack()[0][3]))
           login_activity_class_load.input_phone("18383398524")
           login_activity_class_load.input_code("123456")
           login_activity_class_load.click_login_btn()
           message_value = login_activity_class_load.get_message_value()
           AssertMethod.assert_equal_screen_shot(function_driver, (message_value, "用户不存在"))
   
       @allure.story("Login")
       @allure.severity("normal")
       @allure.description("测试登录")
       @allure.link("https://www.baidu.com", name="连接跳转百度")
       @allure.testcase("https://www.sina.com", name="测试用例位置")
       @allure.title("执行测试用例用于登录模块")
       def test_d2(self, login_activity_class_load, function_driver):
           logging.info("用例编号编码：{}".format(inspect.stack()[0][3]))
           login_activity_class_load.input_phone("18383398524")
           login_activity_class_load.input_code("123456")
           login_activity_class_load.click_login_btn()
           message_value = login_activity_class_load.get_message_value()
           AssertMethod.assert_equal_screen_shot(function_driver, (message_value, "用户存在"))
   
   
   if __name__ == "__main__":
       pytest.main(["test_loginActivityCase.py"])
   
   ```
   
6. 执行用例

   执行用例可以通过两种常用的方法进行

   1. pycharm中配置`test runner`为`pytest`，配置路径为`settings->Tools->Python Integrated Tools->Testing`；配置完成后就能够在打开测试用例文件后看到可执行的按钮了

   2. 在根目录下的`run.py`文件中运行，在pytest.ini中修改默认配置项，配置文件中配置了用例的目录扫描：TestCases，配置了addopts，其中需要配置--mobile_system，根据测试的手机系统进行设置，可选项为ios or android。--allure-features可以配置也可以不进行配置，配置allure标记的feature可以标记执行某一个feature，如果需要执行多个，不同feature之间以`,`号分割，如果需要执行全部，用`;`号注释allure-features这行即可。其他日志项根据自己实际需要启用，默认配置的是启用控制台输出日志，日志不输出日志文件，如果需要输出到日志文件，将log_file取消注释即可。

      ```python
      [pytest]
      testpaths = TestCases
      addopts = -s
                -q
                -v
          --mobile_system=android
                --allure-features TestLoginPageCase
                --alluredir=Report/android
                --clean-alluredir
      log_format = %(asctime)s %(levelname)s %(message)s
      log_level = INFO
      log_file_level = debug
      log_file_date_format = %Y-%m-%d %H:%M:%S
      log_file_format = %(asctime)s %(levelname)s %(message)s
      ;log_file = ./Logs/log.log
      log_cli = true
      log_cli_level = INFO
      log_cli_format = %(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)
      log_cli_date_format=%Y-%m-%d %H:%M:%S
      ```
      
      

