import allure
from Assert_Util.Assertutil import AssertUtil
from request_two.request_two import RequestTwo


class ApiFirst:
    def __init__(self):
        self.session = RequestTwo()

    def request_first(self,json):
        url = json["request_info"]["url"]
        method = json["request_info"]["method"]
        headers = json["request_info"]["headers"]
        allure_story = json["request_info"]["allure_story"]
        allure_title = json["request_info"]["allure_title"]
        allure.dynamic.story(allure_story)
        allure.dynamic.title(allure_title)
        case_info = json["login_data"]
        validate = case_info.pop("validate",None)

        res = self.session.requests_info(url=url,method=method,**case_info)
        AssertUtil().validate_response(res,validate)