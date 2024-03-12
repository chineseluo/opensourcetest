# 脚手架

`OST`为您提供了脚手架，用来创建UI自动化基础框架



## 帮助

OST -h：查看OpenSourceTest帮助说明（使用时：[-h|-H|--help|--Help]等价）

## 创建新项目

OST在创建项目的过程中，您只需要指定项目名称即可（警告：请勿在创建项目的路径中出现opensourcetest，会创建失败）。

OST start_app_project -h：查看创建APP自动化项目时的帮助说明（使用时：[-h|-H|--help|--Help]等价）

OST start_app_project [project_name]：创建APP自动化项目，[project_name]自定义

如果您指定的项目名称已经存在，则会收到警告。

## 运行脚手架项目

脚手架在创建项目后，会提供一个简单的demo给您，您可以执行run.py文件可以运行测试。

## 项目结构

![OST2](\images\UI\OST2.png)