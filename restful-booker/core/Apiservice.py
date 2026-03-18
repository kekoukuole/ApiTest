import allure

from resquest.resquest_client import RequentClient
from AssertUtil.AssertUtil import AssertUtil
from logger.log_util import logger

class Apiservice:
    def __init__(self):
        self.session = RequentClient()

    def handle_case(self,data):
        #获取allure
        allure_story = data["request_info"]["allure_story"]
        allure_title = data["request_info"]["allure_title"]
        allure.dynamic.story(allure_story)
        allure.dynamic.title(allure_title)
        #获取url
        url = data["request_info"]["url"]
        #获取请求方法
        method = data["request_info"]["method"]
        #获取请求参数
        json_data = data["case_info"]["json"]
        #获取断言
        validate = data["validate"]
        response = self.session.requests(url = url,method=method,data=json_data)
        res = response.json()
        if response.status_code == 200 or 201:
            AssertUtil().validate_response(res,validate)
        else:
            logger.info("状态码错误")