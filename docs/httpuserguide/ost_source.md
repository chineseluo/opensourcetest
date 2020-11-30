# OpenSourceTest 请求响应资源

这一部分介绍OpenSourceTest的几个资源对象，便于大家集成，或者二次开发。



## OSTReqRespData

底层封装了两个model:

- OSTReqData：响应request
- OSTRespData：响应response

OSTReqData对象：

~~~python
class OSTReqData(BaseModel):
    """OST Response.Request Model"""
    method: MethodEnum = MethodEnum.GET
    url: Url
    headers: Headers = {}
    cookies: Cookies = {}
    body: Union[Text, bytes, Dict, List, None] = {}
~~~



OSTRespData对象：

~~~python
class OSTRespData(BaseModel):
    """OST Response.Response Model"""
    status_code: int
    headers: Dict
    cookies: Cookies = {}
    encoding: Union[Text, None] = None
    content_type: Text
    body: Union[Dict, Text, bytes]
~~~

调用方式：

在Base包下的requestEngine.py中提供了start_run_case方法，返回了一个请求响应对象ost_req_resp，可以根据自己的需要对返回值进行处理。返回示例如下：

~~~json
================== OSTReqData details ==================
method   : GET
url      : https://www.cnblogs.com/chineseluo/ajax/blogSubscription
headers  : {
    "User-Agent": "python-requests/2.22.0",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "*/*",
    "Connection": "keep-alive",
    "Content-Type": "application/json; charset=utf-8"
}
cookies  : {}
body     : None
================== OSTRespData details ==================
status_code : 200
headers  : {
    "Date": "Fri, 20 Nov 2020 09:39:04 GMT",
    "Content-Type": "application/json; charset=utf-8",
    "Transfer-Encoding": "chunked",
    "Connection": "keep-alive",
    "Strict-Transport-Security": "max-age=2592000; includeSubDomains; preload"
}
cookies  : {}
encoding : utf-8
content_type : application/json; charset=utf-8
body     : {
    "isAuthenticated": false
}
~~~



## OSTReqArgv

requests请求参数对象model，预留一个model在start_run_case中，按需取用:

~~~python
class OSTReqArgv(BaseModel):
    """OST Request model"""
    method: MethodEnum = MethodEnum.GET
    part_url: Url
    params: Dict[Text, Text] = {}
    req_json: Union[Dict, List, Text] = Field(None, alias="json")
    req_data: Union[Text, Dict[Text, Any]] = Field(None, alias="data")
    headers: Headers = {}
    cookies: Cookies = {}
    upload: Dict = Field({}, alias="files")
    auth: Optional[Tuple[Text]]
    timeout: float = 1200
    allow_redirects: bool = True
    proxies: Dict = None
    verify: Verify = False
    stream: bool = True
    cert: Union[Text, Tuple[Text, Text], None]
~~~

