from core.api_util import api_util

def mobile_query(param):
    response = api_util.get_mobile_belong(params=param)
    return response.json()