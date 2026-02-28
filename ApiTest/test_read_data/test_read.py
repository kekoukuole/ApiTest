import pytest
import requests
from utils.read import base_data

url = base_data.read_ini()["host"]["api_sit_url"]
def test_mobile():
    param = base_data.read_data()["mobile_belong"]
    r = requests.get(url= url + "/sell/shouji/query",
                     params={'appkey':param["appkey"],'shouji':param["shouji"]})
    print(r.status_code)
    assert r.status_code == 200

# @pytest.mark.parametrize("appkey,shouji",get_data["mobile_belong_2"])
# def test_mobile2(appkey,shouji):
#     r = requests.post(url=url + "/sell/shouji/query",
#                       params={'appkey':appkey,'shouji':shouji})
#     print(r.status_code)