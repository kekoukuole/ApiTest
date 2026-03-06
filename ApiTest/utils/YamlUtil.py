import os

import yaml


class YamlUtil:
    def __init__(self):
        self.data_path = data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"data/")

    def read_testcase_yaml(self,yaml_name,key_name=None):
        with open(self.data_path +yaml_name,mode="r",encoding="utf-8") as f:
            value = yaml.safe_load(f)
            if key_name:
                return value[key_name]
            return value

if __name__ == '__main__':
    data = YamlUtil().read_testcase_yaml("user_center.yaml")
    print(data)