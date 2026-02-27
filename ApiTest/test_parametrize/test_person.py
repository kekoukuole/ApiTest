import pytest

from utils.read_data import get_data
from utils.yaml_util import func_yaml


def test_person():
    data = get_data["person"]
    print(func_yaml(data))

@pytest.mark.parametrize("data",get_data["person2"])
def test_person_2(data):
    print(func_yaml(data))