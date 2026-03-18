import configparser
import os.path

import yaml


class Filedata:
    def __init__(self):
        self.yaml_data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"yaml_data/")
        self.ini_data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"data_ini","data.ini")

    def read_ini(self):
        config = configparser.ConfigParser()
        if not os.path.exists(self.ini_data_path):
            raise FileNotFoundError(f"INI 文件不存在：{self.ini_data_path}")
        try:
            config.read(self.ini_data_path, encoding="utf-8")
        except Exception as e:
            raise  RuntimeError(f"读取 INI 文件失败：{e}")
        return config

    def read_yaml(self,yaml_name,key_name=None):
        try:
            with open(self.yaml_data_path + yaml_name, mode="r",encoding="utf-8") as f:
                data = yaml.safe_load(f)
                if key_name:
                    return data[key_name]
        except Exception as e:
            raise FileNotFoundError(f"读取异常：{e}")
        return data

base_data = Filedata()


if __name__ == '__main__':
    data1 = base_data.read_ini()["host"]["api_url"]
    data2 = base_data.read_yaml("login.yaml","login")
    print(data1)
    print(data2)




