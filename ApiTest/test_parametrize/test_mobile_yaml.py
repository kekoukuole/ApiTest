import pytest
import requests
from utils.read_ini import read_ini
from utils.read_data import get_data

url = read_ini()["host"]["api_sit_url"]
def test_mobile():
    param = get_data["mobile_belong"]
    r = requests.get(url=url + "/sell/shouji/query",
                     params={'appkey':param["appkey"],'shouji':param["shouji"]})
    print(r.status_code)

@pytest.mark.parametrize("appkey,shouji",get_data["mobile_belong_2"])
def test_mobile2(appkey,shouji):
    r = requests.post(url=url + "/sell/shouji/query",
                      params={'appkey':appkey,'shouji':shouji})
    print(r.status_code)