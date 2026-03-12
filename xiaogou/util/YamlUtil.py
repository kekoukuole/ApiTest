import os

import yaml


class YamlUtil:
    def __init__(self):
        self.data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"yaml_data/")

    def write_extra_yaml(self, data):
        with open(self.data_path + "extract.yaml",mode="a",encoding="utf-8") as f:
            old_value = self.read_extract_yaml()
            if old_value:
                for key,value in data.items():
                    old_value[key] = value
                self.clear_extract()
                yaml.dump(data=data,stream=f,allow_unicode=True,sort_keys=False)
            else:
                yaml.dump(data=data,stream=f,allow_unicode=True,sort_keys=False)

    def read_extract_yaml(self):
        with open(self.data_path +"extract.yaml",mode="r",encoding="utf-8") as f:
            value = yaml.safe_load(f)
            return value

    def clear_extract(self):
        with open(self.data_path +"extract.yaml",mode="w",encoding="utf-8") as f:
            f.truncate()

if __name__ == '__main__':
    data = {"code":200}
    YamlUtil().write_extra_yaml(data)