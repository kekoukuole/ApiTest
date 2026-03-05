import allure
import pytest
from utils.read import base_data
from api.user_api import register, send_code, login, add_shopping_cart, add_message, add_shopping_cart2, add_message2
from testcases.conftest import get_data
from testcases.usercenter.conftest import get_code, delete_user, delete_code, get_shop_cart_num

@allure.feature("用户中心模块")
class TestUser:
    mobile = None

    @allure.story("用户注册后登陆")
    @allure.title("注册手机号测试用例")
    def test_register(self):
        json_data = get_data()["test_register"]
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

    @pytest.mark.parametrize("username,password",get_data()["user_login"])
    @allure.story("用户登陆")
    @allure.title("用户手机号登陆")
    def test_login(self,username,password):
        TestUser.mobile = username
        result = login(username,password)
        assert result.success is True
        assert result.body["token"] is not None

    @allure.story("购物车相关")
    @allure.title("加购物车")
    def test_shopping_cart(self,login_fixture):
        #登陆接口
        token = login_fixture[0]
        username = login_fixture[1]
        param = get_data()["shopping_cart"]
        result = add_shopping_cart(param,token)
        #查询购物车数量
        num = get_shop_cart_num(username,param["goods"])
        assert result.success is True
        assert result.body["nums"] == num

    @allure.story("购物车相关")
    @allure.title("加购物车")
    def test_shopping_cart2(self, login_fixture):
        # 登陆接口
        token = login_fixture[0]
        username = login_fixture[1]
        param = get_data()["shopping_cart"]
        result = add_shopping_cart(param, token)
        # 查询购物车数量
        num = get_shop_cart_num(username, param["goods"])
        assert result.success is True
        assert result.body["nums"] == num

    def test_add_message(self,login_fixture):
        token = login_fixture[0]
        data = get_data()["add_message"]
        files = base_data.read_file()
        result = add_message(data,token,files)
        assert result.success is True
        assert result.body['subject'] == data['subject']

    @allure.story("购物车相关")
    @allure.title("加购物车")
    def test_shopping_cart3(self, login_token):
        # 登陆接口
        param = get_data()["shopping_cart"]
        result = add_shopping_cart2(param, login_token)
        # 查询购物车数量
        num = get_shop_cart_num(TestUser.mobile, param["goods"])
        assert result.success is True
        assert result.body["nums"] == num

    def test_add_message2(self, login_token):
        data = get_data()["add_message"]
        files = base_data.read_file()
        result = add_message2(data, login_token, files)
        assert result.success is True
        assert result.body['subject'] == data['subject']










