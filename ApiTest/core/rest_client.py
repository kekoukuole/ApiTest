import json

import requests
from utils.log_util import logger

from utils.read import base_data

api_root_url = base_data.read_ini()["host"]["api_sit_url"]

class RestClient:
    def __init__(self):
        self.api_root_url = api_root_url

    def get(self,url,**kwargs):
        return self.request(url,"GET",**kwargs)

    def post(self,url,**kwargs):
        return self.request(url,"POST",**kwargs)

    def put(self, url, **kwargs):
        return self.request(url, "PUT", **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, "DELETE", **kwargs)

    def request(self, url, method, **kwargs):
        self.request_log(url,method,**kwargs)
        if method == "GET":
            return requests.get(self.api_root_url+url, **kwargs)
        if method == "POST":
            return requests.post(self.api_root_url+url, **kwargs)
        if method == "PUT":
            return requests.put(self.api_root_url+url, **kwargs)
        if method == "DELETE":
            return requests.delete(self.api_root_url+url, **kwargs)

    def request_log(self, url, method, **kwargs):
        data = dict(**kwargs).get("data")
        json_data = dict(**kwargs).get("json")
        params = dict(**kwargs).get("params")
        headers = dict(**kwargs).get("headers")
        logger.info(f"接口请求地址>>>{self.api_root_url + url}")
        logger.info(f"接口请求方法>>>{method}")
        if data is not None:
            logger.info(f"接口请求data参数>>>\n{json.dumps(data, indent=2,ensure_ascii=False)}")
        if json_data is not None:
            logger.info(f"接口请求json参数>>>\n{json.dumps(json_data, indent=2,ensure_ascii=False)}")
        if params is not None:
            logger.info(f"接口请求params参数>>>\n{json.dumps(params, indent=2,ensure_ascii=False)}")
        if headers is not None:
            logger.info(f"接口请求headers参数>>>\n{json.dumps(headers, indent=2,ensure_ascii=False)}")
