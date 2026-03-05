import configparser
import os
import yaml

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"data","data.yaml")
ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"config","settings.ini")
file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"file","photo_2024-03-29_16-20-33.jpg")

class Fileread:
    def __init__(self):
        self.data_path = data_path
        self.ini_path = ini_path
        self.file_path = file_path

    def read_data(self):
        f = open(self.data_path, 'r',encoding="utf-8")
        data = yaml.safe_load(f)
        return data


    def read_ini(self):
        config = configparser.ConfigParser()
        config.read(self.ini_path,encoding="utf-8")
        return config

    def read_file(self):
        file = open(self.file_path,'rb')
        return {"file":("photo_2024-03-29_16-20-33.jpg",file,"image/jpeg")}

base_data = Fileread()