import json

import requests
from read.read_file import base_data
from logger.log_util import logger

api_host_path = base_data.read_ini()["host"]["api_url"]

class RequentClient:
    def __init__(self):
        self.session = requests.Session()
        self.api_host_path = api_host_path

    def judge_method(self,url,method,**kwargs):
        self.logger(url,method,**kwargs)
        if method == "GET":
            return self.session.get(self.api_host_path + url,**kwargs)
        elif method == "POST":
            return self.session.post(self.api_host_path + url,**kwargs)

    def requests(self,url,method,**kwargs):
        response = self.judge_method(url,method,**kwargs)
        res = response.json()
        logger.info(f"接口返回内容>>>\n{json.dumps(res, indent=2, ensure_ascii=False)}")
        return response

    def logger(self,url,method,**kwargs):
        data = dict(**kwargs).get("data")
        json_data = dict(**kwargs).get("json")
        params = dict(**kwargs).get("params")
        headers = dict(**kwargs).get("headers")
        logger.info(f"接口请求地址>>>{self.api_host_path + url}")
        logger.info(f"接口请求方法>>>{method}")
        if data is not None:
            logger.info(f"接口请求data参数>>>\n{json.dumps(data, indent=2, ensure_ascii=False)}")
        if json_data is not None:
            logger.info(f"接口请求json参数>>>\n{json.dumps(json_data, indent=2, ensure_ascii=False)}")
        if params is not None:
            logger.info(f"接口请求params参数>>>\n{json.dumps(params, indent=2, ensure_ascii=False)}")
        if headers is not None:
            logger.info(f"接口请求headers参数>>>\n{json.dumps(headers, indent=2, ensure_ascii=False)}")