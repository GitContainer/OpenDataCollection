import unittest

from cwb.api.element_name import NextTwoDays, NextOneWeek
from cwb.api.enum import Sort
from cwb.api.fd0047 import FD0047


class TestFD0047(unittest.TestCase):
    def test_payload_none(self):
        api = FD0047("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB", "001")
        payload = api.get_payload()
        self.assertEqual(None, payload)

    def test_payload(self):
        location_name = "頭城鎮"

        api = FD0047("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB", "001", location_name=location_name)
        api.set_limit(2)
        api.set_offset(1)
        api.add_element_name(NextTwoDays.Wx)
        api.add_element_name(NextTwoDays.Wind)
        api.add_sort(Sort.Time)

        payload = api.get_payload()
        print(payload)

    # [2].鄉鎮天氣預報 - 單一鄉鎮市區預報資料(未來2天天氣預報)
    def test_get_data_set_no_payload2(self):
        api = FD0047("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB", "001", location_name="頭城鎮")
        # api.add_element_name(NextTwoDays.Wx)
        # api.add_element_name(NextTwoDays.Wind)
        data_set = api.get_data_set()
        print(data_set)

    # # [3].鄉鎮天氣預報 - 單一鄉鎮市區預報資料(未來1週天氣預報)
    # def test_get_data_set_no_payload3(self):
    #     location_name_list = ["頭城鎮"]
    #     api = FD0047("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB", "003", location_name_list=location_name_list)
    #     api.add_element_name(NextOneWeek.T)
    #     api.add_element_name(NextOneWeek.RH)
    #     api.add_element_name(NextOneWeek.Wx)
    #     data_set = api.get_data_set()
    #     print(data_set)

    # # [4].鄉鎮天氣預報 - 臺灣未來2天天氣預報
    # def test_get_data_set_no_payload4(self):
    #     location_name_list = ["宜蘭縣", "花蓮縣"]
    #     api = FD0047("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB", "089", location_name_list=location_name_list)
    #     api.add_element_name(NextTwoDays.Wx)
    #     api.add_element_name(NextTwoDays.PoP)
    #     data_set = api.get_data_set()
    #     print(data_set)

    # # [5].鄉鎮天氣預報-臺灣未來一週天氣預報
    # def test_get_data_set_no_payload5(self):
    #     location_name_list = ["宜蘭縣", "花蓮縣"]
    #     api = FD0047("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB", "091", location_name_list=location_name_list)
    #     api.add_element_name(NextOneWeek.RH)
    #     api.add_element_name(NextOneWeek.Wx)
    #     data_set = api.get_data_set()
    #     print(data_set)

    # # [6].鄉鎮天氣預報 - 全臺灣各鄉鎮市區預報資料
    # def test_get_data_set_no_payload6(self):
    #     location_name_list = ["頭城鎮"]
    #     api = FD0047("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB", "093", location_name_list=location_name_list)
    #     api.add_location_id("F-D0047-001")
    #     api.add_element_name(NextOneWeek.Wx)
    #     api.add_element_name(NextOneWeek.PoP)
    #     data_set = api.get_data_set()
    #     print(data_set)
