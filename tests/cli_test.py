#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : opensourcetest
@Time    : 2020/11/12 15:01
@Auth    : chineseluo
@Email   : 848257135@qq.com
@File    : cli_test.py
@IDE     : PyCharm
------------------------------------
"""
import os
import sys
import unittest
from opensourcetest.cli import main


class TestCli(unittest.TestCase):

    def test_show_version(self):
        sys.argv = ["OST", "-V"]
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 0)

    def test_show_help(self):
        sys.argv = ["OST", "-h"]
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 0)

    def test_show_create_http_project(self):
        sys.argv = ["OST", "start_http_project"]
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 0)

    def test_show_create_ui_project(self):
        sys.argv = ["OST", "start_ui_project"]
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 0)

    def test_show_create_app_project(self):
        sys.argv = ["OST", "start_app_project"]
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 0)

    def test_show_online_docs_address(self):
        sys.argv = ["OST", "onlinedocs"]
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 0)
