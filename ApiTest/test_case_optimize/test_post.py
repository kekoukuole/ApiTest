from api.api import mobile_query
from utils.read import base_data

def test_post():
    param = base_data.read_data()['mobile_belong']
    result = mobile_query(param)
    assert result["status"] == 0
    assert result["msg"] == "ok"