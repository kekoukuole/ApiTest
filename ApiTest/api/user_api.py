from core.api_util import api_util
from utils.response_util import process_response


def send_code(json_data):
    """
    获取短信验证码
    :param json_data:
    :return:
    """
    response = api_util.get_code(json=json_data)
    return process_response(response)

def register(code,mobile):
    """
    注册接口
    :param code:
    :param mobile:
    :return:
    """
    json_data = {
        "code": str(code),
        "password": "123456",
        "username": str(mobile)
    }
    response = api_util.register_mobile(json=json_data)
    return process_response(response)
