# 运行测试用例

测试脚本书写完毕后，直接执行run.py文件即可运行所有测试用例。

OpenSourceTest支持所有pytest运行用例的方式来运行用例，可以通过命令行，也可以通过pytest.main()，可以指定测试用例运行的颗粒度等等。**PS：在运行用例之前，请先配置好[appium运行环境](`https://download.csdn.net/download/qq_39214101/12721006`)**

**OST提供了两种方法用于用例执行：**

1、ost_app_runner

导入ost_app_runner，参数说明：

-  @param mobile_system:传入手机操作系统，android/ios

~~~python
# !/user/bin/env python
# -*- coding: utf-8 -*-
import os
from loguru import logger
from opensourcetest.builtin.baseAppRunner import ost_app_runner, ost_app_cmd_runner


if __name__ == "__main__":
    mobile_system = ost_app_runner("android")
    url = 'Local Test Report Address:http://127.0.0.1:63342/'+os.getcwd().split("\\")[-1]+f'/Report/{mobile_system.replace(" ", "_")}/allure-report/index.html '
    logger.info(url)
~~~

2、ost_app_cmd_runner

导入ost_app_cmd_runner，用于从控制台执行脚本文件，控制台传递参数说明

-  @param mobile_system:传入手机操作系统，android/ios

~~~python
# !/user/bin/env python
# -*- coding: utf-8 -*-
import os
from loguru import logger
from opensourcetest.builtin.baseAppRunner import ost_app_runner, ost_app_cmd_runner


if __name__ == "__main__":
    mobile_system = ost_app_cmd_runner()
    url = 'Local Test Report Address:http://127.0.0.1:63342/'+os.getcwd().split("\\")[-1]+f'/Report/{mobile_system.replace(" ", "_")}/allure-report/index.html '
    logger.info(url)
~~~

