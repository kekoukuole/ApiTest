from api.api import data_json
from utils.read import base_data
from utils.log_util import logger


def test_post():
    logger.info("开始执行test_post方法")
    json_data = base_data.read_data()['json_data']
    result = data_json(json_data)
    assert result["id"] == 101
    logger.info("用例执行完毕")
