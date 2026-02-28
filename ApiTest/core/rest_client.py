import requests

from utils.read import base_data

api_root_url = base_data.read_ini()["host"]["api_sit_url"]

class RestClient:
    def __init__(self):
        self.api_root_url = api_root_url

    def get(self,url,**kwargs):
        return requests.get(self.api_root_url + url,**kwargs)

    def post(self,url,**kwargs):
        return requests.post(self.api_root_url + url,**kwargs)