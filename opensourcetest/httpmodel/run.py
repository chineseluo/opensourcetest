#!/user/bin/env python
# -*- coding: utf-8 -*-
import os
import pytest
from loguru import logger

if __name__ == '__main__':
    pytest.main()
    # Generate assure Report
    cmd = 'allure generate Report/allure-results -o Report/allure-report -c'
    os.system(cmd)
    logger.info("Local Test Report Address:http://127.0.0.1:63342/" + os.getcwd().split("\\")[-1]+"/Report/allure"
                                                                                                  "-report/index.html")
