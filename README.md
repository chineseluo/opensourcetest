# **OpenSourceTest**

# [![pyversions](https://img.shields.io/badge/opensourcetest-v0.3.x-green)](https://pypi.org/project/opensourcetest/)[![pyversions](https://img.shields.io/badge/pypi-v0.3.x-orange)](https://pypi.org/project/opensourcetest-test-test/)[![pyversions](https://img.shields.io/badge/pytest-5.x-green)](https://docs.pytest.org)[![pyversions](https://img.shields.io/badge/requests-2.x-green)](http://docs.python-requests.org/en/master/ )[![pyversions](https://img.shields.io/badge/allure-2.x-green)](https://docs.qameta.io/allure/  )

`OpenSourceTest`将为您创建更加自由的软件自动化测试，不是为了简单而简单，而是为您提供更自由的可扩展的，适用于不同功能场景的`UI`自动化、APP自动化或接口自动化测试框架。

## **设计思想**

- 不丢弃轮子本身的优秀特性
- 不过度封装
- 提供更加多的可操作对象给使用者，即时你使用基本框架已经满足需求
- 拥抱开源

## **主要特点**

### 支持创建`UI`自动化测试框架

- 以[`yaml`][yaml]格式定义`UI`元素对象，[`yaml`][yaml]对象自动注入
- 支持本地及远程分布式测试
- 支持生成不同浏览器测试报告
- 支持docker容器测试

### 支持创建接口自动化测试框架

- 继承 [`requests`][requests]的所有强大功能
- 以[`yaml`][yaml]格式定义接口，[`yaml`][yaml]对象自动注入
- 使用[`jmespath`][jmespath]提取和验证[`json`][json]响应

### 支持创建APP自动化框架

- 以[`yaml`][yaml]格式定义`UI`元素对象，[`yaml`][yaml]对象自动注入

### 其他

- 完美兼容[`pytest`][pytest]，您可以使用您想使用的任何[`pytest`][pytest]格式
- 完美兼容[`allure`][allure]，您可以使用您想使用的任何[`allure`][allure]命令
- 支持**CLI**命令，直接创建您所需要的项目架构

## **OST计划**

**即将上线微服务架构运维命令自动化测试框架CLI_TEST，基于云原生基础组件的测试框架，敬请期待，满足在集群内部的组件自动化测试，哈哈哈哈**

![OST](/docs/images/OST.png)

## **打赏支持**

**OpenSourceTest由来自中国的成都-阿木木在空闲时间维护。虽然我致力于OpenSourceTest，因为我热爱这个项目，但是如果可能的话，希望可以得到一杯咖啡的打赏支持，您的打赏是我最大的支持。我会将打赏的胖友名单放入赞助者列表中，用以表示感谢。**

​	**这些钱也将被用来维护框架，购买服务器，以及直播公开课等活动**

​	**感谢各位胖友对OpenSourceTest框架的打赏，您的打赏支持是我最大的迭代更新的动力，也希望opensourcetest可以在日常工作中帮助到您，QAQ**

​	**成为打赏者[become a sponsor](/docs/sponsors.md)**

​	**联系作者：[成都-阿木木](mailto:848257135@qq.com)**

**微信赞赏收款码**

<img src="/docs/images/sponsors/wei.png" height="400" width="400" />



## **OpenSourceTest 社区**

欢迎测试小伙伴加群，讨论测试框架技术！

<img src="/docs/images/community.jpg"/>


[json]: http://json.com/
[yaml]: http://www.yaml.org/
[requests]: http://docs.python-requests.org/en/master/
[pytest]: https://docs.pytest.org/
[pydantic]: https://pydantic-docs.helpmanual.io/
[jmespath]: https://jmespath.org/
[allure]: https://docs.qameta.io/allure/