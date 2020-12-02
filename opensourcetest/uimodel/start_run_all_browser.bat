::启动三个浏览器，进行分布式测试，前置条件：执行start_server.bat脚本，启动hub以及三个node节点
::批量启动selenium-server-standalone服务
@echo off
start /D "LocalSeleniumServer/selenium_run_script" run_by_chrome.bat
start /D "LocalSeleniumServer/selenium_run_script" run_by_firefox.bat
start /D "LocalSeleniumServer/selenium_run_script" run_by_ie.bat