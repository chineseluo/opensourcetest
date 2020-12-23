# !/user/bin/env python
# -*- coding: utf-8 -*-
import os
from loguru import logger
from opensourcetest.builtin.baseAppRunner import ost_app_runner, ost_app_cmd_runner


if __name__ == "__main__":
    mobile_system = ost_app_runner("android")
    url = 'Local Test Report Address:http://127.0.0.1:63342/'+os.getcwd().split("\\")[-1]+f'/Report/{mobile_system.replace(" ", "_")}/allure-report/index.html '
    logger.info(url)
