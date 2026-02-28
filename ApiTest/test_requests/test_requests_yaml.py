import pytest
import requests

from utils.read_data import get_data

def test_mobile():
    param = get_data["mobile_belong"]
    r = requests.get(url="http://sellshop.5istudy.online/sell/shouji/query",
                     params={'appkey':param["appkey"],'shouji':param["shouji"]})
    print(r.status_code)

@pytest.mark.parametrize("appkey,shouji",get_data["mobile_belong_2"])
def test_mobile2(appkey,shouji):
    r = requests.post(url="http://sellshop.5istudy.online/sell/shouji/query",
                      params={'appkey':appkey,'shouji':shouji})
    print(r.status_code)