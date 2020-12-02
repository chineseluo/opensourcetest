# 运行测试用例

测试脚本书写完毕后，直接执行run.py文件即可运行所有测试用例。

OpenSourceTest支持所有pytest运行用例的方式来运行用例，可以通过命令行，也可以通过pytest.main()，可以指定测试用例运行的颗粒度等等。**PS：在运行用例之前，请先配置好您对应的浏览器驱动**

**OST提供了两种方法用于用例执行：**

1、ost_ui_runner

导入ost_ui_runner，参数说明：

-  @param browser:传入浏览器，chrome/firefox/ie
- @param browser_opt: 浏览器操作，是否开启浏览器操作窗口，关闭操作窗口效率更高，open or close
- @param type_driver:驱动类型，是本地driver还是远程driver，local or remote，启用本地和远程driver需要在Conf模块的sconfig.yaml中配置selenium_hub_url

~~~python
# !/user/bin/env python
# -*- coding: utf-8 -*-
import os
from loguru import logger
from opensourcetest.builtin.baseUiRunner import ost_ui_runner

if __name__ == "__main__":
    browser = ost_ui_runner("chrome", "close", "local")
    url = 'Local Test Report Address:http://127.0.0.1:63342/'+os.getcwd().split("\\")[-1]+f'/Report/{browser.replace(" ", "_")}/allure-report/index.html '
    logger.info(url)
~~~

2、ost_ui_cmd_runner

导入ost_ui_cmd_runner，用于从控制台执行脚本文件，控制台传递参数说明

-  @param browser:传入浏览器，chrome/firefox/ie
- @param browser_opt: 浏览器操作，是否开启浏览器操作窗口，关闭操作窗口效率更高，open or close
- @param type_driver:驱动类型，是本地driver还是远程driver，local or remote，启用本地和远程driver需要在Conf模块的sconfig.yaml中配置selenium_hub_url

~~~python
# !/user/bin/env python
# -*- coding: utf-8 -*-
import os
from loguru import logger
from opensourcetest.builtin.baseUiRunner import ost_ui_cmd_runner

if __name__ == "__main__":
    browser = ost_ui_cmd_runner()
    url = 'Local Test Report Address:http://127.0.0.1:63342/'+os.getcwd().split("\\")[-1]+f'/Report/{browser.replace(" ", "_")}/allure-report/index.html '
    logger.info(url)
~~~

