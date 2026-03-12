import allure
from Assert_Util.Assertutil import AssertUtil
from request_two.request_two import RequestTwo
from logger.log_util import logger
from util.ExracUtil import ExtractUtil
from read.read import base_data


class ApiFirst:
    def __init__(self):
        self.session = RequestTwo()
        self.extract = ExtractUtil()

    def request_first(self,data_info):
        url = data_info["request_info"]["url"]
        method = data_info["request_info"]["method"]
        headers = data_info["request_info"]["headers"]
        allure_story = data_info["request_info"]["allure_story"]
        allure_title = data_info["request_info"]["allure_title"]
        allure.dynamic.story(allure_story)
        allure.dynamic.title(allure_title)
        case_info = data_info["login_data"]["json"]
        validate = data_info["validate"]
        extract = data_info["extract"]
        res = self.session.request_info(url=url,method=method,data=case_info)
        response = res.json()
        self.extract.extrect_data(response,extract)
        if res.status_code == 200:
            AssertUtil().validate_response(response, validate)
        else:
            logger.info("状态码错误,请检查")

    def data_token(self,data_info):
        token = base_data.read_token()
        url = data_info["request_info"]["url"]
        method = data_info["request_info"]["method"]
        headers = data_info["request_info"]["headers"]
        allure_story = data_info["request_info"]["allure_story"]
        allure_title = data_info["request_info"]["allure_title"]
        allure.dynamic.story(allure_story)
        allure.dynamic.title(allure_title)
        case_info = token
        validate = data_info["validate"]
        res = self.session.request_info(url=url, method=method, data=case_info)
        response = res.json()
        if res.status_code == 200:
            AssertUtil().validate_response(response, validate)
        else:
            logger.info("状态码错误,请检查")