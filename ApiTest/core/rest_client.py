import requests

from utils.read import base_data

api_root_url = base_data.read_ini()["host"]["api_sit_url"]


def get(url,params,**kwargs):
    return requests.get(api_root_url + url,params,**kwargs)