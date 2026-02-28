from core.api_util import get_mobile_belong
from core.rest_client import get

def mobile_query(param):
    r = get_mobile_belong(params=param)
    print(r.status_code)
    result = r.json()
    return result