from read.read import base_data

yaml_file = base_data.read_yaml()["login"]

class TestLogin:
    def __init__(self):
        self.yaml_file = yaml_file

    def test_login(self):
        ApiFirst().request_first(self.yaml_file)