# coding:utf-8
import time
import os
import logging
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from opensourcetest.common.yamlOperation import YamlFileOption

ROOT_PATH = os.path.abspath(os.path.dirname(__file__)).split('Base')[0]
CONF_PATH = os.path.join(ROOT_PATH, "Conf/config.yaml")


# Base layer encapsulates the operation method of elements
def get_login_url_from_config():
    """

    @return: 配置文件URL
    """
    config_info = YamlFileOption().read_yaml(CONF_PATH)
    logging.info(config_info["test_info"]["test_URL"])
    return config_info["test_info"]["test_URL"]


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.poll_frequency = 0.5

    def get_url(self, url):
        """

        @param url: 测试url
        """
        try:
            self.driver.get(url)
            logging.info(f"Get URL successfully:{url}")
        except Exception as e:
            logging.error(f"URL acquisition failed with error message is:{e}")

    def login_by_config_url(self):
        """
            登录URL
        """
        self.driver.maximize_window()
        self.driver.get(get_login_url_from_config())
        if self.driver.name == "internet explorer":
            logging.info("The UI automation test of IE browser is in progress, and the function of skipping HTTP "
                         "security verification is enabled")
            try:
                self.skip_ie_https_check(self.driver)
            except Exception as e:
                logging.info("The HTTPS certificate of the website is normal, and it is not necessary to skip")

    def find_element(self, locator):
        """
        :param locator: 传入定位器参数locator=(By.XX,"value")
        :return: 返回元素对象
        """
        logging.info("Output locator information:{}".format(locator))
        if not isinstance(locator, tuple):
            logging.error(f"find_element：locator Parameter type error,Must pass on the type of Tuple：locator=(By.XX,"
                          f"value),The error parameter is:{locator}")
        else:
            logging.info(
                f"find_element：Locating element information,The positioning mode is:{locator[0]},value:{locator[1]}")
            try:
                time.sleep(0.5)
                elem = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
                    lambda x: x.find_element(*locator))
                logging.info(f"Successfully located element, element object is:{elem}")
                return elem
            except Exception as e:
                logging.warning(f"Failed to locate element with error message:{e}")
                return False

    def find_elements(self, locator):
        """
        :param locator: 传入定位器参数locator=(By.XX,"value")
        :return: 返回元素对象列表
        """
        logging.info("输出定位器信息：{}".format(locator))
        if not isinstance(locator, tuple):
            logging.error(f"Find_element：locator Parameter type error,Must pass on the type of Tuple：locator=(By.XX,"
                          f"value),The error parameter is:{locator}")
        else:
            logging.info(
                f"Find_element：Locating element information,The positioning mode is:{locator[0]},value:{locator[1]}")
            try:
                time.sleep(1)
                elems = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
                    lambda x: x.find_elements(*locator))
                logging.info(f"Successfully located element, element object is:{elems}")
                return elems
            except Exception as e:
                logging.warning(f"Failed to locate element with error message:{e}")
                return []

    def switch_to_frame(self, locator):
        """
        :param locator: 传入定位器参数locator=(By.XX,"value")
        :return:
        """
        elem = self.find_element(locator)
        try:
            self.driver.switch_to.frame(elem)
            logging.info("Frame switched successfully")
        except Exception as e:
            logging.error(f"Frame switch failed. The error message is:{e}")

    def switch_to_handle(self, index):
        """
            切换窗口句柄
        """
        # 获取当前所有窗口句柄
        try:
            handles = self.driver.window_handles
            logging.info(f"The list of handle objects is as follows:{handles}")
        except Exception as e:
            logging.error(f"Failed to get all current window handles. The error message is:{e}")
        # 切换到新窗口句柄
        try:
            self.driver.switch_to.window(handles[index])
            logging.info(f"Switch the new window handle successfully. The index of the switch window is:{index}")
        except Exception as e:
            logging.error(f"Switching new window handle failed with error message:{e}")

    def send_key(self, locator, value):
        """

        @param locator: 定位器
        @param value: value
        """
        elem = self.find_element(locator)
        try:
            elem.send_keys(value)
            logging.info(f"Element object input value succeeded,value is:{value}")
        except Exception as e:
            logging.error(f"Element object input failed with error message:{e}")

    def click_btn(self, locator):
        """

        @param locator: 定位器
        """
        elem = self.find_element(locator)
        try:
            elem.click()
            logging.info("Element object click succeeded")
        except Exception as e:
            logging.error(f"Failed to click the element object. The error message is:{e}")

    def get_text(self, locator):
        """

        @param locator:定位器
        @return:元素文本值
        """
        elem_text = None
        elem = self.find_element(locator)
        try:
            elem_text = elem.text
        except Exception as e:
            logging.error(f"Failed to get the element text. The error message is:{e}")
        logging.info(f"The element text value is:{elem_text}")
        return elem_text

    def get_all_text_by_elements(self, locator):
        elems_text = []
        elems = self.find_elements(locator)
        try:
            for item in elems:
                elems_text.append(item.text)
            logging.info(
                f"The value of getting the list of element group objects was successful, and the value is:{elems_text}")
        except Exception as e:
            logging.error(f"Failed to get the element group object. The failure information is::{e}")
        return elems_text

    def get_one_text_by_elements(self, locator, index):
        """

        @param locator: 定位器
        @return: 返回定位对象组的第一个元素的值
        """
        elem_text = None
        elem = self.find_elements(locator)
        try:
            elem_text = elem[index].text
            logging.info(
                f"Get element group object, the value of index position {index} succeeded, the value is:{elem_text}")
        except Exception as e:
            logging.error(
                f"Failed to get the value of index position {index} of element group object. The failure information is:{e}")
        return elem_text

    def get_placeholder(self, locator):
        """

        @param locator: 定位器
        @return: 返回placeholder属性值
        """
        elem_placeholder_text = None
        elem = self.find_element(locator)
        try:
            elem_placeholder_text = elem.get_attribute("placeholder")
            logging.info(
                f"This element object get the placeholder successful,placeholder values:{elem_placeholder_text}")
        except Exception as e:
            logging.error(f"This element object get the placeholder failed,The error message is:{e}")
        return elem_placeholder_text

    def get_attribute_by_value(self, locator, attribute_value):
        """
        通过传入定位器locator和属性名称attribute_value可以获得属性值
        @param locator: 定位器
        @param attribute_value: 需要获取的元素属性名称
        @return: 该元素属性值
        """
        elem_attribute_text = None
        elem = self.find_element(locator)
        try:
            elem_attribute_text = elem.get_attribute(attribute_value)
            logging.info(
                f"The element object get {attribute_value} successful,{attribute_value} values is:{elem_attribute_text}")
        except Exception as e:
            logging.error(f"This element object get the {attribute_value} failed,The error message is:{e}")
        return elem_attribute_text

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

    def move_mouse_to_element(self, locator):
        """
        移动鼠标到某个元素上面
        @param locator:
        @return:
        """
        elem = self.find_element(locator)
        action = ActionChains(self.driver)
        action.move_to_element(elem).perform()

    def clear_input_value(self, locator):
        """
        清除输入框中的内容
        @param locator:
        @return:
        """
        elem = self.find_element(locator)
        elem.send_keys(Keys.CONTROL, "a")
        elem.send_keys(Keys.DELETE)

    def get_value(self, locator):
        """
        获取输入框的value
        @param locator:
        @return:
        """
        elem = self.find_element(locator)
        return elem.get_attribute("value")

    def double_click_elem(self, locator):
        """
        双击元素
        @param locator:
        @return:
        """
        elem = self.find_element(locator)
        ActionChains(self.driver).double_click(elem).perform()

    def elem_is_display(self, locator):
        """
        判断元素在页面是否显示，显示返回True,不显示返回false
        @param locator:
        @return:
        """
        elem = self.find_element(locator)
        return elem.is_displayed()

    def elem_is_selected(self, locator):
        """
        判断元素是否被选中，用于多选框，如果多选框被选中状态，返回True，否则返回False
        @param locator:
        @return:
        """
        elem = self.find_element(locator)
        return elem.is_selected()

    def elem_is_enable(self, locator):
        """
        判断页面元素是否可用
        @param locator:
        @return:
        """
        elem = self.find_element(locator)
        logging.info(f"Element status:{elem.is_enabled()}")
        return elem.is_enabled()

    def choose_select_by_value(self, locator, value):
        """
        根据内置属性value值值选择下拉输入框
        @param locator:
        @param value:
        @return:
        """
        elem = self.find_element(locator)
        Select(elem).select_by_value(value)

    def choose_select_by_index(self, locator, index):
        """
        根据索引选择下拉框
        @param locator:
        @param index:
        @return:
        """
        elem = self.find_element(locator)
        Select(elem).select_by_index(index)

    def choose_select_by_visible_value(self, locator, value):
        """
        根据下拉选项的文本值选择下拉框
        @param locator:
        @param value:
        @return:
        """
        elem = self.find_element(locator)
        Select(elem).select_by_visible_text(value)

    def choose_elem_by_visible_value(self, locator, value):
        """
        根据一组元素对象中某一个元素对象的文本值确定，哪一个元素对象
        @param locator:
        @param value:
        @return: 单个元素对象
        """
        elems = self.find_elements(locator)
        for item in elems:
            if self.elem_object_get_text(item) == value:
                logging.info(f"The element objects that meet the filter criteria is:{item}")
                return item

    def elem_object_click(self, elem):
        """
        元素点击，传入参数为元素对象
        @param elem:
        @return:
        """
        logging.info(f"The element objects that execute the click event are:{elem}")
        try:
            elem.click()
        except Exception as e:
            logging.error(f"Failed to click the element. The error message is:{e}")

    def elem_object_get_text(self, elem):
        """
        元素对象获取text值，传入元素对象
        @param elem:
        @return:
        """
        elem_text = elem.text
        return elem_text

    def skip_ie_https_check(self, driver):
        """
        通过执行js脚本跳过ie的https安全信息校验
        @param driver:
        @return:
        """
        js = "javascript:document.getElementById('overridelink').click();"
        driver.execute_script(js)

    def refresh_web_page(self):
        """
        Refresh web page
        @return:
        """
        self.driver.refresh()


if __name__ == "__main__":
    ...
