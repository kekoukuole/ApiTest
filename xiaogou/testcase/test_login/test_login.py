from api_first.Api_First import ApiFirst
from read.read import base_data



class TestLogin:

    def test_login(self):
        yaml_file = base_data.read_yaml()["login"]
        ApiFirst().request_first(yaml_file)