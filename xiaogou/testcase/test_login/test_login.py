import pytest

from api_first.Api_First import ApiFirst
from read.read import base_data



class TestLogin:
    @pytest.mark.parametrize("data",base_data.read_yaml()["login"])
    def test_login(self,data):
        ApiFirst().request_first(data)


    @pytest.mark.parametrize("data",base_data.read_yaml()["system"])
    def test_system(self,data):
        ApiFirst().data_token(data)