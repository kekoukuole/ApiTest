import allure
import pytest

from api.goods_api import get_banner
from core.ApiService import Apiservice
from testcases.goodscenter.conftest import banner_num
from utils.YamlUtil import YamlUtil


@allure.feature("用户中心模块")
class TestGoods:
    @allure.story("首页展示内容")
    @allure.title("banner")
    def test_banner(self, banner_num):
        result = get_banner()
        assert result.success is True
        assert len(result.body) == banner_num

    @pytest.mark.parametrize("data",YamlUtil().extract_case("goods_center.yaml","get_banner"))
    def test_goods_new(self,data):
        Apiservice().handle_case(data)
