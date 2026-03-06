import json

from core.ResuitBase import ResultResponse
from utils.log_util import logger


def process_response(response):
    if response.status_code in (200, 201):
        ResultResponse.success = True
        ResultResponse.body =response.json()
    else:
        ResultResponse.success = False
        logger.info("接口状态码不是2开头，请检查")
    logger.info("接口返回内容>>>" + json.dumps(response.json(), ensure_ascii=False))
    return ResultResponse