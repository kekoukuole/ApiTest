import requests
from utils.log_util import logger

from utils.read import base_data

api_root_url = base_data.read_ini()["host"]["api_sit_url"]

class RestClient:
    def __init__(self):
        self.api_root_url = api_root_url

    def get(self,url,**kwargs):
        self.request(url,"GET",**kwargs)

    def post(self,url,**kwargs):
        self.request(url,"POST",**kwargs)

    def request(self, url, method, **kwargs):
        logger.info(f"接口请求地址>>>{self.api_root_url+url}")
        logger.info(f"接口请求方法>>>{method}")
        logger.info(f"接口请求参数>>>{kwargs['json']}")
        if method == "GET":
            return requests.get(self.api_root_url + url, **kwargs)
        if method == "POST":
            return requests.post(self.api_root_url + url, **kwargs)