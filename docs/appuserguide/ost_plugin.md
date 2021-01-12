# OpenSourceTest 内置插件

OpenSourceTest内置插件用于处理OST的UI接口自动化中的driver，pytest新增控制台命令，用例优化，yaml文件定位等操作。在根目录的conftest.py中，导入了OST设置的三个方法ost_driver，ost_option，ost_collection_modifyitems

##  ost_option

用于将OST新增的pytest命令利用hook注入pytest脚手架中在ost_option中定义了三个参数：

- --browser：指定运行的浏览器，默认为chrome，可选firefox or chrome or ie
- --browser_opt：指定浏览器运行是否打开浏览器界面，默认为open，可选open or close
- --type_driver：执行是本地driver还是远程driver，默认是本地，可选local or remote，如果启用本地分布式和远程分布式，需要指定参数为remote



## ost_driver

用于处理ost_option携带的参数请求，处理https不同浏览器证书校验，处理不同浏览器请求，本地或远程driver请求，返回driver对象



## ost_collection_modifyitems

使用pytest的hook，处理测试用例中的中文乱码问题优化。