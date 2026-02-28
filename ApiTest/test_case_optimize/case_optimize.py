import pytest
import requests

from api.api import mobile_query
from utils.read import base_data

url = base_data.read_ini()["host"]["api_sit_url"]
def test_mobile():
    param = base_data.read_data()["mobile_belong"]
    result = mobile_query(param)
    assert result["status"] == 0
    assert result["msg"] == "ok"