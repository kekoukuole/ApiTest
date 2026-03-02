import json

from core.api_util import api_util
from utils.log_util import logger
from utils.response_util import process_response


def mobile_query(param):
    response = api_util.get_mobile_belong(params=param)
    result = process_response(response)
    return result

def data_json(json_data):
    response = api_util.post_data(json=json_data)
    process_response(response)
    return response.json()