import unittest

from cwb.api.element_name import OA0017ElementName
from cwb.api.enum import Sort
from cwb.api.oa0017 import OA0017


class TestOA0017(unittest.TestCase):
    def test_payload_none(self):
        api = OA0017("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB")
        payload = api.get_payload()
        self.assertEqual(None, payload)

    def test_payload(self):
        api = OA0017("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB")
        api.set_limit(2)
        api.set_offset(1)
        api.add_station_id("1436")
        api.add_element_name(OA0017ElementName.TidalHeight)
        api.add_sort(Sort.Time)

        payload = api.get_payload()
        print(payload)

    # [7]. 即時海況-潮位-沿岸潮位站監測資料
    def test_get_data_set_no_payload7(self):
        api = OA0017("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB")
        data_set = api.get_data_set()
        print(data_set)
