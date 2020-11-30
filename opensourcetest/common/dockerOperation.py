#!/user/bin/env python
# -*- coding: utf-8 -*-
import logging
import docker


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
        logging.error(f"Failed to create container with error message:{e}")


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
        logging.error(f"Failed to create container with error message:{e}")
