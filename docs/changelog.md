# 发布 历史

## V0.1.0(2020-10-30)

**项目创建**

- 创建opensourcetest外部CLI框架
- 创建核心opensourcetest http interface框架
- 修改响应模型
- 优化接口数据处理

**待修改项**

- request请求模型修改优化

## V0.2.0(2020-11-25)

**新增功能**

- 创建核心opensourcetest ui 框架
- 优化ui操作模型
- yaml文件对象注入优化
- 修复截图断言功能
- 添加UI自动化本地分布式bat脚本

## V0.2.2(2020-12-21)

**新增功能**

- checker中新增七种内置断言
- 接口框架内baseAssert新增七种断言

**修改项**

- requestEngine中start_run_case返回response对象字典
- 取用OSTReqRespData需要调用内置ostHttp的ost_http_runner

~~~python
from opensourcetest.builtin.ostHttp import ost_http_runner
~~~

**待修改项**

- 项目路径出现小写的“opensourcetest”开头的文件，运行时读取yaml会读取系统本身自带的login.yaml文件

## V0.3.0（2020-12-31）

- 新增APP模板创建功能
- UI自动化底层优化

## V0.3.1（2020-1-7）

- 修复接口自动化框架中控制台显示json.dumps乱码问题

## V0.3.2（2020-1-17）

- 修复底层baseRequest中底层方法入参异常问题
- 修复url_replace入参为int类型异常
- 新增底层interface优化

## V0.3.3（2020-1-27）

- 修复httpmodel、uimodel、appmodel中，pytest控制台命令执行失效问题
- 修复httpmodel中verfiy=False时，控制台日志warning警告
- 修复uimodel中PO对象注入重复，代码冗余问题
- 优化控制台日志过多问题，修改日志级别，需要详细控制台日志信息，请将pytest.ini文件中的日志级别调整为debug

**可选需求**

- OST 日志国际化，提供中英文两种日志格式的输出，计划V0.4.0版本
- OST 对于yaml参数做内层拼接，计划V0.4.0版本

