import unittest

from cwb.api.element_name import TodayTomorrowThirtySixHours
from cwb.api.enum import Sort
from cwb.api.fc0032 import FC0032


class TestFC0032(unittest.TestCase):
    def test_payload_none(self):
        api = FC0032("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB")
        payload = api.get_payload()
        self.assertEqual(None, payload)

    def test_payload(self):
        location_name_list = ["宜蘭縣", "花蓮縣"]

        api = FC0032("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB", location_name_list)
        api.set_limit(2)
        api.set_offset(1)
        api.add_element_name(TodayTomorrowThirtySixHours.Wx)
        api.add_element_name(TodayTomorrowThirtySixHours.PoP)
        api.add_sort(Sort.time)

        payload = api.get_payload()
        print(payload)

        # # [1].一般天氣預報 - 今明36小時天氣預報
        # def test_get_data_set_no_payload1(self):
        #     api = FC0032("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB")
        #     data_set = api.get_data_set()
        #     print(api.get_payload())
        #     print(data_set)
        #
        # # [1].一般天氣預報 - 今明36小時天氣預報
        # def test_get_data_set_payload1(self):
        #     api = FC0032("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB")
        #     api.set_limit(99)
        #     api.set_offset(0)
        #     api.add_location_name("宜蘭縣")
        #     api.add_location_name("花蓮縣")
        #     api.add_element_name(TodayTomorrowThirtySixHours.Wx)
        #     api.add_element_name(TodayTomorrowThirtySixHours.PoP)
        #     api.add_sort(Sort.time)
        #     data_set = api.get_data_set()
        #     print(api.get_payload())
        #     print(data_set)
