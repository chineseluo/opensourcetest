# OpenSourceTest 内置插件

OpenSourceTest内置插件用于处理OST中的请求，断言检查，yaml文件定位等操作。



## start_run_case

requestEngine的start_run_case参数说明：

- params_object：必填，yaml接口文件对象
- params_mark：必填，yaml文件的定位方式，支持str和int两种定位方式，str定位根据yaml中的desc来进行，int根据yaml中的相同数据结构的索引进行（PS：索引从0开始）
- checker：断言器，支持列表和元组，或者元组列表嵌套的方式
- session_connection：用于保持客户端与服务端的连接，传递token/cookie，或者其他header，以字典的形式传入
- url_converter：url转换器，用于替换接口中的$符号，可以通过在yaml的具体某个接口中使用$代替url中的某些需要通过动态获取的参数，然后使用url_converter在脚本中进行替换，支持str/tuple/list（PS：替换的参数必须和yaml中该接口的$个数一一对应）

- 其他参数的传递通原始requests中的参数要求。