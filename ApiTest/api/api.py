from core.api_util import api_util

def mobile_query(param):
    response = api_util.get_mobile_belong(params=param)
    return response.json()

def data_json(json_data):
    response = api_util.post_data(json=json_data)
    return response.json()