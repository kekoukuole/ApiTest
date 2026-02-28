import os

import yaml

path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"config","data.yaml")
def read_data():
    f = open(path, 'r')
    data = yaml.safe_load(f)
    return data

get_data = read_data()
# print(get_data)