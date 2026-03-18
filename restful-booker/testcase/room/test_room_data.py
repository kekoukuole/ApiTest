import pytest

from core.Apiservice import Apiservice
from read.read_file import base_data

class TestRoomData:

    @pytest.mark.parametrize("data", base_data.read_yaml("room.yaml","all_room_information"))
    def test_all_roomdata(self,data):
        Apiservice().handle_case(data)