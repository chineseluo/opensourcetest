::批量启动selenium-server-standalone服务
@echo off
start  /D "LocalSeleniumServer/selenium_server_script" selenium_server_hub.bat
start  /D "LocalSeleniumServer/selenium_server_script" selenium_server_node1.bat
start  /D "LocalSeleniumServer/selenium_server_script" selenium_server_node2.bat
start  /D "LocalSeleniumServer/selenium_server_script" selenium_server_node3.bat