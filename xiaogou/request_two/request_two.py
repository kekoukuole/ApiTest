import json
import requests
from read.read import base_data
from logger.log_util import logger

host_url = base_data.read_ini()["host"]["api_sit_url"]

class RequestTwo:
    def __init__(self):
        self.session = requests.Session()
        self.host_url = host_url

    # def get(self,url,**kwargs):
    #     return self.request(host_url + url,"GET",**kwargs)
    #
    # def post(self,url,**kwargs):
    #     return self.request(host_url + url,"POST",**kwargs)

    def request(self,url,method,**kwargs):
        self.logger(url,method,**kwargs)
        if method == "GET":
            return self.session.get(self.host_url+url,**kwargs)
        elif method == "POST":
            return self.session.post(self.host_url+url,**kwargs)

    def request_info(self,url,method,**kwargs):
        response = self.request(url, method, **kwargs)
        res = response.json()
        logger.info(f"接口返回内容>>>\n{json.dumps(res, indent=2, ensure_ascii=False)}")
        return response

    def logger(self,url,method,**kwargs):
        data = dict(**kwargs).get("data")
        json_data = dict(**kwargs).get("json")
        params = dict(**kwargs).get("params")
        headers = dict(**kwargs).get("headers")
        logger.info(f"接口请求地址>>>{self.host_url+ url}")
        logger.info(f"接口请求方法>>>{method}")
        if data is not None:
            logger.info(f"接口请求data参数>>>\n{json.dumps(data, indent=2, ensure_ascii=False)}")
        if json_data is not None:
            logger.info(f"接口请求json参数>>>\n{json.dumps(json_data, indent=2, ensure_ascii=False)}")
        if params is not None:
            logger.info(f"接口请求params参数>>>\n{json.dumps(params, indent=2, ensure_ascii=False)}")
        if headers is not None:
            logger.info(f"接口请求headers参数>>>\n{json.dumps(headers, indent=2, ensure_ascii=False)}")

