import allure

from core.rest_client_new import RestClient
from utils.AssertUtil import AssertUtil
from utils.ExtractUtil import ExtractUtil


class Apiservice:
    def __init__(self):
        self.session = RestClient()
        self.extract = ExtractUtil()

    def handle_case(self,data,login_token=None):
        #获取url
        url = self.extract.extrect_url(data["request_info"]["url"])
        # 获取method
        method = data["request_info"]["method"]
        # 获取headers
        headers = data["request_info"]["headers"]
        if login_token:
            headers.update(login_token)
        # 获取title
        allure_title = data["request_info"]["case_title"]
        allure.dynamic.title(allure_title)
        #获取case_info
        case_info = data["case_info"]
        #获取validate
        validate = case_info.pop("validate",None)
        #获取extract
        extract = case_info.pop("extract",None)
        res = self.session.do_request(url=url,method=method,headers=headers,**case_info)
        # 写入yaml
        self.extract.extrect_data(res,extract)
        #断言逻辑
        AssertUtil().validate_response(res,validate)
        return res