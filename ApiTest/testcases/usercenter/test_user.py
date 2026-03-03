import allure
from api.user_api import register,send_code
from testcases.usercenter.conftest import get_code, delete_user, delete_code
from utils.read import base_data


@allure.feature("用户中心模块")
class TestUser:
    @allure.story("用户注册后登陆")
    @allure.title("注册手机号测试用例")
    def test_register(self):
        json_data = base_data.read_data()["test_register"]
        #删除验证码
        delete_code(json_data["mobile"])
        #发送验证码
        result = send_code(json_data)
        assert result.success is True
        #获取短信验证码
        mobile = result.body["mobile"]
        code = get_code(mobile)
        #注册
        register_result = register(code,mobile)
        assert register_result.success is True
        #删除用户
        delete_user(mobile)