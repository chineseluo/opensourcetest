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

