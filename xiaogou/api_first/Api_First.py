import allure
from Assert_Util.Assertutil import AssertUtil
from request_two.request_two import RequestTwo
from logger.log_util import logger


class ApiFirst:
    def __init__(self):
        self.session = RequestTwo()

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
        res = self.session.request_info(url=url,method=method,data=case_info)
        if res.status_code == 200:
            response = res.json()
            AssertUtil().validate_response(response, validate)
        else:
            logger.info("状态码错误,请检查")