# !/user/bin/env python
# -*- coding: utf-8 -*-
import os
from loguru import logger
from opensourcetest.builtin.baseUiRunner import ost_ui_cmd_runner, ost_ui_runner

if __name__ == "__main__":
    browser = ost_ui_runner("chrome", "close", "local")
    url = 'Local Test Report Address:http://127.0.0.1:63342/'+os.getcwd().split("\\")[-1]+f'/Report/{browser.replace(" ", "_")}/allure-report/index.html'
    logger.info(url)

