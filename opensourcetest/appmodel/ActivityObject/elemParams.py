# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 21:11
# @Author  : chineseluo
# @Email   : 848257135@qq.com
# @File    : run.py
# @Software: PyCharm

import os
from Common.publicMethod import PubMethod
import logging
from selenium.webdriver.common.by import By
from Base.baseBy import BaseBy
from opensourcetest.builtin.models import OSTAppBaseBy, AppUiLocateMethodEnum

pub_api = PubMethod()
root_dir = os.path.dirname(os.path.dirname(__file__))
config_path = os.path.join(root_dir, 'ActivityObject')
config_path = os.path.abspath(config_path)


class ElemParams:
    def __init__(self, dir_name, file_name, root_dir_name=config_path):
        self.elem_name = []
        self.desc = []
        self.data = []
        self.info = []
        self.__run(dir_name, root_dir_name, file_name)

    def __run(self, dir_name, root_dir_name, file_name):
        config_dir_name = os.path.join(root_dir_name, dir_name)
        file_path = os.path.abspath(os.path.join(config_dir_name, file_name))
        try:

            self.info = PubMethod().read_yaml(file_path)['parameters']
            for i in self.info:
                self.elem_name.append(i['elem_name'])
                self.desc.append(i['desc'])
                self.data.append(i['data'])
        except Exception as e:
            logging.error("文件解析失败！{},文件路径：{}".format(e, file_path))

    def get_locator(self, elem_name):
        """

        @param page_elem_class:传入页面元素对象
        @param elem_name:传入自定义的元素名称
        @return:
        """
        page_obj_elem = self.info
        elems_info = page_obj_elem
        for item in elems_info:
            if item["elem_name"] == elem_name:
                method = item["data"]["method"]
                value = item["data"]["value"]
                logging.info("元素名称为：{}，元素定位方式为：{}，元素对象值为：{}".format(elem_name, method, value))
                if method == AppUiLocateMethodEnum.ID and value is not None:
                    elem_locator = (OSTAppBaseBy.ID, value)
                    return elem_locator
                elif method == AppUiLocateMethodEnum.XPATH and value is not None:
                    elem_locator = (OSTAppBaseBy.XPATH, value)
                    return elem_locator
                elif method == AppUiLocateMethodEnum.LINK_TEXT and value is not None:
                    elem_locator = (OSTAppBaseBy.LINK_TEXT, value)
                    return elem_locator
                elif method == AppUiLocateMethodEnum.PARTIAL_LINK_TEXT and value is not None:
                    elem_locator = (OSTAppBaseBy.PARTIAL_LINK_TEXT, value)
                    return elem_locator
                elif method == AppUiLocateMethodEnum.NAME and value is not None:
                    elem_locator = (OSTAppBaseBy.NAME, value)
                    return elem_locator
                elif method == AppUiLocateMethodEnum.TAG_NAME and value is not None:
                    elem_locator = (OSTAppBaseBy.TAG_NAME, value)
                    return elem_locator
                elif method == AppUiLocateMethodEnum.CLASS_NAME and value is not None:
                    elem_locator = (OSTAppBaseBy.CLASS_NAME, value)
                    return elem_locator
                elif method == AppUiLocateMethodEnum.CSS_SELECTOR and value is not None:
                    elem_locator = (OSTAppBaseBy.CSS_SELECTOR, value)
                    return elem_locator
                elif method == AppUiLocateMethodEnum.IOS_UIAUTOMATION and value is not None:
                    elem_locator = (OSTAppBaseBy.IOS_UIAUTOMATION, value)
                    return elem_locator
                elif method == AppUiLocateMethodEnum.IOS_PREDICATE and value is not None:
                    elem_locator = (OSTAppBaseBy.IOS_PREDICATE, value)
                    return elem_locator
                elif method == AppUiLocateMethodEnum.IOS_CLASS_CHAIN and value is not None:
                    elem_locator = (OSTAppBaseBy.IOS_CLASS_CHAIN, value)
                    return elem_locator
                elif method == AppUiLocateMethodEnum.ANDROID_UIAUTOMATOR and value is not None:
                    elem_locator = (OSTAppBaseBy.ANDROID_UIAUTOMATOR, value)
                    return elem_locator
                elif method == AppUiLocateMethodEnum.ANDROID_VIEWTAG and value is not None:
                    elem_locator = (OSTAppBaseBy.ANDROID_VIEWTAG, value)
                    return elem_locator
                elif method == AppUiLocateMethodEnum.WINDOWS_UI_AUTOMATION and value is not None:
                    elem_locator = (OSTAppBaseBy.WINDOWS_UI_AUTOMATION, value)
                    return elem_locator
                elif method == AppUiLocateMethodEnum.ACCESSIBILITY_ID and value is not None:
                    elem_locator = (OSTAppBaseBy.ACCESSIBILITY_ID, value)
                    return elem_locator
                elif method == AppUiLocateMethodEnum.IMAGE and value is not None:
                    elem_locator = (OSTAppBaseBy.IMAGE, value)
                    return elem_locator
                elif method == AppUiLocateMethodEnum.CUSTOM and value is not None:
                    elem_locator = (OSTAppBaseBy.CUSTOM, value)
                    return elem_locator
                else:
                    logging.error("元素名称：{}，此元素定位方式异常，定位元素值异常，请检查！！！".format(elem_name))


# 注册yaml文件对象
class LoginActivityElem(ElemParams):
    def __init__(self):
        super(LoginActivityElem, self).__init__('Login_activity', 'Login_activity.yaml')


if __name__ == '__main__':
    login_activity = LoginActivityElem()
    print(login_activity.get_locator("phone_number"))
