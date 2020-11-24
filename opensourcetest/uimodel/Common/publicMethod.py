import random
import hashlib
import string
import sys
import yaml
import os
import time
import logging
import docker
import xlrd
import allure
from hashlib import md5
from Common.fileOption import FileOption


class PubMethod:

    @staticmethod
    def get_rand_num(min=10, max=200, type=1):
        """
        获取随机数
        :param min:最小值
        :param max: 最大值
        :param type: 类型，1为浮点型，2为布尔值，0为整型
        :return:
        """
        value = random.uniform(min, max)
        if type == 1:
            return float(round(value, 1))
        elif type == 0:
            return int(value)
        elif type == 2:
            return random.randint(0, 1)

    @staticmethod
    def transfer_md5(msg):
        hl = md5()
        hl.update(msg.encode('utf-8'))
        return hl.hexdigest().upper()

    @staticmethod
    def read_yaml(file):
        """
            读取yaml文件，返回文件对象
        @param file:
        @return:
        """
        if os.path.isfile(file):
            fr = open(file, 'r', encoding='utf-8')
            yaml_info = yaml.safe_load(fr)
            fr.close()
            return yaml_info
        else:
            logging.error(file, '文件不存在')
            sys.exit()

    @staticmethod
    def random_string(strings=string.ascii_letters, length=15):
        """
        获取随机字符串
        @param strings:
        @param length:
        @return:
        """
        values = ''.join(random.choices(strings, k=length))
        return values

    @staticmethod
    def get_file_md5(file_path):
        """
        获取文件的md5
        @param file_path:
        @return:
        """
        with open(file_path, 'rb') as f:
            md5_obj = hashlib.md5()
            md5_obj.update(f.read())
            hash_code = md5_obj.hexdigest()
            file_md5 = str(hash_code).lower()
        return file_md5

    @staticmethod
    def read_excel(file_path):
        wb = xlrd.open_workbook(filename=file_path, encoding_override='utf-8')  # 打开文件
        sheet1 = wb.sheet_by_index(0)  # 通过索引获取表格
        return sheet1

    @staticmethod
    def create_file(file_path):
        """
        创建文件，当目录不存在时自动创建
        :param file_path:
        :return:
        """
        dir_path = os.path.split(file_path)[0]
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        if not os.path.isfile(file_path):
            f = open(file_path, mode='w', encoding='utf-8')
            f.close()

    @staticmethod
    def create_dirs(file_dir):
        """
        创建文件路径,先判断目录是否存在
        :param file_dir:
        :return:
        """
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

    @staticmethod
    def screen_picture(driver):
        """
        截图操作
        @return:
        """
        try:
            logging.info("正在进行截图操作：")
            picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            file_path = "Report/picture"
            file_name = picture_time + ".png"
            FileOption.file_mkdir(file_path)
            res = driver.get_screenshot_as_file(file_path + '/' + file_name)
            picture_url = file_path + '/' + file_name
            allure.attach.file(picture_url, attachment_type=allure.attachment_type.PNG)
            logging.info("截图成功，picture_url为：{}".format(picture_url))
        except Exception as e:
            logging.error("截图失败，错误信息为：{}".format(e))
        finally:
            return picture_url

    @staticmethod
    def create_docker_hub_container(base_url, image, name, ports):
        """
        创建selenium的hub节点
        @param base_url:
        @param image:
        @param name:
        @param ports:
        @return:
        """
        client = docker.DockerClient(base_url=base_url)
        try:
            client.containers.run(
                image=image,
                detach=True,
                tty=True,
                stdin_open=True,
                restart_policy={'Name': 'always'},
                name=name,
                ports=ports,
                privileged=True
            )
        except Exception as e:
            print("创建容器失败，错误信息：{}".format(e))

    @staticmethod
    def create_docker_node_container(base_url, image, name, ports, links):
        """
        在docker中创建selenium的node节点
        @param base_url: docker的URL
        @param image: 镜像
        @param name: 命名
        @param ports: 端口
        @param links: 连接
        @return:
        """
        client = docker.DockerClient(base_url=base_url)
        try:
            client.containers.run(
                image=image,
                detach=True,
                tty=True,
                stdin_open=True,
                restart_policy={'Name': 'always'},
                name=name,
                ports=ports,
                links=links,
                privileged=True
            )
        except Exception as e:
            print("创建容器失败，错误信息：{}".format(e))
