# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 21:11
# @Author  : chineseluo
# @Email   : 848257135@qq.com
# @File    : run.py
# @Software: PyCharm
import random
import string
import sys
import yaml
import os
import time
import logging
import docker
import allure
from Common.fileOption import File_option


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
        values = ''.join(random.choices(strings, k=length))
        return values

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
            File_option.file_mkdir(file_path)
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
        创建hub,docker容器
        :param base_url:docker 地址：端口
        :param image: 镜像名称
        :param name: 容器别名
        :param ports: 映射端口
        :param links: 连接
        :return:
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
        创建node,docker容器
        :param base_url:docker 地址：端口
        :param image: 镜像名称
        :param name: 容器别名
        :param ports: 映射端口
        :param links: 连接
        :return:
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
