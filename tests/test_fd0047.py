import unittest

from cwb.api.ElementName import NextTwoDays, NextOneWeek
from cwb.api.Enum import Format, Sort
from cwb.api.FD0047 import FD0047


class TestFD0047(unittest.TestCase):
    def test_payload_none(self):
        api = FD0047("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB", "001")
        payload = api.test_payload()
        self.assertEqual(None, payload)

    def test_payload(self):
        api = FD0047("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB", "001")
        api.set_limit(2)
        api.set_offset(1)
        api.set_format(Format.xml)
        api.set_location_name("頭城鎮")
        api.add_element_name(NextTwoDays.Wx)
        api.add_element_name(NextTwoDays.Wind)
        api.add_sort(Sort.time)

        payload = api.test_payload()
        print(payload)

    # def test_get_response_no_payload(self):
    #     api = FD0047("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB", "089")
    #     response = api.get_response()
    #     data = response.json()
    #     print(data)

    # def test_get_response_payload(self):
    #     api = FD0047("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB", "001")
    #     api.set_limit(2)
    #     api.set_offset(1)
    #     # api.set_format(Format.xml)
    #     api.set_location_name("頭城鎮")
    #     api.add_element_name(ElementName.Wx)
    #     api.add_element_name(ElementName.Wind)
    #     api.add_sort(Sort.time)
    #
    #     response = api.get_response()
    #     data = response.json()
    #     print(data)

    # # [2].鄉鎮天氣預報 - 單一鄉鎮市區預報資料(未來2天天氣預報)
    # def test_get_data_set_no_payload2(self):
    #     api = FD0047("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB", "001")
    #     api.add_element_name(NextTwoDays.Wx)
    #     api.add_element_name(NextTwoDays.Wind)
    #     data_set = api.get_data_set()
    #     print(data_set)

    # # [3].鄉鎮天氣預報 - 單一鄉鎮市區預報資料(未來1週天氣預報)
    # def test_get_data_set_no_payload3(self):
    #     api = FD0047("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB", "003")
    #     api.add_element_name(NextOneWeek.T)
    #     api.add_element_name(NextOneWeek.RH)
    #     api.add_element_name(NextOneWeek.Wx)
    #     data_set = api.get_data_set()
    #     print(data_set)

    # # [4].鄉鎮天氣預報 - 臺灣未來2天天氣預報
    # def test_get_data_set_no_payload4(self):
    #     api = FD0047("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB", "089")
    #     api.add_element_name(NextTwoDays.Wx)
    #     api.add_element_name(NextTwoDays.PoP)
    #     data_set = api.get_data_set()
    #     print(data_set)

    # # [5].鄉鎮天氣預報-臺灣未來一週天氣預報
    # def test_get_data_set_no_payload5(self):
    #     api = FD0047("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB", "091")
    #     api.add_element_name(NextOneWeek.RH)
    #     api.add_element_name(NextOneWeek.Wx)
    #     data_set = api.get_data_set()
    #     print(data_set)

    # [6].鄉鎮天氣預報 - 全臺灣各鄉鎮市區預報資料
    def test_get_data_set_no_payload6(self):
        api = FD0047("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB", "093")
        api.add_location_id("F-D0047-001")
        api.add_element_name(NextOneWeek.Wx)
        api.add_element_name(NextOneWeek.PoP)
        data_set = api.get_data_set()
        print(data_set)
