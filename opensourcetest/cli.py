#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : opensourcetest
@Time    : 2020/10/13 14:01
@Auth    : chineseluo
@Email   : 848257135@qq.com
@File    : cli.py
@IDE     : PyCharm
------------------------------------
"""
import os
from loguru import logger
import sys
import argparse
from .scaffold import create_scaffold
from opensourcetest import __version__, __description__


def init_http_scaffold_parser(subparsers):
    sub__http_scaffold_parser = subparsers.add_parser(
        "start_http_project", help="Create a new http interface project with template structure."
    )
    sub__http_scaffold_parser.add_argument(
        "project_name", type=str, nargs="?", help="Specify new http interface project name."
    )
    return sub__http_scaffold_parser


def init_ui_scaffold_parser(subparsers):
    sub_ui_scaffold_parser = subparsers.add_parser(
        "start_ui_project", help="Create a new ui project with template structure."
    )
    sub_ui_scaffold_parser.add_argument(
        "project_name", type=str, nargs="?", help="Specify new ui project name."
    )
    return sub_ui_scaffold_parser


def init_app_scaffold_parser(subparsers):
    sub_app_scaffold_parser = subparsers.add_parser(
        "start_app_project", help="Create a new app project with template structure."
    )
    sub_app_scaffold_parser.add_argument(
        "project_name", type=str, nargs="?", help="Specify new app project name."
    )
    return sub_app_scaffold_parser


def init_docs_scaffold_parser(subparsers):
    sub_docs_scaffold_parser = subparsers.add_parser(
        "onlinedocs", help="Welcome to the online documentation:http://docs.opensourcetest.cn"
    )
    return sub_docs_scaffold_parser


def main():
    # Generate subcommand object
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument("-v", "-V", "--version", "--Version", dest="version", action="store_true", help="show version")
    subparsers = parser.add_subparsers(help="OpenSourceTest sub-command help")
    sub_http_scaffold_parser = init_http_scaffold_parser(subparsers)
    sub_ui_scaffold_parser = init_ui_scaffold_parser(subparsers)
    sub_app_scaffold_parser = init_app_scaffold_parser(subparsers)
    sub_docs_scaffold_parser = init_docs_scaffold_parser(subparsers)
    ost_argv = sys.argv
    print(ost_argv)
    if len(ost_argv) == 1:
        parser.print_help()
        sys.exit()
    elif len(ost_argv) == 2:
        if ost_argv[1] in ["-V", "-v", "--Version", "--version"]:
            print(f"""
             +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +++ +-+ +++ +-+ +++ +-+ +++ +-+
             | O | | p | | e | | n | | S | | o | | u | | r | | c | | e | | T | | e | | s | | t |
             +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +++ +-+ +++ +-+ +++ +-+ +++ +-+
            """)
            logger.info(f"The OpenSourceTest version is {__version__}")
        elif ost_argv[1] in ["-h", "-H", "--help", "--Help"]:
            parser.print_help()
        elif ost_argv[1] == "start_http_project":
            sub_http_scaffold_parser.print_help()
        elif ost_argv[1] == "start_ui_project":
            sub_ui_scaffold_parser.print_help()
        elif ost_argv[1] == "start_app_project":
            sub_app_scaffold_parser.print_help()
        elif ost_argv[1] == "onlinedocs":
            sub_docs_scaffold_parser.print_help()
            logger.info("Welcome to the online documentation:http://docs.opensourcetest.cn")
        else:
            print("Please use OST - h to view help information")
        sys.exit(0)
    elif len(sys.argv) == 3 and sys.argv[1] == "start_http_project" and sys.argv[2] in ["-h", "-H", "--help", "--Help"]:
        logger.info("Please follow OST start_http_project with the project file name!")
        sys.exit(0)
    elif len(sys.argv) == 3 and sys.argv[1] == "start_ui_project" and sys.argv[2] in ["-h", "-H", "--help", "--Help"]:
        logger.info("Please follow OST start_ui_project with the project file name!")
        sys.exit(0)
    elif len(sys.argv) == 3 and sys.argv[1] == "start_http_project":
        create_scaffold(sys.argv[1], sys.argv[2])
        sys.exit(0)
    elif len(sys.argv) == 3 and sys.argv[1] == "start_ui_project":
        create_scaffold(sys.argv[1], sys.argv[2])
        sys.exit(0)
    elif len(sys.argv) == 3 and sys.argv[1] == "start_app_project":
        create_scaffold(sys.argv[1], sys.argv[2])
        sys.exit(0)


if __name__ == "__main__":
    print(f"""
                +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +++ +-+ +++ +-+ +++ +-+ +++ +-+
                | O | | p | | e | | n | | S | | o | | u | | r | | c | | e | | T | | e | | s | | t |
                +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +++ +-+ +++ +-+ +++ +-+ +++ +-+
               """)
    logger.info(f"The OpenSourceTest version is {__version__}")
