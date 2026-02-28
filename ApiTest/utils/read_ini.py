import configparser
import os

path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"config","settings.ini")
def read_ini():
    config = configparser.ConfigParser()
    config.read(path,encoding="utf-8")
    return config

get_ini = read_ini()["host"]["api_sit_url"]

# print(get_ini)