import allure
import pytest

from core.ApiService import Apiservice
from utils.YamlUtil import YamlUtil


@allure.feature("用户订单模块")
class TestOrder:
    @pytest.mark.parametrize("data",YamlUtil().extract_case("order_center.yaml","order_list"))
    def test_order_list(self,data,login_token):
        Apiservice().handle_case(data,login_token)

    @pytest.mark.parametrize("data", YamlUtil().extract_case("order_center.yaml", "order_detail"))
    def test_order_detail(self, data, login_token):
        Apiservice().handle_case(data, login_token)

