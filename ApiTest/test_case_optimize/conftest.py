import pytest
from utils.log_util import logger

@pytest.fixture(scope="function",autouse=True)
def func():
    logger.info("开始执行测试用例")
    yield
    logger.info("测试用例执行完毕")