import pytest

from core.Apiservice import Apiservice
from read.read_file import base_data


class TestLogin:

    @pytest.mark.parametrize("data", base_data.read_yaml("login.yaml","login"))
    def test_login(self,data):
        Apiservice().handle_case(data)