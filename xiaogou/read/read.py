import os
import configparser

import yaml

cofig_data = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"config","settings.ini")
yaml_data = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"yaml_data","login.yaml")

class ReadFile:
    def __init__(self):
        self.config_data = cofig_data
        self.yaml_data = yaml_data

    def read_ini(self):
        config = configparser.ConfigParser()
        config.read(self.config_data, encoding="utf-8")
        return config

    def read_yaml(self):
        with open(self.yaml_data,mode="r",encoding="utf-8") as f:
            file = yaml.safe_load(f)
        return file


base_data = ReadFile()

if __name__ == '__main__':
    data = base_data.read_ini()["host"]["api_sit_url"]
    # data2 = base_data.read_yaml()["login"]
    print(data)

