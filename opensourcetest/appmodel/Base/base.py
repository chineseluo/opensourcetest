#!/user/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
import logging
from appium.webdriver.extensions.search_context import AndroidSearchContext


# Base层封装的是元素的操作方法
class Base:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.poll_frequency = 0.5

    def find_element(self, locator):
        logging.info("输出定位器信息：{}".format(locator))
        """
        :param locator: 传入定位器参数locator=(By.XX,"value")
        :return: 返回元素对象
        """
        if not isinstance(locator, tuple):
            logging.error('locator参数类型错误，必须传元祖类型：locator=(By.XX,"value")')
        else:
            logging.info("正在定位元素信息：定位方式->%s,value值->%s" % (locator[0], locator[1]))
            try:
                elem = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
                    lambda x: x.find_element(*locator))
                logging.info("元素对象为：{}".format(elem))
                return elem
            except Exception as e:
                logging.error("定位不到元素，错误信息为:{}".format(e))
                return "定位不到元素"

    def find_elements(self, locator):
        """
        :param locator: 传入定位器参数locator=(By.XX,"value")
        :return: 返回元素对象列表
        """
        try:
            elems = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
                lambda x: x.find_elements(*locator))
            logging.info("元素组对象为：{}".format(elems))
        except Exception as e:
            logging.error("元素组对象获取失败，错误信息为：{}".format(e))
        return elems

    def switch_to_frame(self, locator):
        """
        :param locator: 传入定位器参数locator=(By.XX,"value")
        :return:
        """
        elem = self.find_element(locator)
        try:
            self.driver.switch_to.frame(elem)
            logging.info("frame切换成功")
        except Exception as e:
            logging.error("frame切换失败，错误信息为：{}".format(e))

    def send_key(self, locator, value):
        """

        @param locator: 定位器
        @param value: value
        """
        elem = self.find_element(locator)
        try:
            elem.send_keys(value)
            logging.info("元素对象输入值成功，值为：{}".format(value))
        except Exception as e:
            logging.error("元素对象输入值失败，错误信息为：{}".format(e))

    def click_btn(self, locator):
        """

        @param locator: 定位器
        """
        elem = self.find_element(locator)
        try:
            elem.click()
            logging.info("元素对象点击成功")
        except Exception as e:
            logging.error("元素对象点击失败，错误信息为：{}".format(e))

    def get_text(self, locator):
        """

        @param locator:定位器
        @return:元素文本值
        """
        elem = self.find_element(locator)
        try:
            elem_text = elem.text
            logging.info("元素text值：{}".format(elem_text))
        except Exception as e:
            logging.error("元素text获取失败，错误信息为：{}".format(e))
        return elem_text

    def get_text_by_elements(self, locator, index):
        """

        @param locator: 定位器
        @return: 返回定位对象组的第一个元素的值
        """
        elem = self.find_elements(locator)
        try:
            elem_text = elem[index].text
            logging.info("获取元素组对象，索引位置{}的值获取成功，值为：{}".format(index, elem_text))
        except Exception as e:
            logging.error("获取元素组对象，索引位置{}的值获取失败，失败信息为：{}".format(index, e))
        return elem_text

    def get_placeholder(self, locator):
        """

        @param locator: 定位器
        @return: 返回placeholder属性值
        """
        elem = self.find_element(locator)
        try:
            elem_placeholder_text = elem.get_attribute("placeholder")
            logging.info("该元素对象获取placeholder成功，placeholder值为：{}".format(elem_placeholder_text))
        except Exception as e:
            logging.error("该元素对象获取placeholder失败，错误信息为：{}".format(e))
        return elem_placeholder_text

    def check_select_is_existence(self, locator):
        """

        @param locator: 定位器
        @return: 返回TRUE、FALSE
        """
        try:
            elem = self.find_element(locator)
            return True
        except Exception as e:
            return False


if __name__ == "__main__":
    pass
