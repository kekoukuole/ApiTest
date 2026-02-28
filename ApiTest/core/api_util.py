from core.rest_client import get


def get_mobile_belong(params,**kwargs):
    return get("/sell/shouji/query",params,**kwargs)