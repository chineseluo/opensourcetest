#!/user/bin/env python
# -*- coding: utf-8 -*-
import os
import pytest
from loguru import logger

if __name__ == '__main__':
    TEST_STATUS_CODE = pytest.main()  # 测试执行结果状态码
    # Generate assure Report
    cmd = 'allure generate Report/allure-results -o Report/allure-report -c'
    os.system(cmd)
    logger.info("Local Test Report Address:http://127.0.0.1:63342/" + os.getcwd().split("\\")[-1]+"/Report/allure"
                                                                                           "-report/index.html")
    logger.info(f"测试用例集执行结果状态码TEST_STATUS_CODE:{TEST_STATUS_CODE}")
    if TEST_STATUS_CODE != 0:
        raise Exception("测试用例集执行异常，请检查对应代码！！！")

