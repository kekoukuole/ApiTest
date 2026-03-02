import allure
import pytest

from api.api import mobile_query
from utils.read import base_data

url = base_data.read_ini()["host"]["api_sit_url"]

@allure.epic("数据进制项目epic")
@allure.feature("手机号模块features")
class Testmobile:
    @allure.story("北京的手机号story")
    @allure.title("测试手机号归属地title")
    @allure.testcase("https://www.baidu.com",name="接口地址testcase")
    @allure.issue("htps://www.baidu.com",name="缺陷地址issue")
    @allure.link("htps://www.baidu.com",name="链接地址link")
    @allure.description("当前手机号是13456755448，归属地是北京的description")
    @allure.step("第一步，第二步，第三步。。。")
    @allure.severity(severity_level="blocker")
    def test_mobile(self):
        param = base_data.read_data()["mobile_belong"]
        result = mobile_query(param)
        assert result.body["status"] == 0
        assert result.body["msg"] == "ok"
        assert result.body["result"]["shouji"] == "13456755448"

    # @allure.story("北京的手机号story2")
    # @allure.title("测试手机号归属地title")
    @allure.testcase("https://www.baidu.com", name="接口地址testcase")
    @allure.issue("htps://www.baidu.com", name="缺陷地址issue")
    @allure.description("当前手机号是13456755448，归属地是北京的description")
    @allure.step("第一步，第二步，第三步。。。")
    @allure.severity(severity_level="blocker")
    def test_mobile2(self):
        param = base_data.read_data()["mobile_belong_dynamic"]["params"]
        title = base_data.read_data()["mobile_belong_dynamic"]["title"]
        story = base_data.read_data()["mobile_belong_dynamic"]["story"]
        allure.dynamic.story(title)
        allure.dynamic.title(story)
        result = mobile_query(param)
        assert result.body["status"] == 0
        assert result.body["msg"] == "ok"
        assert result.body["result"]["shouji"] == "13456755448"


if __name__ == "__main__":
    pytest.main([__file__])