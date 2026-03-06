from core.rest_client_new import RestClient
from utils.AssertUtil import AssertUtil

class Apiservice:
    def __init__(self):
        self.session = RestClient()


    def handle_case(self,data):
        #获取url
        url = data["request_info"]["url"]
        # 获取method
        method = data["request_info"]["method"]
        # 获取headers
        headers = data["request_info"]["headers"]

        #获取case_info
        case_info = data["case_info"]
        #获取validate
        validate = case_info.pop("validate",None)
        res = self.session.do_request(url=url,method=method,headers=headers,**case_info)
        #断言逻辑
        AssertUtil().validate_response(res,validate)
        return res