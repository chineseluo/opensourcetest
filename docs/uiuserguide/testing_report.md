# 测试报告

OpenSourceTest完美兼容pytest本身，以及其第三方插件。这意味着，您在使用OpenSourceTest进行测试时，可以自定义的配置任何自己想要使用的插件，以及报告，只要第三方插件本身是可用的。OpenSourceTest提供了allure报告的常用初始配置，您直接使用即可。

# allure测试报告

allure-pytest是OpenSourceTest的必选依赖项，不需要单独安装插件。

我们在pytest.ini文件中指定了alluredir的测试json文件生成地址

~~~ini
[pytest]
addopts = --aluredir=Report/allure-results
~~~

指定了清理alluredir的内容数据

~~~ini
[pytest]
addopts = --clean-alluredir
~~~

如果不需要将pytest获取的日志附加到报告中，可以在addopts后追加--allure-no-capture

~~~ini
[pytest]
addopts = --allure-no-capture
~~~

在框架的入口run.py中，指定了allure读取allure-result和生成allure-report的路径

~~~ini
cmd = 'allure generate Report/allure-results -o Report/allure-report -c'
~~~

测试执行结束后，控制台会输出本地静态访问地址

~~~verilog
2020-11-17 20:15:23.664 | INFO     | __main__:<module>:23 - Local Test Report Address:http://127.0.0.1:63342/model/Report/allure-report/index.html
~~~

如果有其他allure测试报告的相关问题，请参考[`allure-pytest`](https://docs.qameta.io/allure/#_pytest)

## pytes-html测试报告

pytest-html是OpenSourceTest的必选依赖项，不需要单独安装插件。

如果您想使用pytest-html作为测试报告输出，可以在pytest.ini中指定--html的生成路径

~~~ini
[pytest]
addopts = --html=report.html
~~~

如果有其他pytest-html测试报告的相关问题，请参考[`pytest-html`](https://pypi.org/project/pytest-html/)

