import unittest

from cwb.api.element_name import FA0021ElementName
from cwb.api.enum import FA0021Sort
from cwb.api.fa0021 import FA0021


class TestFA0021(unittest.TestCase):
    def test_payload_none(self):
        api = FA0021("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB")
        payload = api.get_payload()
        self.assertEqual(None, payload)

    def test_payload(self):
        location_name_list = ["海水浴場南灣"]
        api = FA0021("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB", location_name_list=location_name_list)
        api.set_limit(2)
        api.set_offset(1)
        api.add_element_name(FA0021ElementName.LunarCalendar)
        api.add_sort(FA0021Sort.ValidTime)
        api.add_sort(FA0021Sort.DataTime)

        payload = api.get_payload()
        print(payload)

    # [10]. 潮汐預報-未來1 個月潮汐預報
    def test_get_data_set_no_payload7(self):
        api = FA0021("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB")
        # api.set_limit(17)
        data_set = api.get_data_set()
        print(data_set)
